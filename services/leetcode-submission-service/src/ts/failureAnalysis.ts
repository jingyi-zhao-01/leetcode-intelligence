import { OpenRouter } from "@openrouter/sdk";

type JsonPrimitive = string | number | boolean | null;
type JsonValue = JsonPrimitive | { [key: string]: JsonValue } | JsonValue[];

export type FailureAnalysisRequest = {
  titleSlug: string;
  title: string;
  questionContent: string;
  editorContent: string;
  submissionContent: string;
  testcase: string;
  judgeResult: JsonValue;
  filetype: string;
};

export type FailureAnnotation = {
  line: number;
  reason: string;
  severity: "error" | "warn";
  column?: number;
};

export type FailureAnalysisResult = {
  summary: string;
  annotations: FailureAnnotation[];
};

const FAILURE_ANALYSIS_PROMPT = `
You are analyzing a failed LeetCode test run.

Explain the bug briefly in Chinese, then identify the most likely problematic lines in the user's editor buffer.
Use the absolute line numbers from the numbered editor buffer below.
Focus on the user's submission and the LeetCode error response. Do not rewrite the whole solution.
If the raw LeetCode error already suggests a location, preserve that signal in your analysis.

Return JSON only with this shape:
{
  "summary": "short Chinese explanation",
  "annotations": [
    {
      "line": 12,
      "reason": "short Chinese reason",
      "severity": "error"
    }
  ]
}

Rules:
- summary must be Chinese.
- reason must be concise and preferably Chinese.
- severity must be "error" or "warn".
- Keep at most 6 annotations.
- If you cannot infer a useful line, return an empty annotations array.
- Do not wrap the JSON in markdown fences.
`.trim();

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

const normalizeSeverity = (value: unknown): "error" | "warn" => {
  return value === "error" ? "error" : "warn";
};

const mergeAnnotations = (items: FailureAnnotation[]): FailureAnnotation[] => {
  const merged = new Map<number, FailureAnnotation>();

  for (const item of items) {
    const existing = merged.get(item.line);
    if (!existing) {
      merged.set(item.line, item);
      continue;
    }

    const reasons = [existing.reason, item.reason].map((value) => value.trim()).filter(Boolean);
    merged.set(item.line, {
      ...existing,
      severity: existing.severity === "error" || item.severity === "error" ? "error" : "warn",
      reason: Array.from(new Set(reasons)).join(" | "),
      column: existing.column ?? item.column,
    });
  }

  return Array.from(merged.values()).sort((left, right) => left.line - right.line);
};

const extractJsonObject = (content: string): string => {
  const trimmed = content.trim();
  if (trimmed.startsWith("{") && trimmed.endsWith("}")) {
    return trimmed;
  }

  const match = trimmed.match(/\{[\s\S]*\}/);
  return match?.[0] ?? trimmed;
};

export const parseFailureAnalysis = (content: string, maxLine: number): FailureAnalysisResult => {
  const parsed = JSON.parse(extractJsonObject(content)) as Partial<FailureAnalysisResult>;
  const rawAnnotations = Array.isArray(parsed.annotations) ? parsed.annotations : [];
  const annotations = rawAnnotations
    .map((item) => {
      if (!item || typeof item !== "object") {
        return null;
      }

      const line = Number((item as { line?: unknown }).line);
      if (!Number.isInteger(line) || line < 1 || line > maxLine) {
        return null;
      }

      const columnValue = Number((item as { column?: unknown }).column);
      return {
        line,
        reason: String((item as { reason?: unknown }).reason ?? "").trim() || "可能与失败结果相关",
        severity: normalizeSeverity((item as { severity?: unknown }).severity),
        column: Number.isInteger(columnValue) && columnValue > 0 ? columnValue : undefined,
      } as FailureAnnotation;
    })
    .filter((item): item is FailureAnnotation => item !== null)
    .slice(0, 6);

  return {
    summary: String(parsed.summary ?? "").trim(),
    annotations: mergeAnnotations(annotations),
  };
};

export class OpenRouterFailureAnalyzer {
  constructor(
    private readonly openRouter: OpenRouter,
    private readonly model: string,
  ) {}

  async analyze(request: FailureAnalysisRequest): Promise<FailureAnalysisResult> {
    const maxLine = Math.max(1, request.editorContent.split("\n").length);
    const response = await this.openRouter.chat.send({
      chatRequest: {
        model: this.model,
        temperature: 0.2,
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

    const text = response.choices?.[0]?.message?.content ?? "{}";
    return parseFailureAnalysis(text, maxLine);
  }
}
