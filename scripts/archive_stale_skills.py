#!/usr/bin/env python3
"""Placeholder for archive workflow.

This script is intentionally conservative. It should suggest archive actions before moving files.
"""


def should_archive(record: dict) -> bool:
    return record.get("usage_frequency", 0) == 0 and record.get("staleness_risk", 0) >= 3
