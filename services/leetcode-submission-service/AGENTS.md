# AGENTS.md

Agent map for `services/leetcode-submission-service`.

Read ADRs first when changing session behavior, companion behavior, or failure-analysis lifecycles. Use [ARCHITECTURE.md](./ARCHITECTURE.md) and code after that.

## What This Service Owns

- newline-delimited JSON over TCP for `leetcode.nvim`
- local OpenAI-compatible HTTP chat endpoint for `CodeCompanion`
- one active in-memory timer/session at a time
- Mem0 session snapshot persistence when a session ends
- recent submission cache with write-through persistence behavior
- durable submission persistence through Prisma
- OpenRouter-backed failure analysis and companion chat

## Start Here

1. [../../docs/adrs/001-stateful-failure-analysis-session-aggregation.md](../../docs/adrs/001-stateful-failure-analysis-session-aggregation.md)
2. [../../docs/adrs/002-session-bound-companion-memory-and-failure-events.md](../../docs/adrs/002-session-bound-companion-memory-and-failure-events.md)
3. [../../docs/adrs/003-mem0-session-snapshot-persistence.md](../../docs/adrs/003-mem0-session-snapshot-persistence.md)
4. [../../docs/adrs/004-mem0-recall-lifecycle-and-hydration.md](../../docs/adrs/004-mem0-recall-lifecycle-and-hydration.md)
5. [ARCHITECTURE.md](./ARCHITECTURE.md)
6. [src/server.ts](./src/server.ts)
7. [src/session/scope.ts](./src/session/scope.ts)
8. [src/session/mem0.ts](./src/session/mem0.ts)
9. [src/core/failureAnalysis.ts](./src/core/failureAnalysis.ts)
10. [src/core/staticAnalysis.ts](./src/core/staticAnalysis.ts)
11. [src/core/companionChat.ts](./src/core/companionChat.ts)

## File Map

- `src/server.ts`
  Top-level TCP server, action dispatch, Prisma wiring, submission shaping.
- `src/session/index.ts`
  Session module exports.
- `src/session/timer.ts`
  Active solve-session timers and lifecycle.
- `src/session/scope.ts`
  Shared in-memory session scope for companion memory, latest failure, and service-owned session memory.
- `src/session/mem0.ts`
  Session-end snapshot rendering and Mem0 persistence.
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

- Update ADRs first when session scope, failure lifecycle, companion/session contracts, or session persistence behavior change.
- Update ADRs first when Mem0 persistence, title-slug recall, hydrate timing, or recalled prompt shape change.
- Update [ARCHITECTURE.md](./ARCHITECTURE.md) when actions, runtime boundaries, or persistence behavior change.
- Update this file only when the navigation map or edit guardrails change.
