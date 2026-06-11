import Link from 'next/link';
import { loginAdmin } from '../../actions';

type SearchParams = {
  error?: string;
  returnTo?: string;
};

type Props = {
  searchParams: Promise<SearchParams>;
};

export const dynamic = 'force-dynamic';

function getErrorMessage(error: string | null) {
  if (error === 'invalid') {
    return 'Invalid password.';
  }

  if (error === 'config') {
    return 'Server write secret is missing. Set ADMIN_PASSWORD on Vercel.';
  }

  return null;
}

export default async function AdminLoginPage({ searchParams }: Props) {
  const resolved = await searchParams;
  const errorMessage = getErrorMessage(resolved.error ?? null);
  const returnTo = resolved.returnTo ?? '/';

  return (
    <main className="admin-login">
      <form className="admin-login-form" action={loginAdmin}>
        <h1>Admin Sign In</h1>
        <p>Need write permission for tag updates, template generation and benchmark actions.</p>
        {errorMessage ? <p className="admin-error">{errorMessage}</p> : null}
        <label>
          <span>Admin Password</span>
          <input name="password" type="password" required minLength={8} />
        </label>
        <input name="returnTo" type="hidden" value={returnTo} />
        <button type="submit">Sign in</button>
      </form>

      <p>
        <Link href="/">Back to workbench</Link>
      </p>
    </main>
  );
}
