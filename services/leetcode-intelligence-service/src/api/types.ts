export type PatternTagSource = 'seeded' | 'manually_created' | 'llm_generated';
export type PatternTagKind = 'template_group' | 'tag';

export type TemplateMetadata = {
  classicProblems?: string[];
  whenToUse?: string[];
  whenNotToUse?: string[];
  signals?: string[];
  pseudocode?: string[];
  invariants?: string[];
  defaultComplexity?: {
    time?: string;
    space?: string;
  };
  relatedDataStructures?: string[];
  similarTemplates?: string[];
};

export type TemplateBenchmarkScore = {
  key: string;
  patternTagId: string;
  score: number;
  confidence: number;
  reason: string;
  evidence: string[];
};

export type TemplateBenchmarkResult = {
  submissionId: string;
  model: string;
  excludedGroupKeys: string[];
  scores: TemplateBenchmarkScore[];
};

export type GeneratedTemplateDraft = {
  key: string;
  label: string;
  description: string;
  metadata: Required<TemplateMetadata>;
};

export type PatternTagOption = {
  id: string;
  key: string;
  label: string;
  dimension: string;
  kind: PatternTagKind;
  source: PatternTagSource;
  assignmentCount: number;
  description: string | null;
  metadata: TemplateMetadata | null;
  parentId: string | null;
  parentKey: string | null;
  parentLabel: string | null;
  sortOrder: number;
};

export type SubmissionRow = {
  id: string;
  titleSlug: string | null;
  title: string | null;
  difficulty: string | null;
  relatedProblems: string[];
  status: string;
  createdAt: string;
  templateBenchmarkOptOut: boolean;
  language: string | null;
  timeComplexity: string | null;
  spaceComplexity: string | null;
  thought: string | null;
  questionDescription: string | null;
  submissionCode: string;
  templateBenchmark: TemplateBenchmarkResult | null;
  tags: Array<{
    id: string;
    key: string;
    label: string;
    dimension: string;
    kind: PatternTagKind;
    parentId: string | null;
    parentKey: string | null;
    parentLabel: string | null;
  }>;
};

export type TemplateCatalogSubmissionRow = {
  id: string;
  titleSlug: string | null;
  title: string | null;
  createdAt: string;
  tags: Array<{
    id: string;
    key: string;
    label: string;
    dimension: string;
    kind: PatternTagKind;
    parentId: string | null;
    parentKey: string | null;
    parentLabel: string | null;
  }>;
};

export type GraphSubmissionRow = {
  id: string;
  titleSlug: string | null;
  title: string | null;
  difficulty: string | null;
  relatedProblems: string[];
  createdAt: string;
  tags: Array<{
    id: string;
    key: string;
    label: string;
    dimension: string;
    kind: PatternTagKind;
    parentId: string | null;
    parentKey: string | null;
    parentLabel: string | null;
  }>;
};
