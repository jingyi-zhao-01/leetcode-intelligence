import type { Force } from 'd3-force';
import type { SubmissionGraphNode } from './submission-graph';

export type ClusterEnvelope = {
  id: string;
  kind: 'template-group' | 'template';
  key: string;
  label: string;
  parentKey?: string;
  nodeIds: string[];
  x: number;
  y: number;
  width: number;
  height: number;
  labelX: number;
  labelY: number;
  labelWidth: number;
  labelHeight: number;
};

export type DanglingTemplateMarker = {
  nodeId: string;
  templateKey: string;
  templateLabel: string;
  parentKey: string;
};

type ClusterAnchor = {
  key: string;
  x: number;
  y: number;
};

type ClusterableNode = {
  id: string;
  x: number;
  y: number;
  vx?: number;
  vy?: number;
  templateGroups: SubmissionGraphNode['templateGroups'];
  templateTags: SubmissionGraphNode['templateTags'];
  primaryTemplateGroup: SubmissionGraphNode['primaryTemplateGroup'];
};

export function buildPrimaryClusterAnchors(
  nodes: Array<Pick<ClusterableNode, 'primaryTemplateGroup'>>,
  canvasWidth: number,
  canvasHeight: number,
) {
  const uniqueGroups = [...new Map(
    nodes
      .filter((node) => node.primaryTemplateGroup)
      .map((node) => [node.primaryTemplateGroup!.key, node.primaryTemplateGroup!]),
  ).values()].sort((left, right) => left.label.localeCompare(right.label));

  if (!uniqueGroups.length) {
    return new Map<string, ClusterAnchor>();
  }

  const centerX = canvasWidth / 2;
  const centerY = canvasHeight / 2;
  const radiusX = Math.max(240, canvasWidth * 0.24);
  const radiusY = Math.max(180, canvasHeight * 0.2);

  return new Map<string, ClusterAnchor>(
    uniqueGroups.map((group, index) => {
      if (uniqueGroups.length === 1) {
        return [group.key, { key: group.key, x: centerX, y: centerY }] as const;
      }

      const angle = Math.PI + (index / uniqueGroups.length) * Math.PI * 2;
      return [
        group.key,
        {
          key: group.key,
          x: centerX + Math.cos(angle) * radiusX,
          y: centerY + Math.sin(angle) * radiusY,
        },
      ] as const;
    }),
  );
}

export function createPrimaryClusterForce<Node extends ClusterableNode>(
  anchorByKey: Map<string, ClusterAnchor>,
  strength: number,
): Force<Node, never> {
  let nodes: Node[] = [];

  const force = ((alpha: number) => {
    for (const node of nodes) {
      const clusterKey = node.primaryTemplateGroup?.key;
      if (!clusterKey) {
        continue;
      }

      const anchor = anchorByKey.get(clusterKey);
      if (!anchor) {
        continue;
      }

      node.vx = (node.vx ?? 0) + (anchor.x - node.x) * strength * alpha;
      node.vy = (node.vy ?? 0) + (anchor.y - node.y) * strength * alpha;
    }
  }) as Force<Node, never>;

  force.initialize = (forceNodes) => {
    nodes = forceNodes as Node[];
  };

  return force;
}

export function createSharedTemplateGroupForce<Node extends ClusterableNode>(
  anchorByKey: Map<string, ClusterAnchor>,
  strength: number,
): Force<Node, never> {
  let nodes: Node[] = [];

  const force = ((alpha: number) => {
    for (const node of nodes) {
      if (!node.templateGroups.length) {
        continue;
      }

      let targetX = 0;
      let targetY = 0;
      let count = 0;

      for (const group of node.templateGroups) {
        const anchor = anchorByKey.get(group.key);
        if (!anchor) {
          continue;
        }

        targetX += anchor.x;
        targetY += anchor.y;
        count += 1;
      }

      if (!count) {
        continue;
      }

      node.vx = (node.vx ?? 0) + (targetX / count - node.x) * strength * alpha;
      node.vy = (node.vy ?? 0) + (targetY / count - node.y) * strength * alpha;
    }
  }) as Force<Node, never>;

  force.initialize = (forceNodes) => {
    nodes = forceNodes as Node[];
  };

  return force;
}

