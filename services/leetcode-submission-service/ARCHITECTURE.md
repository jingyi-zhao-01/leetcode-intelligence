# LeetCode Submission Service Architecture

This service is a local TCP server that accepts newline-delimited JSON requests from `leetcode.nvim`. Its responsibilities are intentionally narrow:

- manage one active timer/session for a problem at a time
- accept and persist submission records
- run static failure analysis using LLM on test on submit failure and send structured lines of problem to vim for rendering so i immediately get feedbacks on whats wrong :D

- it can also use a sqlite for simplicity but remote database is chosen because I have a PC and personally travel a lot with Laptop,
- my laptop and PC has been registered as data plane nodes on my own native home cloud platform so every new changes here will be target deployed and always available on whatever devices that are active with me:D 


The canonical component diagram lives in [architecture.d2](./architecture.d2).

![Submission service architecture](./architecture.svg)

## Runtime Overview

The service starts in [src/server.ts](./src/server.ts). `SubmissionServer` opens a TCP listener, parses one JSON request per line, dispatches by `action`, and returns a JSON response on the same socket.

The supported actions are:

- `start_timer`
- `stop_timer`
- `drop_timer`
- `get_active_timers`
- `get_active_sessions`
- `get_past_submissions`
- `save_submission`
- `analyze_failure`

## Main Components

### SubmissionServer

[src/server.ts](./src/server.ts) owns the top-level runtime:

- TCP socket lifecycle
- request parsing and action dispatch
- Prisma client initialization
- startup database diagnostics and connection logging
- composition of timer, cache, middleware, and failure-analysis dependencies

This file also contains the submission preparation helpers used before a submission is cached or persisted.

### TimerManager

[src/timer.ts](./src/timer.ts) keeps the active solving session in memory.

- only one active timer is kept at a time
- starting a new timer can evict the previous active problem
- stop/get operations report elapsed minutes
- active sessions are derived directly from in-memory timer state

### Cache and Action Middleware

[src/cache.ts](./src/cache.ts) stores recent submissions per `title_slug` in memory. It is optimized for the user-facing behavior that a just-saved submission should be readable immediately, even before asynchronous database persistence finishes.

[src/action-middleware.ts](./src/action-middleware.ts) provides two reusable patterns:

- read-through behavior for `get_past_submissions`
- write-through behavior for `save_submission`

The flow is:

1. `save_submission` creates a pending summary and writes it into the cache.
2. The API responds immediately.
3. Persistence continues asynchronously through Prisma.
4. Once persistence succeeds, the cache entry is marked with the real database ID.

For reads, cached entries are returned first; persisted rows are fetched and merged only when needed.

### Submission Preparation Pipeline

Before persistence, [src/server.ts](./src/server.ts) derives extra metadata from the submission:

- test submission detection
- `#CHEAT#` marker detection
- elapsed timer minutes
- normalized content for storage/embedding
- extracted thought text from the submission body

[src/codeCleaner.ts](./src/codeCleaner.ts) supplies the normalization helpers used in this step.

### Failure Analysis

Failure analysis is split into a small facade plus an OpenRouter-backed implementation:

- [src/failureAnalysis.ts](./src/failureAnalysis.ts): request/result contracts and analyzer construction
- [src/staticAnalysis.ts](./src/staticAnalysis.ts): prompt construction, OpenRouter call, response parsing, and retrieval timing logs
- [src/failureAnalysisParser.ts](./src/failureAnalysisParser.ts): JSON extraction and annotation sanitization

The `analyze_failure` action accepts question context, editor content, submitted code, testcase, and judge result data. The analyzer sends a structured prompt to OpenRouter and returns:

- a short Chinese summary
- a bounded list of line annotations with severity and reason

## Persistence Layer

[src/database.ts](./src/database.ts) normalizes `DATABASE_URL`, especially for pooler-style connections, and exposes startup diagnostics.

[src/server.ts](./src/server.ts) creates a `PrismaClient` and uses the `submission` table for:

- inserting new submission records
- reading recent submissions by `titleSlug`

The service persists:

- cleaned submission content
- status
- cheat/test metadata
- elapsed time
- extracted thought text
- raw submission details payload

## Logging

[src/logger.ts](./src/logger.ts) defines the shared Pino logger and child scopes. Current log streams include:

- server lifecycle and request handling
- cache reads/writes/merges
- timer lifecycle
- database connection timing
- failure-analysis timing and error reporting

## Request Flows

### Save Submission

1. Client sends `save_submission` over TCP.
2. `SubmissionServer` validates and shapes the request.
3. Submission helpers derive timer/test/cheat/content metadata.
4. Write-through middleware stores a pending entry in the in-memory cache.
5. Response is returned immediately.
6. Prisma persistence runs asynchronously.
7. Cache entry is updated with the persisted database ID.

### Get Past Submissions

1. Client sends `get_past_submissions` with `title_slug` and optional `limit`.
2. Read-through middleware checks the in-memory cache.
3. If the cache is insufficient, Prisma fetches recent rows.
4. Persisted rows are merged into cache and returned.

### Analyze Failure

1. Client sends `analyze_failure` with editor/question/judge context.
2. `SubmissionServer` builds a typed analysis request.
3. The default analyzer delegates to the OpenRouter-backed static analyzer.
4. OpenRouter returns structured JSON.
5. The parser sanitizes summary and line annotations.
6. The service returns the final summary and annotations to the client.

## Current Boundaries

This service is currently a single local runtime with ephemeral in-memory state for timers and recent submission cache. If the process restarts:

- active timers are lost
- cache contents are lost
- persisted submissions remain available through PostgreSQL

That tradeoff matches the current use case: fast local UX for `leetcode.nvim`, with the database acting as the durable record.
