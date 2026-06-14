import { LoaderCircle } from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from '../../components/ui/card';
import { Skeleton } from '../../components/ui/skeleton';

export default function AdminLoginLoading() {
  return (
    <main className="admin-login">
      <Card className="admin-login-form">
        <CardHeader>
          <div className="mb-2 flex items-center gap-2 text-muted-foreground">
            <LoaderCircle className="h-4 w-4 animate-spin text-accent" aria-hidden="true" />
            <span className="text-[10px] font-semibold uppercase tracking-[0.14em]">Loading access control</span>
          </div>
          <CardTitle>Admin Sign In</CardTitle>
          <Skeleton className="mt-2 h-4 w-64" />
        </CardHeader>
        <CardContent className="admin-login-content">
          <div className="admin-login-fields">
            <Skeleton className="h-4 w-32" />
            <Skeleton className="h-9 w-full" />
            <Skeleton className="h-9 w-28" />
          </div>
        </CardContent>
      </Card>
    </main>
  );
}
