import { PrismaClient } from "../../../node_modules/@prisma/client";
import {
  analyzeCommentThemes,
  analyzeOverallProgression,
  countComplexityMentions,
  extractComments,
} from "./util.js";

const DIFFICULTY_MAP: Record<string, string> = {
  easy: "Easy",
  medium: "Medium",
  hard: "Hard",
};

function normalizeSlug(value: string): string {
  const slug = (value ?? "").trim();
  if (!slug) {
    throw new Error("'slug' is required and cannot be empty.");
  }
  return slug;
}

function normalizeQuery(value: string): string {
  const query = (value ?? "").trim();
  if (!query) {
    throw new Error("'query' is required and cannot be empty.");
  }
  return query;
}

function normalizeDifficulty(value?: string | null): string | undefined {
  if (!value) {
    return undefined;
  }
  const mapped = DIFFICULTY_MAP[value.trim().toLowerCase()];
  if (!mapped) {
    throw new Error(`Invalid difficulty '${value}'. Allowed values: Easy, Medium, Hard.`);
  }
  return mapped;
}

function normalizeTopic(value?: string | null): string | undefined {
  const topic = (value ?? "").trim();
  return topic || undefined;
}

function normalizeTopics(values?: string[] | null): string[] {
  const seen = new Set<string>();
  const result: string[] = [];
  for (const value of values ?? []) {
    const topic = (value ?? "").trim();
    if (!topic || seen.has(topic)) {
      continue;
    }
    seen.add(topic);
    result.push(topic);
  }
  return result;
}

function normalizePagination(limit: number, offset: number): { limit: number; offset: number } {
  return {
    limit: Math.max(1, Math.min(Number(limit) || 20, 100)),
    offset: Math.max(0, Number(offset) || 0),
  };
}

function questionSummary(question: {
  title: string;
  titleSlug: string;
  difficulty: string;
  topicTags: string[];
  freqBar: number | null;
}) {
  return {
    title: question.title,
    slug: question.titleSlug,
    difficulty: question.difficulty,
    topics: question.topicTags ?? [],
    popularity: question.freqBar,
  };
}

function parseDate(value: string): Date {
  const normalized = value.trim().toLowerCase();
  const now = new Date();

  if (normalized === "today") {
    return new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate()));
  }
  if (normalized === "yesterday") {
    const d = new Date(Date.UTC(now.getUTCFullYear(), now.getUTCMonth(), now.getUTCDate()));
    d.setUTCDate(d.getUTCDate() - 1);
    return d;
  }

  const date = new Date(`${normalized}T00:00:00.000Z`);
  if (Number.isNaN(date.getTime())) {
    throw new Error(`Invalid date '${value}'. Use 'today', 'yesterday', or 'YYYY-MM-DD'.`);
  }
  return date;
}

function resolveDateRange(period?: string, startDate?: string, endDate?: string) {
  if (startDate) {
    const start = parseDate(startDate);
    const endBase = endDate ? parseDate(endDate) : start;
    const end = new Date(endBase);
    end.setUTCDate(end.getUTCDate() + 1);
    return {
      start,
      end,
      label: endDate && endDate !== startDate ? `${startDate} to ${endDate}` : startDate,
    };
  }

  const label = period ?? "today";
  const start = parseDate(label);
  const end = new Date(start);
  end.setUTCDate(end.getUTCDate() + 1);
  return { start, end, label };
}

function toOrderBy(sortBy: string) {
  const key = (sortBy || "title").trim().toLowerCase();
  if (["popularity", "freq_bar", "-popularity", "-freq_bar"].includes(key)) {
    return { orderBy: [{ freqBar: "desc" as const }, { titleSlug: "asc" as const }], label: "freq_bar_desc" };
  }
  if (["-title", "title_desc"].includes(key)) {
    return { orderBy: [{ title: "desc" as const }, { titleSlug: "asc" as const }], label: "title_desc" };
  }
  if (["difficulty", "difficulty_asc"].includes(key)) {
    return { orderBy: [{ difficulty: "asc" as const }, { titleSlug: "asc" as const }], label: "difficulty_asc" };
  }
  if (["-difficulty", "difficulty_desc"].includes(key)) {
    return { orderBy: [{ difficulty: "desc" as const }, { titleSlug: "asc" as const }], label: "difficulty_desc" };
  }
  return { orderBy: [{ title: "asc" as const }, { titleSlug: "asc" as const }], label: "title_asc" };
}

