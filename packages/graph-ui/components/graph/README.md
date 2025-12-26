# ForceGraph Component Refactoring

The ForceGraph component has been broken down into smaller, reusable modules:

## Module Structure

### Core Types (`types.ts`)
- `SimulationNode`: Node with D3 simulation properties
- `SimulationLink`: Link with D3 simulation properties  
- `SectorPosition`: Position and radius of a sector

### Sector Utilities (`sectorUtils.ts`)
- `groupNodesBySector()`: Groups nodes by primary or secondary tags
- `getNodeSector()`: Gets the sector name for a node

### Sector Positioning (`sectorPositions.ts`)
- `calculateSectorPositions()`: Calculates circular positions for sectors
- `sectorForceFunction()`: Custom force that pulls nodes toward sector centers

### Simulation (`simulation.ts`)
- `createSimulation()`: Creates and configures D3 force simulation

### UI Components

#### `PrimaryFilterIndicator.tsx`
Displays the active primary filter tags in top-left corner

#### `ExpansionControls.tsx`
Bottom-center buttons for expanding selected sectors

#### `CloseExpandedViewButton.tsx`
Top-right button for closing expanded view

## Usage

```tsx
import { SimulationNode, SimulationLink } from './graph/types';
import { groupNodesBySector, getNodeSector } from './graph/sectorUtils';
import { calculateSectorPositions } from './graph/sectorPositions';
import { createSimulation } from './graph/simulation';
import { PrimaryFilterIndicator } from './graph/PrimaryFilterIndicator';
import { ExpansionControls } from './graph/ExpansionControls';
import { CloseExpandedViewButton } from './graph/CloseExpandedViewButton';
```

## Benefits

- **Modularity**: Each file has a single responsibility
- **Reusability**: Utilities can be used in other graph components
- **Testability**: Smaller functions are easier to unit test
- **Maintainability**: Changes to one aspect don't affect others
- **Readability**: Main component is now focused on orchestration
