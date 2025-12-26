import React from 'react';

interface CloseExpandedViewButtonProps {
  sectorsToExpand: string[];
  onClose: () => void;
}

export function CloseExpandedViewButton({ sectorsToExpand, onClose }: CloseExpandedViewButtonProps) {
  if (sectorsToExpand.length === 0) return null;

  return (
    <div className="absolute top-4 right-4">
      <button
        onClick={onClose}
        className="px-6 py-3 bg-red-600 hover:bg-red-700 text-white font-semibold rounded-lg shadow-lg transition-colors"
      >
        Close Expanded View
      </button>
    </div>
  );
}
