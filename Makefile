.PHONY: help install mcp mcp-stdio submission analytics dev-mcp prod-mcp dev-submission prod-submission dev-analytics dev-frontend test prisma-generate prisma-db-push prisma-db-pull submission-stats compose-build compose-up compose-down compose-logs compose-ps clean

help:
	@echo "Available commands:"
	@echo "  make install              - Install all dependencies (uv sync + npm)"
	@echo "  make mcp                  - Start MCP server"
	@echo "  make submission           - Start Submission server"
	@echo "  make analytics            - Start Analytics API"
	@echo "  make dev-mcp              - Alias for make mcp"
	@echo "  make prod-mcp             - Alias for make mcp"
	@echo "  make dev-frontend         - Start Next.js frontend"
	@echo "  make test                 - Run Python tests"
	@echo "  make prisma-generate      - Generate Prisma JS client with DATABASE_URL"
	@echo "  make prisma-db-push       - Push schema with DATABASE_URL"
	@echo "  make prisma-db-pull       - Pull schema from database with DATABASE_URL"
	@echo "  make submission-stats     - Show submission statistics"
	@echo "  make compose-build        - [Docker target] Build Docker Compose images"
	@echo "  make compose-up           - [Docker target] Start Compose stack (submission + mcp)"
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
	npm install

# Load environment variables from .env file
-include .env
export

# --- Shared Command Definitions ---
PRISMA_RUN_JS = npm exec prisma --
PRISMA_SCHEMA = --schema services/shared/prisma/schema.prisma
SUB_ENV = PYTHONPATH=services/leetcode-submission-service/src:$$PYTHONPATH

# --- Unified Execution Targets ---
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

# --- Prisma Operations --------------------------------------------------------------------------------------------------
prisma-generate:
	DATABASE_URL=$(DATABASE_URL) $(PRISMA_RUN_JS) generate --generator jsclient $(PRISMA_SCHEMA)

# prisma-db-push:
# 	DATABASE_URL=$(DATABASE_URL) $(PRISMA_RUN_JS) db push $(PRISMA_SCHEMA)

prisma-db-pull:
	DATABASE_URL=$(DATABASE_URL) $(PRISMA_RUN_JS) db pull $(PRISMA_SCHEMA)

# --- Standard Targets --------------------------------------------------
test:
	@echo "Running Tests"
	DATABASE_URL=$(DATABASE_URL) uv run pytest

dev-frontend:
	@echo "Starting Frontend | Port: 3001"
	cd packages/graph-ui && PORT=3001 npm run dev

submission-stats:
	@echo "Fetching Submission Stats"
	$(SUB_ENV) DATABASE_URL=$(DATABASE_URL) uv run submission-stats



# --- Docker Targets --------------------------------------------------------------------------------------------------
# Docker target: build all service images defined in docker-compose.yml
compose-build:
	@echo "Building Compose images" >&2
	@DATABASE_URL=$(DATABASE_URL) docker compose build

# Docker target: start submission_server and mcp_server in detached mode
compose-up:
	@echo "Starting Compose stack" >&2
	@DATABASE_URL=$(DATABASE_URL) docker compose up -d

# Docker target: stop and remove services, network, and compose resources
compose-down:
	@DATABASE_URL=$(DATABASE_URL) docker compose down

# Docker target: stream recent logs from submission_server and mcp_server
compose-logs:
	@DATABASE_URL=$(DATABASE_URL) docker compose logs -f submission_server mcp_server

# Docker target: show runtime status for compose services
compose-ps:
	@DATABASE_URL=$(DATABASE_URL) docker compose ps

clean:
	rm -rf .venv __pycache__ .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	cd packages/graph-ui && rm -rf .next node_modules/.cache out
