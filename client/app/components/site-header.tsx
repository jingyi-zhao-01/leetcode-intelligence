"use client";

import Link from 'next/link';
import { usePathname } from 'next/navigation';

const routes = [
  {
    href: '/submission-history',
    label: 'Submission History',
  },
  {
    href: '/graph',
    label: 'Graph',
  },
  {
    href: '/templates',
    label: 'Templates',
  },
];

function isCurrentPath(pathname: string, href: string) {
  if (href === '/') {
    return pathname === href;
  }

  return pathname === href || pathname.startsWith(`${href}/`);
}

export function SiteHeader() {
  const pathname = usePathname();

  return (
    <header className="site-header">
      <div className="site-brand">
        <Link href="/submission-history" className="site-brand-link">
          LeetCode QA
        </Link>
      </div>

      <nav className="site-nav" aria-label="Main routes">
        {routes.map((route) => (
          <Link
            key={route.href}
            href={route.href}
            className={`site-nav-link ui-btn ui-btn-outline ${isCurrentPath(pathname, route.href) ? 'active ui-btn-primary' : ''}`}
          >
            {route.label}
          </Link>
        ))}
      </nav>
    </header>
  );
}
