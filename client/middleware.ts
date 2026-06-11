import { NextRequest, NextResponse } from 'next/server';
import { ADMIN_COOKIE_NAME } from './lib/access-control';

function isLocalhostHost(host: string | null) {
  if (!host) return false;
  const normalizedHost = host.toLowerCase().split(':')[0];
  return normalizedHost === 'localhost' || normalizedHost === '127.0.0.1' || normalizedHost === '::1';
}

function isLocalRequest(req: NextRequest) {
  const host = req.headers.get('x-forwarded-host') ?? req.headers.get('host') ?? req.nextUrl.host;
  return isLocalhostHost(host);
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
  if (isLocalRequest(req)) {
    return true;
  }

  const expected = process.env.ADMIN_SESSION_TOKEN ?? process.env.ADMIN_PASSWORD;
  const session = req.cookies.get(ADMIN_COOKIE_NAME)?.value;
  return Boolean(expected && session === expected);
}

export function middleware(req: NextRequest) {
  const { pathname } = req.nextUrl;
  if (!isWriteRoute(pathname, req.method)) {
    return NextResponse.next();
  }

  if (isAuthorized(req)) {
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
