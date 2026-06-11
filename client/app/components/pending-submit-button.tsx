'use client';

import type { ReactNode } from 'react';
import { useFormStatus } from 'react-dom';
import { Spinner } from './spinner';
import { cn } from '../lib/utils';

type PendingSubmitButtonProps = {
  children: ReactNode;
  pendingText?: string;
  disabled?: boolean;
  className?: string;
};

export function PendingSubmitButton({
  children,
  pendingText = 'Submitting...',
  disabled,
  className,
}: PendingSubmitButtonProps) {
  const { pending } = useFormStatus();

  return (
    <button type="submit" disabled={disabled || pending} className={cn('ui-btn', className)}>
      {pending ? (
        <span className="loading-inline">
          <Spinner size="small" />
          <span>{pendingText}</span>
        </span>
      ) : (
        children
      )}
    </button>
  );
}
