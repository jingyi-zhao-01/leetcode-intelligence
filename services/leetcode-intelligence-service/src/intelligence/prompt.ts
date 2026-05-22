import { randomInt } from "node:crypto";

import type { PrismaClient } from "@prisma/client";

import type {
  CandidateQuestion,
  CandidateSubmission,
  IntelligenceConfig,
  PromptTransport,
} from "./types.ts";

const buildPromptText = (question: CandidateQuestion, submission: CandidateSubmission): string => {
  const description = question.content?.trim() || `${question.title} (${question.difficulty})`;

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
  constructor(
    private readonly prisma: PrismaClient,
    private readonly config: IntelligenceConfig,
  ) {}

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
          weight: weightBySlug.get(titleSlug) ?? 1,
        };
      })
      .filter((candidate): candidate is PromptCandidate => candidate !== null)
      .slice(0, this.config.INTELLIGENCE_SELECTION_WINDOW);

    if (candidates.length === 0) {
      return null;
    }

    const totalWeight = candidates.reduce((sum: number, candidate: { weight: number }) => sum + Math.max(candidate.weight, 0.01), 0);
    let cursor = (randomInt(0, 1_000_000) / 1_000_000) * totalWeight;

    for (const candidate of candidates) {
      cursor -= Math.max(candidate.weight, 0.01);
      if (cursor <= 0) {
        return candidate;
      }
    }

    return candidates.at(-1) ?? null;
  }
}
