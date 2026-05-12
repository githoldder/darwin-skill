---
name: darwin-skill-auditor
description: Audit existing skills, prompts, SOPs, and reusable workflows for quality, trigger clarity, length, redundancy, missing context, outdated assumptions, scriptability, and lifecycle state. Use when reviewing a skill library, cleaning a prompt collection, or deciding what to keep active versus archive.
---

# Darwin Skill Auditor

## Audit dimensions

Evaluate each skill across:

- Trigger clarity
- Task specificity
- Reusability
- Output clarity
- Tool dependency clarity
- Length and context cost
- Redundancy with other skills
- Scriptability
- Freshness
- Usage value
- Maintenance cost

## Common diagnoses

- Too broad: split into multiple focused skills.
- Too thin: add workflow, examples, failure handling, or outputs.
- Too long: move detail into references.
- Too stale: mark for update or deprecate.
- Too overlapping: merge or clarify boundaries.
- Too manual: extract deterministic scripts.

## Report format

For each reviewed asset, output:

- Current state
- Recommended state
- Main issue
- Suggested action
- Priority
