---
name: requirement-alignment-log
description: Use when turning requirement interviews, stakeholder feedback, or scope changes into an incremental requirement alignment log without rewriting the baseline spec.
---

# Requirement Alignment Log

## Workflow

1. Identify the baseline document or current agreed scope.
2. Classify each item as new requirement, clarification, change, rejection, or open question.
3. Group items by module or workflow.
4. Record impact scope, status, and owner when known.
5. Keep numbering continuous across alignment rounds.
6. Do not rewrite the baseline spec until changes are confirmed.

## Output Template

```markdown
# Requirement Alignment Log N

Baseline: ...
Date: ...
Participants: ...

| # | Type | Module | Point | Baseline | Current Confirmation | Impact | Status |
|---|------|--------|-------|----------|----------------------|--------|--------|
```

## Status Values

- confirmed
- pending
- rejected
- changed
