import type { CompanionChatMessage } from '../core/companionChat.ts';
import type { FailureAnalysisRequest, FailureAnalysisResult } from '../core/failureAnalysis.ts';
import type { RecalledMountSessionSummary } from './mem0.ts';

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
  companionMemory?: {
    updatedAt: string;
    messages: CompanionChatMessage[];
  };
  mem0Recall?: {
    hydratedAt: string;
    recordCount: number;
    message?: CompanionChatMessage;
    mountSummary?: string;
    mountSessions?: RecalledMountSessionSummary[];
  };
  sessionMemory?: {
    updatedAt: string;
    messages: CompanionChatMessage[];
  };
  latestFailure?: {
    eventId: string;
    recordedAt: string;
    judgeResult: FailureAnalysisRequest['judgeResult'];
    submissionContent?: string;
    testcase?: string;
  };
  lastFailureAnalysis?: {
    analyzedAt: string;
    summary: string;
    annotations: FailureAnalysisResult['annotations'];
    judgeResult: FailureAnalysisRequest['judgeResult'];
  };
};

const SESSION_MEMORY_LIMIT = 24;
const SERVICE_MEMORY_LIMIT = 8;

const lineValue = (content: string, label: string): string => {
  const match = content.match(new RegExp(`^- ${label}:\\s*(.+)$`, 'm'));
  return match?.[1]?.trim() ?? '';
};

const markdownSection = (content: string, heading: string): string => {
  const match = content.match(new RegExp(`## ${heading}\\n([\\s\\S]*?)(?:\\n## |$)`));
  return match?.[1]?.trim() ?? '';
};

const stripCodeFence = (content: string): string => {
  const fenced = content.match(/^```[^\n]*\n([\s\S]*?)\n```$/);
  return fenced?.[1]?.trim() ?? content.trim();
};

export function extractCompanionSessionContext(messages: CompanionChatMessage[]): CompanionSessionContext | null {
  for (const message of messages) {
    if (!message.content.includes('# LeetCode Problem Context')) {
      continue;
    }

    const titleSlug = lineValue(message.content, 'Title Slug');
    if (!titleSlug) {
      continue;
    }

    return {
      title: lineValue(message.content, 'Title') || undefined,
      titleSlug,
      difficulty: lineValue(message.content, 'Difficulty') || undefined,
      lang: lineValue(message.content, 'Language') || undefined,
      description: markdownSection(message.content, 'Problem Description') || undefined,
      testcase: stripCodeFence(markdownSection(message.content, 'Active Testcase')) || undefined,
      code: stripCodeFence(markdownSection(message.content, 'Current Code')) || undefined,
    };
  }

  return null;
}

export function renderActiveSessionScope(scope: ActiveSessionScope): string {
  const parts = ['# Submission Service Active Session', '', `- Title Slug: ${scope.titleSlug}`];

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
    parts.push('', '## Problem Description', scope.questionContent);
  }

  if (scope.testcase) {
    parts.push('', '## Active Testcase', '```text', scope.testcase, '```');
  }

  if (scope.editorContent) {
    parts.push('', '## Current Code', `\`\`\`${scope.filetype ?? scope.lang ?? 'text'}`, scope.editorContent, '```');
  }

  if (scope.latestFailure) {
    parts.push('', '## Latest LeetCode Failure');
    parts.push(`- Event ID: ${scope.latestFailure.eventId}`);

    const status =
      scope.latestFailure.judgeResult &&
      typeof scope.latestFailure.judgeResult === 'object' &&
      'status_msg' in scope.latestFailure.judgeResult &&
      typeof scope.latestFailure.judgeResult.status_msg === 'string'
        ? scope.latestFailure.judgeResult.status_msg
        : '';

    if (status) {
      parts.push(`- Judge Status: ${status}`);
    }

    parts.push('```json');
    parts.push(JSON.stringify(scope.latestFailure.judgeResult, null, 2));
    parts.push('```');
  }

  if (scope.lastFailureAnalysis) {
    parts.push('', '## Latest Failure Analysis', `- Summary: ${scope.lastFailureAnalysis.summary}`);

    if (scope.lastFailureAnalysis.annotations.length > 0) {
      parts.push('- Annotations:');
      for (const annotation of scope.lastFailureAnalysis.annotations) {
        parts.push(`  - line ${annotation.line} [${annotation.severity}]: ${annotation.reason}`);
      }
    }
  }

  return parts.join('\n');
}

function isHiddenCompanionContext(message: CompanionChatMessage): boolean {
  return (
    message.content.includes('# LeetCode Problem Context') ||
    message.content.includes('# Submission Service Active Session')
  );
}

function isMem0RecallMessage(message: CompanionChatMessage): boolean {
  return message.content.includes('# Submission Service Mem0 Recall');
}

function normalizeConversationMemory(messages: CompanionChatMessage[]): CompanionChatMessage[] {
  const visibleMessages = messages.filter((message) => !isHiddenCompanionContext(message) && message.role !== 'system');
  if (visibleMessages.length <= SESSION_MEMORY_LIMIT) {
    return visibleMessages;
  }

  return visibleMessages.slice(visibleMessages.length - SESSION_MEMORY_LIMIT);
}

function normalizeServiceMemory(messages: CompanionChatMessage[]): CompanionChatMessage[] {
  if (messages.length <= SERVICE_MEMORY_LIMIT) {
    return messages;
  }

  return messages.slice(messages.length - SERVICE_MEMORY_LIMIT);
}

