import assert from 'node:assert/strict';
import { describe, it } from 'vitest';

import { companionHttpApiSpec, submissionActionApiSpec } from '../src/api-spec.ts';
import { SubmissionServer, ServerAction } from '../src/server.ts';
import { ActiveSessionScopeManager } from '../src/session/index.ts';

function callAction(server: SubmissionServer, request: Record<string, unknown>) {
  return (
    server as unknown as {
      handleRequest: (request: Record<string, unknown>) => Promise<Record<string, unknown>>;
    }
  ).handleRequest(request);
}

describe('submission service API spec', () => {
  it('documents every server action exactly once', () => {
    const documented = submissionActionApiSpec.map((entry) => entry.action).sort();
    const implemented = Object.values(ServerAction).sort();

    assert.deepEqual(documented, implemented);
  });

  it('documents the companion HTTP surface', () => {
    assert.deepEqual(
      companionHttpApiSpec.map((entry) => `${entry.method} ${entry.path}`),
      ['GET /health', 'GET /v1/models', 'POST /v1/chat/completions'],
    );
  });
});

describe('submission service action contracts', () => {
  it('start_timer returns the documented contract', async () => {
    const server = new SubmissionServer();

    const response = await callAction(server, {
      action: ServerAction.START_TIMER,
      title_slug: 'two-sum',
    });

    assert.deepEqual(Object.keys(response).sort(), [
      'action',
      'already_active',
      'evicted_title_slugs',
      'success',
      'title_slug',
    ]);
    assert.equal(response.success, true);
    assert.equal(response.action, ServerAction.START_TIMER);
    assert.equal(response.title_slug, 'two-sum');
    assert.equal(Array.isArray(response.evicted_title_slugs), true);
  });

  it('stop_timer returns elapsed minutes', async () => {
    const server = new SubmissionServer();
    await callAction(server, { action: ServerAction.START_TIMER, title_slug: 'two-sum' });

    const response = await callAction(server, {
      action: ServerAction.STOP_TIMER,
      title_slug: 'two-sum',
    });

    assert.deepEqual(Object.keys(response).sort(), ['action', 'minutes', 'success', 'title_slug']);
    assert.equal(response.success, true);
    assert.equal(response.action, ServerAction.STOP_TIMER);
    assert.equal(typeof response.minutes, 'number');
  });

  it('get_active_timers returns a timers object', async () => {
    const server = new SubmissionServer();
    await callAction(server, { action: ServerAction.START_TIMER, title_slug: 'two-sum' });

    const response = await callAction(server, {
      action: ServerAction.GET_ACTIVE_TIMERS,
    });

    assert.deepEqual(Object.keys(response).sort(), ['action', 'success', 'timers']);
    assert.equal(response.success, true);
    assert.equal(response.action, ServerAction.GET_ACTIVE_TIMERS);
    assert.equal(typeof response.timers, 'object');
  });

  it('get_active_sessions returns a count and session list', async () => {
    const server = new SubmissionServer();
    await callAction(server, { action: ServerAction.START_TIMER, title_slug: 'two-sum' });

    const response = await callAction(server, {
      action: ServerAction.GET_ACTIVE_SESSIONS,
    });

    assert.deepEqual(Object.keys(response).sort(), ['action', 'count', 'sessions', 'success']);
    assert.equal(response.success, true);
    assert.equal(response.action, ServerAction.GET_ACTIVE_SESSIONS);
    assert.equal(Array.isArray(response.sessions), true);
    assert.equal(typeof response.count, 'number');
  });

  it('get_past_submissions returns the documented list shape', async () => {
    const server = new SubmissionServer();
    (
      server as unknown as {
        actionHandlers: Record<string, (...args: unknown[]) => Promise<Record<string, unknown>>>;
      }
    ).actionHandlers[ServerAction.GET_PAST_SUBMISSIONS] = async () => ({
      success: true,
      action: ServerAction.GET_PAST_SUBMISSIONS,
      title_slug: 'two-sum',
      submissions: [],
      count: 0,
    });

    const response = await callAction(server, {
      action: ServerAction.GET_PAST_SUBMISSIONS,
      title_slug: 'two-sum',
    });

    assert.deepEqual(Object.keys(response).sort(), ['action', 'count', 'submissions', 'success', 'title_slug']);
    assert.equal(response.success, true);
    assert.equal(response.action, ServerAction.GET_PAST_SUBMISSIONS);
    assert.equal(Array.isArray(response.submissions), true);
  });

  it('get_mem0_recall_summary rejects missing title_slug with a stable error shape', async () => {
    const server = new SubmissionServer();

    const response = await callAction(server, {
      action: ServerAction.GET_MEM0_RECALL_SUMMARY,
    });

    assert.deepEqual(Object.keys(response).sort(), ['action', 'error', 'success']);
    assert.equal(response.success, false);
    assert.equal(response.action, ServerAction.GET_MEM0_RECALL_SUMMARY);
    assert.match(String(response.error), /title_slug is required/i);
  });

  it('save_submission returns the documented success shape', async () => {
    const server = new SubmissionServer();
    (
      server as unknown as {
        actionHandlers: Record<string, (...args: unknown[]) => Promise<Record<string, unknown>>>;
      }
    ).actionHandlers[ServerAction.SAVE_SUBMISSION] = async () => ({
      success: true,
      action: ServerAction.SAVE_SUBMISSION,
      title_slug: 'two-sum',
    });

    const response = await callAction(server, {
      action: ServerAction.SAVE_SUBMISSION,
      title_slug: 'two-sum',
      content: 'class Solution:\n    pass',
      item: {},
    });

    assert.deepEqual(Object.keys(response).sort(), ['action', 'success', 'title_slug']);
    assert.equal(response.success, true);
    assert.equal(response.action, ServerAction.SAVE_SUBMISSION);
  });

  it('analyze_failure returns the documented success shape', async () => {
    const server = new SubmissionServer();
    (
      server as unknown as {
        failureAnalyzer: {
          analyze: (payload: Record<string, unknown>) => Promise<{
            summary: string;
            annotations: Array<{ line: number; reason: string; severity: string }>;
          }>;
        };
        sessionScope: ActiveSessionScopeManager;
      }
    ).failureAnalyzer = {
      analyze: async () => ({
        summary: 'Wrong branch condition.',
        annotations: [{ line: 2, reason: 'missing guard', severity: 'error' }],
      }),
    };
    (
      server as unknown as {
        sessionScope: ActiveSessionScopeManager;
      }
    ).sessionScope.activate('two-sum');

    const response = await callAction(server, {
      action: ServerAction.ANALYZE_FAILURE,
      title_slug: 'two-sum',
      editor_content: 'class Solution:\n    pass',
    });

    assert.deepEqual(Object.keys(response).sort(), [
      'action',
      'annotations',
      'count',
      'event_id',
      'success',
      'summary',
      'title_slug',
    ]);
    assert.equal(response.success, true);
    assert.equal(response.action, ServerAction.ANALYZE_FAILURE);
    assert.equal(Array.isArray(response.annotations), true);
  });

  it('returns a stable error payload for unknown actions', async () => {
    const server = new SubmissionServer();

    const response = await callAction(server, { action: 'nope' });

    assert.deepEqual(Object.keys(response), ['error']);
    assert.match(String(response.error), /unknown action/i);
  });
});

