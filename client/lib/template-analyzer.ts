import { prisma } from './prisma';
import type { TemplateMetadata } from './data';
import { randomUUID } from 'node:crypto';

export type TemplateBenchmarkScore = {
  key: string;
  patternTagId: string;
  score: number;
  confidence: number;
  reason: string;
  evidence: string[];
};

export type TemplateBenchmarkResult = {
  submissionId: string;
  model: string;
  excludedGroupKeys: string[];
  scores: TemplateBenchmarkScore[];
};

const OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions';
const DEFAULT_TEMPLATE_ANALYZER_MODEL = 'qwen/qwen3-coder-next';

type TemplateCandidate = {
  id: string;
  key: string;
  label: string;
  description: string | null;
  metadata: TemplateMetadata | null;
};

function normalizeExcludedGroupKeys(groupKeys: string[]) {
  return [...new Set(groupKeys.map((key) => key.trim()).filter(Boolean))].sort();
}

function readStringArray(value: unknown): string[] {
  return Array.isArray(value) ? value.filter((entry): entry is string => typeof entry === 'string') : [];
}

function readTemplateMetadata(metadata: unknown): TemplateMetadata | null {
  if (!metadata || typeof metadata !== 'object' || Array.isArray(metadata)) {
    return null;
  }

  const record = metadata as Record<string, unknown>;
  const complexity =
    record.defaultComplexity && typeof record.defaultComplexity === 'object' && !Array.isArray(record.defaultComplexity)
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
      time: typeof complexity.time === 'string' ? complexity.time : undefined,
      space: typeof complexity.space === 'string' ? complexity.space : undefined,
    },
    relatedDataStructures: readStringArray(record.relatedDataStructures),
    similarTemplates: readStringArray(record.similarTemplates),
  };
}

function truncate(value: string, maxLength: number) {
  if (value.length <= maxLength) {
    return value;
  }

  return `${value.slice(0, maxLength - 3)}...`;
}

function clampScore(value: unknown) {
  if (typeof value !== 'number' || !Number.isFinite(value)) {
    return 0;
  }

  return Math.max(0, Math.min(100, Math.round(value)));
}

function parseBenchmarkPayload(payload: string, candidates: TemplateCandidate[]): TemplateBenchmarkScore[] {
  const candidateByKey = new Map(candidates.map((candidate) => [candidate.key, candidate]));

  try {
    const parsed = JSON.parse(payload) as Record<string, unknown>;
    const scores = Array.isArray(parsed.scores) ? parsed.scores : [];

    return scores
      .map((entry) => {
        if (!entry || typeof entry !== 'object' || Array.isArray(entry)) {
          return null;
        }

        const record = entry as Record<string, unknown>;
        const key = typeof record.key === 'string' ? record.key : '';
        const candidate = candidateByKey.get(key);

        if (!candidate) {
          return null;
        }

        return {
          key,
          patternTagId: candidate.id,
          score: clampScore(record.score),
          confidence: clampScore(record.confidence),
          reason: typeof record.reason === 'string' ? record.reason.trim() : '',
          evidence: readStringArray(record.evidence).map((item) => item.trim()).filter(Boolean),
        };
      })
      .filter((entry): entry is TemplateBenchmarkScore => Boolean(entry))
      .sort((a, b) => b.score - a.score);
  } catch {
    return [];
  }
}

async function persistTemplateBenchmarkResult(result: TemplateBenchmarkResult) {
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

function createPrompt(candidates: TemplateCandidate[]) {
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
- The output is invalid if it contains "..." or the ellipsis character "…".
- Do not abbreviate, summarize with ellipses, or omit text inside quoted code clues.
- Write the full reason as complete sentences.
- Write evidence as complete, specific code or behavior observations.
- If a code example would be too long, choose one short self-contained fragment. Never truncate a fragment with ellipses.
- If you cannot fit a long explanation, write a shorter complete explanation instead of an incomplete one.
- Every reason must end as a complete sentence, not a cut-off fragment.
- Every evidence item must be a complete observation or a complete short code fragment.
- Bad: "the code slides by exa..."
- Bad: "for i in range(...)"
- Good: "the code slides the window by advancing i from n1 to n2."
- Good: "for i in range(n1, n2)"
- If any field would contain "..." or "…", rewrite that field before returning.
- Return strict JSON only. No markdown.

JSON format:
{
  "scores": [
    {
      "key": "template-key",
      "score": 0,
      "confidence": 0,
      "reason": "complete explanation of why the code matches or does not match the template",
      "evidence": ["complete code or behavior clue without ellipses"]
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

export async function analyzeSubmissionTemplates(
  submissionId: string,
  excludedGroupKeys: string[] = [],
): Promise<TemplateBenchmarkResult> {
  const apiKey = process.env.OPEN_ROUTER_API_KEY;
  const model = process.env.TEMPLATE_ANALYZER_MODEL ?? DEFAULT_TEMPLATE_ANALYZER_MODEL;
  const excludedGroups = normalizeExcludedGroupKeys(excludedGroupKeys);

  if (!apiKey) {
    throw new Error('OPEN_ROUTER_API_KEY is required for template benchmark analysis.');
  }

  const [submission, tags] = await Promise.all([
    prisma.submission.findFirst({
      where: { id: submissionId, status: 'Accepted' },
      select: {
        id: true,
        titleSlug: true,
        content: true,
        timeComplexity: true,
        spaceComplexity: true,
        submissionDetails: true,
      },
    }),
    prisma.patternTag.findMany({
      where: { dimension: 'template', kind: 'tag', isActive: true },
      include: { parent: true },
      orderBy: [{ sortOrder: 'asc' }, { label: 'asc' }],
    }),
  ]);

  if (!submission) {
    throw new Error('Accepted submission was not found.');
  }

  const candidates = tags
    .filter((tag) => !excludedGroups.includes(tag.parent?.key ?? tag.dimension))
    .map<TemplateCandidate>((tag) => ({
      id: tag.id,
      key: tag.key,
      label: tag.label,
      description: tag.description,
      metadata: readTemplateMetadata(tag.metadata),
    }));

  if (candidates.length === 0) {
    throw new Error('At least one template group must be included for benchmark analysis.');
  }

  const response = await fetch(OPENROUTER_URL, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
      'HTTP-Referer': 'http://localhost:3005',
      'X-Title': 'leetcode-qa template analyzer',
    },
    body: JSON.stringify({
      model,
      temperature: 0,
      response_format: { type: 'json_object' },
      messages: [
        { role: 'system', content: createPrompt(candidates) },
        {
          role: 'user',
          content: JSON.stringify({
            submission: {
              titleSlug: submission.titleSlug,
              timeComplexity: submission.timeComplexity,
              spaceComplexity: submission.spaceComplexity,
              details: submission.submissionDetails,
              code: truncate(submission.content, 14000),
            },
          }),
        },
      ],
    }),
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(`Template analyzer failed: ${response.status} ${truncate(text, 300)}`);
  }

  const payload = (await response.json()) as {
    choices?: Array<{ message?: { content?: string } }>;
  };
  const content = payload.choices?.[0]?.message?.content ?? '{}';

  const result = {
    submissionId,
    model,
    excludedGroupKeys: excludedGroups,
    scores: parseBenchmarkPayload(content, candidates),
  };

  await persistTemplateBenchmarkResult(result);

  return result;
}
