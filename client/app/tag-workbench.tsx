'use client';

import { usePathname, useRouter, useSearchParams } from 'next/navigation';
import Link from 'next/link';
import { useEffect, useMemo, useRef, useState, useTransition } from 'react';
import {
  benchmarkSubmissionTemplates,
  createGeneratedTemplate,
  deleteNonSeededTemplate,
  generateTemplateDraft,
  logoutAdmin,
  setSubmissionTemplateOptOut,
  saveSubmissionTags,
} from './actions';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { oneDark } from 'react-syntax-highlighter/dist/esm/styles/prism';
import type { PatternTagOption, SubmissionRow } from '../lib/data';
import type { TemplateBenchmarkResult, TemplateBenchmarkScore } from '../lib/template-analyzer';
import type { GeneratedTemplateDraft } from '../lib/template-generator';
import { Spinner } from './components/spinner';
import { PendingSubmitButton } from './components/pending-submit-button';

type Props = {
  submissions: SubmissionRow[];
  tags: PatternTagOption[];
  canWrite: boolean;
};

type SubmissionProblemGroup = {
  key: string;
  title: string;
  titleSlug: string | null;
  submissions: SubmissionRow[];
};

type SubmissionDayGroup = {
  key: string;
  label: string;
  dayStart: Date;
  problems: SubmissionProblemGroup[];
};

type LeftPanelFeatureKey = 'submission-history' | 'insights' | 'graph';

