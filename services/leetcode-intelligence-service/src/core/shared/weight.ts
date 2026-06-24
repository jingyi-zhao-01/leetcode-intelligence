import type { IntelligenceConfig } from '../types.ts';

export type WeightBoundsConfig = Pick<IntelligenceConfig, 'INTELLIGENCE_MIN_WEIGHT' | 'INTELLIGENCE_MAX_WEIGHT'>;

export interface WeightCalculator {
  readonly defaultWeight: number;
  readonly minSelectionWeight: number;

  clamp(value: number, min: number, max: number): number;
  scoreToWeightDelta(score: number): number;
  selectionWeight(weight: number | null | undefined): number;
  nextWeightFromScore(previousWeight: number, score: number, config: WeightBoundsConfig): number;
  normalizedSignal(weight: number, maxWeight: number): number;
}

export class LinearWeightCalculator implements WeightCalculator {
  readonly defaultWeight = 1;
  readonly minSelectionWeight = 0.01;

  clamp(value: number, min: number, max: number): number {
    return Math.max(min, Math.min(max, value));
  }

  scoreToWeightDelta(score: number): number {
    return (3 - score) * 0.25;
  }

  selectionWeight(weight: number | null | undefined): number {
    return Math.max(weight ?? this.defaultWeight, this.minSelectionWeight);
  }

  nextWeightFromScore(previousWeight: number, score: number, config: WeightBoundsConfig): number {
    return this.clamp(
      previousWeight + this.scoreToWeightDelta(score),
      config.INTELLIGENCE_MIN_WEIGHT,
      config.INTELLIGENCE_MAX_WEIGHT,
    );
  }

  normalizedSignal(weight: number, maxWeight: number): number {
    return this.clamp(weight / maxWeight, 0, 1.2);
  }
}

// Placeholder for alternative weight policies such as
// decay-based, mastery-bucket, or spaced-repetition strategies.
export class PlaceholderWeightCalculator implements WeightCalculator {
  constructor(private readonly fallback: WeightCalculator = new LinearWeightCalculator()) {}

  get defaultWeight(): number {
    return this.fallback.defaultWeight;
  }

  get minSelectionWeight(): number {
    return this.fallback.minSelectionWeight;
  }

  clamp(value: number, min: number, max: number): number {
    return this.fallback.clamp(value, min, max);
  }

  scoreToWeightDelta(score: number): number {
    return this.fallback.scoreToWeightDelta(score);
  }

  selectionWeight(weight: number | null | undefined): number {
    return this.fallback.selectionWeight(weight);
  }

  nextWeightFromScore(previousWeight: number, score: number, config: WeightBoundsConfig): number {
    return this.fallback.nextWeightFromScore(previousWeight, score, config);
  }

  normalizedSignal(weight: number, maxWeight: number): number {
    return this.fallback.normalizedSignal(weight, maxWeight);
  }
}

const defaultWeightCalculator = new LinearWeightCalculator();

export const DEFAULT_QUESTION_WEIGHT = defaultWeightCalculator.defaultWeight;
export const MIN_SELECTION_WEIGHT = defaultWeightCalculator.minSelectionWeight;
export const clamp = (value: number, min: number, max: number): number =>
  defaultWeightCalculator.clamp(value, min, max);
export const scoreToWeightDelta = (score: number): number => defaultWeightCalculator.scoreToWeightDelta(score);
export const selectionWeight = (weight: number | null | undefined): number =>
  defaultWeightCalculator.selectionWeight(weight);
export const nextWeightFromScore = (previousWeight: number, score: number, config: WeightBoundsConfig): number => {
  return defaultWeightCalculator.nextWeightFromScore(previousWeight, score, config);
};
export const normalizedWeightSignal = (weight: number, maxWeight: number): number => {
  return defaultWeightCalculator.normalizedSignal(weight, maxWeight);
};
