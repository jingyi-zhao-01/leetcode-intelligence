import { OpenRouter } from "@openrouter/sdk";

import type {
  FocusRecommendation,
  FocusRecommendationResult,
  IntelligenceConfig,
} from "../types.ts";
import { createLogger } from "../../logger.ts";
import {
  DAY_MS,
} from "./util.ts";
import {
  HeuristicFocusRecommendationAlgorithm,
  type FocusRecommendationAlgorithm,
  type RecommendationWeightRecord,
} from "./algorithm.ts";
import { RecommendationAggregationBuilder } from "./data.ts";
import {
  FallbackRecommendationNarrativeGenerator,
  OpenRouterRecommendationNarrativeGenerator,
  type RecommendationNarrativeGenerator,
} from "./narrative.ts";
import { LinearWeightCalculator, type WeightCalculator } from "../shared/weight.ts";

const logger = createLogger("intelligence/recommendation");

export class FocusRecommendationService {
  private readonly aggregationBuilder = new RecommendationAggregationBuilder();
  private readonly algorithm: FocusRecommendationAlgorithm;
  private readonly narrativeGenerator: RecommendationNarrativeGenerator;

  constructor(
    private readonly prisma: any,
    private readonly openRouter: OpenRouter | null,
    private readonly config: IntelligenceConfig,
    deps: {
      weightCalculator?: WeightCalculator;
      algorithm?: FocusRecommendationAlgorithm;
      narrativeGenerator?: RecommendationNarrativeGenerator;
    } = {},
  ) {
    const weightCalculator = deps.weightCalculator ?? new LinearWeightCalculator();
    this.algorithm = deps.algorithm ?? new HeuristicFocusRecommendationAlgorithm(weightCalculator);
    this.narrativeGenerator = deps.narrativeGenerator
      ?? (this.openRouter
        ? new OpenRouterRecommendationNarrativeGenerator(this.openRouter, this.config)
        : new FallbackRecommendationNarrativeGenerator());
  }

  async recommend(limit: number): Promise<FocusRecommendationResult> {
    const lookbackDays = this.config.INTELLIGENCE_RECOMMEND_LOOKBACK_DAYS;
    const since = new Date(Date.now() - lookbackDays * DAY_MS);
    const topK = Math.max(1, Math.min(limit, 50));

    const weights = (await this.prisma.intelligenceWeight.findMany({
      orderBy: { weight: "desc" },
      take: this.config.INTELLIGENCE_MAX_CANDIDATES,
      include: { Question: true },
    })) as RecommendationWeightRecord[];

    if (weights.length === 0) {
      return {
        generatedAt: new Date().toISOString(),
        lookbackDays,
        recommendations: [],
        narrative: "No intelligence weights found yet. Trigger a few prompts first.",
      };
    }

    const slugs = [...new Set(weights.map((item) => item.questionSlug))];

    const submissions = (await this.prisma.submission.findMany({
      where: {
        titleSlug: { in: slugs },
        createdAt: { gte: since },
      },
      orderBy: { createdAt: "desc" },
      select: {
        titleSlug: true,
        status: true,
        createdAt: true,
      },
    })) as Array<{ titleSlug: string | null; status: string; createdAt: Date }>;

    const promptEvents = (await this.prisma.intelligencePromptEvent.findMany({
      where: {
        questionSlug: { in: slugs },
        selectedAt: { gte: since },
      },
      select: {
        questionSlug: true,
        responseScore: true,
      },
    })) as Array<{ questionSlug: string; responseScore: number | null }>;

    const submissionAgg = this.aggregationBuilder.buildSubmissionAggregate(submissions);
    const promptAgg = this.aggregationBuilder.buildPromptAggregate(promptEvents);

    const recommendations = this.algorithm.rank({
      lookbackDays,
      topK,
      maxWeight: this.config.INTELLIGENCE_MAX_WEIGHT,
      weights,
      submissionAgg,
      promptAgg,
    });

    const narrative = await this.narrativeGenerator.generate(recommendations);

    return {
      generatedAt: new Date().toISOString(),
      lookbackDays,
      recommendations,
      narrative,
    };
  }
}
