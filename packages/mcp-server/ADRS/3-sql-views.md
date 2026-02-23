# step-3-sql-views.md

## Objective
Introduce stable database primitives that decouple agent logic from schema changes.

## Key Results
- Analytics queries run via views instead of raw tables.
- Core overview + activity + weakness views created.
- Weakness ranking reproducible.
- Query latency acceptable.
- Indexes support view performance.

## Tasks
1. Create `v_submission_core`.
2. Create `v_question_overview`.
3. Create `v_activity_summary`.
4. Create weakness ranking views.
5. Add supporting indexes.