import type { CSSProperties } from 'react';
import './spinner.css';

type Size = 'small' | 'medium' | 'large' | number;

function resolveStyle(size: Size) {
  if (typeof size === 'number') {
    return {
      '--spinner-size': `${size}px`,
    } as CSSProperties;
  }

  return undefined;
}

export function Spinner({ size = 'medium' }: { size?: Size }) {
  return (
    <span className={`inline-spinner ${typeof size === 'string' ? size : ''}`.trim()} style={resolveStyle(size)} />
  );
}
