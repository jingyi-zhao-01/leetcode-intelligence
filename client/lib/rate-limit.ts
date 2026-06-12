import { Ratelimit } from '@upstash/ratelimit';
import { Redis } from '@upstash/redis';

const DEFAULT_NON_ADMIN_RATE_LIMIT_MAX_REQUESTS = 120;
const DEFAULT_NON_ADMIN_RATE_LIMIT_WINDOW_SECONDS = 60;
const RATE_LIMIT_PREFIX = 'leetcode-intelligence:non-admin-ip';

function parsePositiveInteger(value: string | undefined, fallback: number) {
  const parsed = Number.parseInt(value ?? '', 10);
  return Number.isFinite(parsed) && parsed > 0 ? parsed : fallback;
}

function hasUpstashConfig() {
  return Boolean(process.env.UPSTASH_REDIS_REST_URL && process.env.UPSTASH_REDIS_REST_TOKEN);
}

function createNonAdminIpRatelimit() {
  if (!hasUpstashConfig()) {
    return null;
  }

  const maxRequests = parsePositiveInteger(
    process.env.NON_ADMIN_RATE_LIMIT_MAX_REQUESTS,
    DEFAULT_NON_ADMIN_RATE_LIMIT_MAX_REQUESTS,
  );
  const windowSeconds = parsePositiveInteger(
    process.env.NON_ADMIN_RATE_LIMIT_WINDOW_SECONDS,
    DEFAULT_NON_ADMIN_RATE_LIMIT_WINDOW_SECONDS,
  );

  return new Ratelimit({
    redis: Redis.fromEnv(),
    limiter: Ratelimit.slidingWindow(maxRequests, `${windowSeconds} s` as `${number} s`),
    analytics: true,
    prefix: RATE_LIMIT_PREFIX,
  });
}

const nonAdminIpRatelimit = createNonAdminIpRatelimit();

export function isNonAdminIpRateLimitConfigured() {
  return nonAdminIpRatelimit !== null;
}

export async function limitNonAdminIp(identifier: string, ip: string) {
  if (!nonAdminIpRatelimit) {
    return null;
  }

  return nonAdminIpRatelimit.limit(identifier, { ip });
}
