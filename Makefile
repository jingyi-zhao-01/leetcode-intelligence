.PHONY: help install mcp submission analytics test prisma-generate prisma-db-push prisma-generate-prod prisma-db-push-prod submission-stats clean prisma-pull

help:
	@echo "Available commands:"
	@echo "  make install              - Install all dependencies (uv sync + npm)"
	@echo "  make mcp                 - Start MCP server"
	@echo "  make submission          - Start Submission server"
	@echo "  make analytics           - Start Analytics API"
	@echo "  make test                - Run Python tests"
	@echo "  make prisma-generate     - Generate Prisma client"
	@echo "  make prisma-db-push      - Push schema to DB"
	@echo "  make submission-stats    - Show submission statistics"
	@echo "  make clean               - Remove build artifacts and caches"
	@echo "  make prisma-pull         - Pull schema from DB"
	@echo ""
	@echo "Port allocation:"
	@echo "  - Port 3000: TCP submission server"
	@echo "  - Port 3001: Next.js frontend"
	@echo "  - Port 8000: Analytics API"

install:
	uv sync
	cd packages/graph-ui && npm install


clean:
	rm -rf .venv __pycache__ .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	cd packages/graph-ui && rm -rf .next node_modules/.cache out


# Load environment variables from .env file
-include .env
export



# Prisma
CURRENT_DB_URL = $(or $(DATABASE_URL),$(PROD_DB_URL),$(DEV_DB_URL))
CURRENT_DB_URL_CLEAN = $(patsubst "%",%,$(strip $(CURRENT_DB_URL)))

PRISMA_RUN = uv run prisma
PRISMA_SCHEMA = --schema microservices/shared/prisma/schema.prisma
MCP_RUN = uv run python microservices/mcp-server/src/server.py


prisma-pull:
	@if [ -z "$(CURRENT_DB_URL_CLEAN)" ]; then \
	  echo "Error: Set DATABASE_URL (or PROD_DB_URL/DEV_DB_URL) in .env"; exit 1; \
	fi
	DATABASE_URL="$(CURRENT_DB_URL_CLEAN)" $(PRISMA_RUN) db pull $(PRISMA_SCHEMA)


prisma-generate:
	DATABASE_URL="$(CURRENT_DB_URL_CLEAN)" $(PRISMA_RUN) generate $(PRISMA_SCHEMA)



# prisma-db-push:
# 	DATABASE_URL="$(CURRENT_DB_URL_CLEAN)" $(PRISMA_RUN) db push $(PRISMA_SCHEMA)





#----------------------------------------

mcp: prisma-generate
	@echo "Starting MCP Server" >&2
	@DATABASE_URL="$(CURRENT_DB_URL_CLEAN)" $(MCP_RUN)

submission: prisma-generate
	@echo "Starting Submission Server" >&2
	@DATABASE_URL="$(CURRENT_DB_URL_CLEAN)" uv run python microservices/submission-server/src/submission_server.py

analytics: prisma-generate
	@echo "Starting Analytics API" >&2
	@DATABASE_URL="$(CURRENT_DB_URL_CLEAN)" uv run analytics-server


submission-stats: prisma-generate
	@echo "Fetching Submission Stats"
	uv run submission-stats



