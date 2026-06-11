'use client';

import { useRouter } from 'next/navigation';
import { useMemo, useState, useTransition } from 'react';
import {
  benchmarkSubmissionTemplates,
  createGeneratedTemplate,
  generateTemplateDraft,
  saveSubmissionTags,
} from './actions';
import type { PatternTagOption, SubmissionRow } from '../lib/data';
import type { TemplateBenchmarkResult, TemplateBenchmarkScore } from '../lib/template-analyzer';
import type { GeneratedTemplateDraft } from '../lib/template-generator';

type Props = {
  submissions: SubmissionRow[];
  tags: PatternTagOption[];
};

type TemplateForm = {
  key: string;
  label: string;
  description: string;
  classicProblems: string;
  whenToUse: string;
  whenNotToUse: string;
  signals: string;
  pseudocode: string;
  invariants: string;
  timeComplexity: string;
  spaceComplexity: string;
  relatedDataStructures: string;
  similarTemplates: string;
};

type TemplateGeneratorModal = {
  groupKey: string;
  groupLabel: string;
  prompt: string;
  model: string;
  form: TemplateForm;
  error?: string;
};

const DEFAULT_TEMPLATE_GENERATOR_MODEL = 'qwen/qwen3-coder-next';
const TEMPLATE_GENERATOR_MODELS = [
  'qwen/qwen3-coder-next',
  'deepseek/deepseek-chat-v3-0324',
  'openai/gpt-4.1-mini',
];

const TEMPLATE_FORM_ROWS: Array<{
  field: keyof TemplateForm;
  label: string;
  multiline?: boolean;
  placeholder?: string;
}> = [
  { field: 'key', label: 'Key', placeholder: 'canonical-template-key' },
  { field: 'label', label: 'Label', placeholder: 'Canonical Template Name' },
  { field: 'description', label: 'Description', multiline: true },
  { field: 'classicProblems', label: 'Classic Problems', multiline: true, placeholder: 'One item per line' },
  { field: 'whenToUse', label: 'When To Use', multiline: true, placeholder: 'One item per line' },
  { field: 'whenNotToUse', label: 'When Not To Use', multiline: true, placeholder: 'One item per line' },
  { field: 'signals', label: 'Signals', multiline: true, placeholder: 'One item per line' },
  { field: 'pseudocode', label: 'Pseudocode', multiline: true, placeholder: 'One line per pseudocode step' },
  { field: 'invariants', label: 'Invariants', multiline: true, placeholder: 'One item per line' },
  { field: 'timeComplexity', label: 'Time Complexity', placeholder: 'O(n)' },
  { field: 'spaceComplexity', label: 'Space Complexity', placeholder: 'O(1)' },
  { field: 'relatedDataStructures', label: 'Data Structures', multiline: true, placeholder: 'One item per line' },
  { field: 'similarTemplates', label: 'Similar Templates', multiline: true, placeholder: 'template-key per line' },
];

function formatDate(value: string) {
  return new Intl.DateTimeFormat('en', {
    month: 'short',
    day: '2-digit',
    hour: '2-digit',
    minute: '2-digit',
  }).format(new Date(value));
}

function groupTags(tags: PatternTagOption[]) {
  const groups = new Map<string, { label: string; tags: PatternTagOption[] }>();

  for (const tag of tags) {
    const key = tag.parentKey ?? tag.dimension;
    const label = tag.parentLabel ?? tag.dimension.replaceAll('_', ' ');
    const group = groups.get(key) ?? { label, tags: [] };
    group.tags.push(tag);
    groups.set(key, group);
  }

  return [...groups.entries()].map(([key, group]) => ({ key, ...group }));
}

function benchmarkTone(score: number) {
  if (score >= 85) return 'high';
  if (score >= 65) return 'medium';
  if (score >= 40) return 'low';
  return 'weak';
}

function sourceLabel(source: PatternTagOption['source']) {
  return source.replaceAll('_', ' ');
}

function emptyTemplateForm(): TemplateForm {
  return {
    key: '',
    label: '',
    description: '',
    classicProblems: '',
    whenToUse: '',
    whenNotToUse: '',
    signals: '',
    pseudocode: '',
    invariants: '',
    timeComplexity: '',
    spaceComplexity: '',
    relatedDataStructures: '',
    similarTemplates: '',
  };
}

