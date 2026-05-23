import { randomInt } from "node:crypto";

import type { PrismaClient } from "@prisma/client";

import type {
  CandidateQuestion,
  CandidateSubmission,
  IntelligenceConfig,
  PromptTransport,
} from "../types.ts";
import { LinearWeightCalculator, type WeightCalculator } from "../shared/weight.ts";

const DISCORD_DESCRIPTION_MAX_CHARS = 1200;

const decodeHtmlEntities = (text: string): string => {
  const namedEntities: Record<string, string> = {
    nbsp: " ",
    amp: "&",
    lt: "<",
    gt: ">",
    quot: '"',
    apos: "'",
  };

  return text
    .replace(/&([a-z]+);/gi, (match, entityName: string) => namedEntities[entityName.toLowerCase()] ?? match)
    .replace(/&#(\d+);/g, (match, codePointRaw: string) => {
      const codePoint = Number.parseInt(codePointRaw, 10);
      return Number.isFinite(codePoint) ? String.fromCodePoint(codePoint) : match;
    })
    .replace(/&#x([\da-f]+);/gi, (match, codePointRaw: string) => {
      const codePoint = Number.parseInt(codePointRaw, 16);
      return Number.isFinite(codePoint) ? String.fromCodePoint(codePoint) : match;
    });
};

