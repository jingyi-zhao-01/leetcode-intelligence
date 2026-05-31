# AGENTS.md

Agent map for `services/leetcode-mcp-service`.

This service is the tool-access layer over persisted LeetCode data. Read [README.md](./README.md) for the deeper contract overview.

## What This Service Owns

- MCP tool registration and transport startup
- HTTP equivalents for the MCP tools
- read-mostly access to problem and submission intelligence
- one retained mutation path for saving submission mistakes

## Start Here

1. [README.md](./README.md)
2. [ts/server.ts](./ts/server.ts)
3. [ts/tools.ts](./ts/tools.ts)

## Boundaries

- Transport and tool registration live in `ts/server.ts`.
- Tool implementations live in `ts/tools.ts`.
- Keep tool names and argument schemas stable unless the client contract is intentionally changing.
- Prefer read-only operations; `save_submission_mistakes` is the current explicit mutation exception.

## Run And Verify

From repo root:

- `npm run --workspace services/leetcode-mcp-service build`
- `make mcp`
- `make mcp-stdio`

## When To Update Docs

- Update [README.md](./README.md) when tool inventory, transports, or operational assumptions change.
- Update this file only when the navigation map or edit guardrails change.
