import { Brain, Eye, PenLine, ChevronDown, Bell, Settings } from 'lucide-react';

interface AppHeaderProps {
  writeEnabled: boolean;
  onToggleWrite: () => void;
  workspace: string;
}

const WORKSPACE_LABELS: Record<string, string> = {
  submissions: 'Submission Taxonomy',
  templates: 'Template Groups',
  graph: 'Problem Graph',
  insights: 'Insights',
  admin: 'Admin',
};

export function AppHeader({ writeEnabled, onToggleWrite, workspace }: AppHeaderProps) {
  return (
    <header
      className="h-10 flex items-center px-3 gap-4 shrink-0 z-20"
      style={{
        background: '#1B2820',
        borderBottom: '1px solid rgba(255,255,255,0.07)',
      }}
    >
      <div className="flex items-center gap-2 shrink-0">
        <Brain size={15} color="#1C8A79" strokeWidth={2} />
        <span style={{ fontFamily: 'var(--font-sans)', fontWeight: 600, fontSize: '12px', letterSpacing: '0.04em', color: '#F3EFE7' }}>
          LeetCode Intelligence
        </span>
      </div>
      <div className="w-px h-4 shrink-0" style={{ background: 'rgba(255,255,255,0.12)' }} />
      <div className="flex items-center gap-1">
        <span style={{ fontSize: '11px', color: 'rgba(243,239,231,0.45)' }}>Workbench</span>
        <span style={{ fontSize: '11px', color: 'rgba(243,239,231,0.3)' }}>/</span>
        <span style={{ fontSize: '11px', fontWeight: 500, color: 'rgba(243,239,231,0.85)' }}>
          {WORKSPACE_LABELS[workspace] ?? workspace}
        </span>
      </div>
      <div className="flex-1" />
      <button
        onClick={onToggleWrite}
        className="flex items-center gap-1.5 px-2.5 py-1 rounded transition-all"
        style={{
          background: writeEnabled ? 'rgba(28,138,121,0.18)' : 'rgba(255,255,255,0.06)',
          border: `1px solid ${writeEnabled ? 'rgba(28,138,121,0.5)' : 'rgba(255,255,255,0.1)'}`,
          color: writeEnabled ? '#4DCFBE' : 'rgba(243,239,231,0.5)',
          fontSize: '11px', fontWeight: 500, letterSpacing: '0.02em', cursor: 'pointer',
        }}
      >
        {writeEnabled ? <PenLine size={11} /> : <Eye size={11} />}
        {writeEnabled ? 'Write enabled' : 'Read only'}
      </button>
      <div className="flex items-center gap-2 px-2 py-1 rounded" style={{ background: 'rgba(255,255,255,0.05)', cursor: 'pointer' }}>
        <div className="w-5 h-5 rounded-full flex items-center justify-center text-[10px]" style={{ background: '#1C8A79', color: '#fff', fontWeight: 600 }}>AK</div>
        <span style={{ fontSize: '11px', color: 'rgba(243,239,231,0.6)' }}>aryan.k</span>
        <ChevronDown size={10} color="rgba(243,239,231,0.4)" />
      </div>
      <Bell size={14} color="rgba(243,239,231,0.4)" style={{ cursor: 'pointer' }} />
      <Settings size={14} color="rgba(243,239,231,0.4)" style={{ cursor: 'pointer' }} />
    </header>
  );
}
