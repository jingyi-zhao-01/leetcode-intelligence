import { loadIntelligenceConfig } from '../core/env.ts';
import { createRuntimeComposition } from './composition.ts';
import { DatabaseBoundIntelligenceService } from './database-boundary.ts';
import { IntelligenceRuntimeService } from './intelligence-runtime.ts';

export type { IntelligenceService } from './contracts.ts';
export type { DomainServices, ExternalServices, PersistenceServices, RuntimeComposition } from './composition.ts';
export { loadIntelligenceConfig } from '../core/env.ts';

export const createIntelligenceServiceRuntime = () => {
  const config = loadIntelligenceConfig();
  const composition = createRuntimeComposition(config);
  const runtime = new IntelligenceRuntimeService(composition, config);
  const service = new DatabaseBoundIntelligenceService(runtime, composition.persistence);

  return {
    config,
    composition,
    runtime,
    service,
  };
};

export const createIntelligenceService = async () => {
  return createIntelligenceServiceRuntime().service;
};
