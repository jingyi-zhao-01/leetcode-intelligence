# LeetCode Problem Graph Visualization

Full-stack web application for visualizing LeetCode problem relationships with acceptance rates, filtering, and interactive exploration.

## Architecture

- **Backend**: FastAPI (Python) on port 8000 (unified submissions + graph API)
- **Frontend**: Next.js (TypeScript + React) on port 3000
- **Visualization**: D3-force for interactive graph
- **Database**: PostgreSQL via Prisma

## Quick Start

### 1. Install Dependencies

```bash
cd packages
make install-all
```

### 2. Setup Environment

```bash
# Ensure DATABASE_URL is set in packages/submissions/.env
cd submissions
cat .env  # Should contain DATABASE_URL
```

### 3. Generate Prisma Client

```bash
cd packages
make prisma-generate-all
```

### 4. Start Services (Two Terminals)

**Terminal 1 - Backend:**
```bash
cd packages
make dev-backend
# Backend will run on http://localhost:8000
# API docs available at http://localhost:8000/docs
```

**Terminal 2 - Frontend:**
```bash
cd packages
make dev-frontend
# Frontend will run on http://localhost:3000
```

### 5. Open Browser

Navigate to `http://localhost:3000` to see the interactive graph!

## Features

### Backend (submissions)
- `/api/graph` - Get problem graph with filters (solved, includeTags, filterTags, limit)
- `/api/problems/{slug}` - Get detailed problem info with submission history
- `/api/tags` - Get all available topic tags
- `/api/stats` - Get overall statistics
- `/api/timers/*` - Timer management endpoints (start, stop, active)
- `/api/sessions/active` - Get active problem sessions
- `/api/submissions` - Save submission with acceptance tracking
- Calculates acceptance rates from submission data
- Builds graph edges from explicit relationships + tag similarity (2+ shared tags)

### Frontend (graph-ui)
- **Interactive D3-force graph** with pan, zoom, drag
- **Filter controls**: Solved only, include tags (OR), filter tags (AND), custom limit
- **Problem details sidebar**: Shows acceptance rate, tags, submission history, related problems
- **Real-time stats**: Total problems, edges, solved count
- **Visual indicators**: 
  - Node color: Difficulty-based (will add acceptance rate gradient later)
  - Node border: Difficulty color (Easy=green, Medium=orange, Hard=red)
  - Edge style: Solid blue (explicit), dashed gray (tag similarity)

## Development

### Backend Commands
```bash
cd packages/submissions
make install      # Install dependencies
make dev-api      # Start unified API server
make prisma-generate  # Generate Prisma client
make clean        # Clean artifacts
```

### Frontend Commands
```bash
cd packages/graph-ui
make install      # Install dependencies
make dev          # Start dev server
make build        # Build production
make clean        # Clean artifacts
```

### Root Commands
```bash
cd packages
make install-all          # Install both packages
make dev-backend          # Start backend
make dev-frontend         # Start frontend
make clean-all           # Clean both packages
make prisma-generate-all  # Generate Prisma for backend
```

## TODO / Future Enhancements

- [ ] Add acceptance rate-based color gradient (currently using difficulty colors)
- [ ] Implement centralizing logic for solved problems in graph layout
- [ ] Add tag multi-select dropdowns (currently text input)
- [ ] Export graph as PNG/SVG
- [ ] Highlight related problems on graph when viewing details
- [ ] Add search functionality for problem names
- [ ] Show learning paths (BFS from selected node)
- [ ] Performance optimizations for large graphs

## Project Structure

```
packages/
├── Makefile                      # Root commands for both packages
├── submissions/                  # FastAPI backend (unified)
│   ├── src/
│   │   ├── api_server.py        # Unified FastAPI app (graph + submissions)
│   │   ├── graph_models.py      # Pydantic response models (camelCase)
│   │   ├── graph_service.py     # Graph building logic
│   │   ├── submission_server.py # Legacy TCP server
│   │   ├── timer_service.py     # Timer management
│   │   └── code_cleaner.py      # Code normalization
│   ├── prisma/
│   │   └── schema.prisma        # Database schema
│   ├── pyproject.toml
│   └── Makefile
└── graph-ui/                     # Next.js frontend
    ├── app/
    │   └── page.tsx             # Main page with graph
    ├── components/
    │   └── ForceGraph.tsx       # D3-force graph component
    ├── types/
    │   └── api.ts               # TypeScript API types
    ├── lib/
    │   └── api.ts               # API client
    ├── package.json
    └── Makefile
```

## Notes

- Default graph limit: 3000 problems (total LeetCode problem space ~3000)
- Filters are applied server-side for performance
- Graph loads all filtered results in one API call (no pagination for POC)
- Acceptance rates calculated from personal submission history
- Tag similarity requires 2+ shared tags to create edge
