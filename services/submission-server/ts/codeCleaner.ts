function removeLeadingTrailingEmptyLines(lines: string[]): string[] {
  while (lines.length > 0 && !lines[0].trim()) {
    lines.shift();
  }
  while (lines.length > 0 && !lines.at(-1)?.trim()) {
    lines.pop();
  }
  return lines;
}

function updateDocstringState(
  stripped: string,
  inDocstring: boolean,
  docstringDelimiter: string | null,
): { inDocstring: boolean; docstringDelimiter: string | null } {
  if (!stripped.includes('"""') && !stripped.includes("'''")) {
    return { inDocstring, docstringDelimiter };
  }

  const delimiter = stripped.includes('"""') ? '"""' : "'''";
  const count = stripped.split(delimiter).length - 1;

  if (count !== 1) {
    return { inDocstring, docstringDelimiter };
  }

  if (!inDocstring) {
    return { inDocstring: true, docstringDelimiter: delimiter };
  }

  if (docstringDelimiter === delimiter) {
    return { inDocstring: false, docstringDelimiter: null };
  }

  return { inDocstring, docstringDelimiter };
}

function appendThoughtFromLine(stripped: string, thoughtLines: string[]): void {
  if (stripped.startsWith("#")) {
    thoughtLines.push(stripped.slice(1).trim());
  }
}

function shouldStopThoughtCapture(stripped: string, inDocstring: boolean): boolean {
  if (inDocstring) {
    return false;
  }
  return stripped.startsWith('"""') || stripped.startsWith("'''");
}

function readThoughtMarker(line: string): string | null {
  if (!/@thought\s*:/.test(line)) {
    return null;
  }
  return line.replace(/.*@thought\s*:\s*/, "").trim();
}

function collectThoughtLine(
  stripped: string,
  inThought: boolean,
  inDocstring: boolean,
  thoughtLines: string[],
): boolean {
  if (!inThought) {
    return inThought;
  }

  if (!stripped) {
    return inThought;
  }

  if (stripped.startsWith("#")) {
    appendThoughtFromLine(stripped, thoughtLines);
    return inThought;
  }

  if (shouldStopThoughtCapture(stripped, inDocstring)) {
    return false;
  }

  if (inDocstring) {
    thoughtLines.push(stripped);
    return inThought;
  }

  return false;
}

function normalizeIndentation(lines: string[]): string[] {
  return lines.map((line) => {
    if (!line.trim()) {
      return "";
    }

    const leading = line.length - line.trimStart().length;
    const rawLeading = line.slice(0, leading).replaceAll("\t", "    ");
    const normalizedLeading = " ".repeat(Math.floor(rawLeading.length / 4) * 4);
    return `${normalizedLeading}${line.trimStart()}`;
  });
}

function removeMultipleEmptyLines(lines: string[]): string[] {
  const result: string[] = [];
  let prevEmpty = false;

  for (const line of lines) {
    if (!line.trim()) {
      if (!prevEmpty) {
        result.push("");
      }
      prevEmpty = true;
      continue;
    }

    result.push(line);
    prevEmpty = false;
  }

  return result;
}

function cleanPythonCode(code: string): string {
  if (!code) {
    return "";
  }

  let lines = code.split("\n").map((line) => line.replace(/\s+$/g, ""));
  lines = removeLeadingTrailingEmptyLines(lines);
  lines = normalizeIndentation(lines);
  lines = removeMultipleEmptyLines(lines);
  return lines.join("\n");
}

function findFunctionStart(lines: string[]): number {
  for (let i = 0; i < lines.length; i += 1) {
    if (/^\s*def\s+/.test(lines[i])) {
      return i;
    }
  }
  return -1;
}

function calculateMinIndent(lines: string[], startIdx: number): number {
  let minIndent = Number.POSITIVE_INFINITY;
  for (const line of lines.slice(startIdx + 1)) {
    if (!line.trim()) {
      continue;
    }
    const indent = line.length - line.trimStart().length;
    minIndent = Math.min(minIndent, indent);
  }
  return Number.isFinite(minIndent) ? minIndent : 0;
}

function dedentFunction(lines: string[], startIdx: number, minIndent: number): string {
  const result = [lines[startIdx].trimStart()];
  for (const line of lines.slice(startIdx + 1)) {
    if (!line.trim()) {
      result.push("");
      continue;
    }
    result.push(minIndent > 0 ? line.slice(minIndent) : line);
  }
  return result.join("\n");
}

function extractFunctionOnly(code: string): string {
  const cleaned = cleanPythonCode(code);
  if (!cleaned.includes("class Solution")) {
    return cleaned;
  }

  const lines = cleaned.split("\n");
  const startIdx = findFunctionStart(lines);
  if (startIdx < 0) {
    return cleaned;
  }

  const minIndent = calculateMinIndent(lines, startIdx);
  return dedentFunction(lines, startIdx, minIndent);
}

export function normalizeForEmbedding(code: string, extractFunction = true): string {
  const cleaned = cleanPythonCode(code);
  if (!extractFunction) {
    return cleaned;
  }
  return extractFunctionOnly(cleaned);
}

export function extractThought(code: string): string | null {
  if (!code || !/@thought\s*:/.test(code)) {
    return null;
  }

  const lines = code.split("\n");
  const thoughtLines: string[] = [];
  let inThought = false;
  let inDocstring = false;
  let docstringDelimiter: string | null = null;

  for (const line of lines) {
    const stripped = line.trim();

    const docState = updateDocstringState(stripped, inDocstring, docstringDelimiter);
    inDocstring = docState.inDocstring;
    docstringDelimiter = docState.docstringDelimiter;

    const marker = readThoughtMarker(line);
    if (marker !== null) {
      inThought = true;
      if (marker) {
        thoughtLines.push(marker);
      }
      continue;
    }

    inThought = collectThoughtLine(stripped, inThought, inDocstring, thoughtLines);
  }

  const text = thoughtLines.join(" ").trim();
  return text || null;
}
