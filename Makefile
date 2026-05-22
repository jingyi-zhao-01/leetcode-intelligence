.PHONY: help install mcp mcp-stdio submission analytics dev-mcp prod-mcp dev-submission prod-submission dev-analytics dev-frontend test prisma-generate prisma-db-push prisma-db-pull submission-stats submission-image-start submission-image-stop clean

help:
	@echo "Available commands:"
	@echo ""
	@echo "Prisma"
	@echo "  make prisma-generate        - Generate Prisma JS client with DATABASE_URL"
	@echo "  make prisma-db-push         - Push schema with DATABASE_URL"
	@echo "  make prisma-db-pull         - Pull schema from database with DATABASE_URL"
	@echo ""
	@echo "Local Run"
	@echo "  make mcp                    - Start MCP server"
	@echo "  make mcp-stdio              - Start MCP server in stdio mode"
	@echo "  make submission             - Start Submission server"
	@echo "  make dev-mcp                - Alias for make mcp"
	@echo "  make prod-mcp               - Alias for make mcp"
	@echo "  make analytics              - Start Analytics API"
	@echo "  make dev-frontend           - Start Next.js frontend"
	@echo "  make submission-stats       - Show submission statistics"
	@echo "  make test                   - Run Python tests"
	@echo ""
	@echo "Image Run"
	@echo "  make submission-image-start   - Start submission server from Docker image"
	@echo "  make submission-image-stop    - Stop submission server Docker container"
	@echo ""
	@echo "Other"
	@echo "  make install                - Install all dependencies (uv sync + npm)"
	@echo "  make clean                  - Remove build artifacts and caches"
	@echo ""
	@echo "Port allocation:"
	@echo "  - Port 3000: TCP submission server"
	@echo "  - Port 3001: Next.js frontend"
	@echo "  - Port 8000: Analytics API"

install:
	uv sync --dev
	npm install

# Load environment variables from .env file
-include .env
export

# --- Shared Command Definitions ---
PRISMA_RUN_JS = npm exec prisma --
PRISMA_SCHEMA = --schema services/shared/prisma/schema.prisma
SUB_ENV = PYTHONPATH=services/leetcode-submission-service/src:$$PYTHONPATH

# --- Prisma Targets ---
prisma-generate:
	DATABASE_URL=$(DATABASE_URL) $(PRISMA_RUN_JS) generate --generator jsclient $(PRISMA_SCHEMA)

prisma-db-push:
	DATABASE_URL=$(DATABASE_URL) $(PRISMA_RUN_JS) db push $(PRISMA_SCHEMA)

prisma-db-pull:
	DATABASE_URL=$(DATABASE_URL) $(PRISMA_RUN_JS) db pull $(PRISMA_SCHEMA)

# --- Local Run Targets ---
mcp: prisma-generate
	@echo "Starting MCP Server" >&2
	@DATABASE_URL=$(DATABASE_URL) npm run --workspace services/leetcode-mcp-service mcp-server

# Target specifically for stdio-based MCP servers (e.g. for VS Code config)
# Redirects all build/setup output to stderr to keep stdout clean for JSON-RPC
mcp-stdio:
	@$(MAKE) prisma-generate >&2
	@echo "Starting MCP Server (stdio)" >&2
	@DATABASE_URL=$(DATABASE_URL) npm run --workspace services/leetcode-mcp-service --silent mcp-server-stdio

submission: prisma-generate
	@echo "Starting Submission Server" >&2
	@DATABASE_URL=$(DATABASE_URL) npm run --workspace services/leetcode-submission-service submission-server

test:
	@echo "Running Tests"
	DATABASE_URL=$(DATABASE_URL) uv run pytest

dev-frontend:
	@echo "Starting Frontend | Port: 3001"
	cd packages/graph-ui && PORT=3001 npm run dev

submission-stats:
	@echo "Fetching Submission Stats"
	$(SUB_ENV) DATABASE_URL=$(DATABASE_URL) uv run submission-stats

# --- Image Run Targets ---
submission-image-start:
	@$(MAKE) -C docker submission-image-start

submission-image-stop:
	@$(MAKE) -C docker submission-image-stop

clean:
	rm -rf .venv __pycache__ .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	cd packages/graph-ui && rm -rf .next node_modules/.cache out
