import { PrismaClient } from '@prisma/client';
import { OpenRouter } from '@openrouter/sdk';
import type { IntelligenceConfig, ScoringAlgorithm } from '../core/types.ts';
import {
  FallbackScoringAlgorithm,
  OpenRouterScoringAlgorithm,
  PromptGenerator,
  PromptResponseService,
  ReplyScorer,
} from '../core/scoring/index.ts';
import { FocusRecommendationService } from '../core/recommendation/index.ts';
import { LinearWeightCalculator, type WeightCalculator } from '../core/shared/weight.ts';

export type PersistenceServices = {
  prisma: PrismaClient;
};

export type ExternalServices = {
  openRouter: OpenRouter | null;
  primaryScoringAlgorithm: ScoringAlgorithm | null;
};

export type DomainServices = {
  weightCalculator: WeightCalculator;
  promptGenerator: PromptGenerator;
  responseService: PromptResponseService;
  recommendationService: FocusRecommendationService;
};

export type RuntimeComposition = {
  persistence: PersistenceServices;
  externalServices: ExternalServices;
  domainServices: DomainServices;
};

export const createPersistenceServices = (): PersistenceServices => {
  return {
    prisma: new PrismaClient(),
  };
};

export const createExternalServices = (config: IntelligenceConfig): ExternalServices => {
  const openRouter = config.OPEN_ROUTER_API_KEY
    ? new OpenRouter({
        apiKey: config.OPEN_ROUTER_API_KEY,
        httpReferer: 'https://github.com/kawre/leetcode.nvim',
        appTitle: 'leetcode-intelligence-service',
      })
    : null;

  return {
    openRouter,
    primaryScoringAlgorithm: openRouter ? new OpenRouterScoringAlgorithm(openRouter, config.MODEL) : null,
  };
};

export const createDomainServices = (
  persistence: PersistenceServices,
  externalServices: ExternalServices,
  config: IntelligenceConfig,
): DomainServices => {
  const weightCalculator = new LinearWeightCalculator();
  const scorer = new ReplyScorer(externalServices.primaryScoringAlgorithm, new FallbackScoringAlgorithm());

  return {
    weightCalculator,
    promptGenerator: new PromptGenerator(persistence.prisma, config, weightCalculator),
    responseService: new PromptResponseService(persistence.prisma, scorer, config, weightCalculator),
    recommendationService: new FocusRecommendationService(persistence.prisma, externalServices.openRouter, config, {
      weightCalculator,
    }),
  };
};

export const createRuntimeComposition = (config: IntelligenceConfig): RuntimeComposition => {
  const persistence = createPersistenceServices();
  const externalServices = createExternalServices(config);
  const domainServices = createDomainServices(persistence, externalServices, config);

  return {
    persistence,
    externalServices,
    domainServices,
  };
};
