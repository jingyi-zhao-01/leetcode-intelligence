import { readFileSync } from 'node:fs';
import { renderToStaticMarkup } from 'react-dom/server';
import { createElement, type ReactNode } from 'react';
import { describe, expect, it, vi } from 'vitest';

import { TagWorkbench } from '../app/tag-workbench';
import { makeTagWorkbenchSubmissions, makeTagWorkbenchTags } from '../lib/tag-workbench.fixture';
import type { PatternTagOption, SubmissionRow } from '../lib/data';

vi.mock('next/navigation', () => ({
  useRouter: () => ({
    refresh: vi.fn(),
  }),
}));

vi.mock('../app/actions', () => ({
  benchmarkSubmissionTemplates: vi.fn(),
  createGeneratedTemplate: vi.fn(),
  deleteNonSeededTemplate: vi.fn(),
  generateTemplateDraft: vi.fn(),
  saveSubmissionTags: vi.fn(),
  setSubmissionTemplateOptOut: vi.fn(),
  updateSubmissionThought: vi.fn(),
}));

vi.mock('react-syntax-highlighter', () => ({
  Prism: ({
    children,
    className,
    language,
    customStyle,
    PreTag,
  }: {
    children: ReactNode;
    className?: string;
    language?: string;
    customStyle?: Record<string, unknown>;
    PreTag?: string;
  }) =>
    createElement(
      'pre',
      {
        className,
        'data-language': language ?? 'plain',
        'data-custom-style': customStyle ? JSON.stringify(customStyle) : undefined,
        'data-pre-tag': PreTag ?? undefined,
      },
      children,
    ),
}));

vi.mock('react-syntax-highlighter/dist/esm/styles/prism', () => ({
  oneDark: {},
}));

function formatHtmlSnapshot(markup: string) {
  return markup
    .replace(/></g, '>\n<')
    .replace(/\s{2,}/g, ' ')
    .trim();
}

function extractCssBlock(source: string, selector: string) {
  const escaped = selector.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const match = source.match(new RegExp(`${escaped}\\s*\\{[\\s\\S]*?\\n\\}`, 'm'));

  if (!match) {
    throw new Error(`Missing CSS block for selector: ${selector}`);
  }

  return match[0].trim();
}

function renderWorkbench({
  submissions = makeTagWorkbenchSubmissions(),
  tags = makeTagWorkbenchTags(),
}: {
  submissions?: SubmissionRow[];
  tags?: PatternTagOption[];
} = {}) {
  return formatHtmlSnapshot(
    renderToStaticMarkup(
      createElement(TagWorkbench, {
        submissions,
        tags,
        canWrite: true,
      }),
    ),
  );
}

function makeLongHeaderRightPaneFixture() {
  const tags = makeTagWorkbenchTags();
  const submissions = makeTagWorkbenchSubmissions();
  const hashLookup = tags.find((tag) => tag.key === 'hash-map-lookup');

  if (!hashLookup) {
    throw new Error('Missing hash-map-lookup fixture tag');
  }

  const longHeaderTemplate: PatternTagOption = {
    ...hashLookup,
    id: 'tag-template-hash-grouping',
    key: 'hash-map-grouping',
    label: 'Hash map grouping',
    description: 'Map each item to a canonical signature and group equal signatures together.',
    assignmentCount: 12,
    metadata: {
      ...hashLookup.metadata!,
      whenToUse: [
        'Objects are equivalent after normalization.',
        'Need bucket, group, or aggregate items by a derived key.',
      ],
      whenNotToUse: ['Need preserve exact order as the primary constraint.', 'Need range or neighbor queries.'],
      signals: ['group by', 'signature', 'frequency', 'bucket', 'canonical key'],
      invariants: ['Equivalent inputs map to the same key.', 'The grouped value contains all items for that key.'],
      pseudocode: [
        'groups = map()',
        'for item in items:',
        '  key = normalize(item)',
        '  groups[key].append_or_count(item)',
      ],
      classicProblems: ['49. Group Anagrams', '242. Valid Anagram'],
      relatedDataStructures: ['hash-map', 'counter'],
      similarTemplates: [],
      defaultComplexity: {
        time: 'O(n * normalize_cost)',
        space: 'O(n)',
      },
    },
  };

  const firstSubmission = submissions[0];
  submissions[0] = {
    ...firstSubmission,
    tags: [
      {
        id: longHeaderTemplate.id,
        key: longHeaderTemplate.key,
        label: longHeaderTemplate.label,
        dimension: 'template',
        kind: 'tag',
        parentId: longHeaderTemplate.parentId,
        parentKey: longHeaderTemplate.parentKey,
        parentLabel: longHeaderTemplate.parentLabel,
      },
      ...firstSubmission.tags,
    ],
  };

  return {
    submissions,
    tags: [longHeaderTemplate, ...tags],
  };
}

