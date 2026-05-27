import type { FailureAnalysisResult, FailureAnnotation } from "./failureAnalysis.js";

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
    .map<FailureAnnotation | null>((item) => {
      if (!item || typeof item !== "object") {
        return null;
      }

      const line = Number((item as { line?: unknown }).line);
      if (!Number.isInteger(line) || line < 1 || line > maxLine) {
        return null;
      }

      const columnValue = Number((item as { column?: unknown }).column);
      const rawReason = (item as { reason?: unknown }).reason;
      const reason = typeof rawReason === "string" ? rawReason.trim() : "";
      return {
        line,
        reason: reason || "Possibly related to the failing result",
        severity: normalizeSeverity((item as { severity?: unknown }).severity),
        column: Number.isInteger(columnValue) && columnValue > 0 ? columnValue : undefined,
      };
    })
    .filter((item): item is FailureAnnotation => item !== null)
    .slice(0, 6);

  return {
    summary: String(parsed.summary ?? "").trim(),
    annotations: mergeAnnotations(annotations),
  };
};
