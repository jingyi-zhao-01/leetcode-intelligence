# step-4-mcp-handlers.md

## Objective
Ensure the agent layer is deterministic, safe, and observable.

## Key Results
- MCP handlers validate all inputs.
- No raw dynamic SQL execution.
- Stable pagination + ordering.
- Write operations idempotent where possible.
- Tool usage logging available.

## Tasks
1. Implement MCP handlers using views.
2. Add input validation (timestamps, enums, limits).
3. Guarantee deterministic ordering + pagination.
4. Implement write mutation paths.
5. Add logging and metrics.