import Link from 'next/link';
import { loginAdmin } from '../../actions';
import { PendingSubmitButton } from '../../components/pending-submit-button';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import { Input } from '../../components/ui/input';
import { Label } from '../../components/ui/label';

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
      <Card className="admin-login-form">
        <CardHeader>
          <CardTitle>Admin Sign In</CardTitle>
          <p>Need write permission for tag updates, template generation and benchmark actions.</p>
        </CardHeader>
        <CardContent className="admin-login-content">
          <form className="admin-login-fields" action={loginAdmin}>
            {errorMessage ? <p className="admin-error">{errorMessage}</p> : null}
            <Label>
              <span>Admin Password</span>
              <Input name="password" type="password" required minLength={8} />
            </Label>
            <input name="returnTo" type="hidden" value={returnTo} />
            <PendingSubmitButton pendingText="Signing in..." className="ui-btn ui-btn-primary">
              Sign in
            </PendingSubmitButton>
          </form>
        </CardContent>
      </Card>

      <p>
        <Link href="/submission-history" className="admin-back-link">
          Back to workbench
        </Link>
      </p>
    </main>
  );
}
