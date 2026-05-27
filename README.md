
# LeetCode Intelligence

## WHY
a systematic way to handle leetcode solving to manage the entire life cycle:
- How to get immediate feedback to understand which part of the code block is wrong ? is the reason due to not adequately understanding the problem or inproficiency of the syntax ? 
- How to persistently store my submissions overtime so i can understand the full evlution of a specific problem or a specific type of problem ?
- How to manage frictionless refresh of my understanding on solved problem ? 
- How to identify weak spot and plan triage on specific topics ?



## Overview

an AIO solution for tracking LeetCode submissions, analyzing problem-solving evolution, and receiving rule based recommendations (GenAI optional).

![System architecture](./architecture.svg)

## Services

| Service | Ports | Protocol | Description |
|---------|------|----------|-------------|
| **Submission Service** | 3000, 8000 | TCP, HTTP | Submission tracking & analytics API |
| **MCP Service** | stdio | MCP | LLM integration for submission analysis |
| **Intelligence Service** | HTTP, Discord | HTTP | Prompt scoring & recommendations |
| **Ingestor** | CLI | Python | ETL for LeetCode problem ingestion |

### 1. Submission Service

Dual-server backend for receiving and analyzing LeetCode submissions.

- **TCP Submission Server (Port 3000)**: Receives code submissions from the Neovim plugin via JSON-over-newline protocol
- **Analytics API (Port 8000)**: HTTP REST API (FastAPI) for data analytics and visualization

Key features:
- Saves submissions to PostgreSQL database
- Tracks problem-solving timers (start/stop/get active)
- Constructs problem relationship graphs

### 2. MCP Service

Model Context Protocol server for LLM integration. Provides tools for:
- Analyzing submission evolution
- Problem discovery and history
- Solution review

### 3. Intelligence Service

TypeScript service for prompting, scoring, and recommendations:
- Prompt dispatcher (scheduled Discord prompts)
- Prompt response listener and scorer
- Focus recommender


### 5. Ingestor

Python ETL service for ingesting LeetCode problems from the LeetCode API.

### Shared Configuration

All services share:
- **Prisma Schema**: `services/shared/prisma/schema.prisma`
- **Database**: Single PostgreSQL instance

## Docker Compose (submission_server + mcp-server)

You can run the two backend services with Docker Compose:

- `submission_server` on TCP `3000`
- `mcp_server` in MCP `stdio` mode

### Prerequisites

- Docker + Docker Compose installed
- `.env` exists at project root and contains `DEV_DB_URL` and `PROD_DB_URL`

### Start

```bash
make compose-build ENV=dev
make compose-up ENV=dev
```

For production DB URL:

```bash
make compose-up ENV=prod
```

### Stop

```bash
make compose-down ENV=dev
```

### Notes

- Compose uses `DATABASE_URL`, passed by `Makefile` from `ENV`:
  - `ENV=dev` → `DEV_DB_URL`
  - `ENV=prod` → `PROD_DB_URL`
- `submission_server` is configured with `SUBMISSION_HOST=0.0.0.0` so port publishing works.
- `mcp_server` uses `mcp-server-stdio`; it does not expose an HTTP port in this setup.

## Submission Service Image

Build the standalone `leetcode-submission-service` image:

```bash
docker build -f docker/leetcode-submission-service.Dockerfile -t leetcode-submission-service:latest .
```

Run it with your database URL:

```bash
docker run --rm -p 3000:3000 \
  -e DATABASE_URL="postgresql://..." \
  leetcode-submission-service:latest
```

## MCP Features for Submission Evolution

### 1. Submission Timeline Analysis
- **Track all attempts** for a specific problem over time
- **Identify improvement patterns** in code quality and approach
- **Analyze success/failure progression** 

### 2. Thought Evolution Tracking
- **Extract comments** from each submission to understand thought process
- **Compare reasoning** between early and later attempts
- **Identify learning patterns** and conceptual breakthroughs

### 3. Code Quality Metrics
- **Complexity reduction** over time
- **Performance improvements** (time/space complexity)
- **Code readability** and style evolution

### 4. LLM Integration Capabilities
When connected to an LLM via MCP, the system can answer:

- *"How did my approach to two-sum problem evolve over time?"*
- *"What were my initial thoughts vs. final solution for binary search problems?"*
- *"Show me the progression of my understanding of dynamic programming"*
- *"Which problems took me the most attempts to solve correctly?"*
- *"How did my commenting style and problem analysis improve?"*