function lines(value: string) {
  return value
    .split('\n')
    .map((entry) => entry.trim())
    .filter(Boolean);
}

function formFromDraft(draft: GeneratedTemplateDraft): TemplateForm {
  return {
    key: draft.key,
    label: draft.label,
    description: draft.description,
    classicProblems: draft.metadata.classicProblems.join('\n'),
    whenToUse: draft.metadata.whenToUse.join('\n'),
    whenNotToUse: draft.metadata.whenNotToUse.join('\n'),
    signals: draft.metadata.signals.join('\n'),
    pseudocode: draft.metadata.pseudocode.join('\n'),
    invariants: draft.metadata.invariants.join('\n'),
    timeComplexity: draft.metadata.defaultComplexity.time ?? '',
    spaceComplexity: draft.metadata.defaultComplexity.space ?? '',
    relatedDataStructures: draft.metadata.relatedDataStructures.join('\n'),
    similarTemplates: draft.metadata.similarTemplates.join('\n'),
  };
}

function draftFromForm(form: TemplateForm): GeneratedTemplateDraft {
  return {
    key: form.key.trim(),
    label: form.label.trim(),
    description: form.description.trim(),
    metadata: {
      classicProblems: lines(form.classicProblems),
      whenToUse: lines(form.whenToUse),
      whenNotToUse: lines(form.whenNotToUse),
      signals: lines(form.signals),
      pseudocode: lines(form.pseudocode),
      invariants: lines(form.invariants),
      defaultComplexity: {
        time: form.timeComplexity.trim(),
        space: form.spaceComplexity.trim(),
      },
      relatedDataStructures: lines(form.relatedDataStructures),
      similarTemplates: lines(form.similarTemplates),
    },
  };
}

function isTemplateFormComplete(form: TemplateForm) {
  return TEMPLATE_FORM_ROWS.every((row) => form[row.field].trim().length > 0);
}

function valueFromDraftField(draft: GeneratedTemplateDraft, field: keyof TemplateForm) {
  const form = formFromDraft(draft);
  return form[field];
}

