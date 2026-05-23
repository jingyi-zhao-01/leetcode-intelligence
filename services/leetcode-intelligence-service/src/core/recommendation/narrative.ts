import { OpenRouter } from "@openrouter/sdk";

import type {
  FocusRecommendation,
  IntelligenceConfig,
} from "../types.ts";
import { createLogger } from "../../logger.ts";

const logger = createLogger("intelligence/recommendation");

export interface RecommendationNarrativeGenerator {
  generate(recommendations: FocusRecommendation[]): Promise<string>;
}

export class FallbackRecommendationNarrativeGenerator implements RecommendationNarrativeGenerator {
  async generate(recommendations: FocusRecommendation[]): Promise<string> {
    if (recommendations.length === 0) {
      return "No focus recommendations available right now.";
    }

    return `Focus next: ${recommendations.map((item) => item.questionSlug).join(", ")}.`;
  }
}

export class OpenRouterRecommendationNarrativeGenerator implements RecommendationNarrativeGenerator {
  private readonly fallback = new FallbackRecommendationNarrativeGenerator();

  constructor(
    private readonly openRouter: OpenRouter,
    private readonly config: Pick<IntelligenceConfig, "MODEL">,
  ) {}

  async generate(recommendations: FocusRecommendation[]): Promise<string> {
    if (recommendations.length === 0) {
      return this.fallback.generate(recommendations);
    }

    try {
      logger.info(
        {
          model: this.config.MODEL,
          recommendationCount: recommendations.length,
        },
        "requesting narrative",
      );

      const response = await this.openRouter.chat.send({
        chatRequest: {
          model: this.config.MODEL,
          temperature: 0.3,
          messages: [
            {
              role: "system",
              content: "You generate concise LeetCode study plans. Keep output under 120 words.",
            },
            {
              role: "user",
              content: JSON.stringify({
                topRecommendations: recommendations,
                ask: "Summarize why these should be the current focus and suggest a short execution order.",
              }),
            },
          ],
        },
      });

      const content = response.choices?.[0]?.message?.content?.trim();
      if (!content) {
        logger.warn("OpenRouter narrative response was empty, using fallback summary");
        return this.fallback.generate(recommendations);
      }
      return content;
    } catch (error) {
      logger.warn({ err: error }, "Recommendation narrative fallback used");
      return this.fallback.generate(recommendations);
    }
  }
}

// Placeholder for future narrative backends such as template-based,
// topic-aware, or user-history-aware explanation generators.
export class PlaceholderRecommendationNarrativeGenerator implements RecommendationNarrativeGenerator {
  constructor(
    private readonly fallback: RecommendationNarrativeGenerator = new FallbackRecommendationNarrativeGenerator(),
  ) {}

  async generate(recommendations: FocusRecommendation[]): Promise<string> {
    return this.fallback.generate(recommendations);
  }
}
