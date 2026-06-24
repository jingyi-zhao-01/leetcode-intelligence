import type { ActiveSessionScope } from '../scope.ts';
import {
  extractBulletValues,
  readMarkdownSection,
  readMetadataString,
  readMetadataStringArray,
  readStringValue,
} from './shared.ts';
import type {
  RecalledSessionRecord,
  SessionRecordRecallResult,
  SimilarProblemMatch,
  SimilarProblemRecallQuery,
  SimilarProblemRecallResult,
  SimilarityProfile,
} from './types.ts';

type SimilaritySource = {
  titleSlug?: string;
  title?: string;
  difficulty?: string;
  questionContent?: string;
  topicTags?: string[];
  failureSummary?: string;
  failureAnalysis?: string;
  thoughtProcess?: string[];
};

type NormalizedSimilarSession = {
  id: string;
  sourceRecordIds: string[];
  runId?: string;
  titleSlug?: string;
  title?: string;
  difficulty?: string;
  endReason?: string;
  latestFailureStatus?: string;
  endedAt?: string;
  failureSummary?: string;
  failureSummaries: string[];
  stuckPoints: string[];
  thoughtProcess: string[];
  profile: SimilarityProfile;
  sortTimestamp: string;
};

const PATTERN_RULES: Array<{ tag: string; patterns: RegExp[] }> = [
  { tag: 'kadane', patterns: [/\bkadane\b/i, /maximum subarray/i, /maximum product subarray/i] },
  { tag: 'dp', patterns: [/\bdp\b/i, /dynamic programming/i] },
  { tag: 'prefix-sum', patterns: [/prefix sum/i, /prefix sums/i, /cumulative sum/i] },
  { tag: 'sliding-window', patterns: [/sliding window/i, /\bwindow\b/i] },
  { tag: 'two-pointers', patterns: [/two pointers?/i, /two-pointer/i, /left pointer/i, /right pointer/i] },
  { tag: 'binary-search', patterns: [/binary search/i] },
  { tag: 'greedy', patterns: [/\bgreedy\b/i] },
  { tag: 'monotonic-stack', patterns: [/monotonic stack/i] },
  { tag: 'backtracking', patterns: [/backtracking/i, /\bdfs\b/i] },
  { tag: 'bfs', patterns: [/\bbfs\b/i, /breadth first/i] },
  { tag: 'dfs', patterns: [/\bdfs\b/i, /depth first/i] },
  { tag: 'heap', patterns: [/\bheap\b/i, /priority queue/i] },
];

const STATE_RULES: Array<{ tag: string; patterns: RegExp[] }> = [
  { tag: 'contiguous', patterns: [/contiguous/i, /subarray/i, /substring/i] },
  { tag: 'max-min-dual-state', patterns: [/max.*min/i, /minimum.*maximum/i, /min_prod/i, /max_prod/i] },
  { tag: 'negative-flip', patterns: [/negative/i, /sign flip/i, /flip.*sign/i] },
  { tag: 'rolling-state', patterns: [/local optimum/i, /global optimum/i, /running/i, /previous state/i] },
  { tag: 'prefix-accumulation', patterns: [/prefix sum/i, /running sum/i, /cumulative/i] },
  { tag: 'buy-sell-spread', patterns: [/buy and sell stock/i, /max_profit/i, /profit/i] },
  { tag: 'choose-skip', patterns: [/house robber/i, /skip/i, /take or skip/i] },
];

const DOMAIN_RULES: Array<{ tag: string; patterns: RegExp[] }> = [
  { tag: 'array', patterns: [/\barray\b/i, /\bnums\b/i, /\bprices\b/i] },
  { tag: 'subarray', patterns: [/subarray/i] },
  { tag: 'substring', patterns: [/substring/i] },
  { tag: 'string', patterns: [/\bstring\b/i, /palindrome/i] },
  { tag: 'matrix', patterns: [/\bmatrix\b/i, /\bgrid\b/i] },
  { tag: 'tree', patterns: [/\btree\b/i] },
  { tag: 'binary-tree', patterns: [/binary tree/i] },
  { tag: 'graph', patterns: [/\bgraph\b/i] },
  { tag: 'interval', patterns: [/interval/i] },
  { tag: 'linked-list', patterns: [/linked list/i] },
  { tag: 'stack', patterns: [/\bstack\b/i] },
  { tag: 'queue', patterns: [/\bqueue\b/i] },
  { tag: 'heap', patterns: [/\bheap\b/i, /priority queue/i] },
];

