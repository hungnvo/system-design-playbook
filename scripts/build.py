"""Build the static site from the page sources.

Usage: python3 scripts/build.py  ->  writes each page in PAGES to dist/

Each file in src/ is a page fragment (title, styles, markup, script) without
<html>/<head>/<body>. This script wraps each one into a full HTML document so
any static host can serve the dist/ folder as-is.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "src"
OUT = ROOT / "dist"

PAGES = ["index.html", "lru-lfu.html", "consistent-hashing.html"]

HEAD = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<style>
:root { padding-top: env(safe-area-inset-top, 0px); padding-bottom: env(safe-area-inset-bottom, 0px); }
body { margin: 0; }
img { max-width: 100%; }
[hidden] { display: none !important; }
</style>
"""

BACK_LINK = (
    '<a href="index.html" style="font:500 13px var(--f-body);color:var(--accent);'
    'text-decoration:none">← System Design Playbook</a>\n    '
)


def wrap(source: str) -> str:
    # Sources start with <title>/<meta>/<link>/<style>; the first <div is the page body.
    split = source.index("<div")
    return HEAD + source[:split] + "</head>\n<body>\n" + source[split:] + "\n</body>\n</html>\n"


def main() -> None:
    OUT.mkdir(exist_ok=True)
    for name in PAGES:
        html = (SRC / name).read_text(encoding="utf-8")
        if name != "index.html":
            # Playgrounds get a link back to the playbook above their header label
            html = html.replace('<span class="label">', BACK_LINK + '<span class="label">', 1)
        (OUT / name).write_text(wrap(html), encoding="utf-8")
        print(f"wrote dist/{name}")


if __name__ == "__main__":
    main()
