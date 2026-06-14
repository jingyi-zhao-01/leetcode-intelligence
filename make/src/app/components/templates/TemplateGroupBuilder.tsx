import { useState } from 'react';
import { Plus, X, GripVertical, ChevronDown, ChevronRight, BookOpen, Layers } from 'lucide-react';
import { TEMPLATE_GROUPS, TEMPLATES, SUBMISSIONS, TEMPLATE_MAP, GROUP_MAP, TemplateGroup, AlgorithmTemplate } from '../../data/mockData';

const PRESET_COLORS = ['#1C8A79','#2D5FC4','#C97C2A','#8B4DC4','#2B7A4B','#C44B36','#5A8FA8','#7A5C2A'];

function NewGroupModal({ onClose, onCreate }: { onClose: () => void; onCreate: (name: string, color: string) => void }) {
  const [name, setName] = useState('');
  const [color, setColor] = useState('#1C8A79');
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center" style={{ background: 'rgba(27,40,32,0.4)', backdropFilter: 'blur(2px)' }} onClick={e => e.target === e.currentTarget && onClose()}>
      <div className="rounded-lg p-5 flex flex-col gap-4" style={{ width: 380, background: '#F8F6F1', border: '1px solid rgba(27,40,32,0.15)', boxShadow: '0 8px 32px rgba(27,40,32,0.2)' }}>
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-2"><Layers size={14} color="#1C8A79" /><span style={{ fontSize: '13px', fontWeight: 600, color: '#1B2820' }}>Create Template Group</span></div>
          <button onClick={onClose} className="w-6 h-6 rounded flex items-center justify-center hover:bg-black/5"><X size={12} color="#6A7870" /></button>
        </div>
        <div className="flex flex-col gap-3">
          <div><label style={{ fontSize: '11px', fontWeight: 500, color: '#6A7870', display: 'block', marginBottom: 4 }}>Group Name</label><input value={name} onChange={e => setName(e.target.value)} placeholder="e.g. Monotonic Stack" className="w-full px-3 py-2 rounded outline-none" style={{ background: 'rgba(27,40,32,0.06)', border: '1px solid rgba(27,40,32,0.12)', fontSize: '12px', color: '#1B2820', fontFamily: 'var(--font-sans)' }} autoFocus /></div>
          <div><label style={{ fontSize: '11px', fontWeight: 500, color: '#6A7870', display: 'block', marginBottom: 6 }}>Color</label><div className="flex gap-2 flex-wrap">{PRESET_COLORS.map(c => (<button key={c} onClick={() => setColor(c)} className="w-6 h-6 rounded-full transition-all" style={{ background: c, outline: color === c ? `3px solid ${c}` : '3px solid transparent', outlineOffset: 2 }} />))}</div></div>
          {name && <div className="flex items-center gap-2 px-3 py-2 rounded" style={{ background: color + '12', border: `1px solid ${color}30` }}><div className="w-2.5 h-2.5 rounded-full" style={{ background: color }} /><span style={{ fontSize: '12px', fontWeight: 600, color }}>{name}</span></div>}
        </div>
        <div className="flex gap-2 justify-end">
          <button onClick={onClose} className="px-3 py-1.5 rounded" style={{ fontSize: '11px', color: '#6A7870', background: 'rgba(27,40,32,0.07)', border: '1px solid rgba(27,40,32,0.1)' }}>Cancel</button>
          <button onClick={() => { if (name.trim()) { onCreate(name.trim(), color); onClose(); }}} disabled={!name.trim()} className="px-3 py-1.5 rounded flex items-center gap-1.5" style={{ fontSize: '11px', color: name.trim() ? '#fff' : '#B5B0A7', background: name.trim() ? '#1B2820' : 'rgba(27,40,32,0.07)', border: `1px solid ${name.trim() ? 'rgba(27,40,32,0.6)' : 'rgba(27,40,32,0.1)'}`, fontWeight: 500, cursor: name.trim() ? 'pointer' : 'default' }}><Plus size={11} />Create Group</button>
        </div>
      </div>
    </div>
  );
}

