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

type NormalizedRecalledSession = {
  id: string;
  sourceRecordIds: string[];
  rawRecordCount: number;
  runId?: string;
  activatedAt?: string;
  endedAt?: string;
  endReason?: string;
  difficulty?: string;
  language?: string;
  latestFailureStatus?: string;
  elapsedMinutes?: number;
  observedArtifacts: string[];
  codeExcerpt?: string;
  failureSnapshot?: string;
  failureAnalysis?: string;
  failureSummary?: string;
  failureSummaries: string[];
  stuckPoints: string[];
  thoughtProcess: string[];
  sortTimestamp: string;
};

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
  const runId = buildMem0RunId(scope);

  return {
    source: 'leetcode-submission-service',
    recordType: 'leetcode_session_record',
    titleSlug: scope.titleSlug,
    runId,
    endReason: event.reason,
    activatedAt: scope.activatedAt,
    endedAt: event.endedAt,
    elapsedMinutes: event.elapsedMinutes ?? null,
    interactionCount,
    latestFailureStatus,
    replacedByTitleSlug: event.replacedByTitleSlug ?? null,
    record_type: 'leetcode_session_record',
    title_slug: scope.titleSlug,
    run_id: runId,
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

function readRecordLineValue(content: string, label: string): string | undefined {
  const escapedLabel = label.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const match = content.match(new RegExp(`^- ${escapedLabel}:\\s*(.+)$`, 'm'));
  return readStringValue(match?.[1]);
}

function uniqueValues(values: Array<string | undefined>, limit?: number): string[] {
  const seen = new Set<string>();
  const collected: string[] = [];

  for (const value of values) {
    const normalized = readStringValue(value);
    if (!normalized || seen.has(normalized)) {
      continue;
    }

    seen.add(normalized);
    collected.push(normalized);
    if (typeof limit === 'number' && collected.length >= limit) {
      break;
    }
  }

  return collected;
}

function parseRecalledSessionRecord(record: RecalledSessionRecord): NormalizedRecalledSession {
  const metadata = record.metadata ?? {};
  const activatedAt =
    readMetadataString(metadata, 'activated_at', 'activatedAt') ?? readRecordLineValue(record.memory, 'Activated At');
  const endedAt = readMetadataString(metadata, 'ended_at', 'endedAt') ?? readRecordLineValue(record.memory, 'Ended At');
  const endReason = readMetadataString(metadata, 'end_reason', 'endReason') ?? readRecordLineValue(record.memory, 'End Reason');
  const runId = readMetadataString(metadata, 'run_id', 'runId') ?? readRecordLineValue(record.memory, 'Run ID');
  const language = readMetadataString(metadata, 'language') ?? readRecordLineValue(record.memory, 'Language');
  const difficulty = readMetadataString(metadata, 'difficulty') ?? readRecordLineValue(record.memory, 'Difficulty');
  const latestFailureStatus =
    readMetadataString(metadata, 'latest_failure_status', 'latestFailureStatus') ??
    readRecordLineValue(record.memory, 'Judge Status');
  const elapsedMinutes =
    readMetadataNumber(metadata, 'elapsed_minutes', 'elapsedMinutes') ??
    Number(readRecordLineValue(record.memory, 'Elapsed Minutes') ?? NaN);
  const hasEditorCode = hasMarkdownSection(record.memory, 'Final Editor Code');
  const hasSubmittedCode = hasMarkdownSection(record.memory, 'Last Submitted Code');
  const hasFailureSnapshot = hasMarkdownSection(record.memory, 'Latest LeetCode Failure');
  const hasFailureAnalysis = hasMarkdownSection(record.memory, 'Latest Failure Analysis');
  const hasCompanionConversation = hasMarkdownSection(record.memory, 'Companion Conversation');
  const submittedCode = readMarkdownSection(record.memory, 'Last Submitted Code');
  const editorCode = readMarkdownSection(record.memory, 'Final Editor Code');
  const failureSnapshot = readMarkdownSection(record.memory, 'Latest LeetCode Failure');
  const failureAnalysis = readMarkdownSection(record.memory, 'Latest Failure Analysis');
  const companionConversation = readMarkdownSection(record.memory, 'Companion Conversation') ?? '';
  const failureSummaryMatch = failureAnalysis?.match(/^- Summary:\s*(.+)$/m);

  const observedArtifacts: string[] = [];
  if (hasEditorCode) {
    observedArtifacts.push('editor_code');
  }
  if (hasSubmittedCode) {
    observedArtifacts.push('submitted_code');
  }
  if (hasFailureSnapshot) {
    observedArtifacts.push('failure_snapshot');
  }
  if (hasFailureAnalysis) {
    observedArtifacts.push('failure_analysis');
  }
  if (hasCompanionConversation) {
    observedArtifacts.push('companion_conversation');
  }

  return {
    id: record.id,
    sourceRecordIds: [record.id],
    rawRecordCount: 1,
    runId,
    activatedAt,
    endedAt,
    endReason,
    difficulty,
    language,
    latestFailureStatus,
    elapsedMinutes: Number.isFinite(elapsedMinutes) ? elapsedMinutes : undefined,
    observedArtifacts,
    codeExcerpt: submittedCode ? stripCodeFence(submittedCode) : editorCode ? stripCodeFence(editorCode) : undefined,
    failureSnapshot,
    failureAnalysis,
    failureSummary: readStringValue(failureSummaryMatch?.[1]),
    failureSummaries: uniqueValues([readStringValue(failureSummaryMatch?.[1])]),
    stuckPoints: extractBulletValues(failureAnalysis ?? '', /^\s*-\s*line\s+\d+\s+\[[^\]]+\]:\s*(.+)$/gm),
    thoughtProcess: extractBulletValues(companionConversation, /^- user:\s*(.+)$/gm),
    sortTimestamp: endedAt ?? record.createdAt ?? record.updatedAt ?? activatedAt ?? '',
  };
}