const ERROR_RULES: Array<{ tag: string; patterns: RegExp[] }> = [
  { tag: 'forgot-zero-reset', patterns: [/zero reset/i, /reset.*zero/i, /遇到 0/i] },
  { tag: 'missed-min-state', patterns: [/missed min/i, /minimum state/i, /min state/i, /min_prod/i] },
  { tag: 'stale-max-profit', patterns: [/max_profit/i, /profit was never updated/i, /未更新最大利润/i] },
  { tag: 'off-by-one', patterns: [/off by one/i, /boundary/i, /越界/i] },
  { tag: 'double-counted-first-element', patterns: [/double-counted the first element/i, /重复计算/i] },
  { tag: 'wrong-window-shrink', patterns: [/shrink/i, /window/i, /收缩/i] },
  { tag: 'wrong-prefix-init', patterns: [/prefix.*init/i, /初始化/i] },
];

function uniqueStrings(values: Array<string | undefined>, limit?: number): string[] {
  const seen = new Set<string>();
  const items: string[] = [];

  for (const value of values) {
    const normalized = readStringValue(value);
    const dedupeKey = normalized?.toLowerCase();
    if (!normalized || !dedupeKey || seen.has(dedupeKey)) {
      continue;
    }
    seen.add(dedupeKey);
    items.push(normalized);
    if (typeof limit === 'number' && items.length >= limit) {
      break;
    }
  }

  return items;
}

function uniqueTags(values: Array<string | undefined>, limit?: number): string[] {
  const seen = new Set<string>();
  const tags: string[] = [];

  for (const value of values) {
    const normalized = readStringValue(value)
      ?.toLowerCase()
      .replace(/[_\s]+/g, '-');
    if (!normalized || seen.has(normalized)) {
      continue;
    }
    seen.add(normalized);
    tags.push(normalized);
    if (typeof limit === 'number' && tags.length >= limit) {
      break;
    }
  }

  return tags;
}

function collectRuleTags(text: string, rules: Array<{ tag: string; patterns: RegExp[] }>): string[] {
  return rules.flatMap((rule) => (rule.patterns.some((pattern) => pattern.test(text)) ? [rule.tag] : []));
}

function inferSummary(profile: SimilarityProfile): string | undefined {
  const fragments: string[] = [];
  if (profile.patternTags.length > 0) {
    fragments.push(profile.patternTags.slice(0, 2).join('/'));
  }
  if (profile.domainTags.length > 0) {
    fragments.push(profile.domainTags.slice(0, 2).join('/'));
  }
  if (profile.stateTraits.length > 0) {
    fragments.push(profile.stateTraits.slice(0, 2).join('/'));
  }

  if (fragments.length === 0) {
    return undefined;
  }

  return `shared ${fragments.join(' + ')}`;
}

function buildSimilarityProfile(source: SimilaritySource): SimilarityProfile {
  const combinedText = [
    source.titleSlug,
    source.title,
    source.difficulty,
    source.questionContent,
    source.failureSummary,
    source.failureAnalysis,
    ...(source.topicTags ?? []),
    ...(source.thoughtProcess ?? []),
  ]
    .filter((value): value is string => typeof value === 'string' && value.trim().length > 0)
    .join('\n');

  const topicTags = uniqueTags(source.topicTags ?? []);
  const patternTags = uniqueTags(
    [...collectRuleTags(combinedText, PATTERN_RULES), ...topicTags.filter((tag) => tag.includes('dp'))],
    6,
  );
  const stateTraits = uniqueTags(collectRuleTags(combinedText, STATE_RULES), 6);
  const errorTags = uniqueTags(collectRuleTags(combinedText, ERROR_RULES), 6);
  const domainTags = uniqueTags(
    [
      ...collectRuleTags(combinedText, DOMAIN_RULES),
      ...topicTags.filter((tag) => DOMAIN_RULES.some((rule) => rule.tag === tag)),
    ],
    6,
  );

  return {
    patternTags,
    stateTraits,
    errorTags,
    domainTags,
    problemSummary: inferSummary({ patternTags, stateTraits, errorTags, domainTags }),
  };
}

