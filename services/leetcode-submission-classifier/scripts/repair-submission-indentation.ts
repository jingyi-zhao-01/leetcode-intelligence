import { spawnSync } from 'node:child_process';
import { existsSync, mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

import { PrismaClient, type Prisma } from '@prisma/client';

import { normalizeSubmissionForPersistence } from '../../leetcode-submission-service/src/utils/codeCleaner.ts';

type SubmissionRow = {
  id: string;
  titleSlug: string | null;
  status: string;
  content: string;
  createdAt: Date;
  submissionDetails: Prisma.JsonValue | null;
};

type ParseResult = {
  parseOk: boolean;
  error: string | null;
};

type RepairRecord = {
  id: string;
  titleSlug: string | null;
  createdAt: string;
  lang: string | null;
  parseErrorBefore: string | null;
  parseErrorAfter: string | null;
  oldContent: string;
  repairedContent: string | null;
};

type Artifact = {
  generatedAt: string;
  mode: 'dry-run' | 'write';
  options: {
    scan: number;
    limit: number;
    slug?: string;
    out: string;
  };
  summary: {
    scanned: number;
    pythonAccepted: number;
    parseOkBefore: number;
    candidates: number;
    repairable: number;
    unrepairable: number;
    written: number;
  };
  repairable: RepairRecord[];
  unrepairable: RepairRecord[];
};

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);
const repoRoot = resolve(__dirname, '../../..');

const PYTHON_PARSE = String.raw`
import ast, json, sys
rows = json.load(sys.stdin)
out = []
for row in rows:
    code = row.get("content", "")
    try:
        ast.parse(code)
        out.append({"parseOk": True, "error": None})
    except SyntaxError as exc:
        out.append({"parseOk": False, "error": f"{exc.msg} at line {exc.lineno}"})
json.dump(out, sys.stdout)
`;

function loadEnvFile(path: string): void {
  if (!existsSync(path)) {
    return;
  }

  for (const rawLine of readFileSync(path, 'utf8').split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line || line.startsWith('#')) {
      continue;
    }
    const equals = line.indexOf('=');
    if (equals < 0) {
      continue;
    }
    const key = line.slice(0, equals).trim();
    let value = line.slice(equals + 1).trim();
    if ((value.startsWith('"') && value.endsWith('"')) || (value.startsWith("'") && value.endsWith("'"))) {
      value = value.slice(1, -1);
    }
    process.env[key] ??= value;
  }
}

function parseArgs(argv: string[]): { scan: number; limit: number; slug?: string; write: boolean; out?: string } {
  const options = {
    scan: 5000,
    limit: 5000,
    slug: undefined as string | undefined,
    write: false,
    out: undefined as string | undefined,
  };

  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === '--write') {
      options.write = true;
    } else if (arg === '--scan') {
      options.scan = Number(argv[++i] ?? options.scan);
    } else if (arg === '--limit') {
      options.limit = Number(argv[++i] ?? options.limit);
    } else if (arg === '--slug') {
      options.slug = argv[++i];
    } else if (arg === '--out') {
      options.out = argv[++i];
    }
  }

  options.scan = Number.isFinite(options.scan) && options.scan > 0 ? options.scan : 5000;
  options.limit = Number.isFinite(options.limit) && options.limit > 0 ? options.limit : options.scan;
  return options;
}

function languageOf(row: SubmissionRow): string | null {
  if (!row.submissionDetails || typeof row.submissionDetails !== 'object' || Array.isArray(row.submissionDetails)) {
    return null;
  }
  const details = row.submissionDetails as Record<string, unknown>;
  const lang = details.lang ?? details.language ?? details.pretty_lang ?? details.langName ?? details.filetype;
  return typeof lang === 'string' ? lang.toLowerCase() : null;
}

function parsePython(contents: string[]): ParseResult[] {
  if (contents.length === 0) {
    return [];
  }

  const result = spawnSync('python3', ['-c', PYTHON_PARSE], {
    input: JSON.stringify(contents.map((content) => ({ content }))),
    encoding: 'utf8',
    maxBuffer: 50 * 1024 * 1024,
  });

  if (result.status !== 0) {
    throw new Error(result.stderr.trim() || 'python3 parse check failed');
  }

  return JSON.parse(result.stdout) as ParseResult[];
}

