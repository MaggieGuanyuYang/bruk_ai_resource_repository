#!/usr/bin/env python3
"""Build the BR-UK AI Tools site from YAML/markdown sources in content/.

Each YAML in `content/` produces one HTML file at the project root. Page IDs
are derived from the output path (e.g. `section-1/literature-review.html` →
`section-1.literature-review`); cross-page links use these IDs and the build
resolves them to a relative path from the current page.

Run:
    pip install -r build-requirements.txt
    python3 build.py
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass, field
from html import escape as html_escape
from pathlib import Path

import yaml
from jinja2 import Environment, FileSystemLoader, Undefined
import markdown as md_lib


_AMP_NOT_ENTITY = re.compile(r"&(?!#?\w+;)")


def safe_amp(s):
    """Escape a bare `&` to `&amp;` without double-escaping existing entities.

    Short-label YAML fields can contain raw HTML (e.g. `<em>foo</em>`) and
    sometimes contain `&` characters that should appear in the document as
    `&amp;`. Applying this helper means authors can write either form.
    """
    if s is None:
        return ""
    return _AMP_NOT_ENTITY.sub("&amp;", str(s))

ROOT = Path(__file__).resolve().parent
CONTENT_DIR = ROOT / "content"
TEMPLATES_DIR = ROOT / "templates"
SITE_FILE = CONTENT_DIR / "_site.yml"


# ---------------------------------------------------------------------------
# Page registry
# ---------------------------------------------------------------------------

@dataclass
class Page:
    page_id: str            # e.g. "section-1.literature-review"
    source: Path            # YAML source path
    output: Path            # output path relative to ROOT
    section: str            # top-level section id ("home", "section-1", "about", ...)
    data: dict = field(default_factory=dict)

    @property
    def depth(self) -> int:
        rel = self.output.relative_to(ROOT)
        return len(rel.parts) - 1

    @property
    def prefix(self) -> str:
        return "../" * self.depth


def discover_pages() -> dict[str, Page]:
    pages: dict[str, Page] = {}
    for src in sorted(CONTENT_DIR.rglob("*.yml")):
        rel = src.relative_to(CONTENT_DIR)
        if rel.name.startswith("_") and rel.name != "_index.yml":
            continue
        if rel.name == "_index.yml":
            out_rel = rel.parent / "index.html"
            page_id = rel.parent.as_posix().replace("/", ".")
            section = rel.parts[0]
        elif rel.name == "home.yml":
            out_rel = Path("index.html")
            page_id = "home"
            section = "home"
        else:
            out_rel = rel.with_suffix(".html")
            page_id = rel.with_suffix("").as_posix().replace("/", ".")
            section = rel.parts[0] if len(rel.parts) > 1 else page_id
        pages[page_id] = Page(
            page_id=page_id,
            source=src,
            output=ROOT / out_rel,
            section=section,
        )
    return pages


# ---------------------------------------------------------------------------
# Reference resolution
# ---------------------------------------------------------------------------

def ref_to_relative(ref: str, current: Page, pages: dict[str, Page]) -> str:
    if ref not in pages:
        raise KeyError(f"Unknown page ref: {ref!r} (from {current.page_id}). Known: {sorted(pages)}")
    target = pages[ref].output.relative_to(ROOT)
    cur_dir = current.output.relative_to(ROOT).parent
    rel = os.path.relpath(target, cur_dir)
    return Path(rel).as_posix()


# ---------------------------------------------------------------------------
# Markdown
# ---------------------------------------------------------------------------

def render_markdown(text: str | None) -> str:
    if not text:
        return ""
    return md_lib.markdown(text.rstrip(), extensions=["attr_list"])


def strip_p_wrapper(html: str) -> str:
    """Markdown wraps a single paragraph in <p>...</p>; strip when undesired."""
    s = html.strip()
    if s.startswith("<p>") and s.endswith("</p>") and "<p>" not in s[3:-4]:
        return s[3:-4]
    return s


def indent_lines(s: str, n: int) -> str:
    pad = " " * n
    return "\n".join(pad + line if line else line for line in s.splitlines())


# ---------------------------------------------------------------------------
# Block rendering
# ---------------------------------------------------------------------------

def render_blocks(blocks, current, pages, indent=8):
    """Render a list of blocks (each block is a single-key dict) at given indent."""
    out = []
    for block in blocks or []:
        kind, payload = _extract_block(block)
        renderer = _BLOCK_RENDERERS.get(kind)
        if renderer is None:
            raise ValueError(f"Unknown block kind {kind!r} on page {current.page_id}")
        try:
            rendered = renderer(payload, current, pages, indent)
        except KeyError as e:
            raise KeyError(
                f"Missing required key {e!s} in {kind!r} block on page {current.page_id} "
                f"(source: {current.source.relative_to(ROOT)})"
            ) from e
        if rendered:
            out.append(rendered)
    return "\n".join(out)


def _extract_block(block):
    if not isinstance(block, dict):
        raise ValueError(f"Block must be a mapping, got: {block!r}")
    if len(block) == 1:
        ((kind, payload),) = block.items()
        return kind, payload
    if "kind" in block:
        kind = block["kind"]
        payload = {k: v for k, v in block.items() if k != "kind"}
        return kind, payload
    raise ValueError(f"Block must have a single key or `kind` field, got keys: {list(block)}")


# ---- individual block renderers ------------------------------------------

def _r_prose(payload, current, pages, indent):
    inner = render_blocks(payload, current, pages, indent=indent + 2)
    pad = " " * indent
    return f"{pad}<div class=\"prose\">\n{inner}\n{pad}</div>"


def _r_markdown(payload, current, pages, indent):
    text = payload if isinstance(payload, str) else payload.get("body", "")
    html = render_markdown(text)
    return indent_lines(html, indent) if html else ""


def _r_lede(payload, current, pages, indent):
    if isinstance(payload, str):
        text = payload
        font_size = "1.1rem"
        color = "var(--ink-700)"
    else:
        text = payload.get("text", "")
        font_size = payload.get("font_size", "1.1rem")
        color = payload.get("color", "var(--ink-700)")
    style = f"font-size:{font_size}; color: {color};"
    pad = " " * indent
    body_indent = " " * (indent + 2)
    # Collapse internal whitespace before markdown render so the output is one
    # logical line, then re-indent.
    flat = " ".join(text.split())
    md_html = render_markdown(flat)
    body = strip_p_wrapper(md_html)
    return f"{pad}<p class=\"hero__lede\" style=\"{style}\">\n{body_indent}{body}\n{pad}</p>"


def _r_paragraph(payload, current, pages, indent):
    """A single styled <p>. Used for the home page's intro paragraph."""
    if isinstance(payload, str):
        text, classes, style = payload, None, None
    else:
        text = payload.get("text", "")
        classes = payload.get("classes")
        style = payload.get("style")
    attrs = ""
    if classes:
        attrs += f' class="{classes}"'
    if style:
        attrs += f' style="{style}"'
    body = " ".join(text.split())
    pad = " " * indent
    return f"{pad}<p{attrs}>\n{pad}  {body}\n{pad}</p>"


