.PHONY: help install dev build clean

help:
	@echo "Available commands:"
	@echo "  make install  - Install dependencies"
	@echo "  make dev      - Start Next.js dev server on port 3001"
	@echo "  make build    - Build production bundle"
	@echo "  make clean    - Remove build artifacts and caches"

install:
	npm install

dev:
	PORT=3001 npm run dev

build:
	npm run build

clean:
	@echo "Cleaning build artifacts..."
	rm -rf .next node_modules/.cache out
