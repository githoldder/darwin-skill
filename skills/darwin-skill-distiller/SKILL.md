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
