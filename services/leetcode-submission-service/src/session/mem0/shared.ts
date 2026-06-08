import type { CompanionChatMessage } from '../../core/companionChat.ts';
import {
  MAX_JSON_SECTION_CHARS,
  MAX_MESSAGE_CHARS,
  MAX_TEXT_SECTION_CHARS,
} from './constants.ts';

export const readJudgeStatus = (judgeResult: unknown): string | null => {
  if (!judgeResult || typeof judgeResult !== 'object' || Array.isArray(judgeResult)) {
    return null;
  }

  const status = (judgeResult as { status_msg?: unknown }).status_msg;
  return typeof status === 'string' && status.trim().length > 0 ? status.trim() : null;
};

export const truncate = (value: string, maxChars: number): string => {
  const trimmed = value.trim();
  if (trimmed.length <= maxChars) {
    return trimmed;
  }

  const clipped = trimmed.slice(0, maxChars).trimEnd();
  return `${clipped}\n\n[truncated ${trimmed.length - clipped.length} chars]`;
};

export const truncateJson = (value: unknown): string => {
  try {
    return truncate(JSON.stringify(value, null, 2), MAX_JSON_SECTION_CHARS);
  } catch {
    return '"[unserializable judge result]"';
  }
};

export const readStringValue = (value: unknown): string | undefined => {
  const normalized = typeof value === 'string' ? value.trim() : '';
  return normalized.length > 0 ? normalized : undefined;
};

export const readMetadataRecord = (value: unknown): Record<string, unknown> | undefined => {
  if (!value || typeof value !== 'object' || Array.isArray(value)) {
    return undefined;
  }

  return value as Record<string, unknown>;
};

export const readMetadataString = (metadata: Record<string, unknown>, ...keys: string[]): string | undefined => {
  for (const key of keys) {
    const value = readStringValue(metadata[key]);
    if (value) {
      return value;
    }
  }

  return undefined;
};

export const readMetadataStringArray = (metadata: Record<string, unknown>, ...keys: string[]): string[] => {
  for (const key of keys) {
    const value = metadata[key];
    if (!Array.isArray(value)) {
      continue;
    }

    const normalized = value.flatMap((entry) => {
      const item = readStringValue(entry);
      return item ? [item] : [];
    });
    if (normalized.length > 0) {
      return normalized;
    }
  }

  return [];
};

export const readMetadataNumber = (metadata: Record<string, unknown>, ...keys: string[]): number | null => {
  for (const key of keys) {
    const value = metadata[key];
    if (typeof value === 'number' && Number.isFinite(value)) {
      return value;
    }
  }

  return null;
};

export const hasMarkdownSection = (content: string, heading: string): boolean =>
  new RegExp(`(^|\\n)## ${heading}(\\n|$)`).test(content);

export const readMarkdownSection = (content: string, heading: string): string | undefined => {
  const escapedHeading = heading.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  const match = content.match(new RegExp(`(?:^|\\n)## ${escapedHeading}\\n([\\s\\S]*?)(?=\\n## |$)`));
  const section = match?.[1]?.trim();
  return section && section.length > 0 ? section : undefined;
};

export const stripCodeFence = (content: string): string => {
  const fenced = content.match(/^```[^\n]*\n([\s\S]*?)\n```$/);
  return fenced?.[1]?.trim() ?? content.trim();
};

export const extractBulletValues = (content: string, pattern: RegExp): string[] => {
  const matches = content.matchAll(pattern);
  const values: string[] = [];
  for (const match of matches) {
    const value = match[1]?.trim();
    if (value) {
      values.push(value);
    }
  }
  return values;
};

export const pushTextSection = (parts: string[], heading: string, content?: string): void => {
  if (!content || content.trim().length === 0) {
    return;
  }

  parts.push('', `## ${heading}`, truncate(content, MAX_TEXT_SECTION_CHARS));
};

export const pushCodeSection = (parts: string[], heading: string, code: string | undefined, fence: string): void => {
  if (!code || code.trim().length === 0) {
    return;
  }

  parts.push('', `## ${heading}`, `\`\`\`${fence}`, truncate(code, MAX_TEXT_SECTION_CHARS), '```');
};

export const pushMessagesSection = (
  parts: string[],
  heading: string,
  messages: CompanionChatMessage[] | undefined,
  maxItems: number,
): void => {
  if (!messages || messages.length === 0) {
    return;
  }

  parts.push('', `## ${heading}`);
  for (const message of messages.slice(-maxItems)) {
    parts.push(`- ${message.role}: ${truncate(message.content, MAX_MESSAGE_CHARS)}`);
  }
};
