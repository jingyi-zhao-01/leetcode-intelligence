# Architecture Decision Records (ADRs)

This directory contains Architecture Decision Records (ADRs) for the leetcode-qa project.

## What are ADRs?

ADRs document important architectural decisions made during the development of this project. They capture:
- **Context**: What prompted the decision
- **Decision**: What we decided to do
- **Consequences**: What happens as a result
- **Rationale**: Why we chose this approach
- **Alternatives**: What else we considered

## Format

Each ADR follows this structure:

```markdown
# ADR XXX: Title

**Date**: YYYY-MM-DD
**Status**: [Proposed|Accepted|Deprecated|Superseded]
**Context**: Brief category

## Context
What problem are we solving?

## Decision
What did we decide to do?

## Rationale
Why did we decide this?

## Consequences
What are the results of this decision?

## Alternatives Considered
What else did we evaluate?

## References
Links to related resources
```

## Current ADRs

### Project Structure & Architecture

- [ADR 001: Multi-Package Monorepo Structure](.adrs/001-multi-package-monorepo-structure.md)
  - **Status**: Accepted
  - **Summary**: Use separate packages (`tailnet`, `submission_server`, etc.) instead of single monolithic package
  - **Key Decision**: Organize by deployment boundaries and reusability

- [ADR 002: Tailnet Composable Authentication](.adrs/002-tailnet-composable-authentication.md)
  - **Status**: Accepted
  - **Summary**: Create dedicated `tailnet` package for Tailscale authentication
  - **Key Decision**: Use composition pattern (middleware/wrappers) for auth across servers

### Package-Specific ADRs

Some packages maintain their own ADRs for internal decisions:

- **mcp-server**: `/packages/mcp-server/ADRS/` - MCP protocol and tool decisions
- **submission_server**: (future) - Server-specific architecture
- **graph-ui**: (future) - Frontend architecture decisions

## When to Write an ADR

Create an ADR when:

✅ **Making significant architectural decisions**
- Choosing between design patterns
- Deciding on project structure
- Adding new packages or services
- Changing core abstractions

✅ **Solving problems that might recur**
- Authentication strategy
- Deployment patterns
- Testing approach
- Data modeling decisions

✅ **Establishing conventions**
- Code organization
- Naming patterns
- API design principles

❌ **Don't write ADRs for:**
- Minor implementation details
- Temporary experiments
- Obvious/trivial decisions
- Personal preferences without trade-offs

## How to Write an ADR

### 1. Create a New File

```bash
# Next number in sequence
touch .adrs/003-your-decision-title.md
```

### 2. Use the Template

Copy from existing ADRs or use this minimal template:

```markdown
# ADR XXX: Your Title

**Date**: $(date +%Y-%m-%d)
**Status**: Proposed

## Context
[Describe the problem]

## Decision
[What you decided]

## Rationale
[Why this is best]

## Consequences
[What happens]
```

### 3. Get Review

- Commit the ADR with your changes
- Include in PR for review
- Update status to "Accepted" when merged

### 4. Link to Code

Reference ADRs in:
- Code comments: `// See ADR 002 for auth pattern`
- README files: Link to relevant ADRs
- Documentation: Include ADR context

## Status Definitions

- **Proposed**: Under discussion, not yet accepted
- **Accepted**: Decision is final and implemented
- **Deprecated**: No longer applicable, kept for history
- **Superseded**: Replaced by newer ADR (link to it)

## Numbering

- ADRs are numbered sequentially: 001, 002, 003, ...
- Numbers are never reused
- Deprecated/superseded ADRs keep their numbers

## Examples in This Project

**ADR 001** demonstrates:
- Clear problem statement (how to organize code)
- Multiple alternatives (monorepo vs single package)
- Concrete decision criteria
- Implementation guidelines
- Review triggers

**ADR 002** demonstrates:
- Technical design documentation
- Pattern justification (composition)
- Integration examples
- Connection to related ADRs

## Related Reading

- [Architecture Decision Records by Michael Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- [ADR GitHub Organization](https://adr.github.io/)
- [When to Write an ADR](https://github.com/joelparkerhenderson/architecture-decision-record)

## Project-Specific Notes

### ADR vs Package Documentation

- **ADRs**: Why we made architectural decisions
- **README/docs**: How to use the code
- **Code comments**: Implementation details

**Example:**
- ADR 002: "Why we created tailnet package and chose composition pattern"
- tailnet/README.md: "How to use tailnet in your server"
- tailnet/src/config.py: "How this config class works"

### Relationship to Planning Docs

- **.adrs/**: Architecture decisions (past tense - what and why)
- **problems/**: Problems to solve (future tense - planning)
- **packages/*/ADRS/**: Package-internal decisions (e.g., mcp-server)

### Cross-Package Decisions

Decisions affecting multiple packages go in `/.adrs/`.
Package-internal decisions can go in `/packages/xyz/ADRS/`.

Example:
- Multi-package structure: `/.adrs/001-*` (affects whole project)
- MCP tool design: `/packages/mcp-server/ADRS/1-*` (internal to mcp-server)
- Tailnet design: `/.adrs/002-*` (used by multiple packages)

---

**Last Updated**: 2026-02-27
