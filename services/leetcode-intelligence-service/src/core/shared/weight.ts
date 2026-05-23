import type { IntelligenceConfig } from "../types.ts";

export const DEFAULT_QUESTION_WEIGHT = 1;
export const MIN_SELECTION_WEIGHT = 0.01;

export const clamp = (value: number, min: number, max: number): number => {
  return Math.max(min, Math.min(max, value));
};

export const scoreToWeightDelta = (score: number): number => {
  return (3 - score) * 0.25;
};

export const selectionWeight = (weight: number | null | undefined): number => {
  return Math.max(weight ?? DEFAULT_QUESTION_WEIGHT, MIN_SELECTION_WEIGHT);
};

export const nextWeightFromScore = (
  previousWeight: number,
  score: number,
  config: Pick<IntelligenceConfig, "INTELLIGENCE_MIN_WEIGHT" | "INTELLIGENCE_MAX_WEIGHT">,
): number => {
  return clamp(
    previousWeight + scoreToWeightDelta(score),
    config.INTELLIGENCE_MIN_WEIGHT,
    config.INTELLIGENCE_MAX_WEIGHT,
  );
};

export const normalizedWeightSignal = (weight: number, maxWeight: number): number => {
  return clamp(weight / maxWeight, 0, 1.2);
};
