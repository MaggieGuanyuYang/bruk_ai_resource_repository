# Revision request

> [!info] What this file is
> A monthly form for requesting changes to the BR-UK AI Tools &
> Resources Repository. You don't need to know any code, YAML, or
> Markdown to use it — you describe what you want changed in plain
> English, and the developer applies it.
>
> **The blank form is at the bottom of this file** —
> see [Blank form to copy](#blank-form-to-copy). A worked example showing
> what a real filled-in request looks like is just above it.

## Quick start

1. **Open the live site** in your browser and find the page you want changed.
2. **Locate that page in [SITE-STRUCTURE.md](SITE-STRUCTURE.md)** to confirm
   the page name and what's on it.
3. **Copy the [blank form](#blank-form-to-copy)** at the bottom of this
   file into a new note in Obsidian (or a Word doc, or an email).
4. **For each page you want changed**, fill in any of three subsections:
    - **Changes / Additions** — what should be changed, replaced, or added.
    - **Deletions** — what should be removed (with a one-line reason).
    - **Format / Layout Notes** — free-form instructions about styling,
      ordering, position.
5. **Skip what you don't need.** Pages with no changes don't need an
   entry. Subsections that don't apply can be left blank or removed.
6. **Send the filled form to the developer.** They'll come back with any
   clarifying questions before applying changes.

> [!tip] You can keep the form open in Obsidian
> The blank form is wrapped in a fenced code block (four backticks at the
> top and bottom) so you can copy it in one go. Inside Obsidian, paste it
> into a new note and edit freely — the structure won't break as long as
> you stay inside that outer fence.

## What goes in each subsection

### Changes / Additions

The most common kind of edit. For each one, fill in two short
sub-fields:

- **Location or old text.** Where on the page the change goes. This can be:
    - a direct quote of the existing wording (best — removes ambiguity), or
    - a description of position (e.g. *"In the Tools box, after Evidano"*), or
    - the name of a section or box (e.g. *"General reading box"*).
- **Updated text.** The new wording, or the new content to add.

If you're inserting something brand new (no old text to replace), just
describe *where* it goes in the "Location" field, then put the new
content in the "Updated text" field.

### Deletions

For any text or section that should be removed.

- **Text to delete.** Quote the wording, or describe the section clearly.
- **Reason.** One line so the developer knows it's deliberate and not an
  accident — and so future maintainers understand the choice.

### Format / Layout Notes

Free-form sentences for anything about styling, position, ordering, or
appearance. Examples (taken from real previous monthly updates):

- *"Make the references appear different to the main text — bullet
  points or smaller font size"*
- *"Move the page break above the AI literature review section"*
- *"Move the 'Hear from researchers' list above the Tools grid"*
- *"NOTE: 'quantative' is misspelt in the heading"*

If you have a screenshot illustrating what you mean, attach it to your
message and refer to it here ("see attached screenshot").

## Tips

> [!tip] Don't worry about exact phrasing
> *"Move this above that"*, *"make this smaller"*, *"change X to Y"* are
> all fine. The developer translates plain English into the underlying
> code change.

> [!tip] Quote the old text whenever you can
> Quoting removes ambiguity. If the same phrase appears twice on the page,
> the developer can pick the right occurrence rather than guessing.

> [!tip] Side notes are welcome
> Noticed a typo or broken link that wasn't part of the change you came
> in to make? Add it as a quick "NOTE:" in the Format / Layout Notes
> section. Tiny fixes get rolled in alongside the main edits.

> [!warning] Keep the form safe to share
> Don't paste passwords, API keys, internal-only URLs, personally
> identifying participant data, or anything else you wouldn't put in an
> email.

## Worked example

Here's what a filled-in request actually looks like, based on a real
previous monthly update.

```
================================================================
Monthly revision request

Date:           28/04/2026
Requested by:   Dr. A. Researcher
Reason:         Routine monthly content refresh — three pages affected.


----------------------------------------------------------------
Page: Home
----------------------------------------------------------------

Changes / Additions
-------------------

1. Location or old text:
     The lede paragraph at the top of the home page.

   Updated text:
     A practical guide to AI in behavioural research, kept up to date
     by the BR-UK community. Covers every stage of the research
     lifecycle — from literature reviews and study design through
     analysis, writing, and dissemination — plus the ethics,
     regulations, and disclosure expectations researchers actually
     need.

2. Location or old text:
     Add a new paragraph in the "What this repository is — and isn't"
     section, immediately after the third paragraph.

   Updated text:
     You can subscribe to receive an email each month when the
     repository is updated — sign up via our [mailing list](https://example.org/mailing-list).


Deletions
---------

1. Text to delete:
     The "Browse all sections" button on the hero band (the outlined
     teal button next to "Start with the Living Guide").

   Reason:
     Redundant with the section grid immediately below. April's user
     test showed people couldn't tell the two CTAs apart.


Format / Layout Notes
---------------------

Make the small grey "eyebrow" line above the H1 ("Behavioural Research
UK · Living repository") slightly smaller — currently competes visually
with the headline.


----------------------------------------------------------------
Page: 1.1 Background Research & Evidence Synthesis
----------------------------------------------------------------

Changes / Additions
-------------------

1. Location or old text:
     In the "Tools" grid, replace the description for Elicit.

   Old description (currently on the page):
     Pulls research questions, findings and limitations out of papers
     into a table. Built for fast exploratory reviews.

   Updated description:
     Pulls research questions, findings and limitations out of papers
     into a table. Built for fast exploratory reviews — not for
     systematic ones.

   Note:
     Also update the link from https://elicit.com/ to
     https://elicit.com/pricing.

2. Location or old text:
     At the end of the "Evidence Synthesis" section, add a new
     paragraph plus citation.

   Updated text:
     Pang and colleagues (2025) propose a protocol for comparing AI
     tools to manual methods in systematic reviews:

     Pang, X., Saif-Ur-Rahman, K., Berhane, S., Yao, X., Kothari, K.,
     Taneri, P. E., Thomas, J., & Devane, D. (2025). Comparing
     Artificial Intelligence and manual methods in systematic review
     processes: Protocol for a systematic review. *Journal of
     Clinical Epidemiology*, 181, 111738.
     https://doi.org/10.1016/j.jclinepi.2025.111738


Format / Layout Notes
---------------------

NOTE: "quantative" is misspelt in the heading — should be "quantitative".


----------------------------------------------------------------
Page: 2.4 Sustainability Concerns
----------------------------------------------------------------

Changes / Additions
-------------------

1. Location or old text:
     The link "Can We Mitigate AI's Environmental Impacts?" in the
     "Further reading" section.

   Old URL:
     https://environment.yale.edu/news/article/can-we-mitigate-ais-environmental-impacts

   New URL:
     https://e360.yale.edu/features/can-we-mitigate-ais-environmental-impacts

   Reason:
     The old article moved when Yale rebuilt their site.


----------------------------------------------------------------
Page: Section 2 — Ethics overview
----------------------------------------------------------------

Changes / Additions
-------------------

1. Location:
     Add a new banner box below the "Recommended starting reads"
     section, before the prev/next navigation.

   Box title:
     Understanding the Landscape of AI Risks

   Box body:
     The MIT AI Risk Repository is a comprehensive, publicly
     accessible database that consolidates over 1,600 AI risks
     extracted from 65 existing frameworks. It serves as a "common
     frame of reference" for understanding the full spectrum of
     AI-related risks, with three components: an AI Risk Database, a
     Causal Taxonomy, and a Domain Taxonomy.

   Citation to attach at the end of the box:
     Slattery, P., Saeri, A. K., Grundy, E. A. C., Graham, J., Noetel,
     M., Uuk, R., Dao, J., Pour, S., Casper, S., & Thompson, N. (2024).
     The AI Risk Repository: A Comprehensive Meta-Review, Database,
     and Taxonomy of Risks from Artificial Intelligence.
     https://doi.org/10.48550/arXiv.2408.12622

   Screenshot (optional):
     See attached annotated screenshot showing where the new box should
     sit (red arrow) and the styling I have in mind (matches the
     teal-info callout used elsewhere on this page).


End of request.
================================================================
```

## Blank form to copy

Copy everything inside the box below into a new note in Obsidian (or
into a Word document, or directly into an email). Fill in the blanks,
add as many pages as you need, and send.

````
================================================================
Monthly revision request

Date:           ____________________
Requested by:   ____________________
Reason:         ____________________


----------------------------------------------------------------
Page: ____________________________________________
URL (optional): ___________________________________
----------------------------------------------------------------

Changes / Additions
-------------------

1. Location or old text:


   Updated text:


   Screenshot (optional — write a name/filename you'll attach):




2. Location or old text:


   Updated text:


   Screenshot (optional):




Deletions
---------

1. Text to delete:


   Reason:




Format / Layout Notes
---------------------



================================================================
````

> [!tip] Adding more than one page
> To request changes on more than one page, copy the entire dashed
> `Page: ___` block (from one row of dashes to the next) and paste it as
> many times as you need — once per page. Leave subsections empty or
> remove them if you have no changes to that subsection on that page.

> [!tip] Adding a brand-new banner, callout, or sidebar box
> Inside the `Updated text:` area, you can use these extra labels to
> describe a brand-new boxed block of content:
>
> ```
> Box title:   ____
> Box body:    ____
> Citation:    ____
> Screenshot:  ____
> ```
>
> The worked example above shows this in use ("Section 2 — Ethics
> overview" block).

## For AI implementers (and curious editors)

If the implementer of this revision is Claude Code or another AI rather
than a human developer, the implementer must follow the prompt and
safety rules at
[UPDATE-PROCEDURE.md → Handing the form to Claude Code](UPDATE-PROCEDURE.md#handing-the-form-to-claude-code).
Editors don't need to read this section — it's here so the AI knows
exactly which YAML field each common form pattern maps to, and so the
mapping is visible for audit.

### Form pattern → YAML target

| What the editor wrote in the form | YAML target the AI should edit |
| --- | --- |
| Changes / Additions: "add a new tool to the Tools box" + name/url/desc/tag | append to `tool_grid:` list in `content/<page>.yml` |
| Changes / Additions: "remove tool X" or "replace tool X with Y" | edit/remove the matching entry in the same `tool_grid:` |
| Changes / Additions: a broken-link pair (old URL → new URL) | search for old URL in the YAML; replace verbatim |
| Changes / Additions: "rewrite the lede paragraph" + new text | replace `body:` → first `prose:` → first `lede:` field |
| Changes / Additions: "change wording of paragraph X" + old + new text | string-replace inside the matching `markdown:` block |
| Changes / Additions: "rename heading 'Foo' to 'Bar'" | edit the matching `h2:` / `h3:` / `h4:` block's `text:` field |
| Changes / Additions: prev/next pager update | edit `pager.prev` / `pager.next` using **page-id refs** from SITE-STRUCTURE.md, not URLs |
| Changes / Additions: update the "On this page" anchor list | edit the matching `quicknav.items[]` list |
| Changes / Additions: a new banner / sidebar box with `Box title:` + `Box body:` + optional `Citation:` | new `callout:` block with `heading:` and `body:` (citation embedded as a markdown link inside `body:`) — unless the form asks for a different shape |
| Changes / Additions: a brand-new section heading + prose | new `h2:` block + `markdown:` block |
| Changes / Additions: a brand-new sub-page | new YAML file under `content/<section>/`, plus `subpage_list[]` entry on the section index, plus `pager` updates on adjacent pages |
| Changes / Additions: "add another section card on the main page" / hero edit / audience tile edit | edit `content/home.yml` top-level keys (`hero:`, `section_cards:`, `audience:`, `explore:`, `what:`). These are home-page-only structures, **not** `_BLOCK_RENDERERS` blocks — they're consumed by `templates/home.html` directly. |
| Changes / Additions: "add or change a hyperlink inside an existing paragraph" | string-replace inside the matching `markdown:` block; preserve surrounding text verbatim — don't rewrite the whole paragraph |
| Deletions: "remove text X / box Y / list Z" | remove the named block or the matching string |
| Format/Layout Notes: "move section X above section Y" | re-order the YAML blocks under `body:` (or under the relevant `prose:` container) |
| Format/Layout Notes: styling — font size, colour, spacing | this is a `assets/css/style.css` change, **NOT** a YAML edit. Don't apply unless the form explicitly authorises a stylesheet edit. Surface as a question instead. |
| Format/Layout Notes: "NOTE: typo in word X" | one-line search-and-replace in the YAML where that word appears |
| Site-wide changes (top nav / footer / brand) | edit `content/_site.yml` (home page footer overrides live in `content/home.yml`) |

### Hard rules for the AI

1. **Show a diff before applying.** For each numbered edit, output the
   proposed file path and the before/after for the affected lines, then
   wait for the editor's "yes apply".
2. **Ask before guessing.** Multiple tool grids on a page; ambiguous
   "Box title/body" → which block type; partial-quote "old text" that
   doesn't match exactly. Ask, don't infer.
3. **Don't touch CSS or templates** (`assets/css/style.css`,
   `templates/*.html`) unless the form's Format/Layout Notes
   *explicitly* says "edit the stylesheet" or "edit the template".
4. **Don't fabricate URLs, citations, or DOIs.** If a citation lacks a
   DOI, ask.
5. **Use page-id refs, not URLs**, for `pager`, `subpage_list`,
   `breadcrumb`. The page-id table is in SITE-STRUCTURE.md.
6. **After every YAML edit**, run `python3 build.py` to regenerate
   the HTML, **then** `python3 build.py --check -q` to verify the
   build is in sync (must exit 0). `--check` alone does not write —
   it only verifies. Run `build.py` first.
7. **Don't change a block's `id:` (anchor slug) or rename a YAML file
   under `content/`** unless the form explicitly names that change —
   anchor slugs and page IDs are referenced by `quicknav`, `pager`,
   `subpage_list`, and `breadcrumb` entries on other pages, and silent
   renames break cross-page navigation.
8. **After all edits applied**, grep the repo for any
   `quicknav`/`pager`/`subpage_list`/`breadcrumb` entry whose
   `label`/`title` text quotes a heading you renamed in this batch.
   Surface any matches before staging the commit so the editor can
   decide whether to update those references too.

## After you send your request

1. **Turnaround.** A typical monthly request is applied within one
   working day. If anything is urgent, flag it at the top of the request
   ("URGENT: external partner reported broken link").
2. **What happens behind the scenes.** The developer edits the matching
   content file, regenerates the HTML, and pushes the result to GitHub.
   The live site updates automatically within a few minutes.
3. **How to verify your changes are live.** Open the live site
   (`https://maggieguanyuyang.github.io/bruk_ai_resource_repository/`),
   refresh the page (Cmd-Shift-R on Mac, Ctrl-Shift-R on Windows — this
   forces a fresh load and bypasses the cache). If your change isn't
   there after about ten minutes, ask the developer to confirm the build
   went through.
4. **Clarifications.** If anything in your request is ambiguous, the
   developer will reply with a question before applying the change
   rather than guess. Reply with the clarification and they'll proceed.

## Page list (for the "Page:" field)

Copy the page name in the **left** column into the "Page:" field of
each "Page:" block. The right column shows where the page lives on the
live site so you can confirm you're picking the right one.

> [!info] If this list ever disagrees with [SITE-STRUCTURE.md](SITE-STRUCTURE.md#page-list)
> SITE-STRUCTURE.md is the source of truth — the developer keeps it in
> sync with the actual file structure.

| Page name (write this in the "Page:" field) | URL on the live site |
| --- | --- |
| Home | `/` |
| Section 1 — Living Guide overview | `/section-1/` |
| 1.1 Background Research & Evidence Synthesis | `/section-1/literature-review.html` |
| 1.2 Hypothesis Generation & Study Design | `/section-1/hypothesis-generation.html` |
| 1.3 Data Collection & Processing | `/section-1/data-collection.html` |
| 1.4 Data Analysis & Interpretation | `/section-1/data-analysis.html` |
| 1.5 Writing & Reporting | `/section-1/writing-reporting.html` |
| Section 2 — Ethics overview | `/section-2/` |
| 2.1 Disclosure & Transparency | `/section-2/disclosure.html` |
| 2.1a What publishers said about AI use | `/section-2/publishers.html` |
| 2.1b What UK funders said about AI use | `/section-2/uk-funders.html` |
| 2.2 Biases | `/section-2/biases.html` |
| 2.3 Privacy | `/section-2/privacy.html` |
| 2.4 Sustainability Concerns | `/section-2/sustainability.html` |
| 2.5 Key Regulations | `/section-2/key-regulations.html` |
| Section 3 — General AI Learning | `/section-3.html` |
| Section 4 — BR-UK AI Webinars and Advice Sessions | `/section-4.html` |
| Section 5 — BR-UK Statement | `/statement.html` |
| Section 6 — Disclaimer & Contact | `/section-5.html` |

> [!tip] If your target is a section *within* a page (not the whole page)
> Pick the page from the table above for the "Page:" field, then
> describe the section in the "Location or old text" line — for example:
> *"In the 'For more advanced learning' section of Section 3 — General
> AI Learning, add a new tool card after Cooperative AI Interactive
> Course."*

> [!tip] If you can't find your page in the list
> Write the page name freely (whatever you call the page in your head)
> and link to the page URL on the live site. The developer will work
> out which file it maps to.
