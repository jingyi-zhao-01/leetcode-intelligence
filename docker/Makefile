.PHONY: help submission-image-start submission-image-stop intelligence-image-start intelligence-start-server intelligence-start-prompt intelligence-start-listener intelligence-start-recommendation up-all down-all

-include ../.env
export

SUBMISSION_IMAGE ?= leetcode-submission-service:latest
SUBMISSION_CONTAINER_NAME ?= leetcode-submission-service
SUBMISSION_HOST_PORT ?= 3000

INTELLIGENCE_IMAGE ?= leetcode-intelligence-service:latest
INTELLIGENCE_CONTAINER_NAME ?= leetcode-intelligence-service
INTELLIGENCE_HOST_PORT ?= 8030
INTELLIGENCE_PROMPT_CRON_CONTAINER_NAME ?= leetcode-intelligence-prompt-cron
INTELLIGENCE_PROMPT_LISTENER_CONTAINER_NAME ?= leetcode-intelligence-prompt-listener
INTELLIGENCE_RECOMMEND_CRON_CONTAINER_NAME ?= leetcode-intelligence-recommendation-cron

help:
	@echo "Docker/image related commands:"
	@echo "  make -C docker submission-image-start   - Start submission server from Docker image"
	@echo "  make -C docker submission-image-stop    - Stop submission server Docker container"
	@echo "  make -C docker intelligence-image-start - Start intelligence service from Docker image"
	@echo "  make -C docker up-all                   - Start all docker containers for this repo in background"
	@echo "  make -C docker down-all                 - Stop all docker containers for this repo"
	@echo "  make -C docker intelligence-start-server - Start intelligence HTTP server container"
	@echo "  make -C docker intelligence-start-prompt - Start prompt dispatch cron container"
	@echo "  make -C docker intelligence-start-listener - Start prompt listener container"
	@echo "  make -C docker intelligence-start-recommendation - Start recommendation cron container"

