-- Merge overlapping data-structure tags so the taxonomy has one canonical
-- tag for 2D indexed surfaces and one canonical tag for queue-like frontiers.
--
-- Canonical tags:
--   ds-grid  absorbs ds-matrix
--   ds-queue absorbs ds-deque

WITH tags AS (
  SELECT
    matrix.id AS matrix_id,
    grid.id AS grid_id,
    deque.id AS deque_id,
    queue.id AS queue_id
  FROM "PatternTag" matrix
  CROSS JOIN "PatternTag" grid
  CROSS JOIN "PatternTag" deque
  CROSS JOIN "PatternTag" queue
  WHERE matrix.key = 'ds-matrix'
    AND grid.key = 'ds-grid'
    AND deque.key = 'ds-deque'
    AND queue.key = 'ds-queue'
)
DELETE FROM "SubmissionPatternTag" duplicate
USING tags
WHERE duplicate."patternTagId" IN (tags.matrix_id, tags.deque_id)
  AND EXISTS (
    SELECT 1
    FROM "SubmissionPatternTag" canonical
    WHERE canonical."submissionId" = duplicate."submissionId"
      AND canonical."patternTagId" = CASE
        WHEN duplicate."patternTagId" = tags.matrix_id THEN tags.grid_id
        WHEN duplicate."patternTagId" = tags.deque_id THEN tags.queue_id
      END
  );

WITH tags AS (
  SELECT matrix.id AS matrix_id, grid.id AS grid_id
  FROM "PatternTag" matrix
  CROSS JOIN "PatternTag" grid
  WHERE matrix.key = 'ds-matrix'
    AND grid.key = 'ds-grid'
)
UPDATE "SubmissionPatternTag" assignment
SET "patternTagId" = tags.grid_id
FROM tags
WHERE assignment."patternTagId" = tags.matrix_id;

WITH tags AS (
  SELECT deque.id AS deque_id, queue.id AS queue_id
  FROM "PatternTag" deque
  CROSS JOIN "PatternTag" queue
  WHERE deque.key = 'ds-deque'
    AND queue.key = 'ds-queue'
)
UPDATE "SubmissionPatternTag" assignment
SET "patternTagId" = tags.queue_id
FROM tags
WHERE assignment."patternTagId" = tags.deque_id;

WITH tags AS (
  SELECT
    matrix.id AS matrix_id,
    grid.id AS grid_id,
    deque.id AS deque_id,
    queue.id AS queue_id
  FROM "PatternTag" matrix
  CROSS JOIN "PatternTag" grid
  CROSS JOIN "PatternTag" deque
  CROSS JOIN "PatternTag" queue
  WHERE matrix.key = 'ds-matrix'
    AND grid.key = 'ds-grid'
    AND deque.key = 'ds-deque'
    AND queue.key = 'ds-queue'
)
DELETE FROM "TemplateBenchmarkScore" duplicate
USING tags
WHERE duplicate."patternTagId" IN (tags.matrix_id, tags.deque_id)
  AND EXISTS (
    SELECT 1
    FROM "TemplateBenchmarkScore" canonical
    WHERE canonical."submissionId" = duplicate."submissionId"
      AND canonical."patternTagId" = CASE
        WHEN duplicate."patternTagId" = tags.matrix_id THEN tags.grid_id
        WHEN duplicate."patternTagId" = tags.deque_id THEN tags.queue_id
      END
  );

WITH tags AS (
  SELECT matrix.id AS matrix_id, grid.id AS grid_id
  FROM "PatternTag" matrix
  CROSS JOIN "PatternTag" grid
  WHERE matrix.key = 'ds-matrix'
    AND grid.key = 'ds-grid'
)
UPDATE "TemplateBenchmarkScore" score
SET "patternTagId" = tags.grid_id,
    "templateKey" = 'ds-grid',
    "updatedAt" = CURRENT_TIMESTAMP
FROM tags
WHERE score."patternTagId" = tags.matrix_id;

WITH tags AS (
  SELECT deque.id AS deque_id, queue.id AS queue_id
  FROM "PatternTag" deque
  CROSS JOIN "PatternTag" queue
  WHERE deque.key = 'ds-deque'
    AND queue.key = 'ds-queue'
)
UPDATE "TemplateBenchmarkScore" score
SET "patternTagId" = tags.queue_id,
    "templateKey" = 'ds-queue',
    "updatedAt" = CURRENT_TIMESTAMP
FROM tags
WHERE score."patternTagId" = tags.deque_id;

UPDATE "PatternTag"
SET label = 'Grid / Matrix',
    description = 'Two-dimensional indexed surface with neighbor movement or table-style access.',
    "isActive" = true
WHERE key = 'ds-grid';

UPDATE "PatternTag"
SET label = 'Queue / Deque',
    description = 'FIFO or double-ended frontier container for traversal, window, or monotonic state.',
    "isActive" = true
WHERE key = 'ds-queue';

UPDATE "PatternTag"
SET "isActive" = false
WHERE key IN ('ds-matrix', 'ds-deque');
