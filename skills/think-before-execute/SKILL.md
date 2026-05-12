---
name: think-before-execute
description: Use before non-trivial coding, file edits, architecture decisions, bug fixes, refactors, or implementation work to check scope, assumptions, safety, compatibility, and execution fit.
---

# Think Before Execute

## Purpose

Prevent avoidable engineering drift before action starts.

## Workflow

1. Classify the task: simple edit, bug fix, feature, refactor, architecture decision, or read-only analysis.
2. Confirm the smallest useful change that satisfies the user.
3. Identify assumptions, unclear inputs, public API risks, dependency risks, and security red lines.
4. Check the existing project pattern before inventing a new one.
5. Decide whether to execute directly, ask one focused question, or split the task.
6. After execution, verify with the lightest test or inspection that matches the risk.

## Guardrails

- Prefer local fixes over broad rewrites.
- Preserve backward compatibility unless the user explicitly asks for a breaking change.
- Do not introduce dependencies for small tasks without a clear payoff.
- Do not hardcode secrets or private credentials.
- Do not rewrite unrelated code just because it looks improvable.

## Output

Use this skill internally. Only surface assumptions, blockers, or tradeoffs that materially affect the user's decision.
