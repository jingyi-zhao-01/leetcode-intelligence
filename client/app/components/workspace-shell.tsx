import Link from 'next/link';
import { BookOpen, Brain, FileText, Network } from 'lucide-react';
import { logoutAdmin } from '../actions';

type WorkspaceRouteKey = 'submission-history' | 'templates' | 'graph';

type WorkspaceShellProps = {
  activeRoute: WorkspaceRouteKey;
  canWrite: boolean;
  returnTo: string;
  title: string;
  sectionLabel?: string;
  description?: string;
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
    return <FileText aria-hidden="true" />;
  }

  if (routeKey === 'templates') {
    return <BookOpen aria-hidden="true" />;
  }

  return <Network aria-hidden="true" />;
}

export function WorkspaceShell({
  activeRoute,
  canWrite,
  returnTo,
  title,
  sectionLabel = 'Workbench',
  description,
  children,
}: WorkspaceShellProps) {
  const activeRouteMeta = routes.find((route) => route.key === activeRoute);

  return (
    <div className="app-shell">
      <header className="app-topbar">
        <div className="app-topbar-branding">
          <Link href="/submission-history" className="app-brand-link">
            <span className="app-brand-mark" aria-hidden="true">
              <Brain aria-hidden="true" />
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
          <div className="app-workspace-status" aria-hidden="true">
            <span className="app-workspace-status-dot" />
            <div>
              <strong>{activeRouteMeta?.longLabel ?? title}</strong>
              <small>{description ?? 'Workspace ready'}</small>
            </div>
          </div>
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
          <div className="app-rail-heading">
            <span>Workspaces</span>
          </div>
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
          <div className="app-rail-footer">
            <p>{canWrite ? 'Editing mode enabled' : 'Viewing in safe mode'}</p>
          </div>
        </aside>

        <div className="app-content">{children}</div>
      </div>
    </div>
  );
}
