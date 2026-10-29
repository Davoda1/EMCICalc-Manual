# EMCICalc Desktop 1.0.0 manual

[![Manual CI](https://github.com/Davoda1/EMCICalc-Manual/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/Davoda1/EMCICalc-Manual/actions/workflows/ci.yml)

The English user manual for [EMCICalc Desktop 1.0.0](https://github.com/Davoda1/EMCICalc), published as a static website with Gopher HTTP 3.0.0.

- `content/`: editable manual chapters, navigation and screenshots.
- `docs/`: generated static website, including local search and a site index.
- `vendor/gopher/`: the unchanged Gopher publisher and its MIT license.
- `tools/`: reproducible build, accessible screenshot overlays and bounded website validation.
- `manual-images.json` / `manual-annotations.json`: screenshot integrity and numbered callout descriptions.

## Build and preview

Requires Python 3.10 or newer and PHP CLI 8.2 or newer with the `ctype` extension. No Composer, Node package installation, database, CDN or webfont is needed to build or read the manual.

```sh
python3 tools/build.py
python3 tools/check_site.py
python3 -m http.server 8000 --directory docs
```

Open `http://127.0.0.1:8000/`. For another PHP installation, set `PHP_BIN` to the executable path or pass `--php /path/to/php` to the build script. Ordinary pages can also be opened from `docs/index.html`; local HTTP is recommended when checking search.

Edit `content/`, rebuild, and commit both authoring sources and generated `docs/` together. Keep images and all other runtime resources local. Preserve screenshot provenance and use factual captions. Do not edit generated HTML by hand.

## Validation and hosting

CI validates source privacy, local links, image assets, HTML structure and a reproducible Gopher build. It runs on pushes to `master`, pull requests and manual dispatch, with a five-minute limit.

`master` is the repository's sole branch. `docs/.nojekyll` is included for eventual GitHub Pages hosting from `master` / `docs`. The workflow does not enable Pages, deploy a website, change repository visibility or publish software releases.

The manual and original screenshots are MIT licensed; the vendored publisher retains its separate MIT notice in `vendor/gopher/LICENSE`. See `vendor/gopher/PROVENANCE.json` for the exact publisher hashes.
