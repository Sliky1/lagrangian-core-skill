#!/usr/bin/env python3
"""Release completeness validator for lagrangian-skills v1.0.0."""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "VERSION",
    "README.md",
    "CHANGELOG.md",
    "CLAUDE.md",
    "LICENSE",
    "MANIFEST.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "docs/INSTALL.md",
    "docs/USAGE.md",
    "docs/QUALITY_GATE.md",
    "docs/RELEASE_NOTES.md",
    "lagrangian/SKILL.md",
    "lagrangian/references/solver-routing.md",
    "lagrangian/references/fix-catalog.md",
    "lagrangian/references/fixes.md",
    "lagrangian/references/output-templates.md",
    "lagrangian/references/failure-codes.md",
    "lagrangian/references/domain-patterns.md",
    "lagrangian/references/examples.md",
    "tests/README.md",
    "tests/golden/INDEX.md",
    "evals/README.md",
    "evals/run_eval.py",
    "evals/results/v0.9.3-summary.csv",
    "evals/results/v1.0.0-regression-template.csv",
    "evals/ablation/fix_ablation_summary.csv",
    "schemas/failure-output.schema.json",
    "schemas/eval-scenario.schema.json",
    "schemas/skill-metadata.schema.json",
]

REQUIRED_SKILL_PHRASES = [
    "version: \"1.0.0\"",
    "Execution Modes",
    "NO_TOOL",
    "Security Guards",
    "Step 1",
    "Step 2",
    "AMBIGUOUS",
    "OUT_OF_SCOPE",
    "不得",
]


def fail(msg: str) -> None:
    print(f"RELEASE CHECK FAILED: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    for rel in REQUIRED_FILES:
        path = ROOT / rel
        if not path.exists() or path.stat().st_size == 0:
            fail(f"missing or empty required file: {rel}")

    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    if version != "1.0.0":
        fail(f"VERSION must be 1.0.0, got {version!r}")

    skill = (ROOT / "lagrangian" / "SKILL.md").read_text(encoding="utf-8")
    for phrase in REQUIRED_SKILL_PHRASES:
        if phrase not in skill:
            fail(f"SKILL.md missing phrase: {phrase}")
    if "字桑" in skill:
        fail("SKILL.md still contains typo 字桑")
    if len(skill.splitlines()) > 220:
        fail("SKILL.md is too long for v1.0 entrypoint (>220 lines)")

    golden = sorted((ROOT / "tests" / "golden").glob("[0-9][0-9]_*.md"))
    if len(golden) < 8:
        fail(f"expected at least 8 golden tests, got {len(golden)}")

    scenario_files = sorted((ROOT / "evals" / "scenarios").glob("*.jsonl"))
    if len(scenario_files) < 8:
        fail(f"expected at least 8 scenario files, got {len(scenario_files)}")
    scenario_count = 0
    for file in scenario_files:
        for line_no, line in enumerate(file.read_text(encoding="utf-8").splitlines(), 1):
            if not line.strip():
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError as exc:
                fail(f"invalid JSONL in {file.name}:{line_no}: {exc}")
            for key in ("id", "category", "stress", "prompt", "must", "must_not"):
                if key not in obj:
                    fail(f"scenario {file.name}:{line_no} missing {key}")
            if not isinstance(obj["must"], list) or not obj["must"]:
                fail(f"scenario {file.name}:{line_no} must must be a non-empty list")
            if not isinstance(obj["must_not"], list):
                fail(f"scenario {file.name}:{line_no} must_not must be a list")
            scenario_count += 1
    if scenario_count < 8:
        fail(f"expected at least 8 scenario records, got {scenario_count}")

    # CSV sanity checks
    for rel in ["evals/results/v0.9.3-summary.csv", "evals/results/v1.0.0-regression-template.csv", "evals/ablation/fix_ablation_summary.csv"]:
        with (ROOT / rel).open(newline="", encoding="utf-8") as f:
            rows = list(csv.reader(f))
        if len(rows) < 2:
            fail(f"CSV must include header plus data/template row: {rel}")

    # Schema sanity checks
    for schema_path in (ROOT / "schemas").glob("*.json"):
        json.loads(schema_path.read_text(encoding="utf-8"))

    print("RELEASE CHECK PASSED: lagrangian-skills v1.0.0 is complete.")


if __name__ == "__main__":
    main()
