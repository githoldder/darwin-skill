#!/usr/bin/env python3
"""Bucket remaining inventory assets for phase 3 triage."""

from __future__ import annotations

import json
from collections import Counter
from datetime import date
from pathlib import Path


PHASE2_SOURCE_SUFFIXES = {
    "skills_library/before_analyese.md",
    "03_项目三层规训框架.md",
    "06_vibe-coding-CLI-token节省范式.md",
    "08_vibe-coding流水线构建与Skill蒸馏.md",
    "09_vibe-coding-Harness工程规范.md",
    "18_行研信源获取SOP.md",
    "07_vibe-coding-Git版本管理SOP.md",
    "12_AI-Figma建模与二次修改SOP.md",
    "04_需求访谈与分析SOP.md",
    "20_目标拆解与根因分析框架（OKRTS+5W）.md",
}

CONTINUE_SKILL_KEYWORDS = (
    "SOP",
    "工作流",
    "流程",
    "指南",
    "skill",
    "需求",
    "调研",
    "周报",
    "论文",
    "Scrum",
    "产品开发",
)

REFERENCE_KEYWORDS = (
    "模板",
    "规范",
    "索引",
    "README",
    "模型",
    "框架",
    "叙事",
    "标准",
)

SCRIPTABLE_KEYWORDS = (
    "简易待办事项",
    "Dataview",
    "Remove_URLs",
    "Generate_table_of_contents",
    "Generate_glossary",
    "Translate_to_Chinese",
    "Fix_grammar_and_spelling",
    "Summarize",
    "Make_shorter",
    "Make_longer",
    "Emojify",
    "Rewrite_as_tweet",
)

ARCHIVE_KEYWORDS = (
    "未命名",
    "示例",
    "入口",
)


def matches_any(text: str, keywords: tuple[str, ...]) -> bool:
    lower = text.lower()
    return any(keyword.lower() in lower for keyword in keywords)


def assign_bucket(asset: dict) -> tuple[str, str]:
    name = asset["relative_path"]
    display = f"{asset['file_name']} {asset.get('name', '')}"
    line_count = asset["line_count"]

    if matches_any(display, SCRIPTABLE_KEYWORDS):
        return "scriptable", "Highly repetitive prompt-like transform with stable input/output."
    if matches_any(display, ARCHIVE_KEYWORDS) and line_count < 60:
        return "archive", "Low-context utility or fragment better kept outside the active path."
    if asset["layer"] == "inbox" and line_count < 40:
        return "archive", "Thin or weakly classified asset with limited standalone value."
    if line_count > 420 or matches_any(display, REFERENCE_KEYWORDS):
        return "reference", "Long-form framework, template, or standards material better kept as reference."
    if matches_any(display, CONTINUE_SKILL_KEYWORDS) or asset["layer"] == "methods":
        return "continue_skill", "Reusable workflow with enough task structure to justify future distillation."
    return "reference", "Useful context, but not yet strong enough to become an active skill."


def main() -> None:
    index = json.loads(Path("registry/skills_index.json").read_text(encoding="utf-8"))
    remaining = [
        asset
        for asset in index["skills"]
        if asset["relative_path"] not in PHASE2_SOURCE_SUFFIXES
    ]

    buckets: dict[str, list[dict]] = {
        "continue_skill": [],
        "reference": [],
        "scriptable": [],
        "archive": [],
    }

    for asset in remaining:
        bucket, reason = assign_bucket(asset)
        buckets[bucket].append(
            {
                "relative_path": asset["relative_path"],
                "source_path": asset["source_path"],
                "layer": asset["layer"],
                "line_count": asset["line_count"],
                "reason": reason,
            }
        )

    counts = Counter({bucket: len(items) for bucket, items in buckets.items()})
    payload = {
        "schema_version": "0.1.0",
        "generated_on": str(date.today()),
        "scope": {
            "inventory_total": len(index["skills"]),
            "excluded_phase2_assets": len(PHASE2_SOURCE_SUFFIXES),
            "remaining_assets_bucketed": len(remaining),
        },
        "summary": dict(counts),
        "buckets": buckets,
    }
    Path("registry/phase3_asset_buckets.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