export function buildVisibleTemplateGroupEnvelopes<Node extends ClusterableNode>(
  nodes: Node[],
  visiblePrimaryClusterKeys: Set<string>,
  radiusForNode: (node: Node) => number,
) {
  const nodeById = new Map(nodes.map((node) => [node.id, node]));
  const clusterMap = new Map<string, ClusterEnvelope>();
  const templateClusterMap = new Map<string, ClusterEnvelope>();
  const padding = 20;

  for (const node of nodes) {
    for (const group of node.templateGroups) {
      if (!visiblePrimaryClusterKeys.has(group.key)) {
        continue;
      }

      const id = `template-group:${group.key}`;
      const cluster = clusterMap.get(id);
      if (cluster) {
        cluster.nodeIds.push(node.id);
        continue;
      }

      clusterMap.set(id, {
        id,
        kind: 'template-group',
        key: group.key,
        label: group.label,
        nodeIds: [node.id],
        x: 0,
        y: 0,
        width: 0,
        height: 0,
        labelX: 0,
        labelY: 0,
        labelWidth: 0,
        labelHeight: 22,
      });
    }

    for (const template of node.templateTags) {
      if (!template.parentKey || !visiblePrimaryClusterKeys.has(template.parentKey)) {
        continue;
      }

      const id = `template:${template.parentKey}:${template.key}`;
      const cluster = templateClusterMap.get(id);
      if (cluster) {
        cluster.nodeIds.push(node.id);
        continue;
      }

      templateClusterMap.set(id, {
        id,
        kind: 'template',
        key: template.key,
        label: template.label,
        parentKey: template.parentKey,
        nodeIds: [node.id],
        x: 0,
        y: 0,
        width: 0,
        height: 0,
        labelX: 0,
        labelY: 0,
        labelWidth: 0,
        labelHeight: 20,
      });
    }
  }

  const envelopes: ClusterEnvelope[] = [];

  for (const cluster of [...clusterMap.values(), ...templateClusterMap.values()]) {
    let minX = Number.POSITIVE_INFINITY;
    let minY = Number.POSITIVE_INFINITY;
    let maxX = Number.NEGATIVE_INFINITY;
    let maxY = Number.NEGATIVE_INFINITY;

    for (const nodeId of cluster.nodeIds) {
      const node = nodeById.get(nodeId);
      if (!node) {
        continue;
      }

      const radius = radiusForNode(node) + (cluster.kind === 'template-group' ? 20 : 10);
      minX = Math.min(minX, node.x - radius);
      minY = Math.min(minY, node.y - radius);
      maxX = Math.max(maxX, node.x + radius);
      maxY = Math.max(maxY, node.y + radius);
    }

    if (!Number.isFinite(minX) || !Number.isFinite(minY) || !Number.isFinite(maxX) || !Number.isFinite(maxY)) {
      continue;
    }

    const envelopeX = minX - (cluster.kind === 'template-group' ? padding : 12);
    const envelopeY = minY - (cluster.kind === 'template-group' ? padding + 14 : 10);
    const envelopeWidth = maxX - minX + (cluster.kind === 'template-group' ? padding * 2 : 24);
    const envelopeHeight = maxY - minY + (cluster.kind === 'template-group' ? padding * 2 + 14 : 20);
    const labelWidth =
      cluster.kind === 'template-group'
        ? Math.min(320, Math.max(160, 12 + cluster.label.length * 6))
        : Math.min(220, Math.max(110, 12 + cluster.label.length * 6));
    const labelInsetX = cluster.kind === 'template-group' ? 10 : 8;
    const labelGapY = cluster.kind === 'template-group' ? 8 : 6;

    envelopes.push({
      ...cluster,
      x: envelopeX,
      y: envelopeY,
      width: envelopeWidth,
      height: envelopeHeight,
      labelX: envelopeX + envelopeWidth - labelWidth - labelInsetX,
      labelY: envelopeY - cluster.labelHeight - labelGapY,
      labelWidth,
    });
  }

  return envelopes
    .filter((cluster) => cluster.kind === 'template-group' || cluster.nodeIds.length > 2)
    .sort((left, right) => {
      if (left.kind !== right.kind) {
        return left.kind === 'template-group' ? -1 : 1;
      }
      if (left.nodeIds.length !== right.nodeIds.length) {
        return right.nodeIds.length - left.nodeIds.length;
      }
      return left.label.localeCompare(right.label);
    });
}

export function buildDanglingTemplateMarkers<Node extends ClusterableNode>(
  nodes: Node[],
  visiblePrimaryClusterKeys: Set<string>,
) {
  const templateClusterMap = new Map<string, { nodeIds: string[]; label: string; parentKey: string }>();

  for (const node of nodes) {
    for (const template of node.templateTags) {
      if (!template.parentKey || !visiblePrimaryClusterKeys.has(template.parentKey)) {
        continue;
      }

      const id = `template:${template.parentKey}:${template.key}`;
      const cluster = templateClusterMap.get(id);
      if (cluster) {
        cluster.nodeIds.push(node.id);
        continue;
      }

      templateClusterMap.set(id, {
        nodeIds: [node.id],
        label: template.label,
        parentKey: template.parentKey,
      });
    }
  }

  const markers: DanglingTemplateMarker[] = [];

  for (const [clusterId, cluster] of templateClusterMap.entries()) {
    if (cluster.nodeIds.length > 2) {
      continue;
    }

    const templateKey = clusterId.split(':')[2] ?? clusterId;
    for (const nodeId of cluster.nodeIds) {
      markers.push({
        nodeId,
        templateKey,
        templateLabel: cluster.label,
        parentKey: cluster.parentKey,
      });
    }
  }

  return markers;
}
