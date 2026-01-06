.PHONY: help install-all dev-backend dev-submission dev-analytics dev-frontend clean-all prisma-generate-all submission-stats

help:
	@echo "Available commands for managing both packages:"
	@echo "  make install-all          - Install dependencies for both backend and frontend"
	@echo "  make dev-submission       - Start TCP submission server on port 3000"
	@echo "  make dev-analytics        - Start Analytics API on port 8000"
	@echo "  make dev-backend          - Alias for dev-analytics"
	@echo "  make dev-frontend         - Start Next.js frontend on port 3001"
	@echo "  make clean-all           - Clean both packages"
	@echo "  make prisma-generate-all  - Generate Prisma client for backend"
	@echo "  make submission-stats     - Show submission statistics"
	@echo ""
	@echo "Port allocation:"
	@echo "  - Port 3000: TCP submission server (for nvim)"
	@echo "  - Port 3001: Next.js frontend (web UI)"
	@echo "  - Port 8000: Analytics API (HTTP/REST)"
	@echo ""
	@echo "To run all services:"
	@echo "  1. Terminal 1: make dev-submission"
	@echo "  2. Terminal 2: make dev-analytics"
	@echo "  3. Terminal 3: make dev-frontend"

install-all:
	@echo "Installing submissions dependencies..."
	cd submissions && make install
	@echo "\nInstalling graph-ui dependencies..."
	cd graph-ui && make install
	@echo "\n✓ All dependencies installed"

dev-submission:
	@echo "Starting TCP submission server on port 3000..."
	cd submissions && make dev-submission

dev-analytics:
	@echo "Starting Analytics API on port 8000..."
	cd submissions && make dev-analytics

dev-backend:
	@echo "Starting Analytics API on port 8000..."
	cd submissions && make dev-analytics

dev-frontend:
	@echo "Starting Next.js frontend on port 3000..."
	cd graph-ui && make dev

clean-all:
	@echo "Cleaning submissions..."
	cd submissions && make clean
	@echo "Cleaning graph-ui..."
	cd graph-ui && make clean
	@echo "✓ All packages cleaned"

prisma-generate-all:
	@echo "Generating Prisma client for submissions..."
	cd submissions && make prisma-generate
	@echo "✓ Prisma client generated"

submission-stats:
	@echo "Fetching submission statistics..."
	cd submissions && make submission-stats

setup-env:
	@echo "Setting up environment for submissions..."
	@if [ -f ../../.env ]; then \
		cp ../../.env submissions/.env; \
		echo "✓ Copied .env to submissions"; \
	else \
		echo "⚠ Warning: ../../.env not found"; \
	fi
