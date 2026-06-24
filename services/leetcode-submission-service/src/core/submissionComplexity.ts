import { OpenRouter } from '@openrouter/sdk';
import { createLogger } from '../logger.ts';

const COMPLEXITY_ANALYSIS_PROMPT = `
你在做 LeetCode 提交代码的静态复杂度分析。

目标：
- 分析这份代码最主要解法的 time complexity 和 space complexity。
- 只能从给定候选值里各选一个唯一 value。
- 如果代码里有多个辅助函数，按最终主路径的总体复杂度判断。
- 不要输出解释，不要输出 markdown，不要输出额外字段。

只返回 JSON，格式如下：
{
  "time_complexity": "O(n)",
  "space_complexity": "O(1)"
}

time_complexity 可选值：
["O(1)","O(log n)","O(n)","O(n log n)","O(n^2)","O(n^3)","O(2^n)","O(n!)","O(m)","O(m + n)","O(m * n)","O(V + E)","O(V log V + E)"]

space_complexity 可选值：
["O(1)","O(log n)","O(n)","O(n log n)","O(n^2)","O(n^3)","O(m)","O(m + n)","O(m * n)","O(V)","O(V + E)"]
`.trim();

const TIME_COMPLEXITY_VALUES = [
  'O(1)',
  'O(log n)',
  'O(n)',
  'O(n log n)',
  'O(n^2)',
  'O(n^3)',
  'O(2^n)',
  'O(n!)',
  'O(m)',
  'O(m + n)',
  'O(m * n)',
  'O(V + E)',
  'O(V log V + E)',
] as const;

const SPACE_COMPLEXITY_VALUES = [
  'O(1)',
  'O(log n)',
  'O(n)',
  'O(n log n)',
  'O(n^2)',
  'O(n^3)',
  'O(m)',
  'O(m + n)',
  'O(m * n)',
  'O(V)',
  'O(V + E)',
] as const;

type TimeComplexityValue = (typeof TIME_COMPLEXITY_VALUES)[number];
type SpaceComplexityValue = (typeof SPACE_COMPLEXITY_VALUES)[number];

export type SubmissionComplexityAnalysisRequest = {
  titleSlug: string;
  submissionContent: string;
  filetype?: string;
};

export type SubmissionComplexityAnalysisResult = {
  timeComplexity: TimeComplexityValue | null;
  spaceComplexity: SpaceComplexityValue | null;
};

export type SubmissionComplexityAnalyzer = {
  analyze(request: SubmissionComplexityAnalysisRequest): Promise<SubmissionComplexityAnalysisResult>;
};

const logger = createLogger('submission-complexity');

const truncate = (value: string, maxLength: number): string => {
  if (value.length <= maxLength) {
    return value;
  }

  return `${value.slice(0, maxLength - 3)}...`;
};

const normalizeComplexityValue = <TValue extends string>(
  value: unknown,
  allowedValues: readonly TValue[],
): TValue | null => {
  if (typeof value !== 'string') {
    return null;
  }

  const normalized = value.trim();
  return allowedValues.includes(normalized as TValue) ? (normalized as TValue) : null;
};

export const parseSubmissionComplexity = (payload: string): SubmissionComplexityAnalysisResult => {
  try {
    const parsed = JSON.parse(payload) as Record<string, unknown>;
    return {
      timeComplexity: normalizeComplexityValue(parsed.time_complexity, TIME_COMPLEXITY_VALUES),
      spaceComplexity: normalizeComplexityValue(parsed.space_complexity, SPACE_COMPLEXITY_VALUES),
    };
  } catch {
    return {
      timeComplexity: null,
      spaceComplexity: null,
    };
  }
};

class OpenRouterSubmissionComplexityAnalyzer implements SubmissionComplexityAnalyzer {
  constructor(
    private readonly openRouter: OpenRouter,
    private readonly model: string,
  ) {}

  async analyze(request: SubmissionComplexityAnalysisRequest): Promise<SubmissionComplexityAnalysisResult> {
    const startedAt = Date.now();

    try {
      const response = await this.openRouter.chat.send({
        chatRequest: {
          model: this.model,
          temperature: 0,
          responseFormat: { type: 'json_object' },
          messages: [
            {
              role: 'system',
              content: COMPLEXITY_ANALYSIS_PROMPT,
            },
            {
              role: 'user',
              content: JSON.stringify({
                titleSlug: request.titleSlug,
                filetype: request.filetype ?? 'text',
                submissionContent: truncate(request.submissionContent, 12000),
              }),
            },
          ],
        },
      });

      const text = response.choices?.[0]?.message?.content ?? '{}';
      const parsed = parseSubmissionComplexity(text);

      logger.info(
        {
          titleSlug: request.titleSlug,
          model: this.model,
          durationMs: Date.now() - startedAt,
          timeComplexity: parsed.timeComplexity,
          spaceComplexity: parsed.spaceComplexity,
        },
        'Submission complexity analysis completed',
      );

      return parsed;
    } catch (error) {
      logger.error(
        {
          err: error,
          titleSlug: request.titleSlug,
          model: this.model,
          durationMs: Date.now() - startedAt,
        },
        'Submission complexity analysis failed',
      );
      throw error;
    }
  }
}

export const createDefaultSubmissionComplexityAnalyzer = (
  openRouter: OpenRouter,
  model: string,
): SubmissionComplexityAnalyzer => {
  return new OpenRouterSubmissionComplexityAnalyzer(openRouter, model);
};
