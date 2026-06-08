import type { ActiveSessionScope } from '../scope.ts';
import {
  MAX_COMPANION_TURNS,
  MAX_MOUNT_SUMMARY_CHARS,
  MAX_MOUNT_SUMMARY_RECORDS,
  MAX_RECALLED_ANALYSIS_CHARS,
  MAX_RECALLED_CODE_CHARS,
  MAX_RECALLED_FAILURE_CHARS,
  MAX_RECALLED_SESSION_RECORDS,
  MAX_SERVICE_UPDATES,
  MAX_MESSAGE_CHARS,
  MAX_TEXT_SECTION_CHARS,
} from './constants.ts';
import {
  extractBulletValues,
  hasMarkdownSection,
  pushCodeSection,
  pushMessagesSection,
  readJudgeStatus,
  readMarkdownSection,
  readMetadataNumber,
  readMetadataString,
  readStringValue,
  stripCodeFence,
  truncate,
  truncateJson,
} from './shared.ts';
import type {
  RecalledMountSessionSummary,
  RecalledSessionRecord,
  SessionEndEvent,
  SessionRecordRecallResult,
} from './types.ts';

export function buildMem0RunId(scope: ActiveSessionScope): string {
  return `leetcode-session:${scope.titleSlug}:${scope.activatedAt}`;
}

export function countSessionInteractions(scope: ActiveSessionScope): number {
  const companionCount = scope.companionMemory?.messages.length ?? 0;
  const serviceCount = scope.sessionMemory?.messages.length ?? 0;
  return companionCount + serviceCount;
}

export function buildPersistedSessionRecordMetadata(
  scope: ActiveSessionScope,
  event: SessionEndEvent,
): Record<string, unknown> {
  const interactionCount = countSessionInteractions(scope);
  const latestFailureStatus = readJudgeStatus(scope.latestFailure?.judgeResult);

  return {
    source: 'leetcode-submission-service',
    recordType: 'leetcode_session_record',
    titleSlug: scope.titleSlug,
    endReason: event.reason,
    activatedAt: scope.activatedAt,
    endedAt: event.endedAt,
    elapsedMinutes: event.elapsedMinutes ?? null,
    interactionCount,
    latestFailureStatus,
    replacedByTitleSlug: event.replacedByTitleSlug ?? null,
    record_type: 'leetcode_session_record',
    title_slug: scope.titleSlug,
    end_reason: event.reason,
    activated_at: scope.activatedAt,
    ended_at: event.endedAt,
    elapsed_minutes: event.elapsedMinutes ?? null,
    difficulty: scope.difficulty ?? null,
    language: scope.lang ?? null,
    interaction_count: interactionCount,
    latest_failure_status: latestFailureStatus,
    replaced_by_title_slug: event.replacedByTitleSlug ?? null,
  };
}

export function renderPersistedSessionRecord(scope: ActiveSessionScope, event: SessionEndEvent): string {
  const parts = [
    '# LeetCode Session Record',
    '',
    `- Title Slug: ${scope.titleSlug}`,
    `- Run ID: ${buildMem0RunId(scope)}`,
    `- Activated At: ${scope.activatedAt}`,
    `- Ended At: ${event.endedAt}`,
    `- End Reason: ${event.reason}`,
  ];

  if (typeof event.elapsedMinutes === 'number' && Number.isFinite(event.elapsedMinutes)) {
    parts.push(`- Elapsed Minutes: ${event.elapsedMinutes}`);
  }

  if (event.replacedByTitleSlug) {
    parts.push(`- Replaced By Title Slug: ${event.replacedByTitleSlug}`);
  }

  if (scope.title) {
    parts.push(`- Title: ${scope.title}`);
  }

  if (scope.difficulty) {
    parts.push(`- Difficulty: ${scope.difficulty}`);
  }

  if (scope.lang) {
    parts.push(`- Language: ${scope.lang}`);
  }

  if (scope.testcase?.trim()) {
    parts.push('', '## Active Testcase', '```text', truncate(scope.testcase, MAX_TEXT_SECTION_CHARS), '```');
  }

  pushCodeSection(parts, 'Final Editor Code', scope.editorContent, scope.filetype ?? scope.lang ?? 'text');

  if (scope.submissionContent?.trim() && scope.submissionContent.trim() !== scope.editorContent?.trim()) {
    pushCodeSection(parts, 'Last Submitted Code', scope.submissionContent, scope.filetype ?? scope.lang ?? 'text');
  }

  if (scope.latestFailure) {
    parts.push('', '## Latest LeetCode Failure', `- Event ID: ${scope.latestFailure.eventId}`);

    const status = readJudgeStatus(scope.latestFailure.judgeResult);
    if (status) {
      parts.push(`- Judge Status: ${status}`);
    }

    if (scope.latestFailure.testcase?.trim()) {
      parts.push(
        '',
        '### Failed Testcase',
        '```text',
        truncate(scope.latestFailure.testcase, MAX_TEXT_SECTION_CHARS),
        '```',
      );
    }

    parts.push('', '### Raw Judge Result', '```json', truncateJson(scope.latestFailure.judgeResult), '```');
  }

  if (scope.lastFailureAnalysis) {
    parts.push('', '## Latest Failure Analysis', `- Summary: ${truncate(scope.lastFailureAnalysis.summary, MAX_MESSAGE_CHARS)}`);

    if (scope.lastFailureAnalysis.annotations.length > 0) {
      parts.push('- Annotations:');
      for (const annotation of scope.lastFailureAnalysis.annotations) {
        parts.push(`  - line ${annotation.line} [${annotation.severity}]: ${truncate(annotation.reason, 240)}`);
      }
    }
  }

  pushMessagesSection(parts, 'Service Session Memory', scope.sessionMemory?.messages, MAX_SERVICE_UPDATES);
  pushMessagesSection(parts, 'Companion Conversation', scope.companionMemory?.messages, MAX_COMPANION_TURNS);

  return parts.join('\n');
}

