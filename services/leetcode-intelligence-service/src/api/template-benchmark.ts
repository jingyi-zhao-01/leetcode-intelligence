import type { ApiContext } from './context.ts';
import {
  createBenchmarkPrompt,
  DEFAULT_TEMPLATE_ANALYZER_MODEL,
  normalizeExcludedGroupKeys,
  OPENROUTER_URL,
  parseBenchmarkPayload,
  persistTemplateBenchmarkResult,
  readTemplateMetadata,
  truncate,
  type TemplateCandidate,
} from './shared.ts';
import type { TemplateBenchmarkResult } from './types.ts';

export function createTemplateBenchmarkApi({ prisma }: ApiContext) {
  const benchmarkSubmissionTemplates = async (
    submissionId: string,
    excludedGroupKeys: string[] = [],
  ): Promise<TemplateBenchmarkResult> => {
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
          templateBenchmarkOptOut: true,
        },
      }),
      prisma.patternTag.findMany({
        where: { dimension: 'template', kind: 'tag', isActive: true },
        include: { parent: true },
        orderBy: [{ sortOrder: 'asc' }, { label: 'asc' }],
      }),
    ]);

    if (!submission) {
      throw new Error('Submission not found or not accepted.');
    }

    if (submission.templateBenchmarkOptOut) {
      throw new Error('Submission is opted out from templating.');
    }

    const candidates: TemplateCandidate[] = tags
      .filter((tag) => !excludedGroups.includes(tag.parent?.key ?? tag.dimension))
      .map((tag) => ({
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
        'HTTP-Referer': 'https://leetcode-intelligence',
        'X-Title': 'leetcode-intelligence-service',
      },
      body: JSON.stringify({
        model,
        temperature: 0,
        response_format: { type: 'json_object' },
        messages: [
          { role: 'system', content: createBenchmarkPrompt(candidates) },
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

    await persistTemplateBenchmarkResult(prisma, result);
    return result;
  };

  const setSubmissionTemplateOptOut = async (submissionId: string, templateBenchmarkOptOut: boolean) => {
    const submission = await prisma.submission.findFirst({
      where: { id: submissionId, status: 'Accepted' },
      select: { id: true },
    });

    if (!submission) {
      return { status: 'not_found' as const };
    }

    await prisma.submission.update({
      where: { id: submissionId },
      data: { templateBenchmarkOptOut },
    });

    return { status: 'updated' as const, templateBenchmarkOptOut };
  };

  return {
    benchmarkSubmissionTemplates,
    setSubmissionTemplateOptOut,
  };
}
