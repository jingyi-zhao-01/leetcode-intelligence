# Split Vercel BFF From The Intelligence Core Service

Date: 2026-06-12

Related:

- [README.md](../../README.md)
- [docs/architecture/README.md](../architecture/README.md)
- [services/leetcode-intelligence-service/README.md](../../services/leetcode-intelligence-service/README.md)
- [client/app/actions.ts](../../client/app/actions.ts)
- [services/leetcode-intelligence-service/src/server.ts](../../services/leetcode-intelligence-service/src/server.ts)

## Why I am writing this down

Right now the web side is convenient, but it is starting to feel too mixed together.

At the moment:

- `client/` is a Next.js app
- Vercel is hosting the UI
- some business logic is still living in server actions and route handlers
- some other business logic already lives in `services/leetcode-intelligence-service`

That was fine early on, but it is getting awkward now.

The biggest signal is that Vercel is not really building "the whole repo". It is building `client/` as its own little world.

That already caused real issues:

- cross-directory `tsconfig` broke remote Vercel builds
- cross-directory ESLint config broke remote Vercel builds
- local repo build passed while Vercel deploy still failed

So even before talking about code organization, there is already a deployment-boundary problem:

> the Vercel app needs to behave like a self-contained deployable, not like it can freely reach into the rest of the repo forever.

There is also a second problem:

`client/app/actions.ts` is starting to do too many things at once:

- web request parsing
- admin/session checks
- Prisma reads and writes
- tag governance
- cross-record validation
- shaping responses for the UI

That makes it harder to tell what is:

- just web adapter code
- actual intelligence-domain logic

And if I ever want the same logic from somewhere else, like:

- Discord
- CLI
- cron jobs
- batch scripts

then keeping it only in Next.js server actions is the wrong place.

## Decision

I am going to treat these two things differently from now on.

### 1. `client/` is the Vercel BFF

`client/` should mainly own browser-facing concerns:

- UI
- session and auth checks
- request parsing
- rate limiting
- thin server actions / route handlers
- UI-friendly response shaping

In other words, it is the BFF layer, not the long-term home for core intelligence logic.

### 2. `services/leetcode-intelligence-service` is the core service

This service should own the intelligence domain long term:

- domain rules
- scoring
- recommendation
- classification / governance logic
- persistence orchestration
- reusable APIs for non-browser callers

If some logic is likely to be reused outside the browser, it should probably live here instead of inside Next.js actions.

## Practical rule

When I add or touch intelligence-related logic, I should ask:

1. Is this purely a web/BFF concern?
2. If not, should it live in `leetcode-intelligence-service` instead?
3. Can the Next.js side just become a thin adapter over that service?

Default direction:

- reusable domain logic -> `services/leetcode-intelligence-service`
- browser-only adapter logic -> `client/`

## What should stay in the BFF

Stuff that is still reasonable in `client/`:

- admin auth and cookie/session handling
- browser request validation
- `revalidatePath` and other Next-specific glue
- thin server actions that call the core service
- UI-only shaping of results

## What should move out over time

Stuff that should gradually leave `client/app/actions.ts`:

- Prisma-heavy workflows
- tag governance logic
- cross-record mutation rules
- logic that would also make sense for Discord / CLI / cron / batch
- anything that starts feeling like the real source of truth for the intelligence domain

## Why not keep the current setup

Because it is already showing two kinds of pain:

1. deployment pain
   Vercel keeps exposing "this folder is actually its own isolated build root"

2. ownership pain
   the more logic I keep in Next.js actions, the fuzzier the boundary gets between:
   - web adapter code
   - actual intelligence-system behavior

I do not want `client/` to quietly become the real backend by accident.

## Why not move everything at once

Because that is probably overkill and risky for this project right now.

I do not need a big rewrite. I just need a clear direction and a clean extraction path.

So the plan is incremental:

1. lock the boundary mentally first
2. move the heaviest/reusable logic first
3. let `client/` shrink into a proper BFF over time

## First extraction targets

The first things to move out of `client/app/actions.ts` should be:

- tag governance
- `PatternTag` / `SubmissionPatternTag` mutations
- Prisma transaction-heavy logic
- any write flow that I may want to reuse from other surfaces later

## Desired end state

Over time I want this shape:

- `client/`
  thin web layer, thin BFF, self-contained for Vercel

- `services/leetcode-intelligence-service`
  the actual long-term home of intelligence domain behavior

That should make both the deploy story and the architecture story much less annoying.
