# Site Structure

This document maps every page, every named section on each page, and the source
file that controls each piece of content. Use it together with
[REVISION-TEMPLATE.md](REVISION-TEMPLATE.md) when requesting monthly updates.

## How the site is built

Source files live under `content/` (YAML, with markdown for prose). Templates
live under `templates/`. The build script `build.py` reads the YAML, renders
the templates, and writes the published `*.html` files at the project root —
the same paths GitHub Pages already serves.

```
content/         ← edit this to change content
templates/       ← edit this to change layout/chrome
build.py         ← run this to regenerate HTML
*.html           ← generated; safe to overwrite via build.py
```

To rebuild after editing:

```bash
pip install -r build-requirements.txt   # one-time setup
python3 build.py                        # regenerate all 19 HTML files
python3 build.py home                   # rebuild a single page (by page id)
python3 build.py --check                # dry-run; exits non-zero if any
                                        #   output would change (CI gate)
```

The generated HTML files **are committed to the repo** — GitHub Pages serves
them directly. Every generated file starts with a `<!-- GENERATED FILE — DO
NOT EDIT -->` comment naming its YAML source. Always commit both the YAML
you edited *and* the regenerated HTML in the same commit; running
`python3 build.py --check` before committing will catch you if you forget.

## Cross-page links use page IDs

Inside the YAML, links to other pages on the site use a **page ID** (e.g.
`section-1.literature-review`) instead of a relative URL. The build resolves
each ID to a relative path from the page being rendered, so reorganising
files won't silently break links. The full list of page IDs is the second
column of the page index below.

## Global configuration — `content/_site.yml`

Edits to this file affect every page. It controls:

| Element                                              | YAML key                                |
| ---------------------------------------------------- | --------------------------------------- |
| Logo image, brand name, tagline                      | `brand`                                 |
| Top navigation bar (links, labels, active highlight) | `nav`                                   |
| Footer "About BR-UK" paragraph (default)             | `footer.about`                          |
| Footer "Sections" link list                          | `footer.sections`                       |
| Footer "Get in touch" link list (default)            | `footer.contact`                        |
| Footer copyright line                                | `footer.copyright`                      |
| Footer "Last content review YYYY" line               | `footer.status`                         |
| Stylesheet, favicon, JS, font URL                    | `stylesheet`, `favicon`, `script`, `fonts` |

The home page overrides `footer.about` and `footer.contact` (it has fuller
text and an extra "Privacy Statement" link). To make the same change on every
page, edit `_site.yml`. To change just the home page, edit `content/home.yml`'s
`footer_about` / `footer_contact` keys.

## Page index

Every page in the published site is generated from exactly one YAML file. The
table below lists each page's published URL, its page ID, the YAML source, and
which template renders it.

| #   | Published URL                          | Page ID                            | Source YAML                                | Template            |
| --- | -------------------------------------- | ---------------------------------- | ------------------------------------------ | ------------------- |
| 1   | `/index.html` (home)                   | `home`                             | `content/home.yml`                         | `home.html`         |
| 2   | `/about.html`                          | `about`                            | `content/about.yml`                        | `page.html`         |
| 3   | `/section-1/index.html`                | `section-1`                        | `content/section-1/_index.yml`             | `page.html`         |
| 4   | `/section-1/literature-review.html`    | `section-1.literature-review`      | `content/section-1/literature-review.yml`  | `page.html`         |
| 5   | `/section-1/hypothesis-generation.html`| `section-1.hypothesis-generation`  | `content/section-1/hypothesis-generation.yml` | `page.html`      |
| 6   | `/section-1/data-collection.html`      | `section-1.data-collection`        | `content/section-1/data-collection.yml`    | `page.html`         |
| 7   | `/section-1/data-analysis.html`        | `section-1.data-analysis`          | `content/section-1/data-analysis.yml`      | `page.html`         |
| 8   | `/section-1/writing-reporting.html`    | `section-1.writing-reporting`      | `content/section-1/writing-reporting.yml`  | `page.html`         |
| 9   | `/section-2/index.html`                | `section-2`                        | `content/section-2/_index.yml`             | `page.html`         |
| 10  | `/section-2/disclosure.html`           | `section-2.disclosure`             | `content/section-2/disclosure.yml`         | `page.html`         |
| 11  | `/section-2/publishers.html`           | `section-2.publishers`             | `content/section-2/publishers.yml`         | `page.html`         |
| 12  | `/section-2/uk-funders.html`           | `section-2.uk-funders`             | `content/section-2/uk-funders.yml`         | `page.html`         |
| 13  | `/section-2/biases.html`               | `section-2.biases`                 | `content/section-2/biases.yml`             | `page.html`         |
| 14  | `/section-2/privacy.html`              | `section-2.privacy`                | `content/section-2/privacy.yml`            | `page.html`         |
| 15  | `/section-2/sustainability.html`       | `section-2.sustainability`         | `content/section-2/sustainability.yml`     | `page.html`         |
| 16  | `/section-2/key-regulations.html`      | `section-2.key-regulations`        | `content/section-2/key-regulations.yml`    | `page.html`         |
| 17  | `/section-3.html`                      | `section-3`                        | `content/section-3.yml`                    | `page.html`         |
| 18  | `/section-4.html`                      | `section-4`                        | `content/section-4.yml`                    | `page.html`         |
| 19  | `/section-5.html`                      | `section-5`                        | `content/section-5.yml`                    | `page.html`         |

