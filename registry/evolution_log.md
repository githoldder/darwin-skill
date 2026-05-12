# Evolution Log

记录 Skill 的创建、拆分、合并、归档、废弃和升级决策。

## 2026-05-12 - Phase 1 bootstrap

- Created the four-layer `library/` structure: principles, models, methods, cases.
- Migrated the first 6 core assets from the local `04-skills` directory.
- Upgraded `scripts/scan_skills.py` to generate a structured inventory with layer, lifecycle, length, trigger, frontmatter, and recommendation fields.
- Generated `registry/skills_index.json` from the local `04-skills` and `提示词工程` directories.
- Current scan result: 85 markdown assets; 67 need standard skill frontmatter and 16 need clearer trigger descriptions.
