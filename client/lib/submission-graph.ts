import type { SubmissionRow } from './data';

export type SubmissionGraphNode = {
  id: string;
  title: string;
  slug: string;
  difficulty: string | null;
  attempts: number;
  lastAttemptAt: string;
  representativeSubmissionId: string;
  relatedProblems: string[];
  x: number;
  y: number;
  connectionCount: number;
};

export type SubmissionGraphEdge = {
  id: string;
  source: string;
  target: string;
};

export type SubmissionGraph = {
  nodes: SubmissionGraphNode[];
  edges: SubmissionGraphEdge[];
};

export function normalizeRelatedSlug(value: string) {
  const trimmed = value.trim();
  if (!trimmed) {
    return '';
  }

  const cleaned = trimmed
    .replace(/^https?:\/\/leetcode\.com\/problems\//i, '')
    .replace(/^https?:\/\/(www\.)?leetcode\.com\/problems\//i, '')
    .replace(/\/$/, '')
    .split(/[?#]/)[0]
    .trim()
    .toLowerCase();
  if (!cleaned) {
    return '';
  }

  const parts = cleaned.split('/');
  return parts[parts.length - 1] ?? cleaned;
}

export function buildSubmissionGraph(submissions: SubmissionRow[]) {
  const problemMap = new Map<
    string,
    {
      slug: string;
      title: string;
      difficulty: string | null;
      attempts: number;
      lastAttemptAt: string;
      representativeSubmissionId: string;
      relatedProblems: Set<string>;
    }
  >();

  for (const submission of submissions) {
    if (!submission.titleSlug) {
      continue;
    }

    const slug = submission.titleSlug.toLowerCase();
    const existing = problemMap.get(slug);
    if (!existing) {
      problemMap.set(slug, {
        slug,
        title: submission.title ?? slug,
        difficulty: submission.difficulty ?? null,
        attempts: 1,
        lastAttemptAt: submission.createdAt,
        representativeSubmissionId: submission.id,
        relatedProblems: new Set(submission.relatedProblems.map(normalizeRelatedSlug)),
      });
      continue;
    }

    existing.attempts += 1;
    if (new Date(submission.createdAt) > new Date(existing.lastAttemptAt)) {
      existing.lastAttemptAt = submission.createdAt;
      existing.representativeSubmissionId = submission.id;
      existing.title = submission.title ?? existing.title;
      existing.difficulty = submission.difficulty ?? existing.difficulty;
    }
    for (const related of submission.relatedProblems) {
      const normalized = normalizeRelatedSlug(related);
      if (normalized) {
        existing.relatedProblems.add(normalized);
      }
    }
  }

  const nodes = Array.from(problemMap.values())
    .sort((left, right) => {
      if (right.attempts !== left.attempts) {
        return right.attempts - left.attempts;
      }
      return left.title.localeCompare(right.title);
    })
    .map((problem) => ({
      id: problem.slug,
      title: problem.title,
      slug: problem.slug,
      difficulty: problem.difficulty,
      attempts: problem.attempts,
      lastAttemptAt: problem.lastAttemptAt,
      representativeSubmissionId: problem.representativeSubmissionId,
      relatedProblems: Array.from(problem.relatedProblems),
      x: 0,
      y: 0,
      connectionCount: 0,
    }));

  const nodeSet = new Set(nodes.map((node) => node.slug));
  const edges: SubmissionGraphEdge[] = [];
  const edgeSet = new Set<string>();
  const connectedMap = new Map<string, Set<string>>(nodes.map((node) => [node.slug, new Set<string>()]));

  for (const node of nodes) {
    for (const raw of node.relatedProblems) {
      const neighbor = normalizeRelatedSlug(raw);
      if (!neighbor || neighbor === node.slug || !nodeSet.has(neighbor)) {
        continue;
      }

      const sorted = [node.slug, neighbor].sort();
      const edgeKey = `${sorted[0]}::${sorted[1]}`;
      if (edgeSet.has(edgeKey)) {
        continue;
      }
      edgeSet.add(edgeKey);
      edges.push({ id: edgeKey, source: sorted[0], target: sorted[1] });

      connectedMap.get(node.slug)?.add(neighbor);
      connectedMap.get(neighbor)?.add(node.slug);
    }
  }

  const goldenAngle = Math.PI * (3 - Math.sqrt(5));
  const centerX = 760 / 2;
  const centerY = 520 / 2;
  const baseRadius = 26;
  const spread = 14;

  nodes.forEach((node, index) => {
    if (nodes.length === 1) {
      node.x = centerX;
      node.y = centerY;
      return;
    }

    const radius = baseRadius + spread * Math.sqrt(index + 1);
    const angle = index * goldenAngle;
    node.x = centerX + radius * Math.cos(angle);
    node.y = centerY + radius * Math.sin(angle);
  });

  const nodesWithConnection = nodes.map((node) => ({
    ...node,
    connectionCount: connectedMap.get(node.slug)?.size ?? 0,
  }));

  return { nodes: nodesWithConnection, edges };
}
