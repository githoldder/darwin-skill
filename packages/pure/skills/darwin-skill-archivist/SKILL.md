---
name: darwin-skill-archivist
description: Archive, retire, merge, or split low-value and stale skills. Use when skills have low usage, duplicated scope, outdated instructions, excessive maintenance cost, or when the user asks to clean up a skill repository without losing historical knowledge.
---

# Darwin Skill Archivist

## Purpose

Keep the active skill set small, sharp, and useful.

## Archive criteria

Archive a skill when:

- It has not been used for a long time.
- It overlaps with a better active skill.
- It is useful only as historical reference.
- Its environment assumptions are stale.
- It creates more context cost than execution value.

## Before archiving

Preserve:

- Original path
- Reason for archive
- Date
- Replacement skill, if any
- Useful examples or scripts

## Archive record

Use `templates/EVOLUTION_RECORD.md` when recording archive decisions.

## Split and merge guidance

Split an asset when it contains multiple independently triggered workflows, combines principles with implementation details, or requires different tools for different sections.

Merge assets when two files have the same trigger, same output, and mostly duplicate instructions. Preserve the sharper trigger and the more reliable workflow.

## Archive workflow

1. Confirm the asset path and current state from `registry/skills_index.json`.
2. Decide whether the action is archive, merge, split, deprecate, or move to references.
3. Preserve source path, decision date, reason, and replacement path if one exists.
4. Move the content only after the replacement or archive location is clear.
5. Update `registry/evolution_log.md` and regenerate the skills index.
