import assert from 'node:assert/strict';
import { describe, it } from 'vitest';

import { sanitizeCompanionMessages } from '../src/core/companionChat.ts';
import { Cache } from '../src/cache.ts';
import { SubmissionServer } from '../src/server.ts';
import {
  ActiveSessionScopeManager,
  extractCompanionSessionContext,
  Mem0SessionRecordPersister,
  renderActiveSessionScope,
  renderPersistedSessionRecord,
} from '../src/session/index.ts';
import { parseFailureAnalysis } from '../src/utils/failureAnalysisParser.ts';
import { formatPacificTimestamp, inferIsTestSubmission } from '../src/server.ts';

describe('submission server helpers', () => {
  it('formats timestamps in America/Los_Angeles time', () => {
    const formatted = formatPacificTimestamp(new Date('2026-01-15T18:30:45.000Z'));

    assert.equal(formatted, '2026-01-15 10:30:45 PST');
  });

  it('detects test submissions from leetcode metadata', () => {
    const isTest = inferIsTestSubmission("print('hello')", {
      _: {
        submission: false,
      },
    });

    assert.equal(isTest, true);
  });

  it('prefers persisted lcnvim_is_test when present', () => {
    const isTest = inferIsTestSubmission("print('hello')", {
      lcnvim_is_test: false,
      _: {
        submission: false,
      },
    });

    assert.equal(isTest, false);
  });

  it('serves recent submissions from cache in descending order', () => {
    const cache = new Cache();

    cache.savePending({
      id: 'pending-1',
      title_slug: 'insert-interval',
      submitted_at: '2026-05-25T21:00:00.000Z',
      submitted_at_pst: '2026-05-25 14:00:00 PDT',
      time_spent_minutes: 12,
      submit_result: 'Accepted',
      is_test: false,
    });
    cache.savePending({
      id: 'pending-2',
      title_slug: 'insert-interval',
      submitted_at: '2026-05-25T21:01:00.000Z',
      submitted_at_pst: '2026-05-25 14:01:00 PDT',
      time_spent_minutes: 15,
      submit_result: 'Wrong Answer',
      is_test: true,
    });

    const result = cache.get('insert-interval', 2);
    assert.deepEqual(
      result.map((entry) => entry.id),
      ['pending-2', 'pending-1'],
    );
  });

  it('replaces pending ids with persisted ids and avoids duplicate merges', () => {
    const cache = new Cache();
    const cacheKey = cache.savePending({
      id: 'pending-1',
      title_slug: 'insert-interval',
      submitted_at: '2026-05-25T21:00:00.000Z',
      submitted_at_pst: '2026-05-25 14:00:00 PDT',
      time_spent_minutes: 12,
      submit_result: 'Accepted',
      is_test: false,
    });

    cache.markPersisted('insert-interval', cacheKey, 'db-1');
    const merged = cache.mergePersisted('insert-interval', [
      {
        id: 'db-1',
        title_slug: 'insert-interval',
        submitted_at: '2026-05-25T21:00:00.000Z',
        submitted_at_pst: '2026-05-25 14:00:00 PDT',
        time_spent_minutes: 12,
        submit_result: 'Accepted',
        is_test: false,
      },
    ]);

    assert.equal(merged.length, 1);
    assert.equal(merged[0]?.id, 'db-1');
  });

  it('parses structured failure annotations and filters invalid lines', () => {
    const parsed = parseFailureAnalysis(
      JSON.stringify({
        summary: '第 2 行条件分支少考虑了空输入。',
        annotations: [
          { line: 2, reason: '这里可能越界', severity: 'error' },
          { line: 9, reason: '超出编辑器范围', severity: 'warn' },
          { line: 2, reason: '需要先判空', severity: 'warn' },
        ],
      }),
      4,
    );

    assert.equal(parsed.summary, '第 2 行条件分支少考虑了空输入。');
    assert.deepEqual(parsed.annotations, [
      {
        line: 2,
        reason: '这里可能越界 | 需要先判空',
        severity: 'error',
        column: undefined,
      },
    ]);
  });

  it('sanitizes companion messages and drops invalid entries', () => {
    const messages = sanitizeCompanionMessages([
      { role: 'system', content: 'hidden prompt' },
      { role: 'user', content: ' explain this ' },
      { role: 'assistant', content: 'previous answer' },
      { role: 'tool', content: 'unsupported' },
      { role: 'user', content: '   ' },
      null,
    ]);

    assert.deepEqual(messages, [
      { role: 'system', content: 'hidden prompt' },
      { role: 'user', content: 'explain this' },
      { role: 'assistant', content: 'previous answer' },
    ]);
  });

  it('extracts leetcode companion context from the hidden problem message', () => {
    const context = extractCompanionSessionContext([
      {
        role: 'user',
        content: [
          '# LeetCode Problem Context',
          '',
          '- Title: Two Sum',
          '- Title Slug: two-sum',
          '- Difficulty: Easy',
          '- Language: python3',
          '',
          '## Problem Description',
          'Find two numbers.',
          '',
          '## Active Testcase',
          '```text',
          '[2,7,11,15]',
          '```',
          '',
          '## Current Code',
          '```python3',
          'class Solution:',
          '    pass',
          '```',
        ].join('\n'),
      },
    ]);

    assert.deepEqual(context, {
      title: 'Two Sum',
      titleSlug: 'two-sum',
      difficulty: 'Easy',
      lang: 'python3',
      description: 'Find two numbers.',
      testcase: '[2,7,11,15]',
      code: 'class Solution:\n    pass',
    });
  });

  it('binds failure analysis and companion context into the same active session scope', () => {
    const manager = new ActiveSessionScopeManager();
    manager.activate('two-sum');
    manager.recordCompanionContext({
      title: 'Two Sum',
      titleSlug: 'two-sum',
      difficulty: 'Easy',
      lang: 'python3',
      description: 'Find two numbers.',
      testcase: '[2,7,11,15]',
      code: 'class Solution:\n    pass',
    });
    manager.recordCompanionMessages('two-sum', [{ role: 'user', content: '为什么我的哈希表做法不对？' }]);
    manager.appendCompanionReply('two-sum', '因为你先插入再查找，会错过配对。');
    manager.recordFailureAnalysis(
      {
        titleSlug: 'two-sum',
        title: 'Two Sum',
        questionContent: 'Find two numbers.',
        editorContent: 'class Solution:\n    pass',
        submissionContent: 'class Solution:\n    pass',
        testcase: '[2,7,11,15]',
        judgeResult: { status_msg: 'Wrong Answer' },
        filetype: 'python',
      },
      {
        summary: 'The hash map lookup happens after the insert.',
        annotations: [{ line: 2, reason: 'order is wrong', severity: 'error' }],
      },
      'failure_test_1',
    );

    const scope = manager.getActiveScope();
    assert.ok(scope);
    assert.equal(scope.titleSlug, 'two-sum');
    assert.equal(scope.companionMemory?.messages.length, 2);
    assert.equal(scope.sessionMemory?.messages.length, 1);
    assert.match(scope.sessionMemory?.messages[0]?.content ?? '', /Submission Service Failure Update/);
    assert.match(scope.sessionMemory?.messages[0]?.content ?? '', /Event ID: failure_test_1/);
    assert.match(scope.sessionMemory?.messages[0]?.content ?? '', /Static Analysis Summary/);
    assert.match(scope.sessionMemory?.messages[0]?.content ?? '', /Wrong Answer/);
    assert.equal(scope.latestFailure?.eventId, 'failure_test_1');
    assert.equal(
      scope.latestFailure?.judgeResult && typeof scope.latestFailure.judgeResult === 'object'
        ? scope.latestFailure.judgeResult.status_msg
        : '',
      'Wrong Answer',
    );
    assert.equal(scope.lastFailureAnalysis?.summary, 'The hash map lookup happens after the insert.');

    const rendered = renderActiveSessionScope(scope);
    assert.match(rendered, /Title Slug: two-sum/);
    assert.match(rendered, /Latest LeetCode Failure/);
    assert.match(rendered, /Event ID: failure_test_1/);
    assert.match(rendered, /Wrong Answer/);
    assert.match(rendered, /Latest Failure Analysis/);
    assert.match(rendered, /order is wrong/);
  });

  it('stores companion turns as session memory while stripping hidden context messages', () => {
    const manager = new ActiveSessionScopeManager();
    manager.activate('two-sum');
    manager.recordCompanionContext({
      titleSlug: 'two-sum',
      title: 'Two Sum',
      description: 'Find two numbers.',
      code: 'class Solution:\n    pass',
    });

    const messages = manager.buildCompanionMessages([
      {
        role: 'user',
        content: ['# LeetCode Problem Context', '', '- Title: Two Sum', '- Title Slug: two-sum'].join('\n'),
      },
      { role: 'user', content: '帮我看下为什么 test 过不了' },
    ]);

    assert.equal(messages[0]?.role, 'user');
    assert.match(messages[0]?.content ?? '', /Submission Service Active Session/);
    assert.deepEqual(manager.getActiveScope()?.companionMemory?.messages, [
      { role: 'user', content: '帮我看下为什么 test 过不了' },
    ]);
  });

  it('always injects the latest failure snapshot before companion history', () => {
    const manager = new ActiveSessionScopeManager();
    manager.activate('two-sum');
    manager.recordCompanionMessages('two-sum', [
      { role: 'user', content: '我刚刚犯了什么错误' },
      { role: 'assistant', content: '这是旧诊断。' },
    ]);
    manager.recordFailureAnalysis(
      {
        titleSlug: 'two-sum',
        title: 'Two Sum',
        questionContent: 'Find two numbers.',
        editorContent: 'class Solution:\n    return []',
        submissionContent: 'class Solution:\n    return []',
        testcase: '[3,2,4]\n6',
        judgeResult: { status_msg: 'Wrong Answer', expected_code_answer: '[1,2]' },
        filetype: 'python',
      },
      {
        summary: 'The current code returns an empty list for every input.',
        annotations: [{ line: 2, reason: 'always returns []', severity: 'error' }],
      },
      'failure_test_2',
    );

    const messages = manager.buildCompanionMessages([{ role: 'user', content: '我刚刚犯了什么错误' }]);

    assert.equal(messages[0]?.role, 'user');
    assert.match(messages[0]?.content ?? '', /Submission Service Active Session/);
    assert.equal(messages[1]?.role, 'user');
    assert.match(messages[1]?.content ?? '', /Submission Service Failure Update/);
    assert.match(messages[1]?.content ?? '', /Event ID: failure_test_2/);
    assert.match(messages[1]?.content ?? '', /supersedes any earlier companion diagnosis/);
    assert.match(messages[1]?.content ?? '', /always returns \[\]/);
    assert.deepEqual(messages.slice(2), [{ role: 'user', content: '我刚刚犯了什么错误' }]);
  });

  it('clears agent memory when the active session ends', () => {
    const manager = new ActiveSessionScopeManager();
    manager.activate('two-sum');
    manager.recordCompanionContext({
      title: 'Two Sum',
      titleSlug: 'two-sum',
      difficulty: 'Easy',
      lang: 'python3',
      description: 'Find two numbers.',
      testcase: '[2,7,11,15]',
      code: 'class Solution:\n    return []',
    });
    manager.recordCompanionMessages('two-sum', [
      { role: 'user', content: '我刚刚哪里错了' },
      { role: 'assistant', content: '你现在总是返回空数组。' },
    ]);
    manager.recordFailureAnalysis(
      {
        titleSlug: 'two-sum',
        title: 'Two Sum',
        questionContent: 'Find two numbers.',
        editorContent: 'class Solution:\n    return []',
        submissionContent: 'class Solution:\n    return []',
        testcase: '[2,7,11,15]',
        judgeResult: { status_msg: 'Wrong Answer' },
        filetype: 'python',
      },
      {
        summary: 'The current code returns an empty list for every input.',
        annotations: [{ line: 2, reason: 'always returns []', severity: 'error' }],
      },
      'failure_test_3',
    );

    assert.ok(manager.getActiveScope()?.companionMemory);
    assert.ok(manager.getActiveScope()?.sessionMemory);
    assert.ok(manager.getActiveScope()?.latestFailure);

    manager.clear('two-sum');

    assert.equal(manager.getActiveScope(), null);

    const nextScope = manager.activate('two-sum');
    assert.equal(nextScope.titleSlug, 'two-sum');
    assert.equal(nextScope.companionMemory, undefined);
    assert.equal(nextScope.sessionMemory, undefined);
    assert.equal(nextScope.latestFailure, undefined);
    assert.equal(nextScope.lastFailureAnalysis, undefined);
  });

  it('renders a session snapshot for Mem0 persistence', () => {
    const manager = new ActiveSessionScopeManager();
    manager.activate('two-sum');
    manager.recordCompanionContext({
      title: 'Two Sum',
      titleSlug: 'two-sum',
      difficulty: 'Easy',
      lang: 'python3',
      description: 'Find two numbers.',
      testcase: '[2,7,11,15]\n9',
      code: 'class Solution:\n    return []',
    });
    manager.recordCompanionMessages('two-sum', [
      { role: 'user', content: '我刚刚哪里错了' },
      { role: 'assistant', content: '你现在总是返回空数组。' },
    ]);
    manager.recordFailureAnalysis(
      {
        titleSlug: 'two-sum',
        title: 'Two Sum',
        questionContent: 'Find two numbers.',
        editorContent: 'class Solution:\n    return []',
        submissionContent: 'class Solution:\n    return []',
        testcase: '[2,7,11,15]\n9',
        judgeResult: { status_msg: 'Wrong Answer', expected_code_answer: '[0,1]' },
        filetype: 'python',
      },
      {
        summary: 'The current code returns an empty list for every input.',
        annotations: [{ line: 2, reason: 'always returns []', severity: 'error' }],
      },
      'failure_test_mem0',
    );

    const scope = manager.getActiveScope();
    assert.ok(scope);

    const rendered = renderPersistedSessionRecord(scope, {
      reason: 'stop_timer',
      endedAt: '2026-06-08T00:00:00.000Z',
      elapsedMinutes: 7,
    });

    assert.match(rendered, /LeetCode Session Record/);
    assert.match(rendered, /Title Slug: two-sum/);
    assert.match(rendered, /End Reason: stop_timer/);
    assert.match(rendered, /Latest LeetCode Failure/);
    assert.match(rendered, /Wrong Answer/);
    assert.match(rendered, /Companion Conversation/);
    assert.match(rendered, /always returns \[\]/);
  });

  it('submits a session snapshot to Mem0 with session-scoped ids', async () => {
    let requestMessages:
      | Array<{
          role: 'user' | 'assistant';
          content: string;
        }>
      | undefined;
    let requestOptions: Record<string, unknown> | undefined;

    const persister = new Mem0SessionRecordPersister({
      apiKey: 'mem0-test-key',
      userId: 'jingyi',
      agentId: 'leetcode-submission-service',
      appId: 'leetcode-qa',
      client: {
        add: async (messages, options) => {
          requestMessages = messages;
          requestOptions = options;
          return {
            status: 'PENDING',
            eventId: 'evt_mem0_1',
          };
        },
      },
    });

    await persister.persist(
      {
        titleSlug: 'two-sum',
        activatedAt: '2026-06-08T00:00:00.000Z',
        title: 'Two Sum',
        lang: 'python3',
        editorContent: 'class Solution:\n    return []',
      },
      {
        reason: 'stop_timer',
        endedAt: '2026-06-08T00:05:00.000Z',
        elapsedMinutes: 5,
      },
    );

    assert.equal(requestOptions?.userId, 'jingyi');
    assert.equal(requestOptions?.agentId, 'leetcode-submission-service');
    assert.equal(requestOptions?.appId, 'leetcode-qa');
    assert.equal(requestOptions?.runId, 'leetcode-session:two-sum:2026-06-08T00:00:00.000Z');
    assert.equal(requestOptions?.infer, false);
    assert.equal(Array.isArray(requestMessages), true);
    assert.match(String(requestMessages?.[0]?.content ?? ''), /Title Slug: two-sum/);
  });

  it('persists a session snapshot when the server stops an active session', async () => {
    const server = new SubmissionServer();
    const persisted: Array<{ titleSlug: string; reason: string }> = [];

    (
      server as {
        sessionRecordPersister: { persist: (scope: { titleSlug: string }, event: { reason: string }) => Promise<void> };
      }
    ).sessionRecordPersister = {
      persist: async (scope, event) => {
        persisted.push({
          titleSlug: scope.titleSlug,
          reason: event.reason,
        });
      },
    };

    (server as { timerManager: { start: (titleSlug: string) => void } }).timerManager.start('two-sum');
    (server as { sessionScope: ActiveSessionScopeManager }).sessionScope.activate('two-sum');
    (server as { sessionScope: ActiveSessionScopeManager }).sessionScope.recordCompanionContext({
      titleSlug: 'two-sum',
      title: 'Two Sum',
      description: 'Find two numbers.',
      code: 'class Solution:\n    return []',
    });

    (server as { stopSession: (titleSlug: string) => number }).stopSession('two-sum');
    await Promise.resolve();

    assert.equal((server as { sessionScope: ActiveSessionScopeManager }).sessionScope.getActiveScope(), null);
    assert.deepEqual(persisted, [{ titleSlug: 'two-sum', reason: 'stop_timer' }]);
  });
});
