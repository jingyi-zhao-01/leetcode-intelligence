import type { SubmissionRow } from './data';
import {
  forceCenter,
  forceCollide,
  forceLink,
  forceManyBody,
  forceSimulation,
  forceX,
  forceY,
  type SimulationLinkDatum,
  type SimulationNodeDatum,
} from 'd3-force';

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
  templateTags: Array<{
    key: string;
    label: string;
  }>;
  templateGroups: Array<{
    key: string;
    label: string;
  }>;
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

type GraphLayoutNode = SubmissionGraphNode &
  SimulationNodeDatum & {
    radius: number;
  };

type GraphLayoutLink = SimulationLinkDatum<GraphLayoutNode> & {
  source: string | GraphLayoutNode;
  target: string | GraphLayoutNode;
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
      templateTags: Map<string, string>;
      templateGroups: Map<string, string>;
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
        templateTags: new Map(
          submission.tags
            .filter((tag) => tag.dimension === 'template')
            .map((tag) => [tag.key, tag.label] as const),
        ),
        templateGroups: new Map(
          submission.tags
            .filter((tag) => tag.dimension === 'template' && Boolean(tag.parentKey))
            .map((tag) => [tag.parentKey as string, tag.parentLabel ?? tag.parentKey ?? tag.key] as const),
        ),
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

    for (const tag of submission.tags) {
      if (tag.dimension !== 'template') {
        continue;
      }

      existing.templateTags.set(tag.key, tag.label);
      if (tag.parentKey) {
        existing.templateGroups.set(tag.parentKey, tag.parentLabel ?? tag.parentKey);
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
      templateTags: [...problem.templateTags.entries()].map(([key, label]) => ({ key, label })),
      templateGroups: [...problem.templateGroups.entries()].map(([key, label]) => ({ key, label })),
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

  const nodeState: GraphLayoutNode[] = nodes.map((node, index) => {
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

  const layoutLinks: GraphLayoutLink[] = edges.map((edge) => ({ ...edge }));
  const nodeById = new Map(nodeState.map((node) => [node.id, node]));
  const resolveLayoutNode = (value: string | GraphLayoutNode) => {
    return typeof value === 'string' ? nodeById.get(value) ?? null : value;
  };

  const simulation = forceSimulation<GraphLayoutNode>(nodeState)
    .force('charge', forceManyBody().strength(-420))
    .force(
      'link',
      forceLink<GraphLayoutNode, GraphLayoutLink>(layoutLinks)
        .id((node) => node.id)
        .distance((edge) => {
          const source = resolveLayoutNode(edge.source);
          const target = resolveLayoutNode(edge.target);
          if (!source || !target) {
            return 190;
          }
          return 190 + Math.min(source.attempts + target.attempts, 5) * 12;
        })
        .strength(0.22),
    )
    .force(
      'collide',
      forceCollide<GraphLayoutNode>().radius((node) => node.radius + 10).strength(0.95).iterations(2),
    )
    .force('center', forceCenter(centerX, centerY))
    .force('x', forceX(centerX).strength(0.022))
    .force('y', forceY(centerY).strength(0.022))
    .alpha(1)
    .alphaDecay(0.03)
    .velocityDecay(0.36);

  for (let iteration = 0; iteration < 220; iteration += 1) {
    simulation.tick();
  }
  simulation.stop();

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
    templateTags: node.templateTags,
    templateGroups: node.templateGroups,
  }));

  return { nodes: nodesWithConnection, edges, canvasWidth: finalWidth, canvasHeight: finalHeight };
}
