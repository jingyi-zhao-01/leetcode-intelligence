ROOT_DIR := ../..
SERVICE_DIR := services/leetcode-intelligence-service

.PHONY: help intelligence intelligence-cli intelligence-server intelligence-recommender intelligence-prompt-dispatch intelligence-prompt-response intelligence-image-start intelligence-image-stop prisma-generate

help:
	@echo "Available commands:"
	@echo ""
	@echo "Local Run"
	@echo "  make intelligence             - Start the default intelligence CLI flow"
	@echo "  make intelligence-cli         - Start the CLI prompt/response session"
	@echo "  make intelligence-server      - Start the HTTP API server"
	@echo "  make intelligence-prompt-dispatch - Scheduled prompt dispatcher for PROMPT_DISCORD_CHANNEL_ID"
	@echo "  make intelligence-prompt-response - Always-on prompt response listener for PROMPT_DISCORD_CHANNEL_ID"
	@echo "  make intelligence-recommender - Scheduled recommendation push for RECOMMEND_DISCORD_CHANNEL_ID"
	@echo ""
	@echo "Image Run"
	@echo "  make intelligence-image-start - Start intelligence service from Docker image"
	@echo "  make intelligence-image-stop  - Stop intelligence service Docker container"
	@echo ""
	@echo "Other"
	@echo "  make prisma-generate          - Generate Prisma JS client from repo root"

-include ../../.env
export

PRISMA_RUN_JS = npm exec prisma --
PRISMA_SCHEMA = --schema services/shared/prisma/schema.prisma
INTELLIGENCE_IMAGE ?= leetcode-intelligence-service:latest
INTELLIGENCE_CONTAINER_NAME ?= leetcode-intelligence-service
INTELLIGENCE_HOST_PORT ?= 8030

prisma-generate:
	# Generate the Prisma client before any intelligence command runs.
	@cd $(ROOT_DIR) && DATABASE_URL=$(DATABASE_URL) $(PRISMA_RUN_JS) generate --generator jsclient $(PRISMA_SCHEMA)

# Default intelligence entrypoint: run the CLI prompt/response loop.
intelligence: intelligence-cli

# Run a one-off CLI session that asks for a solution and scores the reply.
intelligence-cli: prisma-generate
	@cd $(ROOT_DIR) && DATABASE_URL=$(DATABASE_URL) \
		OPEN_ROUTER_API_KEY=$(OPEN_ROUTER_API_KEY) \
		MODEL=$(MODEL) \
		npm run --workspace $(SERVICE_DIR) intelligence-cli

# Run the HTTP server that exposes health and reply/recommendation APIs.
intelligence-server: prisma-generate
	@cd $(ROOT_DIR) && DATABASE_URL=$(DATABASE_URL) \
		npm run --workspace $(SERVICE_DIR) intelligence-server

# Run the scheduled Discord prompt dispatcher for the prompt channel.
intelligence-prompt-dispatch: prisma-generate
	@cd $(ROOT_DIR) && DATABASE_URL=$(DATABASE_URL) \
		DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		PROMPT_DISCORD_CHANNEL_ID=$(PROMPT_DISCORD_CHANNEL_ID) \
		INTELLIGENCE_PROMPT_CRON=$(INTELLIGENCE_PROMPT_CRON) \
		TZ=$(TZ) \
		npm run --workspace $(SERVICE_DIR) intelligence-prompt-dispatch

# Run the always-on Discord reply listener in the prompt channel.
intelligence-prompt-response: prisma-generate
	@cd $(ROOT_DIR) && DATABASE_URL=$(DATABASE_URL) \
		DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		PROMPT_DISCORD_CHANNEL_ID=$(PROMPT_DISCORD_CHANNEL_ID) \
		npm run --workspace $(SERVICE_DIR) intelligence-prompt-response

# Run the focus recommendation dispatcher on the recommendation channel.
intelligence-recommender: prisma-generate
	@cd $(ROOT_DIR) && DATABASE_URL=$(DATABASE_URL) \
		DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		RECOMMEND_DISCORD_CHANNEL_ID=$(RECOMMEND_DISCORD_CHANNEL_ID) \
		INTELLIGENCE_RECOMMEND_CRON=$(INTELLIGENCE_RECOMMEND_CRON) \
		npm run --workspace $(SERVICE_DIR) intelligence-recommender

# Start the intelligence Docker image with all runtime env vars.
intelligence-image-start:
	@echo "Starting intelligence service from image $(INTELLIGENCE_IMAGE) on port $(INTELLIGENCE_HOST_PORT)" >&2
	@docker rm -f $(INTELLIGENCE_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker run --rm --name $(INTELLIGENCE_CONTAINER_NAME) -p $(INTELLIGENCE_HOST_PORT):8030 \
		-e DATABASE_URL=$(DATABASE_URL) \
		-e OPEN_ROUTER_API_KEY=$(OPEN_ROUTER_API_KEY) \
		-e API_KEY=$(API_KEY) \
		-e MODEL=$(MODEL) \
		-e DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		-e PROMPT_DISCORD_CHANNEL_ID=$(PROMPT_DISCORD_CHANNEL_ID) \
		-e RECOMMEND_DISCORD_CHANNEL_ID=$(RECOMMEND_DISCORD_CHANNEL_ID) \
		-e INTELLIGENCE_PROMPT_CRON=$(INTELLIGENCE_PROMPT_CRON) \
		-e INTELLIGENCE_RECOMMEND_CRON=$(INTELLIGENCE_RECOMMEND_CRON) \
		-e INTELLIGENCE_RECOMMEND_TOP_K=$(INTELLIGENCE_RECOMMEND_TOP_K) \
		-e INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS=$(INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS) \
		$(INTELLIGENCE_IMAGE)

# Stop and remove the intelligence Docker container if it is running.
intelligence-image-stop:
	@echo "Stopping intelligence service container $(INTELLIGENCE_CONTAINER_NAME)" >&2
	@docker rm -f $(INTELLIGENCE_CONTAINER_NAME) >/dev/null 2>&1 || true
