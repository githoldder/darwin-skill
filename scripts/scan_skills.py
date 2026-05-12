#!/usr/bin/env python3
"""Scan local markdown skills and produce a lightweight inventory.

Usage:
  python3 scripts/scan_skills.py /path/to/skills
"""

from pathlib import Path
import json
import sys


def inspect_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    headings = [line.strip() for line in lines if line.startswith("#")]
    return {
        "path": str(path),
        "name": path.stem,
        "line_count": len(lines),
        "heading_count": len(headings),
        "has_frontmatter": text.startswith("---"),
        "state": "inbox",
        "layer": None,
        "recommendation": None,
    }


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage: scan_skills.py /path/to/skills")
    root = Path(sys.argv[1]).expanduser()
    files = sorted(root.rglob("*.md"))
    records = [inspect_file(path) for path in files if path.is_file()]
    print(json.dumps({"source": str(root), "skills": records}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
