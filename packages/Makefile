.PHONY: help install-all dev-backend dev-frontend clean-all prisma-generate-all

help:
	@echo "Available commands for managing both packages:"
	@echo "  make install-all          - Install dependencies for both backend and frontend"
	@echo "  make dev-backend          - Start FastAPI backend on port 8000"
	@echo "  make dev-frontend         - Start Next.js frontend on port 3000"
	@echo "  make clean-all           - Clean both packages"
	@echo "  make prisma-generate-all  - Generate Prisma client for backend"
	@echo ""
	@echo "To run both services:"
	@echo "  1. Terminal 1: make dev-backend"
	@echo "  2. Terminal 2: make dev-frontend"

install-all:
	@echo "Installing submissions dependencies..."
	cd submissions && make install
	@echo "\nInstalling graph-ui dependencies..."
	cd graph-ui && make install
	@echo "\n✓ All dependencies installed"

dev-backend:
	@echo "Starting FastAPI backend on port 8000..."
	cd submissions && make dev-api

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

setup-env:
	@echo "Setting up environment for submissions..."
	@if [ -f ../../.env ]; then \
		cp ../../.env submissions/.env; \
		echo "✓ Copied .env to submissions"; \
	else \
		echo "⚠ Warning: ../../.env not found"; \
	fi
