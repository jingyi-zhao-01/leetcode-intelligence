# LeetCode Submissions Package

A package for managing LeetCode submissions, including tracking, statistics, and problem graph analysis.

## Architecture

This package consists of **two separate servers**:

1. **TCP Submission Server** (Port 3000): Handles submissions and timers from nvim via TCP
2. **Analytics API** (Port 8000): Read-only HTTP API for data analytics and visualization

See [ARCHITECTURE.md](./ARCHITECTURE.md) for detailed server architecture documentation.

## Features

- **TCP Submission Server**: Primary integration with LeetCode nvim plugin via TCP
  - Saves submissions to database
  - Manages problem-solving timers
  - Real-time session tracking
- **Analytics API**: Read-only data access and visualization
  - Query submission data and statistics
  - Problem graph visualization with filters
  - Overall statistics and metrics
- **CLI Tools**: Statistics and graph generation utilities

## Installation

```bash
poetry install
```

## Usage

### Start the TCP Submission Server (Port 3000)

Primary server for LeetCode nvim plugin integration:

```bash
poetry run submission-server
# or
make dev-submission
```

This is the main server that nvim connects to via TCP.

### Start the Analytics API (Port 8000)

Read-only HTTP API for data analytics and graph visualization:

```bash
poetry run analytics-server
# or
make dev-analytics
```

### View Statistics

```bash
poetry run submission-stats
```

### Generate Problem Graph

```bash
poetry run problem-graph
```

## Development

```bash
poetry install --with dev
poetry run pytest
```

## API Endpoints

### Submission Server (Port 3000 - TCP)

TCP protocol with JSON messages:
- `start_timer` - Start timer for a problem
- `stop_timer` - Stop timer and save session
- `get_active_timers` - Get active timers
- `get_active_sessions` - Get active sessions
- `save_submission` - Save new submission from nvim

### Analytics Server (Port 8000 - HTTP)

Read-only HTTP REST API:
- `GET /api/graph` - Get problem graph with filters
- `GET /api/problems/{title_slug}` - Get problem details
- `GET /api/tags` - Get all available tags
- `GET /api/stats` - Get overall statistics

## Problem Graph 

```bash
poetry run problem-graph --solved 
# This will generate graph with interrelations only on solved questions, auto convered into svg 
# for problem that is solved, it will color it based on acception rate 
# for every problem, it will have a indication whether it is easy, medium, hard 
```

```bash 
poetry run problem-graph --include-tags "Array" "Two-pointers" 
# This will generate graph with interrelations on ALL problems that contain at least 1 of the tags, while preservering the output from poetry run problem-graph --sovled 
```

```bash
poetry run problem-graph --filter-tags "Array" "Two-pointers"
# This will generate graph with interrelations on ALL problems that must contain all tags, while preserving the output from poetry run problem-graph --solved
```