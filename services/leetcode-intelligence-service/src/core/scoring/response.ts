import type { PrismaClient } from "@prisma/client";

import type {
  IntelligenceConfig,
  PromptEventWithRelations,
  ScoreRequest,
} from "../types.ts";
import type { ReplyScorer } from "./scoring.ts";
import { LinearWeightCalculator, type WeightCalculator } from "../shared/weight.ts";

export class PromptResponseService {
  private readonly weightCalculator: WeightCalculator;

  constructor(
    private readonly prisma: PrismaClient,
    private readonly scorer: ReplyScorer,
    private readonly config: IntelligenceConfig,
    weightCalculator?: WeightCalculator,
  ) {
    this.weightCalculator = weightCalculator ?? new LinearWeightCalculator();
  }

  async accept(promptEventId: string, rawReply: string): Promise<Record<string, unknown>> {
    const promptEvent = (await this.prisma.intelligencePromptEvent.findUnique({
      where: { id: promptEventId },
      include: { Question: true, Submission: true, IntelligenceResponse: true },
    })) as PromptEventWithRelations | null;

    if (!promptEvent) {
      throw new Error(`Prompt event ${promptEventId} not found.`);
    }

    if (promptEvent.IntelligenceResponse) {
      return { ok: false, message: "Prompt event already scored.", promptEventId };
    }

    const structured = await this.scorer.score({
      questionSlug: promptEvent.questionSlug,
      promptText: promptEvent.promptText,
      submission: promptEvent.Submission,
      rawReply,
    } satisfies ScoreRequest);

    const previousWeight = promptEvent.weightBefore ?? this.weightCalculator.defaultWeight;
    const nextWeight = this.weightCalculator.nextWeightFromScore(previousWeight, structured.score, this.config);

    await this.prisma.$transaction(async (tx: any) => {
      await tx.intelligenceResponse.create({
        data: {
          promptEventId,
          rawContent: rawReply,
          structuredTags: structured.tags,
          approachSummary: structured.approachSummary,
          complexityNotes: structured.complexityNotes,
          blindSpots: structured.blindSpots,
          llmScore: structured.score,
          llmReason: structured.reason,
        },
      });

      await tx.intelligencePromptEvent.update({
        where: { id: promptEventId },
        data: {
          respondedAt: new Date(),
          scoredAt: new Date(),
          responseScore: structured.score,
          weightAfter: nextWeight,
          status: "scored",
        },
      });

      await tx.intelligenceWeight.upsert({
        where: { questionSlug: promptEvent.questionSlug },
        create: {
          questionSlug: promptEvent.questionSlug,
          weight: nextWeight,
          sampleCount: 1,
          lastScore: structured.score,
          lastPromptAt: promptEvent.selectedAt,
          lastResponseAt: new Date(),
        },
        update: {
          weight: nextWeight,
          lastScore: structured.score,
          lastResponseAt: new Date(),
        },
      });

      await tx.intelligenceWeightAudit.create({
        data: {
          questionSlug: promptEvent.questionSlug,
          promptEventId,
          previousWeight,
          nextWeight,
          score: structured.score,
          reason: structured.reason,
        },
      });
    });

    return {
      ok: true,
      promptEventId,
      questionSlug: promptEvent.questionSlug,
      score: structured.score,
      previousWeight,
      nextWeight,
      tags: structured.tags,
      reason: structured.reason,
    };
  }

  async acceptByMessageId(messageId: string, rawReply: string): Promise<Record<string, unknown> | null> {
    const promptEvent = await this.prisma.intelligencePromptEvent.findUnique({
      where: { discordMessageId: messageId },
      select: { id: true },
    });

    if (!promptEvent) {
      return null;
    }

    return this.accept(promptEvent.id, rawReply);
  }
}
