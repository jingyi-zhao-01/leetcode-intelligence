.PHONY: help install run-mcp-server run-submission-server dev-analytics dev-frontend test prisma-generate submission-stats clean

help:
	@echo "Available commands:"
	@echo "  make install              - Install all dependencies (uv sync + npm)"
	@echo "  make run-mcp-server       - Start MCP server (stdio, for Copilot/editors)"
	@echo "  make run-submission-server- Start TCP submission server on port 3000 (for nvim)"
	@echo "  make dev-analytics        - Start Analytics API on port 8000"
	@echo "  make dev-frontend         - Start Next.js frontend on port 3001"
	@echo "  make test                 - Run Python tests"
	@echo "  make prisma-generate      - Generate Prisma client"
	@echo "  make submission-stats     - Show submission statistics"
	@echo "  make clean                - Remove build artifacts and caches"
	@echo ""
	@echo "Port allocation:"
	@echo "  - Port 3000: TCP submission server (for nvim)"
	@echo "  - Port 3001: Next.js frontend (web UI)"
	@echo "  - Port 8000: Analytics API (HTTP/REST)"

install:
	uv sync --dev
	cd packages/graph-ui && npm install

run-mcp-server:
	uv run mcp-server-stdio

run-submission-server:
	PYTHONPATH=packages/submissions/src:$$PYTHONPATH uv run submission-server

dev-analytics:
	PYTHONPATH=packages/submissions/src:$$PYTHONPATH uv run analytics-server

dev-frontend:
	cd packages/graph-ui && PORT=3001 npm run dev

test:
	uv run pytest

prisma-generate:
	uv run prisma generate --schema prisma/schema.prisma

submission-stats:
	PYTHONPATH=packages/submissions/src:$$PYTHONPATH uv run submission-stats

clean:
	rm -rf .venv __pycache__ .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	cd packages/graph-ui && rm -rf .next node_modules/.cache out
