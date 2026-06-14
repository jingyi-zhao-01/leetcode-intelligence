import { LoaderCircle } from 'lucide-react';
import { Skeleton } from './ui/skeleton';
import { WorkspaceShell } from './workspace-shell';

type LoadingKind = 'submissions' | 'templates' | 'graph';

type PageLoadingScreenProps = {
  kind: LoadingKind;
  title: string;
  description: string;
  returnTo: string;
};

const activeRouteByKind = {
  submissions: 'submission-history',
  templates: 'templates',
  graph: 'graph',
} as const;

function LoadingHeader({ title, description }: { title: string; description: string }) {
  return (
    <div className="flex items-center justify-between gap-4 border-b border-border bg-card px-5 py-3">
      <div className="min-w-0">
        <div className="mb-2 flex items-center gap-2">
          <LoaderCircle className="h-4 w-4 animate-spin text-accent" aria-hidden="true" />
          <span className="text-[10px] font-semibold uppercase tracking-[0.14em] text-muted-foreground">Loading workspace</span>
        </div>
        <h1 className="text-base font-semibold text-foreground">{title}</h1>
        <p className="mt-1 text-xs text-muted-foreground">{description}</p>
      </div>
      <div className="hidden items-center gap-2 sm:flex">
        <Skeleton className="h-8 w-24" />
        <Skeleton className="h-8 w-24" />
      </div>
    </div>
  );
}

function SubmissionLoadingBody() {
  return (
    <main className="grid h-full min-h-0 grid-cols-[272px_minmax(0,1fr)] bg-background">
      <aside className="flex min-h-0 flex-col border-r border-border bg-[#f0ece4]">
        <div className="grid grid-cols-4 border-b border-border bg-[#eceae3]">
          {['Total', 'AC', 'Tagged', 'Benched'].map((label) => (
            <div className="grid justify-items-center gap-1 py-2" key={label}>
              <Skeleton className="h-4 w-7" />
              <span className="text-[9px] uppercase tracking-[0.08em] text-muted-foreground">{label}</span>
            </div>
          ))}
        </div>
        <div className="flex gap-2 border-b border-border p-3">
          <Skeleton className="h-9 flex-1" />
          <Skeleton className="h-9 w-16" />
        </div>
        <div className="space-y-2 p-3">
          {Array.from({ length: 7 }).map((_, index) => (
            <div className="space-y-2 rounded-md border border-border bg-card/60 p-3" key={index}>
              <div className="flex items-center justify-between">
                <Skeleton className="h-3 w-28" />
                <Skeleton className="h-4 w-9 rounded-full" />
              </div>
              <div className="flex items-center gap-2">
                <Skeleton className="h-3 w-12" />
                <Skeleton className="h-3 w-14" />
                <Skeleton className="h-3 w-8" />
              </div>
            </div>
          ))}
        </div>
      </aside>
      <section className="flex min-h-0 flex-col overflow-hidden">
        <LoadingHeader
          title="Submission Taxonomy"
          description="Fetching accepted submissions, tags, benchmark scores, code, and problem statements."
        />
        <div className="space-y-3 border-b border-border bg-[#f5f2eb] p-5">
          <Skeleton className="h-3 w-40" />
          <div className="flex flex-wrap gap-2">
            {Array.from({ length: 6 }).map((_, index) => (
              <Skeleton className="h-7 w-28 rounded-full" key={index} />
            ))}
          </div>
          <div className="space-y-2">
            {Array.from({ length: 4 }).map((_, index) => (
              <Skeleton className="h-11 w-full" key={index} />
            ))}
          </div>
        </div>
        <div className="flex border-b border-border bg-card px-5">
          <Skeleton className="my-2 h-8 w-32" />
          <Skeleton className="my-2 ml-2 h-8 w-36" />
        </div>
        <div className="flex-1 p-4">
          <div className="h-full rounded-lg border border-border bg-[#1b2820] p-4">
            <div className="mb-4 flex items-center justify-between">
              <Skeleton className="h-4 w-32 bg-white/10" />
              <Skeleton className="h-4 w-24 bg-white/10" />
            </div>
            <div className="space-y-3">
              {Array.from({ length: 9 }).map((_, index) => (
                <Skeleton className="h-3 bg-white/10" style={{ width: `${92 - index * 5}%` }} key={index} />
              ))}
            </div>
          </div>
        </div>
      </section>
    </main>
  );
}

function TemplateLoadingBody() {
  return (
    <main className="h-full overflow-hidden bg-background p-5">
      <LoadingHeader title="Template Groups" description="Loading canonical template groups and associated submissions." />
      <div className="mt-5 grid h-[calc(100%-92px)] grid-cols-5 gap-4">
        {Array.from({ length: 5 }).map((_, column) => (
          <section className="flex min-h-0 flex-col rounded-lg border border-border bg-card" key={column}>
            <div className="flex items-center justify-between border-b border-border p-3">
              <Skeleton className="h-4 w-28" />
              <Skeleton className="h-5 w-8 rounded-full" />
            </div>
            <div className="space-y-3 p-3">
              {Array.from({ length: column === 1 ? 4 : 3 }).map((_, index) => (
                <div className="space-y-2 rounded-md border border-border p-3" key={index}>
                  <Skeleton className="h-4 w-36" />
                  <Skeleton className="h-3 w-24" />
                  <div className="flex gap-2">
                    <Skeleton className="h-5 w-14 rounded-full" />
                    <Skeleton className="h-5 w-12 rounded-full" />
                  </div>
                </div>
              ))}
            </div>
          </section>
        ))}
      </div>
    </main>
  );
}

function GraphLoadingBody() {
  return (
    <main className="flex h-full min-h-0 bg-background">
      <aside className="w-[272px] border-r border-border bg-card p-4">
        <Skeleton className="mb-4 h-9 w-full" />
        <div className="space-y-2">
          {Array.from({ length: 7 }).map((_, index) => (
            <Skeleton className="h-10 w-full" key={index} />
          ))}
        </div>
      </aside>
      <section className="relative flex-1 overflow-hidden">
        <LoadingHeader title="Problem Graph" description="Building solved-question relationship nodes and template clusters." />
        <div className="relative h-[calc(100%-74px)]">
          {Array.from({ length: 5 }).map((_, index) => (
            <Skeleton
              className="absolute rounded-full border border-border/60 bg-muted/50"
              style={{
                width: `${140 + index * 22}px`,
                height: `${140 + index * 22}px`,
                left: `${14 + (index % 3) * 26}%`,
                top: `${12 + Math.floor(index / 2) * 30}%`,
              }}
              key={index}
            />
          ))}
          {Array.from({ length: 12 }).map((_, index) => (
            <Skeleton
              className="absolute h-8 w-8 rounded-full bg-accent/40"
              style={{
                left: `${18 + (index * 13) % 68}%`,
                top: `${18 + (index * 17) % 58}%`,
              }}
              key={index}
            />
          ))}
        </div>
      </section>
    </main>
  );
}

export function PageLoadingScreen({ kind, title, description, returnTo }: PageLoadingScreenProps) {
  return (
    <WorkspaceShell
      activeRoute={activeRouteByKind[kind]}
      canWrite={false}
      returnTo={returnTo}
      title={title}
      description={description}
    >
      {kind === 'submissions' ? <SubmissionLoadingBody /> : null}
      {kind === 'templates' ? <TemplateLoadingBody /> : null}
      {kind === 'graph' ? <GraphLoadingBody /> : null}
    </WorkspaceShell>
  );
}
