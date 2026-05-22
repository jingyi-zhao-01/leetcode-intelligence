.PHONY: help install mcp mcp-stdio submission intelligence analytics dev-mcp prod-mcp dev-submission prod-submission dev-analytics dev-frontend test prisma-generate prisma-db-push prisma-db-pull submission-stats submission-image-start submission-image-stop intelligence-image-start intelligence-image-stop compose-build compose-up compose-down compose-logs compose-ps clean

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
	@echo "  make intelligence           - Start Intelligence CLI client"
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
	@echo "  make intelligence-image-start - Start intelligence service from Docker image"
	@echo "  make intelligence-image-stop  - Stop intelligence service Docker container"
	@echo "  make compose-build            - Build Docker Compose images"
	@echo "  make compose-up               - Start Compose stack (submission + mcp)"
	@echo "  make compose-down             - Stop and remove Compose stack"
	@echo "  make compose-logs             - Tail logs for Compose services"
	@echo "  make compose-ps               - Show Compose service status"
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
SUBMISSION_IMAGE ?= leetcode-submission-service:latest
SUBMISSION_CONTAINER_NAME ?= leetcode-submission-service
SUBMISSION_HOST_PORT ?= 3000
INTELLIGENCE_IMAGE ?= leetcode-intelligence-service:latest
INTELLIGENCE_CONTAINER_NAME ?= leetcode-intelligence-service
INTELLIGENCE_HOST_PORT ?= 8030

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

intelligence: prisma-generate
	@echo "Starting Intelligence CLI Client" >&2
	@DATABASE_URL=$(DATABASE_URL) \
		OPEN_ROUTER_API_KEY=$(OPEN_ROUTER_API_KEY) \
		MODEL=$(MODEL) \
		npm run --workspace services/leetcode-intelligence-service intelligence-cli

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
	@echo "Starting submission server from image $(SUBMISSION_IMAGE) on port $(SUBMISSION_HOST_PORT)" >&2
	@docker rm -f $(SUBMISSION_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker run --rm --name $(SUBMISSION_CONTAINER_NAME) -p $(SUBMISSION_HOST_PORT):3000 \
		-e DATABASE_URL=$(DATABASE_URL) \
		$(SUBMISSION_IMAGE)

submission-image-stop:
	@echo "Stopping submission server container $(SUBMISSION_CONTAINER_NAME)" >&2
	@docker rm -f $(SUBMISSION_CONTAINER_NAME) >/dev/null 2>&1 || true

intelligence-image-start:
	@echo "Starting intelligence service from image $(INTELLIGENCE_IMAGE) on port $(INTELLIGENCE_HOST_PORT)" >&2
	@docker rm -f $(INTELLIGENCE_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker run --rm --name $(INTELLIGENCE_CONTAINER_NAME) -p $(INTELLIGENCE_HOST_PORT):8030 \
		-e DATABASE_URL=$(DATABASE_URL) \
		-e OPEN_ROUTER_API_KEY=$(OPEN_ROUTER_API_KEY) \
		-e API_KEY=$(API_KEY) \
		-e MODEL=$(MODEL) \
		-e DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		-e DISCORD_CHANNEL_ID=$(DISCORD_CHANNEL_ID) \
		$(INTELLIGENCE_IMAGE)

intelligence-image-stop:
	@echo "Stopping intelligence service container $(INTELLIGENCE_CONTAINER_NAME)" >&2
	@docker rm -f $(INTELLIGENCE_CONTAINER_NAME) >/dev/null 2>&1 || true

# --- Compose Targets ---
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
