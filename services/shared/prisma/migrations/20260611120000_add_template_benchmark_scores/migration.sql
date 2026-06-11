CREATE TABLE "TemplateBenchmarkScore" (
  "id" TEXT NOT NULL,
  "submissionId" TEXT NOT NULL,
  "patternTagId" TEXT NOT NULL,
  "templateKey" TEXT NOT NULL,
  "model" TEXT NOT NULL,
  "score" INTEGER NOT NULL,
  "confidence" INTEGER NOT NULL,
  "reason" TEXT,
  "evidence" TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[],
  "excludedGroupKeys" TEXT[] NOT NULL DEFAULT ARRAY[]::TEXT[],
  "createdAt" TIMESTAMPTZ(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
  "updatedAt" TIMESTAMPTZ(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,

  CONSTRAINT "TemplateBenchmarkScore_pkey" PRIMARY KEY ("id")
);

ALTER TABLE "TemplateBenchmarkScore"
  ADD CONSTRAINT "TemplateBenchmarkScore_submissionId_patternTagId_key"
  UNIQUE ("submissionId", "patternTagId");

CREATE INDEX "TemplateBenchmarkScore_submissionId_idx"
  ON "TemplateBenchmarkScore" ("submissionId");

CREATE INDEX "TemplateBenchmarkScore_patternTagId_idx"
  ON "TemplateBenchmarkScore" ("patternTagId");

CREATE INDEX "TemplateBenchmarkScore_score_idx"
  ON "TemplateBenchmarkScore" ("score");

ALTER TABLE "TemplateBenchmarkScore"
  ADD CONSTRAINT "TemplateBenchmarkScore_submissionId_fkey"
  FOREIGN KEY ("submissionId") REFERENCES "Submission"("id")
  ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE "TemplateBenchmarkScore"
  ADD CONSTRAINT "TemplateBenchmarkScore_patternTagId_fkey"
  FOREIGN KEY ("patternTagId") REFERENCES "PatternTag"("id")
  ON DELETE CASCADE ON UPDATE CASCADE;
