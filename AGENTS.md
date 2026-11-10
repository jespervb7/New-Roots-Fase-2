# AGENTS.md

Instructions for AI coding agents working in this repository.

## What this project is

A documentation website for residents of **New Roots Fase 2**, an apartment complex in Utrecht. The site gathers and combines everything that is useful to know when living there: how-to guides for appliances and installations (e.g. the WTW/ventilation unit), contact details for the VvE, property manager and contractors, practical tips (parking, locks, waste), and checklists such as moving in.

The audience is **residents, not developers**. Every page should be understandable by someone with no technical background who just wants to get something done at home.

The site is built with [Zensical](https://zensical.org/docs/) and published publicly to GitHub Pages.

## Repository layout

| Path | Purpose |
| --- | --- |
| `docs/` | Source Markdown pages: `index.md` (home) plus one folder per tab (`mijn-woning/`, `gebouw-en-omgeving/`, `verhuizen/`, `vve-en-contact/`, `bijdragen/`), each with an `index.md` landing page. |
| `docs/images/<page-name>/` | Screenshots and images used by a specific page (one subfolder per page). |
| `docs/assets/` | Downloadable files such as manuals and PDFs, and site-wide assets. |
| `docs/gebouw-en-omgeving/openstaande-punten.md` | Open issues in the complex that may later become pages. |
| `zensical.toml` | Site config: name, `nav`, theme, and enabled Markdown extensions. |
| `includes/afkortingen.md` | Site-wide glossary of abbreviations, auto-appended to every page (see `includes/README.md`). |
| `overrides/main.html` | Theme override (`custom_dir`). Renders the announcement bar from `[project.extra.announcement]` in `zensical.toml`. |
| `site/` | Generated build output. Never edit by hand; it is not committed. |
| `.github/workflows/docs.yml` | Builds and deploys the site to GitHub Pages on push to `main`. |

## Commands

Use `uv` so tooling matches the lockfile:

```sh
uv sync --group dev              # install zensical + pre-commit
uv run pre-commit install        # enable the strict-build hook
uv run zensical serve --open     # live preview at http://localhost:8000
uv run zensical build --clean --strict   # authoritative validation
```

There are no unit tests or linters. **A passing `uv run zensical build --clean --strict` is the definition of done** for any change to `docs/` or `zensical.toml`. Fix every warning; the build is strict on purpose (broken links, missing images, etc.).

## Writing content

### Language and tone
- The site content is primarily **Dutch**. Write new pages in Dutch unless asked otherwise, and keep the language of an existing page consistent when editing it.
- Write for residents: short sentences, concrete steps, no jargon. Explain technical terms the first time (e.g. "WTW-unit (warmteterugwinning, het ventilatiesysteem)").
- **Abbreviations** (VvE, WTW, HRU, …): when a page uses an abbreviation that is not yet in `includes/afkortingen.md`, add it there (`*[AFK]: Uitleg`, alphabetical, plain Dutch). It then gets a tooltip on every page automatically; do not define abbreviations inside individual pages.
- Lead with the answer or action; put background and details after.

### Page structure
- Every page starts with a single `# Title`.
- Add front matter with at least `title` and `description`; use `status: new` for freshly added pages and give content pages 1–3 `tags`:
  ```yaml
  ---
  title: Hoe vervang ik mijn luchtfilters?
  description: Waar je luchtfilters koopt, welke je nodig hebt en hoe je ze plaatst.
  status: new
  tags:
    - Ventilatie
    - Onderhoud
  ---
  ```
- **Tags** group pages by topic across tabs; they appear as chips on the page and on the overview `docs/tags.md` ("Onderwerpen A-Z"). Only tags listed in `tags_allowed` under `[project.plugins.tags]` in `zensical.toml` are accepted: the build fails on any other tag. Reuse existing tags; add a new one to `tags_allowed` (alphabetical, Dutch, capitalised) only for a real new topic. Landing pages (`index.md`) don't get tags.
- For how-to pages, follow the pattern of `docs/mijn-woning/luchtfilters-vervangen.md`: a tip/summary at the top, numbered or clearly headed steps with screenshots, then a `FAQ` section.
- Use Zensical features where they help readability: admonitions (`!!! tip`, `!!! warning`) for important notes, collapsible `???` blocks for FAQs, task lists for checklists, buttons (`{ .md-button }`) for primary links. See `docs/bijdragen/markdown.md` and `docs/bijdragen/opmaakvoorbeelden.md` for examples of the enabled extensions.
- Prefer one topic per page. If information relates to an existing page, extend that page instead of creating a near-duplicate, and cross-link related pages.

### Sources and reliability
- Cite the source of factual information (official manual, VvE announcement, municipality page, supplier) with a link.
- When linking to an external manual or PDF that might disappear, also store a copy in `docs/assets/` and link to both (as done for the HRU ECO 200 manual).
- Clearly mark uncertain or resident-derived information (e.g. "Dit lijkt te werken, maar is niet officieel bevestigd") instead of presenting it as fact.
- Do not invent phone numbers, email addresses, prices, opening hours, or procedures. If something is unknown, leave a clear placeholder or ask the user.

### Privacy and safety (the site is public)
- Never publish personal data of individual residents: no names tied to apartment numbers, private phone numbers, personal email addresses, or photos showing people or identifiable home interiors without consent.
- Business/organisation contacts (VvE mailbox, property manager, contractors) are fine.
- Do not publish access codes, alarm/door codes, Wi-Fi passwords, key/cylinder numbers, or anything that would weaken building security.
- Do not commit secrets or private share links (e.g. private Power BI or Google Drive links).

## Files, images, and navigation

- **New pages**: create them in the folder of the tab they belong to (e.g. `docs/gebouw-en-omgeving/afval-scheiden.md`) with lowercase, hyphenated filenames, and link them from that tab's `index.md`. If a page moves, update all links, `nav`, and the URLs in `.github/ISSUE_TEMPLATE/config.yml`.
- **Navigation**: every page that should be visible must be added to the `nav` array in `zensical.toml`, with a clear Dutch label. Each top-level `nav` entry is a tab (`navigation.tabs`); its first item is the folder's `index.md` landing page. Add pages to an existing tab rather than creating new tabs; group related pages under a sub-section (like `Installaties` under `Mijn woning`). When a planned topic on a landing page's "Nog geen pagina" list gets its own page, move it into the page list.
- **Images**: put them in `docs/images/<page-name>/` with descriptive filenames (`step1_navigate_to_filters.png`), and always provide alt text: `![Itho webshop keuzewijzer](../images/...)` (pages sit one folder deep, so use `../images/` and `../assets/`).
- **Downloads/manuals**: put them in `docs/assets/`.
- Use relative links between pages (`[contactgegevens](../vve-en-contact/contactgegevens.md)`). Paths with spaces must be URL-encoded (`%20`) in links.
- Keep files reasonably small; compress large screenshots before adding them.

## Configuration changes

- Make all site configuration changes in `zensical.toml`. Do not introduce another docs generator (MkDocs, Docusaurus, etc.) or a custom build script.
- Only enable a Markdown extension or theme feature if a page actually uses it, and validate with a strict build afterward.
- Keep `.github/workflows/docs.yml` and the pre-commit hook in line with any change to the build command.
- **Announcement bar**: to post or change a notice (e.g. maintenance, a VvE meeting), edit `text`, `link`, `link_text` and `until` under `[project.extra.announcement]` in `zensical.toml`; set `text = ""` to remove it. Always set `until` (YYYY-MM-DD) so old notices disappear on their own. Keep it to one short Dutch sentence and do not put personal data or codes in it. Only change `overrides/main.html` to change how the bar looks.
- **"Laatst geüpdatet" dates**: every page has `revision_date: "10 november 2026"` (Dutch format) in its front matter, which Zensical shows at the bottom of the page. It must equal the date of the last commit that changed the page.
  - The `revision-date` pre-commit hook (`scripts/revision_dates.py update`) sets it to today on every changed page. When it changes a file the commit stops; `git add` the page and commit again.
  - On pull requests, `.github/workflows/check-revision-dates.yml` runs `scripts/revision_dates.py check` and fails if a changed page's date doesn't match its last commit.
  - When you edit a page, update `revision_date` to today yourself if the hook isn't installed. New pages get the field from the hook; `scripts/revision_dates.py backfill` fills it for pages that lack it.

## Before you finish

1. `uv run zensical build --clean --strict` passes without warnings.
2. New or moved pages are in `nav`, and all internal links and images resolve.
3. No personal resident data, codes, or secrets were added.
4. Content is in Dutch (or matches the existing page), sourced, and written for residents.
5. Don't commit `site/`, `.venv/`, or `.cache/`.
