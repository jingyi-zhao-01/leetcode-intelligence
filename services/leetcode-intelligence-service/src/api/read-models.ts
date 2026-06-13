import type { ApiContext } from "./context.ts";
import {
  mapPatternTagOption,
  readLanguage,
  readQuestionDescription,
  type ActivePatternTag,
  type PatternTagRecord,
  type SubmissionPatternTagRecord,
  type TemplateBenchmarkRecord,
} from "./shared.ts";
import type {
  GraphSubmissionRow,
  PatternTagKind,
  PatternTagSource,
  SubmissionRow,
  TemplateBenchmarkResult,
  TemplateCatalogSubmissionRow,
} from "./types.ts";

type TagWorkbenchSubmission = {
  id: string;
  titleSlug: string | null;
  status: string;
  createdAt: Date;
  templateBenchmarkOptOut: boolean;
  submissionDetails: unknown;
  timeComplexity: string | null;
  spaceComplexity: string | null;
  content: string;
  SubmissionPatternTag: SubmissionPatternTagRecord[];
};

type TemplateCatalogSubmission = {
  id: string;
  titleSlug: string | null;
  createdAt: Date;
  SubmissionPatternTag: SubmissionPatternTagRecord[];
};

type GraphSubmission = {
  id: string;
  titleSlug: string | null;
  createdAt: Date;
  SubmissionPatternTag: SubmissionPatternTagRecord[];
};

type TagWorkbenchQuestionRecord = {
  titleSlug: string;
  title: string | null;
  difficulty: string | null;
  content: string | null;
  relatedProblems: string[];
};

type TemplateCatalogQuestionRecord = {
  titleSlug: string;
  title: string | null;
};

type GraphQuestionRecord = {
  titleSlug: string;
  title: string | null;
  difficulty: string | null;
  relatedProblems: string[];
};

type SubmissionTagShape = {
  id: string;
  key: string;
  label: string;
  dimension: string;
  kind: PatternTagKind;
  parentId: string | null;
  parentKey: string | null;
  parentLabel: string | null;
};

function mapSubmissionTags(records: SubmissionPatternTagRecord[]): SubmissionTagShape[] {
  return records.map((entry) => ({
    id: entry.PatternTag.id,
    key: entry.PatternTag.key,
    label: entry.PatternTag.label,
    dimension: entry.PatternTag.dimension,
    kind: entry.PatternTag.kind,
    parentId: entry.PatternTag.parent?.id ?? null,
    parentKey: entry.PatternTag.parent?.key ?? null,
    parentLabel: entry.PatternTag.parent?.label ?? null,
  }));
}

function buildTemplateBenchmarkLookup(records: TemplateBenchmarkRecord[]) {
  const benchmarkRecordsBySubmission = new Map<string, TemplateBenchmarkRecord[]>();
  for (const record of records) {
    const rows = benchmarkRecordsBySubmission.get(record.submissionId) ?? [];
    rows.push(record);
    benchmarkRecordsBySubmission.set(record.submissionId, rows);
  }

  return (submissionId: string): TemplateBenchmarkResult | null => {
    const rows = benchmarkRecordsBySubmission.get(submissionId) ?? [];
    if (!rows.length) {
      return null;
    }

    return {
      submissionId,
      model: rows[0]?.model ?? "",
      excludedGroupKeys: rows[0]?.excludedGroupKeys ?? [],
      scores: rows.map((record) => ({
        key: record.templateKey,
        patternTagId: record.patternTagId,
        score: record.score,
        confidence: record.confidence,
        reason: record.reason ?? "",
        evidence: record.evidence ?? [],
      })),
    };
  };
}

export function createReadModelsApi({ prisma }: ApiContext) {
  const getTagWorkbenchData = async () => {
    const [submissions, tags]: [TagWorkbenchSubmission[], ActivePatternTag[]] = await Promise.all([
      prisma.submission.findMany({
        where: { status: "Accepted" },
        orderBy: { createdAt: "desc" },
        take: 250,
        include: {
          SubmissionPatternTag: {
            include: {
              PatternTag: {
                include: { parent: true },
              },
            },
            orderBy: { createdAt: "asc" },
          },
        },
      }),
      prisma.patternTag.findMany({
        where: { isActive: true },
        include: { parent: true, _count: { select: { SubmissionPatternTag: true } } },
        orderBy: [{ dimension: "asc" }, { sortOrder: "asc" }, { label: "asc" }],
      }),
    ]);

    const slugs = [...new Set(submissions.map((submission) => submission.titleSlug).filter((slug): slug is string => Boolean(slug)))];
    const questions: TagWorkbenchQuestionRecord[] = await prisma.question.findMany({
      where: { titleSlug: { in: slugs } },
      select: { titleSlug: true, title: true, difficulty: true, content: true, relatedProblems: true },
    });
    const questionBySlug = new Map(questions.map((question) => [question.titleSlug, question]));

    const submissionIds = submissions.map((submission) => submission.id);
    const benchmarkRecords: TemplateBenchmarkRecord[] = submissionIds.length
      ? await prisma.templateBenchmarkScore.findMany({
          where: { submissionId: { in: submissionIds } },
          select: {
            submissionId: true,
            patternTagId: true,
            templateKey: true,
            model: true,
            score: true,
            confidence: true,
            reason: true,
            evidence: true,
            excludedGroupKeys: true,
            updatedAt: true,
          },
          orderBy: [{ submissionId: "asc" }, { score: "desc" }, { updatedAt: "desc" }],
        })
      : [];

    const readTemplateBenchmark = buildTemplateBenchmarkLookup(benchmarkRecords);

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
          tags: mapSubmissionTags(submission.SubmissionPatternTag),
        };
      }),
      tags: tags.map(mapPatternTagOption),
    };
  };

  const getTemplatesPageData = async () => {
    const [submissions, tags]: [TemplateCatalogSubmission[], ActivePatternTag[]] = await Promise.all([
      prisma.submission.findMany({
        where: { status: "Accepted" },
        orderBy: { createdAt: "desc" },
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
            orderBy: { createdAt: "asc" },
          },
        },
      }),
      prisma.patternTag.findMany({
        where: { isActive: true },
        include: { parent: true, _count: { select: { SubmissionPatternTag: true } } },
        orderBy: [{ dimension: "asc" }, { sortOrder: "asc" }, { label: "asc" }],
      }),
    ]);

    const slugs = [...new Set(submissions.map((submission) => submission.titleSlug).filter((slug): slug is string => Boolean(slug)))];
    const questions: TemplateCatalogQuestionRecord[] = await prisma.question.findMany({
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
        tags: mapSubmissionTags(submission.SubmissionPatternTag),
      })),
      tags: tags.map(mapPatternTagOption),
    };
  };

  const getGraphPageData = async () => {
    const submissions: GraphSubmission[] = await prisma.submission.findMany({
      where: { status: "Accepted" },
      orderBy: { createdAt: "desc" },
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
          orderBy: { createdAt: "asc" },
        },
      },
    });

    const slugs = [...new Set(submissions.map((submission) => submission.titleSlug).filter((slug): slug is string => Boolean(slug)))];
    const questions: GraphQuestionRecord[] = await prisma.question.findMany({
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
        tags: mapSubmissionTags(submission.SubmissionPatternTag),
      };
    });
  };

  return {
    getTagWorkbenchData,
    getTemplatesPageData,
    getGraphPageData,
  };
}
