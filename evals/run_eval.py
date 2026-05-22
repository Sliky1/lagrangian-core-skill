#!/usr/bin/env python3
"""Lightweight scenario-structure checker for lagrangian-skills.

This script intentionally does not call an LLM or solver. It validates that JSONL
scenario files are well formed and include the fields needed for manual or
external automated scoring.
"""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCENARIOS = ROOT / "scenarios"
REQUIRED = {"id", "category", "stress", "prompt", "must", "must_not"}


def validate_file(path: Path) -> tuple[int, list[str]]:
    errors: list[str] = []
    count = 0
    for line_no, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        count += 1
        try:
            obj = json.loads(line)
        except json.JSONDecodeError as exc:
            errors.append(f"{path.name}:{line_no}: invalid JSON: {exc}")
            continue
        missing = REQUIRED - obj.keys()
        if missing:
            errors.append(f"{path.name}:{line_no}: missing fields {sorted(missing)}")
        for key in ("must", "must_not"):
            if key in obj and not isinstance(obj[key], list):
                errors.append(f"{path.name}:{line_no}: {key} must be a list")
        if not str(obj.get("prompt", "")).strip():
            errors.append(f"{path.name}:{line_no}: empty prompt")
    return count, errors


def main() -> int:
    files = sorted(SCENARIOS.glob("*.jsonl"))
    if not files:
        print("No scenario files found.")
        return 1
    total = 0
    all_errors: list[str] = []
    for path in files:
        count, errors = validate_file(path)
        total += count
        all_errors.extend(errors)
    if all_errors:
        print("FAILED")
        for err in all_errors:
            print(f"- {err}")
        return 1
    print(f"OK: validated {total} scenarios across {len(files)} files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