describe('submission service companion contracts', () => {
  it('documents the OpenAI-compatible completion shape', async () => {
    const server = new SubmissionServer();
    (
      server as unknown as {
        companionChat: {
          chat: () => Promise<{
            model: string;
            content: string;
            finishReason: string;
            usage: { prompt_tokens: number; completion_tokens: number; total_tokens: number };
          }>;
        };
        sessionScope: ActiveSessionScopeManager;
      }
    ).companionChat = {
      chat: async () => ({
        model: 'qwen/qwen3-coder-next',
        content: 'Use a hash map.',
        finishReason: 'stop',
        usage: {
          prompt_tokens: 12,
          completion_tokens: 4,
          total_tokens: 16,
        },
      }),
    };

    const sessionScope = (
      server as unknown as {
        sessionScope: ActiveSessionScopeManager;
      }
    ).sessionScope;
    sessionScope.activate('two-sum');
    sessionScope.recordMem0Recall('two-sum', 0);
    sessionScope.recordSimilarRecall('two-sum', 0);

    const response = await (
      server as unknown as {
        createCompanionChatCompletion: (body: Record<string, unknown>) => Promise<Record<string, unknown>>;
      }
    ).createCompanionChatCompletion({
      messages: [{ role: 'user', content: 'help me' }],
    });

    assert.equal(response.object, 'chat.completion');
    assert.equal(typeof response.id, 'string');
    assert.equal(Array.isArray(response.choices), true);
    assert.equal(response.model, 'qwen/qwen3-coder-next');
  });

  it('returns the documented error shape when no active session is bound', async () => {
    const server = new SubmissionServer();
    (
      server as unknown as {
        companionChat: { chat: () => Promise<never> };
      }
    ).companionChat = {
      chat: async () => {
        throw new Error('not reached');
      },
    };

    const response = await (
      server as unknown as {
        createCompanionChatCompletion: (body: Record<string, unknown>) => Promise<Record<string, unknown>>;
      }
    ).createCompanionChatCompletion({
      messages: [{ role: 'user', content: 'help me' }],
    });

    assert.deepEqual(Object.keys(response), ['error']);
    assert.equal(typeof response.error, 'object');
    assert.match(String((response.error as { type?: string }).type ?? ''), /invalid_request_error/);
  });
});
