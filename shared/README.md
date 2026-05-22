# Shared Assets

This directory contains shared configuration and data structures used by all services in the LeetCode analytics platform.

## Directory Structure

```
shared/
├── types/                  # Shared type definitions
├── utils/                  # Shared utility functions/modules
└── README.md               # This file
```

## Components

### Prisma Schema
The single source of truth for database schema is now located at `services/prisma/schema.prisma` and shared by all services (submission-server, mcp-server, ingestor).

**Key File**:
- `services/prisma/schema.prisma` — PostgreSQL schema definitions
  - Models: User, Problem, Submission, Session, etc.
  - Relations between entities
  - Indexes and constraints

**Usage**:
All services reference this schema during Prisma client generation:
```bash
prisma generate --schema services/prisma/schema.prisma
```

**Migrations**:
- Generated and applied from the root directory or any service directory
- All services use the same database, so migrations are centralized

### `types/` (Reserved for Future Use)
Planned location for shared TypeScript/Python type definitions or generated clients used across multiple services.

Examples:
- Shared TypeScript types exported for the frontend
- Generated API client types
- Common domain model types

### `utils/` (Reserved for Future Use)
Planned location for shared utility functions and helper modules used by multiple services.

Examples:
- Common database helpers
- Shared validation logic
- Utility functions for data processing

---

## Why Shared?

1. **Single Source of Truth**: All services connect to the same PostgreSQL database with the same schema
2. **Consistency**: Prevents schema drift or inconsistent models between services
3. **Migrations**: Database migrations are applied once and inherit to all services
4. **Dependency Management**: Services can independently depend on specific assets without coupling to each other

---

## References

- **Services**: See [services/README.md](../services/README.md)
- **Root Configuration**: See pyproject.toml and Makefile
- **Database**: Prisma documentation at https://www.prisma.io/docs/
