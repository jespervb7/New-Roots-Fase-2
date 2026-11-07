# Copilot instructions for New-Roots-Fase-2

## Project shape

This repository is a static documentation site powered by Zensical. The source of truth for pages is `docs/`, while `zensical.toml` defines the site metadata, navigation, theme, and Markdown extensions. The generated static output is written to `site/` and is published via GitHub Pages.

## Build, validation, and local workflow

Use the repo's `uv` environment for local commands:

- Install the dev tooling and enable the pre-commit hook:
  - `uv sync --group dev`
  - `uv run pre-commit install`
- Run the strict documentation build locally:
  - `uv run zensical build --strict`
- Regenerate from scratch when needed:
  - `uv run zensical build --clean --strict`

The repository does not currently define a separate unit-test or lint suite. The authoritative validation step here is the Zensical build, and the pre-commit hook enforces the same strict build when docs or build config files change.

## Architecture

- `docs/` contains authored Markdown pages that become the website content.
- `zensical.toml` is the configuration center for site metadata, navigation, theme, and Markdown extensions.
- `site/` is generated output and should not be edited by hand; rebuild it instead.
- `.github/workflows/docs.yml` deploys the built site to GitHub Pages using `zensical build --clean`.
- `main.py` is currently just a placeholder and does not drive the site build.

## Conventions specific to this repo

- Treat `docs/*.md` as the source for user-facing documentation; avoid duplicating content into generated output.
- If you add or move a page, update the `nav` array in `zensical.toml` so the docs navigation stays in sync.
- Keep configuration changes consistent with the existing Zensical setup instead of introducing a second docs tool or custom build path.
- Prefer `uv run ...` commands so the environment stays aligned with the lockfile and dev dependencies.
- When a change affects docs or build settings, validate with the strict Zensical build before considering it complete.
