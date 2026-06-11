import type { ButtonHTMLAttributes } from 'react';
import { cn } from '../../lib/utils';

type ButtonVariant = 'default' | 'outline' | 'ghost' | 'destructive';
type ButtonSize = 'default' | 'sm' | 'lg' | 'icon';

type ButtonProps = ButtonHTMLAttributes<HTMLButtonElement> & {
  variant?: ButtonVariant;
  size?: ButtonSize;
};

export function Button({
  className,
  variant = 'default',
  size = 'default',
  ...props
}: ButtonProps) {
  const classes = cn(
    'ui-btn',
    `ui-btn-${variant}`,
    `ui-btn-${size}`,
    props.disabled ? 'ui-btn-disabled' : null,
    className,
  );

  return <button className={classes} {...props} />;
}
