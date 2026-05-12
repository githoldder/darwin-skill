---
name: cli-token-saving-pattern
description: Use when reducing token cost by replacing repeated AI reasoning, browsing, GUI work, or manual workflows with CLI commands, scripts, templates, or reusable toolchains.
---

# CLI Token Saving Pattern

## Core Idea

Use AI for judgment and generation. Use deterministic tools for repeatable execution.

## Workflow

1. Identify repeated task steps that consume tokens or time.
2. Separate judgment-heavy steps from deterministic steps.
3. Prefer stable CLIs, local scripts, structured files, and logs for repeatable work.
4. Capture successful command combinations in an SOP.
5. Turn the SOP into a script once inputs and outputs stabilize.
6. Save the script, usage example, and failure notes near the relevant skill.

## Good Candidates

- GitHub, deployment, testing, scraping, reporting, document conversion, browser automation, and data extraction.
- Tasks with stable input/output formats.
- Tasks that need to run many times after one successful exploration.

## Avoid

- Automating uncertain workflows before the first successful manual run.
- Treating outdated CLI claims as facts without checking current docs when accuracy matters.
