# Shared Schema

Shared database assets live here. The source of truth remains the Prisma schema in `prisma/schema.prisma`.

## Shared D2 Style System

Reusable D2 palette and rendering defaults live under `d2/`.

- `d2/rendering.d2`: shared render config such as padding and centering
- `d2/architecture-style.d2`: shared classes for architecture diagrams

## DDL Relationships

![Shared schema relationships](./schema-relations.svg)

Source diagram: `schema-relations.d2`

## Source of Truth

- Prisma schema: `prisma/schema.prisma`
- Relationship diagram: `schema-relations.d2`
