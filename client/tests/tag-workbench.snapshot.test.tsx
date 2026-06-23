import { readFileSync } from 'node:fs';
import { renderToStaticMarkup } from 'react-dom/server';
import { createElement, type ReactNode } from 'react';
import { describe, expect, it, vi } from 'vitest';

import { TagWorkbench } from '../app/tag-workbench';
import { makeTagWorkbenchSubmissions, makeTagWorkbenchTags } from '../lib/tag-workbench.fixture';

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

function renderWorkbench() {
  return formatHtmlSnapshot(
    renderToStaticMarkup(
      createElement(TagWorkbench, {
        submissions: makeTagWorkbenchSubmissions(),
        tags: makeTagWorkbenchTags(),
        canWrite: true,
      }),
    ),
  );
}

function extractPane(markup: string, tagName: 'section' | 'aside', className: string) {
  const startToken = `<${tagName} class="${className}"`;
  const start = markup.indexOf(startToken);

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

    expect(extractPane(markup, 'aside', 'template-plane template-plane-inspector')).toMatchSnapshot();
  });

  it('keeps the submission code panel on a single scroll contract', () => {
    const markup = renderWorkbench();
    const stylesheet = readFileSync(new URL('../app/globals.css', import.meta.url), 'utf8');

    expect(markup).toContain('class="context-panel-shell context-panel-code"');
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
});
