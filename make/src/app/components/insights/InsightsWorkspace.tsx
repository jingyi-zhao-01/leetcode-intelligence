import { BarChart2, TrendingUp, Award, Target, Clock } from 'lucide-react';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';
import { SUBMISSIONS, TEMPLATE_GROUPS, TEMPLATES, TEMPLATE_MAP, GROUP_MAP } from '../../data/mockData';

const DIFF_DATA = [
  { name: 'Easy', value: SUBMISSIONS.filter(s => s.difficulty === 'Easy' && s.status === 'Accepted').length, color: '#2B7A4B' },
  { name: 'Medium', value: SUBMISSIONS.filter(s => s.difficulty === 'Medium' && s.status === 'Accepted').length, color: '#C97C2A' },
  { name: 'Hard', value: SUBMISSIONS.filter(s => s.difficulty === 'Hard' && s.status === 'Accepted').length, color: '#C44B36' },
];
const GROUP_DATA = TEMPLATE_GROUPS.map(g => ({ name: g.name.split(' ')[0], value: SUBMISSIONS.filter(s => s.tags.some(t => TEMPLATE_MAP[t]?.groupId === g.id)).length, color: g.color }));

function KPICard({ icon: Icon, label, value, sub, color }: { icon: React.ElementType; label: string; value: string; sub?: string; color: string }) {
  return (<div className="flex flex-col gap-2 p-4 rounded-lg" style={{ background: '#F8F6F1', border: '1px solid rgba(27,40,32,0.1)' }}><div className="flex items-center gap-2"><Icon size={13} color={color} /><span style={{ fontSize: '10px', fontWeight: 600, letterSpacing: '0.06em', color: '#6A7870', textTransform: 'uppercase' }}>{label}</span></div><div><span style={{ fontSize: '24px', fontWeight: 700, color: '#1B2820', lineHeight: 1 }}>{value}</span>{sub && <span style={{ fontSize: '11px', color: '#6A7870', marginLeft: 6 }}>{sub}</span>}</div></div>);
}

const CustomTooltip = ({ active, payload, label }: any) => {
  if (!active || !payload?.length) return null;
  return <div className="px-2 py-1.5 rounded" style={{ background: '#1B2820', border: '1px solid rgba(255,255,255,0.1)', fontSize: 11, color: '#F3EFE7' }}><p>{label}: <strong>{payload[0].value}</strong></p></div>;
};