export function buildSyntheticRecalledSessionRecord(
  scope: ActiveSessionScope,
  event: SessionEndEvent,
): RecalledSessionRecord {
  const runId = buildMem0RunId(scope);

  return {
    id: `local:${runId}:${event.reason}:${event.endedAt}`,
    memory: renderPersistedSessionRecord(scope, event),
    createdAt: event.endedAt,
    updatedAt: event.endedAt,
    metadata: buildPersistedSessionRecordMetadata(scope, event),
  };
}

export function renderRecalledSessionRecords(result: SessionRecordRecallResult) {
  const records = [...result.records].sort((left, right) =>
    (left.createdAt ?? left.updatedAt ?? '').localeCompare(right.createdAt ?? right.updatedAt ?? ''),
  );
  const visibleRecords = records.slice(-MAX_RECALLED_SESSION_RECORDS);
  const omittedCount = records.length - visibleRecords.length;
  const parts = [
    '# Submission Service Mem0 Recall',
    '',
    `- Title Slug: ${result.titleSlug}`,
    `- Recalled Session Count: ${records.length}`,
    '- These are historical session records recalled from Mem0 for this exact LeetCode problem.',
    '- Records may include ended-session snapshots and failure-analysis-triggered snapshots.',
    '- Treat these as historical summaries only; do not assume omitted code or truncated snapshots are ground truth.',
  ];

  if (omittedCount > 0) {
    parts.push(`- Omitted Older Session Count: ${omittedCount}`);
  }

  visibleRecords.forEach((record, index) => {
    const metadata = record.metadata ?? {};
    const activatedAt = readMetadataString(metadata, 'activated_at', 'activatedAt');
    const endedAt = readMetadataString(metadata, 'ended_at', 'endedAt');
    const endReason = readMetadataString(metadata, 'end_reason', 'endReason');
    const language = readMetadataString(metadata, 'language');
    const difficulty = readMetadataString(metadata, 'difficulty');
    const latestFailureStatus = readMetadataString(metadata, 'latest_failure_status', 'latestFailureStatus');
    const elapsedMinutes = readMetadataNumber(metadata, 'elapsed_minutes', 'elapsedMinutes');
    const hasEditorCode = hasMarkdownSection(record.memory, 'Final Editor Code');
    const hasSubmittedCode = hasMarkdownSection(record.memory, 'Last Submitted Code');
    const hasFailureSnapshot = hasMarkdownSection(record.memory, 'Latest LeetCode Failure');
    const hasFailureAnalysis = hasMarkdownSection(record.memory, 'Latest Failure Analysis');
    const hasCompanionConversation = hasMarkdownSection(record.memory, 'Companion Conversation');
    const submittedCode = readMarkdownSection(record.memory, 'Last Submitted Code');
    const editorCode = readMarkdownSection(record.memory, 'Final Editor Code');
    const failureSnapshot = readMarkdownSection(record.memory, 'Latest LeetCode Failure');
    const failureAnalysis = readMarkdownSection(record.memory, 'Latest Failure Analysis');

    parts.push('', `## Session ${index + 1}`);

    if (activatedAt) {
      parts.push(`- Activated At: ${activatedAt}`);
    }
    if (endedAt) {
      parts.push(`- Ended At: ${endedAt}`);
    }
    if (endReason) {
      parts.push(`- End Reason: ${endReason}`);
    }
    if (typeof elapsedMinutes === 'number' && Number.isFinite(elapsedMinutes)) {
      parts.push(`- Elapsed Minutes: ${elapsedMinutes}`);
    }
    if (difficulty) {
      parts.push(`- Difficulty: ${difficulty}`);
    }
    if (language) {
      parts.push(`- Language: ${language}`);
    }
    if (latestFailureStatus) {
      parts.push(`- Latest Failure Status: ${latestFailureStatus}`);
    }

    const observed: string[] = [];
    if (hasEditorCode) {
      observed.push('editor_code');
    }
    if (hasSubmittedCode) {
      observed.push('submitted_code');
    }
    if (hasFailureSnapshot) {
      observed.push('failure_snapshot');
    }
    if (hasFailureAnalysis) {
      observed.push('failure_analysis');
    }
    if (hasCompanionConversation) {
      observed.push('companion_conversation');
    }
    parts.push(`- Observed Artifacts: ${observed.length > 0 ? observed.join(', ') : 'metadata_only'}`);

    const preferredCode = submittedCode ?? editorCode;
    if (preferredCode) {
      parts.push('', '### Recalled Code Excerpt', '```text', truncate(stripCodeFence(preferredCode), MAX_RECALLED_CODE_CHARS), '```');
    }

    if (failureSnapshot) {
      parts.push('', '### Recalled Failure Snapshot', truncate(failureSnapshot, MAX_RECALLED_FAILURE_CHARS));
    }
    if (failureAnalysis) {
      parts.push('', '### Recalled Failure Analysis', truncate(failureAnalysis, MAX_RECALLED_ANALYSIS_CHARS));
    }
  });

  return {
    role: 'user' as const,
    content: parts.join('\n'),
  };
}

