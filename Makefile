.PHONY: help install mcp submission analytics dev-mcp prod-mcp dev-submission prod-submission dev-analytics dev-frontend test prisma-generate prisma-db-push prisma-generate-dev prisma-generate-prod prisma-db-push-dev prisma-db-push-prod submission-stats clean

help:
	@echo "Available commands:"
	@echo "  make install              - Install all dependencies (uv sync + npm)"
	@echo "  make mcp [ENV=dev|prod]   - Start MCP server (default: dev)"
	@echo "  make submission [ENV=...] - Start Submission server"
	@echo "  make analytics [ENV=...]  - Start Analytics API"
	@echo "  make dev-mcp              - Alias for make mcp ENV=dev"
	@echo "  make prod-mcp             - Alias for make mcp ENV=prod"
	@echo "  make dev-frontend         - Start Next.js frontend"
	@echo "  make test                 - Run Python tests"
	@echo "  make prisma-generate      - Generate Prisma client for current ENV"
	@echo "  make prisma-db-push       - Push schema to current ENV DB"
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

# Default environment
ENV ?= dev

# Support for dev and prod as arguments (make mcp dev)
ifneq ($(filter dev,$(MAKECMDGOALS)),)
    ENV := dev
endif
ifneq ($(filter prod,$(MAKECMDGOALS)),)
    ENV := prod
endif

# Prevents make from complaining about dev and prod as missing targets
dev prod:
	@:

# Select database URL based on ENV
ifeq ($(ENV),prod)
CURRENT_DB_URL = $(PROD_DB_URL)
PRISMA_GEN_TARGET = prisma-generate-prod
else
CURRENT_DB_URL = $(DEV_DB_URL)
PRISMA_GEN_TARGET = prisma-generate-dev
endif

# --- Shared Command Definitions ---
PRISMA_RUN = uv run prisma
PRISMA_SCHEMA = --schema prisma/schema.prisma
SUB_ENV = PYTHONPATH=packages/submission_server/src:$$PYTHONPATH
MCP_RUN = uv run python packages/mcp-server/src/server.py

# --- Unified Execution Targets ---
mcp: $(PRISMA_GEN_TARGET)
	@echo "Starting MCP Server | Environment: $(ENV)" >&2
	@DATABASE_URL=$(CURRENT_DB_URL) $(MCP_RUN)

# Target specifically for stdio-based MCP servers (e.g. for VS Code config)
# Redirects all build/setup output to stderr to keep stdout clean for JSON-RPC
mcp-stdio: 
	@$(MAKE) $(PRISMA_GEN_TARGET) >&2
	@echo "Starting MCP Server (stdio) | Environment: $(ENV)" >&2
	@DATABASE_URL=$(CURRENT_DB_URL) uv run mcp-server-stdio

submission: $(PRISMA_GEN_TARGET)
	@echo "Starting Submission Server | Environment: $(ENV)" >&2
	@$(SUB_ENV) DATABASE_URL=$(CURRENT_DB_URL) uv run submission-server

analytics: $(PRISMA_GEN_TARGET)
	@echo "Starting Analytics API | Environment: $(ENV)" >&2
	@$(SUB_ENV) DATABASE_URL=$(CURRENT_DB_URL) uv run analytics-server

# --- Legacy/Convenience Aliases ---
dev-mcp:
	@$(MAKE) mcp ENV=dev
prod-mcp:
	@$(MAKE) mcp ENV=prod
dev-submission:
	@$(MAKE) submission ENV=dev
prod-submission:
	@$(MAKE) submission ENV=prod
dev-analytics:
	@$(MAKE) analytics ENV=dev

# --- Prisma Operations ---
prisma-generate:
	DATABASE_URL=$(CURRENT_DB_URL) $(PRISMA_RUN) generate $(PRISMA_SCHEMA)

prisma-db-push:
	DATABASE_URL=$(CURRENT_DB_URL) $(PRISMA_RUN) db push $(PRISMA_SCHEMA)

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
	@echo "Running Tests | Environment: dev"
	DATABASE_URL=$(DEV_DB_URL) uv run pytest

dev-frontend:
	@echo "Starting Frontend | Port: 3001"
	cd packages/graph-ui && PORT=3001 npm run dev

submission-stats: prisma-generate-dev
	@echo "Fetching Submission Stats | Environment: dev"
	$(SUB_ENV) uv run submission-stats

clean:
	rm -rf .venv __pycache__ .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	cd packages/graph-ui && rm -rf .next node_modules/.cache out
