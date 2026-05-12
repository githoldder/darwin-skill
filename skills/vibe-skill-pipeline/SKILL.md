---
name: vibe-skill-pipeline
description: Use when converting repeated AI-assisted work into a reusable skill, reference, script, browser automation, or low-token execution pipeline after a successful real task.
---

# Vibe Skill Pipeline

## Pipeline

1. Run the task once with AI assistance and record what actually worked.
2. Extract the repeatable workflow, inputs, outputs, commands, and failure modes.
3. Decide the durable form:
   - skill for judgment-heavy repeatable workflows
   - script for deterministic command sequences
   - template for stable document outputs
   - reference for long standards or examples
4. Distill the active instruction into a compact `SKILL.md`.
5. Move long context into `references/` or `library/`.
6. Re-run or inspect the workflow to verify it still works.

## Distillation Checklist

- Trigger is clear.
- Steps are executable.
- Inputs and outputs are explicit.
- Failure modes are preserved.
- Verification is included.
- Token-heavy background is not kept in active context.
