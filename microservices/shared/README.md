# Shared Assets

This directory contains shared configuration and data structures used by all services in the LeetCode analytics platform.

## Directory Structure

```
shared/
├── prisma/
│   ├── schema.prisma       # Shared Prisma database schema
│   └── migrations/         # (if migrations are versioned)
├── types/                  # Shared type definitions
├── utils/                  # Shared utility functions/modules
└── README.md               # This file
```

## Components

### `prisma/`
Contains the single source of truth for database schema shared by all services (submission-server, mcp-server, ingestor).

**Key Files**:
- `schema.prisma` — PostgreSQL schema definitions
  - Models: User, Problem, Submission, Session, etc.
  - Relations between entities
  - Indexes and constraints

**Usage**:
All services reference this schema during Prisma client generation:
```bash
prisma generate --schema shared/prisma/schema.prisma
```

**Migrations**:
- Generated and applied from the root directory or any service directory
- All services use the same database, so migrations are centralized

### `types/` (Reserved for Future Use)
Planned location for shared TypeScript/Python type definitions or generated clients used across multiple services.
