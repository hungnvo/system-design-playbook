.PHONY: build serve clean deploy deploy-preview

PORT ?= 8000
PROJECT ?= $(shell sed -n 's/^name = "\(.*\)"/\1/p' wrangler.toml)
WRANGLER ?= npx --yes wrangler@4.149.0

build:
	python3 scripts/build.py

serve: build
	python3 -m http.server $(PORT) --directory dist

clean:
	rm -rf dist

# Publish dist/ to the production URL (https://$(PROJECT).pages.dev).
deploy: build
	$(WRANGLER) pages deploy dist --project-name $(PROJECT) --branch main

# Publish to a separate preview URL without touching production.
deploy-preview: build
	$(WRANGLER) pages deploy dist --project-name $(PROJECT) --branch preview