function buildFailureMemoryMessage(
  eventId: string,
  request: FailureAnalysisRequest,
  result: FailureAnalysisResult,
): CompanionChatMessage {
  const parts = [
    '# Submission Service Failure Update',
    '',
    `- Event ID: ${eventId}`,
    `- Title Slug: ${request.titleSlug}`,
    '- This update supersedes any earlier companion diagnosis for the current failed run.',
  ];

  const status =
    request.judgeResult &&
    typeof request.judgeResult === 'object' &&
    'status_msg' in request.judgeResult &&
    typeof request.judgeResult.status_msg === 'string'
      ? request.judgeResult.status_msg
      : '';

  if (status) {
    parts.push(`- Judge Status: ${status}`);
  }

  if (request.testcase.trim().length > 0) {
    parts.push('', '## Failed Testcase', '```text', request.testcase.trim(), '```');
  }

  parts.push('', '## Static Analysis Summary', result.summary);

  if (result.annotations.length > 0) {
    parts.push('', '## Static Analysis Annotations');
    for (const annotation of result.annotations) {
      parts.push(`- line ${annotation.line} [${annotation.severity}]: ${annotation.reason}`);
    }
  }

  parts.push('', '## Raw Judge Result', '```json', JSON.stringify(request.judgeResult, null, 2), '```');

  return {
    role: 'user',
    content: parts.join('\n'),
  };
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
    this.take(titleSlug);
  }

  take(titleSlug: string): ActiveSessionScope | null {
    const scope = this.scopes.get(titleSlug) ?? null;
    this.scopes.delete(titleSlug);
    if (this.activeTitleSlug === titleSlug) {
      this.activeTitleSlug = null;
    }
    return scope;
  }

  getActiveScope(): ActiveSessionScope | null {
    if (!this.activeTitleSlug) {
      return null;
    }

    return this.scopes.get(this.activeTitleSlug) ?? null;
  }

  getScope(titleSlug: string): ActiveSessionScope | null {
    return this.scopes.get(titleSlug) ?? null;
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

  recordCompanionMessages(titleSlug: string, messages: CompanionChatMessage[]): ActiveSessionScope {
    const scope = this.activate(titleSlug);
    scope.companionMemory = {
      updatedAt: new Date().toISOString(),
      messages: normalizeConversationMemory(messages),
    };
    return scope;
  }

  appendCompanionReply(titleSlug: string, content: string): ActiveSessionScope {
    const scope = this.activate(titleSlug);
    const existingMessages = scope.companionMemory?.messages ?? [];
    scope.companionMemory = {
      updatedAt: new Date().toISOString(),
      messages: normalizeConversationMemory([
        ...existingMessages,
        {
          role: 'assistant',
          content,
        },
      ]),
    };
    return scope;
  }

  recordSessionMemory(titleSlug: string, message: CompanionChatMessage): ActiveSessionScope {
    const scope = this.activate(titleSlug);
    const existingMessages = scope.sessionMemory?.messages ?? [];
    scope.sessionMemory = {
      updatedAt: new Date().toISOString(),
      messages: normalizeServiceMemory([...existingMessages, message]),
    };
    return scope;
  }

  hasMem0Recall(titleSlug: string): boolean {
    return !!this.scopes.get(titleSlug)?.mem0Recall;
  }

  recordMem0Recall(
    titleSlug: string,
    recordCount: number,
    message?: CompanionChatMessage,
    mountSummary?: string,
    mountSessions?: RecalledMountSessionSummary[],
  ): ActiveSessionScope {
    const scope = this.activate(titleSlug);
    scope.mem0Recall = {
      hydratedAt: new Date().toISOString(),
      recordCount,
      message,
      mountSummary,
      mountSessions,
    };

    if (!message) {
      return scope;
    }

    const existingMessages = (scope.sessionMemory?.messages ?? []).filter((entry) => !isMem0RecallMessage(entry));
    scope.sessionMemory = {
      updatedAt: new Date().toISOString(),
      messages: normalizeServiceMemory(existingMessages),
    };
    return scope;
  }

  recordFailureAnalysis(
    request: FailureAnalysisRequest,
    result: FailureAnalysisResult,
    eventId: string,
  ): ActiveSessionScope {
    const scope = this.activate(request.titleSlug);
    scope.title = request.title || scope.title;
    scope.questionContent = request.questionContent || scope.questionContent;
    scope.editorContent = request.editorContent || scope.editorContent;
    scope.submissionContent = request.submissionContent || scope.submissionContent;
    scope.testcase = request.testcase || scope.testcase;
    scope.filetype = request.filetype || scope.filetype;
    scope.latestFailure = {
      eventId,
      recordedAt: new Date().toISOString(),
      judgeResult: request.judgeResult,
      submissionContent: request.submissionContent || scope.submissionContent,
      testcase: request.testcase || scope.testcase,
    };
    scope.lastFailureAnalysis = {
      analyzedAt: new Date().toISOString(),
      summary: result.summary,
      annotations: result.annotations,
      judgeResult: request.judgeResult,
    };
    this.recordSessionMemory(request.titleSlug, buildFailureMemoryMessage(eventId, request, result));
    return scope;
  }

  buildCompanionMessages(messages: CompanionChatMessage[]): CompanionChatMessage[] {
    const scope = this.getActiveScope();
    if (!scope) {
      return messages;
    }

    const visibleMessages = normalizeConversationMemory(messages);
    if (visibleMessages.length > 0) {
      this.recordCompanionMessages(scope.titleSlug, visibleMessages);
    }

    const refreshedScope = this.getActiveScope();
    if (!refreshedScope) {
      return messages;
    }

    return [
      {
        role: 'user',
        content: renderActiveSessionScope(refreshedScope),
      },
      ...(refreshedScope.mem0Recall?.message ? [refreshedScope.mem0Recall.message] : []),
      ...(refreshedScope.sessionMemory?.messages ?? []),
      ...(refreshedScope.companionMemory?.messages ?? []),
    ];
  }
}
