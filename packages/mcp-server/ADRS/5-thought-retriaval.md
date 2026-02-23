# step-5-thought-retrieval.md

## Objective
Enable reliable recall of learning insights without increasing schema complexity.

## Key Results
- Full-text search returns relevant thoughts.
- Retrieval latency acceptable.
- Snippets highlight reasoning.
- Fallback search prevents empty results.
- Retrieval improves coaching quality.

## Tasks
1. Add FTS index on `Submission.thought`.
2. Implement `search_thoughts` using FTS.
3. Return highlighted snippets.
4. Add fallback ILIKE search.
5. Add retrieval tests.