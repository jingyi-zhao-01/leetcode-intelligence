# step-1-tool-surface.md

## Objective
Establish a stable MCP interface so the agent interacts with your LeetCode memory through clear primitives rather than ad-hoc queries.

## Key Results
- All agent reads happen through ≤5 MCP read tools.
- All writes to learning memory happen through controlled write tools only.
- No direct SQL execution from the agent layer.
- Tool responses follow a consistent JSON contract.
- `Question` remains strictly read-only.

## Tasks
1. Freeze the rule: `Question` is read-only; MCP must never write to it.
2. Expose read tools:
   - `get_question_overview`
   - `list_submissions`
   - `get_activity_summary`
   - `find_weaknesses`
   - `search_thoughts`
3. Expose write tools:
   - `update_submission_thought`
   - `mark_submission_cheat`
   - `set_submission_time_spent`
   - `ingest_submissions`
4. Define supported weakness metrics.
5. Standardize JSON response shape + ordering.