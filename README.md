# System Design Playbook

A single-page system design reference: a step-by-step design process, estimation rules of thumb, core building blocks, 16 classic problems with sketch answers, ML and LLM systems, and architecture patterns. It includes an interactive LRU vs LFU cache playground.

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

The site is hosted on Cloudflare Pages. The project name in [`wrangler.toml`](wrangler.toml) sets the address (`<name>.pages.dev`); the Makefile and the deploy workflow both read it from there.

### From your computer

Requires Node.js 18 or newer (for `npx wrangler`).

```bash
npx --yes wrangler@4.149.0 login   # one time: opens the browser to sign in to Cloudflare
make deploy                        # builds, then publishes to <name>.pages.dev
make deploy-preview                # publishes to a separate preview URL instead
```

The first `make deploy` asks to create the Pages project if it doesn't exist yet.

### Automatically on every push to `main`

[`.github/workflows/deploy.yml`](.github/workflows/deploy.yml) builds and deploys on each push to `main`, and can be run by hand from the Actions tab. One-time setup:

1. In Cloudflare, create an API token: My Profile → API Tokens → Create Token → **Edit Cloudflare Workers** template (or a custom token with **Account → Cloudflare Pages → Edit**).
2. Copy your **Account ID** from the Cloudflare dashboard (Workers & Pages overview, right side).
3. In this GitHub repo: Settings → Secrets and variables → Actions → add `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID`.
4. Create the project once with `make deploy`, or let the first workflow run create it.

### Without any tooling

Run `make build`, then in Cloudflare go to Workers & Pages → Create → Pages → Upload assets and drag in `dist/`.

### Changing the address

- **Custom domain:** in the Pages project, open Custom domains and add your domain. You can do this at any time without redeploying.
- **Different `pages.dev` name:** a project can't be renamed. Change `name` in `wrangler.toml`, run `make deploy` to create the new project, then delete the old one in the dashboard.

## License

[MIT](LICENSE)
