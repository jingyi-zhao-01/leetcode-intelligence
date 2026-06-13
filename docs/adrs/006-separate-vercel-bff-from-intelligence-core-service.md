# Keep Vercel Thin, Move Core Logic To The Intelligence Service

Date: 2026-06-12

Related:

- [client/app/actions.ts](../../client/app/actions.ts)
- [services/leetcode-intelligence-service/src/server.ts](../../services/leetcode-intelligence-service/src/server.ts)
- [client/eslint.config.mjs](../../client/eslint.config.mjs)
- [client/tsconfig.json](../../client/tsconfig.json)

## Why this ADR exists

This one is mostly me writing down a pattern that kept showing up while fixing real issues.

The web app is deployed from `client/` on Vercel, but some of the actual intelligence logic is still split between:

- Next.js server actions / route handlers
- `services/leetcode-intelligence-service`

That was fine at first, but the boundary has been getting messy.

## Problems I actually ran into

### 1. Vercel treats `client/` like its own world

This was the first big signal.

A few times, local checks passed, but Vercel still failed because `client/` was not self-contained enough:

- root ESLint config vs `client/` ESLint config
- root/shared TypeScript config vs what Vercel can see from `client/`
- local repo build passing while remote Vercel build still broke

So even before architecture purity, there is a practical rule here:

> if Vercel deploys `client/`, then `client/` has to be able to stand on its own.

### 2. `client/app/actions.ts` is starting to feel like backend code

The server actions are not just doing web glue anymore.

They are gradually taking on things like:

- auth/session checks
- Prisma reads and writes
- tag mutation rules
- cross-record validation
- transaction-heavy flows

That is the point where BFF code starts quietly turning into the real backend.

### 3. The same logic wants to be reused outside the web app

A lot of the interesting logic here is not really "for Next.js".

It could also be used by:

- Discord flows
- cron jobs
- CLI tools
- local automation

Once that is true, it is a bad fit for the logic to live only inside Vercel-facing server actions.

## Decision

I am going to treat the two sides differently.

### `client/` is the BFF

`client/` should stay thin and own browser-facing concerns:

- UI
- auth/session glue
- request validation
- server actions as adapters
- Next.js-specific cache / revalidation behavior

It can still have server code, but that code should mostly be adapter code.

### `services/leetcode-intelligence-service` is the real backend

This service should own the reusable domain behavior:

- recommendation logic
- scoring / analysis flows
- pattern tag rules
- DB orchestration
- logic that may be used by non-browser callers

If something feels like actual product behavior rather than web glue, it should probably live here.
