import { useState, useRef } from 'react';
import { Search, Filter, Info, ZoomIn, ZoomOut, Maximize2, ChevronDown } from 'lucide-react';
import { TEMPLATE_GROUPS, SUBMISSIONS, TEMPLATES, TEMPLATE_MAP, GROUP_MAP } from '../../data/mockData';

const DIFF_COLOR: Record<string, string> = {
  Easy: '#2B7A4B',
  Medium: '#C97C2A',
  Hard: '#C44B36',
};

const ACCEPTED = SUBMISSIONS.filter(s => s.status === 'Accepted');

const CLUSTER_CENTERS: Record<string, { x: number; y: number }> = {
  'tg-sliding': { x: 160, y: 150 },
  'tg-tree': { x: 420, y: 100 },
  'tg-dp': { x: 600, y: 260 },
  'tg-graph': { x: 160, y: 340 },
  'tg-binary': { x: 440, y: 360 },
};

function nodePosition(subIndex: number, groupId: string, totalInGroup: number) {
  const center = CLUSTER_CENTERS[groupId] ?? { x: 350, y: 240 };
  const angle = (subIndex / totalInGroup) * Math.PI * 2;
  const r = Math.min(60, 20 + totalInGroup * 10);
  return { x: center.x + Math.cos(angle) * r, y: center.y + Math.sin(angle) * r };
}

interface GraphNode { id: string; title: string; difficulty: string; groupId: string | null; x: number; y: number; }

function buildNodes(): GraphNode[] {
  const byGroup: Record<string, string[]> = {};
  for (const sub of ACCEPTED) {
    const gid = sub.tags[0] ? (TEMPLATE_MAP[sub.tags[0]]?.groupId ?? 'ungrouped') : 'ungrouped';
    if (!byGroup[gid]) byGroup[gid] = [];
    byGroup[gid].push(sub.id);
  }
  return ACCEPTED.map(sub => {
    const gid = sub.tags[0] ? (TEMPLATE_MAP[sub.tags[0]]?.groupId ?? null) : null;
    const effectiveGid = gid ?? 'tg-dp';
    const groupSubs = byGroup[effectiveGid] ?? [];
    const idx = groupSubs.indexOf(sub.id);
    const pos = nodePosition(idx, effectiveGid, groupSubs.length);
    return { id: sub.id, title: sub.problemTitle, difficulty: sub.difficulty, groupId: gid, x: pos.x, y: pos.y };
  });
}

const GRAPH_NODES = buildNodes();
const EDGES: Array<[string, string]> = [];
for (let i = 0; i < ACCEPTED.length; i++) {
  for (let j = i + 1; j < ACCEPTED.length; j++) {
    const a = ACCEPTED[i]; const b = ACCEPTED[j];
    if (a.tags.some(t => b.tags.includes(t))) EDGES.push([a.id, b.id]);
  }
}
const NODE_MAP: Record<string, GraphNode> = Object.fromEntries(GRAPH_NODES.map(n => [n.id, n]));

