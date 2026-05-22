# LeetCode Intelligence Service

Intelligence service for prompting, scoring, and focus recommendations.

## What it does

- Prompt dispatcher: periodically picks a problem and posts it to the prompt channel.
- Prompt response listener: stays online in the prompt channel and scores replies.
- HTTP API: exposes health, prompt triggering, reply scoring, and recommendations.
- Recommender: periodically ranks problems and posts them to the recommendation channel.

## Entry Points

- `make intelligence-cli` - one-off CLI prompt/response session
- `make intelligence-server` - HTTP API server
- `make intelligence-prompt-dispatch` - scheduled Discord prompt dispatcher
- `make intelligence-prompt-response` - always-on Discord reply listener
- `make intelligence-recommender` - periodic focus recommender and push channel
- `make intelligence-image-start` - run the service from Docker image

## Helm Values Sample

Use your existing SSM/External Secret setup for sensitive values. Keep secrets out of `values.yaml` and inject them from an external secret store.

```yaml
image:
  repository: ghcr.io/<owner>/leetcode-intelligence-service
  tag: latest

service:
  port: 8030

env:
  MODEL: openai/gpt-4o-mini
  INTELLIGENCE_HOST: "0.0.0.0"
  INTELLIGENCE_PROMPT_CRON: "0 9 * * *"
  INTELLIGENCE_RECOMMEND_CRON: "0 20 * * *"
  INTELLIGENCE_RECOMMEND_TOP_K: "5"
  INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS: "30"
  PROMPT_DISCORD_CHANNEL_ID: "<prompt-channel-id>"
  RECOMMEND_DISCORD_CHANNEL_ID: "<recommend-channel-id>"

existingSecret:
  name: leetcode-intelligence-service-secrets
  keys:
    DATABASE_URL: DATABASE_URL
    OPEN_ROUTER_API_KEY: OPEN_ROUTER_API_KEY
    DISCORD_BOT_TOKEN: DISCORD_BOT_TOKEN
```

Suggested secret source:
- SSM Parameter Store or AWS External Secrets Operator
- Mount or sync the secret into `leetcode-intelligence-service-secrets`
- Keep `DATABASE_URL`, `OPEN_ROUTER_API_KEY`, and `DISCORD_BOT_TOKEN` out of Helm values

## HTTP API

- `GET /health`
- `POST /trigger`
- `POST /reply-by-event`
- `POST /reply-by-message`
- `GET /recommendations`
- `POST /recommendations/trigger`

## Required Environment

- `DATABASE_URL`
- `OPEN_ROUTER_API_KEY` or `API_KEY`
- `MODEL`
- `DISCORD_BOT_TOKEN`
- `PROMPT_DISCORD_CHANNEL_ID` for prompt dispatch and prompt responses
- `RECOMMEND_DISCORD_CHANNEL_ID` for recommendation pushes
- `INTELLIGENCE_PROMPT_CRON` for prompt dispatch
- `INTELLIGENCE_RECOMMEND_CRON`, `INTELLIGENCE_RECOMMEND_TOP_K`, `INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS` for recommendations

## Notes

- Prisma schema is shared from `services/shared/prisma/schema.prisma`.
- Use the service-local Makefile in this directory for intelligence commands.
- Default scoring and recommendation paths use OpenRouter when available and fall back locally when needed.