def _r_heading(level, payload, current, pages, indent):
    if isinstance(payload, str):
        text, ident, classes = payload, None, None
    else:
        text = payload.get("text", "")
        ident = payload.get("id")
        classes = payload.get("classes")
    attrs = ""
    if classes:
        attrs += f' class="{classes}"'
    if ident:
        attrs += f' id="{ident}"'
    pad = " " * indent
    return f"{pad}<h{level}{attrs}>{safe_amp(text)}</h{level}>"


def _r_quicknav(payload, current, pages, indent):
    heading = payload.get("heading", "On this page")
    items = []
    for it in payload["items"]:
        if "ref" in it:
            href = ref_to_relative(it["ref"], current, pages)
            if it.get("anchor"):
                href = f"{href}#{it['anchor']}"
        else:
            href = it["href"]
        items.append((href, it["label"]))
    pad = " " * indent
    lines = [f"{pad}<div class=\"quicknav\">",
             f"{pad}  <h4>{html_escape(heading)}</h4>",
             f"{pad}  <ul>"]
    for href, label in items:
        lines.append(f'{pad}    <li><a href="{href}">{label}</a></li>')
    lines += [f"{pad}  </ul>", f"{pad}</div>"]
    return "\n".join(lines)


def _r_tool_grid(payload, current, pages, indent):
    pad = " " * indent
    lines = [f"{pad}<div class=\"tool-grid\">"]
    for t in payload:
        if "name" not in t or "desc" not in t:
            raise KeyError(
                f"tool_grid item is missing 'name' or 'desc' on page {current.page_id}: {t!r}"
            )
        name_html = safe_amp(t["name"])
        if t.get("url"):
            name_html = f'<a href="{t["url"]}">{name_html}</a>'
        if t.get("tag"):
            name_html = f'{name_html} <span class="tool-card__tag">{safe_amp(t["tag"])}</span>'
        desc_html = strip_p_wrapper(render_markdown(" ".join(t["desc"].split())))
        lines.append(f"{pad}  <div class=\"tool-card\">")
        lines.append(f"{pad}    <h3 class=\"tool-card__name\">{name_html}</h3>")
        lines.append(f"{pad}    <p class=\"tool-card__desc\">{desc_html}</p>")
        if t.get("link_url"):
            lines.append(f'{pad}    <a class="tool-card__link" href="{t["link_url"]}">{safe_amp(t.get("link_text", ""))}</a>')
        lines.append(f"{pad}  </div>")
    lines.append(f"{pad}</div>")
    return "\n".join(lines)


