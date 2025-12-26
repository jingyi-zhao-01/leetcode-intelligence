.PHONY: help install dev build clean

help:
	@echo "Available commands:"
	@echo "  make install  - Install dependencies"
	@echo "  make dev      - Start Next.js dev server on port 3000"
	@echo "  make build    - Build production bundle"
	@echo "  make clean    - Remove build artifacts and caches"

install:
	npm install

dev:
	npm run dev

build:
	npm run build

clean:
	@echo "Cleaning build artifacts..."
	rm -rf .next node_modules/.cache out
