# BR-UK AI Tools & Resources Repository

A GitHub Pages rebuild of the [Behavioural Research UK AI Tools and Resources Repository](https://usher.ed.ac.uk/behavioural-research-uk/learning-resources/ai-tools-and-resources-repository), rehoused as a standalone, behavioural-researcher-friendly site.

**Live site:** _deploy this repo to GitHub Pages; see below._

## Structure

```
.
├── index.html                      Home page with section navigation
├── about.html                      BR-UK Statement
├── section-1/
│   ├── index.html                  Living Guide overview
│   ├── literature-review.html
│   ├── hypothesis-generation.html
│   ├── data-collection.html
│   ├── data-analysis.html
│   └── writing-reporting.html
├── section-2/
│   ├── index.html                  Ethics overview
│   ├── disclosure.html
│   ├── publishers.html             Publisher policies (nested under Disclosure)
│   ├── uk-funders.html             Funder policies (nested under Disclosure)
│   ├── biases.html
│   ├── privacy.html
│   ├── sustainability.html
│   └── key-regulations.html
├── section-3.html                  General AI learning resources
├── section-4.html                  BR-UK AI Advice Sessions
├── section-5.html                  Disclaimer & contact
├── assets/
│   ├── css/style.css
│   └── js/main.js
├── .nojekyll                       Tells GitHub Pages to skip Jekyll
└── README.md
```

Every page follows the same template: header nav, breadcrumb, content, prev/next pager, and footer. All assets are referenced with relative paths so the site works equally well at the domain root, on GitHub Pages (`/<repo>/`), or locally.

## Deploying to GitHub Pages

1. Create a new GitHub repository (e.g. `bruk-ai-repository`).
2. Push this directory to the repo:
   ```bash
   git init
   git add .
   git commit -m "Initial import of BR-UK AI Tools & Resources Repository"
   git branch -M main
   git remote add origin https://github.com/<your-user>/<repo-name>.git
   git push -u origin main
   ```
3. On GitHub, go to **Settings → Pages**.
4. Under **Build and deployment → Source**, choose **Deploy from a branch**, pick `main` and `/ (root)`, then save.
5. Wait a minute, then visit `https://<your-user>.github.io/<repo-name>/`.

The `.nojekyll` file prevents GitHub from processing the site through Jekyll — which is what you want here, since the site is plain HTML/CSS/JS and contains no Liquid templates.

## Local preview

Any static file server works. Easiest:

```bash
# From the project root
python3 -m http.server 8080
# then open http://localhost:8080
```

## Editing content

Each content page is self-contained HTML — no build step, no framework. To edit:

1. Open the relevant `.html` file.
2. Edit the content inside `<main>`. Keep the header/footer blocks consistent across pages.
3. For styling tweaks, edit `assets/css/style.css`.

Common tweaks:

- **Adding a new tool** to a stage → add a `.tool-card` block inside the `.tool-grid`.
- **Adding a new sub-section** to Section 1 or 2 → create a new HTML page (copy an existing one as a template) and add it to the section's `index.html` `subpage-list` plus the prev/next pagers on adjacent pages.
- **Changing the teal colour** → edit the `--teal-*` custom properties at the top of `style.css`.

## Content coverage

All pages from the original Usher Institute repository are mirrored, with every outbound hyperlink preserved. Sources reviewed:

- Main page
- Section 1 (Living Guide) + 5 stage sub-pages
- Section 2 (Ethics) + 5 topic sub-pages + 2 nested pages (Publishers, UK Funders)
- Sections 3, 4, 5
- BR-UK Statement

## Accessibility

- Semantic HTML (landmarks, headings, lists, breadcrumbs).
- Skip-to-content link on every page.
- Visible focus outlines, 4.5:1+ contrast for body text against backgrounds.
- Keyboard-navigable mobile menu.
- Respects `prefers-reduced-motion`.

## Browser support

Targeted at evergreen browsers: Chrome, Firefox, Safari, Edge (current releases). No polyfills or transpilation required.

## Licence

Content references and signposts resources created by third parties; consult each originator for their own licensing terms. This repository's structure and wording mirrors the publicly published BR-UK pages.
