#!/usr/bin/env python3
"""Placeholder for skill refactor suggestions."""


def suggest(record: dict) -> str:
    line_count = record.get("line_count", 0)
    has_frontmatter = record.get("has_frontmatter", False)
    if line_count > 500:
        return "split_or_move_references"
    if line_count < 30:
        return "expand_context"
    if not has_frontmatter:
        return "add_skill_frontmatter"
    return "keep_reviewing"
