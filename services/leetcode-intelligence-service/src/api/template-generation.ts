import type { ApiContext } from './context.ts';
import {
  createGeneratorPrompt,
  DEFAULT_TEMPLATE_GENERATOR_MODEL,
  OPENROUTER_URL,
  parseDraftPayload,
  slugify,
  truncate,
} from './shared.ts';
import type { GeneratedTemplateDraft } from './types.ts';

type TemplateGeneratorChildTagRecord = {
  key: string;
  label: string;
  description: string | null;
};

type TemplateGeneratorGroupRecord = {
  id: string;
  label: string;
  description: string | null;
  children: TemplateGeneratorChildTagRecord[];
};

type TemplateGeneratorSubmissionRecord = {
  titleSlug: string | null;
  content: string;
  timeComplexity: string | null;
  spaceComplexity: string | null;
  submissionDetails: unknown;
};

type TemplateGeneratorQuestionRecord = {
  title: string | null;
  difficulty: string | null;
  content: string | null;
};

export function createTemplateGenerationApi({ prisma }: ApiContext) {
  const generateTemplateDraft = async (input: {
    groupKey: string;
    submissionId: string;
    prompt: string;
    model?: string;
  }) => {
    const apiKey = process.env.OPEN_ROUTER_API_KEY;
    const selectedModel =
      input.model?.trim() || process.env.TEMPLATE_GENERATOR_MODEL || DEFAULT_TEMPLATE_GENERATOR_MODEL;

    if (!apiKey) {
      throw new Error('OPEN_ROUTER_API_KEY is required for template generation.');
    }

    const [group, submission] = (await Promise.all([
      prisma.patternTag.findFirst({
        where: { key: input.groupKey, dimension: 'template', kind: 'template_group', isActive: true },
        include: {
          children: {
            where: { isActive: true, dimension: 'template', kind: 'tag' },
            orderBy: [{ sortOrder: 'asc' }, { label: 'asc' }],
          },
        },
      }),
      prisma.submission.findFirst({
        where: { id: input.submissionId, status: 'Accepted' },
        select: {
          titleSlug: true,
          content: true,
          timeComplexity: true,
          spaceComplexity: true,
          submissionDetails: true,
        },
      }),
    ])) as [TemplateGeneratorGroupRecord | null, TemplateGeneratorSubmissionRecord | null];

    if (!group) {
      throw new Error('Template group was not found.');
    }

    if (!submission) {
      throw new Error('Accepted submission was not found.');
    }

    const question: TemplateGeneratorQuestionRecord | null = submission.titleSlug
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
        'HTTP-Referer': 'https://leetcode-intelligence',
        'X-Title': 'leetcode-intelligence-service',
      },
      body: JSON.stringify({
        model: selectedModel,
        temperature: 0.2,
        response_format: { type: 'json_object' },
        messages: [
          {
            role: 'system',
            content: createGeneratorPrompt({
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
              userIntent: input.prompt,
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
      draft: parseDraftPayload(content, input.prompt),
    };
  };

  const createGeneratedTemplate = async (groupKey: string, draft: GeneratedTemplateDraft) => {
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
  };

  return {
    generateTemplateDraft,
    createGeneratedTemplate,
  };
}
