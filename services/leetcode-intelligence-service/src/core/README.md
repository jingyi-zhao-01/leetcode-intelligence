# Intelligence Module

This folder contains the domain logic for the intelligence service. It is the layer that:

- selects a past LeetCode submission to revisit
- builds a prompt for the user
- scores the user's reply
- updates per-question learning weights
- recommends which questions to focus on next

## Files

- `index.ts`: orchestration entrypoint used by the service runtime
- `env.ts`: environment parsing and defaults
- `types.ts`: shared domain types
- `shared/weight.ts`: shared weight semantics used by both cores
- `evaluation/`: prompt generation, scoring, and reply evaluation
- `recommendation/`: focus recommendation ranking and narrative generation

## Core Layout

The intelligence domain is split into two cores that share one abstract weight model.

- `evaluation core`
  - `evaluation/prompt.ts`
  - `evaluation/scoring.ts`
  - `evaluation/response.ts`
- `recommendation core`
  - `recommendation/index.ts`
- `shared weight model`
  - `shared/weight.ts`

The shared weight layer defines the common meaning of a question weight:

- default weight for unseen questions
- minimum selection weight for weighted sampling
- score-to-weight update delta
- bounded next weight computation
- normalized weight signal for recommendations

## End-to-End Flow

1. `IntelligenceService.triggerPrompt()` calls `PromptGenerator.generate()`.
2. `PromptGenerator` loads recent submissions, joins them with question metadata and existing weights, and performs weighted random selection.
3. A prompt event is persisted to `intelligencePromptEvent`.
4. The client layer sends the prompt to Discord or CLI.
5. A reply comes back through `scorePromptReply()` or `scorePromptReplyByMessageId()`.
6. `PromptResponseService` asks `ReplyScorer` for a structured score.
7. The reply, score, and updated weight are written in one transaction.
8. `FocusRecommendationService` uses the accumulated weights and history to rank what to practice next.

## Prompt Selection

Prompt selection happens in `evaluation/prompt.ts`.

- The service reads recent submissions, capped by `INTELLIGENCE_MAX_CANDIDATES`.
- It keeps only the first `INTELLIGENCE_SELECTION_WINDOW` viable candidates.
- Each candidate gets a selection weight from `intelligenceWeight.weight`.
- If a question has no recorded weight yet, it defaults to `1`.
- Final selection is weighted random, not pure top-1.

This means weaker questions are more likely to resurface, but the system still keeps some variety.

## Reply Scoring

Reply scoring happens in `evaluation/scoring.ts`.

Primary path:

- If `OPEN_ROUTER_API_KEY` is present, the service sends the prompt context, prior submission, and raw reply to OpenRouter.
- The model is asked to return structured JSON with:
  - `score` in the range `1-5`
  - `approachSummary`
  - `complexityNotes`
  - `blindSpots`
  - `tags`
  - `reason`

Fallback path:

- If OpenRouter is unavailable, the service uses a local fallback scorer.
- The fallback is intentionally simple:
  - reply length `>= 120` chars => score `4`
  - reply length `>= 40` chars => score `3`
  - otherwise => score `2`

The fallback exists for resiliency, not for nuanced evaluation.

## Weight Updates

Weight updates happen in `evaluation/response.ts`.

After a reply is scored, the service computes the next weight through the shared weight abstraction in `shared/weight.ts`:

```ts
delta = (3 - score) * 0.25
nextWeight = clamp(previousWeight + delta, INTELLIGENCE_MIN_WEIGHT, INTELLIGENCE_MAX_WEIGHT)
```

Implications:

- score below `3` increases the weight
- score above `3` decreases the weight
- score `3` leaves the weight unchanged

In practice, lower-scoring questions become more likely to be selected again later.

The response transaction writes:

- `intelligenceResponse`
- updates `intelligencePromptEvent`
- upserts `intelligenceWeight`
- inserts `intelligenceWeightAudit`

## Focus Recommendations

Recommendation ranking happens in `recommendation.ts`.
Recommendation ranking happens in `recommendation/index.ts`.

Each question gets a `priority` based on a combination of signals:

- current learning `weight`
- recent submission failure rate
- staleness since last prompt or response
- difficulty boost
- low historical average reply score

The recommendation core does not define its own weight semantics. It reuses the shared weight model to normalize `weight` before combining it with the other signals.

The service then sorts by `priority`, returns the top K, and optionally asks OpenRouter for a short narrative summary.

If OpenRouter is unavailable, the narrative falls back to a simple slug list.

## Health and Database Access

The service layer uses `IntelligenceService.withDatabase()` to connect only around active operations.

Current behavior:

- prompt generation hits the database
- reply scoring hits the database
- recommendations hit the database
- `health()` does not query the database

This is intentional so health checks do not keep Neon awake unnecessarily.

## Important Config

Defined in `env.ts`:

- `MODEL`
- `OPEN_ROUTER_API_KEY`
- `INTELLIGENCE_PROMPT_CRON`
- `INTELLIGENCE_RECOMMEND_CRON`
- `INTELLIGENCE_RECOMMEND_TOP_K`
- `INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS`
- `INTELLIGENCE_MAX_CANDIDATES`
- `INTELLIGENCE_SELECTION_WINDOW`
- `INTELLIGENCE_MIN_WEIGHT`
- `INTELLIGENCE_MAX_WEIGHT`

## Notes for Future Changes

- Keep prompt selection, reply scoring, and recommendation logic separate. They evolve at different speeds.
- If you change the weight update formula, also re-check recommendation behavior because `weight` is used in both evaluation and ranking.
- If you improve fallback scoring, preserve the same output shape as the LLM scorer.
