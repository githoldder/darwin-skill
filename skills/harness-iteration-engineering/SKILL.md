---
name: harness-iteration-engineering
description: Use when planning long-running AI agent execution with task queues, fresh-context iterations, progress logs, git checkpoints, tests, and completion criteria.
---

# Harness Iteration Engineering

## Purpose

Keep long AI work from drifting by externalizing memory into files and checkpoints.

## Three-Part Memory

- Task list: what remains to be done.
- Progress log: what was tried, learned, fixed, or blocked.
- Git commits: recoverable checkpoints for completed slices.

## Workflow

1. Turn the goal into small tasks with acceptance criteria.
2. Process one task per iteration when the work is complex.
3. Read the task list and progress log at the start of each iteration.
4. Implement, test, and record what changed.
5. Commit at stable milestones.
6. Stop only when all tasks meet completion criteria.

## Quality Checks

- No hidden TODOs are treated as done.
- Each iteration leaves a trace in code, tests, logs, or commits.
- The next iteration can resume without relying on chat memory.
