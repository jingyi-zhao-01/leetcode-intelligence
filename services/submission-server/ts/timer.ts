export class TimerManager {
  private timers = new Map<string, Date>();

  start(titleSlug: string, allowMultiple = false): void {
    const existing = this.timers.get(titleSlug);

    if (existing && allowMultiple) {
      const elapsed = Math.floor((Date.now() - existing.getTime()) / 60000);
      console.error(`⏱️  Timer already running for ${titleSlug} (${elapsed}min elapsed)`);
      return;
    }

    if (!allowMultiple && this.timers.size > 0) {
      if (existing) {
        const elapsed = Math.floor((Date.now() - existing.getTime()) / 60000);
        console.error(`⏱️  Clearing all timers, restarting ${titleSlug} (was ${elapsed}min)`);
      } else {
        console.error(`⏱️  Clearing ${this.timers.size} existing timer(s)`);
      }
      this.timers.clear();
    }

    this.timers.set(titleSlug, new Date());
    console.error(`⏱️  Timer started for ${titleSlug}`);
  }

  stop(titleSlug: string): number {
    const start = this.timers.get(titleSlug);
    if (!start) {
      return 0;
    }

    this.timers.delete(titleSlug);
    const minutes = Math.max(1, Math.floor((Date.now() - start.getTime()) / 60000));
    console.error(`⏱️  Timer stopped for ${titleSlug}: ${minutes} minutes`);
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