function mergeRecalledSessions(primary: NormalizedRecalledSession, secondary: NormalizedRecalledSession): NormalizedRecalledSession {
  return {
    id: primary.id,
    sourceRecordIds: uniqueValues([...primary.sourceRecordIds, ...secondary.sourceRecordIds]),
    rawRecordCount: primary.rawRecordCount + secondary.rawRecordCount,
    runId: primary.runId ?? secondary.runId,
    activatedAt: primary.activatedAt ?? secondary.activatedAt,
    endedAt: primary.endedAt ?? secondary.endedAt,
    endReason: primary.endReason ?? secondary.endReason,
    difficulty: primary.difficulty ?? secondary.difficulty,
    language: primary.language ?? secondary.language,
    latestFailureStatus: primary.latestFailureStatus ?? secondary.latestFailureStatus,
    elapsedMinutes: primary.elapsedMinutes ?? secondary.elapsedMinutes,
    observedArtifacts: uniqueValues([...primary.observedArtifacts, ...secondary.observedArtifacts]),
    codeExcerpt: primary.codeExcerpt ?? secondary.codeExcerpt,
    failureSnapshot: primary.failureSnapshot ?? secondary.failureSnapshot,
    failureAnalysis: primary.failureAnalysis ?? secondary.failureAnalysis,
    failureSummary: primary.failureSummary ?? secondary.failureSummary,
    failureSummaries: uniqueValues([...primary.failureSummaries, ...secondary.failureSummaries], 6),
    stuckPoints: uniqueValues([...primary.stuckPoints, ...secondary.stuckPoints], 6),
    thoughtProcess: uniqueValues([...primary.thoughtProcess, ...secondary.thoughtProcess], 6),
    sortTimestamp: primary.sortTimestamp || secondary.sortTimestamp,
  };
}

function normalizeRecalledSessions(result: SessionRecordRecallResult): NormalizedRecalledSession[] {
  const parsed = result.records
    .map(parseRecalledSessionRecord)
    .sort((left, right) => right.sortTimestamp.localeCompare(left.sortTimestamp));
  const grouped = new Map<string, NormalizedRecalledSession>();

  for (const session of parsed) {
    const groupKey = session.runId ?? session.activatedAt ?? session.id;
    const existing = grouped.get(groupKey);
    if (!existing) {
      grouped.set(groupKey, session);
      continue;
    }

    grouped.set(groupKey, mergeRecalledSessions(existing, session));
  }

  return [...grouped.values()].sort((left, right) => right.sortTimestamp.localeCompare(left.sortTimestamp));
}

export function countNormalizedRecalledSessions(result: SessionRecordRecallResult): number {
  return normalizeRecalledSessions(result).length;
}

