import type { FocusRecommendation, FocusRecommendationResult } from '../core/types.ts';
import type { IntelligenceService } from '../service-runtime/index.ts';
import { createLogger } from '../logger.ts';
import type { PromptDelivery, TextRenderClient } from './contracts.ts';

const logger = createLogger('client/recommendation-flow');
const DEFAULT_MESSAGE_MAX_LENGTH = 2000;

const formatScore = (avgScore: number | null): string => (avgScore === null ? 'n/a' : avgScore.toFixed(2));
const formatRecentSubmission = (days: number | null): string => (days === null ? 'n/a' : `${days.toFixed(1)}d ago`);
const formatEstimatedTime = (minutes: number | null): string => (minutes === null ? 'n/a' : `${minutes}m`);

const formatRecommendations = (recommendations: FocusRecommendation[]): string => {
  if (recommendations.length === 0) {
    return 'No recommendations available right now.';
  }

  return recommendations
    .map((item, index) =>
      [
        `### ${index + 1}. **${item.title}**`,
        `- Slug: \`${item.questionSlug}\``,
        `- Difficulty: **${item.difficulty}**`,
        `- Estimated time: \`${formatEstimatedTime(item.signals.estimatedSolveMinutes)}\``,
        `- Priority: \`${item.priority.toFixed(3)}\``,
        `- Signals: weight \`${item.signals.weight.toFixed(2)}\` | failure \`${Math.round(item.signals.failureRate * 100)}%\` | staleness \`${item.signals.stalenessDays}d\` | avg score \`${formatScore(item.signals.avgScore)}\``,
        `- Recent submissions: attempts \`${item.signals.recentAttemptCount}\` | failure streak \`${item.signals.recentFailureStreak}\` | last submit \`${formatRecentSubmission(item.signals.recentSubmissionDays)}\``,
        `- Why: ${item.reason}`,
      ].join('\n'),
    )
    .join('\n');
};

export const formatRecommendationMessage = (result: FocusRecommendationResult): string =>
  [
    '## Focus Recommendation',
    '',
    '**Summary**',
    result.narrative,
    '',
    '**Recommended Problems**',
    formatRecommendations(result.recommendations),
  ].join('\n');

export const splitRenderedMessage = (body: string, maxLength = DEFAULT_MESSAGE_MAX_LENGTH): string[] => {
  if (body.length <= maxLength) {
    return [body];
  }

  const chunks: string[] = [];
  let remaining = body;

  while (remaining.length > maxLength) {
    const preferredBreak = remaining.lastIndexOf('\n### ', maxLength);
    const fallbackBreak = remaining.lastIndexOf('\n', maxLength);
    const splitAt = preferredBreak > 0 ? preferredBreak : fallbackBreak > 0 ? fallbackBreak : maxLength;

    chunks.push(remaining.slice(0, splitAt).trimEnd());
    remaining = remaining.slice(splitAt).trimStart();
  }

  if (remaining.length > 0) {
    chunks.push(remaining);
  }

  return chunks;
};

export async function dispatchRecommendation(
  service: IntelligenceService,
  client: TextRenderClient,
  topK: number,
  maxLength = DEFAULT_MESSAGE_MAX_LENGTH,
): Promise<{ result: FocusRecommendationResult; deliveries: PromptDelivery[] }> {
  const result = await service.recommendFocus(topK);
  const body = formatRecommendationMessage(result);
  const chunks = splitRenderedMessage(body, maxLength);
  const deliveries: PromptDelivery[] = [];

  for (const chunk of chunks) {
    deliveries.push(await client.renderText(chunk));
  }

  logger.info(
    {
      messageId: deliveries[0]?.messageId ?? null,
      channelId: client.channelId,
      count: result.recommendations.length,
      chunkCount: deliveries.length,
    },
    'sent recommendations message',
  );

  return { result, deliveries };
}
