# AGENTS.md

Agent map for `services/leetcode-submission-service`.

Read this before editing the submission runtime, then use [ARCHITECTURE.md](./ARCHITECTURE.md) as the deeper source of truth.

## What This Service Owns

- newline-delimited JSON over TCP for `leetcode.nvim`
- local OpenAI-compatible HTTP chat endpoint for `CodeCompanion`
- one active in-memory timer/session at a time
- recent submission cache with write-through persistence behavior
- durable submission persistence through Prisma
- OpenRouter-backed failure analysis and companion chat

## Start Here

1. [ARCHITECTURE.md](./ARCHITECTURE.md)
2. [src/server.ts](./src/server.ts)
3. [src/action-middleware.ts](./src/action-middleware.ts)
4. [src/core/failureAnalysis.ts](./src/core/failureAnalysis.ts)
5. [src/core/staticAnalysis.ts](./src/core/staticAnalysis.ts)
6. [src/core/companionChat.ts](./src/core/companionChat.ts)

## File Map

- `src/server.ts`
  Top-level TCP server, action dispatch, Prisma wiring, submission shaping.
- `src/timer.ts`
  Active solve-session state.
- `src/cache.ts`
  Recent submission cache.
- `src/action-middleware.ts`
  Read-through and write-through patterns around cache and persistence.
- `src/core/failureAnalysis.ts`
  Failure-analysis contracts and facade.
- `src/core/staticAnalysis.ts`
  OpenRouter integration for failure analysis.
- `src/core/companionChat.ts`
  Service-owned chat prompt and OpenRouter call used by the local companion HTTP endpoint.
- `src/utils/failureAnalysisParser.ts`
  Structured response parsing and sanitization.
- `src/database.ts`
  Database URL normalization and diagnostics.

## Guardrails

- Keep request/response payloads backward compatible with the editor integration unless explicitly changing the client contract.
- Keep the companion HTTP endpoint OpenAI-compatible enough for local editor adapters.
- Do not silently move durable state into memory-only paths.
- Keep timer/cache behavior cheap and synchronous on the request path.
- Keep failure-analysis output bounded and structured for editor rendering.

## Run And Verify

From repo root:

- `npm run --workspace services/leetcode-submission-service build`
- `npm run --workspace services/leetcode-submission-service test`
- `make submission`

## When To Update Docs

- Update [ARCHITECTURE.md](./ARCHITECTURE.md) when actions, runtime boundaries, or persistence behavior change.
- Update this file only when the navigation map or edit guardrails change.