export function InsightsWorkspace() {
  const accepted = SUBMISSIONS.filter(s => s.status === 'Accepted').length;
  const tagged = SUBMISSIONS.filter(s => s.tags.length > 0).length;
  const benchmarked = SUBMISSIONS.filter(s => s.benchmarkState === 'complete').length;
  const avgScore = Math.round(TEMPLATES.reduce((a, t) => a + t.benchmarkScore, 0) / TEMPLATES.length);

  return (
    <div className="flex-1 overflow-y-auto p-5" style={{ background: '#F3EFE7', scrollbarWidth: 'thin' }}>
      <div className="max-w-5xl mx-auto flex flex-col gap-5">
        <div><h2 style={{ fontSize: '15px', fontWeight: 600, color: '#1B2820', marginBottom: 2 }}>Submission Insights</h2><p style={{ fontSize: '11px', color: '#6A7870' }}>Overview of taxonomy coverage and template benchmark performance</p></div>
        <div className="grid grid-cols-4 gap-3">
          <KPICard icon={Target} label="Accepted" value={String(accepted)} sub={`of ${SUBMISSIONS.length}`} color="#2B7A4B" />
          <KPICard icon={Award} label="Tagged" value={String(tagged)} sub={`${Math.round(tagged / accepted * 100)}% coverage`} color="#1C8A79" />
          <KPICard icon={TrendingUp} label="Benchmarked" value={String(benchmarked)} sub="submissions" color="#2D5FC4" />
          <KPICard icon={BarChart2} label="Avg Score" value={String(avgScore)} sub="benchmark" color="#C97C2A" />
        </div>
        <div className="grid grid-cols-3 gap-4">
          <div className="rounded-lg p-4" style={{ background: '#F8F6F1', border: '1px solid rgba(27,40,32,0.1)' }}>
            <span style={{ fontSize: '11px', fontWeight: 600, color: '#6A7870', letterSpacing: '0.05em', textTransform: 'uppercase', display: 'block', marginBottom: 12 }}>By Difficulty</span>
            <ResponsiveContainer width="100%" height={140}><PieChart><Pie data={DIFF_DATA} dataKey="value" cx="50%" cy="50%" innerRadius={35} outerRadius={55} paddingAngle={3}>{DIFF_DATA.map((entry, i) => <Cell key={i} fill={entry.color} />)}</Pie><Tooltip content={<CustomTooltip />} /></PieChart></ResponsiveContainer>
            <div className="flex justify-center gap-3 mt-1">{DIFF_DATA.map(d => (<div key={d.name} className="flex items-center gap-1"><div className="w-2 h-2 rounded-full" style={{ background: d.color }} /><span style={{ fontSize: '10px', color: '#6A7870' }}>{d.name} ({d.value})</span></div>))}</div>
          </div>
          <div className="rounded-lg p-4" style={{ background: '#F8F6F1', border: '1px solid rgba(27,40,32,0.1)' }}>
            <span style={{ fontSize: '11px', fontWeight: 600, color: '#6A7870', letterSpacing: '0.05em', textTransform: 'uppercase', display: 'block', marginBottom: 12 }}>By Template Group</span>
            <ResponsiveContainer width="100%" height={160}><BarChart data={GROUP_DATA} layout="vertical" margin={{ left: -20 }}><XAxis type="number" tick={{ fontSize: 9, fill: '#B5B0A7' }} axisLine={false} tickLine={false} /><YAxis type="category" dataKey="name" tick={{ fontSize: 10, fill: '#6A7870' }} axisLine={false} tickLine={false} width={60} /><Tooltip content={<CustomTooltip />} /><Bar dataKey="value" radius={[0, 3, 3, 0]}>{GROUP_DATA.map((entry, i) => <Cell key={i} fill={entry.color} />)}</Bar></BarChart></ResponsiveContainer>
          </div>
          <div className="rounded-lg p-4 flex flex-col gap-3" style={{ background: '#F8F6F1', border: '1px solid rgba(27,40,32,0.1)' }}>
            <span style={{ fontSize: '11px', fontWeight: 600, color: '#6A7870', letterSpacing: '0.05em', textTransform: 'uppercase' }}>Taxonomy Coverage</span>
            <div className="flex flex-col gap-2.5">
              {[{ label: 'Tagged submissions', val: tagged / accepted, color: '#1C8A79' }, { label: 'Benchmarked', val: benchmarked / SUBMISSIONS.length, color: '#2D5FC4' }, { label: 'Opted in', val: SUBMISSIONS.filter(s => !s.optOut).length / SUBMISSIONS.length, color: '#2B7A4B' }].map(({ label, val, color }) => (<div key={label}><div className="flex justify-between mb-1"><span style={{ fontSize: '11px', color: '#6A7870' }}>{label}</span><span style={{ fontSize: '11px', fontWeight: 500, color: '#1B2820' }}>{Math.round(val * 100)}%</span></div><div className="h-1.5 rounded-full overflow-hidden" style={{ background: 'rgba(27,40,32,0.08)' }}><div className="h-full rounded-full" style={{ width: `${val * 100}%`, background: color }} /></div></div>))}
            </div>
          </div>
        </div>
        <div className="rounded-lg overflow-hidden" style={{ background: '#F8F6F1', border: '1px solid rgba(27,40,32,0.1)' }}>
          <div className="px-4 py-3" style={{ borderBottom: '1px solid rgba(27,40,32,0.09)' }}><span style={{ fontSize: '11px', fontWeight: 600, color: '#6A7870', letterSpacing: '0.05em', textTransform: 'uppercase' }}>Template Benchmark Scores</span></div>
          <div className="overflow-x-auto"><table className="w-full"><thead><tr style={{ borderBottom: '1px solid rgba(27,40,32,0.07)' }}>{['Template', 'Group', 'Score', 'Source', 'Time Complexity'].map(h => <th key={h} className="px-4 py-2 text-left" style={{ fontSize: '10px', fontWeight: 600, letterSpacing: '0.05em', color: '#6A7870', textTransform: 'uppercase' }}>{h}</th>)}</tr></thead><tbody>{TEMPLATES.map(t => { const group = GROUP_MAP[t.groupId]; const sc = t.benchmarkScore; const scoreColor = sc >= 90 ? '#2B7A4B' : sc >= 80 ? '#C97C2A' : '#C44B36'; return (<tr key={t.id} style={{ borderBottom: '1px solid rgba(27,40,32,0.06)' }} className="hover:bg-black/[0.02] transition-colors"><td className="px-4 py-2"><span style={{ fontSize: '12px', color: '#1B2820' }}>{t.name}</span></td><td className="px-4 py-2"><span className="px-1.5 py-0.5 rounded text-[10px]" style={{ background: group?.color + '18', color: group?.color }}>{group?.name}</span></td><td className="px-4 py-2"><div className="flex items-center gap-2"><span style={{ fontSize: '12px', fontWeight: 600, color: scoreColor, fontFamily: 'var(--font-mono)' }}>{sc}</span><div className="w-16 h-1.5 rounded-full overflow-hidden" style={{ background: 'rgba(27,40,32,0.1)' }}><div className="h-full rounded-full" style={{ width: `${sc}%`, background: scoreColor }} /></div></div></td><td className="px-4 py-2"><span style={{ fontSize: '11px', color: '#6A7870' }}>{t.source === 'seeded' ? 'Seeded' : t.source === 'llm_generated' ? 'LLM' : 'Manual'}</span></td><td className="px-4 py-2"><span style={{ fontSize: '11px', color: '#6A7870', fontFamily: 'var(--font-mono)' }}>{t.complexity.time}</span></td></tr>); })}</tbody></table></div>
        </div>
      </div>
    </div>
  );
}