export function buildSimilarityProfileForScope(scope: ActiveSessionScope): SimilarityProfile {
  return buildSimilarityProfile({
    titleSlug: scope.titleSlug,
    title: scope.title,
    difficulty: scope.difficulty,
    questionContent: scope.questionContent,
    topicTags: scope.topicTags,
    failureSummary: scope.lastFailureAnalysis?.summary,
    failureAnalysis: scope.lastFailureAnalysis?.annotations.map((entry) => entry.reason).join('\n'),
    thoughtProcess: scope.companionMemory?.messages
      ?.filter((message) => message.role === 'user')
      .map((message) => message.content),
  });
}

export function buildSimilarityProfileForQuery(query: SimilarProblemRecallQuery): SimilarityProfile {
  return buildSimilarityProfile(query);
}

export function buildSimilarityMetadata(scope: ActiveSessionScope): Record<string, unknown> {
  const profile = buildSimilarityProfileForScope(scope);
  return {
    patternTags: profile.patternTags,
    pattern_tags: profile.patternTags,
    stateTraits: profile.stateTraits,
    state_traits: profile.stateTraits,
    errorTags: profile.errorTags,
    error_tags: profile.errorTags,
    domainTags: profile.domainTags,
    domain_tags: profile.domainTags,
    problemSummary: profile.problemSummary ?? null,
    problem_summary: profile.problemSummary ?? null,
    topicTags: scope.topicTags ?? [],
    topic_tags: scope.topicTags ?? [],
  };
}

function readProfileFromMetadata(metadata: Record<string, unknown>): SimilarityProfile {
  const patternTags = uniqueTags(readMetadataStringArray(metadata, 'pattern_tags', 'patternTags'), 6);
  const stateTraits = uniqueTags(readMetadataStringArray(metadata, 'state_traits', 'stateTraits'), 6);
  const errorTags = uniqueTags(readMetadataStringArray(metadata, 'error_tags', 'errorTags'), 6);
  const domainTags = uniqueTags(readMetadataStringArray(metadata, 'domain_tags', 'domainTags'), 6);
  const problemSummary = readMetadataString(metadata, 'problem_summary', 'problemSummary');

  if (patternTags.length + stateTraits.length + errorTags.length + domainTags.length > 0) {
    return { patternTags, stateTraits, errorTags, domainTags, problemSummary };
  }

  return buildSimilarityProfile({
    titleSlug: readMetadataString(metadata, 'title_slug', 'titleSlug'),
    title: readMetadataString(metadata, 'title'),
    difficulty: readMetadataString(metadata, 'difficulty'),
  });
}

function readRecordLineValue(content: string, label: string): string | undefined {
  const escapedLabel = label.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const match = content.match(new RegExp(`^- ${escapedLabel}:\\s*(.+)$`, 'm'));
  return readStringValue(match?.[1]);
}

function parseSimilarSessionRecord(record: RecalledSessionRecord): NormalizedSimilarSession {
  const metadata = record.metadata ?? {};
  const failureAnalysis = readMarkdownSection(record.memory, 'Latest Failure Analysis') ?? '';
  const companionConversation = readMarkdownSection(record.memory, 'Companion Conversation') ?? '';
  const failureSummary =
    readStringValue(failureAnalysis.match(/^- Summary:\s*(.+)$/m)?.[1]) ??
    readMetadataString(metadata, 'failure_summary', 'failureSummary');

  return {
    id: record.id,
    sourceRecordIds: [record.id],
    runId: readMetadataString(metadata, 'run_id', 'runId') ?? readRecordLineValue(record.memory, 'Run ID'),
    titleSlug:
      readMetadataString(metadata, 'title_slug', 'titleSlug') ?? readRecordLineValue(record.memory, 'Title Slug'),
    title: readMetadataString(metadata, 'title') ?? readRecordLineValue(record.memory, 'Title'),
    difficulty: readMetadataString(metadata, 'difficulty') ?? readRecordLineValue(record.memory, 'Difficulty'),
    endReason:
      readMetadataString(metadata, 'end_reason', 'endReason') ?? readRecordLineValue(record.memory, 'End Reason'),
    latestFailureStatus:
      readMetadataString(metadata, 'latest_failure_status', 'latestFailureStatus') ??
      readRecordLineValue(record.memory, 'Judge Status'),
    endedAt: readMetadataString(metadata, 'ended_at', 'endedAt') ?? readRecordLineValue(record.memory, 'Ended At'),
    failureSummary,
    failureSummaries: uniqueStrings([failureSummary], 6),
    stuckPoints: uniqueStrings(extractBulletValues(failureAnalysis, /^\s*-\s*line\s+\d+\s+\[[^\]]+\]:\s*(.+)$/gm), 6),
    thoughtProcess: uniqueStrings(extractBulletValues(companionConversation, /^- user:\s*(.+)$/gm), 6),
    profile: readProfileFromMetadata(metadata),
    sortTimestamp:
      readMetadataString(metadata, 'ended_at', 'endedAt') ??
      record.createdAt ??
      record.updatedAt ??
      readMetadataString(metadata, 'activated_at', 'activatedAt') ??
      '',
  };
}

