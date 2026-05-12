#!/usr/bin/env python3
"""Scan local markdown skills and produce a Darwin skills inventory.

Examples:
  python3 scripts/scan_skills.py /path/to/04-skills
  python3 scripts/scan_skills.py /path/to/04-skills --output registry/skills_index.json
"""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TRIGGER_KEYWORDS = (
    "description:",
    "trigger",
    "触发",
    "when to use",
    "use when",
    "适用",
    "使用场景",
)

METHOD_KEYWORDS = ("sop", "流程", "工作流", "pipeline", "流水线", "checklist", "清单", "规范")
MODEL_KEYWORDS = ("框架", "模型", "范式", "原则", "思路", "方法论", "pattern")
PRINCIPLE_KEYWORDS = ("底层", "准则", "原则", "policy", "safeguard", "红线", "思考")
CASE_KEYWORDS = ("案例", "示例", "实操", "harness", "ralph", "figma", "latex", "valyu")


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    match = re.match(r"^---\s*\n(.*?)\n---\s*", text, re.DOTALL)
    if not match:
        return {}
    data: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip("\"'")
    return data


def headings(lines: list[str]) -> list[dict[str, Any]]:
    records = []
    for index, line in enumerate(lines, start=1):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if match:
            records.append(
                {
                    "level": len(match.group(1)),
                    "title": match.group(2),
                    "line": index,
                }
            )
    return records


def has_trigger_description(text: str, meta: dict[str, str]) -> bool:
    if meta.get("description"):
        return True
    lower = text[:2500].lower()
    return any(keyword.lower() in lower for keyword in TRIGGER_KEYWORDS)


def classify_layer(path: Path, text: str) -> str:
    signal = f"{path.name}\n{text[:2000]}".lower()
    scores = {
        "principles": sum(keyword.lower() in signal for keyword in PRINCIPLE_KEYWORDS),
        "models": sum(keyword.lower() in signal for keyword in MODEL_KEYWORDS),
        "methods": sum(keyword.lower() in signal for keyword in METHOD_KEYWORDS),
        "cases": sum(keyword.lower() in signal for keyword in CASE_KEYWORDS),
    }
    best_layer, best_score = max(scores.items(), key=lambda item: item[1])
    return best_layer if best_score > 0 else "inbox"


def length_diagnosis(line_count: int) -> str:
    if line_count < 30:
        return "too_short"
    if line_count > 500:
        return "too_long"
    if line_count > 260:
        return "large_but_reviewable"
    return "normal"


def recommend(record: dict[str, Any]) -> str:
    if not record["has_frontmatter"]:
        return "add_skill_frontmatter"
    if not record["has_trigger_description"]:
        return "add_trigger_description"
    if record["length_diagnosis"] == "too_short":
        return "expand_context"
    if record["length_diagnosis"] == "too_long":
        return "split_or_move_references"
    if record["layer"] == "inbox":
        return "classify_layer"
    return "keep_reviewing"


def lifecycle_state(record: dict[str, Any]) -> str:
    if record["recommendation"] in {"add_skill_frontmatter", "add_trigger_description", "expand_context"}:
        return "candidate"
    if record["recommendation"] == "split_or_move_references":
        return "needs_refactor"
    if record["layer"] == "inbox":
        return "inbox"
    return "active"


def inspect_file(path: Path, root: Path) -> dict[str, Any]:
    text = read_text(path)
    lines = text.splitlines()
    meta = frontmatter(text)
    title = meta.get("name") or next((h["title"] for h in headings(lines) if h["level"] == 1), path.stem)
    record: dict[str, Any] = {
        "id": path.with_suffix("").relative_to(root).as_posix(),
        "name": title,
        "file_name": path.name,
        "source_path": str(path),
        "relative_path": path.relative_to(root).as_posix(),
        "line_count": len(lines),
        "char_count": len(text),
        "heading_count": len(headings(lines)),
        "headings": headings(lines)[:20],
        "has_frontmatter": bool(meta),
        "frontmatter_keys": sorted(meta.keys()),
        "has_trigger_description": has_trigger_description(text, meta),
        "layer": classify_layer(path, text),
        "length_diagnosis": length_diagnosis(len(lines)),
    }
    record["recommendation"] = recommend(record)
    record["state"] = lifecycle_state(record)
    return record


def build_index(sources: list[Path]) -> dict[str, Any]:
    records = []
    source_records = []
    for source in sources:
        root = source.expanduser().resolve()
        files = sorted(path for path in root.rglob("*.md") if path.is_file())
        source_records.append({"path": str(root), "file_count": len(files)})
        records.extend(inspect_file(path, root) for path in files)

    layer_counts: dict[str, int] = {}
    state_counts: dict[str, int] = {}
    recommendation_counts: dict[str, int] = {}
    for record in records:
        layer_counts[record["layer"]] = layer_counts.get(record["layer"], 0) + 1
        state_counts[record["state"]] = state_counts.get(record["state"], 0) + 1
        recommendation_counts[record["recommendation"]] = recommendation_counts.get(record["recommendation"], 0) + 1

    return {
        "schema_version": "0.2.0",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "sources": source_records,
        "summary": {
            "total_assets": len(records),
            "layer_counts": layer_counts,
            "state_counts": state_counts,
            "recommendation_counts": recommendation_counts,
        },
        "skills": records,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Scan markdown skill assets.")
    parser.add_argument("sources", nargs="+", type=Path, help="Skill or prompt directories to scan.")
    parser.add_argument("--output", "-o", type=Path, help="Write JSON inventory to this path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    index = build_index(args.sources)
    payload = json.dumps(index, ensure_ascii=False, indent=2)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)


if __name__ == "__main__":
    main()
