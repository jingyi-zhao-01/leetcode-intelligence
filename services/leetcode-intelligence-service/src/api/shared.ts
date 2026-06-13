import { randomUUID } from "node:crypto";

import type { PrismaClient } from "@prisma/client";
import type {
  GeneratedTemplateDraft,
  PatternTagKind,
  PatternTagOption,
  PatternTagSource,
  TemplateBenchmarkResult,
  TemplateBenchmarkScore,
  TemplateMetadata,
} from "./types.ts";

export type PatternTagParentRecord = {
  id: string;
  key: string;
  label: string;
};

export type PatternTagRecord = {
  id: string;
  key: string;
  label: string;
  dimension: string;
  kind: PatternTagKind;
  source: PatternTagSource;
  description: string | null;
  metadata: unknown;
  parentId: string | null;
  parent: PatternTagParentRecord | null;
  sortOrder: number;
};

export type SubmissionPatternTagRecord = {
  PatternTag: PatternTagRecord;
};

export type ActivePatternTag = PatternTagRecord & {
  _count: {
    SubmissionPatternTag: number;
  };
};

export type TemplateBenchmarkRecord = {
  submissionId: string;
  patternTagId: string;
  templateKey: string;
  model: string;
  score: number;
  confidence: number;
  reason: string | null;
  evidence: string[];
  excludedGroupKeys: string[];
  updatedAt: Date;
};

export type TemplateCandidate = {
  id: string;
  key: string;
  label: string;
  description: string | null;
  metadata: TemplateMetadata | null;
};

export const OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions";
export const DEFAULT_TEMPLATE_ANALYZER_MODEL = "qwen/qwen3-coder-next";
export const DEFAULT_TEMPLATE_GENERATOR_MODEL = "qwen/qwen3-coder-next";

export function readStringArray(value: unknown): string[] {
  return Array.isArray(value) ? value.filter((entry): entry is string => typeof entry === "string") : [];
}

export function readTemplateMetadata(metadata: unknown): TemplateMetadata | null {
  if (!metadata || typeof metadata !== "object" || Array.isArray(metadata)) {
    return null;
  }

  const record = metadata as Record<string, unknown>;
  const complexity =
    record.defaultComplexity && typeof record.defaultComplexity === "object" && !Array.isArray(record.defaultComplexity)
      ? (record.defaultComplexity as Record<string, unknown>)
      : {};

  return {
    classicProblems: readStringArray(record.classicProblems),
    whenToUse: readStringArray(record.whenToUse),
    whenNotToUse: readStringArray(record.whenNotToUse),
    signals: readStringArray(record.signals),
    pseudocode: readStringArray(record.pseudocode),
    invariants: readStringArray(record.invariants),
    defaultComplexity: {
      time: typeof complexity.time === "string" ? complexity.time : undefined,
      space: typeof complexity.space === "string" ? complexity.space : undefined,
    },
    relatedDataStructures: readStringArray(record.relatedDataStructures),
    similarTemplates: readStringArray(record.similarTemplates),
  };
}

export function readLanguage(details: unknown): string | null {
  if (!details || typeof details !== "object" || Array.isArray(details)) {
    return null;
  }

  const record = details as Record<string, unknown>;
  const language = record.lang ?? record.language ?? record.programming_language;
  return typeof language === "string" && language.trim() ? language : null;
}

export function readQuestionDescription(content: string | null): string | null {
  if (!content) {
    return null;
  }

  const text = content
    .replace(/<br\s*\/?>/gi, "\n")
    .replace(/<\/(p|div|li|pre|ul|ol|h[1-6])>/gi, "\n")
    .replace(/<li[^>]*>/gi, "- ")
    .replace(/<[^>]*>/g, " ")
    .replace(/&nbsp;/g, " ")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">")
    .replace(/&quot;/g, "\"")
    .replace(/&#39;/g, "'")
    .replace(/[ \t]+\n/g, "\n")
    .replace(/\n[ \t]+/g, "\n")
    .replace(/[ \t]{2,}/g, " ")
    .replace(/\n{3,}/g, "\n\n")
    .trim();

  return text || null;
}

