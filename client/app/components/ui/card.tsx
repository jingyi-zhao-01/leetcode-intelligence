import type { HTMLAttributes, ReactNode } from 'react';
import { cn } from '../../lib/utils';

type CardPartProps<T extends HTMLElement = HTMLElement> = HTMLAttributes<T> & {
  children?: ReactNode;
};

export function Card({ className, children, ...props }: CardPartProps<HTMLElement>) {
  return (
    <section className={cn('rounded-lg border border-border bg-card text-card-foreground shadow-sm', className)} {...props}>
      {children}
    </section>
  );
}

export function CardHeader({ className, children, ...props }: CardPartProps<HTMLElement>) {
  return (
    <header className={cn('flex flex-col space-y-1.5 p-6', className)} {...props}>
      {children}
    </header>
  );
}

export function CardTitle({ className, children, ...props }: CardPartProps<HTMLHeadingElement>) {
  return (
    <h3 className={cn('text-2xl font-semibold leading-none tracking-tight', className)} {...props}>
      {children}
    </h3>
  );
}

export function CardDescription({ className, children, ...props }: CardPartProps<HTMLParagraphElement>) {
  return (
    <p className={cn('text-sm text-muted-foreground', className)} {...props}>
      {children}
    </p>
  );
}

export function CardContent({ className, children, ...props }: CardPartProps<HTMLDivElement>) {
  return (
    <div className={cn('p-6 pt-0', className)} {...props}>
      {children}
    </div>
  );
}

export function CardFooter({ className, children, ...props }: CardPartProps<HTMLElement>) {
  return (
    <footer className={cn('flex items-center p-6 pt-0', className)} {...props}>
      {children}
    </footer>
  );
}
