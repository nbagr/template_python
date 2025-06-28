install:
	uv sync

run:
	uv run template-code

test:
	uv run pytest

lint:
	uv run ruff check

check: test lint

build:
	uv build
