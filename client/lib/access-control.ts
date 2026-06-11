import { cookies } from 'next/headers';
import { redirect } from 'next/navigation';

export const ADMIN_COOKIE_NAME = process.env.ADMIN_COOKIE_NAME ?? 'leetcode-qa-admin';
const ADMIN_COOKIE_MAX_AGE_SECONDS = Number(process.env.ADMIN_COOKIE_MAX_AGE_SECONDS ?? 60 * 60 * 8);

const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD;
const ADMIN_SESSION_TOKEN = process.env.ADMIN_SESSION_TOKEN;

function getSessionToken() {
  return ADMIN_SESSION_TOKEN ?? ADMIN_PASSWORD;
}

export function isWriteConfigured() {
  return Boolean(ADMIN_PASSWORD && getSessionToken());
}

export async function readWriteSession() {
  const cookieStore = await cookies();
  return cookieStore.get(ADMIN_COOKIE_NAME)?.value ?? null;
}

export async function isWriteAllowed() {
  const token = getSessionToken();
  if (!token) {
    return false;
  }
  const session = await readWriteSession();
  return session === token;
}

export async function assertWriteAccess() {
  if (!(await isWriteAllowed())) {
    throw new Error('Write access is required.');
  }
}

export async function requireWriteSession() {
  if (!(await isWriteAllowed())) {
    redirect('/admin/login');
  }
}

export async function setWriteSession() {
  const token = getSessionToken();
  if (!token) {
    throw new Error('Write access is not configured.');
  }

  const cookieStore = await cookies();
  cookieStore.set({
    name: ADMIN_COOKIE_NAME,
    value: token,
    path: '/',
    httpOnly: true,
    sameSite: 'lax',
    secure: process.env.NODE_ENV === 'production',
    maxAge: ADMIN_COOKIE_MAX_AGE_SECONDS,
  });
}

export async function clearWriteSession() {
  const cookieStore = await cookies();
  cookieStore.delete({
    name: ADMIN_COOKIE_NAME,
    path: '/',
  });
}