function mergeSimilarSessions(
  primary: NormalizedSimilarSession,
  secondary: NormalizedSimilarSession,
): NormalizedSimilarSession {
  return {
    ...primary,
    sourceRecordIds: uniqueStrings([...primary.sourceRecordIds, ...secondary.sourceRecordIds]),
    runId: primary.runId ?? secondary.runId,
    titleSlug: primary.titleSlug ?? secondary.titleSlug,
    title: primary.title ?? secondary.title,
    difficulty: primary.difficulty ?? secondary.difficulty,
    endReason: primary.endReason ?? secondary.endReason,
    latestFailureStatus: primary.latestFailureStatus ?? secondary.latestFailureStatus,
    endedAt: primary.endedAt ?? secondary.endedAt,
    failureSummary: primary.failureSummary ?? secondary.failureSummary,
    failureSummaries: uniqueStrings([...primary.failureSummaries, ...secondary.failureSummaries], 6),
    stuckPoints: uniqueStrings([...primary.stuckPoints, ...secondary.stuckPoints], 6),
    thoughtProcess: uniqueStrings([...primary.thoughtProcess, ...secondary.thoughtProcess], 6),
    profile: {
      patternTags: uniqueTags([...primary.profile.patternTags, ...secondary.profile.patternTags], 6),
      stateTraits: uniqueTags([...primary.profile.stateTraits, ...secondary.profile.stateTraits], 6),
      errorTags: uniqueTags([...primary.profile.errorTags, ...secondary.profile.errorTags], 6),
      domainTags: uniqueTags([...primary.profile.domainTags, ...secondary.profile.domainTags], 6),
      problemSummary: primary.profile.problemSummary ?? secondary.profile.problemSummary,
    },
    sortTimestamp: primary.sortTimestamp || secondary.sortTimestamp,
  };
}

function normalizeSimilarSessions(result: SessionRecordRecallResult): NormalizedSimilarSession[] {
  const grouped = new Map<string, NormalizedSimilarSession>();
  const parsed = result.records
    .map(parseSimilarSessionRecord)
    .sort((left, right) => right.sortTimestamp.localeCompare(left.sortTimestamp));

  for (const session of parsed) {
    const key = session.runId ?? `${session.titleSlug ?? session.id}:${session.id}`;
    const existing = grouped.get(key);
    grouped.set(key, existing ? mergeSimilarSessions(existing, session) : session);
  }

  return [...grouped.values()].sort((left, right) => right.sortTimestamp.localeCompare(left.sortTimestamp));
}

function overlap(left: string[], right: string[]): string[] {
  const rightSet = new Set(right);
  return left.filter((value) => rightSet.has(value));
}

function scoreSimilarity(
  queryProfile: SimilarityProfile,
  candidateProfile: SimilarityProfile,
): { score: number; overlap: SimilarProblemMatch['overlap'] } {
  const patternOverlap = overlap(queryProfile.patternTags, candidateProfile.patternTags);
  const stateOverlap = overlap(queryProfile.stateTraits, candidateProfile.stateTraits);
  const errorOverlap = overlap(queryProfile.errorTags, candidateProfile.errorTags);
  const domainOverlap = overlap(queryProfile.domainTags, candidateProfile.domainTags);
  const score = patternOverlap.length * 4 + stateOverlap.length * 3 + errorOverlap.length * 2 + domainOverlap.length;

  return {
    score,
    overlap: {
      patternTags: patternOverlap,
      stateTraits: stateOverlap,
      errorTags: errorOverlap,
      domainTags: domainOverlap,
    },
  };
}

