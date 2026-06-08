# AGENTS.md

This file is the agent entrypoint for `leetcode-qa`.

It follows the harness-engineering pattern described by OpenAI on February 11, 2026: keep `AGENTS.md` short, treat it as a map, and push durable knowledge into repo-local docs and code-adjacent READMEs.

## How To Use This File

- Start here for repo shape, boundaries, and safe defaults.
- Do not treat this file as the full source of truth.
- Follow links into service-local docs before changing behavior.
- Prefer updating nearby docs when code changes invalidate them.

## System Intent

`leetcode-qa` is a local-first LeetCode learning system with three active service surfaces:

1. `services/leetcode-submission-service`
   Records submissions, tracks active solve sessions, and runs failure analysis for editor feedback.
2. `services/leetcode-intelligence-service`
   Scores reflection prompts, updates learning weights, and produces focus recommendations.
3. `services/leetcode-mcp-service`
   Exposes submission/problem intelligence through MCP and HTTP tool endpoints.

Shared persistence lives in `services/shared/prisma/schema.prisma`.

## Read In This Order

1. [README.md](./README.md)
2. [services/leetcode-submission-service/AGENTS.md](./services/leetcode-submission-service/AGENTS.md)
3. [services/leetcode-intelligence-service/AGENTS.md](./services/leetcode-intelligence-service/AGENTS.md)
4. [services/leetcode-mcp-service/AGENTS.md](./services/leetcode-mcp-service/AGENTS.md)

If you are only touching one service, stop after the relevant service-local documents.

## Repo Map

- `README.md`
  Product-level overview and service list.
- `services/shared/prisma/schema.prisma`
  Shared database schema used by the TypeScript services.
- `services/leetcode-submission-service/`
  TCP submission runtime and OpenRouter-backed failure analysis.
- `services/leetcode-intelligence-service/`
  Prompting, scoring, recommendation, HTTP, and Discord runtimes.
- `services/leetcode-mcp-service/`
  MCP/HTTP access layer over persisted LeetCode data.

## Service Sources Of Truth

### Submission Service

- [docs/adrs/001-stateful-failure-analysis-session-aggregation.md](./docs/adrs/001-stateful-failure-analysis-session-aggregation.md)
- [docs/adrs/002-session-bound-companion-memory-and-failure-events.md](./docs/adrs/002-session-bound-companion-memory-and-failure-events.md)
- [docs/adrs/003-mem0-session-snapshot-persistence.md](./docs/adrs/003-mem0-session-snapshot-persistence.md)
- [docs/adrs/004-mem0-recall-lifecycle-and-hydration.md](./docs/adrs/004-mem0-recall-lifecycle-and-hydration.md)
- [services/leetcode-submission-service/AGENTS.md](./services/leetcode-submission-service/AGENTS.md)
- [services/leetcode-submission-service/ARCHITECTURE.md](./services/leetcode-submission-service/ARCHITECTURE.md)

### Intelligence Service

- [services/leetcode-intelligence-service/AGENTS.md](./services/leetcode-intelligence-service/AGENTS.md)
- [services/leetcode-intelligence-service/README.md](./services/leetcode-intelligence-service/README.md)
- [services/leetcode-intelligence-service/src/core/README.md](./services/leetcode-intelligence-service/src/core/README.md)
- [services/leetcode-intelligence-service/src/service-runtime/README.md](./services/leetcode-intelligence-service/src/service-runtime/README.md)

### MCP Service

- [services/leetcode-mcp-service/AGENTS.md](./services/leetcode-mcp-service/AGENTS.md)
- [services/leetcode-mcp-service/README.md](./services/leetcode-mcp-service/README.md)

## Working Norms For Agents

- Keep changes scoped to the user request.
- Preserve the split between domain logic and runtime composition when editing the intelligence service.
- Preserve the split between request handling, caching, persistence, and failure analysis when editing the submission service.
- When touching submission-session behavior, Mem0 persistence/recall, or companion context hydration, read the submission-service ADRs before editing code.
- Keep MCP tool names and payload shapes stable unless the user explicitly asks for a contract change.
- Prefer code-adjacent documentation over adding large top-level prose.

## D2 Diagram Style Preference

When adding or updating D2 diagrams, prefer the user's established high-level architecture style:

- Treat D2 as a system overview first, not an implementation-detail dump.
- Group nodes by runtime boundary before drawing flows, for example `Strict local` or `Can be cloud hosted`.
- Clearly separate entry points, runtime surfaces, external systems, and data planes.
- Prefer a left-to-right primary reading direction with straight main flows and minimal crossing lines.
- Optimize for ownership and data flow clarity, not source-file completeness.
- Use a small number of stable responsibility-oriented node labels rather than many file/module names.
- Keep edge labels short and protocol/action-oriented, such as `JSON over TCP`, `Prisma ORM`, or `GraphQL`.
- Preserve generous whitespace and a clean overview feel; prefer one readable system map plus optional focused sub-diagrams.

## Commands

From repo root:

- `npm test`
- `npm run format:check`
- `npm run lint`
- `make submission`
- `make mcp`
- `make -C services/leetcode-intelligence-service intelligence-server`

Service-local scripts are documented in each service's own `AGENTS.md` or `README.md`.

## Documentation Policy

- If you add or change a runtime entrypoint, update the nearest service doc.
- If you change cross-service behavior, update root `README.md` and any affected service docs.
- If a service gains enough complexity that this file starts to grow, move detail downward instead of expanding this file.

## Known Gaps

- Root `README.md` currently emphasizes submission and intelligence flows more than the MCP service.
- Some legacy files with near-duplicate names such as `agent.md` may exist in user worktrees; prefer the canonical uppercase `AGENTS.md`.