export function TagWorkbench({ submissions, tags }: Props) {
  const router = useRouter();
  const [query, setQuery] = useState('');
  const [selectedId, setSelectedId] = useState(submissions[0]?.id ?? '');
  const [selectedTemplateId, setSelectedTemplateId] = useState(
    submissions[0]?.tags.find((tag) => tag.dimension === 'template')?.id ??
      tags.find((tag) => tag.metadata)?.id ??
      tags[0]?.id ??
      '',
  );
  const [draftTagIds, setDraftTagIds] = useState<Set<string>>(
    () => new Set(submissions[0]?.tags.map((tag) => tag.id) ?? []),
  );
  const [message, setMessage] = useState('');
  const [isPending, startTransition] = useTransition();
  const [isBenchmarkPending, startBenchmarkTransition] = useTransition();
  const [benchmarkError, setBenchmarkError] = useState('');
  const [benchmarksBySubmission, setBenchmarksBySubmission] = useState<Record<string, TemplateBenchmarkResult>>({});
  const [excludedBenchmarkGroupKeys, setExcludedBenchmarkGroupKeys] = useState<Set<string>>(() => new Set());
  const [isTemplateGenerationPending, startTemplateGenerationTransition] = useTransition();
  const [templateGeneratorModal, setTemplateGeneratorModal] = useState<TemplateGeneratorModal | null>(null);

  const selectedSubmission = submissions.find((submission) => submission.id === selectedId) ?? submissions[0] ?? null;
  const selectedTags = tags.filter((tag) => draftTagIds.has(tag.id));
  const selectedTemplate = tags.find((tag) => tag.id === selectedTemplateId) ?? tags[0] ?? null;
  const benchmark = selectedSubmission ? benchmarksBySubmission[selectedSubmission.id] : null;
  const scoreByTagId = useMemo(() => {
    return new Map(benchmark?.scores.map((score) => [score.patternTagId, score]) ?? []);
  }, [benchmark]);
  const selectedTemplateScore = selectedTemplate ? scoreByTagId.get(selectedTemplate.id) : null;

  const filteredSubmissions = useMemo(() => {
    const needle = query.trim().toLowerCase();
    return submissions.filter((submission) => {
      const haystack = [submission.titleSlug, submission.title, submission.status, submission.language]
        .filter(Boolean)
        .join(' ')
        .toLowerCase();
      return !needle || haystack.includes(needle);
    });
  }, [query, submissions]);

  const tagGroups = useMemo(() => groupTags(tags), [tags]);
  const includedBenchmarkGroupCount = tagGroups.length - excludedBenchmarkGroupKeys.size;

  function selectSubmission(submission: SubmissionRow) {
    setSelectedId(submission.id);
    setDraftTagIds(new Set(submission.tags.map((tag) => tag.id)));
    const firstTemplate = submission.tags.find((tag) => tag.dimension === 'template');
    if (firstTemplate) {
      setSelectedTemplateId(firstTemplate.id);
    }
    setMessage('');
    setBenchmarkError('');
  }

  function toggleTag(tagId: string) {
    setDraftTagIds((current) => {
      const next = new Set(current);
      if (next.has(tagId)) {
        next.delete(tagId);
      } else {
        next.add(tagId);
      }
      return next;
    });
  }

  function removeTag(tagId: string) {
    setDraftTagIds((current) => {
      const next = new Set(current);
      next.delete(tagId);
      return next;
    });
  }

  function saveSelectedSubmission() {
    if (!selectedSubmission) return;
    startTransition(async () => {
      await saveSubmissionTags(selectedSubmission.id, [...draftTagIds]);
      router.refresh();
      setMessage('Saved tags for this submission.');
    });
  }

  function clearTags() {
    if (!selectedSubmission) return;
    const shouldClear = window.confirm(
      'Clear all tags for this submission? This will remove the saved tag assignments from the database.',
    );

    if (!shouldClear) return;

    setDraftTagIds(new Set());
    startTransition(async () => {
      await saveSubmissionTags(selectedSubmission.id, []);
      router.refresh();
      setMessage('Cleared tags for this submission.');
    });
  }

  function toggleBenchmarkGroup(groupKey: string) {
    setExcludedBenchmarkGroupKeys((current) => {
      const next = new Set(current);
      if (next.has(groupKey)) {
        next.delete(groupKey);
      } else {
        next.add(groupKey);
      }
      return next;
    });
    setBenchmarkError('');
    if (selectedSubmission) {
      setBenchmarksBySubmission((current) => {
        const next = { ...current };
        delete next[selectedSubmission.id];
        return next;
      });
    }
  }

  function runTemplateBenchmark() {
    if (!selectedSubmission) return;

    setBenchmarkError('');
    startBenchmarkTransition(async () => {
      try {
        const result = await benchmarkSubmissionTemplates(selectedSubmission.id, [...excludedBenchmarkGroupKeys]);
        setBenchmarksBySubmission((current) => ({
          ...current,
          [selectedSubmission.id]: result,
        }));
      } catch (error) {
        setBenchmarkError(error instanceof Error ? error.message : 'Template benchmark failed.');
      }
    });
  }

  function openTemplateGenerator(group: { key: string; label: string }) {
    setTemplateGeneratorModal({
      groupKey: group.key,
      groupLabel: group.label,
      prompt: '',
      model: DEFAULT_TEMPLATE_GENERATOR_MODEL,
      form: emptyTemplateForm(),
    });
  }

  function updateTemplateGeneratorModal(patch: Partial<TemplateGeneratorModal>) {
    setTemplateGeneratorModal((current) => (current ? { ...current, ...patch } : current));
  }

  function updateTemplateForm(field: keyof TemplateForm, value: string) {
    setTemplateGeneratorModal((current) =>
      current
        ? {
            ...current,
            form: {
              ...current.form,
              [field]: value,
            },
          }
        : current,
    );
  }

  function runTemplateGenerator() {
    if (!selectedSubmission || !templateGeneratorModal) return;
    const modal = templateGeneratorModal;

    updateTemplateGeneratorModal({ error: undefined });
    startTemplateGenerationTransition(async () => {
      try {
        const result = await generateTemplateDraft({
          groupKey: modal.groupKey,
          submissionId: selectedSubmission.id,
          prompt: modal.prompt || `Generate one missing canonical template for ${modal.groupLabel}.`,
          model: modal.model || DEFAULT_TEMPLATE_GENERATOR_MODEL,
        });
        updateTemplateGeneratorModal({
          form: formFromDraft(result.draft),
          model: result.model,
          error: undefined,
        });
      } catch (error) {
        updateTemplateGeneratorModal({
          error: error instanceof Error ? error.message : 'Template generation failed.',
        });
      }
    });
  }

  function assistTemplateRow(field: keyof TemplateForm, label: string) {
    if (!selectedSubmission || !templateGeneratorModal) return;
    const modal = templateGeneratorModal;

    startTemplateGenerationTransition(async () => {
      try {
        const result = await generateTemplateDraft({
          groupKey: modal.groupKey,
          submissionId: selectedSubmission.id,
          prompt:
            modal.prompt ||
            `Fill the ${label} field for a new canonical template in ${modal.groupLabel}. Preserve the user's existing form intent when possible.`,
          model: modal.model || DEFAULT_TEMPLATE_GENERATOR_MODEL,
        });
        updateTemplateForm(field, valueFromDraftField(result.draft, field));
        updateTemplateGeneratorModal({ model: result.model, error: undefined });
      } catch (error) {
        updateTemplateGeneratorModal({
          error: error instanceof Error ? error.message : 'Template row assist failed.',
        });
      }
    });
  }

  function createTemplateFromModal() {
    if (!templateGeneratorModal || !isTemplateFormComplete(templateGeneratorModal.form)) return;
    const modal = templateGeneratorModal;

    startTemplateGenerationTransition(async () => {
      try {
        const template = await createGeneratedTemplate(modal.groupKey, draftFromForm(modal.form));
        setTemplateGeneratorModal(null);
        setSelectedTemplateId(template.id);
        setMessage(`Created LLM generated template: ${template.key}.`);
        router.refresh();
      } catch (error) {
        updateTemplateGeneratorModal({
          error: error instanceof Error ? error.message : 'Template creation failed.',
        });
      }
    });
  }

  return (
    <main className="workspace">
      <section className="sidebar">
        <div className="brand">
          <div>
            <p className="eyebrow">Pattern Tag Workbench</p>
            <h1>Submission taxonomy</h1>
          </div>
          <span>{submissions.length}</span>
        </div>

        <div className="filters">
          <input
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Search slug, title, language"
            aria-label="Search submissions"
          />
        </div>

        <div className="submission-list">
          {filteredSubmissions.map((submission) => (
            <button
              key={submission.id}
              className={submission.id === selectedSubmission?.id ? 'submission active' : 'submission'}
              onClick={() => selectSubmission(submission)}
            >
              <span className="submission-title">
                {submission.title ?? submission.titleSlug ?? 'Untitled submission'}
              </span>
              <span className="submission-meta">
                {submission.status} · {formatDate(submission.createdAt)}
              </span>
              <span className="tag-preview">
                {submission.tags.length ? submission.tags.map((tag) => tag.key).join(', ') : 'untagged'}
              </span>
            </button>
          ))}
        </div>
      </section>

      <section className="detail">
        {selectedSubmission ? (
          <>
            <div className="detail-header">
              <div>
                <p className="eyebrow">{selectedSubmission.titleSlug ?? 'no slug'}</p>
                <h2>{selectedSubmission.title ?? selectedSubmission.titleSlug ?? 'Submission'}</h2>
                <p className="detail-meta">
                  {selectedSubmission.status} · {selectedSubmission.difficulty ?? 'unknown difficulty'} ·{' '}
                  {selectedSubmission.language ?? 'unknown language'}
                </p>
              </div>
              <div className="complexity">
                <span>Time {selectedSubmission.timeComplexity ?? 'n/a'}</span>
                <span>Space {selectedSubmission.spaceComplexity ?? 'n/a'}</span>
              </div>
            </div>

            <div className="selected-tags">
              {selectedTags.length ? (
                selectedTags.map((tag) => (
                  <button key={tag.id} className="selected-tag" onClick={() => removeTag(tag.id)}>
                    <span>{tag.key}</span>
                    <small>Remove</small>
                  </button>
                ))
              ) : (
                <span className="untagged">untagged</span>
              )}
            </div>

            <div className="benchmark-status">
              {isBenchmarkPending ? <span>Benchmarking templates with LLM...</span> : null}
              {benchmark ? <span>Benchmark model: {benchmark.model}</span> : null}
              {excludedBenchmarkGroupKeys.size ? (
                <span>
                  Excluded groups: {excludedBenchmarkGroupKeys.size} · Included: {includedBenchmarkGroupCount}
                </span>
              ) : null}
              {benchmarkError ? <span className="error">{benchmarkError}</span> : null}
            </div>

            <SubmissionContext submission={selectedSubmission} />

            <div className="taxonomy-layout">
              <div className="tag-grid">
                {tagGroups.map((group) => (
                  <section
                    className={excludedBenchmarkGroupKeys.has(group.key) ? 'tag-group excluded' : 'tag-group'}
                    key={group.key}
                  >
                    <div className="tag-group-header">
                      <div>
                        <h3>{group.label}</h3>
                        {excludedBenchmarkGroupKeys.has(group.key) ? <small>Excluded from LLM benchmark</small> : null}
                      </div>
                      <button
                        className="exclude-group-button"
                        onClick={() => toggleBenchmarkGroup(group.key)}
                        type="button"
                        aria-pressed={excludedBenchmarkGroupKeys.has(group.key)}
                        aria-label={
                          excludedBenchmarkGroupKeys.has(group.key)
                            ? `Include ${group.label} in LLM benchmark`
                            : `Exclude ${group.label} from LLM benchmark`
                        }
                        title={
                          excludedBenchmarkGroupKeys.has(group.key)
                            ? 'Include this group in LLM benchmark'
                            : 'Exclude this group from LLM benchmark'
                        }
                      >
                        ×
                      </button>
                    </div>
                    <div className="tag-options">
                      {group.tags.map((tag) => {
                        const score = scoreByTagId.get(tag.id);
                        return (
                          <button
                            key={tag.id}
                            className={[
                              'tag-option',
                              draftTagIds.has(tag.id) ? 'selected' : '',
                              selectedTemplate?.id === tag.id ? 'focused' : '',
                              score ? `score-${benchmarkTone(score.score)}` : '',
                            ]
                              .filter(Boolean)
                              .join(' ')}
                            onClick={() => {
                              setSelectedTemplateId(tag.id);
                              toggleTag(tag.id);
                            }}
                            title={tag.description ?? tag.label}
                          >
                            {score ? <strong className="benchmark-score">{score.score}</strong> : null}
                            <span>{tag.label}</span>
                            <small>{tag.key}</small>
                            <strong className={`source-badge source-${tag.source}`}>{sourceLabel(tag.source)}</strong>
                            {tag.metadata ? <em>documented</em> : null}
                          </button>
                        );
                      })}
                      <button className="add-template-card" type="button" onClick={() => openTemplateGenerator(group)}>
                        <span>+</span>
                        <strong>Generate template</strong>
                        <small>{group.label}</small>
                      </button>
                    </div>
                  </section>
                ))}
              </div>

              {selectedTemplate ? (
                <TemplateControlPlane template={selectedTemplate} tags={tags} benchmarkScore={selectedTemplateScore} />
              ) : null}
            </div>

            {templateGeneratorModal ? (
              <TemplateGeneratorModal
                modal={templateGeneratorModal}
                isPending={isTemplateGenerationPending}
                isComplete={isTemplateFormComplete(templateGeneratorModal.form)}
                onClose={() => setTemplateGeneratorModal(null)}
                onChange={updateTemplateGeneratorModal}
                onChangeField={updateTemplateForm}
                onAssistAll={runTemplateGenerator}
                onAssistField={assistTemplateRow}
                onCreate={createTemplateFromModal}
              />
            ) : null}

            <div className="actions">
              <button className="primary" onClick={saveSelectedSubmission} disabled={isPending}>
                {isPending ? 'Saving...' : 'Save submission'}
              </button>
              <button onClick={runTemplateBenchmark} disabled={isBenchmarkPending || includedBenchmarkGroupCount <= 0}>
                {isBenchmarkPending ? 'Benchmarking...' : benchmark ? 'Rerun benchmark' : 'Benchmark templates'}
              </button>
              <button onClick={clearTags} disabled={isPending || draftTagIds.size === 0}>
                Clear tags
              </button>
              {message ? <p>{message}</p> : null}
            </div>
          </>
        ) : (
          <div className="empty">No submissions found.</div>
        )}
      </section>
    </main>
  );
}