function TemplateCard({ template, group, onDragStart, writeEnabled }: { template: AlgorithmTemplate; group: TemplateGroup; onDragStart: (e: React.DragEvent, templateId: string, fromGroupId: string) => void; writeEnabled: boolean }) {
  const problemCount = SUBMISSIONS.filter(s => s.tags.includes(template.id) && s.status === 'Accepted').length;
  const scoreColor = template.benchmarkScore >= 90 ? '#2B7A4B' : template.benchmarkScore >= 80 ? '#C97C2A' : '#6A7870';
  return (
    <div draggable={writeEnabled} onDragStart={e => writeEnabled && onDragStart(e, template.id, template.groupId)} className="rounded p-2.5 flex flex-col gap-1.5 transition-all" style={{ background: '#F8F6F1', border: '1px solid rgba(27,40,32,0.1)', cursor: writeEnabled ? 'grab' : 'default', borderLeft: `3px solid ${group.color}60` }}>
      <div className="flex items-start justify-between gap-1"><span style={{ fontSize: '11px', fontWeight: 500, color: '#1B2820', lineHeight: 1.3, flex: 1 }}>{template.name}</span>{writeEnabled && <GripVertical size={12} color="#B5B0A7" style={{ marginTop: 1 }} />}</div>
      <div className="flex items-center gap-2"><span style={{ fontSize: '10px', fontFamily: 'var(--font-mono)', color: '#6A7870' }}>{template.complexity.time}</span><span style={{ fontSize: '10px', color: '#B5B0A7' }}>·</span><span style={{ fontSize: '10px', color: scoreColor, fontWeight: 500 }}>{template.benchmarkScore}</span><span style={{ fontSize: '10px', color: '#B5B0A7' }}>·</span><span style={{ fontSize: '10px', color: '#6A7870' }}>{problemCount} probs</span><span className="px-1 rounded text-[9px] ml-auto" style={{ background: template.source === 'seeded' ? 'rgba(43,122,75,0.1)' : template.source === 'llm_generated' ? 'rgba(139,77,196,0.1)' : 'rgba(45,95,196,0.1)', color: template.source === 'seeded' ? '#2B7A4B' : template.source === 'llm_generated' ? '#8B4DC4' : '#2D5FC4' }}>{template.source === 'seeded' ? 'seed' : template.source === 'llm_generated' ? 'llm' : 'manual'}</span></div>
    </div>
  );
}

