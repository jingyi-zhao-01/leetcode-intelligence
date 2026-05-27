# Service Runtime

This folder owns runtime composition for `leetcode-intelligence-service`.

It intentionally sits above `src/core/` so the domain layer does not need to know about:

- Prisma connection lifecycle
- OpenRouter client construction
- process entrypoints
- Discord / HTTP startup wiring

## Runtime Layout

- `contracts.ts`
  - public `IntelligenceService` interface used by HTTP and Discord entrypoints
- `composition.ts`
  - runtime dependency composition
  - groups runtime dependencies into:
    - `persistence`
    - `externalServices`
    - `domainServices`
- `intelligence-runtime.ts`
  - orchestration service that delegates to the domain plane
- `database-boundary.ts`
  - wraps runtime operations with connect / disconnect and queueing
- `index.ts`
  - public factory and exports for the runtime layer

## Why This Exists

Before this split, service composition, OpenRouter wiring, Prisma lifecycle, and domain orchestration all lived in `src/core/index.ts`.

That made the service harder to explain because the diagram boundary between:

- domain logic
- runtime orchestration
- external dependencies
- database access

was implicit.

Now those boundaries are explicit in code, which makes the D2 diagram easier to keep high-level without losing accuracy.
