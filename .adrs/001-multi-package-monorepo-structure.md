# ADR 001: Multi-Package Monorepo Structure

**Date**: 2026-02-27  
**Status**: Accepted  
**Context**: Project architecture and code organization

## Context

The leetcode-qa project has evolved to include multiple services and components:
- Backend services (submission server, analytics API, MCP server)
- Frontend application (Next.js graph UI)
- Shared libraries (ingestor, tailnet authentication)
- Different runtimes (Python, Node.js)

We needed to decide between:
1. **Multi-package monorepo**: Separate packages under `packages/` directory
2. **Single package with services**: All Python code under one `src/` directory

## Decision

We will use a **multi-package monorepo structure** with packages organized by deployment boundaries and reusability.

### Package Structure

```
packages/
├── tailnet/              # Reusable authentication library
├── submission_server/    # Backend services (TCP + FastAPI)
├── mcp-server/          # MCP protocol server
├── ingestor/            # Batch processing/data ingestion
└── graph-ui/            # Next.js frontend application
```

## Rationale

### Why Multi-Package

1. **Independent Deployment Cycles**
   - `tailnet` is stable and changes infrequently
   - `submission_server` deploys to VPS
   - `graph-ui` deploys to Vercel/static hosting
   - `mcp-server` runs as stdio-based tool
   - Each can be versioned and deployed independently

2. **Different Dependency Requirements**
   - `tailnet`: Minimal deps (pydantic only)
   - `submission_server`: Database-heavy (prisma, fastapi)
   - `graph-ui`: Node.js ecosystem (React, Next.js)
   - `mcp-server`: MCP-specific (fastmcp)
   - Prevents dependency conflicts and bloat

3. **Clear Reusability**
   - `tailnet` is a composable library used by multiple servers
   - Could be extracted to separate repo or open-sourced
   - Clean API boundaries enforce good design
   - Other projects could depend on specific packages

4. **Mixed Language Support**
   - Python packages and TypeScript packages coexist
   - Each has appropriate build tooling
   - Language-specific best practices preserved

5. **Team/Ownership Boundaries**
   - Security team could own `tailnet`
   - Backend team owns servers
   - Frontend team owns `graph-ui`
   - Clear ownership model as team grows

6. **Appropriate Granularity**
   - Each package is substantial (>500 LOC)
   - Packages don't always deploy together
   - No circular dependencies
   - Each has clear, single responsibility

### Why Not Single Package

A single package approach would force:
- All Python code to share dependencies (version conflicts)
- Everything to deploy together (coupling)
- Mixed language code in unnatural structure
- Shared `requirements.txt` with conflicting needs
- Loss of reusability (can't import `tailnet` elsewhere)

## Consequences

### Positive

✅ **Flexibility**: Services deploy independently  
✅ **Reusability**: Libraries can be shared/extracted  
✅ **Clarity**: Clear boundaries and responsibilities  
✅ **Scalability**: Easy to add new packages  
✅ **Composability**: `tailnet` exemplifies good design  
✅ **Mixed runtimes**: Python + Node.js coexist naturally

### Negative

⚠️ **Complexity**: More `pyproject.toml` files to maintain  
⚠️ **Dependencies**: Must explicitly declare inter-package deps  
⚠️ **Installation**: Need to install multiple packages  
⚠️ **Path management**: Requires proper Python path handling

### Mitigations

- Use workspace-relative imports where possible
- Document installation in each package's README
- Consider monorepo tools (Poetry workspaces, uv workspaces) if overhead grows
- Keep package count reasonable (5-10 max)

## Implementation

### Package Guidelines

A new package is warranted when:
- ✅ Independent deployment is needed
- ✅ Different dependency set is required
- ✅ Code is reusable across projects
- ✅ Different team/owner
- ✅ Different runtime/language
- ✅ >500 lines of cohesive code

Do NOT create a new package when:
- ❌ Code is <500 lines
- ❌ Always deploys with parent service
- ❌ Shares all dependencies
- ❌ Would create circular dependencies
- ❌ Is tightly coupled to one service

### Current Package Rationale

| Package | Justification |
|---------|--------------|
| `tailnet` | ✅ Reusable library, minimal deps, composable design |
| `submission_server` | ✅ Independent service, unique deps (prisma) |
| `mcp-server` | ✅ Different protocol, stdio-based, separate use case |
| `ingestor` | ✅ Batch processing, different resource profile |
| `graph-ui` | ✅ Different runtime (Node.js), separate deployment |

## Examples

### Good: Adding a New Service
```
# New service with unique protocol -> New package
packages/websocket_server/
```

### Good: Extracting Shared Logic
```
# Common utilities used by all servers -> New library package
packages/leetcode_common/
```

### Bad: Over-Separation
```
# Bad: Feature-per-package (always deploy together)
packages/user_auth/
packages/user_profile/
packages/user_settings/

# Better: Single package
packages/user_service/
  src/
    auth.py
    profile.py
    settings.py
```

## Review Criteria

Review this decision when:
- Adding 6th+ package (might need better tooling)
- Packages frequently updated together (might be too granular)
- Circular dependencies emerge (wrong boundaries)
- Significant deployment coupling appears (reconsider boundaries)

## References

- [INTEGRATION_SUMMARY.md](/packages/tailnet/INTEGRATION_SUMMARY.md) - Example of composable package design
- Package structure inspired by: Nx, Turborepo, Poetry workspaces
- Composition pattern: [tailnet package](/packages/tailnet/)

## Notes

This structure emerged organically as the project grew. The `tailnet` package, created to solve authentication across multiple servers, validated the multi-package approach by demonstrating clear reusability and composition benefits.
