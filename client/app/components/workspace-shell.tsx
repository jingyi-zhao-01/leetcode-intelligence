import Link from 'next/link';
import { logoutAdmin } from '../actions';

type WorkspaceRouteKey = 'submission-history' | 'templates' | 'graph';

type WorkspaceShellProps = {
  activeRoute: WorkspaceRouteKey;
  canWrite: boolean;
  returnTo: string;
  title: string;
  sectionLabel?: string;
  children: React.ReactNode;
};

const routes: Array<{
  key: WorkspaceRouteKey;
  href: string;
  shortLabel: string;
  longLabel: string;
}> = [
  {
    key: 'submission-history',
    href: '/submission-history',
    shortLabel: 'Subm',
    longLabel: 'Submissions',
  },
  {
    key: 'templates',
    href: '/templates',
    shortLabel: 'Temp',
    longLabel: 'Template Groups',
  },
  {
    key: 'graph',
    href: '/graph',
    shortLabel: 'Graph',
    longLabel: 'Problem Graph',
  },
];

function RouteIcon({ routeKey }: { routeKey: WorkspaceRouteKey }) {
  if (routeKey === 'submission-history') {
    return (
      <svg viewBox="0 0 16 16" aria-hidden="true">
        <path d="M4 1.5h5l3 3V14a.5.5 0 0 1-.5.5h-7A.5.5 0 0 1 4 14z" fill="none" stroke="currentColor" strokeWidth="1.3" />
        <path d="M9 1.5v3h3" fill="none" stroke="currentColor" strokeWidth="1.3" />
        <path d="M6 7.25h4M6 9.75h4" fill="none" stroke="currentColor" strokeWidth="1.3" strokeLinecap="round" />
      </svg>
    );
  }

  if (routeKey === 'templates') {
    return (
      <svg viewBox="0 0 16 16" aria-hidden="true">
        <path d="M2 3.5h12v9H2z" fill="none" stroke="currentColor" strokeWidth="1.3" />
        <path d="M8 3.5v9M2 8h12" fill="none" stroke="currentColor" strokeWidth="1.3" />
      </svg>
    );
  }

  return (
    <svg viewBox="0 0 16 16" aria-hidden="true">
      <circle cx="3.5" cy="4" r="1.3" fill="none" stroke="currentColor" strokeWidth="1.2" />
      <circle cx="12.5" cy="4" r="1.3" fill="none" stroke="currentColor" strokeWidth="1.2" />
      <circle cx="8" cy="12" r="1.3" fill="none" stroke="currentColor" strokeWidth="1.2" />
      <path d="M4.6 4h6.8M4.3 5l2.9 5.8M11.7 5 8.8 10.8" fill="none" stroke="currentColor" strokeWidth="1.2" strokeLinecap="round" />
    </svg>
  );
}

export function WorkspaceShell({
  activeRoute,
  canWrite,
  returnTo,
  title,
  sectionLabel = 'Workbench',
  children,
}: WorkspaceShellProps) {
  return (
    <div className="app-shell">
      <header className="app-topbar">
        <div className="app-topbar-branding">
          <Link href="/submission-history" className="app-brand-link">
            <span className="app-brand-mark" aria-hidden="true">
              &lt;/&gt;
            </span>
            <span>LeetCode Intelligence</span>
          </Link>
          <span className="app-topbar-divider" aria-hidden="true">
            |
          </span>
          <p className="app-topbar-breadcrumb">
            {sectionLabel} / <strong>{title}</strong>
          </p>
        </div>

        <div className="app-topbar-actions">
          <span className={`app-mode-pill ${canWrite ? 'write-enabled' : 'write-disabled'}`}>
            {canWrite ? 'Write enabled' : 'Read only'}
          </span>
          {canWrite ? (
            <form action={logoutAdmin}>
              <button type="submit" className="app-session-link">
                Sign out
              </button>
            </form>
          ) : (
            <Link className="app-session-link" href={`/admin/login?returnTo=${encodeURIComponent(returnTo)}`}>
              Sign in
            </Link>
          )}
        </div>
      </header>

      <div className="app-body">
        <aside className="app-rail" aria-label="Primary workspace navigation">
          {routes.map((route) => {
            const active = route.key === activeRoute;
            return (
              <Link
                key={route.key}
                href={route.href}
                className={`app-rail-link ${active ? 'active' : ''}`}
                aria-current={active ? 'page' : undefined}
              >
                <RouteIcon routeKey={route.key} />
                <span>{route.shortLabel}</span>
                <small>{route.longLabel}</small>
              </Link>
            );
          })}
        </aside>

        <div className="app-content">{children}</div>
      </div>
    </div>
  );
}
