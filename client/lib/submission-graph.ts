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
  canvasWidth: number;
  canvasHeight: number;
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

  const canvasWidth = Math.max(1600, Math.ceil(Math.sqrt(Math.max(nodes.length, 1)) * 340));
  const canvasHeight = Math.max(1200, Math.ceil(Math.sqrt(Math.max(nodes.length, 1)) * 280));
  const centerX = canvasWidth / 2;
  const centerY = canvasHeight / 2;

  const nodeState = nodes.map((node, index) => {
    const angle = (index / Math.max(nodes.length, 1)) * Math.PI * 2;
    const ringRadius = Math.min(canvasWidth, canvasHeight) * 0.26 + 70 * Math.sqrt(index + 1);
    return {
      ...node,
      x: centerX + ringRadius * Math.cos(angle),
      y: centerY + ringRadius * Math.sin(angle),
      vx: 0,
      vy: 0,
      radius: 72 + Math.min(node.title.length * 2, 68),
    };
  });

  const nodeById = new Map(nodeState.map((node) => [node.id, node]));
  const springLength = 190;
  const repulsionStrength = 24000;
  const centerStrength = 0.0025;
  const damping = 0.82;

  for (let iteration = 0; iteration < 180; iteration += 1) {
    for (let i = 0; i < nodeState.length; i += 1) {
      const left = nodeState[i];
      for (let j = i + 1; j < nodeState.length; j += 1) {
        const right = nodeState[j];
        let dx = right.x - left.x;
        let dy = right.y - left.y;
        const distance = Math.hypot(dx, dy) || 0.001;
        const minDistance = left.radius + right.radius;
        const overlap = Math.max(minDistance - distance, 0);
        const force = overlap > 0 ? overlap * 0.12 : repulsionStrength / (distance * distance);
        dx /= distance;
        dy /= distance;
        left.vx -= dx * force * 0.5;
        left.vy -= dy * force * 0.5;
        right.vx += dx * force * 0.5;
        right.vy += dy * force * 0.5;
      }
    }

    for (const edge of edges) {
      const source = nodeById.get(edge.source);
      const target = nodeById.get(edge.target);
      if (!source || !target) {
        continue;
      }

      let dx = target.x - source.x;
      let dy = target.y - source.y;
      const distance = Math.hypot(dx, dy) || 0.001;
      const desired = springLength + Math.min(source.attempts + target.attempts, 5) * 12;
      const force = (distance - desired) * 0.015;
      dx /= distance;
      dy /= distance;
      source.vx += dx * force;
      source.vy += dy * force;
      target.vx -= dx * force;
      target.vy -= dy * force;
    }

    for (const node of nodeState) {
      node.vx += (centerX - node.x) * centerStrength;
      node.vy += (centerY - node.y) * centerStrength;
      node.vx *= damping;
      node.vy *= damping;
      node.x += node.vx;
      node.y += node.vy;
    }
  }

  const minX = Math.min(...nodeState.map((node) => node.x - node.radius));
  const minY = Math.min(...nodeState.map((node) => node.y - node.radius));
  const maxX = Math.max(...nodeState.map((node) => node.x + node.radius));
  const maxY = Math.max(...nodeState.map((node) => node.y + node.radius));
  const padding = 140;
  const offsetX = padding - minX;
  const offsetY = padding - minY;
  const finalWidth = Math.ceil(maxX - minX + padding * 2);
  const finalHeight = Math.ceil(maxY - minY + padding * 2);

  const nodesWithConnection = nodeState.map((node) => ({
    id: node.id,
    title: node.title,
    slug: node.slug,
    difficulty: node.difficulty,
    attempts: node.attempts,
    lastAttemptAt: node.lastAttemptAt,
    representativeSubmissionId: node.representativeSubmissionId,
    relatedProblems: node.relatedProblems,
    x: node.x + offsetX,
    y: node.y + offsetY,
    connectionCount: connectedMap.get(node.slug)?.size ?? 0,
  }));

  return { nodes: nodesWithConnection, edges, canvasWidth: finalWidth, canvasHeight: finalHeight };
}
