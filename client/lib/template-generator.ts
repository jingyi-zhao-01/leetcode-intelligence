import { prisma } from './prisma';
import type { TemplateMetadata } from './data';

export type GeneratedTemplateDraft = {
  key: string;
  label: string;
  description: string;
  metadata: Required<TemplateMetadata>;
};

export type TemplateGenerationInput = {
  groupKey: string;
  submissionId: string;
  prompt: string;
  model?: string;
};

const OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions';
const DEFAULT_TEMPLATE_GENERATOR_MODEL = 'qwen/qwen3-coder-next';

function truncate(value: string, maxLength: number) {
  if (value.length <= maxLength) {
    return value;
  }

  return `${value.slice(0, maxLength - 3)}...`;
}

function slugify(value: string) {
  return value
    .trim()
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, '-')
    .replace(/^-+|-+$/g, '')
    .slice(0, 80);
}

function readString(value: unknown, fallback = '') {
  return typeof value === 'string' && value.trim() ? value.trim() : fallback;
}

function readStringArray(value: unknown, fallback: string[]) {
  if (!Array.isArray(value)) {
    return fallback;
  }

  const entries = value.filter((entry): entry is string => typeof entry === 'string' && entry.trim().length > 0);
  return entries.length ? entries.slice(0, 8) : fallback;
}

function readMetadata(value: unknown): Required<TemplateMetadata> {
  const record = value && typeof value === 'object' && !Array.isArray(value) ? (value as Record<string, unknown>) : {};
  const complexity =
    record.defaultComplexity && typeof record.defaultComplexity === 'object' && !Array.isArray(record.defaultComplexity)
      ? (record.defaultComplexity as Record<string, unknown>)
      : {};

  return {
    classicProblems: readStringArray(record.classicProblems, []),
    whenToUse: readStringArray(record.whenToUse, ['Use when this canonical algorithm skeleton fits the problem.']),
    whenNotToUse: readStringArray(record.whenNotToUse, ['Do not use when a simpler canonical template matches better.']),
    signals: readStringArray(record.signals, []),
    pseudocode: readStringArray(record.pseudocode, ['state = initialize()', 'for item in input:', '  update state and answer']),
    invariants: readStringArray(record.invariants, ['State has one stable meaning throughout the algorithm.']),
    defaultComplexity: {
      time: readString(complexity.time, 'O(n)'),
      space: readString(complexity.space, 'O(1) or O(n)'),
    },
    relatedDataStructures: readStringArray(record.relatedDataStructures, []),
    similarTemplates: readStringArray(record.similarTemplates, []),
  };
}

function parseDraftPayload(payload: string, prompt: string): GeneratedTemplateDraft {
  const parsed = JSON.parse(payload) as Record<string, unknown>;
  const label = readString(parsed.label, prompt || 'Generated Template');
  const key = slugify(readString(parsed.key, label));

  if (!key) {
    throw new Error('Template generator returned an invalid key.');
  }

  return {
    key,
    label,
    description: readString(parsed.description, `Canonical template for ${label}.`),
    metadata: readMetadata(parsed.metadata),
  };
}

