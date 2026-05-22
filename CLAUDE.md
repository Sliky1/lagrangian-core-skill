# CLAUDE.md

This repository contains the `lagrangian` Agent Skill.

## Version

Current package version: **v1.0.0**

## Skill entrypoint

```text
lagrangian/SKILL.md
```

`SKILL.md` is the executable core. Detailed reference material lives in:

```text
lagrangian/references/
```

## Development rules

When editing this skill:

1. Keep no-tool behavior strict: never allow fabricated optima, multipliers, residuals, cache hits, posterior parameters, or multi-start statistics.
2. Keep exact integer/MIP solving out of scope unless the user accepts approximation, relaxation, or case split.
3. Preserve the structured failure contract.
4. Update `tests/golden/` when adding a new behavior.
5. Update `evals/scenarios/` when adding a new benchmark scenario.
6. Do not claim a new measured success rate unless a new result file is added to `evals/results/`.

## Lightweight validation

```bash
python evals/run_eval.py
```

This validates scenario file structure. It does not run a model or solver.
