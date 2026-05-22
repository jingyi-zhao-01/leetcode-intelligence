.PHONY: help submission-image-start submission-image-stop intelligence-image-start intelligence-image-stop

-include ../.env
export

SUBMISSION_IMAGE ?= leetcode-submission-service:latest
SUBMISSION_CONTAINER_NAME ?= leetcode-submission-service
SUBMISSION_HOST_PORT ?= 3000

INTELLIGENCE_IMAGE ?= leetcode-intelligence-service:latest
INTELLIGENCE_CONTAINER_NAME ?= leetcode-intelligence-service
INTELLIGENCE_HOST_PORT ?= 8030

help:
	@echo "Docker/image related commands:"
	@echo "  make -C docker submission-image-start   - Start submission server from Docker image"
	@echo "  make -C docker submission-image-stop    - Stop submission server Docker container"
	@echo "  make -C docker intelligence-image-start - Start intelligence service from Docker image"
	@echo "  make -C docker intelligence-image-stop  - Stop intelligence service Docker container"

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
		-e MODEL=$(MODEL) \
		-e DISCORD_BOT_TOKEN=$(DISCORD_BOT_TOKEN) \
		-e PROMPT_DISCORD_CHANNEL_ID=$(PROMPT_DISCORD_CHANNEL_ID) \
		-e RECOMMEND_DISCORD_CHANNEL_ID=$(RECOMMEND_DISCORD_CHANNEL_ID) \
		-e INTELLIGENCE_PROMPT_CRON=$(INTELLIGENCE_PROMPT_CRON) \
		-e INTELLIGENCE_RECOMMEND_CRON=$(INTELLIGENCE_RECOMMEND_CRON) \
		-e INTELLIGENCE_RECOMMEND_TOP_K=$(INTELLIGENCE_RECOMMEND_TOP_K) \
		-e INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS=$(INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS) \
		$(INTELLIGENCE_IMAGE)

intelligence-image-stop:
	@echo "Stopping intelligence service container $(INTELLIGENCE_CONTAINER_NAME)" >&2
	@docker rm -f $(INTELLIGENCE_CONTAINER_NAME) >/dev/null 2>&1 || true