---
name: vibe-git-version-management
description: Use when managing AI-driven coding work with git initialization, checkpoints, branch isolation, commits, rollback safety, and clear work summaries.
---

# Vibe Git Version Management

## Workflow

1. Check repository state before editing or committing.
2. Initialize git only when the project is not already under version control.
3. Use branches for risky features, bug fixes, or parallel work.
4. Commit at stable milestones with clear messages.
5. Before rollback or destructive operations, inspect history and ask when user work could be lost.
6. Summarize changed files, commit hash, and remaining risks after committing.

## Branching Rules

- Keep `main` stable.
- Use feature or fix branches for isolated work.
- Merge only after verification.
- Preserve user changes that are outside the current task.

## Verification

Run the relevant test, build, or inspection before commit when feasible. If not feasible, state what was not verified.