export function summarizeRecalledSessionsForMount(result: SessionRecordRecallResult): RecalledMountSessionSummary[] {
  const records = [...result.records].sort((left, right) =>
    (right.createdAt ?? right.updatedAt ?? '').localeCompare(left.createdAt ?? left.updatedAt ?? ''),
  );

  return records.slice(0, MAX_MOUNT_SUMMARY_RECORDS).map((record) => {
    const metadata = record.metadata ?? {};
    const endedAt = readMetadataString(metadata, 'ended_at', 'endedAt');
    const endReason = readMetadataString(metadata, 'end_reason', 'endReason');
    const latestFailureStatus = readMetadataString(metadata, 'latest_failure_status', 'latestFailureStatus');
    const failureAnalysis = readMarkdownSection(record.memory, 'Latest Failure Analysis') ?? '';
    const companionConversation = readMarkdownSection(record.memory, 'Companion Conversation') ?? '';
    const failureSummaryMatch = failureAnalysis.match(/^- Summary:\s*(.+)$/m);

    return {
      endedAt,
      endReason,
      latestFailureStatus,
      failureSummary: readStringValue(failureSummaryMatch?.[1]),
      stuckPoints: extractBulletValues(failureAnalysis, /^\s*-\s*line\s+\d+\s+\[[^\]]+\]:\s*(.+)$/gm).slice(0, 3),
      thoughtProcess: extractBulletValues(companionConversation, /^- user:\s*(.+)$/gm).slice(-3),
    };
  });
}

export function renderRecalledMountSummary(result: SessionRecordRecallResult): string | undefined {
  const sessions = summarizeRecalledSessionsForMount(result);
  if (sessions.length === 0) {
    return undefined;
  }

  const parts = [
    `You have historical LeetCode memory for \`${result.titleSlug}\`.`,
    `Recent recalled sessions: ${result.records.length}.`,
  ];

  sessions.forEach((session, index) => {
    parts.push('', `Session ${index + 1}:`);
    if (session.endReason) {
      parts.push(`- End reason: ${session.endReason}`);
    }
    if (session.latestFailureStatus) {
      parts.push(`- Failure status: ${session.latestFailureStatus}`);
    }
    if (session.failureSummary) {
      parts.push(`- Failure reason: ${session.failureSummary}`);
    }
    if (session.stuckPoints.length > 0) {
      parts.push(`- Stuck points: ${session.stuckPoints.join(' | ')}`);
    }
    if (session.thoughtProcess.length > 0) {
      parts.push(`- Thought process: ${session.thoughtProcess.join(' | ')}`);
    }
  });

  return truncate(parts.join('\n'), MAX_MOUNT_SUMMARY_CHARS);
}
