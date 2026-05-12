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

## Lifecycle recommendations

Use these default actions:

- `active`: keep loaded or easy to trigger because it saves meaningful work.
- `candidate`: promising, but missing frontmatter, trigger clarity, workflow, or verification.
- `needs_refactor`: too broad, too long, duplicated, stale, or mixing multiple jobs.
- `scriptable`: deterministic enough to become a command-line tool.
- `archived`: low-frequency or historical, useful to keep but not as active context.
- `deprecated`: misleading, obsolete, or replaced by a better asset.

## Audit workflow

1. Start from `registry/skills_index.json` when available.
2. Sort by high-risk signals: no frontmatter, no trigger description, very long files, duplicate topics, stale tool claims.
3. Review only the smallest useful batch.
4. Produce concrete actions: add frontmatter, split, merge, move to references, script, archive, or keep.
5. Avoid rewriting the skill during audit unless the user asked for fixes too.