## Flow Description

1. **Code Submission**: Neovim plugin captures code with inline comments
2. **Processing**: Code cleaned while preserving comments for semantic analysis
3. **Storage**: Timestamped submissions with both cleaned and raw versions
4. **MCP Analysis**: LLM queries submission history for evolution insights
5. **Thought Tracking**: Comments analyzed for learning progression

---

## `submission_server` Package Structure

The `packages/submission_server` package is the core backend responsible for receiving, storing, and serving submission data.

```
packages/submission_server/
├── pyproject.toml              # Package config & script entry points
├── Makefile                    # Dev targets (dev, dev-api, install, clean)
├── ARCHITECTURE.md             # Server design overview (TCP vs HTTP)
├── README.md                   # Package-level docs
├── docs/
│   └── agenda.md               # Development agenda & notes
├── tests/
│   ├── test_code_cleaner.py    # Unit tests for code cleaning logic
│   └── test_submission_db_saver.lua  # Integration test for Lua TCP client
└── src/
    ├── submission_server.py    # TCP server (port 3000) — nvim integration
    │                           #   Actions: save_submission, start_timer (via start_session),
    │                           #            stop_timer, get_active_timers
    ├── analytics_server.py     # HTTP/REST API (port 8000) — read-only analytics
    │                           #   GET /api/graph, /api/problems/{slug},
    │                           #        /api/tags, /api/stats
    ├── code_cleaner.py         # Strips boilerplate, preserves inline comments
    ├── submission_db_saver.lua # Lua client for nvim → TCP server communication
    ├── graph_models.py         # Pydantic models for problem graph API
    ├── graph_service.py        # Graph construction (tag similarity + explicit edges)
    ├── problem_graph.py        # CLI entry point: generate/export problem graph
    ├── submission_stats.py     # CLI entry point: print submission statistics
    └── timer_service.py        # In-memory timer state management
```

### Design Decisions

| Component | Protocol | Port | Purpose |
|---|---|---|---|
| `submission_server.py` | TCP + JSON-newline | 3000 | Low-latency write path from nvim via `nc` |
| `analytics_server.py` | HTTP/REST (FastAPI) | 8000 | Read-only analytics; CORS-enabled for frontend |
| `submission_db_saver.lua` | TCP client | — | Lua wrapper used by the Neovim plugin |
| `code_cleaner.py` | — | — | Normalises code before DB storage while keeping comments |
| `timer_service.py` | — | — | Tracks per-problem solve-time sessions in memory |

### Why is there a Timer?

The timer answers a key analytics question: **how long did it actually take to solve a problem?**

Submission count and code evolution tell you *what* changed, but time-spent tells you *how hard* the problem was at each attempt. This unlocks metrics like:

- Which problems caused the longest struggle before acceptance
- Whether solve time decreases on revisit (a concrete measure of learning)
- Correlating time-per-attempt with the type of mistake made

#### Timer Lifecycle

```
Open problem in Neovim
        │
        ▼
  start_timer (title_slug)          ← sent by Lua plugin via `Leet session start`
  [in-memory: timers[slug] = now()]
        │
        │  (coding happens)
        │
        ▼
  save_submission (title_slug, code, item)
        │
        ├─ timer active? → attach elapsed minutes to submission row (timeSpentMinutes)
        │
        ├─ status == "Accepted"?
        │       ├── stop timer  → persist ProblemSession to DB
        │       └── restart timer  (tracks time for any follow-up attempt)
        │
        └─ status != "Accepted"?  → timer keeps running (accumulates across failed attempts)
```

#### Key Behaviours

| Situation | Behaviour |
|---|---|
| Opening a new problem | `Leet session start` clears any other active timer and starts fresh (only one active problem at a time by default) |
| Failed submission | Timer keeps running; elapsed time is still snapshotted onto the submission row |
| Accepted submission | Timer is stopped → session saved to `ProblemSession` table → timer restarted for follow-up work |
| Code contains `#TEST#` | Submission is **skipped entirely** — not saved, timer unaffected |
| Code contains `#CHEAT#` | Submission saved with `isCheat = true` flag for later revisit |
| Server restart | In-memory timers are lost; DB sessions already committed are retained |

#### Storage

- **`Submission.timeSpentMinutes`** — elapsed minutes at the moment a submission is saved (snapshot, not total)
- **`ProblemSession`** — a dedicated table recording completed sessions (stopped timers), enabling total-time-per-problem queries independent of submission count