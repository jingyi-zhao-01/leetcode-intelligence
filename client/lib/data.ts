import { prisma } from './prisma';
import type { TemplateBenchmarkResult, TemplateBenchmarkScore } from './template-analyzer';
import { Prisma } from '@prisma/client';

export type PatternTagOption = {
  id: string;
  key: string;
  label: string;
  dimension: string;
  kind: PatternTagKind;
  source: PatternTagSource;
  assignmentCount: number;
  description: string | null;
  metadata: TemplateMetadata | null;
  parentId: string | null;
  parentKey: string | null;
  parentLabel: string | null;
  sortOrder: number;
};

export type PatternTagSource = 'seeded' | 'manually_created' | 'llm_generated';
export type PatternTagKind = 'template_group' | 'tag';

export type TemplateMetadata = {
  classicProblems?: string[];
  whenToUse?: string[];
  whenNotToUse?: string[];
  signals?: string[];
  pseudocode?: string[];
  invariants?: string[];
  defaultComplexity?: {
    time?: string;
    space?: string;
  };
  relatedDataStructures?: string[];
  similarTemplates?: string[];
};

export type SubmissionRow = {
  id: string;
  titleSlug: string | null;
  title: string | null;
  difficulty: string | null;
  relatedProblems: string[];
  status: string;
  createdAt: string;
  templateBenchmarkOptOut: boolean;
  language: string | null;
  timeComplexity: string | null;
  spaceComplexity: string | null;
  questionDescription: string | null;
  submissionCode: string;
  templateBenchmark: TemplateBenchmarkResult | null;
  tags: Array<{
    id: string;
    key: string;
    label: string;
    dimension: string;
    kind: PatternTagKind;
    parentId: string | null;
    parentKey: string | null;
    parentLabel: string | null;
  }>;
};

type TemplateBenchmarkRecord = {
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

type TagWorkbenchSubmission = Prisma.SubmissionGetPayload<{
  include: {
    SubmissionPatternTag: {
      include: {
        PatternTag: {
          include: { parent: true };
        };
      };
    };
  };
}>;

type TemplateCatalogSubmission = Prisma.SubmissionGetPayload<{
  select: {
    id: true;
    titleSlug: true;
    createdAt: true;
    SubmissionPatternTag: {
      include: {
        PatternTag: {
          include: { parent: true };
        };
      };
    };
  };
}>;

type GraphSubmission = Prisma.SubmissionGetPayload<{
  select: {
    id: true;
    titleSlug: true;
    createdAt: true;
    SubmissionPatternTag: {
      include: {
        PatternTag: {
          include: { parent: true };
        };
      };
    };
  };
}>;

type ActivePatternTag = Prisma.PatternTagGetPayload<{
  include: {
    parent: true;
    _count: {
      select: {
        SubmissionPatternTag: true;
      };
    };
  };
}>;

export type TemplateCatalogSubmissionRow = {
  id: string;
  titleSlug: string | null;
  title: string | null;
  createdAt: string;
  tags: Array<{
    id: string;
    key: string;
    label: string;
    dimension: string;
    kind: PatternTagKind;
    parentId: string | null;
    parentKey: string | null;
    parentLabel: string | null;
  }>;
};

export type GraphSubmissionRow = {
  id: string;
  titleSlug: string | null;
  title: string | null;
  difficulty: string | null;
  relatedProblems: string[];
  createdAt: string;
  tags: Array<{
    id: string;
    key: string;
    label: string;
    dimension: string;
    kind: PatternTagKind;
    parentId: string | null;
    parentKey: string | null;
    parentLabel: string | null;
  }>;
};

function readLanguage(details: unknown): string | null {
  if (!details || typeof details !== 'object' || Array.isArray(details)) {
    return null;
  }

  const record = details as Record<string, unknown>;
  const language = record.lang ?? record.language ?? record.programming_language;
  return typeof language === 'string' && language.trim() ? language : null;
}

function readQuestionDescription(content: string | null): string | null {
  if (!content) {
    return null;
  }

  const text = content
    .replace(/<br\s*\/?>/gi, '\n')
    .replace(/<\/(p|div|li|pre|ul|ol|h[1-6])>/gi, '\n')
    .replace(/<li[^>]*>/gi, '- ')
    .replace(/<[^>]*>/g, ' ')
    .replace(/&nbsp;/g, ' ')
    .replace(/&amp;/g, '&')
    .replace(/&lt;/g, '<')
    .replace(/&gt;/g, '>')
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/[ \t]+\n/g, '\n')
    .replace(/\n[ \t]+/g, '\n')
    .replace(/[ \t]{2,}/g, ' ')
    .replace(/\n{3,}/g, '\n\n')
    .trim();

  return text || null;
}

