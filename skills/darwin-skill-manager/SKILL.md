---
name: darwin-skill-manager
description: Manage a local AI agent skill repository. Use whenever the user wants to create, organize, refine, split, merge, archive, score, or evolve skills, prompts, SOPs, scripts, or reusable workflows. Also use during real work when a repeated, stable, complex, token-heavy, or scriptable task appears and may deserve skill distillation.
---

# Darwin Skill Manager

This is the control skill for the `darwin-skill` repository.

## Mission

Help the agent treat skills as living assets rather than static notes.

The agent should continuously identify work that can be:

- skillized
- scripted
- templated
- compressed
- split
- merged
- archived
- deprecated

## Default decision loop

When working on a user task, check whether the task has any of these signals:

- It has appeared three or more times.
- It has stable steps but costs many tokens to explain.
- It has a repeated input/output format.
- It depends on local files, commands, tools, or conventions.
- It has common failure modes worth preserving.
- It can be partially replaced by a deterministic script.

If yes, mention that the task is a candidate for skill distillation and propose a lightweight next step.

## Routing rules

Use this skill as the front door, then route to a child skill when the intent is clear:

- Distill: use `darwin-skill-distiller` when a real task, prompt, SOP, or repeated workflow should become a compact reusable skill.
- Audit: use `darwin-skill-auditor` when a skill library needs quality review, redundancy detection, lifecycle state decisions, or missing-trigger checks.
- Archive: use `darwin-skill-archivist` when an asset should be merged, split, retired, moved out of active use, or preserved as historical reference.
- Script: create or update a deterministic script when the workflow has stable inputs, stable outputs, and repeatable command steps.
- Ask: ask the user only when the target asset, source directory, or intended lifecycle decision is ambiguous enough that guessing would cause churn.

## First-phase workflow

1. Run `scripts/scan_skills.py` on the source directory.
2. Review `registry/skills_index.json` summary counts.
3. Move a small batch of high-value assets into `library/principles`, `library/models`, `library/methods`, or `library/cases`.
4. Distill only the assets that are ready to become active `skills/*/SKILL.md`.
5. Record major moves, splits, merges, and archive decisions in `registry/evolution_log.md`.

## Repository layers

Classify knowledge into four layers:

- Principle: durable beliefs and judgment rules.
- Model: reusable thinking structures.
- Method: executable SOPs, workflows, and checklists.
- Case: concrete skills, scripts, and examples.

## Skill lifecycle states

Use these states in registry records:

- inbox
- candidate
- active
- incubating
- needs_refactor
- scriptable
- archived
- deprecated

## Survival score

Score skills with this intuition:

```text
survival_score = usage_frequency + success_value + token_saving + reusability
                 - maintenance_cost - redundancy - staleness_risk
```

Do not keep a skill active only because it exists. Active skills should earn their place.
