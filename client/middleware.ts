import { NextFetchEvent, NextRequest, NextResponse } from 'next/server';
import { ADMIN_COOKIE_NAME } from './lib/access-control';
import { isNonAdminIpRateLimitConfigured, limitNonAdminIp } from './lib/rate-limit';

function isLocalhostHost(host: string | null) {
  if (!host) return false;
  const normalizedHost = host.toLowerCase().split(':')[0];
  return normalizedHost === 'localhost' || normalizedHost === '127.0.0.1' || normalizedHost === '::1';
}

function isLocalRequest(req: NextRequest) {
  const host = req.headers.get('x-forwarded-host') ?? req.headers.get('host') ?? req.nextUrl.host;
  return isLocalhostHost(host);
}

function isLocalWriteBypassEnabled() {
  return process.env.ENABLE_LOCAL_WRITE_BYPASS === 'true';
}

function isProductionDeployment() {
  const vercelEnv = process.env.VERCEL_ENV?.toLowerCase();
  if (vercelEnv) {
    return vercelEnv === 'production';
  }

  return process.env.NODE_ENV === 'production';
}

export const config = {
  matcher: ['/((?!_next/static|_next/image|favicon.ico|robots.txt).*)'],
};

function isWriteRoute(pathname: string, method: string) {
  if (method !== 'POST' && method !== 'PUT' && method !== 'PATCH' && method !== 'DELETE') {
    return false;
  }
  return true;
}

function isAuthorized(req: NextRequest) {
  if (isLocalWriteBypassEnabled() && isLocalRequest(req)) {
    return true;
  }

  const expected = process.env.ADMIN_SESSION_TOKEN ?? process.env.ADMIN_PASSWORD;
  const session = req.cookies.get(ADMIN_COOKIE_NAME)?.value;
  return Boolean(expected && session === expected);
}

function getClientIp(req: NextRequest) {
  const forwardedFor = req.headers.get('x-forwarded-for');
  if (forwardedFor) {
    const firstHop = forwardedFor.split(',')[0]?.trim();
    if (firstHop) {
      return firstHop;
    }
  }

  const realIp = req.headers.get('x-real-ip')?.trim();
  if (realIp) {
    return realIp;
  }

  return 'unknown';
}

function buildRateLimitResponse(result: { limit: number; remaining: number; reset: number }) {
  const retryAfterSeconds = Math.max(1, Math.ceil((result.reset - Date.now()) / 1000));
  return new NextResponse('Too Many Requests', {
    status: 429,
    headers: {
      'content-type': 'text/plain; charset=utf-8',
      'retry-after': String(retryAfterSeconds),
      'x-ratelimit-limit': String(result.limit),
      'x-ratelimit-remaining': String(Math.max(0, result.remaining)),
      'x-ratelimit-reset': String(result.reset),
    },
  });
}

export async function middleware(req: NextRequest, event: NextFetchEvent) {
  const { pathname } = req.nextUrl;
  const isAdmin = isAuthorized(req);

  if (isProductionDeployment() && !isAdmin && isNonAdminIpRateLimitConfigured()) {
    const ip = getClientIp(req);
    const result = await limitNonAdminIp(`ip:${ip}`, ip);
    if (result) {
      event.waitUntil(result.pending);
      if (!result.success) {
        return buildRateLimitResponse(result);
      }
    }
  }

  if (!isWriteRoute(pathname, req.method)) {
    return NextResponse.next();
  }

  if (isAdmin) {
    return NextResponse.next();
  }

  if (pathname.startsWith('/admin/login')) {
    return NextResponse.next();
  }

  const loginUrl = req.nextUrl.clone();
  loginUrl.pathname = '/admin/login';
  const fallback = new URL(req.url);
  loginUrl.searchParams.set('returnTo', fallback.pathname + fallback.search);
  return NextResponse.redirect(loginUrl);
}