export async function getSubmissionHistory(db: PrismaClient, titleSlug: string) {
  try {
    const submissions = await db.submission.findMany({
      where: { titleSlug },
      orderBy: { createdAt: "asc" },
    });

    if (submissions.length === 0) {
      return {
        title_slug: titleSlug,
        total_submissions: 0,
        message: "No submissions found for this problem",
      };
    }

    return {
      title_slug: titleSlug,
      total_submissions: submissions.length,
      submissions: submissions.map((s) => ({
        submissionId: s.id,
        submittedCode: s.content ?? "",
        result: s.status,
        mistakes: s.mistake,
        time: s.createdAt.toISOString(),
      })),
    };
  } catch (error) {
    return { error: `Failed to get submission history: ${String(error)}`, title_slug: titleSlug };
  }
}

export async function getSubmissionDetail(db: PrismaClient, submissionId: string) {
  try {
    const submission = await db.submission.findUnique({ where: { id: submissionId } });
    if (!submission) {
      return { submissionId, message: "Submission not found" };
    }

    return {
      submissionId: submission.id,
      titleSlug: submission.titleSlug,
      submittedCode: submission.content,
      result: submission.status,
      thought: submission.thought,
      mistakes: submission.mistake,
      time: submission.createdAt.toISOString(),
      submissionDetails: submission.submissionDetails,
      isCheat: submission.isCheat,
      timeSpentMinutes: submission.timeSpentMinutes,
    };
  } catch (error) {
    return { error: `Failed to get submission detail: ${String(error)}` };
  }
}

export async function analyzeThoughtProgression(db: PrismaClient, titleSlug: string) {
  try {
    const submissions = await db.submission.findMany({
      where: { titleSlug },
      orderBy: { createdAt: "asc" },
    });

    if (submissions.length === 0) {
      return { title_slug: titleSlug, message: "No submissions found for this problem" };
    }

    const commentEvolution = submissions.map((submission, index) => {
      const comments = extractComments(submission.content ?? "");
      return {
        attempt_number: index + 1,
        timestamp: submission.createdAt.toISOString(),
        status: submission.status,
        comments_count: comments.length,
        comments,
        comment_themes: analyzeCommentThemes(comments),
        complexity_mentions: countComplexityMentions(comments),
        thought: submission.thought,
      };
    });

    return {
      title_slug: titleSlug,
      total_submissions: submissions.length,
      comment_evolution: commentEvolution,
      progression_analysis: analyzeOverallProgression(commentEvolution),
    };
  } catch (error) {
    return { error: `Failed to analyze thought progression: ${String(error)}`, title_slug: titleSlug };
  }
}

export async function reviewSubmissions(
  db: PrismaClient,
  period = "today",
  startDate?: string,
  endDate?: string,
) {
  const label = startDate || period || "today";
  try {
    const range = resolveDateRange(period, startDate, endDate);

    const submissions = await db.submission.findMany({
      where: {
        createdAt: {
          gte: range.start,
          lt: range.end,
        },
      },
      orderBy: { createdAt: "asc" },
    });

    if (submissions.length === 0) {
      return {
        period: range.label,
        date_range: { start: range.start.toISOString(), end: range.end.toISOString() },
        message: `No submissions found for '${range.label}'.`,
        problems: [],
        summary_stats: {
          total_problems_attempted: 0,
          total_accepted: 0,
          acceptance_rate_pct: 0,
          total_submissions: 0,
          error_type_counts: {},
          topics_covered: [],
        },
      };
    }

    const grouped = new Map<string, typeof submissions>();
    for (const sub of submissions) {
      const key = sub.titleSlug ?? "unknown";
      const curr = grouped.get(key) ?? [];
      curr.push(sub);
      grouped.set(key, curr);
    }

    const questionSlugs = Array.from(grouped.keys()).filter((slug) => slug !== "unknown");
    const questions = await db.question.findMany({ where: { titleSlug: { in: questionSlugs } } });
    const questionMap = new Map(questions.map((q) => [q.titleSlug, q]));

    const errorTypeCounts: Record<string, number> = {};
    const topicsCovered = new Set<string>();
    let totalAccepted = 0;

    const problems = Array.from(grouped.entries()).map(([slug, subs]) => {
      const q = questionMap.get(slug);
      const statuses = subs.map((s) => s.status);
      const finalStatus = statuses[statuses.length - 1] ?? "Unknown";
      if (finalStatus === "Accepted") {
        totalAccepted += 1;
      }
      for (const status of statuses) {
        if (status !== "Accepted") {
          errorTypeCounts[status] = (errorTypeCounts[status] ?? 0) + 1;
        }
      }

      const tags = q?.topicTags ?? [];
      for (const tag of tags) {
        topicsCovered.add(tag);
      }

      return {
        title_slug: slug,
        title: q?.title ?? slug,
        difficulty: q?.difficulty ?? "Unknown",
        topic_tags: tags,
        attempts: subs.length,
        statuses,
        final_status: finalStatus,
        total_time_spent_minutes: subs.reduce((sum, item) => sum + (item.timeSpentMinutes ?? 0), 0),
        first_attempt_at: subs[0].createdAt.toISOString(),
        final_submission_code: subs[subs.length - 1].content,
        final_submission_thought: subs[subs.length - 1].thought,
      };
    });

    return {
      period: range.label,
      date_range: { start: range.start.toISOString(), end: range.end.toISOString() },
      summary_stats: {
        total_problems_attempted: problems.length,
        total_accepted: totalAccepted,
        acceptance_rate_pct: problems.length > 0 ? Number(((totalAccepted / problems.length) * 100).toFixed(1)) : 0,
        total_submissions: submissions.length,
        error_type_counts: errorTypeCounts,
        topics_covered: Array.from(topicsCovered).sort(),
      },
      problems,
    };
  } catch (error) {
    return { error: `Failed to review submissions: ${String(error)}`, period: label };
  }
}