function onlyIndentationChanged(before: string, after: string): boolean {
  const normalize = (code: string): string[] =>
    code
      .split('\n')
      .filter((line) => line.trim().length > 0)
      .map((line) => line.trimStart().replace(/\s+$/g, ''));
  const left = normalize(before);
  const right = normalize(after);
  return left.length === right.length && left.every((line, index) => line === right[index]);
}

async function main(): Promise<void> {
  loadEnvFile(resolve(repoRoot, '.env'));
  loadEnvFile(resolve(repoRoot, 'services/leetcode-submission-service/.env'));

  const options = parseArgs(process.argv.slice(2));
  const artifactPath =
    options.out ??
    resolve(
      repoRoot,
      `services/leetcode-submission-classifier/artifacts/submission-indentation-repair-${new Date()
        .toISOString()
        .replace(/[:.]/g, '-')}.json`,
    );

  const prisma = new PrismaClient();
  try {
    const rows = await prisma.submission.findMany({
      take: options.scan,
      orderBy: { createdAt: 'desc' },
      where: {
        status: 'Accepted',
        ...(options.slug ? { titleSlug: options.slug } : {}),
      },
      select: {
        id: true,
        titleSlug: true,
        status: true,
        content: true,
        createdAt: true,
        submissionDetails: true,
      },
    });

    const pythonRows = rows.filter((row) => languageOf(row)?.includes('python')).slice(0, options.limit);
    const before = parsePython(pythonRows.map((row) => row.content));

    const candidates: Array<{ row: SubmissionRow; before: ParseResult; repaired: string; after: ParseResult }> = [];
    const unrepairable: RepairRecord[] = [];
    let parseOkBefore = 0;

    pythonRows.forEach((row, index) => {
      const beforeParse = before[index] ?? { parseOk: false, error: 'missing parse result' };
      if (beforeParse.parseOk) {
        parseOkBefore += 1;
        return;
      }

      const lang = languageOf(row);
      const repaired = normalizeSubmissionForPersistence({
        code: row.content,
        status: row.status,
        filetype: lang,
      });

      if (repaired === row.content || !onlyIndentationChanged(row.content, repaired)) {
        unrepairable.push({
          id: row.id,
          titleSlug: row.titleSlug,
          createdAt: row.createdAt.toISOString(),
          lang,
          parseErrorBefore: beforeParse.error,
          parseErrorAfter: null,
          oldContent: row.content,
          repairedContent: repaired === row.content ? null : repaired,
        });
        return;
      }

      candidates.push({
        row,
        before: beforeParse,
        repaired,
        after: { parseOk: false, error: null },
      });
    });

    const after = parsePython(candidates.map((candidate) => candidate.repaired));
    const repairable: RepairRecord[] = [];

    candidates.forEach((candidate, index) => {
      const afterParse = after[index] ?? { parseOk: false, error: 'missing parse result' };
      candidate.after = afterParse;
      const lang = languageOf(candidate.row);
      const record = {
        id: candidate.row.id,
        titleSlug: candidate.row.titleSlug,
        createdAt: candidate.row.createdAt.toISOString(),
        lang,
        parseErrorBefore: candidate.before.error,
        parseErrorAfter: afterParse.error,
        oldContent: candidate.row.content,
        repairedContent: candidate.repaired,
      };

      if (afterParse.parseOk) {
        repairable.push(record);
      } else {
        unrepairable.push(record);
      }
    });

    let written = 0;
    if (options.write) {
      for (const record of repairable) {
        await prisma.submission.update({
          where: { id: record.id },
          data: { content: record.repairedContent ?? record.oldContent },
        });
        written += 1;
      }
    }

    const artifact: Artifact = {
      generatedAt: new Date().toISOString(),
      mode: options.write ? 'write' : 'dry-run',
      options: {
        scan: options.scan,
        limit: options.limit,
        slug: options.slug,
        out: artifactPath,
      },
      summary: {
        scanned: rows.length,
        pythonAccepted: pythonRows.length,
        parseOkBefore,
        candidates: pythonRows.length - parseOkBefore,
        repairable: repairable.length,
        unrepairable: unrepairable.length,
        written,
      },
      repairable,
      unrepairable,
    };

    mkdirSync(dirname(artifactPath), { recursive: true });
    writeFileSync(artifactPath, `${JSON.stringify(artifact, null, 2)}\n`);
    console.log(JSON.stringify(artifact.summary, null, 2));
    console.log(`artifact: ${artifactPath}`);
  } finally {
    await prisma.$disconnect();
  }
}

void main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
