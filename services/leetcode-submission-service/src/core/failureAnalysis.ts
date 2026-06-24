import { OpenRouter } from '@openrouter/sdk';
import { OpenRouterFailureStaticAnalyzer, type FailureStaticAnalyzer } from './staticAnalysis.ts';

type JsonPrimitive = string | number | boolean | null;
export type JsonValue = JsonPrimitive | { [key: string]: JsonValue } | JsonValue[];

export type FailureAnalysisRequest = {
  titleSlug: string;
  title: string;
  difficulty?: string;
  topicTags?: string[];
  questionContent: string;
  editorContent: string;
  submissionContent: string;
  testcase: string;
  judgeResult: JsonValue;
  filetype: string;
};

export type FailureAnnotation = {
  line: number;
  reason: string;
  severity: 'error' | 'warn';
  column?: number;
};

export type FailureAnalysisResult = {
  summary: string;
  annotations: FailureAnnotation[];
};

export type FailureAnalyzer = {
  analyze(request: FailureAnalysisRequest): Promise<FailureAnalysisResult>;
};

class DefaultFailureAnalyzer implements FailureAnalyzer {
  constructor(private readonly staticAnalyzer: FailureStaticAnalyzer) {}

  analyze(request: FailureAnalysisRequest): Promise<FailureAnalysisResult> {
    return this.staticAnalyzer.analyze(request);
  }
}

export const createDefaultFailureAnalyzer = (openRouter: OpenRouter, model: string): FailureAnalyzer => {
  return new DefaultFailureAnalyzer(new OpenRouterFailureStaticAnalyzer(openRouter, model));
};