export async function searchProblems(
  db: PrismaClient,
  query: string,
  topic?: string,
  difficulty?: string,
  limit = 20,
  offset = 0,
) {
  try {
    const normalizedQuery = normalizeQuery(query);
    const normalizedTopic = normalizeTopic(topic);
    const normalizedDifficulty = normalizeDifficulty(difficulty);
    const page = normalizePagination(limit, offset);

    const where: Record<string, unknown> = {
      title: { contains: normalizedQuery, mode: "insensitive" },
    };
    if (normalizedTopic) {
      where.topicTags = { has: normalizedTopic };
    }
    if (normalizedDifficulty) {
      where.difficulty = normalizedDifficulty;
    }

    const [total, items] = await Promise.all([
      db.question.count({ where }),
      db.question.findMany({
        where,
        orderBy: [{ title: "asc" }, { titleSlug: "asc" }],
        skip: page.offset,
        take: page.limit,
      }),
    ]);

    return {
      query: normalizedQuery,
      filters: { topic: normalizedTopic ?? null, difficulty: normalizedDifficulty ?? null },
      items: items.map(questionSummary),
      total,
      limit: page.limit,
      offset: page.offset,
    };
  } catch (error) {
    return { error: String(error) };
  }
}

export async function getProblemDetails(db: PrismaClient, slug: string) {
  try {
    const normalizedSlug = normalizeSlug(slug);
    const question = await db.question.findUnique({ where: { titleSlug: normalizedSlug } });
    if (!question) {
      return { error: `Problem '${normalizedSlug}' not found.` };
    }

    const [attempts, accepted] = await Promise.all([
      db.submission.count({ where: { titleSlug: normalizedSlug } }),
      db.submission.count({ where: { titleSlug: normalizedSlug, status: "Accepted" } }),
    ]);

    return {
      title: question.title,
      slug: question.titleSlug,
      difficulty: question.difficulty,
      description: question.content,
      topics: question.topicTags ?? [],
      related_problems: question.relatedProblems ?? [],
      popularity: question.freqBar,
      submission_summary: {
        attempts,
        accepted_submissions: accepted,
        is_solved: accepted > 0,
      },
    };
  } catch (error) {
    return { error: `Failed to get problem details: ${String(error)}` };
  }
}

export async function getRelatedProblems(db: PrismaClient, slug: string, includeDetails = true) {
  try {
    const normalizedSlug = normalizeSlug(slug);
    const source = await db.question.findUnique({ where: { titleSlug: normalizedSlug } });
    if (!source) {
      return { error: `Problem '${normalizedSlug}' not found.` };
    }

    const relatedSlugs = source.relatedProblems ?? [];
    if (relatedSlugs.length === 0) {
      return { slug: normalizedSlug, related_problems: [], missing_slugs: [] };
    }

    const relatedRows = await db.question.findMany({
      where: { titleSlug: { in: relatedSlugs } },
      orderBy: { titleSlug: "asc" },
    });
    const rowMap = new Map(relatedRows.map((row) => [row.titleSlug, row]));
    const missing = relatedSlugs.filter((s) => !rowMap.has(s));

    if (includeDetails) {
      return {
        slug: normalizedSlug,
        related_problems: relatedSlugs.filter((s) => rowMap.has(s)).map((s) => questionSummary(rowMap.get(s)!)),
        missing_slugs: missing,
      };
    }

    return {
      slug: normalizedSlug,
      related_problems: relatedSlugs.filter((s) => rowMap.has(s)),
      missing_slugs: missing,
    };
  } catch (error) {
    return { error: `Failed to get related problems: ${String(error)}` };
  }
}

