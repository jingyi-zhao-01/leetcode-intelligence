import React from 'react';

interface ExpansionControlsProps {
  selectedSectorsForExpansion: string[];
  onExpand: () => void;
  onClearSelection: () => void;
}

export function ExpansionControls({ 
  selectedSectorsForExpansion, 
  onExpand, 
  onClearSelection 
}: ExpansionControlsProps) {
  if (selectedSectorsForExpansion.length === 0) return null;

  return (
    <div className="absolute bottom-4 left-1/2 transform -translate-x-1/2 flex gap-2">
      <button
        onClick={onExpand}
        className="px-6 py-3 bg-blue-600 hover:bg-blue-700 text-white font-semibold rounded-lg shadow-lg transition-colors"
      >
        Expand {selectedSectorsForExpansion.length} Sector{selectedSectorsForExpansion.length > 1 ? 's' : ''}
      </button>
      <button
        onClick={onClearSelection}
        className="px-6 py-3 bg-gray-600 hover:bg-gray-700 text-white font-semibold rounded-lg shadow-lg transition-colors"
      >
        Clear Selection
      </button>
    </div>
  );
}