const htmlToDiscordText = (html: string): string => {
  const withStructure = html
    .replace(/<br\s*\/?>(\s*)/gi, "\n")
    .replace(/<\/p>/gi, "\n\n")
    .replace(/<p[^>]*>/gi, "")
    .replace(/<li[^>]*>/gi, "- ")
    .replace(/<\/li>/gi, "\n")
    .replace(/<\/?(?:ul|ol)[^>]*>/gi, "\n")
    .replace(/<pre[^>]*>/gi, "\n```text\n")
    .replace(/<\/pre>/gi, "\n```\n")
    .replace(/<code[^>]*>/gi, "`")
    .replace(/<\/code>/gi, "`")
    .replace(/<\/?(?:strong|b)[^>]*>/gi, "**")
    .replace(/<\/?(?:em|i)[^>]*>/gi, "*");

  const withoutTags = withStructure.replace(/<[^>]+>/g, "");
  const decoded = decodeHtmlEntities(withoutTags);

  return decoded
    .replace(/[ \t]+\n/g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
};

const formatProblemDescription = (rawDescription: string): string => {
  const cleaned = htmlToDiscordText(rawDescription);
  if (cleaned.length <= DISCORD_DESCRIPTION_MAX_CHARS) {
    return cleaned;
  }

  return `${cleaned.slice(0, DISCORD_DESCRIPTION_MAX_CHARS)}\n\n...(truncated for Discord readability)`;
};

const buildPromptText = (question: CandidateQuestion, submission: CandidateSubmission): string => {
  const description = question.content
    ? formatProblemDescription(question.content)
    : `${question.title} (${question.difficulty})`;

  return [
    `Problem: ${question.title} [${question.titleSlug}]`,
    `Difficulty: ${question.difficulty}`,
    `Topics: ${(question.topicTags ?? []).join(", ") || "n/a"}`,
    "",
    "Problem description:",
    description,
    "",
    "Past submission:",
    `Submission ID: ${submission.id}`,
    `Status: ${submission.status}`,
    `SubmittedAt: ${submission.createdAt.toISOString()}`,
    "",
    "Reply in this channel with your approach. Include your reasoning, complexity, and any blind spot you see.",
  ].join("\n");
};

export type PromptCandidate = {
  submission: CandidateSubmission;
  question: CandidateQuestion;
  weight: number;
};

export type PromptGenerationResult = {
  ok: true;
  promptEventId: string;
  questionSlug: string;
  submissionId: string;
  weightBefore: number;
  promptText: string;
};

export type PromptGenerationFailure = {
  ok: false;
  message: string;
};

export type PromptGenerationOutcome = PromptGenerationResult | PromptGenerationFailure;

export class PromptGenerator {
  private readonly weightCalculator: WeightCalculator;

  constructor(
    private readonly prisma: PrismaClient,
    private readonly config: IntelligenceConfig,
    weightCalculator?: WeightCalculator,
  ) {
    this.weightCalculator = weightCalculator ?? new LinearWeightCalculator();
  }

  async generate(triggerSource: string, transport?: PromptTransport): Promise<PromptGenerationOutcome> {
    const resolvedTransport = transport ?? { channelId: "cli" };
    const candidate = await this.pickCandidate();
    if (!candidate) {
      return { ok: false, message: "No candidate submission found." };
    }

    const promptText = buildPromptText(candidate.question, candidate.submission);
    const weightBefore = candidate.weight;

    const promptEvent = await this.prisma.intelligencePromptEvent.create({
      data: {
        questionSlug: candidate.question.titleSlug,
        submissionId: candidate.submission.id,
        promptText,
        triggerSource,
        discordChannelId: resolvedTransport.channelId,
        discordMessageId: resolvedTransport.messageId ?? null,
        weightBefore,
        metadata: {
          selectionWindow: this.config.INTELLIGENCE_SELECTION_WINDOW,
          selectedSubmissionStatus: candidate.submission.status,
          selectedSubmissionAt: candidate.submission.createdAt.toISOString(),
        },
      },
    });

    await this.prisma.intelligenceWeight.upsert({
      where: { questionSlug: candidate.question.titleSlug },
      create: {
        questionSlug: candidate.question.titleSlug,
        weight: weightBefore,
        sampleCount: 1,
        lastPromptAt: new Date(),
      },
      update: {
        sampleCount: { increment: 1 },
        lastPromptAt: new Date(),
      },
    });

    return {
      ok: true,
      promptEventId: promptEvent.id,
      questionSlug: candidate.question.titleSlug,
      submissionId: candidate.submission.id,
      weightBefore,
      promptText,
    };
  }
  private async pickCandidate(): Promise<PromptCandidate | null> {
    const submissions = (await this.prisma.submission.findMany({
      where: { titleSlug: { not: null } },
      orderBy: { createdAt: "desc" },
      take: this.config.INTELLIGENCE_MAX_CANDIDATES,
    })) as CandidateSubmission[];

    if (submissions.length === 0) {
      return null;
    }

    const titleSlugs = [
      ...new Set(submissions.map((submission) => submission.titleSlug).filter((titleSlug): titleSlug is string => Boolean(titleSlug))),
    ];
    const questions = (await this.prisma.question.findMany({
      where: { titleSlug: { in: titleSlugs } },
    })) as CandidateQuestion[];
    const questionBySlug = new Map<string, CandidateQuestion>(questions.map((question) => [question.titleSlug, question]));

    const weights = (await this.prisma.intelligenceWeight.findMany({
      where: { questionSlug: { in: titleSlugs } },
    })) as Array<{ questionSlug: string; weight: number }>;
    const weightBySlug = new Map(weights.map((weight) => [weight.questionSlug, weight.weight]));

    const candidates = submissions
      .map<PromptCandidate | null>((submission) => {
        const titleSlug = submission.titleSlug;
        if (!titleSlug) {
          return null;
        }
        const question = questionBySlug.get(titleSlug);
        if (!question) {
          return null;
        }
        return {
          submission: {
            id: submission.id,
            titleSlug,
            content: submission.content,
            status: submission.status,
            createdAt: submission.createdAt,
          },
          question: {
            title: question.title,
            titleSlug: question.titleSlug,
            difficulty: question.difficulty,
            content: question.content,
            topicTags: question.topicTags,
            freqBar: question.freqBar,
          },
          weight: weightBySlug.get(titleSlug) ?? this.weightCalculator.defaultWeight,
        };
      })
      .filter((candidate): candidate is PromptCandidate => candidate !== null)
      .slice(0, this.config.INTELLIGENCE_SELECTION_WINDOW);

    if (candidates.length === 0) {
      return null;
    }

    const totalWeight = candidates.reduce((sum: number, candidate: { weight: number }) => {
      return sum + this.weightCalculator.selectionWeight(candidate.weight);
    }, 0);
    let cursor = (randomInt(0, 1_000_000) / 1_000_000) * totalWeight;

    for (const candidate of candidates) {
      cursor -= this.weightCalculator.selectionWeight(candidate.weight);
      if (cursor <= 0) {
        return candidate;
      }
    }

    return candidates.at(-1) ?? null;
  }
}
