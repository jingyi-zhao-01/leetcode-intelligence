import { createLogger } from '../logger.ts';

const logger = createLogger('timer');

export type EvictedTimer = {
  titleSlug: string;
  elapsedMinutes: number;
};

export class TimerManager {
  private readonly timers = new Map<string, Date>();

  start(titleSlug: string): { alreadyActive: boolean; evictedTimers: EvictedTimer[] } {
    const existing = this.timers.get(titleSlug);
    const evictedTimers: EvictedTimer[] = [];

    if (existing && this.timers.size === 1) {
      const elapsed = Math.floor((Date.now() - existing.getTime()) / 60000);
      logger.info({ titleSlug, elapsedMinutes: elapsed }, 'Timer already active');
      return { alreadyActive: true, evictedTimers };
    }

    if (this.timers.size > 0) {
      for (const [slug, start] of this.timers.entries()) {
        const elapsedMinutes = Math.floor((Date.now() - start.getTime()) / 60000);
        evictedTimers.push({ titleSlug: slug, elapsedMinutes });
        logger.info(
          {
            titleSlug: slug,
            elapsedMinutes,
            replacedBy: titleSlug,
          },
          'Evicting active timer',
        );
      }
      this.timers.clear();
    }

    this.timers.set(titleSlug, new Date());
    logger.info(
      {
        titleSlug,
        evictedTitleSlugs: evictedTimers.map((entry) => entry.titleSlug),
      },
      'Timer started',
    );
    return { alreadyActive: false, evictedTimers };
  }

  stop(titleSlug: string): number {
    const start = this.timers.get(titleSlug);
    if (!start) {
      return 0;
    }

    this.timers.delete(titleSlug);
    const minutes = Math.max(1, Math.floor((Date.now() - start.getTime()) / 60000));
    logger.info({ titleSlug, minutes }, 'Timer stopped');
    return minutes;
  }

  getActiveTimers(): Record<string, number> {
    const now = Date.now();
    const result: Record<string, number> = {};
    for (const [slug, start] of this.timers.entries()) {
      result[slug] = Math.floor((now - start.getTime()) / 60000);
    }
    return result;
  }

  hasActiveTimer(titleSlug: string): boolean {
    return this.timers.has(titleSlug);
  }

  getElapsedTime(titleSlug: string): number {
    const start = this.timers.get(titleSlug);
    if (!start) {
      return 0;
    }
    return Math.max(1, Math.floor((Date.now() - start.getTime()) / 60000));
  }
}
