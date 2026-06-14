import { LoaderCircle } from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import { Skeleton } from '../../components/ui/skeleton';

export default function AdminLogoutLoading() {
  return (
    <main className="admin-login">
      <Card className="admin-login-form">
        <CardHeader>
          <div className="mb-2 flex items-center gap-2 text-muted-foreground">
            <LoaderCircle className="h-4 w-4 animate-spin text-accent" aria-hidden="true" />
            <span className="text-[10px] font-semibold uppercase tracking-[0.14em]">Ending session</span>
          </div>
          <CardTitle>Signing out</CardTitle>
        </CardHeader>
        <CardContent className="space-y-3">
          <Skeleton className="h-4 w-56" />
          <Skeleton className="h-9 w-36" />
        </CardContent>
      </Card>
    </main>
  );
}
