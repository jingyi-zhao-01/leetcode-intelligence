const DEFAULT_POOLER_CONNECTION_LIMIT = '1';
const DEFAULT_POOLER_TIMEOUT_SECONDS = '30';

export function resolveDatabaseUrl(databaseUrl = process.env.DATABASE_URL): string | undefined {
  if (!databaseUrl) {
    return undefined;
  }

  try {
    const parsed = new URL(databaseUrl);
    if (!parsed.hostname.includes('-pooler.')) {
      return databaseUrl;
    }

    if (!parsed.searchParams.has('pgbouncer')) {
      parsed.searchParams.set('pgbouncer', 'true');
    }

    if (!parsed.searchParams.has('connection_limit')) {
      parsed.searchParams.set(
        'connection_limit',
        process.env.PRISMA_CONNECTION_LIMIT ?? DEFAULT_POOLER_CONNECTION_LIMIT,
      );
    }

    if (!parsed.searchParams.has('pool_timeout')) {
      parsed.searchParams.set('pool_timeout', process.env.PRISMA_POOL_TIMEOUT ?? DEFAULT_POOLER_TIMEOUT_SECONDS);
    }

    return parsed.toString();
  } catch {
    return databaseUrl;
  }
}

export function getDatabaseDiagnostics(databaseUrl = process.env.DATABASE_URL): Record<string, unknown> {
  const effectiveDatabaseUrl = resolveDatabaseUrl(databaseUrl);

  if (!effectiveDatabaseUrl) {
    return { configured: false };
  }

  try {
    const parsed = new URL(effectiveDatabaseUrl);
    return {
      configured: true,
      protocol: parsed.protocol.replace(/:$/, ''),
      host: parsed.host,
      database: parsed.pathname.replace(/^\//, '') || undefined,
      usesPooler: parsed.hostname.includes('-pooler.'),
      sslmode: parsed.searchParams.get('sslmode') ?? undefined,
      channelBinding: parsed.searchParams.get('channel_binding') ?? undefined,
      connectionLimit: parsed.searchParams.get('connection_limit') ?? undefined,
      poolTimeout: parsed.searchParams.get('pool_timeout') ?? undefined,
      pgbouncer: parsed.searchParams.get('pgbouncer') ?? undefined,
    };
  } catch {
    return {
      configured: true,
      parseable: false,
    };
  }
}