export function summarizeSimilarProblemRecall(
  recalled: SessionRecordRecallResult,
  query: SimilarProblemRecallQuery,
): SimilarProblemRecallResult {
  const queryProfile = buildSimilarityProfileForQuery(query);
  const bestBySlug = new Map<string, SimilarProblemMatch>();

  for (const session of normalizeSimilarSessions(recalled)) {
    if (!session.titleSlug || session.titleSlug === query.titleSlug) {
      continue;
    }

    const scored = scoreSimilarity(queryProfile, session.profile);
    if (scored.score <= 0) {
      continue;
    }

    const existing = bestBySlug.get(session.titleSlug);
    const match: SimilarProblemMatch = {
      titleSlug: session.titleSlug,
      title: session.title,
      difficulty: session.difficulty,
      score: scored.score,
      overlap: scored.overlap,
      profile: session.profile,
      endReason: session.endReason,
      latestFailureStatus: session.latestFailureStatus,
      failureSummary: session.failureSummary,
      failureSummaries: session.failureSummaries.slice(0, 3),
      stuckPoints: session.stuckPoints.slice(0, 3),
      thoughtProcess: session.thoughtProcess.slice(-3),
      endedAt: session.endedAt,
      runId: session.runId,
    };

    if (!existing || match.score > existing.score) {
      bestBySlug.set(session.titleSlug, match);
    }
  }

  return {
    titleSlug: query.titleSlug,
    queryProfile,
    matches: [...bestBySlug.values()]
      .sort((left, right) => right.score - left.score || left.titleSlug.localeCompare(right.titleSlug))
      .slice(0, 5),
  };
}

export function renderSimilarProblemRecall(result: SimilarProblemRecallResult) {
  const parts = [
    '# Submission Service Similar Problem Recall',
    '',
    `- Title Slug: ${result.titleSlug}`,
    `- Similar Match Count: ${result.matches.length}`,
    '- These are historically solved LeetCode problems that look similar by extracted strategy tags and failure patterns.',
    '- Treat them as candidate analogies, not exact proof that the current problem has the same solution.',
  ];

  if (result.queryProfile.problemSummary) {
    parts.push(`- Query Summary: ${result.queryProfile.problemSummary}`);
  }

  result.matches.forEach((match, index) => {
    parts.push('', `## Similar Problem ${index + 1}`);
    parts.push(`- Title Slug: ${match.titleSlug}`);
    if (match.title) {
      parts.push(`- Title: ${match.title}`);
    }
    if (match.difficulty) {
      parts.push(`- Difficulty: ${match.difficulty}`);
    }
    parts.push(`- Similarity Score: ${match.score}`);
    if (match.profile.problemSummary) {
      parts.push(`- Why Similar: ${match.profile.problemSummary}`);
    }
    if (match.overlap.patternTags.length > 0) {
      parts.push(`- Shared Patterns: ${match.overlap.patternTags.join(', ')}`);
    }
    if (match.overlap.stateTraits.length > 0) {
      parts.push(`- Shared State Traits: ${match.overlap.stateTraits.join(', ')}`);
    }
    if (match.overlap.domainTags.length > 0) {
      parts.push(`- Shared Domains: ${match.overlap.domainTags.join(', ')}`);
    }
    if (match.failureSummaries.length > 0) {
      parts.push(`- Historical Failure Reasons: ${match.failureSummaries.join(' | ')}`);
    }
    if (match.stuckPoints.length > 0) {
      parts.push(`- Historical Stuck Points: ${match.stuckPoints.join(' | ')}`);
    }
    if (match.thoughtProcess.length > 0) {
      parts.push(`- Historical Thought Process: ${match.thoughtProcess.join(' | ')}`);
    }
  });

  return {
    role: 'user' as const,
    content: parts.join('\n'),
  };
}

export function renderSimilarProblemMountSummary(result: SimilarProblemRecallResult): string | undefined {
  if (result.matches.length === 0) {
    return undefined;
  }

  const lines = ['You also solved similar LeetCode problems before.'];
  for (const match of result.matches.slice(0, 3)) {
    lines.push(`- ${match.titleSlug}: ${match.profile.problemSummary ?? 'shared strategy signals'}`);
    if (match.failureSummaries.length > 0) {
      lines.push(`  failure: ${match.failureSummaries.join(' | ')}`);
    }
    if (match.stuckPoints.length > 0) {
      lines.push(`  stuck: ${match.stuckPoints.join(' | ')}`);
    }
  }

  return lines.join('\n');
}
