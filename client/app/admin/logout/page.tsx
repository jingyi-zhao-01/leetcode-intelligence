import { logoutAdmin } from '../../actions';
import { PendingSubmitButton } from '../../components/pending-submit-button';

export const dynamic = 'force-dynamic';

export default function AdminLogoutPage() {
  return (
    <main className="admin-login">
      <form action={logoutAdmin}>
        <p>Signing out…</p>
        <PendingSubmitButton pendingText="Signing out...">Confirm sign out</PendingSubmitButton>
      </form>
    </main>
  );
}
