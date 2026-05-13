# Package Guide

Version: `v1.0.0`

## Package Profiles

### Full

Use the repository root as the package root.

Full includes:

- Darwin core skills
- author-provided skills
- scripts
- registry files
- library references
- templates
- logo assets

Plugin descriptor:

```text
.codex-plugin/plugin.json
```

### Pure

Pure is for users who want the Darwin mechanism without the author's personal skills.

Plugin descriptor:

```text
packages/pure/.codex-plugin/plugin.json
```

Recommended Pure contents:

```text
packages/pure/.codex-plugin/plugin.json
packages/pure/assets/logo.png
packages/pure/docs/mechanism.md
packages/pure/scripts/archive_stale_skills.py
packages/pure/scripts/scan_skills.py
packages/pure/scripts/score_skills.py
packages/pure/scripts/suggest_refactor.py
packages/pure/skills/darwin-skill-archivist/
packages/pure/skills/darwin-skill-auditor/
packages/pure/skills/darwin-skill-distiller/
packages/pure/skills/darwin-skill-manager/
packages/pure/templates/
packages/pure/README.md
VERSION
```

## Author-Provided Skills

The following skills are bundled only in Full:

- `think-before-execute`
- `project-three-layer-discipline`
- `cli-token-saving-pattern`
- `vibe-skill-pipeline`
- `harness-iteration-engineering`
- `industry-source-research`
- `vibe-git-version-management`
- `ai-figma-vector-production`
- `requirement-alignment-log`
- `okrts-root-cause-analysis`
- `solo-scrum-vibe-workflow`
- `paper-research-workflow`
- `paper-expansion-assistant`
- `document-lifecycle-governance`
- `document-naming-versioning`
- `document-quality-audit`
- `standards-monitoring-task-bank`
- `requirements-doc-update-pipeline`

## Release Notes

`v1.0.0` is the first package-ready release. It defines the project purpose, package profiles, plugin metadata, logo, and source attribution.
