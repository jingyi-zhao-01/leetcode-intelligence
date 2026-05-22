.PHONY: help install mcp mcp-stdio submission analytics dev-mcp prod-mcp dev-submission prod-submission dev-analytics dev-frontend test prisma-generate prisma-db-push prisma-generate-dev prisma-generate-prod prisma-db-push-dev prisma-db-push-prod submission-stats compose-build compose-up compose-down compose-logs compose-ps clean

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
	@echo "  make compose-build        - [Docker target] Build Docker Compose images"
	@echo "  make compose-up [ENV=...] - [Docker target] Start Compose stack (submission + mcp)"
	@echo "  make compose-down         - [Docker target] Stop and remove Compose stack"
	@echo "  make compose-logs         - [Docker target] Tail logs for Compose services"
	@echo "  make compose-ps           - [Docker target] Show Compose service status"
	@echo "  make clean                - Remove build artifacts and caches"
	@echo ""
	@echo "Port allocation:"
	@echo "  - Port 3000: TCP submission server"
	@echo "  - Port 3001: Next.js frontend"
	@echo "  - Port 8000: Analytics API"

install:
	uv sync --dev
	cd services/submission-server && npm install
	cd services/mcp-server && npm install
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
PRISMA_SCHEMA = --schema services/prisma/schema.prisma
SUB_ENV = PYTHONPATH=services/submission-server/src:$$PYTHONPATH
MCP_NPM = cd services/mcp-server &&
SUB_NPM = cd services/submission-server &&

# --- Unified Execution Targets ---
mcp: $(PRISMA_GEN_TARGET)
	@echo "Starting MCP Server | Environment: $(ENV)" >&2
	@$(MCP_NPM) DATABASE_URL=$(CURRENT_DB_URL) npm run mcp-server

# Target specifically for stdio-based MCP servers (e.g. for VS Code config)
# Redirects all build/setup output to stderr to keep stdout clean for JSON-RPC
mcp-stdio: 
	@$(MAKE) $(PRISMA_GEN_TARGET) >&2
	@echo "Starting MCP Server (stdio) | Environment: $(ENV)" >&2
	@$(MCP_NPM) DATABASE_URL=$(CURRENT_DB_URL) npm run --silent mcp-server-stdio

submission: $(PRISMA_GEN_TARGET)
	@echo "Starting Submission Server | Environment: $(ENV)" >&2
	@$(SUB_NPM) DATABASE_URL=$(CURRENT_DB_URL) npm run submission-server

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

# --- Docker Targets ---
# Docker target: build all service images defined in docker-compose.yml
compose-build:
	@echo "Building Compose images | Environment: $(ENV)" >&2
	@DATABASE_URL=$(CURRENT_DB_URL) docker compose build

# Docker target: start submission_server and mcp_server in detached mode
compose-up:
	@echo "Starting Compose stack | Environment: $(ENV)" >&2
	@DATABASE_URL=$(CURRENT_DB_URL) docker compose up -d

# Docker target: stop and remove services, network, and compose resources
compose-down:
	@DATABASE_URL=$(CURRENT_DB_URL) docker compose down

# Docker target: stream recent logs from submission_server and mcp_server
compose-logs:
	@DATABASE_URL=$(CURRENT_DB_URL) docker compose logs -f submission_server mcp_server

# Docker target: show runtime status for compose services
compose-ps:
	@DATABASE_URL=$(CURRENT_DB_URL) docker compose ps

clean:
	rm -rf .venv __pycache__ .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	cd packages/graph-ui && rm -rf .next node_modules/.cache out
