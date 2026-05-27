import { OpenRouter } from "@openrouter/sdk";
import type { FailureAnalysisRequest, FailureAnalysisResult } from "./failureAnalysis.js";
import { parseFailureAnalysis } from "./failureAnalysisParser.js";
import { createLogger } from "./logger.js";

const FAILURE_ANALYSIS_PROMPT = `
You are analyzing a failed LeetCode test run.

Explain the bug briefly in English, then identify the most likely problematic lines in the user's editor buffer.
Use the absolute line numbers from the numbered editor buffer below.
Focus on the user's submission and the LeetCode error response. Do not rewrite the whole solution.
If the raw LeetCode error already suggests a location, preserve that signal in your analysis.

Return JSON only with this shape:
{
  "summary": "short English explanation",
  "annotations": [
    {
      "line": 12,
      "reason": "short English reason",
      "severity": "error"
    }
  ]
}

Rules:
- summary must be English.
- reason must be concise and in English.
- severity must be "error" or "warn".
- Keep at most 6 annotations.
- If you cannot infer a useful line, return an empty annotations array.
- Do not wrap the JSON in markdown fences.
`.trim();

const logger = createLogger("static-analysis");

const truncate = (value: string, maxLength: number): string => {
  if (value.length <= maxLength) {
    return value;
  }

  return `${value.slice(0, maxLength - 3)}...`;
};

const numberedText = (content: string): string => {
  const lines = content.split("\n");
  return lines.map((line, index) => `${String(index + 1).padStart(4, " ")} | ${line}`).join("\n");
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
    const maxLine = Math.max(1, request.editorContent.split("\n").length);
    const startedAt = Date.now();

    try {
      const response = await this.openRouter.chat.send({
        chatRequest: {
          model: this.model,
          temperature: 0,
          responseFormat: { type: "json_object" },
          messages: [
            {
              role: "system",
              content: FAILURE_ANALYSIS_PROMPT,
            },
            {
              role: "user",
              content: JSON.stringify({
                question: {
                  titleSlug: request.titleSlug,
                  title: request.title,
                  description: truncate(request.questionContent, 4000),
                },
                editor: {
                  filetype: request.filetype || "text",
                  numberedBuffer: numberedText(request.editorContent),
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
          analyzer: "openrouter-llm",
          titleSlug: request.titleSlug,
          model: this.model,
          durationMs: Date.now() - startedAt,
        },
        "Static analysis completed",
      );

      const text = response.choices?.[0]?.message?.content ?? "{}";
      return parseFailureAnalysis(text, maxLine);
    } catch (error) {
      logger.error(
        {
          err: error,
          analyzer: "openrouter-llm",
          titleSlug: request.titleSlug,
          model: this.model,
          durationMs: Date.now() - startedAt,
        },
        "Static analysis failed",
      );
      throw error;
    }
  }
}
