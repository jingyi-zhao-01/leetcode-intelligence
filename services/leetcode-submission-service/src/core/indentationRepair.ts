import type { OpenRouter } from '@openrouter/sdk';
import { createLogger } from '../logger.ts';
import { isPythonFiletype } from '../utils/codeCleaner.ts';

const INDENTATION_REPAIR_PROMPT = `
You repair indentation only for accepted Python LeetCode submissions.

Return JSON only:
{"content":"<same code with indentation repaired>"}

Rules:
- Do not change tokens, names, operators, comments, or line order.
- Do not add imports, explanations, markdown, or code fences.
- Only leading whitespace may change.
`.trim();

type OpenRouterLike = Pick<OpenRouter, 'chat'>;

export type SubmissionIndentationRepairRequest = {
  titleSlug: string;
  content: string;
  filetype: string | null;
};

export type SubmissionIndentationRepairer = {
  repair(request: SubmissionIndentationRepairRequest): Promise<string | null>;
};

const logger = createLogger('submission-indentation-repair');

const truncate = (value: string, maxLength: number): string => {
  if (value.length <= maxLength) {
    return value;
  }
  return `${value.slice(0, maxLength - 3)}...`;
};

const leadingSpaces = (line: string): number => line.length - line.trimStart().length;

const findFunctionStart = (lines: string[]): number => lines.findIndex((line) => /^\s*def\s+/.test(line));

const nextNonEmptyLine = (lines: string[], start: number): string | null => {
  for (const line of lines.slice(start)) {
    if (line.trim()) {
      return line;
    }
  }
  return null;
};

export const isLikelyPythonIndentationDamaged = (code: string): boolean => {
  const lines = code.split('\n');
  const functionStart = findFunctionStart(lines);
  if (functionStart < 0) {
    return false;
  }

  const firstBodyLine = nextNonEmptyLine(lines, functionStart + 1);
  if (!firstBodyLine) {
    return false;
  }
  if (leadingSpaces(firstBodyLine) === 0) {
    return true;
  }

  for (let i = functionStart + 1; i < lines.length - 1; i += 1) {
    const line = lines[i];
    const trimmed = line.trim();
    if (!trimmed || !/:\s*(?:#.*)?$/.test(trimmed)) {
      continue;
    }

    const next = nextNonEmptyLine(lines, i + 1);
    if (next && leadingSpaces(next) <= leadingSpaces(line)) {
      return true;
    }
  }

  return false;
};

const normalizedLineTokens = (code: string): string[] =>
  code
    .split('\n')
    .filter((line) => line.trim().length > 0)
    .map((line) => line.trimStart().replace(/\s+$/g, ''));

export const onlyIndentationChanged = (before: string, after: string): boolean => {
  const left = normalizedLineTokens(before);
  const right = normalizedLineTokens(after);
  return left.length === right.length && left.every((line, index) => line === right[index]);
};

export const parseIndentationRepairPayload = (payload: string): string | null => {
  try {
    const parsed = JSON.parse(payload) as { content?: unknown };
    return typeof parsed.content === 'string' && parsed.content.trim().length > 0 ? parsed.content : null;
  } catch {
    return null;
  }
};

class HourlyRateLimiter {
  private timestamps: number[] = [];

  constructor(private readonly maxPerHour: number) {}

  tryTake(now = Date.now()): boolean {
    if (this.maxPerHour <= 0) {
      return false;
    }
    const cutoff = now - 60 * 60 * 1000;
    this.timestamps = this.timestamps.filter((timestamp) => timestamp > cutoff);
    if (this.timestamps.length >= this.maxPerHour) {
      return false;
    }
    this.timestamps.push(now);
    return true;
  }
}

class OpenRouterSubmissionIndentationRepairer implements SubmissionIndentationRepairer {
  private readonly rateLimiter: HourlyRateLimiter;

  constructor(
    private readonly openRouter: OpenRouterLike,
    private readonly model: string,
    maxPerHour: number,
  ) {
    this.rateLimiter = new HourlyRateLimiter(maxPerHour);
  }

  async repair(request: SubmissionIndentationRepairRequest): Promise<string | null> {
    if (!isPythonFiletype(request.filetype) || !isLikelyPythonIndentationDamaged(request.content)) {
      return null;
    }
    if (!this.rateLimiter.tryTake()) {
      logger.info({ titleSlug: request.titleSlug, model: this.model }, 'Skipped indentation repair due to rate limit');
      return null;
    }

    const startedAt = Date.now();
    const response = await this.openRouter.chat.send({
      chatRequest: {
        model: this.model,
        temperature: 0,
        responseFormat: { type: 'json_object' },
        messages: [
          { role: 'system', content: INDENTATION_REPAIR_PROMPT },
          {
            role: 'user',
            content: JSON.stringify({
              titleSlug: request.titleSlug,
              filetype: request.filetype ?? 'python3',
              content: truncate(request.content, 12000),
            }),
          },
        ],
      },
    });

    const repaired = parseIndentationRepairPayload(response.choices?.[0]?.message?.content ?? '{}');
    if (!repaired || !onlyIndentationChanged(request.content, repaired)) {
      logger.info(
        { titleSlug: request.titleSlug, model: this.model, durationMs: Date.now() - startedAt },
        'Rejected indentation repair because it changed code tokens',
      );
      return null;
    }

    logger.info(
      { titleSlug: request.titleSlug, model: this.model, durationMs: Date.now() - startedAt },
      'Accepted LLM indentation repair',
    );
    return repaired;
  }
}

export const createDefaultSubmissionIndentationRepairer = (
  openRouter: OpenRouterLike,
  model: string,
  maxPerHour: number,
): SubmissionIndentationRepairer => new OpenRouterSubmissionIndentationRepairer(openRouter, model, maxPerHour);
