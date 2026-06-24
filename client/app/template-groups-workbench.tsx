'use client';

import { useRouter } from 'next/navigation';
import { useMemo, useState, useTransition } from 'react';
import { createTemplateGroup, moveTemplateToGroup } from './actions';
import { Spinner } from './components/spinner';
import { Button } from './components/ui/button';
import { Input } from './components/ui/input';
import { Label } from './components/ui/label';
import { Textarea } from './components/ui/textarea';
import type { TemplateGroupCatalog } from '../lib/template-catalog';

const UNKNOWN_TIME = 'unknown';
const GROUP_TONES = ['teal', 'blue', 'amber', 'purple', 'green'] as const;

function AsyncLabel({ isPending, idle, pending }: { isPending: boolean; idle: string; pending: string }) {
  if (!isPending) {
    return <>{idle}</>;
  }

  return (
    <span className="loading-inline">
      <Spinner size="small" />
      <span>{pending}</span>
    </span>
  );
}

export function TemplateGroupsWorkbench({
  clusters,
  canWrite,
}: {
  clusters: TemplateGroupCatalog[];
  canWrite: boolean;
}) {
  const router = useRouter();
  const [isCreateModalOpen, setIsCreateModalOpen] = useState(false);
  const [groupLabel, setGroupLabel] = useState('');
  const [groupKey, setGroupKey] = useState('');
  const [groupDescription, setGroupDescription] = useState('');
  const [message, setMessage] = useState('');
  const [draggingTemplateId, setDraggingTemplateId] = useState<string | null>(null);
  const [draggingTemplateLabel, setDraggingTemplateLabel] = useState<string | null>(null);
  const [dropTargetGroupKey, setDropTargetGroupKey] = useState<string | null>(null);
  const [isCreatePending, startCreateTransition] = useTransition();
  const [isMovePending, startMoveTransition] = useTransition();

  const groupByKey = useMemo(() => new Map(clusters.map((cluster) => [cluster.id, cluster])), [clusters]);

  function resetCreateForm() {
    setGroupLabel('');
    setGroupKey('');
    setGroupDescription('');
  }

  function openCreateModal() {
    if (!canWrite) return;
    setMessage('');
    setIsCreateModalOpen(true);
  }

  function openTemplateGenerationHint(groupLabel: string) {
    setMessage(
      `To generate a new template for ${groupLabel}, open Submission Taxonomy, select a representative submission, then use Generate template in that template group.`,
    );
  }

  function closeCreateModal() {
    if (isCreatePending) return;
    setIsCreateModalOpen(false);
    resetCreateForm();
  }

  function submitCreateGroup() {
    if (!canWrite) return;
    if (!groupLabel.trim()) {
      setMessage('Template group label is required.');
      return;
    }

    setMessage('');
    startCreateTransition(async () => {
      try {
        const group = await createTemplateGroup({
          label: groupLabel,
          key: groupKey,
          description: groupDescription,
        });
        resetCreateForm();
        setIsCreateModalOpen(false);
        setMessage(`Created template group: ${group.label}.`);
        router.refresh();
      } catch (error) {
        setMessage(error instanceof Error ? error.message : 'Unable to create template group.');
      }
    });
  }

  function beginDrag(templateId: string, templateLabel: string) {
    if (!canWrite) return;
    setDraggingTemplateId(templateId);
    setDraggingTemplateLabel(templateLabel);
    setMessage('');
  }

  function clearDragState() {
    setDraggingTemplateId(null);
    setDraggingTemplateLabel(null);
    setDropTargetGroupKey(null);
  }

  function handleDrop(targetGroupKey: string) {
    if (!canWrite || !draggingTemplateId) return;

    const targetGroup = groupByKey.get(targetGroupKey);
    if (!targetGroup) {
      clearDragState();
      return;
    }

    const shouldMove = window.confirm(
      `Move "${draggingTemplateLabel ?? 'this template'}" into template group "${targetGroup.label}"?`,
    );

    if (!shouldMove) {
      clearDragState();
      return;
    }

    setMessage('');
    startMoveTransition(async () => {
      try {
        const result = await moveTemplateToGroup({
          templateId: draggingTemplateId,
          targetGroupId: targetGroupKey,
        });

        if (result.status === 'moved') {
          setMessage(`Moved ${result.template.label} to ${result.group.label}.`);
        } else if (result.status === 'unchanged') {
          setMessage(`${result.template.label} is already in ${result.group.label}.`);
        } else if (result.status === 'invalid_target_group') {
          setMessage('That drop target is not a valid template group.');
        } else {
          setMessage('That template could not be moved.');
        }

        router.refresh();
      } catch (error) {
        setMessage(error instanceof Error ? error.message : 'Unable to move template.');
      } finally {
        clearDragState();
      }
    });
  }

  return (
    <main className="template-builder-page">
      <header className="template-builder-header">
        <div>
          <h1>Template Group Builder</h1>
          <p className="template-builder-stats">
            {clusters.length} groups · {clusters.reduce((count, cluster) => count + cluster.templates.length, 0)}{' '}
            templates
          </p>
        </div>
        <div className="template-builder-actions">
          {canWrite ? (
            <Button type="button" size="sm" className="template-workbench-primary" onClick={openCreateModal}>
              + New template group
            </Button>
          ) : (
            <span className="template-builder-readonly">Read-only</span>
          )}
        </div>
      </header>

      {message ? <p className="template-builder-message">{message}</p> : null}
      {isMovePending ? (
        <p className="template-builder-message">
          <AsyncLabel isPending={true} idle="" pending="Moving template..." />
        </p>
      ) : null}

      {clusters.length ? (
        <section className="template-builder-grid template-builder-board">
          {clusters.map((cluster, clusterIndex) => {
            const tone = GROUP_TONES[clusterIndex % GROUP_TONES.length];
            const associatedProblems = [
              ...new Map(
                cluster.templates.flatMap((entry) => entry.problems).map((problem) => [problem.id, problem]),
              ).values(),
            ]
              .sort((left, right) => {
                if (right.attempts !== left.attempts) {
                  return right.attempts - left.attempts;
                }

                return right.latest.localeCompare(left.latest);
              })
              .slice(0, 5);

            return (
              <section
                className={[
                  'template-builder-cluster',
                  `template-builder-cluster-${tone}`,
                  canWrite ? 'template-builder-cluster-droppable' : '',
                  dropTargetGroupKey === cluster.id ? 'drop-target-active' : '',
                ]
                  .filter(Boolean)
                  .join(' ')}
                key={cluster.id}
                onDragOver={(event) => {
                  if (!canWrite || !draggingTemplateId) return;
                  event.preventDefault();
                  setDropTargetGroupKey(cluster.id);
                }}
                onDragEnter={(event) => {
                  if (!canWrite || !draggingTemplateId) return;
                  event.preventDefault();
                  setDropTargetGroupKey(cluster.id);
                }}
                onDragLeave={(event) => {
                  if (!canWrite) return;
                  const nextTarget = event.relatedTarget;
                  if (nextTarget instanceof Node && event.currentTarget.contains(nextTarget)) {
                    return;
                  }
                  setDropTargetGroupKey((current) => (current === cluster.id ? null : current));
                }}
                onDrop={(event) => {
                  if (!canWrite || !draggingTemplateId) return;
                  event.preventDefault();
                  handleDrop(cluster.id);
                }}
              >
                <div className="template-cluster-heading">
                  <div>
                    <span className="template-cluster-dot" aria-hidden="true" />
                    <h2>{cluster.label}</h2>
                    <span className="template-cluster-count">{cluster.templates.length}</span>
                  </div>
                  <span className="template-cluster-chevron" aria-hidden="true">
                    ⌄
                  </span>
                </div>

                {canWrite ? (
                  <p className="template-drop-hint">
                    {dropTargetGroupKey === cluster.id && draggingTemplateLabel
                      ? `Release to move ${draggingTemplateLabel} here`
                      : 'Drag a template card here to reorganize this group'}
                  </p>
                ) : null}

                <div className="template-directory" id={`template-directory-${cluster.id}`}>
                  {cluster.templates.map((entry) => {
                    const complexityTime = entry.template.metadata?.defaultComplexity?.time ?? UNKNOWN_TIME;
                    const complexitySpace = entry.template.metadata?.defaultComplexity?.space ?? UNKNOWN_TIME;
                    const sourceClass = entry.template.source.replaceAll('_', '-');

                    return (
                      <article
                        key={entry.template.id}
                        className={[
                          'template-directory-item',
                          canWrite ? 'template-directory-item-draggable' : '',
                          draggingTemplateId === entry.template.id ? 'dragging-template-card' : '',
                        ]
                          .filter(Boolean)
                          .join(' ')}
                        draggable={canWrite}
                        onDragStart={(event) => {
                          beginDrag(entry.template.id, entry.template.label);
                          event.dataTransfer.effectAllowed = 'move';
                          event.dataTransfer.setData('text/plain', entry.template.id);
                        }}
                        onDragEnd={clearDragState}
                      >
                        <div className="template-directory-item-header">
                          <div className="template-directory-item-heading">
                            <h3>{entry.template.label}</h3>
                            <p>{entry.template.key}</p>
                          </div>
                        </div>
                        <div className="template-directory-item-meta">
                          <span className={`template-source-tag source-${sourceClass}`}>
                            {entry.template.source === 'seeded' ? 'seeded' : entry.template.source.replaceAll('_', ' ')}
                          </span>
                          <span
                            className={`template-doc-state ${entry.template.metadata ? 'documented' : 'undocumented'}`}
                          >
                            {entry.template.metadata ? 'Documented' : 'Needs docs'}
                          </span>
                        </div>
                        <p className="template-complexity">
                          <span>Time {complexityTime}</span>
                          <span>Space {complexitySpace}</span>
                          <strong>{entry.template.assignmentCount || entry.problems.length || 0} uses</strong>
                          <span>{entry.problems.length} probs</span>
                        </p>
                        <div className="template-card-accent" aria-hidden="true" />
                      </article>
                    );
                  })}

                  {canWrite ? (
                    <button
                      className="template-directory-create"
                      type="button"
                      onClick={() => openTemplateGenerationHint(cluster.label)}
                    >
                      <span className="template-create-icon">+</span>
                      <div>
                        <strong>Generate template</strong>
                        <small>{cluster.label}</small>
                      </div>
                    </button>
                  ) : null}
                </div>

                <div className="template-associated-problems">
                  <h3>Associated Problems</h3>
                  {associatedProblems.length ? (
                    <ul>
                      {associatedProblems.map((problem) => (
                        <li key={problem.id}>
                          <span aria-hidden="true" />
                          <p>{problem.title}</p>
                        </li>
                      ))}
                    </ul>
                  ) : (
                    <p className="template-empty-problem">No associated problems yet.</p>
                  )}
                </div>
              </section>
            );
          })}
        </section>
      ) : (
        <p className="template-empty">No template data found. Seed templates first, then refresh this page.</p>
      )}

      {isCreateModalOpen ? (
        <div className="modal-backdrop" role="presentation">
          <section
            className="template-group-modal"
            role="dialog"
            aria-modal="true"
            aria-labelledby="template-group-modal-title"
          >
            <div className="modal-header">
              <div>
                <p className="eyebrow">Template Group</p>
                <h2 id="template-group-modal-title">Create new template group</h2>
              </div>
              <Button
                type="button"
                variant="ghost"
                size="icon"
                className="modal-close"
                onClick={closeCreateModal}
                aria-label="Close create template group modal"
              >
                ×
              </Button>
            </div>

            <div className="template-group-form-grid">
              <Label>
                <span>Label</span>
                <Input
                  value={groupLabel}
                  onChange={(event) => setGroupLabel(event.target.value)}
                  placeholder="e.g. Interval scheduling and greedy"
                />
              </Label>
              <Label>
                <span>Key</span>
                <Input
                  value={groupKey}
                  onChange={(event) => setGroupKey(event.target.value)}
                  placeholder="Optional; auto-slugged from label"
                />
              </Label>
              <Label className="template-group-form-tall">
                <span>Description</span>
                <Textarea
                  value={groupDescription}
                  onChange={(event) => setGroupDescription(event.target.value)}
                  placeholder="Describe the canonical family this group should hold."
                  rows={4}
                />
              </Label>
            </div>

            <div className="template-group-modal-actions">
              <Button type="button" variant="outline" onClick={closeCreateModal} disabled={isCreatePending}>
                Cancel
              </Button>
              <Button type="button" className="primary" onClick={submitCreateGroup} disabled={isCreatePending}>
                <AsyncLabel isPending={isCreatePending} idle="Create template group" pending="Creating..." />
              </Button>
            </div>
          </section>
        </div>
      ) : null}
    </main>
  );
}
