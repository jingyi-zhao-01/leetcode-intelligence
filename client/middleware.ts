import { NextRequest, NextResponse } from 'next/server';
import { ADMIN_COOKIE_NAME } from './lib/access-control';

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
