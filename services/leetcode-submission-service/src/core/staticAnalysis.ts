import { OpenRouter } from '@openrouter/sdk';
import type { FailureAnalysisRequest, FailureAnalysisResult } from './failureAnalysis.ts';
import { parseFailureAnalysis } from '../utils/failureAnalysisParser.ts';
import { createLogger } from '../logger.ts';

const FAILURE_ANALYSIS_PROMPT = `
你在分析一次 LeetCode 失败测试。

请用中文、尽可能短地说明 bug，并找出最可能出问题的代码行。
行号必须使用下面带编号 editor buffer 的绝对行号。
只关注用户当前提交和 LeetCode 返回结果，不要重写整题解法。
如果原始错误信息已经暗示了位置，优先保留这个信号。

只返回 JSON，格式如下：
{
  "summary": "极短中文总结",
  "annotations": [
    {
      "line": 12,
      "reason": "极短中文原因",
      "severity": "error"
    }
  ]
}

规则：
- summary 必须是中文，最好 8-20 个字。
- reason 必须是中文，尽量不超过 16 个字。
- severity 只能是 "error" 或 "warn"。
- 最多返回 6 条 annotations。
- 如果推不出有价值的行号，就返回空数组。
- 不要输出 markdown code fence。
- 不要解释，不要寒暄，不要输出 JSON 之外的任何文字。
`.trim();

const logger = createLogger('static-analysis');

const truncate = (value: string, maxLength: number): string => {
  if (value.length <= maxLength) {
    return value;
  }

  return `${value.slice(0, maxLength - 3)}...`;
};

const numberedText = (content: string): string => {
  const lines = content.split('\n');
  return lines.map((line, index) => `${String(index + 1).padStart(4, ' ')} | ${line}`).join('\n');
};

export type FailureStaticAnalyzer = {
  analyze(request: FailureAnalysisRequest): Promise<FailureAnalysisResult>;
};

export class OpenRouterFailureStaticAnalyzer implements FailureStaticAnalyzer {
  constructor(
    private readonly openRouter: OpenRouter,
    private readonly model: string,
  ) {}

  async analyze(request: FailureAnalysisRequest): Promise<FailureAnalysisResult> {
    const maxLine = Math.max(1, request.editorContent.split('\n').length);
    const startedAt = Date.now();
    const numberedBuffer = numberedText(request.editorContent);

    try {
      logger.info(
        {
          analyzer: 'openrouter-llm',
          titleSlug: request.titleSlug,
          filetype: request.filetype || 'text',
          editorContent: numberedBuffer,
        },
        'Static analysis editor content',
      );

      const response = await this.openRouter.chat.send({
        chatRequest: {
          model: this.model,
          temperature: 0,
          responseFormat: { type: 'json_object' },
          messages: [
            {
              role: 'system',
              content: FAILURE_ANALYSIS_PROMPT,
            },
            {
              role: 'user',
              content: JSON.stringify({
                question: {
                  titleSlug: request.titleSlug,
                  title: request.title,
                  description: truncate(request.questionContent, 4000),
                },
                editor: {
                  filetype: request.filetype || 'text',
                  numberedBuffer,
                },
                submissionSentToLeetCode: truncate(request.submissionContent, 6000),
                testcase: truncate(request.testcase, 1500),
                judgeResult: request.judgeResult,
              }),
            },
          ],
        },
      });

      logger.info(
        {
          analyzer: 'openrouter-llm',
          titleSlug: request.titleSlug,
          model: this.model,
          durationMs: Date.now() - startedAt,
        },
        'Static analysis completed',
      );

      const text = response.choices?.[0]?.message?.content ?? '{}';
      return parseFailureAnalysis(text, maxLine);
    } catch (error) {
      logger.error(
        {
          err: error,
          analyzer: 'openrouter-llm',
          titleSlug: request.titleSlug,
          model: this.model,
          durationMs: Date.now() - startedAt,
        },
        'Static analysis failed',
      );
      throw error;
    }
  }
}
