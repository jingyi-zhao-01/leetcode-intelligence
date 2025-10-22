Project overview

This repository is my personal LeetCode submission history. Each file is a standalone attempt stored as Markdown (.md) containing valid Python code (headings are comments). Many problems include multiple versions (e.g., a correct solution and an intentionally buggy variant) to document thinking, pitfalls, and progress over time. Please treat the problem files as an immutable record; add new attempts rather than editing old ones.

File structure

- Flat top-level layout. Files are named <ID>_<label>.md (e.g., 001_correct.md, 001_wrong.md). Labels like correct/OK are working solutions; wrong variants capture specific mistakes (e.g., MissingTail, VisitedMarkingMissing, DPInitZero). README.md offers a brief index and may lag behind recent additions.
- Common themes: hash map/two-sum (001_*.md, 167_OK.md), sliding window/two pointers (003_*.md, 167_OK.md), dynamic programming (064_*, 072_*, 1143_*, 139_*, 152_*, 213_*, 322_*), classic data structures (020_*, 021_*, 146_*, 200_*, 704_*).

Running and quick checks

- No centralized test harness. Use Python 3.x and run files directly (they usually define classes/functions only):
  - Ad‑hoc run: python 072_correct.md
  - REPL/experiment: from runpy import run_path; ns = run_path('064_correct.md'); then call ns['Solution']().minPathSum(...)
  - For local assertions, copy to a .py file and add a small __main__ block; avoid modifying existing submission files.

Tips for new readers

- Search by ID or keyword (e.g., grep -Ri "twoSum" or "dp["). Skim both correct and wrong variants to see typical traps and their fixes. If adding more content, follow the naming convention and keep snippets self-contained.