type LeftPanelFeature = {
  key: LeftPanelFeatureKey;
  label: string;
  description: string;
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

type DeleteTemplateBlocker = {
  tag: { key: string; label: string };
  assignmentCount: number;
  submissions: Array<{
    id: string;
    titleSlug: string | null;
    status: string;
    createdAt: string;
  }>;
};

type SubmissionHistoryPanelProps = {
  query: string;
  setQuery: (value: string) => void;
  filteredDays: SubmissionDayGroup[];
  selectedSubmission: SubmissionRow | null;
  collapsedDayKeys: Set<string>;
  onToggleDay: (dayKey: string) => void;
  onSelectSubmission: (submission: SubmissionRow) => void;
};

type LeftPanelGraphModuleProps = {
  selectedSubmission: SubmissionRow | null;
  onOpenGraph: () => void;
};

type LeftPanelInsightsProps = {
  selectedSubmission: SubmissionRow | null;
  submissionCount: number;
  tags: PatternTagOption[];
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

const LEFT_PANEL_FEATURES: LeftPanelFeature[] = [
  {
    key: 'submission-history',
    label: 'Submission History',
    description: 'Browse attempts, group by day, and select a submission.',
  },
  {
    key: 'insights',
    label: 'Insights',
    description: 'Future work area for stats, review, and learning metrics.',
  },
  {
    key: 'graph',
    label: 'Graph',
    description: 'Quick access to the graph explorer and relationship drills.',
  },
];

const DATE_TIME_FORMATTER = new Intl.DateTimeFormat('en-US', {
  timeZone: 'UTC',
  month: 'short',
  day: '2-digit',
  hour: '2-digit',
  minute: '2-digit',
});

const WEEK_FORMATTER = new Intl.DateTimeFormat('en-US', {
  timeZone: 'UTC',
  month: 'short',
  day: '2-digit',
  year: 'numeric',
});

function formatDate(value: string) {
  return DATE_TIME_FORMATTER.format(new Date(value));
}

function formatDayLabel(value: Date) {
  return WEEK_FORMATTER.format(value);
}

function startOfDayUTC(value: Date) {
  const dayStart = new Date(value);
  dayStart.setUTCHours(0, 0, 0, 0);
  return dayStart;
}

function getProblemKey(submission: SubmissionRow) {
  return submission.titleSlug ?? submission.title ?? submission.id;
}

function getProblemTitle(submission: SubmissionRow) {
  return submission.title ?? submission.titleSlug ?? 'Untitled submission';
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

function dimensionClass(dimension: string) {
  return `dimension-${dimension}`;
}

function AsyncButtonLabel({
  isPending,
  label,
  pendingLabel,
}: {
  isPending: boolean;
  label: string;
  pendingLabel: string;
}) {
  if (isPending) {
    return (
      <span className="loading-inline">
        <Spinner size="small" />
        <span>{pendingLabel}</span>
      </span>
    );
  }

  return <>{label}</>;
}

function submissionTaxonomyState(submission: SubmissionRow) {
  const hasTemplate = submission.tags.some((tag) => tag.dimension === 'template');
  const hasDataStructure = submission.tags.some((tag) => tag.dimension === 'data_structure');

  if (!hasTemplate && !hasDataStructure) {
    return 'none';
  }

  if (hasTemplate && hasDataStructure) {
    return 'complete';
  }

  return 'partial';
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

export function TagWorkbench({ submissions, tags, canWrite }: Props) {
  const router = useRouter();
  const pathname = usePathname();
  const searchParams = useSearchParams();
  const [query, setQuery] = useState('');
  const [selectedId, setSelectedId] = useState(submissions[0]?.id ?? '');
  const [selectedTemplateId, setSelectedTemplateId] = useState<string | null>(submissions[0]?.tags[0]?.id ?? null);
  const [templateBenchmarkOptOut, setTemplateBenchmarkOptOut] = useState(submissions[0]?.templateBenchmarkOptOut ?? false);
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
  const [isDeleteTemplatePending, startDeleteTemplateTransition] = useTransition();
  const [templateGeneratorModal, setTemplateGeneratorModal] = useState<TemplateGeneratorModal | null>(null);
  const [deleteTemplateBlocker, setDeleteTemplateBlocker] = useState<DeleteTemplateBlocker | null>(null);
  const [collapsedDayKeys, setCollapsedDayKeys] = useState<Set<string>>(() => new Set());
  const [leftPanelFeature, setLeftPanelFeature] = useState<LeftPanelFeatureKey>('submission-history');
  const hasInitializedDayCollapse = useRef(false);
  const returnTo = useMemo(() => {
    const query = searchParams.toString();
    const current = query ? `${pathname}?${query}` : pathname;
    return current || '/';
  }, [pathname, searchParams]);

  const selectedSubmission = submissions.find((submission) => submission.id === selectedId) ?? submissions[0] ?? null;
  const selectedTags = tags.filter((tag) => draftTagIds.has(tag.id));
  const selectedTemplate = selectedTemplateId ? tags.find((tag) => tag.id === selectedTemplateId) ?? null : null;
  const benchmark = selectedSubmission ? benchmarksBySubmission[selectedSubmission.id] : null;
  const scoreByTagId = useMemo(() => {
    return new Map(benchmark?.scores.map((score) => [score.patternTagId, score]) ?? []);
  }, [benchmark]);
  const selectedTemplateScore = selectedTemplate ? scoreByTagId.get(selectedTemplate.id) : null;
  const filteredSubmissionDays = useMemo(() => {
    const needle = query.trim().toLowerCase();
    const filtered = submissions.filter((submission) => {
      const haystack = [submission.titleSlug, submission.title, submission.status, submission.language]
        .filter(Boolean)
        .join(' ')
        .toLowerCase();
      return !needle || haystack.includes(needle);
    });
    const sorted = [...filtered].sort(
      (left, right) => new Date(right.createdAt).getTime() - new Date(left.createdAt).getTime(),
    );

    const days = new Map<
      string,
      {
        dayStart: Date;
        problems: Map<string, SubmissionProblemGroup>;
      }
    >();

    for (const submission of sorted) {
      const dayStart = startOfDayUTC(new Date(submission.createdAt));
      const dayKey = dayStart.toISOString();
      const day = days.get(dayKey) ?? { dayStart, problems: new Map<string, SubmissionProblemGroup>() };
      const problemKey = getProblemKey(submission);
      const problem = day.problems.get(problemKey) ?? {
        key: problemKey,
        title: getProblemTitle(submission),
        titleSlug: submission.titleSlug,
        submissions: [],
      };

      problem.submissions.push(submission);
      day.problems.set(problemKey, problem);
      days.set(dayKey, day);
    }

    return [...days.entries()]
      .sort((left, right) => right[1].dayStart.getTime() - left[1].dayStart.getTime())
      .map(([dayKey, day]) => ({
        key: dayKey,
        dayStart: day.dayStart,
        label: formatDayLabel(day.dayStart),
        problems: [...day.problems.values()].sort(
          (left, right) =>
            new Date(right.submissions[0]?.createdAt ?? 0).getTime() -
            new Date(left.submissions[0]?.createdAt ?? 0).getTime(),
        ),
      }));
  }, [query, submissions]);

  const tagGroups = useMemo(() => groupTags(tags), [tags]);
  const benchmarkableGroupCount = tagGroups.filter((group) =>
    group.tags.some((tag) => tag.dimension === 'template'),
  ).length;
  const includedBenchmarkGroupCount = benchmarkableGroupCount - excludedBenchmarkGroupKeys.size;
  const defaultCollapsedDayKeys = useMemo(
    () => new Set(filteredSubmissionDays.slice(2).map((day) => day.key)),
    [filteredSubmissionDays],
  );

  useEffect(() => {
    setTemplateBenchmarkOptOut(selectedSubmission?.templateBenchmarkOptOut ?? false);
  }, [selectedSubmission?.id, selectedSubmission?.templateBenchmarkOptOut]);

  useEffect(() => {
    if (hasInitializedDayCollapse.current) return;
    if (!filteredSubmissionDays.length) return;
    setCollapsedDayKeys(defaultCollapsedDayKeys);
    hasInitializedDayCollapse.current = true;
  }, [defaultCollapsedDayKeys, filteredSubmissionDays.length]);

  function selectSubmission(submission: SubmissionRow) {
    setSelectedId(submission.id);
    setTemplateBenchmarkOptOut(submission.templateBenchmarkOptOut);
    setDraftTagIds(new Set(submission.tags.map((tag) => tag.id)));
    setSelectedTemplateId(submission.tags[0]?.id ?? null);
    setMessage('');
    setBenchmarkError('');
  }

  function toggleDayCollapsed(dayKey: string) {
    setCollapsedDayKeys((current) => {
      const next = new Set(current);
      if (next.has(dayKey)) {
        next.delete(dayKey);
      } else {
        next.add(dayKey);
      }
      return next;
    });
  }

  function openGraphView() {
    const selectedSlug = selectedSubmission?.titleSlug?.toLowerCase() ?? null;
    router.push(selectedSlug ? `/graph?slug=${encodeURIComponent(selectedSlug)}` : '/graph');
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
    if (!canWrite) {
      setMessage('Read-only mode. Please sign in to save tags.');
      return;
    }
    if (!selectedSubmission) return;
    startTransition(async () => {
      await saveSubmissionTags(selectedSubmission.id, [...draftTagIds]);
      router.refresh();
      setMessage('Saved tags for this submission.');
    });
  }

  function clearTags() {
    if (!canWrite) {
      setMessage('Read-only mode. Please sign in to clear tags.');
      return;
    }
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
    if (!canWrite) {
      setBenchmarkError('Read-only mode. Please sign in to run benchmark.');
      return;
    }
    if (!selectedSubmission) return;
    if (templateBenchmarkOptOut) {
      setBenchmarkError('This submission is opted out from templating. Turn off opt-out to run benchmark.');
      return;
    }

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
    if (!canWrite) return;
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
    if (!canWrite) return;
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
    if (!canWrite) return;
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
    if (!canWrite) return;
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

  function deleteTemplate(tag: PatternTagOption) {
    if (!canWrite) return;
    if (isDeleteTemplatePending) return;
    if (tag.source === 'seeded' || tag.dimension !== 'template') return;
    const shouldDelete = window.confirm(`Delete template "${tag.label}"? This is only allowed when no submissions use it.`);
    if (!shouldDelete) return;

    startDeleteTemplateTransition(async () => {
      const result = await deleteNonSeededTemplate(tag.id);
      if (result.status === 'blocked') {
        setDeleteTemplateBlocker({
          tag: result.tag,
          assignmentCount: result.assignmentCount,
          submissions: result.submissions,
        });
        return;
      }

      if (result.status === 'deleted') {
        setMessage(`Deleted template: ${result.key}.`);
        if (selectedTemplateId === tag.id) {
          setSelectedTemplateId(tags.find((candidate) => candidate.id !== tag.id)?.id ?? null);
        }
        router.refresh();
        return;
      }

      setMessage('This template cannot be deleted.');
    });
  }

  function toggleTemplateBenchmarkOptOut(next: boolean) {
    if (!canWrite) {
      setMessage('Read-only mode. Please sign in to change opt-out settings.');
      return;
    }
    if (!selectedSubmission) return;
    if (isPending) return;

    setTemplateBenchmarkOptOut(next);
    setMessage('');
    setBenchmarkError('');
    setBenchmarksBySubmission((current) => {
      const nextBenchmarks = { ...current };
      delete nextBenchmarks[selectedSubmission.id];
      return nextBenchmarks;
    });
    startTransition(async () => {
      const result = await setSubmissionTemplateOptOut(selectedSubmission.id, next);
      if (result.status === 'not_found') {
        setTemplateBenchmarkOptOut(selectedSubmission.templateBenchmarkOptOut);
        setMessage('Unable to update because this submission is no longer accepted.');
        return;
      }

      setMessage(next ? 'Opted out from templating for this submission.' : 'Included this submission in templating again.');
      router.refresh();
    });
  }

  return (
    <main className="workspace">
      <button className="floating-view-toggle" type="button" onClick={openGraphView}>
        Graph view
      </button>

      <section className="sidebar">
        <div className="brand">
          <div>
            <p className="eyebrow">Pattern Tag Workbench</p>
            <h1>Submission taxonomy</h1>
          </div>
          <div className="admin-access">
            {canWrite ? (
              <form action={logoutAdmin}>
                <PendingSubmitButton className="admin-control-button" pendingText="Signing out...">
                  Sign out
                </PendingSubmitButton>
              </form>
            ) : (
              <Link className="admin-control-button" href={`/admin/login?returnTo=${encodeURIComponent(returnTo)}`}>
                Sign in
              </Link>
            )}
            <span className={`write-badge ${canWrite ? 'write-enabled' : 'write-disabled'}`}>
              {canWrite ? 'Write enabled' : 'Read-only'}
            </span>
          </div>
        </div>

        <div className="left-panel-section-header">
          <div>
            <p className="eyebrow">Workspace modules</p>
            <h2>Switch the left panel</h2>
          </div>
          <span>{LEFT_PANEL_FEATURES.length} views</span>
        </div>

        <nav className="left-panel-nav" role="tablist" aria-label="Left panel modules">
          {LEFT_PANEL_FEATURES.map((feature) => {
            const isActive = feature.key === leftPanelFeature;
            return (
              <button
                key={feature.key}
                type="button"
                role="tab"
                aria-selected={isActive}
                className={`left-panel-tab ${isActive ? 'left-panel-tab-active' : ''}`}
                onClick={() => setLeftPanelFeature(feature.key)}
              >
                <span>{feature.label}</span>
                <small>{feature.description}</small>
              </button>
            );
          })}
        </nav>

        <div className="left-panel-body">
          {leftPanelFeature === 'submission-history' ? (
            <SubmissionHistoryPanel
              query={query}
              setQuery={setQuery}
              filteredDays={filteredSubmissionDays}
              selectedSubmission={selectedSubmission}
              collapsedDayKeys={collapsedDayKeys}
              onToggleDay={toggleDayCollapsed}
              onSelectSubmission={selectSubmission}
            />
          ) : null}

          {leftPanelFeature === 'graph' ? (
            <LeftPanelGraphModule selectedSubmission={selectedSubmission} onOpenGraph={openGraphView} />
          ) : null}

          {leftPanelFeature === 'insights' ? (
            <LeftPanelInsights selectedSubmission={selectedSubmission} submissionCount={submissions.length} tags={tags} />
          ) : null}
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
                <label className="template-optout-control">
                  <input
                    type="checkbox"
                    checked={templateBenchmarkOptOut}
                    onChange={(event) => toggleTemplateBenchmarkOptOut(event.target.checked)}
                    disabled={isPending || !canWrite}
                  />
                  <span>
                    Opt out from templating
                    {isPending ? (
                      <span className="loading-inline" style={{ marginLeft: '8px' }}>
                        <Spinner size="small" />
                        <span>Updating...</span>
                      </span>
                    ) : null}
                  </span>
                </label>
              </div>
              <div className="complexity">
                <span>Time {selectedSubmission.timeComplexity ?? 'n/a'}</span>
                <span>Space {selectedSubmission.spaceComplexity ?? 'n/a'}</span>
              </div>
            </div>

            <div className="selected-tags">
              {selectedTags.length ? (
                selectedTags.map((tag) => (
                  <button
                    key={tag.id}
                    className={['selected-tag', dimensionClass(tag.dimension)].filter(Boolean).join(' ')}
                    disabled={!canWrite}
                    onClick={() => {
                      if (!canWrite) return;
                      removeTag(tag.id);
                    }}
                  >
                    <span>{tag.key}</span>
                    <small>Remove</small>
                  </button>
                ))
              ) : (
                <span className="untagged">untagged</span>
              )}
            </div>

            <div className="benchmark-status">
              {isBenchmarkPending ? (
                <span className="loading-inline">
                  <Spinner size="small" />
                  <span>Benchmarking templates with LLM...</span>
                </span>
              ) : null}
              {benchmark ? <span>Benchmark model: {benchmark.model}</span> : null}
              {templateBenchmarkOptOut ? <span>Template benchmarking is opted out</span> : null}
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
                    className={[
                      'tag-group',
                      dimensionClass(group.tags[0]?.dimension ?? 'unknown'),
                      excludedBenchmarkGroupKeys.has(group.key) ? 'excluded' : '',
                    ]
                      .filter(Boolean)
                      .join(' ')}
                    key={group.key}
                  >
                    <div className="tag-group-header">
                      <div>
                        <h3>{group.label}</h3>
                        {excludedBenchmarkGroupKeys.has(group.key) ? <small>Excluded from LLM benchmark</small> : null}
                      </div>
                      {group.tags.some((tag) => tag.dimension === 'template') ? (
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
                      ) : null}
                    </div>
                    <div className="tag-options">
                      {group.tags.map((tag) => {
                        const score = scoreByTagId.get(tag.id);
                        return (
                          <button
                            key={tag.id}
                            className={[
                              'tag-option',
                              dimensionClass(tag.dimension),
                              tag.source !== 'seeded' ? 'custom-template' : '',
                              draftTagIds.has(tag.id) ? 'selected' : '',
                              selectedTemplate?.id === tag.id ? 'focused' : '',
                              score ? `score-${benchmarkTone(score.score)}` : '',
                            ]
                            .filter(Boolean)
                            .join(' ')}
                            onClick={() => {
                              setSelectedTemplateId(tag.id);
                              if (canWrite) {
                                toggleTag(tag.id);
                              }
                            }}
                            title={tag.description ?? tag.label}
                          >
                            {score ? <strong className="benchmark-score">{score.score}</strong> : null}
                            {canWrite && tag.source !== 'seeded' && tag.dimension === 'template' ? (
                              <span
                                className="delete-template-button"
                                role="button"
                                tabIndex={0}
                                aria-label={`Delete ${tag.label}`}
                                onClick={(event) => {
                                  event.stopPropagation();
                                  deleteTemplate(tag);
                                }}
                                onKeyDown={(event) => {
                                  if (event.key === 'Enter' || event.key === ' ') {
                                    event.preventDefault();
                                    event.stopPropagation();
                                    deleteTemplate(tag);
                                  }
                                }}
                              >
                                ×
                              </span>
                            ) : null}
                            <span>{tag.label}</span>
                            <small>{tag.key}</small>
                            <strong className={`source-badge source-${tag.source}`}>{sourceLabel(tag.source)}</strong>
                            {tag.metadata ? <em>documented</em> : null}
                          </button>
                        );
                      })}
                      {canWrite && group.tags.some((tag) => tag.dimension === 'template') ? (
                        <button className="add-template-card" type="button" onClick={() => openTemplateGenerator(group)}>
                          <span>+</span>
                          <strong>Generate template</strong>
                          <small>{group.label}</small>
                        </button>
                      ) : null}
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
                canWrite={canWrite}
                onClose={() => setTemplateGeneratorModal(null)}
                onChange={updateTemplateGeneratorModal}
                onChangeField={updateTemplateForm}
                onAssistAll={runTemplateGenerator}
                onAssistField={assistTemplateRow}
                onCreate={createTemplateFromModal}
              />
            ) : null}

            {deleteTemplateBlocker ? (
              <DeleteTemplateBlockedModal blocker={deleteTemplateBlocker} onClose={() => setDeleteTemplateBlocker(null)} />
            ) : null}

            <div className="actions">
              <button
                className="primary"
                onClick={saveSelectedSubmission}
                disabled={isPending || !canWrite}
                title={canWrite ? undefined : 'Sign in to enable saving tags'}
              >
                <AsyncButtonLabel isPending={isPending} label="Save submission" pendingLabel="Saving..." />
              </button>
              <button
                onClick={runTemplateBenchmark}
                disabled={isBenchmarkPending || includedBenchmarkGroupCount <= 0 || templateBenchmarkOptOut || !canWrite}
                title={canWrite ? undefined : 'Sign in to run benchmark'}
              >
                <AsyncButtonLabel
                  isPending={isBenchmarkPending}
                  label={benchmark ? 'Rerun benchmark' : 'Benchmark templates'}
                  pendingLabel="Benchmarking..."
                />
              </button>
              <button
                onClick={clearTags}
                disabled={isPending || draftTagIds.size === 0 || !canWrite}
                title={canWrite ? undefined : 'Sign in to clear tags'}
              >
                <AsyncButtonLabel isPending={isPending} label="Clear tags" pendingLabel="Clearing tags..." />
              </button>
              {message ? <p>{message}</p> : null}
              {isDeleteTemplatePending ? (
                <p className="loading-inline">
                  <Spinner size="small" />
                  <span>Checking template deletion...</span>
                </p>
              ) : null}
            </div>
          </>
        ) : (
          <div className="empty">No submissions found.</div>
        )}
      </section>
    </main>
  );
}

function SubmissionHistoryPanel({
  query,
  setQuery,
  filteredDays,
  selectedSubmission,
  collapsedDayKeys,
  onToggleDay,
  onSelectSubmission,
}: SubmissionHistoryPanelProps) {
  return (
    <>
      <div className="filters">
        <input
          value={query}
          onChange={(event) => setQuery(event.target.value)}
          placeholder="Search slug, title, language"
          aria-label="Search submissions"
        />
      </div>

      <div className="submission-list">
        <div className="submission-week-list">
          {filteredDays.length ? (
            filteredDays.map((day) => {
              const isCollapsed = collapsedDayKeys.has(day.key);
              return (
                <section className="submission-week" key={day.key}>
                  <button
                    className={`submission-week-header ${isCollapsed ? 'collapsed' : ''}`}
                    type="button"
                    onClick={() => onToggleDay(day.key)}
                    aria-expanded={!isCollapsed}
                    aria-label={`${isCollapsed ? 'Expand' : 'Collapse'} day ${day.label}`}
                  >
                    <h3>{day.label}</h3>
                    <span>{day.problems.reduce((count, problem) => count + problem.submissions.length, 0)} submissions</span>
                  </button>
                  {!isCollapsed && (
                    <div className="submission-problem-list">
                      {day.problems.map((problem) => {
                        const active = problem.submissions.some((submission) => submission.id === selectedSubmission?.id);
                        return (
                          <section
                            className={['submission-problem-group', active ? 'active' : ''].filter(Boolean).join(' ')}
                            key={problem.key}
                          >
                            <button
                              type="button"
                              className="submission-problem-header"
                              onClick={() => onSelectSubmission(problem.submissions[0])}
                            >
                              <span className="submission-title">{problem.title}</span>
                              <span className="submission-problem-count">{problem.submissions.length}</span>
                            </button>
                            <div className="submission-attempt-list">
                              {problem.submissions.map((submission) => {
                                const taxonomyState = submissionTaxonomyState(submission);
                                const taxonomyClass =
                                  taxonomyState === 'complete'
                                    ? 'taxonomy-complete'
                                    : taxonomyState === 'partial'
                                      ? 'taxonomy-partial'
                                      : 'taxonomy-none';

                                return (
                                  <button
                                    key={submission.id}
                                    type="button"
                                    className={[
                                      'submission-attempt',
                                      taxonomyClass,
                                      submission.id === selectedSubmission?.id ? 'active' : '',
                                    ]
                                      .filter(Boolean)
                                      .join(' ')}
                                    onClick={() => onSelectSubmission(submission)}
                                  >
                                    <span className="submission-meta">
                                      {submission.status} · {formatDate(submission.createdAt)}
                                    </span>
                                    <span className="tag-preview">
                                      {submission.tags.length ? submission.tags.map((tag) => tag.key).join(', ') : 'untagged'}
                                    </span>
                                    <span
                                      className={`submission-optout ${submission.templateBenchmarkOptOut ? 'active' : ''}`}
                                    >
                                      {submission.templateBenchmarkOptOut
                                        ? 'Template benchmark: opt out'
                                        : 'Template benchmark: included'}
                                    </span>
                                  </button>
                                );
                              })}
                            </div>
                          </section>
                        );
                      })}
                    </div>
                  )}
                </section>
              );
            })
          ) : (
            <div className="empty">No matching submissions found.</div>
          )}
        </div>
      </div>
    </>
  );
}

function LeftPanelGraphModule({ selectedSubmission, onOpenGraph }: LeftPanelGraphModuleProps) {
  return (
    <section className="left-panel-card">
      <p className="eyebrow">Graph workspace</p>
      <h3>Submission Relationship Explorer</h3>
      <p>
        Open graph mode from the currently selected submission or jump straight into a full traversal with your current focus.
      </p>
      <p className="muted-copy">
        Current focus: {selectedSubmission ? selectedSubmission.titleSlug ?? selectedSubmission.title ?? 'selected submission' : 'none'}
      </p>
      <button type="button" className="primary" onClick={onOpenGraph}>
        Open graph view
      </button>
      <p className="detail-meta">Graph pages include first-depth related-problem links and submission filtering by date.</p>
    </section>
  );
}

function LeftPanelInsights({ selectedSubmission, submissionCount, tags }: LeftPanelInsightsProps) {
  const seededTemplateCount = tags.filter((tag) => tag.source === 'seeded' && tag.dimension === 'template').length;
  const customTemplateCount = tags.filter((tag) => tag.source === 'manually_created' && tag.dimension === 'template').length;
  const llmTemplateCount = tags.filter((tag) => tag.source === 'llm_generated' && tag.dimension === 'template').length;

  return (
    <section className="left-panel-card">
      <p className="eyebrow">Insights</p>
      <h3>Convergence dashboard</h3>
      <p className="detail-meta">
        Use this panel for quick context before refining metadata, benchmarks, and canonical taxonomy.
      </p>
      <div className="left-panel-kpi-grid">
        <article>
          <p>Accepted submissions</p>
          <strong>{submissionCount}</strong>
        </article>
        <article>
          <p>Template tags (seeded)</p>
          <strong>{seededTemplateCount}</strong>
        </article>
        <article>
          <p>Template tags (custom)</p>
          <strong>{customTemplateCount}</strong>
        </article>
        <article>
          <p>Template tags (LLM)</p>
          <strong>{llmTemplateCount}</strong>
        </article>
      </div>
      {selectedSubmission ? (
        <div className="left-panel-highlight">
          <p>Selected</p>
          <strong>{selectedSubmission.titleSlug ?? selectedSubmission.title ?? 'Untitled'}</strong>
          <p className="muted-copy">{selectedSubmission.language ?? 'language unknown'} · {selectedSubmission.difficulty ?? 'difficulty unknown'}</p>
        </div>
      ) : null}
      <p className="muted-copy">更多分析（例如复盘率、标签覆盖率、失败模式）可以在这里继续扩展。</p>
    </section>
  );
}

function TemplateGeneratorModal({
  modal,
  isPending,
  isComplete,
  canWrite,
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
  canWrite: boolean;
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
              disabled={!canWrite}
            />
          </label>
          <label>
            <span>Brief</span>
            <input
              value={modal.prompt}
              onChange={(event) => onChange({ prompt: event.target.value })}
              placeholder="e.g. generalize this submission into a reusable canonical template"
              disabled={!canWrite}
            />
          </label>
          <button type="button" onClick={onAssistAll} disabled={isPending || !canWrite}>
            <AsyncButtonLabel isPending={isPending} label="LLM assist all" pendingLabel="Assisting..." />
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
                    disabled={!canWrite}
                    required
                  />
                ) : (
                  <input
                    value={modal.form[row.field]}
                    onChange={(event) => onChangeField(row.field, event.target.value)}
                    placeholder={row.placeholder}
                    disabled={!canWrite}
                    required
                  />
                )}
              </label>
              <button type="button" onClick={() => onAssistField(row.field, row.label)} disabled={isPending || !canWrite}>
                <AsyncButtonLabel isPending={isPending} label="LLM assist" pendingLabel="Assisting..." />
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
            <button
              type="button"
              className="primary"
              onClick={onCreate}
              disabled={isPending || !isComplete || !canWrite}
            >
              <AsyncButtonLabel isPending={isPending} label="Create template" pendingLabel="Creating..." />
            </button>
          </div>
        </div>
      </section>
    </div>
  );
}

