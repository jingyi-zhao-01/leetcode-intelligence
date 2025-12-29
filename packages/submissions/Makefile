.PHONY: install dev dev-submission dev-analytics clean test prisma-generate

install:
	poetry install

dev-submission:
	PYTHONPATH=src:$$PYTHONPATH poetry run submission-server

dev-analytics:
	PYTHONPATH=src:$$PYTHONPATH poetry run analytics-server

dev:
	@echo "Two-server architecture:"
	@echo "  - Submission server (TCP): port 3000 - for nvim integration"
	@echo "  - Analytics server (HTTP): port 8000 - for data visualization"
	@echo ""
	@echo "Run 'make dev-submission' for submission server (port 3000)"
	@echo "Run 'make dev-analytics' for analytics server (port 8000)"

clean:
	rm -rf __pycache__
	rm -rf .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +

test:
	poetry run pytest

prisma-generate:
	poetry run prisma generate