function createPrompt({
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

JSON format:
{
  "key": "canonical-template-key",
  "label": "Human label",
  "description": "One sentence canonical description",
  "metadata": {
    "classicProblems": ["problem examples"],
    "whenToUse": ["specific reusable conditions"],
    "whenNotToUse": ["nearby templates or anti-signals"],
    "signals": ["short recognition signals"],
    "pseudocode": ["line 1", "line 2"],
    "invariants": ["stable invariant"],
    "defaultComplexity": { "time": "O(...)", "space": "O(...)" },
    "relatedDataStructures": ["data structure"],
    "similarTemplates": ["existing-template-key"]
  }
}
`.trim();
}

export async function generateTemplateDraft({
  groupKey,
  submissionId,
  prompt,
  model,
}: TemplateGenerationInput): Promise<{ model: string; draft: GeneratedTemplateDraft }> {
  const apiKey = process.env.OPEN_ROUTER_API_KEY;
  const selectedModel = model?.trim() || process.env.TEMPLATE_GENERATOR_MODEL || DEFAULT_TEMPLATE_GENERATOR_MODEL;

  if (!apiKey) {
    throw new Error('OPEN_ROUTER_API_KEY is required for template generation.');
  }

  const [group, submission] = await Promise.all([
    prisma.patternTag.findFirst({
      where: { key: groupKey, dimension: 'template', kind: 'template_group', isActive: true },
      include: {
        children: {
          where: { isActive: true, dimension: 'template', kind: 'tag' },
          orderBy: [{ sortOrder: 'asc' }, { label: 'asc' }],
        },
      },
    }),
    prisma.submission.findFirst({
      where: { id: submissionId, status: 'Accepted' },
      select: {
        titleSlug: true,
        content: true,
        timeComplexity: true,
        spaceComplexity: true,
        submissionDetails: true,
      },
    }),
  ]);

  if (!group) {
    throw new Error('Template group was not found.');
  }

  if (!submission) {
    throw new Error('Accepted submission was not found.');
  }

  const question = submission.titleSlug
    ? await prisma.question.findUnique({
        where: { titleSlug: submission.titleSlug },
        select: { title: true, difficulty: true, content: true },
      })
    : null;

  const response = await fetch(OPENROUTER_URL, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${apiKey}`,
      'Content-Type': 'application/json',
      'HTTP-Referer': 'http://localhost:3005',
      'X-Title': 'leetcode-qa template generator',
    },
    body: JSON.stringify({
      model: selectedModel,
      temperature: 0.2,
      response_format: { type: 'json_object' },
      messages: [
        {
          role: 'system',
          content: createPrompt({
            groupLabel: group.label,
            groupDescription: group.description,
            existingTemplates: group.children.map((tag) => ({
              key: tag.key,
              label: tag.label,
              description: tag.description,
            })),
          }),
        },
        {
          role: 'user',
          content: JSON.stringify({
            userIntent: prompt,
            currentSubmission: {
              titleSlug: submission.titleSlug,
              questionTitle: question?.title,
              difficulty: question?.difficulty,
              questionContent: truncate(question?.content ?? '', 6000),
              timeComplexity: submission.timeComplexity,
              spaceComplexity: submission.spaceComplexity,
              details: submission.submissionDetails,
              code: truncate(submission.content, 12000),
            },
          }),
        },
      ],
    }),
  });

  if (!response.ok) {
    const text = await response.text();
    throw new Error(`Template generator failed: ${response.status} ${truncate(text, 300)}`);
  }

  const payload = (await response.json()) as {
    choices?: Array<{ message?: { content?: string } }>;
  };
  const content = payload.choices?.[0]?.message?.content ?? '{}';

  return {
    model: selectedModel,
    draft: parseDraftPayload(content, prompt),
  };
}

export async function createGeneratedTemplate(groupKey: string, draft: GeneratedTemplateDraft) {
  const group = await prisma.patternTag.findFirst({
    where: { key: groupKey, dimension: 'template', kind: 'template_group', isActive: true },
    select: { id: true },
  });

  if (!group) {
    throw new Error('Template group was not found.');
  }

  const baseKey = slugify(draft.key || draft.label);
  if (!baseKey) {
    throw new Error('Template key is required.');
  }

  let key = baseKey;
  for (let suffix = 2; await prisma.patternTag.findUnique({ where: { key } }); suffix += 1) {
    key = `${baseKey}-${suffix}`;
  }

  const maxSortOrder = await prisma.patternTag.aggregate({
    where: { parentId: group.id, dimension: 'template', kind: 'tag' },
    _max: { sortOrder: true },
  });

  return prisma.patternTag.create({
    data: {
      key,
      label: draft.label.trim(),
      dimension: 'template',
      kind: 'tag',
      source: 'llm_generated',
      description: draft.description.trim(),
      metadata: draft.metadata,
      parentId: group.id,
      isActive: true,
      sortOrder: (maxSortOrder._max.sortOrder ?? 0) + 1,
    },
    select: { id: true, key: true },
  });
}
