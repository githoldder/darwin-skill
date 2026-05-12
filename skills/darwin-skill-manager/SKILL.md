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