function TemplateGeneratorModal({
  modal,
  isPending,
  isComplete,
  onClose,
  onChange,
  onChangeField,
  onAssistAll,
  onAssistField,
  onCreate,
}: {
  modal: TemplateGeneratorModal;
  isPending: boolean;
  isComplete: boolean;
  onClose: () => void;
  onChange: (patch: Partial<TemplateGeneratorModal>) => void;
  onChangeField: (field: keyof TemplateForm, value: string) => void;
  onAssistAll: () => void;
  onAssistField: (field: keyof TemplateForm, label: string) => void;
  onCreate: () => void;
}) {
  return (
    <div className="modal-backdrop" role="presentation">
      <section className="template-generator-modal" role="dialog" aria-modal="true" aria-labelledby="template-generator-title">
        <div className="modal-header">
          <div>
            <p className="eyebrow">Generate Template</p>
            <h2 id="template-generator-title">New canonical template</h2>
            <p>Group: {modal.groupLabel}</p>
          </div>
          <button type="button" className="modal-close" onClick={onClose} aria-label="Close template generator">
            ×
          </button>
        </div>

        <div className="modal-assist-bar">
          <label>
            <span>Model</span>
            <input
              list="template-generator-models"
              value={modal.model}
              onChange={(event) => onChange({ model: event.target.value })}
              placeholder={DEFAULT_TEMPLATE_GENERATOR_MODEL}
            />
          </label>
          <label>
            <span>Brief</span>
            <input
              value={modal.prompt}
              onChange={(event) => onChange({ prompt: event.target.value })}
              placeholder="e.g. generalize this submission into a reusable canonical template"
            />
          </label>
          <button type="button" onClick={onAssistAll} disabled={isPending}>
            {isPending ? 'Assisting...' : 'LLM assist all'}
          </button>
        </div>
        <datalist id="template-generator-models">
          {TEMPLATE_GENERATOR_MODELS.map((model) => (
            <option value={model} key={model} />
          ))}
        </datalist>

        <div className="template-form-grid">
          {TEMPLATE_FORM_ROWS.map((row) => (
            <div className={row.multiline ? 'template-form-row tall' : 'template-form-row'} key={row.field}>
              <label>
                <span>{row.label}</span>
                {row.multiline ? (
                  <textarea
                    value={modal.form[row.field]}
                    onChange={(event) => onChangeField(row.field, event.target.value)}
                    placeholder={row.placeholder}
                    rows={4}
                    required
                  />
                ) : (
                  <input
                    value={modal.form[row.field]}
                    onChange={(event) => onChangeField(row.field, event.target.value)}
                    placeholder={row.placeholder}
                    required
                  />
                )}
              </label>
              <button type="button" onClick={() => onAssistField(row.field, row.label)} disabled={isPending}>
                LLM assist
              </button>
            </div>
          ))}
        </div>

        {modal.error ? <p className="generator-error">{modal.error}</p> : null}

        <div className="modal-footer">
          <p>{isComplete ? 'Ready to create.' : 'Fill every row before creating this template.'}</p>
          <div>
            <button type="button" onClick={onClose}>
              Cancel
            </button>
            <button type="button" className="primary" onClick={onCreate} disabled={isPending || !isComplete}>
              Create template
            </button>
          </div>
        </div>
      </section>
    </div>
  );
}