function extractPane(markup: string, tagName: 'section' | 'aside', className: string) {
  const startPattern = new RegExp(`<${tagName}\\s+class="[^"]*\\b${className.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')}\\b[^"]*"`);
  const startMatch = markup.match(startPattern);
  const start = startMatch?.index ?? -1;

  if (start < 0) {
    throw new Error(`Missing ${tagName}.${className}`);
  }

  const tokenPattern = new RegExp(`<${tagName}(?:\\s|>)|</${tagName}>`, 'g');
  tokenPattern.lastIndex = start;

  let depth = 0;
  let match: RegExpExecArray | null = null;

  while ((match = tokenPattern.exec(markup))) {
    depth += match[0].startsWith(`</${tagName}`) ? -1 : 1;
    if (depth === 0) {
      return markup.slice(start, tokenPattern.lastIndex);
    }
  }

  throw new Error(`Unbalanced ${tagName}.${className}`);
}

describe('TagWorkbench snapshots', () => {
  it('matches the submission history pane', () => {
    const markup = renderWorkbench();

    expect(extractPane(markup, 'section', 'sidebar')).toMatchSnapshot();
  });

  it('matches the tag workbench pane', () => {
    const markup = renderWorkbench();

    expect(extractPane(markup, 'section', 'detail')).toMatchSnapshot();
  });

  it('matches the template control plane', () => {
    const markup = renderWorkbench();

    expect(extractPane(markup, 'aside', 'template-plane-inspector')).toMatchSnapshot();
  });

  it('matches the template control plane with a long header and no benchmark score', () => {
    const markup = renderWorkbench(makeLongHeaderRightPaneFixture());

    expect(extractPane(markup, 'aside', 'template-plane-inspector')).toMatchSnapshot();
  });

  it('keeps the submission code panel on a single scroll contract', () => {
    const markup = renderWorkbench();
    const stylesheet = readFileSync(new URL('../app/globals.css', import.meta.url), 'utf8');

    expect(markup).toContain('class="context-panel-shell overflow-auto context-panel-code"');
    expect(markup).toContain('data-pre-tag="div"');
    expect(markup).toContain('data-custom-style="{&quot;margin&quot;:0,&quot;minHeight&quot;:&quot;100%&quot;}"');

    expect(
      [
        extractCssBlock(stylesheet, '.submission-utility-grid .context-panel-shell'),
        extractCssBlock(
          stylesheet,
          '.submission-utility-grid .context-panel-code .submission-code,\n.submission-utility-grid .context-panel-code .python-code,\n.submission-utility-grid .context-panel-statement .problem-description',
        ),
      ].join('\n\n'),
    ).toMatchSnapshot();
  });

  it('keeps the template control plane header wrapping contract', () => {
    const stylesheet = readFileSync(new URL('../app/globals.css', import.meta.url), 'utf8');

    expect(
      [
        extractCssBlock(stylesheet, '.template-plane-header > div,\n.template-plane-header-actions,\n.plane-complexity'),
        extractCssBlock(stylesheet, '.template-plane-header h2'),
      ].join('\n\n'),
    ).toMatchSnapshot();
  });
});
