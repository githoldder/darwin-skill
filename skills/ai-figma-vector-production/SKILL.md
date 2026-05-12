---
name: ai-figma-vector-production
description: Use when converting requirements into diagrams, UML, SVG, Figma-editable vector assets, exports, or visual refinements through an AI-assisted Figma workflow.
---

# AI Figma Vector Production

## Workflow

1. Convert fuzzy requirements into diagram logic: actors, entities, relationships, modules, and notes.
2. Generate an intermediate structure such as PlantUML, Mermaid, or SVG when useful.
3. Check logical completeness before styling.
4. Create or paste vector content into Figma.
5. Ungroup and refine layout, labels, alignment, spacing, and visual hierarchy.
6. Export in the target format: PNG, SVG, PDF, or design handoff asset.

## Checks

- Actors and systems are complete.
- Relationship directions are correct.
- Labels remain editable where possible.
- Text does not overlap.
- Export format matches the destination use.

## Failure Handling

- If generated SVG text shifts, repair anchors and alignment in Figma.
- If logic is too shallow, ask the model to expand the specific module before styling.
