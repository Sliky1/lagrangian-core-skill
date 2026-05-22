# Contributing

## Change policy

Changes to `lagrangian/SKILL.md` must preserve:

- explicit execution modes;
- no-tool no-fabrication behavior;
- MIP and out-of-scope boundaries;
- prompt-injection resistance;
- structured failure outputs;
- KKT/feasibility verification before numeric claims.

## Required checks before release

```bash
python scripts/check_release.py
python evals/run_eval.py
```

## Adding a new behavior

1. Add or update the rule in `lagrangian/SKILL.md` or `lagrangian/references/`.
2. Add a golden test in `tests/golden/`.
3. Add or update an eval scenario in `evals/scenarios/`.
4. Update `CHANGELOG.md` and `docs/RELEASE_NOTES.md`.

## Versioning

- Patch: wording, examples, or documentation fixes.
- Minor: new behavior category or additional solver-routing logic.
- Major: incompatible output contract or capability-boundary change.
