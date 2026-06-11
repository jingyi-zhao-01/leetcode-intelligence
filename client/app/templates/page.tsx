import Link from 'next/link';
import { getTagWorkbenchData, type PatternTagOption, type SubmissionRow } from '../../lib/data';

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

const FALLBACK_CLUSTER = {
  key: 'ungrouped-templates',
  label: 'Ungrouped templates',
  description: 'Templates without a parent primary group.',
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

function formatTitle(submission: SubmissionRow) {
  return submission.title ?? submission.titleSlug ?? 'Untitled problem';
}

function buildTemplateCatalog(tags: PatternTagOption[], submissions: SubmissionRow[]) {
  const templateTags = tags.filter((tag) => tag.dimension === 'template');
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

  for (const tag of templateTags) {
    if (!tag.parentId) {
      ensureCluster(tag.id, tag.label, tag.description, tag.sortOrder);
      continue;
    }
  }

  const templatesById = new Map<string, PatternTagOption>(templateTags.map((tag) => [tag.id, tag]));
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
      if (tag.dimension !== 'template') {
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

  for (const tag of templateTags) {
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
    .filter((cluster) => cluster.templates.length > 0)
    .sort((left, right) => {
      if (left.sortOrder !== right.sortOrder) {
        return left.sortOrder - right.sortOrder;
      }

      return left.label.localeCompare(right.label);
    });
}

export const dynamic = 'force-dynamic';

export default async function TemplatesPage() {
  const { tags, submissions } = await getTagWorkbenchData();
  const clusters = buildTemplateCatalog(tags, submissions);

  return (
    <main className="template-builder-page">
      <header className="template-builder-header">
        <div>
          <p className="eyebrow">Template Builder</p>
          <h1>Primary Template Groups</h1>
        </div>
        <Link className="template-workbench-back" href="/submission-history">
          Back to submission workbench
        </Link>
      </header>

      {clusters.length ? (
        <section className="template-builder-grid">
          {clusters.map((cluster) => (
            <section className="template-builder-cluster" key={cluster.key}>
              <div className="template-cluster-heading">
                <p className="eyebrow">Primary cluster</p>
                <h2>{cluster.label}</h2>
                <p className="cluster-description">{cluster.description ?? 'Template group with reusable approach metadata.'}</p>
              </div>

              <div className="template-list">
                {cluster.templates.map((entry) => {
                  const complexityTime = entry.template.metadata?.defaultComplexity?.time ?? UNKNOWN_TIME;
                  const complexitySpace = entry.template.metadata?.defaultComplexity?.space ?? UNKNOWN_TIME;
                  const sourceClass = entry.template.source.replaceAll('_', '-');

                  return (
                    <article key={entry.template.id} className="template-builder-card">
                      <div className="template-card-head">
                        <div>
                          <h3>{entry.template.label}</h3>
                          <p>{entry.template.key}</p>
                        </div>
                        <span className={`template-source-tag source-${sourceClass}`}>{entry.template.source}</span>
                      </div>
                      {entry.template.description ? <p className="template-desc">{entry.template.description}</p> : null}

                      <p className="template-complexity">
                        Time {complexityTime} · Space {complexitySpace}
                      </p>

                      <div className="template-problem-list">
                        <p className="template-problem-title">
                          Associated problems ({entry.problems.length})
                        </p>
                        {entry.problems.length ? (
                          <ul>
                            {entry.problems.map((problem) => (
                              <li key={problem.id}>
                                <span>{problem.title}</span>
                                <small>
                                  {problem.attempts} attempt{problem.attempts === 1 ? '' : 's'} · latest {formatDate(problem.latest)}
                                </small>
                              </li>
                            ))}
                          </ul>
                        ) : (
                          <p className="template-empty-problem">No problems tagged yet.</p>
                        )}
                      </div>
                    </article>
                  );
                })}
              </div>
            </section>
          ))}
        </section>
      ) : (
        <p className="template-empty">No template data found. Seed templates first, then refresh this page.</p>
      )}
    </main>
  );
}
