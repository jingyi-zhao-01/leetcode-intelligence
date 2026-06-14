import { ShieldCheck, Database, RefreshCw, Trash2, Download, Upload, Activity, Users } from 'lucide-react';
import { SUBMISSIONS, TEMPLATES, TEMPLATE_GROUPS } from '../../data/mockData';

interface AdminWorkspaceProps { writeEnabled: boolean; }

function AdminSection({ title, children }: { title: string; children: React.ReactNode }) {
  return (<div className="rounded-lg overflow-hidden" style={{ background: '#F8F6F1', border: '1px solid rgba(27,40,32,0.1)' }}><div className="px-4 py-2.5" style={{ borderBottom: '1px solid rgba(27,40,32,0.09)', background: 'rgba(27,40,32,0.03)' }}><span style={{ fontSize: '11px', fontWeight: 600, letterSpacing: '0.06em', color: '#6A7870', textTransform: 'uppercase' }}>{title}</span></div><div className="p-4">{children}</div></div>);
}

function ActionRow({ label, desc, icon: Icon, color, disabled, action }: { label: string; desc: string; icon: React.ElementType; color: string; disabled?: boolean; action: string }) {
  return (<div className="flex items-center justify-between py-2.5" style={{ borderBottom: '1px solid rgba(27,40,32,0.06)' }}><div className="flex items-start gap-3"><Icon size={13} color={color} style={{ marginTop: 1 }} /><div><p style={{ fontSize: '12px', fontWeight: 500, color: '#1B2820' }}>{label}</p><p style={{ fontSize: '11px', color: '#6A7870' }}>{desc}</p></div></div><button disabled={disabled} className="flex items-center gap-1.5 px-3 py-1.5 rounded transition-all shrink-0" style={{ background: disabled ? 'rgba(27,40,32,0.04)' : `${color}12`, border: `1px solid ${disabled ? 'rgba(27,40,32,0.08)' : color + '30'}`, color: disabled ? '#B5B0A7' : color, fontSize: '11px', fontWeight: 500, cursor: disabled ? 'default' : 'pointer' }}>{action}</button></div>);
}

export function AdminWorkspace({ writeEnabled }: AdminWorkspaceProps) {
  const stats = [
    { label: 'Submissions', value: SUBMISSIONS.length, icon: Activity, color: '#1C8A79' },
    { label: 'Templates', value: TEMPLATES.length, icon: Database, color: '#2D5FC4' },
    { label: 'Groups', value: TEMPLATE_GROUPS.length, icon: Users, color: '#C97C2A' },
    { label: 'Accepted', value: SUBMISSIONS.filter(s => s.status === 'Accepted').length, icon: ShieldCheck, color: '#2B7A4B' },
  ];
  return (
    <div className="flex-1 overflow-y-auto p-5" style={{ background: '#F3EFE7', scrollbarWidth: 'thin' }}>
      <div className="max-w-3xl mx-auto flex flex-col gap-5">
        <div className="flex items-center justify-between">
          <div><h2 style={{ fontSize: '15px', fontWeight: 600, color: '#1B2820', marginBottom: 2 }}>Admin</h2><p style={{ fontSize: '11px', color: '#6A7870' }}>Data management, export, and system configuration</p></div>
          {!writeEnabled && <div className="flex items-center gap-1.5 px-3 py-1.5 rounded" style={{ background: 'rgba(201,124,42,0.1)', border: '1px solid rgba(201,124,42,0.25)', fontSize: '11px', color: '#C97C2A' }}><ShieldCheck size={11} />Read-only mode — destructive actions disabled</div>}
        </div>
        <div className="grid grid-cols-4 gap-3">{stats.map(({ label, value, icon: Icon, color }) => (<div key={label} className="flex items-center gap-3 p-3 rounded-lg" style={{ background: '#F8F6F1', border: '1px solid rgba(27,40,32,0.1)' }}><Icon size={16} color={color} /><div><p style={{ fontSize: '18px', fontWeight: 700, color: '#1B2820', lineHeight: 1 }}>{value}</p><p style={{ fontSize: '10px', color: '#6A7870', textTransform: 'uppercase', letterSpacing: '0.05em' }}>{label}</p></div></div>))}</div>
        <AdminSection title="Data Operations"><div className="flex flex-col"><ActionRow label="Re-run all benchmarks" desc="Queue all accepted submissions for LLM benchmark evaluation" icon={RefreshCw} color="#2D5FC4" disabled={!writeEnabled} action="Run" /><ActionRow label="Clear all tags" desc="Remove all template assignments from all submissions" icon={Trash2} color="#C44B36" disabled={!writeEnabled} action="Clear" /><ActionRow label="Export taxonomy" desc="Download all tags and benchmark results as JSON" icon={Download} color="#2B7A4B" disabled={false} action="Export" /><ActionRow label="Import template definitions" desc="Upload a JSON file with algorithm template definitions" icon={Upload} color="#1C8A79" disabled={!writeEnabled} action="Import" /></div></AdminSection>
        <AdminSection title="Access Control"><div className="flex flex-col gap-3"><div className="flex items-center justify-between p-3 rounded" style={{ background: 'rgba(27,40,32,0.04)', border: '1px solid rgba(27,40,32,0.08)' }}><div><p style={{ fontSize: '12px', fontWeight: 500, color: '#1B2820' }}>Write Access</p><p style={{ fontSize: '11px', color: '#6A7870' }}>Current session: {writeEnabled ? 'Write-enabled' : 'Read-only'}</p></div><span className="px-2 py-1 rounded text-[11px] font-medium" style={{ background: writeEnabled ? 'rgba(28,138,121,0.12)' : 'rgba(201,124,42,0.12)', color: writeEnabled ? '#1C8A79' : '#C97C2A' }}>{writeEnabled ? 'Active' : 'Restricted'}</span></div></div></AdminSection>
        <AdminSection title="System Info"><div className="grid grid-cols-2 gap-2">{[{ label: 'LLM Provider', value: 'OpenAI GPT-4o' }, { label: 'Benchmark Model', value: 'gpt-4o-2024-11-20' }, { label: 'Template Version', value: '2.1.4' }, { label: 'Last Sync', value: '2025-01-14 09:42 UTC' }, { label: 'API Credits Used', value: '12,440 / 50,000' }, { label: 'Cache Hit Rate', value: '73.2%' }].map(({ label, value }) => (<div key={label} className="flex justify-between items-center py-2 px-3 rounded" style={{ background: 'rgba(27,40,32,0.03)', border: '1px solid rgba(27,40,32,0.07)' }}><span style={{ fontSize: '11px', color: '#6A7870' }}>{label}</span><span style={{ fontSize: '11px', fontWeight: 500, color: '#1B2820', fontFamily: 'var(--font-mono)' }}>{value}</span></div>))}</div></AdminSection>
      </div>
    </div>
  );
}
