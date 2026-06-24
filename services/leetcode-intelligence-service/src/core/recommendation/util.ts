import type { FocusRecommendation } from '../types.ts';

export const DAY_MS = 24 * 60 * 60 * 1000;

export const round = (value: number, digits = 3): number => {
  const factor = 10 ** digits;
  return Math.round(value * factor) / factor;
};

export const daysSince = (value: Date | null | undefined): number => {
  if (!value) {
    return 365;
  }
  return Math.max(0, (Date.now() - value.getTime()) / DAY_MS);
};

export const normalizeStatus = (status: string | null | undefined): string => {
  return (status ?? '').trim().toLowerCase();
};

export const isFailedStatus = (status: string | null | undefined): boolean => {
  const normalized = normalizeStatus(status);
  return ['wrong answer', 'runtime error', 'time limit exceeded', 'memory limit exceeded', 'compile error'].includes(
    normalized,
  );
};

export const difficultyBoost = (difficulty: string): number => {
  const normalized = difficulty.trim().toLowerCase();
  if (normalized === 'hard') {
    return 0.45;
  }
  if (normalized === 'medium') {
    return 0.2;
  }
  return 0;
};

export const estimatedSolveMinutes = (difficulty: string): number | null => {
  const normalized = difficulty.trim().toLowerCase();
  if (normalized === 'hard') {
    return 45;
  }
  if (normalized === 'medium') {
    return 30;
  }
  if (normalized === 'easy') {
    return 15;
  }
  return null;
};

export const buildReason = (recommendation: FocusRecommendation): string => {
  const failurePct = Math.round(recommendation.signals.failureRate * 100);
  const avgScoreText = recommendation.signals.avgScore === null ? 'n/a' : recommendation.signals.avgScore.toFixed(2);
  const recentSubmissionText =
    recommendation.signals.recentSubmissionDays === null
      ? 'n/a'
      : `${Math.round(recommendation.signals.recentSubmissionDays)}d ago`;
  const estimatedTimeText =
    recommendation.signals.estimatedSolveMinutes === null ? 'n/a' : `${recommendation.signals.estimatedSolveMinutes}m`;

  return [
    `weight=${recommendation.signals.weight.toFixed(2)}`,
    `failureRate=${failurePct}%`,
    `staleness=${Math.round(recommendation.signals.stalenessDays)}d`,
    `avgScore=${avgScoreText}`,
    `estimatedTime=${estimatedTimeText}`,
    `attempts=${recommendation.signals.recentAttemptCount}`,
    `failureStreak=${recommendation.signals.recentFailureStreak}`,
    `lastSubmission=${recentSubmissionText}`,
  ].join(', ');
};
