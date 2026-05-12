#!/usr/bin/env python3
"""Deterministic text-transform utilities for Darwin skill assets."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


URL_PATTERN = re.compile(r"https?://\S+")
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")


def read_input(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def write_output(text: str, output: str | None) -> None:
    if output:
        Path(output).write_text(text, encoding="utf-8")
        return
    sys.stdout.write(text)


def remove_urls(text: str) -> str:
    cleaned = URL_PATTERN.sub("", text)
    return re.sub(r"[ \t]+\n", "\n", cleaned)


def normalize_whitespace(text: str) -> str:
    lines = [re.sub(r"[ \t]+$", "", line) for line in text.splitlines()]
    collapsed: list[str] = []
    blank_streak = 0
    for line in lines:
        if line.strip():
            blank_streak = 0
            collapsed.append(line)
        else:
            blank_streak += 1
            if blank_streak <= 1:
                collapsed.append("")
    return "\n".join(collapsed).rstrip() + "\n"


def slugify(title: str) -> str:
    slug = re.sub(r"[^\w\u4e00-\u9fff -]", "", title.lower()).strip()
    slug = slug.replace(" ", "-")
    return slug or "section"


def markdown_toc(text: str, max_level: int = 3) -> str:
    rows = []
    for line in text.splitlines():
        match = HEADING_PATTERN.match(line)
        if not match:
            continue
        level = len(match.group(1))
        if level > max_level:
            continue
        title = match.group(2).strip()
        indent = "  " * (level - 1)
        rows.append(f"{indent}- [{title}](#{slugify(title)})")
    return ("\n".join(rows) + "\n") if rows else ""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run deterministic text transforms.")
    parser.add_argument("--input", "-i", help="Read text from a file instead of stdin.")
    parser.add_argument("--output", "-o", help="Write transformed text to a file instead of stdout.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("remove-urls", help="Remove HTTP(S) URLs from text.")
    subparsers.add_parser("normalize-whitespace", help="Trim trailing spaces and collapse repeated blank lines.")
    toc_parser = subparsers.add_parser("markdown-toc", help="Generate a Markdown table of contents.")
    toc_parser.add_argument("--max-level", type=int, default=3, help="Maximum heading depth to include.")
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    text = read_input(args.input)

    if args.command == "remove-urls":
        result = remove_urls(text)
    elif args.command == "normalize-whitespace":
        result = normalize_whitespace(text)
    elif args.command == "markdown-toc":
        result = markdown_toc(text, max_level=args.max_level)
    else:
        raise SystemExit(f"Unsupported command: {args.command}")

    write_output(result, args.output)


if __name__ == "__main__":
    main()