submission-image-start:
	@echo "Starting submission server from image $(SUBMISSION_IMAGE) on port $(SUBMISSION_HOST_PORT)" >&2
	@docker rm -f $(SUBMISSION_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker run --rm --name $(SUBMISSION_CONTAINER_NAME) -p $(SUBMISSION_HOST_PORT):3000 \
		-e DATABASE_URL=$(DATABASE_URL) \
		$(SUBMISSION_IMAGE)

submission-image-stop:
	@echo "Stopping submission server container $(SUBMISSION_CONTAINER_NAME)" >&2
	@docker rm -f $(SUBMISSION_CONTAINER_NAME) >/dev/null 2>&1 || true


intelligence-start-server:
	@echo "Starting intelligence server container $(INTELLIGENCE_CONTAINER_NAME) on port $(INTELLIGENCE_HOST_PORT)" >&2
	@docker rm -f $(INTELLIGENCE_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker run --rm --name $(INTELLIGENCE_CONTAINER_NAME) -p $(INTELLIGENCE_HOST_PORT):8030 \
		-e DATABASE_URL=$(DATABASE_URL) \
		-e OPEN_ROUTER_API_KEY=$(OPEN_ROUTER_API_KEY) \
		-e MODEL=$(MODEL) \
		-e DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		-e PROMPT_DISCORD_CHANNEL_ID=$(PROMPT_DISCORD_CHANNEL_ID) \
		-e RECOMMEND_DISCORD_CHANNEL_ID=$(RECOMMEND_DISCORD_CHANNEL_ID) \
		-e INTELLIGENCE_PROMPT_CRON=$(INTELLIGENCE_PROMPT_CRON) \
		-e INTELLIGENCE_RECOMMEND_CRON=$(INTELLIGENCE_RECOMMEND_CRON) \
		-e INTELLIGENCE_RECOMMEND_TOP_K=$(INTELLIGENCE_RECOMMEND_TOP_K) \
		-e INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS=$(INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS) \
		$(INTELLIGENCE_IMAGE) \
		npm run --workspace services/leetcode-intelligence-service intelligence-server

intelligence-start-prompt:
	@echo "Starting prompt dispatch cron container $(INTELLIGENCE_PROMPT_CRON_CONTAINER_NAME)" >&2
	@docker rm -f $(INTELLIGENCE_PROMPT_CRON_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker run --rm --name $(INTELLIGENCE_PROMPT_CRON_CONTAINER_NAME) \
		-e DATABASE_URL=$(DATABASE_URL) \
		-e DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		-e PROMPT_DISCORD_CHANNEL_ID=$(PROMPT_DISCORD_CHANNEL_ID) \
		-e INTELLIGENCE_PROMPT_CRON=$(INTELLIGENCE_PROMPT_CRON) \
		-e TZ=$(TZ) \
		$(INTELLIGENCE_IMAGE) \
		npm run --workspace services/leetcode-intelligence-service intelligence-prompt-dispatch

intelligence-start-listener:
	@echo "Starting prompt listener container $(INTELLIGENCE_PROMPT_LISTENER_CONTAINER_NAME)" >&2
	@docker rm -f $(INTELLIGENCE_PROMPT_LISTENER_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker run --rm --name $(INTELLIGENCE_PROMPT_LISTENER_CONTAINER_NAME) \
		-e DATABASE_URL=$(DATABASE_URL) \
		-e OPEN_ROUTER_API_KEY=$(OPEN_ROUTER_API_KEY) \
		-e MODEL=$(MODEL) \
		-e DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		-e PROMPT_DISCORD_CHANNEL_ID=$(PROMPT_DISCORD_CHANNEL_ID) \
		$(INTELLIGENCE_IMAGE) \
		npm run --workspace services/leetcode-intelligence-service intelligence-prompt-listener

intelligence-start-recommendation:
	@echo "Starting recommendation cron container $(INTELLIGENCE_RECOMMEND_CRON_CONTAINER_NAME)" >&2
	@docker rm -f $(INTELLIGENCE_RECOMMEND_CRON_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker run --rm --name $(INTELLIGENCE_RECOMMEND_CRON_CONTAINER_NAME) \
		-e DATABASE_URL=$(DATABASE_URL) \
		-e OPEN_ROUTER_API_KEY=$(OPEN_ROUTER_API_KEY) \
		-e MODEL=$(MODEL) \
		-e DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		-e RECOMMEND_DISCORD_CHANNEL_ID=$(RECOMMEND_DISCORD_CHANNEL_ID) \
		-e INTELLIGENCE_RECOMMEND_CRON=$(INTELLIGENCE_RECOMMEND_CRON) \
		-e INTELLIGENCE_RECOMMEND_TOP_K=$(INTELLIGENCE_RECOMMEND_TOP_K) \
		-e INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS=$(INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS) \
		-e TZ=$(TZ) \
		$(INTELLIGENCE_IMAGE) \
		npm run --workspace services/leetcode-intelligence-service intelligence-recommender

up-all:
	@echo "Starting all repo docker containers in background" >&2
	@docker rm -f $(INTELLIGENCE_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker rm -f $(INTELLIGENCE_PROMPT_CRON_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker rm -f $(INTELLIGENCE_PROMPT_LISTENER_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker rm -f $(INTELLIGENCE_RECOMMEND_CRON_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker rm -f $(SUBMISSION_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker run -d --rm --name $(SUBMISSION_CONTAINER_NAME) -p $(SUBMISSION_HOST_PORT):3000 \
		-e DATABASE_URL=$(DATABASE_URL) \
		$(SUBMISSION_IMAGE)
	@docker run -d --rm --name $(INTELLIGENCE_CONTAINER_NAME) -p $(INTELLIGENCE_HOST_PORT):8030 \
		-e DATABASE_URL=$(DATABASE_URL) \
		-e OPEN_ROUTER_API_KEY=$(OPEN_ROUTER_API_KEY) \
		-e MODEL=$(MODEL) \
		-e DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		-e PROMPT_DISCORD_CHANNEL_ID=$(PROMPT_DISCORD_CHANNEL_ID) \
		-e RECOMMEND_DISCORD_CHANNEL_ID=$(RECOMMEND_DISCORD_CHANNEL_ID) \
		-e INTELLIGENCE_PROMPT_CRON=$(INTELLIGENCE_PROMPT_CRON) \
		-e INTELLIGENCE_RECOMMEND_CRON=$(INTELLIGENCE_RECOMMEND_CRON) \
		-e INTELLIGENCE_RECOMMEND_TOP_K=$(INTELLIGENCE_RECOMMEND_TOP_K) \
		-e INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS=$(INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS) \
		$(INTELLIGENCE_IMAGE) \
		npm run --workspace services/leetcode-intelligence-service intelligence-server
	@docker run -d --rm --name $(INTELLIGENCE_PROMPT_CRON_CONTAINER_NAME) \
		-e DATABASE_URL=$(DATABASE_URL) \
		-e DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		-e PROMPT_DISCORD_CHANNEL_ID=$(PROMPT_DISCORD_CHANNEL_ID) \
		-e INTELLIGENCE_PROMPT_CRON=$(INTELLIGENCE_PROMPT_CRON) \
		-e TZ=$(TZ) \
		$(INTELLIGENCE_IMAGE) \
		npm run --workspace services/leetcode-intelligence-service intelligence-prompt-dispatch
	@docker run -d --rm --name $(INTELLIGENCE_PROMPT_LISTENER_CONTAINER_NAME) \
		-e DATABASE_URL=$(DATABASE_URL) \
		-e OPEN_ROUTER_API_KEY=$(OPEN_ROUTER_API_KEY) \
		-e MODEL=$(MODEL) \
		-e DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		-e PROMPT_DISCORD_CHANNEL_ID=$(PROMPT_DISCORD_CHANNEL_ID) \
		$(INTELLIGENCE_IMAGE) \
		npm run --workspace services/leetcode-intelligence-service intelligence-prompt-listener
	@docker run -d --rm --name $(INTELLIGENCE_RECOMMEND_CRON_CONTAINER_NAME) \
		-e DATABASE_URL=$(DATABASE_URL) \
		-e OPEN_ROUTER_API_KEY=$(OPEN_ROUTER_API_KEY) \
		-e MODEL=$(MODEL) \
		-e DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		-e RECOMMEND_DISCORD_CHANNEL_ID=$(RECOMMEND_DISCORD_CHANNEL_ID) \
		-e INTELLIGENCE_RECOMMEND_CRON=$(INTELLIGENCE_RECOMMEND_CRON) \
		-e INTELLIGENCE_RECOMMEND_TOP_K=$(INTELLIGENCE_RECOMMEND_TOP_K) \
		-e INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS=$(INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS) \
		-e TZ=$(TZ) \
		$(INTELLIGENCE_IMAGE) \
		npm run --workspace services/leetcode-intelligence-service intelligence-recommender

down-all:
	@echo "Stopping all repo docker containers" >&2
	@docker rm -f $(INTELLIGENCE_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker rm -f $(INTELLIGENCE_PROMPT_CRON_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker rm -f $(INTELLIGENCE_PROMPT_LISTENER_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker rm -f $(INTELLIGENCE_RECOMMEND_CRON_CONTAINER_NAME) >/dev/null 2>&1 || true
	@docker rm -f $(SUBMISSION_CONTAINER_NAME) >/dev/null 2>&1 || true