function DeleteTemplateBlockedModal({
  blocker,
  onClose,
}: {
  blocker: DeleteTemplateBlocker;
  onClose: () => void;
}) {
  return (
    <div className="modal-backdrop" role="presentation">
      <section className="delete-template-modal" role="dialog" aria-modal="true" aria-labelledby="delete-template-title">
        <div className="modal-header">
          <div>
            <p className="eyebrow">Delete blocked</p>
            <h2 id="delete-template-title">{blocker.tag.label}</h2>
            <p>
              This template is still associated with {blocker.assignmentCount} submission
              {blocker.assignmentCount === 1 ? '' : 's'}. Manually remove or replace those tags before deleting it.
            </p>
          </div>
          <button type="button" className="modal-close" onClick={onClose} aria-label="Close delete blocker">
            ×
          </button>
        </div>

        <div className="blocked-submission-list">
          {blocker.submissions.map((submission) => (
            <div key={submission.id} className="blocked-submission">
              <strong>{submission.titleSlug ?? 'Untitled submission'}</strong>
              <span>
                {submission.status} · {formatDate(submission.createdAt)}
              </span>
            </div>
          ))}
        </div>

        {blocker.assignmentCount > blocker.submissions.length ? (
          <p className="blocked-note">Showing latest {blocker.submissions.length}; resolve all associations before deleting.</p>
        ) : null}

        <div className="modal-footer">
          <p>Deletion is intentionally blocked until the associations are resolved manually.</p>
          <div>
            <button type="button" className="primary" onClick={onClose}>
              I will resolve manually
            </button>
          </div>
        </div>
      </section>
    </div>
  );
}

function SubmissionContext({ submission }: { submission: SubmissionRow }) {
  const submissionCode = submission.submissionCode || 'No submission code found.';
  const language = submission.language?.toLowerCase() ?? '';
  const isPythonLanguage = language.includes('python') || language.includes('py');

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
        {isPythonLanguage ? (
          <SyntaxHighlighter
            className="submission-code python-code"
            language="python"
            style={oneDark}
            wrapLongLines
            customStyle={{ margin: 0, maxHeight: 360, overflow: 'auto', borderTop: '1px solid var(--line)' }}
            PreTag="div"
          >
            {submissionCode}
          </SyntaxHighlighter>
        ) : (
          <pre className="submission-code">
            <code>{submissionCode}</code>
          </pre>
        )}
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
