import React from 'react';

interface PrimaryFilterIndicatorProps {
  selectedSectors: string[];
}

export function PrimaryFilterIndicator({ selectedSectors }: PrimaryFilterIndicatorProps) {
  if (selectedSectors.length === 0) return null;

  return (
    <div className="absolute top-4 left-4 bg-blue-900/90 border-2 border-blue-500 rounded-lg px-4 py-2 shadow-lg">
      <div className="text-xs text-blue-300 font-semibold mb-1">Primary Filter:</div>
      <div className="flex flex-wrap gap-2">
        {selectedSectors.map(sector => (
          <span key={sector} className="px-3 py-1 bg-blue-600 text-white text-sm font-medium rounded-md">
            {sector}
          </span>
        ))}
      </div>
      <div className="text-xs text-blue-200 mt-2 italic">
        Showing secondary tags only
      </div>
    </div>
  );
}
