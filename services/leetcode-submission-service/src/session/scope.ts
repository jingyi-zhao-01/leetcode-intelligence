import type { CompanionChatMessage } from "../core/companionChat.ts";
import type { FailureAnalysisRequest, FailureAnalysisResult } from "../core/failureAnalysis.ts";

export type CompanionSessionContext = {
  title?: string;
  titleSlug: string;
  difficulty?: string;
  lang?: string;
  description?: string;
  testcase?: string;
  code?: string;
};

export type ActiveSessionScope = {
  titleSlug: string;
  activatedAt: string;
  title?: string;
  difficulty?: string;
  lang?: string;
  questionContent?: string;
  editorContent?: string;
  submissionContent?: string;
  testcase?: string;
  filetype?: string;
  lastFailureAnalysis?: {
    analyzedAt: string;
    summary: string;
    annotations: FailureAnalysisResult["annotations"];
    judgeResult: FailureAnalysisRequest["judgeResult"];
  };
};

const lineValue = (content: string, label: string): string => {
  const match = content.match(new RegExp(`^- ${label}:\\s*(.+)$`, "m"));
  return match?.[1]?.trim() ?? "";
};

const markdownSection = (content: string, heading: string): string => {
  const match = content.match(new RegExp(`## ${heading}\\n([\\s\\S]*?)(?:\\n## |$)`));
  return match?.[1]?.trim() ?? "";
};

const stripCodeFence = (content: string): string => {
  const fenced = content.match(/^```[^\n]*\n([\s\S]*?)\n```$/);
  return fenced?.[1]?.trim() ?? content.trim();
};

export function extractCompanionSessionContext(messages: CompanionChatMessage[]): CompanionSessionContext | null {
  for (const message of messages) {
    if (!message.content.includes("# LeetCode Problem Context")) {
      continue;
    }

    const titleSlug = lineValue(message.content, "Title Slug");
    if (!titleSlug) {
      continue;
    }

    return {
      title: lineValue(message.content, "Title") || undefined,
      titleSlug,
      difficulty: lineValue(message.content, "Difficulty") || undefined,
      lang: lineValue(message.content, "Language") || undefined,
      description: markdownSection(message.content, "Problem Description") || undefined,
      testcase: stripCodeFence(markdownSection(message.content, "Active Testcase")) || undefined,
      code: stripCodeFence(markdownSection(message.content, "Current Code")) || undefined,
    };
  }

  return null;
}

export function renderActiveSessionScope(scope: ActiveSessionScope): string {
  const parts = [
    "# Submission Service Active Session",
    "",
    `- Title Slug: ${scope.titleSlug}`,
  ];

  if (scope.title) {
    parts.push(`- Title: ${scope.title}`);
  }

  if (scope.difficulty) {
    parts.push(`- Difficulty: ${scope.difficulty}`);
  }

  if (scope.lang) {
    parts.push(`- Language: ${scope.lang}`);
  }

  if (scope.questionContent) {
    parts.push("", "## Problem Description", scope.questionContent);
  }

  if (scope.testcase) {
    parts.push("", "## Active Testcase", "```text", scope.testcase, "```");
  }

  if (scope.editorContent) {
    parts.push("", "## Current Code", `\`\`\`${scope.filetype ?? scope.lang ?? "text"}`, scope.editorContent, "```");
  }

  if (scope.lastFailureAnalysis) {
    parts.push("", "## Latest Failure Analysis", `- Summary: ${scope.lastFailureAnalysis.summary}`);

    if (scope.lastFailureAnalysis.annotations.length > 0) {
      parts.push("- Annotations:");
      for (const annotation of scope.lastFailureAnalysis.annotations) {
        parts.push(`  - line ${annotation.line} [${annotation.severity}]: ${annotation.reason}`);
      }
    }
  }

  return parts.join("\n");
}

export class ActiveSessionScopeManager {
  private readonly scopes = new Map<string, ActiveSessionScope>();
  private activeTitleSlug: string | null = null;

  activate(titleSlug: string, evictedTitleSlugs: string[] = []): ActiveSessionScope {
    for (const evictedTitleSlug of evictedTitleSlugs) {
      this.scopes.delete(evictedTitleSlug);
      if (this.activeTitleSlug === evictedTitleSlug) {
        this.activeTitleSlug = null;
      }
    }

    const next =
      this.scopes.get(titleSlug) ??
      ({
        titleSlug,
        activatedAt: new Date().toISOString(),
      } satisfies ActiveSessionScope);

    if (!this.scopes.has(titleSlug)) {
      this.scopes.set(titleSlug, next);
    }

    this.activeTitleSlug = titleSlug;
    return next;
  }

  clear(titleSlug: string): void {
    this.scopes.delete(titleSlug);
    if (this.activeTitleSlug === titleSlug) {
      this.activeTitleSlug = null;
    }
  }

  getActiveScope(): ActiveSessionScope | null {
    if (!this.activeTitleSlug) {
      return null;
    }

    return this.scopes.get(this.activeTitleSlug) ?? null;
  }

  recordCompanionContext(context: CompanionSessionContext): ActiveSessionScope {
    const scope = this.activate(context.titleSlug);
    scope.title = context.title ?? scope.title;
    scope.difficulty = context.difficulty ?? scope.difficulty;
    scope.lang = context.lang ?? scope.lang;
    scope.questionContent = context.description ?? scope.questionContent;
    scope.editorContent = context.code ?? scope.editorContent;
    scope.testcase = context.testcase ?? scope.testcase;
    return scope;
  }

  recordFailureAnalysis(request: FailureAnalysisRequest, result: FailureAnalysisResult): ActiveSessionScope {
    const scope = this.activate(request.titleSlug);
    scope.title = request.title || scope.title;
    scope.questionContent = request.questionContent || scope.questionContent;
    scope.editorContent = request.editorContent || scope.editorContent;
    scope.submissionContent = request.submissionContent || scope.submissionContent;
    scope.testcase = request.testcase || scope.testcase;
    scope.filetype = request.filetype || scope.filetype;
    scope.lastFailureAnalysis = {
      analyzedAt: new Date().toISOString(),
      summary: result.summary,
      annotations: result.annotations,
      judgeResult: request.judgeResult,
    };
    return scope;
  }

  buildCompanionMessages(messages: CompanionChatMessage[]): CompanionChatMessage[] {
    const scope = this.getActiveScope();
    if (!scope) {
      return messages;
    }

    return [
      {
        role: "user",
        content: renderActiveSessionScope(scope),
      },
      ...messages,
    ];
  }
}