## Per-page section map

Each entry below names every meaningful section on a page, the YAML key (or
sub-block path) that controls it, and the in-page anchor where applicable.

### 1. Home — `content/home.yml`
| Section                               | YAML path                  | Anchor      |
| ------------------------------------- | -------------------------- | ----------- |
| Page title (browser tab)              | `title`                    | —           |
| SEO description                       | `description`              | —           |
| Footer "About BR-UK" override         | `footer_about`             | —           |
| Footer "Get in touch" override        | `footer_contact`           | —           |
| Hero eyebrow line                     | `hero.eyebrow`             | —           |
| Hero H1 headline                      | `hero.heading`             | —           |
| Hero lede paragraph                   | `hero.lede`                | —           |
| Hero CTAs (primary / ghost)           | `hero.actions`             | —           |
| "Explore the repository" heading      | `explore.heading`          | `#sections` |
| "Explore the repository" intro        | `explore.intro`            | —           |
| Six section cards (Section 1–5, About)| `section_cards[]`          | —           |
| Three audience tiles (with SVG icons) | `audience[]`               | —           |
| "What this is — and isn't" heading    | `what.heading`             | —           |
| "What this is — and isn't" body       | `what.paragraphs[]`        | —           |

### 2. About / BR-UK Statement — `content/about.yml`
| Section                                | YAML path                                       |
| -------------------------------------- | ----------------------------------------------- |
| Page title, description                | `title`, `description`                          |
| Breadcrumb crumbs                      | `breadcrumb[]`                                  |
| Section badge ("Living document…")     | `badge`                                         |
| H1                                     | `heading`                                       |
| Italicised subtitle H2                 | `h2_alt.text`                                   |
| Lede paragraph                         | `body[0].prose[0].lede`                         |
| "Stay informed" section                | `body[0].prose` blocks 1–3 (h2 + markdown)      |
| "About BR-UK" section                  | `body[0].prose` blocks 4–5 (h2 + markdown)      |
| "External behavioural-AI resources"    | `body[0].prose` blocks 6–7 (h2 + markdown)      |
| Pager (prev / next)                    | `pager.prev`, `pager.next`                      |

### 3. Section 1 (Living Guide) overview — `content/section-1/_index.yml`
| Section                                       | YAML path               |
| --------------------------------------------- | ----------------------- |
| Title, description, breadcrumb, badge, H1     | top-level keys          |
| Lede paragraph                                | `body[0].prose[0].lede` |
| "Jump to a stage of your research" intro      | `body[0].prose` blocks  |
| Five sub-page cards (Stage 1–5)               | `body[1].subpage_list`  |
| "A note on role" callout                      | `body[2].callout`       |
| "Selected references for this section"        | `body[3].references`    |
| Pager                                         | `pager`                 |

### 4–8. Section 1 sub-pages (one yml per stage)
Each follows the same shape:

| Section            | YAML path                                                                  |
| ------------------ | -------------------------------------------------------------------------- |
| Title              | `title`                                                                    |
| SEO description    | `description`                                                              |
| Breadcrumb         | `breadcrumb[]`                                                             |
| Badge ("Stage N")  | `badge`                                                                    |
| H1                 | `heading`                                                                  |
| Hero lede          | `body[0].prose[0].lede`                                                    |
| On-this-page nav   | `body[0].prose[…].quicknav.items[]`                                         |
| H2/H3 headings     | `body[0].prose[…].h2`, `h3` (each takes `id` + `text`)                     |
| Prose paragraphs   | `body[0].prose[…].markdown` (markdown — links via `[text](url)`)           |
| Tool grids         | `body[0].prose[…].tool_grid[]` — items have `name`, `url`, `tag`, `desc`, optional `link_url`, `link_text` |
| Blockquote (cite)  | `body[0].prose[…].blockquote.body`                                          |
| Callouts           | `body[0].prose[…].callout` — optional `kind` (`caution`, `warning`), `heading`, `body` |
| References block   | `body[0].prose[…].references.items[]`                                       |
| Pager              | `pager.prev`, `pager.next`                                                  |

