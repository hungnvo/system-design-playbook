.PHONY: build serve clean

PORT ?= 8000

build:
	python3 scripts/build.py

serve: build
	python3 -m http.server $(PORT) --directory dist

clean:
	rm -rf dist
