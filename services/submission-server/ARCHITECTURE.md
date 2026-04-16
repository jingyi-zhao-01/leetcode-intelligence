# Server Architecture

## Overview

The LeetCode submissions system consists of **two separate servers**, each serving a distinct purpose:

## 1. TCP Submission Server (Port 3000)
**File**: `submission_server.py`  
**Purpose**: Direct TCP connection for nvim plugin integration  
**Protocol**: TCP with JSON over newline  

### Features:
- Receives submissions directly from nvim via TCP
- Manages timers for problem-solving sessions
- Saves submissions to database
- Handles timer operations (start/stop/get active)

### Endpoints (TCP Actions):
- `start_timer` - Start timing a problem session
- `stop_timer` - Stop timer and save session
- `get_active_timers` - Get all active timers
- `get_active_sessions` - Get active sessions
- `save_submission` - Save submission to database

### Usage:
```bash
poetry run submission-server
```

### Client (nvim):
Uses `submission_db_saver.lua` to communicate via netcat (`nc`)

---

## 2. Analytics API (Port 8000)
**File**: `analytics_server.py`  
**Purpose**: Read-only HTTP API for data analytics and visualization  
**Protocol**: HTTP/REST (FastAPI)

### Features:
- Read-only analytics on submission data
- Problem graph visualization with filters
- Statistics and metrics
- CORS enabled for frontend integration

### Endpoints:
- `GET /api/graph` - Get problem graph with filters
- `GET /api/problems/{title_slug}` - Get problem details
- `GET /api/tags` - Get all available tags
- `GET /api/stats` - Get overall statistics

### Usage:
```bash
make dev-analytics
# or
poetry run analytics-server
```

---

## Port Summary

| Server | Port | Purpose | Protocol | Client |
|--------|------|---------|----------|--------|
| TCP Submission Server | 3000 | nvim submissions & timers | TCP/JSON | nvim via netcat |
| Analytics API | 8000 | Read-only data analytics | HTTP/REST | Frontend/API consumers |

---

## Architecture Principles

### Separation of Concerns

1. **Write Operations (Port 3000)**
   - All data mutations (submissions, timers)
   - Stateful timer management
   - Optimized for nvim integration via TCP

2. **Read Operations (Port 8000)**
   - All data queries and analytics
   - Stateless HTTP API
   - Optimized for frontend/dashboard consumption

### Why TCP for Submissions?

- **Simplicity**: nvim can use `nc` (netcat) without HTTP libraries
- **Efficiency**: Direct socket connection, minimal overhead
- **Reliability**: Already implemented and working well

### Why HTTP for Analytics?

- **Standard**: REST API for frontend integration
- **CORS**: Easy browser access
- **Documentation**: Auto-generated Swagger docs at `/docs`

---

## Recommendations

1. **Keep TCP Server (Port 3000)** for nvim - it's working perfectly
2. **Use Analytics API (Port 8000)** for:
   - Frontend dashboards (e.g., Next.js on port 3000)
   - Data exploration and visualization
   - Third-party integrations
   - API consumers

3. **Never mix concerns**: 
   - Submission server = write operations only
   - Analytics server = read operations only
