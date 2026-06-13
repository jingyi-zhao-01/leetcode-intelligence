# AGENTS.md

Agent map for `services/leetcode-intelligence-service`.

This service already has good code-adjacent docs. Use this file as the short routing layer, not the full explanation.

## What This Service Owns

- prompt selection from historical submissions
- reflection/reply scoring
- learning-weight updates
- focus recommendation ranking and narrative generation
- HTTP and Discord entrypoints around the domain logic

## Read In This Order

1. [README.md](./README.md)
2. [../../docs/adrs/006-separate-vercel-bff-from-intelligence-core-service.md](../../docs/adrs/006-separate-vercel-bff-from-intelligence-core-service.md)
3. [../../docs/architecture/architecture-v1.d2](../../docs/architecture/architecture-v1.d2)
4. [src/core/README.md](./src/core/README.md)
5. [src/service-runtime/README.md](./src/service-runtime/README.md)
6. [src/server.ts](./src/server.ts) or the relevant CLI entrypoint

## Architectural Split

- `src/core/`
  Domain logic for prompting, scoring, weights, and recommendations.
- `src/service-runtime/`
  Runtime composition, Prisma lifecycle, external clients, and orchestration.
- `src/client/`, `src/cli/`, `src/cron/`, and `src/discord/`
  Delivery surfaces for Discord adapters, one-off CLI flows, and scheduled workers.

Keep this split intact. Domain code should not grow implicit runtime wiring.

## High-Value Entry Points

- `src/server.ts`
  HTTP API surface.
- `src/cli.ts`
  One-off CLI flow.
- `src/cron/prompt-dispatch.ts`
  Scheduled or one-shot prompt dispatch.
- `src/discord/prompt-response.ts`
  Discord reply listener.
- `src/cron/recommender.ts`
  Scheduled or one-shot recommendation dispatch.

## Guardrails

- Preserve score and weight semantics unless the user asks for behavior changes.
- Keep OpenRouter-backed paths resilient with clear fallback behavior.
- Treat Discord and HTTP as adapters around the runtime/domain layers, not places for core business rules.
- Prefer moving reusable intelligence domain logic into this service instead of growing Next.js server actions in `client/`.

## Run And Verify

From this directory:

- `make intelligence-server`
- `make intelligence-cli`
- `make intelligence-prompt-dispatch-once`
- `make intelligence-recommender-once`

From repo root:

- `npm run --workspace services/leetcode-intelligence-service test`
- `npm run --workspace services/leetcode-intelligence-service build`

## When To Update Docs

- Keep architecture docs and diagrams under `../../docs/architecture/`.
- Do not add service-specific architecture diagrams; update the single versioned repo diagram instead.
- Update [../../docs/adrs/006-separate-vercel-bff-from-intelligence-core-service.md](../../docs/adrs/006-separate-vercel-bff-from-intelligence-core-service.md) if the BFF/core-service boundary changes.
- Update [README.md](./README.md) when service capabilities, env vars, or deployment surfaces change.
- Update [src/core/README.md](./src/core/README.md) when scoring/recommendation semantics change.
- Update [src/service-runtime/README.md](./src/service-runtime/README.md) when runtime composition boundaries change.
