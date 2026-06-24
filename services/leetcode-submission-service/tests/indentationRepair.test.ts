import assert from 'node:assert/strict';
import { describe, it } from 'vitest';
import {
  createDefaultSubmissionIndentationRepairer,
  isLikelyPythonIndentationDamaged,
  onlyIndentationChanged,
  parseIndentationRepairPayload,
} from '../src/core/indentationRepair.ts';

type RepairClient = Parameters<typeof createDefaultSubmissionIndentationRepairer>[0];

describe('submission indentation repair', () => {
  it('detects nested indentation damage after a block opener', () => {
    const code = `def solve(self, nums):\n    if nums:\n    return nums[0]\n    return 0`;

    assert.equal(isLikelyPythonIndentationDamaged(code), true);
  });

  it('accepts only indentation-only changes', () => {
    const before = `def solve(self):\nreturn 1`;
    const after = `def solve(self):\n    return 1`;
    const changed = `def solve(self):\n    return 2`;

    assert.equal(onlyIndentationChanged(before, after), true);
    assert.equal(onlyIndentationChanged(before, changed), false);
  });

  it('parses repair JSON payloads', () => {
    assert.equal(
      parseIndentationRepairPayload(JSON.stringify({ content: 'def f():\n    pass' })),
      'def f():\n    pass',
    );
    assert.equal(parseIndentationRepairPayload('not json'), null);
  });

  it('rate-limits LLM indentation repair calls', async () => {
    let calls = 0;
    const client = {
      chat: {
        send: async () => {
          calls += 1;
          return {
            choices: [
              {
                message: {
                  content: JSON.stringify({ content: `def solve(self):\n    return 1` }),
                },
              },
            ],
          };
        },
      },
    } as RepairClient;
    const repairer = createDefaultSubmissionIndentationRepairer(client, 'test-model', 1);

    const request = {
      titleSlug: 'two-sum',
      filetype: 'python3',
      content: `def solve(self):\nreturn 1`,
    };

    assert.equal(await repairer.repair(request), `def solve(self):\n    return 1`);
    assert.equal(await repairer.repair(request), null);
    assert.equal(calls, 1);
  });
});
