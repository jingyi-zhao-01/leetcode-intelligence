# LeetCode Intelligence — Workbench UI

This directory contains the Figma Make output for the LeetCode Intelligence workbench redesign.

## Stack
- React + TypeScript + Tailwind CSS v4
- Vite
- Recharts (charts), react-dnd (drag-and-drop), lucide-react (icons)

## Workspaces

| Workspace | Description |
|---|---|
| **Submissions** | Taxonomy workbench — review accepted submissions, assign algorithm template tags, benchmark with LLMs |
| **Templates** | Template Group Builder — kanban-style drag-and-drop organizer for algorithm templates |
| **Graph** | Problem Graph — SVG cluster visualization of solved problem relationships |
| **Insights** | KPI dashboard — coverage stats, benchmark scores, difficulty breakdown |
| **Admin** | Data operations, access control, system info |

## Design Tokens
- Background: `#F3EFE7` (warm sand)
- Panels: `#F8F6F1` (near-white)
- Ink: `#1B2820` (dark green-black)
- Accent: `#1C8A79` (teal)
- Secondary: `#C97C2A` (amber), `#2D5FC4` (blue)
- Font: Plus Jakarta Sans + JetBrains Mono

## Key Interactions
- Toggle **Read only / Write enabled** in the top header
- Click any template chip to open the **Template Control Plane** inspector
- Drag template cards between columns in the **Template Group Builder**
- Switch to **Mobile** preview via the toggle in the preview chrome bar
