# System Design Playbook

A single-page system design reference: a step-by-step design process, numbers worth knowing, core building blocks, 18 classic problems with sketch answers, AI-era systems, and current trends. It includes an interactive LRU vs LFU cache playground.

The site is plain HTML, CSS and JavaScript with no framework and no dependencies beyond Google Fonts.

## Features

- Collapsible topic cards with a progress checklist (saved in the browser)
- Topic filter
- Back-of-envelope estimation calculator
- LRU vs LFU playground with scenarios, step-through playback and manual requests
- Light and dark themes that follow the system setting

## Project structure

```
src/
  index.html      Playbook page source
  lru-lfu.html    LRU vs LFU playground source
scripts/
  build.py        Wraps each source page into a full HTML document in dist/
dist/             Build output (not committed)
```

## Develop

Requires Python 3.9 or newer.

```bash
make build    # writes dist/
make serve    # builds, then serves dist/ at http://localhost:8000
```

Without `make`:

```bash
python3 scripts/build.py
python3 -m http.server 8000 --directory dist
```

## Deploy

The `dist/` folder is a static site and works on any static host.

**Cloudflare Pages (direct upload):** Workers & Pages → Create → Pages → Upload assets, then drag in `dist/`. To update, open the project → Create new deployment and upload `dist/` again.

**Cloudflare Pages (connected to this repo):**

| Setting | Value |
|---|---|
| Build command | `python3 scripts/build.py` |
| Build output directory | `dist` |

## License

[MIT](LICENSE)
