import type { CandidateQuestion, CandidateSubmission } from "../core/types.ts";

const DESCRIPTION_MAX_CHARS = 1200;

const decodeHtmlEntities = (text: string): string => {
  const namedEntities: Record<string, string> = {
    nbsp: " ",
    amp: "&",
    lt: "<",
    gt: ">",
    quot: '"',
    apos: "'",
  };

  return text
    .replace(/&([a-z]+);/gi, (match, entityName: string) => namedEntities[entityName.toLowerCase()] ?? match)
    .replace(/&#(\d+);/g, (match, codePointRaw: string) => {
      const codePoint = Number.parseInt(codePointRaw, 10);
      return Number.isFinite(codePoint) ? String.fromCodePoint(codePoint) : match;
    })
    .replace(/&#x([\da-f]+);/gi, (match, codePointRaw: string) => {
      const codePoint = Number.parseInt(codePointRaw, 16);
      return Number.isFinite(codePoint) ? String.fromCodePoint(codePoint) : match;
    });
};

export const renderHtmlToText = (html: string): string => {
  const withStructure = html
    .replace(/<br\s*\/?>(\s*)/gi, "\n")
    .replace(/<\/p>/gi, "\n\n")
    .replace(/<p[^>]*>/gi, "")
    .replace(/<li[^>]*>/gi, "- ")
    .replace(/<\/li>/gi, "\n")
    .replace(/<\/?(?:ul|ol)[^>]*>/gi, "\n")
    .replace(/<pre[^>]*>/gi, "\n```text\n")
    .replace(/<\/pre>/gi, "\n```\n")
    .replace(/<code[^>]*>/gi, "`")
    .replace(/<\/code>/gi, "`")
    .replace(/<\/?(?:strong|b)[^>]*>/gi, "**")
    .replace(/<\/?(?:em|i)[^>]*>/gi, "*");

  const withoutTags = withStructure.replace(/<[^>]+>/g, "");
  const decoded = decodeHtmlEntities(withoutTags);

  return decoded
    .replace(/[ \t]+\n/g, "\n")
    .replace(/\n{3,}/g, "\n\n")
    .trim();
};

export const formatProblemDescription = (rawDescription: string, maxChars = DESCRIPTION_MAX_CHARS): string => {
  const cleaned = renderHtmlToText(rawDescription);
  if (cleaned.length <= maxChars) {
    return cleaned;
  }

  return `${cleaned.slice(0, maxChars)}\n\n...(truncated for readability)`;
};

export const buildPromptText = (question: CandidateQuestion, submission: CandidateSubmission): string => {
  const description = question.content
    ? formatProblemDescription(question.content)
    : `${question.title} (${question.difficulty})`;

  return [
    `Problem: ${question.title} [${question.titleSlug}]`,
    `Difficulty: ${question.difficulty}`,
    `Topics: ${(question.topicTags ?? []).join(", ") || "n/a"}`,
    "",
    "Problem description:",
    description,
    "",
    "Past submission:",
    `Submission ID: ${submission.id}`,
    `Status: ${submission.status}`,
    `SubmittedAt: ${submission.createdAt.toISOString()}`,
    "",
    "Reply in this channel with your interview-style approach.",
    "Explain your reasoning, expected time/space complexity, edge cases, and any blind spot you notice.",
    "You do not need to provide code. We are evaluating the quality and soundness of your thinking.",
  ].join("\n");
};
