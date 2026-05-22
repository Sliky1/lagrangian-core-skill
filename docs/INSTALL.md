# Installation Guide

## Minimal installation

Copy the `lagrangian/` directory into the host agent's skills directory.

## Full package installation

Keep the full repository layout when you want testability, reproducibility, and release governance:

```text
lagrangian-skills/
  lagrangian/
  tests/
  evals/
  scripts/
  schemas/
  docs/
```

## Validation after installation

Run:

```bash
python scripts/check_release.py
python evals/run_eval.py
```

Both commands should exit with code 0.

## Host capability assumptions

This skill does not require a numerical solver to be useful. When no solver or Python runtime is available, it must operate in `NO_TOOL` mode and avoid fabricated numeric optima, KKT residuals, multipliers, solver convergence claims, or cached results.
