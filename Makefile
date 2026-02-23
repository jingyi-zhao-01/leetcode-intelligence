.PHONY: help install dev-mcp prod-mcp dev-submission prod-submission dev-analytics dev-frontend test prisma-generate-dev prisma-generate-prod prisma-db-push-dev prisma-db-push-prod submission-stats clean

help:
	@echo "Available commands:"
	@echo "  make install              - Install all dependencies (uv sync + npm)"
	@echo "  make dev-mcp              - Start MCP server (DEV DB)"
	@echo "  make prod-mcp             - Start MCP server (PROD DB)"
	@echo "  make dev-submission       - Start Submission server (DEV DB)"
	@echo "  make prod-submission      - Start Submission server (PROD DB)"
	@echo "  make dev-analytics        - Start Analytics API (DEV DB)"
	@echo "  make dev-frontend         - Start Next.js frontend"
	@echo "  make test                 - Run Python tests"
	@echo "  make prisma-generate-dev  - Generate Prisma client (DEV DB)"
	@echo "  make prisma-generate-prod - Generate Prisma client (PROD DB)"
	@echo "  make prisma-db-push-dev   - Push schema to DEV DB"
	@echo "  make prisma-db-push-prod  - Push schema to PROD DB"
	@echo "  make submission-stats     - Show submission statistics"
	@echo "  make clean                - Remove build artifacts and caches"
	@echo ""
	@echo "Port allocation:"
	@echo "  - Port 3000: TCP submission server"
	@echo "  - Port 3001: Next.js frontend"
	@echo "  - Port 8000: Analytics API"

install:
	uv sync --dev
	cd packages/graph-ui && npm install

# Load environment variables from .env file
-include .env
export

# --- Shared Command Definitions ---
PRISMA_RUN = uv run prisma
PRISMA_SCHEMA = --schema prisma/schema.prisma
SUB_ENV = PYTHONPATH=packages/submission_server/src:$$PYTHONPATH
MCP_RUN = uv run python packages/mcp-server/src/server.py

# --- Development Environment ---
dev-mcp: prisma-generate-dev
	DATABASE_URL=$(DEV_DB_URL) $(MCP_RUN)

dev-submission: prisma-generate-dev
	$(SUB_ENV) DATABASE_URL=$(DEV_DB_URL) uv run submission-server

dev-analytics: prisma-generate-dev
	$(SUB_ENV) DATABASE_URL=$(DEV_DB_URL) uv run analytics-server

# --- Production Environment ---
prod-mcp: prisma-generate-prod
	DATABASE_URL=$(PROD_DB_URL) $(MCP_RUN)

prod-submission: prisma-generate-prod
	$(SUB_ENV) DATABASE_URL=$(PROD_DB_URL) uv run submission-server

# --- Prisma Operations ---
prisma-generate-dev:
	DATABASE_URL=$(DEV_DB_URL) $(PRISMA_RUN) generate $(PRISMA_SCHEMA)

prisma-generate-prod:
	DATABASE_URL=$(PROD_DB_URL) $(PRISMA_RUN) generate $(PRISMA_SCHEMA)

prisma-db-push-dev:
	DATABASE_URL=$(DEV_DB_URL) $(PRISMA_RUN) db push $(PRISMA_SCHEMA)

prisma-db-push-prod:
	DATABASE_URL=$(PROD_DB_URL) $(PRISMA_RUN) db push $(PRISMA_SCHEMA)

# --- Standard Targets ---
test: prisma-generate-dev
	DATABASE_URL=$(DEV_DB_URL) uv run pytest

dev-frontend:
	cd packages/graph-ui && PORT=3001 npm run dev

submission-stats: prisma-generate-dev
	$(SUB_ENV) uv run submission-stats

clean:
	rm -rf .venv __pycache__ .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	cd packages/graph-ui && rm -rf .next node_modules/.cache out
