export {
  createDomainServices as createDomainPlane,
  createExternalServices as createExternalDependencyPlane,
  createPersistenceServices as createDataPlane,
  createRuntimeComposition as createServicePlanes,
} from "./composition.ts";
export type {
  DomainServices as DomainPlane,
  ExternalServices as ExternalDependencyPlane,
  PersistenceServices as DataPlane,
  RuntimeComposition as ServicePlanes,
} from "./composition.ts";
