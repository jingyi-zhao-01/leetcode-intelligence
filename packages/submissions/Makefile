.PHONY: install dev dev-api clean test prisma-generate

install:
	poetry install

dev:
	poetry run submission-server

dev-api:
	PYTHONPATH=src:$$PYTHONPATH poetry run uvicorn api_server:app --reload --host 0.0.0.0 --port 8000

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +

test:
	poetry run pytest

prisma-generate:
	poetry run prisma generate