export function GraphWorkspace() {
  const [search, setSearch] = useState('');
  const [activeGroups, setActiveGroups] = useState<Set<string>>(new Set(TEMPLATE_GROUPS.map(g => g.id)));
  const [selectedNode, setSelectedNode] = useState<string | null>(null);
  const [colorByDiff, setColorByDiff] = useState(false);
  const [zoom, setZoom] = useState(1);
  const svgRef = useRef<SVGSVGElement>(null);

  const toggleGroup = (gid: string) => setActiveGroups(prev => { const next = new Set(prev); if (next.has(gid)) next.delete(gid); else next.add(gid); return next; });
  const visibleNodes = GRAPH_NODES.filter(n => (n.groupId ? activeGroups.has(n.groupId) : true) && (!search || n.title.toLowerCase().includes(search.toLowerCase())));
  const visibleIds = new Set(visibleNodes.map(n => n.id));
  const visibleEdges = EDGES.filter(([a, b]) => visibleIds.has(a) && visibleIds.has(b));
  const selectedSub = selectedNode ? ACCEPTED.find(s => s.id === selectedNode) : null;
  const selectedNodeData = selectedNode ? NODE_MAP[selectedNode] : null;
  const selectedGroup = selectedNodeData?.groupId ? GROUP_MAP[selectedNodeData.groupId] : null;

  return (
    <div className="flex-1 flex overflow-hidden" style={{ background: '#F3EFE7' }}>
      <div className="flex flex-col w-56 shrink-0 overflow-y-auto" style={{ borderRight: '1px solid rgba(27,40,32,0.1)', background: '#F0ECE4', scrollbarWidth: 'thin' }}>
        <div className="px-3 py-2.5" style={{ borderBottom: '1px solid rgba(27,40,32,0.1)' }}><span style={{ fontSize: '10px', fontWeight: 600, letterSpacing: '0.07em', color: '#6A7870', textTransform: 'uppercase' }}>Template Groups</span></div>
        <div className="px-3 py-2" style={{ borderBottom: '1px solid rgba(27,40,32,0.08)' }}>
          <div className="flex items-center gap-1.5 px-2 py-1 rounded" style={{ background: 'rgba(27,40,32,0.07)', border: '1px solid rgba(27,40,32,0.1)' }}>
            <Search size={10} color="#6A7870" />
            <input value={search} onChange={e => setSearch(e.target.value)} placeholder="Filter nodes…" className="flex-1 bg-transparent outline-none" style={{ fontSize: '11px', color: '#1B2820', fontFamily: 'var(--font-sans)' }} />
          </div>
        </div>
        <div className="flex flex-col gap-0 flex-1">
          {TEMPLATE_GROUPS.map(group => {
            const active = activeGroups.has(group.id);
            const groupSubs = GRAPH_NODES.filter(n => n.groupId === group.id);
            return (
              <button key={group.id} onClick={() => toggleGroup(group.id)} className="flex items-center gap-2 px-3 py-2 transition-colors" style={{ borderBottom: '1px solid rgba(27,40,32,0.07)', background: active ? `${group.color}08` : 'transparent', cursor: 'pointer', opacity: active ? 1 : 0.5 }}>
                <div className="w-2.5 h-2.5 rounded-full shrink-0" style={{ background: active ? group.color : '#B5B0A7', border: `1px solid ${group.color}60` }} />
                <span style={{ fontSize: '11px', color: active ? group.color : '#6A7870', fontWeight: active ? 500 : 400, flex: 1, textAlign: 'left' }}>{group.name}</span>
                <span style={{ fontSize: '10px', color: '#B5B0A7' }}>{groupSubs.length}</span>
              </button>
            );
          })}
        </div>
        <div className="px-3 py-3" style={{ borderTop: '1px solid rgba(27,40,32,0.1)' }}>
          <span style={{ fontSize: '10px', fontWeight: 600, letterSpacing: '0.07em', color: '#6A7870', textTransform: 'uppercase' }}>Color By</span>
          <div className="flex flex-col gap-1 mt-2">
            {[{ label: 'Template Group', value: false }, { label: 'Difficulty', value: true }].map(opt => (
              <button key={String(opt.value)} onClick={() => setColorByDiff(opt.value)} className="flex items-center gap-2 px-2 py-1.5 rounded transition-colors text-left" style={{ background: colorByDiff === opt.value ? 'rgba(28,138,121,0.1)' : 'transparent', border: `1px solid ${colorByDiff === opt.value ? 'rgba(28,138,121,0.3)' : 'transparent'}`, cursor: 'pointer' }}>
                <div className="w-2 h-2 rounded-full" style={{ background: colorByDiff === opt.value ? '#1C8A79' : '#B5B0A7' }} />
                <span style={{ fontSize: '11px', color: colorByDiff === opt.value ? '#1C8A79' : '#6A7870' }}>{opt.label}</span>
              </button>
            ))}
          </div>
        </div>
      </div>
      <div className="flex-1 flex flex-col overflow-hidden relative">
        <div className="flex items-center justify-between px-4 py-2 shrink-0" style={{ borderBottom: '1px solid rgba(27,40,32,0.1)', background: '#F8F6F1' }}>
          <span style={{ fontSize: '11px', color: '#6A7870' }}>{visibleNodes.length} problems · {visibleEdges.length} connections</span>
          <div className="flex items-center gap-1">
            <button onClick={() => setZoom(z => Math.max(0.5, z - 0.1))} className="w-6 h-6 rounded flex items-center justify-center hover:bg-black/5"><ZoomOut size={12} color="#6A7870" /></button>
            <span style={{ fontSize: '10px', color: '#6A7870', minWidth: 36, textAlign: 'center' }}>{Math.round(zoom * 100)}%</span>
            <button onClick={() => setZoom(z => Math.min(2, z + 0.1))} className="w-6 h-6 rounded flex items-center justify-center hover:bg-black/5"><ZoomIn size={12} color="#6A7870" /></button>
            <button onClick={() => setZoom(1)} className="w-6 h-6 rounded flex items-center justify-center hover:bg-black/5"><Maximize2 size={11} color="#6A7870" /></button>
          </div>
        </div>
        <div className="flex-1 overflow-hidden relative">
          <svg ref={svgRef} width="100%" height="100%" viewBox="0 0 760 480" style={{ transform: `scale(${zoom})`, transformOrigin: 'center center', transition: 'transform 0.15s' }}>
            {TEMPLATE_GROUPS.map(group => { if (!activeGroups.has(group.id)) return null; const center = CLUSTER_CENTERS[group.id]; if (!center) return null; return (<g key={group.id}><circle cx={center.x} cy={center.y} r={75} fill={group.color} opacity={0.04} /><circle cx={center.x} cy={center.y} r={75} fill="none" stroke={group.color} strokeWidth={1} opacity={0.15} strokeDasharray="4 4" /><text x={center.x} y={center.y + 90} textAnchor="middle" style={{ fontFamily: 'var(--font-sans)', fontSize: 10, fill: group.color, opacity: 0.7, fontWeight: 600 }}>{group.name}</text></g>); })}
            {visibleEdges.map(([aid, bid], i) => { const a = NODE_MAP[aid]; const b = NODE_MAP[bid]; if (!a || !b) return null; return <line key={i} x1={a.x} y1={a.y} x2={b.x} y2={b.y} stroke="rgba(27,40,32,0.12)" strokeWidth={1} />; })}
            {visibleNodes.map(node => { const group = node.groupId ? GROUP_MAP[node.groupId] : null; const color = colorByDiff ? DIFF_COLOR[node.difficulty] : (group?.color ?? '#6A7870'); const isSelected = selectedNode === node.id; const r = isSelected ? 9 : 7; return (<g key={node.id} onClick={() => setSelectedNode(node.id === selectedNode ? null : node.id)} style={{ cursor: 'pointer' }}>{isSelected && <circle cx={node.x} cy={node.y} r={14} fill={color} opacity={0.15} />}<circle cx={node.x} cy={node.y} r={r} fill={color} opacity={isSelected ? 1 : 0.75} stroke={isSelected ? color : 'rgba(255,255,255,0.6)'} strokeWidth={isSelected ? 2 : 1} />{isSelected && <text x={node.x} y={node.y - 14} textAnchor="middle" style={{ fontFamily: 'var(--font-sans)', fontSize: 9, fill: '#1B2820', fontWeight: 600 }}>{node.title.length > 22 ? node.title.slice(0, 22) + '…' : node.title}</text>}</g>); })}
          </svg>
          <div className="absolute bottom-3 left-3 rounded p-2 flex flex-col gap-1" style={{ background: 'rgba(248,246,241,0.92)', border: '1px solid rgba(27,40,32,0.1)', backdropFilter: 'blur(4px)' }}>
            <span style={{ fontSize: '9px', fontWeight: 600, color: '#6A7870', letterSpacing: '0.06em', textTransform: 'uppercase' }}>{colorByDiff ? 'Difficulty' : 'Groups'}</span>
            {colorByDiff ? Object.entries(DIFF_COLOR).map(([d, c]) => (<div key={d} className="flex items-center gap-1.5"><div className="w-2 h-2 rounded-full" style={{ background: c }} /><span style={{ fontSize: '10px', color: '#3A4840' }}>{d}</span></div>)) : TEMPLATE_GROUPS.filter(g => activeGroups.has(g.id)).map(g => (<div key={g.id} className="flex items-center gap-1.5"><div className="w-2 h-2 rounded-full" style={{ background: g.color }} /><span style={{ fontSize: '10px', color: '#3A4840' }}>{g.name}</span></div>))}
          </div>
        </div>
      </div>
      {selectedSub && selectedNodeData && (
        <div className="flex flex-col w-56 shrink-0 overflow-y-auto" style={{ borderLeft: '1px solid rgba(27,40,32,0.1)', background: '#F8F6F1', scrollbarWidth: 'thin' }}>
          <div className="flex items-center justify-between px-3 py-2.5" style={{ borderBottom: '1px solid rgba(27,40,32,0.1)' }}>
            <span style={{ fontSize: '10px', fontWeight: 600, letterSpacing: '0.07em', color: '#6A7870', textTransform: 'uppercase' }}>Node Details</span>
            <button onClick={() => setSelectedNode(null)} className="w-5 h-5 rounded flex items-center justify-center hover:bg-black/5"><ZoomOut size={10} color="#6A7870" /></button>
          </div>
          <div className="px-3 py-3 flex flex-col gap-3">
            <div><p style={{ fontSize: '13px', fontWeight: 600, color: '#1B2820', lineHeight: 1.3 }}>{selectedSub.problemTitle}</p><p style={{ fontSize: '10px', color: '#B5B0A7', fontFamily: 'var(--font-mono)', marginTop: 2 }}>/{selectedSub.slug}</p></div>
            <div className="flex flex-wrap gap-1.5">
              <span className="px-1.5 py-0.5 rounded text-[10px]" style={{ background: DIFF_COLOR[selectedSub.difficulty] + '18', color: DIFF_COLOR[selectedSub.difficulty] }}>{selectedSub.difficulty}</span>
              <span className="px-1.5 py-0.5 rounded text-[10px]" style={{ background: 'rgba(27,40,32,0.07)', color: '#6A7870', fontFamily: 'var(--font-mono)' }}>{selectedSub.language}</span>
              {selectedGroup && <span className="px-1.5 py-0.5 rounded text-[10px]" style={{ background: selectedGroup.color + '18', color: selectedGroup.color }}>{selectedGroup.name}</span>}
            </div>
            <div className="flex flex-col gap-1.5">
              <span style={{ fontSize: '10px', fontWeight: 600, letterSpacing: '0.05em', color: '#6A7870', textTransform: 'uppercase' }}>Tags</span>
              {selectedSub.tags.length === 0 ? <span style={{ fontSize: '11px', color: '#B5B0A7', fontStyle: 'italic' }}>No tags</span> : selectedSub.tags.map(tid => { const t = TEMPLATE_MAP[tid]; const g = t ? GROUP_MAP[t.groupId] : null; return <span key={tid} className="px-2 py-0.5 rounded text-[11px]" style={{ background: (g?.color ?? '#1C8A79') + '15', color: g?.color ?? '#1C8A79', border: `1px solid ${(g?.color ?? '#1C8A79')}30` }}>{t?.name}</span>; })}
            </div>
            <div className="flex flex-col gap-1">
              <span style={{ fontSize: '10px', fontWeight: 600, letterSpacing: '0.05em', color: '#6A7870', textTransform: 'uppercase' }}>Connected Problems</span>
              {EDGES.filter(([a, b]) => a === selectedNode || b === selectedNode).slice(0, 5).map(([a, b]) => { const otherId = a === selectedNode ? b : a; const other = NODE_MAP[otherId]; if (!other) return null; const g = other.groupId ? GROUP_MAP[other.groupId] : null; return (<button key={otherId} onClick={() => setSelectedNode(otherId)} className="flex items-center gap-2 px-2 py-1 rounded text-left transition-colors hover:bg-black/5" style={{ border: '1px solid rgba(27,40,32,0.07)' }}><div className="w-2 h-2 rounded-full shrink-0" style={{ background: g?.color ?? '#6A7870' }} /><span style={{ fontSize: '11px', color: '#3A4840', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{other.title}</span></button>); })}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
