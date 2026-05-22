# LeetCode Services

This directory contains standalone microservices for the LeetCode analytics platform.

## Services

### 1. **leetcode-submission-service** — Submission Tracking & Analytics Backend
Dual-server backend for receiving and analyzing LeetCode submissions.

**Components**:
- **TCP Submission Server (Port 3000)**: Receives code submissions from the Neovim plugin via JSON-over-newline protocol
- **Analytics API (Port 8000)**: HTTP REST API (FastAPI) for data analytics and visualization

**Key Features**:
- Saves submissions to PostgreSQL database
- Tracks problem-solving timers (start/stop/get active timers)
- Constructs problem relationship graphs
- Serves submission and timing statistics

**Entry Points**:
- `submission-server` — Start TCP server
- `analytics-server` — Start HTTP analytics API
- `submission-stats` — CLI for viewing submission statistics
- `problem-graph` — CLI for generating problem graphs

**Database**: PostgreSQL via Prisma ORM

---

### 2. **leetcode-mcp-service** — Model Context Protocol Server
LLM integration server for analyzing submission evolution and helping AI assistants understand coding patterns.

**Features**:
- Analyzes thought progression by comparing code comments across attempts
- Provides problem discovery, submission history, and solution review tools
- Exposes tools via MCP protocol for LLM clients (Claude, GPT, etc.)

**Entry Points**:
- `mcp-server` — HTTP server mode
- `mcp-server-stdio` — Standard I/O mode (for VS Code and other editors)
- `mcp-server-dev` — Development mode with auto-reload

**Database**: PostgreSQL via Prisma ORM  
**Depends On**: leetcode-submission-service (shares the same database)

---

### 3. **ingestor** — Problem Ingestion Service
ETL service for ingesting LeetCode problems from the LeetCode API into the database.

**Features**:
- Fetches problem data from LeetCode platform
- Normalizes and stores in PostgreSQL
- Handles problem metadata (difficulty, tags, related problems)

**Entry Points**:
- `ingest-problems` — Run problem ingestion

**Database**: PostgreSQL via Prisma ORM

---

### 4. **leetcode-intelligence-service** — Prompting, Scoring & Recommendations
TypeScript service for prompting solutions, scoring replies, and generating focus recommendations.

**Entry Points**:
- `intelligence-cli` — One-off CLI prompt/response session
- `intelligence-server` — HTTP API server
- `intelligence-prompt-dispatch` — Scheduled prompt dispatcher
- `intelligence-prompt-listener` — Always-on prompt response listener
- `intelligence-recommender` — Periodic focus recommender

**Database**: PostgreSQL via Prisma ORM

---

## Shared Configuration

All services share:
- **Prisma Schema**: `services/shared/prisma/schema.prisma`
- **Environment**: `.env` file at repository root with `DATABASE_URL`

## Running Services

### Local Development

```bash
# Install dependencies (from repo root)
make install

# Set environment (from repo root or service directory)
export DATABASE_URL="postgresql://user:pass@localhost/leetcode_db"

# Start individual services
make submission        # TCP server + analytics API
make mcp              # MCP server
make test             # Run all tests
```

### Docker Compose

```bash
docker-compose up -d
# Starts both submission_server and mcp_server in containers
```

## Workspace Structure

Each service is a Python package with:
```
service-name/
├── pyproject.toml          # Package metadata, dependencies, entry points
├── src/
│   ├── <service>.py        # Main module(s)
│   └── ...
├── tests/
│   └── test_*.py
└── README.md
```

## Dependencies

- **Python**: ≥ 3.12
- **Database**: PostgreSQL 12+
- **Package Manager**: `uv`

All services use the shared Prisma schema at `services/shared/prisma/schema.prisma` and depend on a single PostgreSQL database.