function readTemplateMetadata(metadata: unknown): TemplateMetadata | null {
  if (!metadata || typeof metadata !== 'object' || Array.isArray(metadata)) {
    return null;
  }

  const record = metadata as Record<string, unknown>;
  return {
    classicProblems: readStringArray(record.classicProblems),
    whenToUse: readStringArray(record.whenToUse),
    whenNotToUse: readStringArray(record.whenNotToUse),
    signals: readStringArray(record.signals),
    pseudocode: readStringArray(record.pseudocode),
    invariants: readStringArray(record.invariants),
    defaultComplexity: readComplexity(record.defaultComplexity),
    relatedDataStructures: readStringArray(record.relatedDataStructures),
    similarTemplates: readStringArray(record.similarTemplates),
  };
}

function readStringArray(value: unknown): string[] | undefined {
  if (!Array.isArray(value)) {
    return undefined;
  }

  const entries = value.filter((entry): entry is string => typeof entry === 'string' && entry.trim().length > 0);
  return entries.length ? entries : undefined;
}

function readComplexity(value: unknown): TemplateMetadata['defaultComplexity'] | undefined {
  if (!value || typeof value !== 'object' || Array.isArray(value)) {
    return undefined;
  }

  const record = value as Record<string, unknown>;
  const time = typeof record.time === 'string' ? record.time : undefined;
  const space = typeof record.space === 'string' ? record.space : undefined;
  return time || space ? { time, space } : undefined;
}

export async function getTagWorkbenchData() {
  const [submissions, tags]: [TagWorkbenchSubmission[], ActivePatternTag[]] = await Promise.all([
    prisma.submission.findMany({
      where: { status: 'Accepted' },
      orderBy: { createdAt: 'desc' },
      take: 250,
      include: {
        SubmissionPatternTag: {
          include: {
            PatternTag: {
              include: { parent: true },
            },
          },
          orderBy: { createdAt: 'asc' },
        },
      },
    }),
    prisma.patternTag.findMany({
      where: { isActive: true },
      include: { parent: true, _count: { select: { SubmissionPatternTag: true } } },
      orderBy: [{ dimension: 'asc' }, { sortOrder: 'asc' }, { label: 'asc' }],
    }),
  ]);

  const slugs = [
    ...new Set(submissions.map((submission) => submission.titleSlug).filter((slug): slug is string => Boolean(slug))),
  ];
  const questions = await prisma.question.findMany({
    where: { titleSlug: { in: slugs } },
    select: { titleSlug: true, title: true, difficulty: true, content: true, relatedProblems: true },
  });
  const questionBySlug = new Map(questions.map((question) => [question.titleSlug, question]));
  const submissionIds = submissions.map((submission) => submission.id);
  const benchmarkRecords = submissionIds.length
    ? await prisma.$queryRaw<TemplateBenchmarkRecord[]>`
        SELECT
          "submissionId",
          "patternTagId",
          "templateKey",
          "model",
          "score",
          "confidence",
          "reason",
          "evidence",
          "excludedGroupKeys",
          "updatedAt"
        FROM "TemplateBenchmarkScore"
        WHERE "submissionId" IN (${Prisma.join(submissionIds)})
        ORDER BY "submissionId" ASC, "score" DESC, "updatedAt" DESC
      `
    : [];
  const benchmarkRecordsBySubmission = new Map<string, TemplateBenchmarkRecord[]>();
  for (const record of benchmarkRecords) {
    const records = benchmarkRecordsBySubmission.get(record.submissionId) ?? [];
    records.push(record);
    benchmarkRecordsBySubmission.set(record.submissionId, records);
  }

  function readTemplateBenchmark(submissionId: string): TemplateBenchmarkResult | null {
    const records = benchmarkRecordsBySubmission.get(submissionId) ?? [];
    if (!records.length) {
      return null;
    }

    const model = records[0]?.model ?? '';
    const excludedGroupKeys = records[0]?.excludedGroupKeys ?? [];

    return {
      submissionId,
      model,
      excludedGroupKeys,
      scores: records.map<TemplateBenchmarkScore>((record) => ({
        key: record.templateKey,
        patternTagId: record.patternTagId,
        score: record.score,
        confidence: record.confidence,
        reason: record.reason ?? '',
        evidence: record.evidence ?? [],
      })),
    };
  }

  return {
    submissions: submissions.map<SubmissionRow>((submission) => {
      const question = submission.titleSlug ? questionBySlug.get(submission.titleSlug) : null;
      return {
        id: submission.id,
        titleSlug: submission.titleSlug,
        title: question?.title ?? null,
        difficulty: question?.difficulty ?? null,
        relatedProblems: question?.relatedProblems ?? [],
        status: submission.status,
        templateBenchmarkOptOut: submission.templateBenchmarkOptOut,
        createdAt: submission.createdAt.toISOString(),
        language: readLanguage(submission.submissionDetails),
        timeComplexity: submission.timeComplexity,
        spaceComplexity: submission.spaceComplexity,
        questionDescription: readQuestionDescription(question?.content ?? null),
        submissionCode: submission.content,
        templateBenchmark: readTemplateBenchmark(submission.id),
        tags: submission.SubmissionPatternTag.map((entry) => ({
          id: entry.PatternTag.id,
          key: entry.PatternTag.key,
          label: entry.PatternTag.label,
          dimension: entry.PatternTag.dimension,
          kind: entry.PatternTag.kind,
          parentId: entry.PatternTag.parent?.id ?? null,
          parentKey: entry.PatternTag.parent?.key ?? null,
          parentLabel: entry.PatternTag.parent?.label ?? null,
        })),
      };
    }),
    tags: tags.map<PatternTagOption>((tag) => ({
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
    })),
  };
}

