# Site structure — what's on each page, and which file to edit

This guide is a **map of the live site**. For every page, it tells you:

1. The page's name (as it appears on the website).
2. Where the page lives (its URL).
3. Which file holds its content (so a developer knows what to open).
4. What pieces of content are on the page (so you know what you can change).

If you want to **request a monthly update**, you don't edit this file —
you copy [REVISION-FORM.md](REVISION-FORM.md), which is the empty fill-in
form (with a worked example included). This guide (SITE-STRUCTURE.md) is
the reference you reach for when you need to confirm which page is which
and what's on each one.

> [!info] No coding required to use this guide
> You only need to read it. The developer takes the changes you describe
> in [REVISION-FORM.md](REVISION-FORM.md) and applies them to the
> matching file listed below.

## A few terms you'll see in this guide

These show up everywhere on a website, but the names can be unfamiliar.
None of them are programming concepts.

- **YAML file** — a plain-text file that holds a page's content. It looks
  like a structured shopping list (each line is a label and a value).
  You don't need to read or edit YAML — just treat each filename as a
  label for "the file that holds page X".
- **H2 / H3 / H4** — sub-headings on a page. H2 is the big section
  heading, H3 is a smaller heading inside an H2, etc. The page's main
  title (the very biggest one) is called the H1.
- **Block type** — the name for a kind of content piece on the page (a
  heading, a paragraph, a tool grid, a callout box, a citation list, …).
  This guide names them out so you can say "the tool grid on page X" or
  "the callout under the Tools heading" and the developer knows exactly
  where to look.
- **Anchor / anchor id** — a short, hyphenated label attached to a
  heading so the "On this page" box can link directly to it. You'll
  rarely need to interact with anchors directly; if you do, the form
  calls them "Short link name" instead.
- **Lede** — the grey introductory paragraph that appears immediately
  under a page's main title (an old journalism term). Every page on the
  site has one.
- **Pager** — the "Previous / Next" links at the bottom of every page
  (except Home).
- **Breadcrumb** — the trail at the top of a page (`Home / Section 1: Living Guide / …`).
- **Callout** — a coloured tip box (teal "info", amber "caution", red
  "warning") set apart from the body text.

