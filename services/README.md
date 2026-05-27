# Shared Prisma Schema

This directory shares one PostgreSQL schema managed through Prisma.

## Source Of Truth

- Prisma schema: `shared/prisma/schema.prisma`
- ERD: `shared/schema-relations.svg`
- D2 source: `shared/schema-relations.d2`

![Shared schema relationships](./shared/schema-relations.svg)

## Database Design

- `Question`: problem catalog and metadata
- `Submission`: solve attempts and outcomes
- `FollowUp -> Submission`: follow-up items per submission (`N:1`)
- `IntelligencePromptEvent -> Question, Submission`: prompt/recommendation events (`N:1`, `N:1`)
- `IntelligenceResponse -> IntelligencePromptEvent`: one stored model response per prompt event (`1:1`)
- `IntelligenceWeight -> Question`: current per-question weight (`1:1`)
- `IntelligenceWeightAudit -> Question, IntelligencePromptEvent?`: weight history with optional originating event (`N:1`, optional `N:1`)

## Design Considerations

- Single shared schema across services
- Prisma is the schema authority
- `Question.titleSlug` is the stable business key used by intelligence tables
- `Submission.id` is the operational key for attempt-linked records
- Current state and audit history are separated: `IntelligenceWeight` vs `IntelligenceWeightAudit`
- Prompt lifecycle is separated from model output: `IntelligencePromptEvent` vs `IntelligenceResponse`
- Optional foreign key on `IntelligenceWeightAudit.promptEventId` allows manual or offline recalculations
