---
name: darwin-skill-distiller
description: Distill reusable AI agent skills from completed work, repeated workflows, prompts, SOPs, scripts, debugging sessions, browser automations, research routines, or local project conventions. Use when a task should become a skill, when the user says to summarize a workflow into a skill, or when repeated work can be compressed into reusable instructions.
---

# Darwin Skill Distiller

## Purpose

Turn real work into reusable skills.

## Distillation checklist

Extract these parts from the source workflow:

- Trigger conditions
- User intent
- Required context
- Inputs
- Outputs
- Tools and commands
- Step-by-step workflow
- Failure modes
- Quality checks
- Examples
- Scriptable parts
- Maintenance notes

## Output structure

Create or update a skill with:

```markdown
---
name: skill-name
description: Trigger-focused description.
---

# Skill Name

## When to use
## Workflow
## Inputs
## Outputs
## Tools
## Quality checks
## Failure handling
## Maintenance notes
```

Keep the main `SKILL.md` compact. Move long references, examples, and standards into `references/`.

## Distillation workflow

1. Identify the source asset and the real task it came from.
2. Separate durable instructions from one-off context.
3. Write a trigger-focused `description` that names when the skill should be used.
4. Convert prose into executable workflow steps.
5. Move long background, examples, standards, and data tables into `references/`.
6. Mark scriptable steps that can become `scripts/` tools.
7. Add quality checks that prove the skill worked.
8. Update `registry/skills_index.json` after creating or changing the skill.

## Good output constraints

- The trigger should be specific enough to avoid accidental activation.
- The workflow should fit in one screen when possible.
- The skill should tell the agent what to do, what to inspect, what to produce, and how to verify it.
- The skill should not preserve motivational prose unless it changes execution quality.
