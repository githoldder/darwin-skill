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

## 2026-05-13 - Phase 3 asset bucketing

- Bucketed the remaining 75 inventory assets after excluding the 10 phase-2 distillations.
- Added `scripts/bucket_phase3_assets.py` so the bucketing pass can be regenerated.
- Added `registry/phase3_asset_buckets.json`.
- Current machine-assisted split: 19 continue-to-skill, 40 reference, 13 scriptable, 3 archive.
- Added `docs/phase3_bucket_plan.md` to document the decision logic and next-stage work.

## 2026-05-13 - Phase 3 execution batch 1

- Selected 8 assets from the continue-to-skill bucket.
- Migrated their source material into `library/` with `name` and `description` frontmatter.
- Distilled 8 new active skills for sprint workflow, paper research, paper expansion, document governance, document naming, document audit, standards monitoring, and requirements sync.
- Added `registry/phase3_batch1_candidates.json`.
- Refreshed `registry/active_skills_index.json`; active skill inventory now contains 22 skill files.
- Designed the first `text-transform` script family with `scripts/text_transform.py`, `docs/text_transform_family.md`, and `registry/text_transform_family.json`.