A fuller glossary of every named block type — with one example for each
— is in the [Block-type glossary](#glossary-of-block-types) further down.

## How the site is organised

The website has **19 pages**, grouped into a home page and six numbered
sections:

- **Home** — the front page, with a section grid and audience tiles.
- **Section 1: Living Guide** — five stage sub-pages on using AI in research.
- **Section 2: Ethics & Responsibility** — five topic pages, two of which
  have nested guides for Publishers and UK Funders.
- **Section 3: Learning Resources** — courses, videos, podcasts.
- **Section 4: Webinars & Advice Sessions** — recordings of BR-UK panels.
- **Section 5: BR-UK Statement** — the living statement, currently out for
  community consultation. Its file is `content/statement.yml` and it publishes
  to `/statement.html`.
- **Section 6: Disclaimer & Contact** — contact details and disclaimer.
  Its file is `content/section-5.yml` and it publishes to `/section-5.html`.

> [!warning] Section 6's number and filename diverge
> Disclaimer & Contact was renumbered to Section 6 in August 2026, but its
> **filename was deliberately left alone** — page IDs are derived from
> filenames, so renaming would break every cross-page `ref:` and change a
> published URL. It is still `content/section-5.yml` → `/section-5.html`.
> (Section 5's file *was* renamed, from `about.yml` to `statement.yml`, because
> the editor asked for that URL change specifically.) Always go by the file
> paths above, not by the section number.

All content lives in the `content/` folder. Each page is one YAML file.
**You don't need to know what YAML is** to use this guide — just treat the
filenames as labels.

The published `*.html` files at the root of the repository are
**generated automatically** by a build script. **Do not hand-edit them** —
any change will be overwritten the next time the site is built. Every
generated `.html` file says this in a comment at the top.

## Page list

Use this table to find which file holds which page. Click a row's "What's
on it" link to jump to the section breakdown below.

| Page name on the website | URL on the live site | File the developer edits | What's on it |
| --- | --- | --- | --- |
| Home (front page) | `/` (or `/index.html`) | `content/home.yml` | [details](#home-page) |
| Section 1 — Living Guide overview | `/section-1/` | `content/section-1/_index.yml` | [details](#section-1-overview) |
| 1.1 Background Research & Evidence Synthesis | `/section-1/literature-review.html` | `content/section-1/literature-review.yml` | [details](#11-background-research--evidence-synthesis) |
| 1.2 Hypothesis Generation & Study Design | `/section-1/hypothesis-generation.html` | `content/section-1/hypothesis-generation.yml` | [details](#12-hypothesis-generation) |
| 1.3 Data Collection & Processing | `/section-1/data-collection.html` | `content/section-1/data-collection.yml` | [details](#13-data-collection) |
| 1.4 Data Analysis & Interpretation | `/section-1/data-analysis.html` | `content/section-1/data-analysis.yml` | [details](#14-data-analysis) |
| 1.5 Writing & Reporting | `/section-1/writing-reporting.html` | `content/section-1/writing-reporting.yml` | [details](#15-writing-and-reporting) |
| Section 2 — Ethics overview | `/section-2/` | `content/section-2/_index.yml` | [details](#section-2-overview) |
| 2.1 Disclosure & Transparency | `/section-2/disclosure.html` | `content/section-2/disclosure.yml` | [details](#21-disclosure-and-transparency) |
| 2.1a What publishers said about AI use | `/section-2/publishers.html` | `content/section-2/publishers.yml` | [details](#21a-publishers) |
| 2.1b What UK funders said about AI use | `/section-2/uk-funders.html` | `content/section-2/uk-funders.yml` | [details](#21b-uk-funders) |
| 2.2 Biases | `/section-2/biases.html` | `content/section-2/biases.yml` | [details](#22-biases) |
| 2.3 Privacy | `/section-2/privacy.html` | `content/section-2/privacy.yml` | [details](#23-privacy) |
| 2.4 Sustainability Concerns | `/section-2/sustainability.html` | `content/section-2/sustainability.yml` | [details](#24-sustainability) |
| 2.5 Key Regulations | `/section-2/key-regulations.html` | `content/section-2/key-regulations.yml` | [details](#25-key-regulations) |
| Section 3 — General AI Learning | `/section-3.html` | `content/section-3.yml` | [details](#section-3-general-ai-learning) |
| Section 4 — BR-UK AI Webinars and Advice Sessions | `/section-4.html` | `content/section-4.yml` | [details](#section-4-webinars-and-advice-sessions) |
| Section 5 — BR-UK Statement | `/statement.html` | `content/statement.yml` | [details](#br-uk-statement) |
| Section 6 — Disclaimer & Contact | `/section-5.html` | `content/section-5.yml` | [details](#section-6-disclaimer-and-contact) |

## Site-wide elements (header, footer, navigation)

Some things appear on **every** page — the logo, top navigation menu,
footer, contact links. Those don't live in any single page's file;
they live in **`content/_site.yml`**.

| What you see on every page | Where in `content/_site.yml` |
| --- | --- |
| Logo image | `brand.logo` |
| Brand text "AI Tools & Resource Repository" | `brand.name` |
| Tagline "Behavioural Research UK" | `brand.tag` |
| Top navigation labels (Home, 1. Living Guide, …) | `nav` |
| Footer "About BR-UK" paragraph | `footer.about` |
| Footer "Sections" link list | `footer.sections` |
| Footer "Get in touch" link list | `footer.contact` |
| Footer copyright line | `footer.copyright` |
| Footer "A living repository · Last content review …" | `footer.status` |

The white header uses a cropped version of the official colour logo, with the
repository name above the BR-UK tagline. Desktop navigation occupies its own row;
at 1160px and below it opens from the menu button. The layout lives in
`assets/css/style.css` and the shared markup in `templates/_base.html`.

The home page has a slightly fuller footer (it lists the Privacy Statement
PDF and includes "comprising partner institutions and government bodies
across the UK"). Those overrides live in `content/home.yml` under
`footer_about` and `footer_contact`.

---

# Per-page details

For each page below, the **left column** is what you see on the live site,
and the **right column** is what kind of block the developer will look for
in the file. You don't need to memorise these — they're here so you can
say "please change the third tool card on the literature review page" and
the developer can find it instantly.

## Home page

**File:** `content/home.yml`

| What you see on the page | Block type in the file |
| --- | --- |
| Teal hero band — small pre-headline ("Behavioural Research UK · Living repository") | `hero.eyebrow` |
| Big main headline ("AI tools and resources for behavioural researchers") | `hero.heading` |
| Hero introductory paragraph (grey, under the headline) | `hero.lede` |
| *No hero buttons.* Adding a `hero.actions` list back to the file restores them | `hero.actions` (absent since Aug 2026) |
| Three teal-band tiles directly under the hero: "New to AI in research?", "Concerned about responsible use?", "Looking for learning resources?" | `audience` (one entry per tile) |
| "How to explore the repository" heading. An optional `explore.intro` renders a grey line underneath it — currently unset, so no line shows | `explore.heading` / `explore.intro` |
| Six cards in the grid (Sections 1–4, then Section 5 = BR-UK Statement, Section 6 = Disclaimer & Contact) | `section_cards` (one entry per card) |
| "The Repository in a Nutshell" heading + 2 paragraphs | `what.heading` / `what.paragraphs` |
| "Any suggestions?" teal box at the very bottom, with the suggestion-form link | `suggest` (a `callout` block) |

## BR-UK Statement

**File:** `content/statement.yml` — published at `/statement.html`.

| What you see on the page | Block type in the file |
| --- | --- |
| Page title in the browser tab | `title` |
| Breadcrumb at top ("Home / Section 5: BR-UK Statement") | `breadcrumb` |
| Teal pill near the top ("Section 5 · Living document") | `badge` |
| Big page heading ("BR-UK Statement") | `heading` |
| Subtitle ("Using AI for Behavioural Research Effectively and Responsibly") | `h2_alt.text` |
| Lede paragraph (grey) | inside `body` → first `lede` block |
| Two short paragraphs on the consultation and Wellcome Open Research | inside `body` → `markdown` |
| Three full-width linked boxes (OSF draft, YouTube, Media Hopper) | inside `body` → `subpage_list` |
| Prev / next navigation at the bottom | `pager` |

> [!note] This page was `about.html` until August 2026
> The editor asked for the URL to say "statement". `content/about.yml` became
> `content/statement.yml`, so the page ID changed from `about` to `statement`
> and every cross-page `ref:` was updated. A small redirect stub is left at
> `about.html` so old inbound links still resolve.

## Section 1 overview

**File:** `content/section-1/_index.yml`

| What you see | Block |
| --- | --- |
| Breadcrumb | `breadcrumb` |
| "Section 1" pill | `badge` |
| Page heading | `heading` |
| Lede paragraph | `body` → first `lede` |
| "Not sure where to start?" list of three external resources, fenced by a horizontal rule above and below | `body` → `raw` (`<hr>`) + `markdown` + `raw` (`<hr>`) |
| "Jump to a stage of your research" heading | `body` → `h2` |
| Five numbered, full-width stage cards | `body` → `subpage_list` with `variant: "stages"` and one entry per card in `items` |
| "A Note on Responsible Use" callout box | `body` → `callout` |
| Prev / next navigation | `pager` |

> The starter list is deliberately kept off the heading hierarchy (bold lead-in,
> not an `h2`) so "Jump to a stage of your research" stays the page's only `h2`
> and the sub-page list reads as the main path.

The stage list uses `labelledby: "research-stages"` to connect it to the heading.
Each item contains `ref`, `title`, and `blurb`; stage numbers follow the item order.

## Section 1 sub-pages — common shape

The five Section 1 sub-pages (Background Research & Evidence Synthesis,
Hypothesis Generation, Data Collection, Data Analysis, Writing & Reporting)
all follow the same basic shape:

| What you see | Block |
| --- | --- |
| Browser tab title | `title` |
| Breadcrumb at top | `breadcrumb` |
| Stage pill ("Section 1 · Stage 1", etc.) | `badge` |
| Page heading | `heading` |
| Lede paragraph (grey, slightly larger) | `body` → first `lede` |
| Optional intro paragraphs after the lede | `body` → `markdown` blocks |
| "On this page" box (anchor links to sections) | `body` → `quicknav` |
| Each H2 section with its content | `body` → `h2` block followed by `markdown`, `tool_grid`, `callout`, `blockquote`, etc. |
| Prev / next navigation | `pager` |

**Tip: how to find a specific section in the file.** Open the YAML file
and search (Cmd-F / Ctrl-F) for either the heading text (e.g. `text: "Tools"`)
or its anchor id (e.g. `id: "tools"`). The block immediately under that
match is the one you'll edit.

The five sub-pages and the H2 sections each one contains:

### 1.1 Background Research & Evidence Synthesis

**File:** `content/section-1/literature-review.yml` — note the filename still
says `literature-review`; see the warning below.

This page is split into **two major H2 sections**, separated by a horizontal
rule, with everything else nested underneath as H3s:

- **Background Research** — "What AI can help with", "Tools" (a tool grid of ten
  tools, ordered so related ones sit side by side), "Hear from researchers
  using them".
- **Evidence Synthesis** — an intro, then the three numbered core resources
  (the Cochrane/Campbell/JBI/CEE joint position statement, RAISE, and tool
  repositories), then "Putting this into practice".

> [!warning] Page title and filename diverge
> This page was renamed from "Literature Review & Background Research" to
> "Background Research & Evidence Synthesis" in August 2026, but the file is
> still `literature-review.yml` and the live URL is still
> `/section-1/literature-review.html`. Page IDs are derived from filenames, so
> renaming the file would break every cross-page `ref:` and change a published
> URL. Go by the file path, not the title.

### 1.2 Hypothesis Generation

**File:** `content/section-1/hypothesis-generation.yml`. Sections: "What
AI can help with", "Tools", and seven "Example: …" sections covering
refining questions, designing surveys, suggesting methods, intervention
content, and analysing past data. Closes with "Other key readings".

### 1.3 Data Collection

**File:** `content/section-1/data-collection.yml`. Sections: "What AI can
help with", "Tools", and three "Example: …" sections (chatbots for
qualitative data, delivering interventions, synthetic data and populations).

### 1.4 Data Analysis

**File:** `content/section-1/data-analysis.yml`. Sections: short intro
lists for qualitative and quantitative analyses, "Tools" (a tool grid),
"AI for quantitative analysis" (with a caution callout), "AI for
qualitative analysis — case studies" (five short case studies),
"References".

### 1.5 Writing and Reporting

**File:** `content/section-1/writing-reporting.yml`. Sections: "Writing
& reporting", a caution callout, "Publication" (with a tool grid for
pre-submission tools), "Presentation & outreach" (tool grid for
NotebookLM, Gamma, Napkin), "Citation generation tools", "Further
reading".

## Section 2 overview

**File:** `content/section-2/_index.yml`

| What you see | Block |
| --- | --- |
| Breadcrumb, badge, heading | top-level keys |
| Lede paragraph | `body` → first `lede` |
| "Jump to a topic" heading | `body` → `h2` |
| Five linked topic cards. The Disclosure card has two nested children: Publishers, UK Funders. | `body` → `subpage_list`. The Disclosure entry has a `children` list of two items. |
| "Three questions to ask before you integrate AI" + numbered list | `body` → `h2` + `markdown` |
| "Recommended starting reads" + bullet list | `body` → `h2` + `markdown` |
| Prev / next navigation | `pager` |

## Section 2 sub-pages — common shape

The seven Section 2 sub-pages have the same shape as the Section 1
sub-pages (breadcrumb, badge, heading, lede, optional quicknav, H2
sections, pager). The two nested pages (Publishers and UK Funders) have
a three-level breadcrumb (Home / Section 2 / Disclosure / current).

### 2.1 Disclosure and Transparency

**File:** `content/section-2/disclosure.yml`. Sections: "When using AI
tools", an inline grid linking to the Publishers and Funders pages,
"Core rules for AI use" (seven numbered subsections "1. AI cannot be
an author" through "7. Always check specific guidelines"), "Publisher
disclosure template (Elsevier)" quote, "Planning a submission?" callout.

### 2.1a Publishers

**File:** `content/section-2/publishers.yml`. One H2 per publisher
(11 total): Nature, Elsevier, Taylor & Francis, SAGE, Wiley, APA,
Frontiers, Cambridge, PNAS, MDPI, Cell Press. Each has sub-headings
and bullet lists.

### 2.1b UK Funders

**File:** `content/section-2/uk-funders.yml`. Sections: "Joint funder
statement" (six paragraphs), "Links to funders", "Current members of
the Research Funders Policy Group", "Other major funding charities",
"The National Academies".

### 2.2 Biases

**File:** `content/section-2/biases.yml`. Sections: "A real-world
example: Bias in AI-assisted policing" (with numbered list 1–3),
"Special responsibilities for researchers" (bullet list), "Further
reading".

### 2.3 Privacy

**File:** `content/section-2/privacy.yml`. Sections: "Why privacy
matters in AI research" (two numbered subsections), "Researchers
should" bullets, "A deeper issue" warning callout, "Further reading".

### 2.4 Sustainability

**File:** `content/section-2/sustainability.yml`. Sections: "Where
AI's resource demand comes from" (Data centres, Carbon emissions
from training, Hardware production, Global supply chain), an emissions
table, "Can AI still be part of the solution?", a "For behavioural
researchers" callout, "Further reading".

### 2.5 Key Regulations

**File:** `content/section-2/key-regulations.yml`. Sections: "When in
doubt" callout, "Copyright and intellectual property" (Input/Output
subsections), "Data Protection and Privacy (UK GDPR)" (Security/Data
transfers subsections), "International regulations", "UK regulations",
"University regulations", "AI guidance and policies in other UK
institutions".

## Section 3: General AI Learning

**File:** `content/section-3.yml`. Sections: "BR-UK AI Webinars" (3
recordings), "Online courses" (5-tool grid), "YouTube channels" (4-tool
grid), "Advanced learning resources" (3-tool grid).

## Section 4: Webinars and Advice Sessions

**File:** `content/section-4.yml`. Sections: three intro paragraphs
about the advice sessions, "Recordings" (3 video links), a callout
inviting future questions.

## Section 6: Disclaimer and Contact

**File:** `content/section-5.yml`. Sections: "Disclaimer" callout,
"Contact" with two email addresses, "Suggest a resource", "Privacy"
link to the BR-UK Privacy Statement PDF.

---

# Glossary of "block types"

Most of the changes you'll request fall into one of these block types.
You don't need to memorise them — the form takes plain English — but
it's useful to have the names in one place if you want to say *"in the
tool grid"* or *"in the references list"* with precision.

| Block type | Plain-English meaning | Example on the live site |
| --- | --- | --- |
| `lede` | The big grey paragraph immediately under the page title | The intro under "Background Research & Evidence Synthesis" |
| `markdown` | Free-flowing prose: paragraphs, bullet lists, links | Almost every paragraph of body text |
| `h2` / `h3` / `h4` | A sub-heading on the page | "Background Research", "Tools", "Evidence Synthesis" |
| `quicknav` | The "On this page" anchor box near the top | The blue box with a list of links to in-page sections |
| `tool_grid` | The grid of tool cards (each card has a name, description, and link) | The five paired tool cards on 1.1 (Elicit vs. Undermind, etc.) |
| `subpage_list` | A list of links to other pages on the site | The five-stage list on the Section 1 overview |
| `callout` | A coloured tip box (teal "info", amber "caution", red "warning") | The "A Note on Responsible Use" box on Section 1 overview |
| `blockquote` | A pull quote, often a citation | The Fatih Birol quote on 2.4 Sustainability |
| `references` | A numbered citation list, usually at the bottom of a page | The "References" list on 1.4 Data Analysis |
| `raw` | Literal HTML passed straight through — used sparingly, e.g. for a `<hr>` divider | The rules around the starter list on the Section 1 overview |
| `data_table` | A simple table | The carbon-emissions table on Sustainability |
| `breadcrumb` | The trail at the top: Home / Section / Page | Top of every page except Home |
| `pager` | The "Previous / Next" links at the bottom | Bottom of every page except Home |
| `badge` | The small teal pill above the page heading | "Section 1 · Stage 1", "Living document · Coming 2026" |

---

# For developers — technical appendix

> [!warning] Content editors: you can stop reading here
> Everything below is for the person who applies your requested changes
> to the files. You don't need any of it to fill in a revision request —
> [REVISION-FORM.md](REVISION-FORM.md) covers everything you need.

This section is only needed if you're the person actually editing the YAML
files.

## Build, preview, commit

```bash
pip install -r build-requirements.txt    # one-time
python3 build.py                         # rebuild every page
python3 build.py home                    # rebuild a single page (by page id)
python3 build.py --check                 # dry-run; exits non-zero on drift
python3 -m http.server 8080              # local preview at http://localhost:8080
```

The published `*.html` files are committed to the repo (so GitHub Pages
serves them with no toolchain), but they are regenerated from the YAML
sources by `build.py`. Always commit the YAML *and* the regenerated HTML
in the same commit; `python3 build.py --check` before commit will catch
you if you forget. Each generated HTML file starts with a comment naming
its YAML source.

## Cross-page links use page IDs, not URLs

Inside a YAML file, links to other pages on the site use a **page ID**
(e.g. `section-1.literature-review`), not a relative URL. The build
resolves each ID to the correct relative path from the page being
rendered, so reorganising files won't silently break links. The full list
of page IDs:

| Page ID | YAML source |
| --- | --- |
| `home` | `content/home.yml` |
| `statement` | `content/statement.yml` |
| `section-1` | `content/section-1/_index.yml` |
| `section-1.literature-review` | `content/section-1/literature-review.yml` |
| `section-1.hypothesis-generation` | `content/section-1/hypothesis-generation.yml` |
| `section-1.data-collection` | `content/section-1/data-collection.yml` |
| `section-1.data-analysis` | `content/section-1/data-analysis.yml` |
| `section-1.writing-reporting` | `content/section-1/writing-reporting.yml` |
| `section-2` | `content/section-2/_index.yml` |
| `section-2.disclosure` | `content/section-2/disclosure.yml` |
| `section-2.publishers` | `content/section-2/publishers.yml` |
| `section-2.uk-funders` | `content/section-2/uk-funders.yml` |
| `section-2.biases` | `content/section-2/biases.yml` |
| `section-2.privacy` | `content/section-2/privacy.yml` |
| `section-2.sustainability` | `content/section-2/sustainability.yml` |
| `section-2.key-regulations` | `content/section-2/key-regulations.yml` |
| `section-3` | `content/section-3.yml` |
| `section-4` | `content/section-4.yml` |
| `section-5` | `content/section-5.yml` |

## Renaming a page

1. Rename / move the YAML file in `content/`.
2. Update any `ref:` values that pointed at the old page ID (the build
   fails loudly with `KeyError` listing the bad reference and the page
   that contains it).
3. Run `python3 build.py`.
4. Commit YAML + regenerated HTML together.

## Visual fidelity vs byte fidelity

The build is designed to produce **visually identical** output to the
pre-refactor HTML. It is not byte-identical — nested `<li>` indents are
flatter than the original, multi-line paragraphs in the source HTML are
collapsed onto a single line, and a few blank lines between elements have
shifted. None of these affect rendering — the browser ignores all
whitespace between block-level tags. Verified at refactor time: every
published page has the identical set of links, anchor IDs, CSS classes,
and word-for-word visible text as the previous deploy.

## Asset locations

- `assets/css/style.css` — site-wide stylesheet (palette, layout, components).
- `assets/js/main.js` — minimal JS for the mobile menu toggle.
- `assets/favicon.svg` — favicon.
- `assets/BR-UK_LogoIcon_White.svg` — header logo (white, on the teal band).
- Other logo files in `assets/` — alternative formats, not currently referenced.

To change the teal colour, edit the `--teal-*` CSS custom properties at
the top of `assets/css/style.css`. To change the logo on every page,
replace `assets/BR-UK_LogoIcon_White.svg` (keep the dimensions) and
rebuild.
