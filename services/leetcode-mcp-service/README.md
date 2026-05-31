# LeetCode MCP Service

This service exposes persisted LeetCode problem and submission data through MCP tools and a small HTTP API.

## What It Does

- serves MCP tools over stdio or HTTP
- reads shared submission/problem data through Prisma
- provides search, review, history, and detail lookups
- keeps one explicit mutation tool for saving submission mistakes

## Entry Points

- `ts/server.ts`
  Starts either the HTTP server or stdio MCP transport.
- `ts/tools.ts`
  Houses the actual Prisma-backed tool implementations.

## Available Tools

- `get_submission_history`
- `analyze_thought_progression`
- `review_submissions`
- `search_problems`
- `get_problem_details`
- `get_related_problems`
- `list_problems_by_filters`
- `list_popular_problems`
- `check_problem_solved`
- `get_submission_detail`
- `save_submission_mistakes`

The HTTP server mirrors these tools under `/tools/<tool_name>`.

## Runtime Modes

- `npm run --workspace services/leetcode-mcp-service mcp-server`
  HTTP mode. Defaults to `MCP_PORT=8000`.
- `npm run --workspace services/leetcode-mcp-service mcp-server-stdio`
  Stdio mode for MCP clients that expect JSON-RPC over stdio.

Repo-level shortcuts:

- `make mcp`
- `make mcp-stdio`

## Dependencies

- `DATABASE_URL`
  Required for Prisma-backed reads and writes.
- shared schema:
  `services/shared/prisma/schema.prisma`

## Editing Notes

- Preserve tool names and payload contracts unless the calling client is being updated in the same change.
- Prefer adding new read tools over expanding mutation surface area.
- Keep transport setup thin; business logic belongs in `ts/tools.ts`.