def _r_subpage_list(payload, current, pages, indent):
    if isinstance(payload, list):
        items = payload
        style = None
    else:
        items = payload.get("items", [])
        style = payload.get("style")
    pad = " " * indent
    # When `style` requests a grid display, the original markup uses <div>, not <ul>
    is_div = bool(style and "display: grid" in style)
    open_tag = f'{pad}<{"div" if is_div else "ul"} class="subpage-list"'
    if style:
        open_tag += f' style="{style}"'
    open_tag += ">"
    lines = [open_tag]
    inner_pad = "  " if is_div else "    "
    for it in items:
        url = ref_to_relative(it["ref"], current, pages) if "ref" in it else it["href"]
        title_html = safe_amp(it["title"])
        if not is_div:
            lines.append(f"{pad}  <li>")
        lines.append(f"{pad}{inner_pad}<a href=\"{url}\">")
        lines.append(f"{pad}{inner_pad}  {title_html}")
        if it.get("blurb"):
            blurb_html = safe_amp(" ".join(it["blurb"].split()))
            lines.append(f"{pad}{inner_pad}  <span>{blurb_html}</span>")
        lines.append(f"{pad}{inner_pad}</a>")
        if it.get("children"):
            lines.append(f"{pad}    <ul class=\"subpage-nested\">")
            for c in it["children"]:
                child_url = ref_to_relative(c["ref"], current, pages) if "ref" in c else c["href"]
                lines.append(f'{pad}      <li><a href="{child_url}">{safe_amp(c["label"])}</a></li>')
            lines.append(f"{pad}    </ul>")
        if not is_div:
            lines.append(f"{pad}  </li>")
    lines.append(f"{pad}</{'div' if is_div else 'ul'}>")
    return "\n".join(lines)


def _r_callout(payload, current, pages, indent):
    classes = "callout"
    kind = payload.get("kind")
    if kind:
        classes += f" callout--{kind}"
    pad = " " * indent
    lines = [f"{pad}<div class=\"{classes}\">"]
    if payload.get("heading"):
        lines.append(f"{pad}  <h4>{safe_amp(payload['heading'])}</h4>")
    body = render_markdown(payload.get("body", ""))
    if body:
        body_indented = indent_lines(body, indent + 2)
        lines.append(body_indented)
    if payload.get("body_blocks"):
        lines.append(render_blocks(payload["body_blocks"], current, pages, indent=indent + 2))
    lines.append(f"{pad}</div>")
    return "\n".join(lines)


def _r_blockquote(payload, current, pages, indent):
    if isinstance(payload, str):
        body = payload
        cite = None
    else:
        body = payload.get("body", "")
        cite = payload.get("cite")
    body_html = render_markdown(body)
    pad = " " * indent
    lines = [f"{pad}<blockquote>"]
    if body_html:
        lines.append(indent_lines(body_html, indent + 2))
    if cite:
        cite_html = strip_p_wrapper(render_markdown(cite))
        lines.append(f"{pad}  <cite>{cite_html}</cite>")
    lines.append(f"{pad}</blockquote>")
    return "\n".join(lines)


