import { getTemplatesPageData, type PatternTagOption, type TemplateCatalogSubmissionRow } from '../../lib/data';
import { isWriteAllowed } from '../../lib/access-control';
import { TemplateGroupsWorkbench } from '../template-groups-workbench';

const UNKNOWN_TIME = 'unknown';

type TemplateProblem = {
  id: string;
  title: string;
  attempts: number;
  latest: string;
};

type TemplateWithProblems = {
  template: PatternTagOption;
  problems: TemplateProblem[];
};

type TemplateCluster = {
  key: string;
  label: string;
  description: string | null;
  sortOrder: number;
  templates: TemplateWithProblems[];
};

export type TemplateGroupCatalog = TemplateCluster;

const FALLBACK_CLUSTER = {
  key: 'ungrouped-templates',
  label: 'Ungrouped templates',
  description: 'Templates without a parent template group.',
  sortOrder: Number.MAX_SAFE_INTEGER,
};

const DATE_FORMATTER = new Intl.DateTimeFormat('en-US', {
  timeZone: 'UTC',
  month: 'short',
  day: '2-digit',
  year: 'numeric',
});

function formatDate(value: string) {
  return DATE_FORMATTER.format(new Date(value));
}

function formatTitle(submission: TemplateCatalogSubmissionRow) {
  return submission.title ?? submission.titleSlug ?? 'Untitled problem';
}

function buildTemplateCatalog(tags: PatternTagOption[], submissions: TemplateCatalogSubmissionRow[]): TemplateGroupCatalog[] {
  const templateTags = tags.filter((tag) => tag.dimension === 'template');
  const templateGroups = templateTags.filter((tag) => tag.kind === 'template_group');
  const templateLeaves = templateTags.filter((tag) => tag.kind === 'tag');
  const clusters = new Map<string, TemplateCluster>();
  const fallbackClusterKey = FALLBACK_CLUSTER.key;

  function ensureCluster(key: string, label: string, description: string | null, sortOrder: number) {
    if (!clusters.has(key)) {
      clusters.set(key, {
        key,
        label,
        description,
        sortOrder,
        templates: [],
      });
    }
    return clusters.get(key)!;
  }

  for (const tag of templateGroups) {
    if (!tag.parentId) {
      ensureCluster(tag.id, tag.label, tag.description, tag.sortOrder);
    }
  }

  const templatesById = new Map<string, PatternTagOption>(templateLeaves.map((tag) => [tag.id, tag]));
  const problemsByTemplateId = new Map<string, Map<string, TemplateProblem>>();

  for (const submission of submissions) {
    const problemId = submission.titleSlug?.trim() || submission.id;
    const problemEntry = {
      id: problemId,
      title: formatTitle(submission),
      attempts: 1,
      latest: submission.createdAt,
    };

    const visitedTemplateIds = new Set<string>();

    for (const tag of submission.tags) {
      if (tag.dimension !== 'template' || tag.kind !== 'tag') {
        continue;
      }

      if (!templatesById.has(tag.id)) {
        continue;
      }

      if (visitedTemplateIds.has(tag.id)) {
        continue;
      }

      const templateProblems = problemsByTemplateId.get(tag.id) ?? new Map<string, TemplateProblem>();
      const current = templateProblems.get(problemId);
      templateProblems.set(problemId, {
        id: current?.id ?? problemEntry.id,
        title: current?.title ?? problemEntry.title,
        attempts: (current?.attempts ?? 0) + 1,
        latest: current && current.latest > submission.createdAt ? current.latest : submission.createdAt,
      });
      problemsByTemplateId.set(tag.id, templateProblems);
      visitedTemplateIds.add(tag.id);
    }
  }

  for (const tag of templateLeaves) {
    if (!tag.parentId || tag.id === tag.parentId) {
      continue;
    }

    const targetKey = clusters.has(tag.parentId)
      ? tag.parentId
      : fallbackClusterKey;

    const problemsByTemplate = problemsByTemplateId.get(tag.id);
    const problems = problemsByTemplate
      ? [...problemsByTemplate.values()].sort((left, right) => {
          if (right.attempts !== left.attempts) {
            return right.attempts - left.attempts;
          }

          return right.latest.localeCompare(left.latest);
        })
      : [];

    const cluster = ensureCluster(
      targetKey,
      targetKey === fallbackClusterKey ? FALLBACK_CLUSTER.label : clusters.get(tag.parentId)?.label ?? FALLBACK_CLUSTER.label,
      targetKey === fallbackClusterKey ? FALLBACK_CLUSTER.description : clusters.get(tag.parentId)?.description ?? null,
      targetKey === fallbackClusterKey ? FALLBACK_CLUSTER.sortOrder : clusters.get(tag.parentId)?.sortOrder ?? Number.MAX_SAFE_INTEGER,
    );

    cluster.templates.push({ template: tag, problems });
  }

  return [...clusters.values()]
    .map((cluster) => ({
      ...cluster,
      templates: cluster.templates
        .filter((template) => template.template.parentId)
        .sort((left, right) => {
          if (left.template.parentId && right.template.parentId && left.template.parentId === right.template.parentId) {
            return left.template.sortOrder - right.template.sortOrder;
          }

          return left.template.label.localeCompare(right.template.label);
        }),
    }))
    .filter((cluster) => cluster.key !== fallbackClusterKey || cluster.templates.length > 0)
    .sort((left, right) => {
      if (left.sortOrder !== right.sortOrder) {
        return left.sortOrder - right.sortOrder;
      }

      return left.label.localeCompare(right.label);
    });
}

export const dynamic = 'force-dynamic';

export default async function TemplatesPage() {
  const [{ tags, submissions }, canWrite] = await Promise.all([getTemplatesPageData(), isWriteAllowed()]);
  const clusters = buildTemplateCatalog(tags, submissions);

  return (
    <TemplateGroupsWorkbench clusters={clusters} canWrite={canWrite} />
  );
}