The five Section 1 sub-pages and their distinguishing on-page anchors:

- **Literature Review** (`literature-review.yml`): `#what-ai-helps-with`, `#tools`, `#further-reading`, `#systematic`, `#case-studies`, `#evidence-synthesis`
- **Hypothesis Generation** (`hypothesis-generation.yml`): `#help`, `#tools`, `#refining`, `#designing`, `#methods`, `#intervention-content`, `#past-data`, `#further`
- **Data Collection** (`data-collection.yml`): `#help`, `#tools`, `#chatbots-qual`, `#interventions`, `#synthetic`
- **Data Analysis** (`data-analysis.yml`): `#tools`, `#quantitative`, `#qualitative`, `#references`
- **Writing & Reporting** (`writing-reporting.yml`): `#writing`, `#caution`, `#publication`, `#presentation`, `#citations`, `#further`

> **How to find a specific block in a sub-page YAML:** open the file and
> search (Cmd-F / Ctrl-F) for either the anchor id (e.g. `id: "tools"`) or
> the heading text (e.g. `text: "Tools"`). The block you're looking for is
> the next one that follows. Each anchor matches a `h2` block; the prose,
> tool grid, callout, or references that *belong* to that section appear
> as siblings immediately under it in the same `body[0].prose[…]` list.

### 9. Section 2 (Ethics) overview — `content/section-2/_index.yml`
| Section                                              | YAML path                          |
| ---------------------------------------------------- | ---------------------------------- |
| Title, description, breadcrumb, badge, H1            | top-level keys                     |
| Lede paragraph                                       | `body[0].prose[0].lede`            |
| "Jump to a topic" heading                            | `body[0].prose[1].h2`              |
| Five topic cards + nested children under "Disclosure"| `body[1].subpage_list[]` (Disclosure has `children[]` for Publishers + UK Funders) |
| "Three questions to ask…" + ordered list             | `body[2].prose[…]`                 |
| "Recommended starting reads" + bullet list           | `body[2].prose[…]`                 |
| Pager                                                | `pager`                            |

### 10. Disclosure & Transparency — `content/section-2/disclosure.yml`
Standard sub-page shape, plus a special grid-styled link block to the
nested Publishers + Funders pages:

- Inline grid of 2 sub-page cards: `body[0].prose[…].subpage_list` with `style:` containing `display: grid …`.
- Eight numbered sub-headings ("1. AI cannot be an author", …, "7. Always check specific guidelines"): each is a `h3` block.
- Elsevier disclosure template: `blockquote`.
- "Planning a submission?" callout: `callout`.

### 11. What publishers said about AI use — `content/section-2/publishers.yml`
- Three-level breadcrumb (Home / Section 2 / Disclosure / current).
- Quicknav with 11 anchors (one per publisher).
- Eleven `h2` sections (`#nature`, `#elsevier`, `#tf`, `#sage`, `#wiley`, `#apa`, `#frontiers`, `#cambridge`, `#pnas`, `#mdpi`, `#cell`), each with sub-headings and bullet lists.

### 12. What UK funders said about AI use — `content/section-2/uk-funders.yml`
- Three-level breadcrumb.
- Joint funder statement: 6 markdown paragraphs.
- "Links to funders" with two inline links.
- Three sub-lists ("Current members", "Other major funding charities", "The National Academies").

### 13. Biases — `content/section-2/biases.yml`
- "A real-world example: Bias in AI-assisted policing" with ordered list (1–3).
- "Special responsibilities for researchers" with bold-prefixed bullets.
- "Further reading" links.

### 14. Privacy — `content/section-2/privacy.yml`
- Two numbered H3 subsections (`1. Private information…`, `2. How AI inputs…`).
- "Researchers should" bullet list.
- Warning callout (`callout.kind: warning`, "A deeper issue").

### 15. Sustainability Concerns — `content/section-2/sustainability.yml`
- "Where AI's resource demand comes from" with four H3 sub-headings.
- Two `blockquote` blocks with `cite:` (Fatih Birol, Anil Madhavapeddy).
- Carbon-emissions `data_table` with `headers`, `rows`.
- "Can AI still be part of the solution?" bullets.
- "For behavioural researchers" callout.

### 16. Key Regulations — `content/section-2/key-regulations.yml`
- "When in doubt" callout near the top.
- Copyright section with `Input` / `Output` H3 subsections.
- UK GDPR section with `Security` / `Data transfers` H3 subsections.
- "International regulations", "UK regulations", "University regulations", "AI guidance and policies in other UK institutions" lists.

### 17. Section 3 — `content/section-3.yml`
- Quicknav with 4 anchors.
- Four H2 sections, each followed by a `tool_grid`:
  - `#bruk-webinars` (markdown list of 3 webinars)
  - `#online-courses` (`tool_grid` of 5 courses)
  - `#youtube` (`tool_grid` of 4 channels)
  - `#advanced` (`tool_grid` of 3 advanced courses)

