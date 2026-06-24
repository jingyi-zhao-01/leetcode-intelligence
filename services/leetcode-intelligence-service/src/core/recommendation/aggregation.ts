import { createLogger } from '../../logger.ts';
import { isFailedStatus } from './util.ts';
import type { ScoringAggregate, SubmissionAggregate } from './algorithm.ts';

const logger = createLogger('intelligence/recommendation');

export class RecommendationAggregationBuilder {
  /**
   * Collapse recent submission rows into per-question stats used by ranking,
   * including failure counts, failure streak, and last submission time.
   */
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

    logger.info(
      {
        aggregateCount: submissionAgg.size,
        submissionAggregate: Array.from(submissionAgg.entries()).map(([titleSlug, aggregate]) => ({
          titleSlug,
          ...aggregate,
        })),
      },
      'built submission aggregate',
    );

    return submissionAgg;
  }

  /**
   * Collapse prompt-response history into per-question scoring stats so
   * ranking can derive review frequency and average evaluation score.
   */
  buildScoringAggregate(
    promptEvents: Array<{ questionSlug: string; responseScore: number | null }>,
  ): Map<string, ScoringAggregate> {
    const scoringAgg = new Map<string, ScoringAggregate>();
    for (const event of promptEvents) {
      const current = scoringAgg.get(event.questionSlug) ?? { count: 0, scoreSum: 0, scoreCount: 0 };
      current.count += 1;
      if (typeof event.responseScore === 'number') {
        current.scoreSum += event.responseScore;
        current.scoreCount += 1;
      }
      scoringAgg.set(event.questionSlug, current);
    }

    logger.info(
      {
        aggregateCount: scoringAgg.size,
        scoringAggregate: Array.from(scoringAgg.entries()).map(([questionSlug, aggregate]) => ({
          questionSlug,
          ...aggregate,
        })),
      },
      'built scoring aggregate',
    );

    return scoringAgg;
  }
}
