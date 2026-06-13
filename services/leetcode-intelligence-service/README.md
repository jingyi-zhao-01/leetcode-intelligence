# LeetCode Intelligence Service

Service runtime for prompting, scoring, and focus recommendations on top of shared LeetCode submission data.

## What it does

- Prompt dispatcher: periodically picks a problem and posts it to the prompt channel.
- Prompt response listener: stays online in the prompt channel and scores replies.
- HTTP API: exposes health, prompt triggering, reply scoring, and recommendations.
- Recommender: periodically ranks problems and posts them to the recommendation channel.

## Architecture

This directory is split into a service runtime layer and a domain core.

![System architecture](../../docs/architecture/architecture-v1.svg)

D2 source: [`../../docs/architecture/architecture-v1.d2`](../../docs/architecture/architecture-v1.d2)

- Service runtime concerns live in [`src/service-runtime`](./src/service-runtime):
  - runtime composition
  - database boundary lifecycle
  - external dependency wiring
  - process entrypoints, Discord, and HTTP startup
- Domain logic lives in [`src/core/README.md`](./src/core/README.md):
  - prompt generation
  - reply scoring
  - weight calculation
  - recommendation ranking
  - recommendation narrative generation

If you want to understand how scoring, weight, and recommendation interact, start with [`src/core/README.md`](./src/core/README.md).

## Entry Points

- `make intelligence-cli` - one-off CLI prompt/response session
- `make intelligence-server` - HTTP API server
- `make intelligence-prompt-dispatch` - scheduled Discord prompt dispatcher
- `make intelligence-prompt-listener` - always-on Discord reply listener
- `make intelligence-recommender` - periodic focus recommender and push channel
- `make -C docker intelligence-image-start` - run the service from Docker image
- `make -C docker intelligence-image-stop` - stop the Docker container

## Helm Values Sample

Use your existing SSM/External Secret setup for sensitive values. Keep secrets out of `values.yaml` and inject them from an external secret store.

Recommended values file for homelab:

- `homelab.value.yaml` in this directory

```yaml
# Apply with your own chart path/release name.
helm upgrade --install leetcode-intelligence <chart-path> -f homelab.value.yaml
```

Suggested secret source:
- SSM Parameter Store or AWS External Secrets Operator
- Mount or sync the secret into `leetcode-intelligence-service-secrets`
- Keep `DATABASE_URL`, `OPEN_ROUTER_API_KEY`, and `DISCORD_BOT_TOKEN` out of Helm values

## k3s Integration

Use the checked-in manifest file in this directory:

- `homelab-k3s.yml`

### 1) Prepare configuration

- Edit `homelab-k3s.yml` placeholders before deployment:
	- `<owner>` in image path
	- `<postgres-url>`
	- `<openrouter-key>`
	- `<discord-bot-token>`
	- `<prompt-channel-id>`
	- `<recommend-channel-id>`

### 2) Apply resources

```bash
kubectl apply -f homelab-k3s.yml
```

### 3) Verify all workloads are running

```bash
kubectl -n leetcode get deploy
kubectl -n leetcode get pods
kubectl -n leetcode logs deploy/intelligence-server --tail=100
kubectl -n leetcode logs deploy/intelligence-prompt-listener --tail=100
kubectl -n leetcode logs deploy/intelligence-prompt-dispatch --tail=100
kubectl -n leetcode logs deploy/intelligence-recommender --tail=100
```

Expected deployments:

- `intelligence-server`
- `intelligence-prompt-listener`
- `intelligence-prompt-dispatch`
- `intelligence-recommender`

### 4) If only server is running

- Confirm you applied `homelab-k3s.yml` (not only Helm values).
- Re-check deployment list with `kubectl -n leetcode get deploy`.
- If prompt/recommend deployments exist but pods are failing, inspect events:

```bash
kubectl -n leetcode describe pod <pod-name>
```

- Verify secret/config values are present and valid:

```bash
kubectl -n leetcode get secret leetcode-intelligence-secrets -o yaml
kubectl -n leetcode get configmap leetcode-intelligence-config -o yaml
```

## HTTP API

- `GET /health`
- `POST /trigger`
- `POST /reply-by-event`
- `POST /reply-by-message`
- `GET /recommendations`
- `POST /recommendations/trigger`

`GET /health` is process-level only and does not query Neon.

## Required Environment

- `DATABASE_URL`
- `OPEN_ROUTER_API_KEY`
- `MODEL`
- `DISCORD_BOT_TOKEN`
- `PROMPT_DISCORD_CHANNEL_ID` for prompt dispatch and prompt responses
- `RECOMMEND_DISCORD_CHANNEL_ID` for recommendation pushes
- `INTELLIGENCE_PROMPT_CRON` for prompt dispatch
- `INTELLIGENCE_RECOMMEND_CRON`, `INTELLIGENCE_RECOMMEND_TOP_K`, `INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS` for recommendations

## Notes

- Prisma schema is shared from `services/shared/prisma/schema.prisma`.
- Use the service-local Makefile in this directory for intelligence commands.
- The default domain implementation uses:
  - OpenRouter-first scoring with local fallback
  - a shared pluggable `WeightCalculator`
  - heuristic recommendation ranking
  - OpenRouter narrative generation with local fallback
- Detailed core design and extension points are documented in [`src/core/README.md`](./src/core/README.md).