export async function listProblemsByFilters(
  db: PrismaClient,
  topics?: string[],
  difficulty?: string,
  sortBy = "title",
  limit = 50,
  offset = 0,
) {
  try {
    const normalizedTopics = normalizeTopics(topics);
    const normalizedDifficulty = normalizeDifficulty(difficulty);
    const page = normalizePagination(limit, offset);
    const order = toOrderBy(sortBy);

    const where: Record<string, unknown> = {};
    if (normalizedTopics.length > 0) {
      where.topicTags = { hasEvery: normalizedTopics };
    }
    if (normalizedDifficulty) {
      where.difficulty = normalizedDifficulty;
    }

    const [total, items] = await Promise.all([
      db.question.count({ where }),
      db.question.findMany({
        where,
        orderBy: order.orderBy,
        skip: page.offset,
        take: page.limit,
      }),
    ]);

    return {
      filters: { topics: normalizedTopics, difficulty: normalizedDifficulty ?? null },
      sort_by: order.label,
      items: items.map(questionSummary),
      total,
      limit: page.limit,
      offset: page.offset,
    };
  } catch (error) {
    return { error: `Failed to list problems by filters: ${String(error)}` };
  }
}

export async function listPopularProblems(
  db: PrismaClient,
  topic?: string,
  difficulty?: string,
  limit = 20,
  offset = 0,
) {
  try {
    const normalizedTopic = normalizeTopic(topic);
    const normalizedDifficulty = normalizeDifficulty(difficulty);
    const page = normalizePagination(limit, offset);

    const where: Record<string, unknown> = {};
    if (normalizedTopic) {
      where.topicTags = { has: normalizedTopic };
    }
    if (normalizedDifficulty) {
      where.difficulty = normalizedDifficulty;
    }

    const [total, items] = await Promise.all([
      db.question.count({ where }),
      db.question.findMany({
        where,
        orderBy: [{ freqBar: "desc" }, { titleSlug: "asc" }],
        skip: page.offset,
        take: page.limit,
      }),
    ]);

    return {
      filters: { topic: normalizedTopic ?? null, difficulty: normalizedDifficulty ?? null },
      sort_by: "freq_bar_desc",
      items: items.map(questionSummary),
      total,
      limit: page.limit,
      offset: page.offset,
    };
  } catch (error) {
    return { error: `Failed to list popular problems: ${String(error)}` };
  }
}

export async function checkProblemSolved(db: PrismaClient, slug: string) {
  try {
    const normalizedSlug = normalizeSlug(slug);
    const accepted = await db.submission.count({
      where: { titleSlug: normalizedSlug, status: "Accepted" },
    });

    return {
      slug: normalizedSlug,
      is_solved: accepted > 0,
      accepted_submissions: accepted,
    };
  } catch (error) {
    return { error: `Failed to check solved state: ${String(error)}` };
  }
}

export async function saveSubmissionMistakes(
  db: PrismaClient,
  submissionId: string,
  mistakes: string[],
) {
  if (!(submissionId ?? "").trim()) {
    return { error: "'submission_id' is required and cannot be empty." };
  }
  if (!mistakes || mistakes.length === 0) {
    return { error: "'mistakes' list cannot be empty." };
  }

  const bulletText = mistakes
    .map((item) => item.trim())
    .filter(Boolean)
    .map((item) => `- ${item}`)
    .join("\n");

  if (!bulletText) {
    return { error: "All provided mistake items were blank." };
  }

  const existing = await db.submission.findUnique({ where: { id: submissionId } });
  if (!existing) {
    return {
      submission_id: submissionId,
      message: "Submission not found",
    };
  }

  await db.submission.update({
    where: { id: submissionId },
    data: { mistake: bulletText },
  });

  return {
    submission_id: submissionId,
    mistakes: bulletText,
  };
}
