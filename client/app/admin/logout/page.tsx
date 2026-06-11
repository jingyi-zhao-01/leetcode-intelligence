import { logoutAdmin } from '../../actions';

export const dynamic = 'force-dynamic';

export default function AdminLogoutPage() {
  return (
    <main className="admin-login">
      <form action={logoutAdmin}>
        <p>Signing out…</p>
        <button type="submit">Confirm sign out</button>
      </form>
    </main>
  );
}