### 18. Section 4 — `content/section-4.yml`
- Three intro paragraphs introducing the panel.
- "Recordings" section using a single-column `subpage_list` with `style: "grid-template-columns: 1fr"`.
- Closing callout linking to the contact form.

### 19. Section 5 — `content/section-5.yml`
- Disclaimer in a `callout`.
- Contact: bullet list with email addresses (deliberately written `[@]` to deter scraping).
- Suggest a resource: link to the suggestion form.
- Privacy: link to the BR-UK Privacy Statement PDF.

## Block types reference

These are the YAML block kinds that can appear inside a page's `body` (or
inside a `prose` container). All blocks are written as a single-key mapping
(e.g. `- markdown: |`).

| Block            | What it renders                                  | Notes                                                       |
| ---------------- | ------------------------------------------------ | ----------------------------------------------------------- |
| `prose`          | `<div class="prose">…</div>` wrapper             | Children render inside this div. Multiple `prose` blocks per page allowed. |
| `lede`           | `<p class="hero__lede" style="…">…</p>`          | Optional `font_size` (default `1.1rem`); markdown inline.    |
| `markdown`       | Free-form prose                                  | Markdown links, lists, emphasis, blockquotes etc.            |
| `paragraph`      | A single styled `<p>`                            | Used by `home.yml` for the "Six sections cover…" intro.      |
| `h2`/`h3`/`h4`   | Headings, optionally with `id` for anchors       | `text` + optional `id`. Use a string shorthand if no id.     |
| `quicknav`       | "On this page" anchor list                       | `items[]` of `{href, label}` or `{ref, label, anchor}`.      |
| `tool_grid`      | Grid of tool cards                               | `items[].name`, `url`, `tag`, `desc`, `link_url`, `link_text`. |
| `subpage_list`   | Children-page link list (used on overview pages) | Items with `ref`/`href`, `title`, `blurb`. Optional `children[]` for nested links. Optional `style:` for inline grid CSS. |
| `callout`        | Coloured notice box                              | Optional `kind` (`caution`, `warning`), `heading`, `body` markdown. |
| `blockquote`     | Pull quote                                       | `body` (markdown) + optional `cite` rendered as `<cite>`.    |
| `references`     | Numbered citation list                           | Optional `id`, `heading`, `heading_level` (default `h3`), `items[]`. |
| `data_table`     | Plain `<table class="data-table">`               | `headers`, `rows[][]`. Used on Sustainability page.          |
| `breadcrumb`     | Top-of-page breadcrumb trail                     | Always supplied at page top-level (`breadcrumb:` key), not inside `body`. |
| `pager`          | Bottom prev/next navigation                      | Always supplied at page top-level (`pager:` key), not inside `body`. |
| `raw`            | Verbatim HTML escape hatch                       | Use sparingly.                                               |

## Asset locations

- `assets/css/style.css` — site-wide stylesheet (palette, layout, components).
- `assets/js/main.js` — minimal JS for the mobile menu toggle.
- `assets/favicon.svg` — favicon.
- `assets/BR-UK_LogoIcon_White.svg` — header logo (white, on the teal band).
- `assets/BR-UK_LogoFull_Colour_JPG.jpg`, `assets/BR-UK_LogoIcon_Colour_PNG.png`, `assets/BR-UK_LogoIcon_Colour_SVG.svg` — alternative logo files (not currently referenced from any HTML page; kept for future use).

To change the teal colour, edit the `--teal-*` CSS custom properties at the
top of `assets/css/style.css`. To change the logo on every page, replace
`assets/BR-UK_LogoIcon_White.svg` (keep the dimensions) and rebuild.

## Visual fidelity vs byte fidelity

The build is designed to produce **visually identical** output to the
pre-refactor HTML. It is *not* byte-identical: nested `<li>` indents are
flatter than the original, multi-line paragraphs in the source HTML are
collapsed onto a single line, and a few blank lines between elements have
shifted. None of these affect rendering — the browser ignores all whitespace
between block-level tags. The cross-page tests confirmed that every published
page has the identical set of links, anchor IDs, CSS classes, and
word-for-word visible text as the previous deploy.

## How to refactor or rename a page

1. Move/rename the YAML in `content/`.
2. Update any cross-page `ref:` values that pointed at the old page ID
   (page IDs are derived from path; renaming the file changes the ID).
3. Run `python3 build.py`. The build will fail loudly with `KeyError` if any
   `ref:` value is unresolvable, listing the bad reference and the page that
   contains it.
4. Verify the regenerated HTML and commit both YAML and HTML together.
