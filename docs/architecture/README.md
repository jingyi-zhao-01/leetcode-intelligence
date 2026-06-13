# Architecture Docs

This directory is the only place for architecture material in `leetcode-qa`.

## Canonical Diagram

![System architecture](./architecture-v1.svg)

D2 source: [`architecture-v1.d2`](./architecture-v1.d2)

Current version: `v1`

## Rule

When adding or updating architecture material:

- keep it under `docs/architecture/`
- keep exactly one canonical diagram version at a time, for example `architecture-v1.d2` and `architecture-v1.svg`
- do not add granular per-service architecture diagrams under subdirectories
- update the nearest `AGENTS.md` or `README.md` link