def _r_references(payload, current, pages, indent):
    pad = " " * indent
    div_attrs = ' class="references"'
    if payload.get("id"):
        div_attrs += f' id="{payload["id"]}"'
    heading = payload.get("heading", "References")
    heading_level = payload.get("heading_level", "h3")
    lines = [f"{pad}<div{div_attrs}>",
             f"{pad}  <{heading_level}>{html_escape(heading)}</{heading_level}>",
             f"{pad}  <ol>"]
    for it in payload["items"]:
        rendered = strip_p_wrapper(render_markdown(it))
        lines.append(f"{pad}    <li>{rendered}</li>")
    lines += [f"{pad}  </ol>", f"{pad}</div>"]
    return "\n".join(lines)


def _r_data_table(payload, current, pages, indent):
    pad = " " * indent
    lines = [f"{pad}<table class=\"data-table\">", f"{pad}  <thead>"]
    headers = "".join(f"<th>{strip_p_wrapper(render_markdown(h))}</th>" for h in payload["headers"])
    lines.append(f"{pad}    <tr>{headers}</tr>")
    lines.append(f"{pad}  </thead>")
    lines.append(f"{pad}  <tbody>")
    for row in payload["rows"]:
        cells = "".join(f"<td>{strip_p_wrapper(render_markdown(c))}</td>" for c in row)
        lines.append(f"{pad}    <tr>{cells}</tr>")
    lines.append(f"{pad}  </tbody>")
    lines.append(f"{pad}</table>")
    return "\n".join(lines)


def _r_breadcrumb(payload, current, pages, indent):
    pad = " " * indent
    lines = [f'{pad}<nav class="breadcrumb" aria-label="Breadcrumb">']
    items = payload if isinstance(payload, list) else payload.get("items", [])
    for i, it in enumerate(items):
        is_last = i == len(items) - 1
        label = safe_amp(it["label"])
        if is_last and not it.get("href") and not it.get("ref"):
            lines.append(f'{pad}  <span class="breadcrumb__current">{label}</span>')
        else:
            href = ref_to_relative(it["ref"], current, pages) if "ref" in it else it["href"]
            lines.append(f'{pad}  <a href="{href}">{label}</a>')
        if not is_last:
            lines.append(f'{pad}  <span class="breadcrumb__sep">/</span>')
    lines.append(f"{pad}</nav>")
    return "\n".join(lines)


def _r_pager(payload, current, pages, indent):
    pad = " " * indent

    def link(item, cls):
        href = ref_to_relative(item["ref"], current, pages) if "ref" in item else item["href"]
        return [
            f'{pad}  <a class="{cls}" href="{href}">',
            f'{pad}    <div class="pager__label">{safe_amp(item["label"])}</div>',
            f'{pad}    <div class="pager__title">{safe_amp(item["title"])}</div>',
            f'{pad}  </a>',
        ]

    lines = [f'{pad}<nav class="pager" aria-label="Page navigation">']
    if payload.get("prev"):
        lines += link(payload["prev"], "pager__prev")
    if payload.get("next"):
        lines += link(payload["next"], "pager__next")
    lines.append(f'{pad}</nav>')
    return "\n".join(lines)


def _r_section_badge(payload, current, pages, indent):
    pad = " " * indent
    return f'{pad}<span class="section-badge">{safe_amp(payload)}</span>'


def _r_h1(payload, current, pages, indent):
    pad = " " * indent
    return f"{pad}<h1>{safe_amp(payload)}</h1>"


def _r_raw(payload, current, pages, indent):
    text = payload if isinstance(payload, str) else payload.get("html", "")
    return indent_lines(text, indent) if indent else text


_BLOCK_RENDERERS = {
    "prose": _r_prose,
    "markdown": _r_markdown,
    "lede": _r_lede,
    "paragraph": _r_paragraph,
    "h1": _r_h1,
    "h2": lambda p, c, pg, i: _r_heading(2, p, c, pg, i),
    "h3": lambda p, c, pg, i: _r_heading(3, p, c, pg, i),
    "h4": lambda p, c, pg, i: _r_heading(4, p, c, pg, i),
    "quicknav": _r_quicknav,
    "tool_grid": _r_tool_grid,
    "subpage_list": _r_subpage_list,
    "callout": _r_callout,
    "blockquote": _r_blockquote,
    "references": _r_references,
    "data_table": _r_data_table,
    "breadcrumb": _r_breadcrumb,
    "pager": _r_pager,
    "section_badge": _r_section_badge,
    "raw": _r_raw,
}


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------

