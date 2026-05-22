# Lagrangian Skills v1.0.0 Manifest

This is the complete v1.0.0 release manifest for the `lagrangian` skill package.

## Package identity

- Package: `lagrangian-skills`
- Skill id: `lagrangian`
- Release: `v1.0.0`
- Status: stable
- Scope: constrained optimization reasoning, Lagrangian formulation, KKT checks, solver routing, feasibility triage, and optimization output rendering.

## Included release assets

| Path | Purpose | Required for v1.0 |
|---|---|---:|
| `lagrangian/SKILL.md` | Main skill entrypoint | Yes |
| `lagrangian/references/` | Detailed reusable reference docs | Yes |
| `tests/golden/` | Golden behavioral test cases | Yes |
| `evals/scenarios/` | Machine-readable eval scenarios | Yes |
| `evals/results/` | Historical and template result files | Yes |
| `evals/ablation/` | FIX ablation summary | Yes |
| `scripts/check_release.py` | Release completeness validator | Yes |
| `scripts/run_eval.py` | Eval scenario structure checker | Yes |
| `schemas/` | JSON schemas for outputs and eval cases | Yes |
| `docs/` | Installation, usage, quality, release and governance docs | Yes |
| `archive/` | Historical skill snapshots | Yes |

## Completeness rule

A release is considered complete only when `python scripts/check_release.py` passes with exit code 0.
