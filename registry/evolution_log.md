# Evolution Log

记录 Skill 的创建、拆分、合并、归档、废弃和升级决策。

## 2026-05-12 - Phase 1 bootstrap

- Created the four-layer `library/` structure: principles, models, methods, cases.
- Migrated the first 6 core assets from the local `04-skills` directory.
- Upgraded `scripts/scan_skills.py` to generate a structured inventory with layer, lifecycle, length, trigger, frontmatter, and recommendation fields.
- Generated `registry/skills_index.json` from the local `04-skills` and `提示词工程` directories.
- Current scan result: 85 markdown assets; 67 need standard skill frontmatter and 16 need clearer trigger descriptions.

## 2026-05-13 - Phase 2 small-batch distillation

- Selected 10 high-value candidates from the 85-asset inventory.
- Added `name` and `description` frontmatter to the migrated library copies.
- Distilled 10 active skills under `skills/*/SKILL.md`.
- Added `registry/phase2_candidates.json` to preserve candidate-to-skill lineage.
- Generated `registry/active_skills_index.json`; current active skill count is 14 including the Darwin core skills.