export function renderRecalledSessionRecords(result: SessionRecordRecallResult) {
  const sessions = normalizeRecalledSessions(result);
  const visibleSessions = sessions.slice(0, MAX_RECALLED_SESSION_RECORDS);
  const omittedCount = sessions.length - visibleSessions.length;
  const parts = [
    '# Submission Service Mem0 Recall',
    '',
    `- Title Slug: ${result.titleSlug}`,
    `- Recalled Session Count: ${sessions.length}`,
    '- These are historical session records recalled from Mem0 for this exact LeetCode problem.',
    '- Records may include ended-session snapshots and failure-analysis-triggered snapshots.',
    '- When the user asks about past mistakes, enumerate every distinct recalled mistake summary instead of collapsing them into one primary issue.',
    '- Treat these as historical summaries only; do not assume omitted code or truncated snapshots are ground truth.',
  ];

  if (result.records.length !== sessions.length) {
    parts.push(`- Raw Mem0 Record Count: ${result.records.length}`);
  }

  if (omittedCount > 0) {
    parts.push(`- Omitted Older Session Count: ${omittedCount}`);
  }

  visibleSessions.forEach((session, index) => {
    parts.push('', `## Session ${index + 1}`);

    if (session.runId) {
      parts.push(`- Run ID: ${session.runId}`);
    }
    if (session.activatedAt) {
      parts.push(`- Activated At: ${session.activatedAt}`);
    }
    if (session.endedAt) {
      parts.push(`- Ended At: ${session.endedAt}`);
    }
    if (session.endReason) {
      parts.push(`- End Reason: ${session.endReason}`);
    }
    if (typeof session.elapsedMinutes === 'number' && Number.isFinite(session.elapsedMinutes)) {
      parts.push(`- Elapsed Minutes: ${session.elapsedMinutes}`);
    }
    if (session.difficulty) {
      parts.push(`- Difficulty: ${session.difficulty}`);
    }
    if (session.language) {
      parts.push(`- Language: ${session.language}`);
    }
    if (session.latestFailureStatus) {
      parts.push(`- Latest Failure Status: ${session.latestFailureStatus}`);
    }
    if (session.rawRecordCount > 1) {
      parts.push(`- Merged Raw Record Count: ${session.rawRecordCount}`);
    }
    if (session.failureSummaries.length > 0) {
      parts.push(`- Distinct Historical Mistake Count: ${session.failureSummaries.length}`);
    }

    parts.push(
      `- Observed Artifacts: ${session.observedArtifacts.length > 0 ? session.observedArtifacts.join(', ') : 'metadata_only'}`,
    );

    if (session.codeExcerpt) {
      parts.push('', '### Recalled Code Excerpt', '```text', truncate(session.codeExcerpt, MAX_RECALLED_CODE_CHARS), '```');
    }

    if (session.failureSnapshot) {
      parts.push('', '### Recalled Failure Snapshot', truncate(session.failureSnapshot, MAX_RECALLED_FAILURE_CHARS));
    }
    if (session.failureAnalysis) {
      parts.push('', '### Recalled Failure Analysis', truncate(session.failureAnalysis, MAX_RECALLED_ANALYSIS_CHARS));
    }
    if (session.failureSummaries.length > 0) {
      parts.push('', '### Recalled Mistake Summaries');
      for (const summary of session.failureSummaries) {
        parts.push(`- ${truncate(summary, MAX_MESSAGE_CHARS)}`);
      }
    }
    if (session.stuckPoints.length > 0) {
      parts.push('', '### Recalled Stuck Points');
      for (const stuckPoint of session.stuckPoints) {
        parts.push(`- ${truncate(stuckPoint, 240)}`);
      }
    }
  });

  return {
    role: 'user' as const,
    content: parts.join('\n'),
  };
}

export function summarizeRecalledSessionsForMount(result: SessionRecordRecallResult): RecalledMountSessionSummary[] {
  return normalizeRecalledSessions(result).slice(0, MAX_MOUNT_SUMMARY_RECORDS).map((session) => ({
    runId: session.runId,
    endedAt: session.endedAt,
    endReason: session.endReason,
    latestFailureStatus: session.latestFailureStatus,
    distinctMistakeCount: session.failureSummaries.length,
    failureSummary: session.failureSummary,
    failureSummaries: session.failureSummaries.slice(0, 3),
    stuckPoints: session.stuckPoints.slice(0, 3),
    thoughtProcess: session.thoughtProcess.slice(-3),
  }));
}

export function renderRecalledMountSummary(result: SessionRecordRecallResult): string | undefined {
  const sessions = summarizeRecalledSessionsForMount(result);
  if (sessions.length === 0) {
    return undefined;
  }

  const parts = [
    `You have historical LeetCode memory for \`${result.titleSlug}\`.`,
    `Recent recalled sessions: ${sessions.length}.`,
  ];

  sessions.forEach((session, index) => {
    parts.push('', `Session ${index + 1}:`);
    if (session.runId) {
      parts.push(`- Run ID: ${session.runId}`);
    }
    if (session.endReason) {
      parts.push(`- End reason: ${session.endReason}`);
    }
    if (session.latestFailureStatus) {
      parts.push(`- Failure status: ${session.latestFailureStatus}`);
    }
    if (typeof session.distinctMistakeCount === 'number' && session.distinctMistakeCount > 0) {
      parts.push(`- Distinct mistakes: ${session.distinctMistakeCount}`);
    }
    if (session.failureSummary) {
      parts.push(`- Failure reason: ${session.failureSummary}`);
    }
    if (session.failureSummaries && session.failureSummaries.length > 1) {
      parts.push(`- Other failure reasons: ${session.failureSummaries.slice(1).join(' | ')}`);
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