export async function getTemplatesPageData() {
  const [submissions, tags]: [TemplateCatalogSubmission[], ActivePatternTag[]] = await Promise.all([
    prisma.submission.findMany({
      where: { status: 'Accepted' },
      orderBy: { createdAt: 'desc' },
      take: 250,
      select: {
        id: true,
        titleSlug: true,
        createdAt: true,
        SubmissionPatternTag: {
          include: {
            PatternTag: {
              include: { parent: true },
            },
          },
          orderBy: { createdAt: 'asc' },
        },
      },
    }),
    prisma.patternTag.findMany({
      where: { isActive: true },
      include: { parent: true, _count: { select: { SubmissionPatternTag: true } } },
      orderBy: [{ dimension: 'asc' }, { sortOrder: 'asc' }, { label: 'asc' }],
    }),
  ]);

  const slugs = [
    ...new Set(submissions.map((submission) => submission.titleSlug).filter((slug): slug is string => Boolean(slug))),
  ];
  const questions = await prisma.question.findMany({
    where: { titleSlug: { in: slugs } },
    select: { titleSlug: true, title: true },
  });
  const questionBySlug = new Map(questions.map((question) => [question.titleSlug, question]));

  return {
    submissions: submissions.map<TemplateCatalogSubmissionRow>((submission) => ({
      id: submission.id,
      titleSlug: submission.titleSlug,
      title: submission.titleSlug ? questionBySlug.get(submission.titleSlug)?.title ?? null : null,
      createdAt: submission.createdAt.toISOString(),
      tags: submission.SubmissionPatternTag.map((entry) => ({
        id: entry.PatternTag.id,
        key: entry.PatternTag.key,
        label: entry.PatternTag.label,
        dimension: entry.PatternTag.dimension,
        kind: entry.PatternTag.kind,
        parentId: entry.PatternTag.parent?.id ?? null,
        parentKey: entry.PatternTag.parent?.key ?? null,
        parentLabel: entry.PatternTag.parent?.label ?? null,
      })),
    })),
    tags: tags.map<PatternTagOption>((tag) => ({
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
    })),
  };
}

export async function getGraphPageData() {
  const submissions: GraphSubmission[] = await prisma.submission.findMany({
    where: { status: 'Accepted' },
    orderBy: { createdAt: 'desc' },
    take: 250,
    select: {
      id: true,
      titleSlug: true,
      createdAt: true,
      SubmissionPatternTag: {
        include: {
          PatternTag: {
            include: { parent: true },
          },
        },
        orderBy: { createdAt: 'asc' },
      },
    },
  });

  const slugs = [
    ...new Set(submissions.map((submission) => submission.titleSlug).filter((slug): slug is string => Boolean(slug))),
  ];
  const questions = await prisma.question.findMany({
    where: { titleSlug: { in: slugs } },
    select: { titleSlug: true, title: true, difficulty: true, relatedProblems: true },
  });
  const questionBySlug = new Map(questions.map((question) => [question.titleSlug, question]));

  return submissions.map<GraphSubmissionRow>((submission) => {
    const question = submission.titleSlug ? questionBySlug.get(submission.titleSlug) : null;
    return {
      id: submission.id,
      titleSlug: submission.titleSlug,
      title: question?.title ?? null,
      difficulty: question?.difficulty ?? null,
      relatedProblems: question?.relatedProblems ?? [],
      createdAt: submission.createdAt.toISOString(),
      tags: submission.SubmissionPatternTag.map((entry) => ({
        id: entry.PatternTag.id,
        key: entry.PatternTag.key,
        label: entry.PatternTag.label,
        dimension: entry.PatternTag.dimension,
        kind: entry.PatternTag.kind,
        parentId: entry.PatternTag.parent?.id ?? null,
        parentKey: entry.PatternTag.parent?.key ?? null,
        parentLabel: entry.PatternTag.parent?.label ?? null,
      })),
    };
  });
}