function SubmissionContext({ submission }: { submission: SubmissionRow }) {
  return (
    <section className="submission-context">
      <details className="context-card" open>
        <summary>
          <span>Problem Description</span>
          <small>{submission.titleSlug ?? 'question'}</small>
        </summary>
        {submission.questionDescription ? (
          <pre className="problem-description">{submission.questionDescription}</pre>
        ) : (
          <p className="context-empty">No question description found for this submission.</p>
        )}
      </details>

      <details className="context-card code-context" open>
        <summary>
          <span>Submission Code</span>
          <small>{submission.language ?? 'code'}</small>
        </summary>
        <pre className="submission-code">
          <code>{submission.submissionCode || 'No submission code found.'}</code>
        </pre>
      </details>
    </section>
  );
}

function TemplateControlPlane({
  template,
  tags,
  benchmarkScore,
}: {
  template: PatternTagOption;
  tags: PatternTagOption[];
  benchmarkScore?: TemplateBenchmarkScore | null;
}) {
  const metadata = template.metadata;
  const similarTemplates = metadata?.similarTemplates
    ?.map((key) => tags.find((tag) => tag.key === key))
    .filter((tag): tag is PatternTagOption => Boolean(tag));

  return (
    <aside className="template-plane">
      <div className="template-plane-header">
        <div>
          <p className="eyebrow">Template Control Plane</p>
          <h2>{template.label}</h2>
          <div className="template-identity">
            <p>{template.key}</p>
            <strong className={`source-badge source-${template.source}`}>{sourceLabel(template.source)}</strong>
          </div>
        </div>
        {metadata?.defaultComplexity ? (
          <div className="plane-complexity">
            <span>Time {metadata.defaultComplexity.time ?? 'n/a'}</span>
            <span>Space {metadata.defaultComplexity.space ?? 'n/a'}</span>
            {benchmarkScore ? (
              <span className={`plane-score ${benchmarkTone(benchmarkScore.score)}`}>{benchmarkScore.score}</span>
            ) : null}
          </div>
        ) : null}
      </div>

      {template.description ? <p className="template-description">{template.description}</p> : null}

      {metadata ? (
        <div className="template-plane-grid">
          {benchmarkScore ? (
            <section className="template-card wide benchmark-card">
              <h3>LLM Benchmark</h3>
              <p>
                Score {benchmarkScore.score}/100 · Confidence {benchmarkScore.confidence}/100
              </p>
              {benchmarkScore.reason ? <p>{benchmarkScore.reason}</p> : null}
              {benchmarkScore.evidence.length ? (
                <ul>
                  {benchmarkScore.evidence.map((item) => (
                    <li key={item}>{item}</li>
                  ))}
                </ul>
              ) : null}
            </section>
          ) : null}
          <TemplateList title="Classic Problems" items={metadata.classicProblems} compact />
          <TemplateList title="When To Use" items={metadata.whenToUse} />
          <TemplateList title="When Not To Use" items={metadata.whenNotToUse} />
          <TemplateList title="Signals" items={metadata.signals} compact />
          <TemplateList title="Invariants" items={metadata.invariants} />
          {metadata.pseudocode?.length ? (
            <section className="template-card wide">
              <h3>Pseudocode</h3>
              <pre>{metadata.pseudocode.join('\n')}</pre>
            </section>
          ) : null}
          <TemplateList title="Data Structures" items={metadata.relatedDataStructures} compact />
          {similarTemplates?.length ? (
            <section className="template-card">
              <h3>Similar Templates</h3>
              <div className="related-tags">
                {similarTemplates.map((tag) => (
                  <span key={tag.id}>{tag.key}</span>
                ))}
              </div>
            </section>
          ) : null}
        </div>
      ) : (
        <div className="template-card wide">
          <h3>No metadata yet</h3>
          <p>This template exists in the controlled tag set, but its control-plane details have not been seeded yet.</p>
        </div>
      )}
    </aside>
  );
}

function TemplateList({ title, items, compact = false }: { title: string; items?: string[]; compact?: boolean }) {
  if (!items?.length) {
    return null;
  }

  return (
    <section className={compact ? 'template-card compact' : 'template-card'}>
      <h3>{title}</h3>
      <ul>
        {items.map((item) => (
          <li key={item}>{item}</li>
        ))}
      </ul>
    </section>
  );
}