export function TemplateGroupBuilder({ writeEnabled }: { writeEnabled: boolean }) {
  const [groups, setGroups] = useState<TemplateGroup[]>(() => TEMPLATE_GROUPS.map(g => ({ ...g })));
  const [templateGroups, setTemplateGroups] = useState<Record<string, string[]>>(() => { const m: Record<string, string[]> = {}; for (const g of TEMPLATE_GROUPS) m[g.id] = [...g.templateIds]; return m; });
  const [expandedGroups, setExpandedGroups] = useState<Set<string>>(new Set(TEMPLATE_GROUPS.map(g => g.id)));
  const [showNewGroupModal, setShowNewGroupModal] = useState(false);
  const [dragState, setDragState] = useState<{ templateId: string; fromGroupId: string } | null>(null);
  const [dragOverGroupId, setDragOverGroupId] = useState<string | null>(null);

  const toggleGroup = (gid: string) => setExpandedGroups(eg => { const next = new Set(eg); if (next.has(gid)) next.delete(gid); else next.add(gid); return next; });
  const createGroup = (name: string, color: string) => { const id = `tg-custom-${Date.now()}`; setGroups(g => [...g, { id, name, color, templateIds: [] }]); setTemplateGroups(m => ({ ...m, [id]: [] })); };
  const handleDragStart = (e: React.DragEvent, templateId: string, fromGroupId: string) => { setDragState({ templateId, fromGroupId }); e.dataTransfer.effectAllowed = 'move'; };
  const handleDrop = (e: React.DragEvent, toGroupId: string) => { e.preventDefault(); if (!dragState || dragState.fromGroupId === toGroupId) { setDragState(null); setDragOverGroupId(null); return; } const { templateId, fromGroupId } = dragState; setTemplateGroups(m => ({ ...m, [fromGroupId]: m[fromGroupId].filter(id => id !== templateId), [toGroupId]: [...(m[toGroupId] ?? []), templateId] })); setDragState(null); setDragOverGroupId(null); };
  const handleDragOver = (e: React.DragEvent, gid: string) => { e.preventDefault(); setDragOverGroupId(gid); };
  const getProblemsForGroup = (tids: string[]) => SUBMISSIONS.filter(s => s.status === 'Accepted' && s.tags.some(t => tids.includes(t))).slice(0, 3);

  return (
    <div className="flex-1 flex flex-col overflow-hidden" style={{ background: '#F3EFE7' }}>
      {showNewGroupModal && <NewGroupModal onClose={() => setShowNewGroupModal(false)} onCreate={createGroup} />}
      <div className="flex items-center justify-between px-5 py-2.5 shrink-0" style={{ borderBottom: '1px solid rgba(27,40,32,0.1)', background: '#F8F6F1' }}>
        <div className="flex items-center gap-3"><span style={{ fontSize: '12px', fontWeight: 600, color: '#1B2820' }}>Template Group Builder</span><span style={{ fontSize: '11px', color: '#6A7870' }}>{groups.length} groups · {TEMPLATES.length} templates</span></div>
        {writeEnabled && <button onClick={() => setShowNewGroupModal(true)} className="flex items-center gap-1.5 px-3 py-1.5 rounded transition-all" style={{ background: '#1B2820', border: '1px solid rgba(27,40,32,0.8)', color: '#F3EFE7', fontSize: '11px', fontWeight: 500, cursor: 'pointer' }}><Plus size={11} />New Group</button>}
      </div>
      <div className="flex-1 overflow-x-auto overflow-y-auto p-4" style={{ scrollbarWidth: 'thin' }}>
        <div className="flex gap-4 h-full" style={{ minWidth: groups.length * 260 }}>
          {groups.map(group => {
            const tids = templateGroups[group.id] ?? [];
            const templates = tids.map(id => TEMPLATE_MAP[id]).filter(Boolean) as AlgorithmTemplate[];
            const expanded = expandedGroups.has(group.id);
            const isDragTarget = dragOverGroupId === group.id;
            const associatedProblems = getProblemsForGroup(tids);
            return (
              <div key={group.id} className="flex flex-col rounded-lg overflow-hidden shrink-0" style={{ width: 248, background: '#F8F6F1', border: `1px solid ${isDragTarget ? group.color + '60' : 'rgba(27,40,32,0.1)'}`, boxShadow: isDragTarget ? `0 0 0 2px ${group.color}30` : 'none', transition: 'border-color 0.1s, box-shadow 0.1s' }} onDragOver={e => handleDragOver(e, group.id)} onDrop={e => handleDrop(e, group.id)} onDragLeave={() => setDragOverGroupId(null)}>
                <div className="flex items-center justify-between px-3 py-2.5" style={{ borderBottom: `2px solid ${group.color}40`, background: group.color + '0C' }}>
                  <div className="flex items-center gap-2"><div className="w-2.5 h-2.5 rounded-full" style={{ background: group.color }} /><span style={{ fontSize: '12px', fontWeight: 600, color: group.color }}>{group.name}</span><span className="px-1.5 py-0.5 rounded-full text-[10px]" style={{ background: group.color + '20', color: group.color }}>{templates.length}</span></div>
                  <button onClick={() => toggleGroup(group.id)} style={{ cursor: 'pointer' }}>{expanded ? <ChevronDown size={13} color={group.color} /> : <ChevronRight size={13} color={group.color} />}</button>
                </div>
                {expanded && <div className="flex-1 overflow-y-auto p-2 flex flex-col gap-2" style={{ scrollbarWidth: 'thin', minHeight: 80 }}>{templates.length === 0 && <div className="flex flex-col items-center justify-center py-6 rounded" style={{ border: `2px dashed ${group.color}30`, color: '#B5B0A7', background: isDragTarget ? group.color + '08' : 'transparent' }}><Layers size={16} strokeWidth={1} color="#B5B0A7" /><span style={{ fontSize: '10px', marginTop: 4 }}>{writeEnabled ? 'Drop templates here' : 'No templates'}</span></div>}{templates.map(t => <TemplateCard key={t.id} template={t} group={group} onDragStart={handleDragStart} writeEnabled={writeEnabled} />)}</div>}
                {expanded && associatedProblems.length > 0 && <div className="px-3 pb-2 pt-1" style={{ borderTop: '1px solid rgba(27,40,32,0.07)', background: group.color + '05' }}><div className="flex items-center gap-1 mb-1.5"><BookOpen size={9} color={group.color} /><span style={{ fontSize: '9px', fontWeight: 600, letterSpacing: '0.05em', color: group.color, textTransform: 'uppercase' }}>Associated Problems</span></div><div className="flex flex-col gap-1">{associatedProblems.map(s => <div key={s.id} className="flex items-center gap-1.5"><div className="w-1.5 h-1.5 rounded-full" style={{ background: group.color + '80' }} /><span style={{ fontSize: '10px', color: '#6A7870', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{s.problemTitle}</span></div>)}{SUBMISSIONS.filter(s => s.status === 'Accepted' && s.tags.some(t => tids.includes(t))).length > 3 && <span style={{ fontSize: '10px', color: '#B5B0A7' }}>+{SUBMISSIONS.filter(s => s.status === 'Accepted' && s.tags.some(t => tids.includes(t))).length - 3} more</span>}</div></div>}
              </div>
            );
          })}
          {writeEnabled && <button onClick={() => setShowNewGroupModal(true)} className="flex flex-col items-center justify-center gap-2 rounded-lg shrink-0 transition-all hover:bg-black/5" style={{ width: 248, border: '2px dashed rgba(27,40,32,0.15)', background: 'rgba(27,40,32,0.02)', cursor: 'pointer', minHeight: 120 }}><Plus size={20} color="#B5B0A7" strokeWidth={1.5} /><span style={{ fontSize: '11px', color: '#B5B0A7' }}>New Template Group</span></button>}
        </div>
      </div>
    </div>
  );
}
