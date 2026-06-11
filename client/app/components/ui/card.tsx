import { ReactNode } from 'react';
import { cn } from '../../../lib/utils';

export function Card({ className, children }: { className?: string; children: ReactNode }) {
  return <section className={cn('ui-card', className)}>{children}</section>;
}

export function CardHeader({ className, children }: { className?: string; children: ReactNode }) {
  return <header className={cn('ui-card-header', className)}>{children}</header>;
}

export function CardTitle({ className, children }: { className?: string; children: ReactNode }) {
  return <h3 className={cn('ui-card-title', className)}>{children}</h3>;
}

export function CardDescription({ className, children }: { className?: string; children: ReactNode }) {
  return <p className={cn('ui-card-description', className)}>{children}</p>;
}

export function CardContent({ className, children }: { className?: string; children: ReactNode }) {
  return <div className={cn('ui-card-content', className)}>{children}</div>;
}

export function CardFooter({ className, children }: { className?: string; children: ReactNode }) {
  return <footer className={cn('ui-card-footer', className)}>{children}</footer>;
}
