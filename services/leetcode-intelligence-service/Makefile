ROOT_DIR := ../..
SERVICE_DIR := services/leetcode-intelligence-service

.PHONY: help intelligence intelligence-cli intelligence-server intelligence-recommender intelligence-prompt-dispatch intelligence-prompt-listener intelligence-image-start intelligence-image-stop prisma-generate

help:
	@echo "Available commands:"
	@echo ""
	@echo "Local Run"
	@echo "  make intelligence             - Start the default intelligence CLI flow"
	@echo "  make intelligence-cli         - Start the CLI prompt/response session"
	@echo "  make intelligence-server      - Start the HTTP API server"
	@echo "  make intelligence-prompt-dispatch - Scheduled prompt dispatcher for PROMPT_DISCORD_CHANNEL_ID"
	@echo "  make intelligence-prompt-listener - Always-on prompt response listener for PROMPT_DISCORD_CHANNEL_ID"
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
intelligence-prompt-listener: prisma-generate
	@cd $(ROOT_DIR) && DATABASE_URL=$(DATABASE_URL) \
		OPEN_ROUTER_API_KEY=$(OPEN_ROUTER_API_KEY) \
		DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		PROMPT_DISCORD_CHANNEL_ID=$(PROMPT_DISCORD_CHANNEL_ID) \
		npm run --workspace $(SERVICE_DIR) intelligence-prompt-listener

# Run the focus recommendation dispatcher on the recommendation channel.
intelligence-recommender: prisma-generate
	@cd $(ROOT_DIR) && DATABASE_URL=$(DATABASE_URL) \
		DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		RECOMMEND_DISCORD_CHANNEL_ID=$(RECOMMEND_DISCORD_CHANNEL_ID) \
		INTELLIGENCE_RECOMMEND_CRON=$(INTELLIGENCE_RECOMMEND_CRON) \
		npm run --workspace $(SERVICE_DIR) intelligence-recommender

# Start the intelligence Docker image with all runtime env vars.
intelligence-image-start:
	@cd $(ROOT_DIR) && $(MAKE) -C docker intelligence-image-start

# Stop and remove the intelligence Docker container if it is running.
intelligence-image-stop:
	@cd $(ROOT_DIR) && $(MAKE) -C docker intelligence-image-stop
