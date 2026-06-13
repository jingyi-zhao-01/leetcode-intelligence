.PHONY: help install submission analytics dev-submission prod-submission dev-analytics dev-frontend test prisma-generate prisma-db-push prisma-db-pull submission-stats submission-image-start submission-image-stop d2-render-architecture clean

help:
	@echo "Available commands:"
	@echo ""
	@echo "Prisma"
	@echo "  make prisma-generate        - Generate Prisma JS client with DATABASE_URL"
	@echo "  make prisma-db-push         - Push schema with DATABASE_URL"
	@echo "  make prisma-db-pull         - Pull schema from database with DATABASE_URL"
	@echo ""
	@echo "Local Run"
	@echo "  make submission             - Start Submission server"
	@echo "  make analytics              - Start Analytics API"
	@echo "  make dev-frontend           - Start Next.js frontend"
	@echo "  make submission-stats       - Show submission statistics"
	@echo "  make d2-render-architecture - Render all architecture.d2 files to architecture.svg"
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

d2-render-architecture:
	@command -v d2 >/dev/null 2>&1 || { echo "d2 CLI not found" >&2; exit 1; }
	@find . -name 'architecture.d2' -print0 | while IFS= read -r -d '' file; do \
		output="$${file%.d2}.svg"; \
		echo "Rendering $$file -> $$output"; \
		d2 "$$file" "$$output"; \
	done

clean:
	rm -rf .venv __pycache__ .pytest_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	cd packages/graph-ui && rm -rf .next node_modules/.cache out
