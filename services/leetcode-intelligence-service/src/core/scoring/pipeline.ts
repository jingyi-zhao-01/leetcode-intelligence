import type { PromptCooldownRule, WeightedCandidate } from "../types.ts";

export type PromptPipelineEntry = WeightedCandidate & {
  lastPromptAt: Date | null;
};

const matchesRule = (entry: PromptPipelineEntry, rule: PromptCooldownRule): boolean => {
  if (rule.titleSlugs && !rule.titleSlugs.includes(entry.question.titleSlug)) {
    return false;
  }

  if (rule.statuses && !rule.statuses.includes(entry.submission.status)) {
    return false;
  }

  if (rule.difficulties && !rule.difficulties.includes(entry.question.difficulty)) {
    return false;
  }

  return true;
};

export class PromptCandidatePipeline {
  constructor(
    private readonly entries: PromptPipelineEntry[],
    private readonly now: Date = new Date(),
  ) {}

  dropPromptedQuestions(rules: PromptCooldownRule[]): PromptCandidatePipeline {
    return new PromptCandidatePipeline(
      this.entries.filter((entry) => {
        const rule = rules.find((candidateRule) => matchesRule(entry, candidateRule));
        if (!rule || !entry.lastPromptAt) {
          return true;
        }

        const cooldownMs = rule.cooldownHours * 60 * 60 * 1000;
        return this.now.getTime() - entry.lastPromptAt.getTime() >= cooldownMs;
      }),
      this.now,
    );
  }

  dedupeByQuestion(): PromptCandidatePipeline {
    const seen = new Set<string>();

    return new PromptCandidatePipeline(
      this.entries.filter((entry) => {
        if (seen.has(entry.question.titleSlug)) {
          return false;
        }

        seen.add(entry.question.titleSlug);
        return true;
      }),
      this.now,
    );
  }

  take(limit: number): PromptCandidatePipeline {
    return new PromptCandidatePipeline(this.entries.slice(0, limit), this.now);
  }

  toArray(): PromptPipelineEntry[] {
    return [...this.entries];
  }
}