export function truncate(value: string, maxLength: number) {
  if (value.length <= maxLength) {
    return value;
  }

  return `${value.slice(0, maxLength - 3)}...`;
}

export function clampScore(value: unknown) {
  if (typeof value !== "number" || !Number.isFinite(value)) {
    return 0;
  }

  return Math.max(0, Math.min(100, Math.round(value)));
}

export function normalizeExcludedGroupKeys(groupKeys: string[]) {
  return [...new Set(groupKeys.map((key) => key.trim()).filter(Boolean))].sort();
}

export function slugify(value: string) {
  return value
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80);
}

export function readMetadata(value: unknown): Required<TemplateMetadata> {
  const record = value && typeof value === "object" && !Array.isArray(value) ? (value as Record<string, unknown>) : {};
  const complexity =
    record.defaultComplexity && typeof record.defaultComplexity === "object" && !Array.isArray(record.defaultComplexity)
      ? (record.defaultComplexity as Record<string, unknown>)
      : {};

  return {
    classicProblems: readStringArray(record.classicProblems),
    whenToUse: readStringArray(record.whenToUse).length
      ? readStringArray(record.whenToUse)
      : ["Use when this canonical algorithm skeleton fits the problem."],
    whenNotToUse: readStringArray(record.whenNotToUse).length
      ? readStringArray(record.whenNotToUse)
      : ["Do not use when a simpler canonical template matches better."],
    signals: readStringArray(record.signals),
    pseudocode: readStringArray(record.pseudocode).length
      ? readStringArray(record.pseudocode)
      : ["state = initialize()", "for item in input:", "  update state and answer"],
    invariants: readStringArray(record.invariants).length
      ? readStringArray(record.invariants)
      : ["State has one stable meaning throughout the algorithm."],
    defaultComplexity: {
      time: typeof complexity.time === "string" && complexity.time.trim() ? complexity.time : "O(n)",
      space: typeof complexity.space === "string" && complexity.space.trim() ? complexity.space : "O(1) or O(n)",
    },
    relatedDataStructures: readStringArray(record.relatedDataStructures),
    similarTemplates: readStringArray(record.similarTemplates),
  };
}

export function parseBenchmarkPayload(payload: string, candidates: TemplateCandidate[]): TemplateBenchmarkScore[] {
  const candidateByKey = new Map(candidates.map((candidate) => [candidate.key, candidate]));

  try {
    const parsed = JSON.parse(payload) as Record<string, unknown>;
    const scores = Array.isArray(parsed.scores) ? parsed.scores : [];

    return scores
      .map((entry) => {
        if (!entry || typeof entry !== "object" || Array.isArray(entry)) {
          return null;
        }

        const record = entry as Record<string, unknown>;
        const key = typeof record.key === "string" ? record.key : "";
        const candidate = candidateByKey.get(key);
        if (!candidate) {
          return null;
        }

        return {
          key,
          patternTagId: candidate.id,
          score: clampScore(record.score),
          confidence: clampScore(record.confidence),
          reason: typeof record.reason === "string" ? record.reason.trim() : "",
          evidence: readStringArray(record.evidence).map((item) => item.trim()).filter(Boolean),
        };
      })
      .filter((entry): entry is TemplateBenchmarkScore => Boolean(entry))
      .sort((a, b) => b.score - a.score);
  } catch {
    return [];
  }
}

export async function persistTemplateBenchmarkResult(prisma: PrismaClient, result: TemplateBenchmarkResult) {
  await prisma.$transaction(
    result.scores.map((score) =>
      prisma.$executeRaw`
        INSERT INTO "TemplateBenchmarkScore" (
          "id",
          "submissionId",
          "patternTagId",
          "templateKey",
          "model",
          "score",
          "confidence",
          "reason",
          "evidence",
          "excludedGroupKeys",
          "createdAt",
          "updatedAt"
        )
        VALUES (
          ${randomUUID()},
          ${result.submissionId},
          ${score.patternTagId},
          ${score.key},
          ${result.model},
          ${score.score},
          ${score.confidence},
          ${score.reason || null},
          ${score.evidence},
          ${result.excludedGroupKeys},
          now(),
          now()
        )
        ON CONFLICT ("submissionId", "patternTagId")
        DO UPDATE SET
          "templateKey" = EXCLUDED."templateKey",
          "model" = EXCLUDED."model",
          "score" = EXCLUDED."score",
          "confidence" = EXCLUDED."confidence",
          "reason" = EXCLUDED."reason",
          "evidence" = EXCLUDED."evidence",
          "excludedGroupKeys" = EXCLUDED."excludedGroupKeys",
          "updatedAt" = now()
      `,
    ),
  );
}

