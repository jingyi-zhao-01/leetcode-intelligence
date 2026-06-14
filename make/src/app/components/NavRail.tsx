import { FileText, BookOpen, Network, BarChart2, ShieldCheck } from 'lucide-react';

type Workspace = 'submissions' | 'templates' | 'graph' | 'insights' | 'admin';

interface NavRailProps {
  active: Workspace;
  onChange: (w: Workspace) => void;
}

const NAV_ITEMS: { id: Workspace; icon: React.ElementType; label: string }[] = [
  { id: 'submissions', icon: FileText, label: 'Submissions' },
  { id: 'templates', icon: BookOpen, label: 'Templates' },
  { id: 'graph', icon: Network, label: 'Graph' },
  { id: 'insights', icon: BarChart2, label: 'Insights' },
  { id: 'admin', icon: ShieldCheck, label: 'Admin' },
];

export function NavRail({ active, onChange }: NavRailProps) {
  return (
    <nav
      className="flex flex-col items-center py-3 gap-1 shrink-0"
      style={{ width: 52, background: '#1F2F28', borderRight: '1px solid rgba(255,255,255,0.05)' }}
    >
      {NAV_ITEMS.map(({ id, icon: Icon, label }) => {
        const isActive = active === id;
        return (
          <button
            key={id}
            onClick={() => onChange(id)}
            title={label}
            className="w-9 h-9 flex flex-col items-center justify-center rounded gap-0.5 transition-all"
            style={{
              background: isActive ? 'rgba(28,138,121,0.2)' : 'transparent',
              border: isActive ? '1px solid rgba(28,138,121,0.4)' : '1px solid transparent',
              cursor: 'pointer',
            }}
          >
            <Icon size={15} color={isActive ? '#4DCFBE' : 'rgba(243,239,231,0.38)'} strokeWidth={isActive ? 2 : 1.75} />
            <span style={{ fontSize: '9px', letterSpacing: '0.03em', fontWeight: 500, color: isActive ? '#4DCFBE' : 'rgba(243,239,231,0.3)', lineHeight: 1 }}>
              {label.slice(0, 4)}
            </span>
          </button>
        );
      })}
    </nav>
  );
}