def load_yaml(path: Path) -> dict:
    with path.open(encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def build(verbose: bool = True, check: bool = False, only: str | None = None) -> int:
    """Render every YAML in `content/` to HTML.

    Args:
      verbose: print one line per page written.
      check:   dry-run mode. Don't write anything; return non-zero if any
               output would change. Use as a CI / pre-commit gate to catch
               hand-edited HTML or stale generated files.
      only:    if set, build only the page with this id (e.g. "section-1.literature-review").
    """
    if not SITE_FILE.exists():
        sys.exit(f"Missing {SITE_FILE}")
    site = load_yaml(SITE_FILE)
    pages = discover_pages()
    if only is not None and only not in pages:
        sys.exit(f"Unknown page id {only!r}. Known ids: {', '.join(sorted(pages))}")

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=False,
        undefined=Undefined,
        keep_trailing_newline=True,
    )
    env.filters["e"] = lambda s: html_escape(str(s) if s is not None else "")
    env.filters["safe_amp"] = safe_amp

    written = 0
    drift = 0
    for page in pages.values():
        if only is not None and page.page_id != only:
            continue
        page.data = load_yaml(page.source)
        template_name = page.data.get("template", _default_template(page))
        template = env.get_template(template_name)

        def link_for(ref: str, _current=page) -> str:
            return ref_to_relative(ref, _current, pages)

        def render_block_list(blocks, indent=8, _current=page):
            return render_blocks(blocks, _current, pages, indent=indent)

        ctx = {
            "page": page,
            "data": page.data,
            "site": site,
            "prefix": page.prefix,
            "link_for": link_for,
            "render_blocks": render_block_list,
            "section_id": _nav_match_for(page),
            "page_id": page.page_id,
            "content_dir": CONTENT_DIR,
        }
        html = template.render(**ctx)
        if not html.endswith("\n"):
            html += "\n"
        rel_out = page.output.relative_to(ROOT)
        prev_bytes = page.output.read_bytes() if page.output.exists() else None
        new_bytes = html.encode("utf-8")
        changed = prev_bytes != new_bytes
        if check:
            if changed:
                drift += 1
                if verbose:
                    print(f"  DRIFT  {page.page_id:38s} → {rel_out}")
            else:
                if verbose:
                    print(f"  ok     {page.page_id:38s} → {rel_out}")
        else:
            page.output.parent.mkdir(parents=True, exist_ok=True)
            page.output.write_text(html, encoding="utf-8")
            if verbose:
                tag = "WRITE" if changed else "no-op"
                print(f"  {tag}  {page.page_id:38s} → {rel_out}")
        written += 1

    if check:
        if drift:
            if verbose:
                print(f"\n{drift} page(s) would change. Run `python3 build.py` and commit the result.")
            return 1
        if verbose:
            print(f"\nAll {written} page(s) up to date.")
        return 0
    if verbose:
        print(f"\nBuilt {written} page(s).")
    return 0


def _nav_match_for(page: Page) -> str:
    """The nav 'match' value for is-active highlighting.

    Top-level pages match their own id; sub-pages match the section id.
    """
    if page.page_id == "home":
        return "home"
    if "." in page.page_id:
        return page.page_id.split(".", 1)[0]
    return page.page_id


def _default_template(page: Page) -> str:
    if page.page_id == "home":
        return "home.html"
    return "page.html"


def main():
    ap = argparse.ArgumentParser(
        description="Build the BR-UK AI Tools site from YAML/markdown sources.",
        epilog="Without --check, regenerates every *.html file. Always commit "
               "the regenerated files alongside the YAML edits that produced them.",
    )
    ap.add_argument("page_id", nargs="?", help="restrict build to one page id (e.g. 'section-1.literature-review')")
    ap.add_argument("-q", "--quiet", action="store_true", help="suppress per-page log lines")
    ap.add_argument("--check", action="store_true",
                    help="dry-run: exit non-zero if any output would change. Use as a CI / pre-commit gate.")
    args = ap.parse_args()
    return build(verbose=not args.quiet, check=args.check, only=args.page_id)


if __name__ == "__main__":
    sys.exit(main())