export function createBenchmarkPrompt(candidates: TemplateCandidate[]) {
  return `
You are a LeetCode template benchmark analyzer.

Task:
- Score how well the submitted code matches each provisioned template.
- Use code structure, algorithm behavior, time complexity, space complexity, and template metadata.
- Score every candidate template from 0 to 100.
- 90-100 means the code is a direct instance of the template.
- 70-89 means strongly related but not exact.
- 40-69 means partial overlap.
- 0-39 means weak or unrelated.
- Do not change tags. Only benchmark fit.
- Return strict JSON only. No markdown.

JSON format:
{
  "scores": [
    {
      "key": "template-key",
      "score": 0,
      "confidence": 0,
      "reason": "complete explanation",
      "evidence": ["complete clue"]
    }
  ]
}

Candidate templates:
${JSON.stringify(
    candidates.map((candidate) => ({
      key: candidate.key,
      label: candidate.label,
      description: candidate.description,
      classicProblems: candidate.metadata?.classicProblems ?? [],
      whenToUse: candidate.metadata?.whenToUse ?? [],
      whenNotToUse: candidate.metadata?.whenNotToUse ?? [],
      defaultComplexity: candidate.metadata?.defaultComplexity ?? null,
      signals: candidate.metadata?.signals ?? [],
      pseudocode: candidate.metadata?.pseudocode ?? [],
    })),
  )}
`.trim();
}

export function readString(value: unknown, fallback = "") {
  return typeof value === "string" && value.trim() ? value.trim() : fallback;
}

export function parseDraftPayload(payload: string, prompt: string): GeneratedTemplateDraft {
  const parsed = JSON.parse(payload) as Record<string, unknown>;
  const label = readString(parsed.label, prompt || "Generated Template");
  const key = slugify(readString(parsed.key, label));

  if (!key) {
    throw new Error("Template generator returned an invalid key.");
  }

  return {
    key,
    label,
    description: readString(parsed.description, `Canonical template for ${label}.`),
    metadata: readMetadata(parsed.metadata),
  };
}

export function createGeneratorPrompt({
  groupLabel,
  groupDescription,
  existingTemplates,
}: {
  groupLabel: string;
  groupDescription: string | null;
  existingTemplates: Array<{ key: string; label: string; description: string | null }>;
}) {
  return `
You are designing a controlled LeetCode canonical template taxonomy.

Task:
- Generate exactly one new canonical template draft for the requested primary group.
- The template must be a reusable algorithm skeleton, not a problem-specific trick.
- Do not generate duplicates of existing templates.
- Classic problems are only examples in metadata, not the template identity.
- Keep key lowercase kebab-case.
- Return strict JSON only. No markdown.

Primary group:
${JSON.stringify({ groupLabel, groupDescription })}

Existing templates in this group:
${JSON.stringify(existingTemplates)}
`.trim();
}

export function mapPatternTagOption(tag: ActivePatternTag): PatternTagOption {
  return {
    id: tag.id,
    key: tag.key,
    label: tag.label,
    dimension: tag.dimension,
    kind: tag.kind,
    source: tag.source,
    assignmentCount: tag._count.SubmissionPatternTag,
    description: tag.description,
    metadata: readTemplateMetadata(tag.metadata),
    parentId: tag.parentId,
    parentKey: tag.parent?.key ?? null,
    parentLabel: tag.parent?.label ?? null,
    sortOrder: tag.sortOrder,
  };
}
