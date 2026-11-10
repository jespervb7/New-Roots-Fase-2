# social-cards

Cache folder of the social plugin (`cache_dir` under `[project.plugins.social]` in `zensical.toml`), which makes the share cards: the preview images shown when a page link is shared in WhatsApp, Signal, email, etc.

- `fonts/Roboto/` — **committed on purpose.** The plugin would otherwise download Roboto from Google Fonts on every fresh build. That download fails on PCs whose antivirus scans HTTPS traffic (e.g. Norton), which breaks the build. With the fonts here, no build needs to download anything. Roboto is licensed under the SIL Open Font License (`OFL.txt`).
- `background.webp` — the picture behind every card (artist impression of the building). It is set as `background_image` in `cards_layout_options`; `background_color` (`#1f4d3a99`, dark green at 60% opacity) is laid over it so the white text stays readable. Use a lower opacity (e.g. `80` instead of `99`) to show more of the picture, or a higher one (`bf` = 75%) for more contrast.
- `cards/` — generated card images. Not committed (see `.gitignore`).

The cards use `Roboto-Regular.ttf` and `Roboto-Bold.ttf`. If you change `font_family` in `cards_layout_options`, put that font's `.ttf` files in `fonts/<Family>/` too.
