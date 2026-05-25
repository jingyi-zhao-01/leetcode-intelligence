import { isFailedStatus } from "./util.ts";
import type {
  PromptAggregate,
  SubmissionAggregate,
} from "./algorithm.ts";

export class RecommendationAggregationBuilder {
  buildSubmissionAggregate(
    submissions: Array<{ titleSlug: string | null; status: string; createdAt: Date }>,
  ): Map<string, SubmissionAggregate> {
    const submissionAgg = new Map<string, SubmissionAggregate>();
    for (const submission of submissions) {
      if (!submission.titleSlug) {
        continue;
      }
      const current = submissionAgg.get(submission.titleSlug) ?? {
        total: 0,
        failed: 0,
        recentFailureStreak: 0,
        lastSubmittedAt: null,
      };
      const failed = isFailedStatus(submission.status);
      current.total += 1;
      if (failed) {
        current.failed += 1;
      }
      if (current.total === 1) {
        current.lastSubmittedAt = submission.createdAt;
      }
      if (current.total - 1 === current.recentFailureStreak && failed) {
        current.recentFailureStreak += 1;
      }
      submissionAgg.set(submission.titleSlug, current);
    }
    return submissionAgg;
  }

  buildPromptAggregate(
    promptEvents: Array<{ questionSlug: string; responseScore: number | null }>,
  ): Map<string, PromptAggregate> {
    const promptAgg = new Map<string, PromptAggregate>();
    for (const event of promptEvents) {
      const current = promptAgg.get(event.questionSlug) ?? { count: 0, scoreSum: 0, scoreCount: 0 };
      current.count += 1;
      if (typeof event.responseScore === "number") {
        current.scoreSum += event.responseScore;
        current.scoreCount += 1;
      }
      promptAgg.set(event.questionSlug, current);
    }
    return promptAgg;
  }
}
