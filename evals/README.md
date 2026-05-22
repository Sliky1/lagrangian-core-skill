# Evals

This directory makes the benchmark claims auditable. The included public result summary is inherited from the v0.9.3 logic benchmark. v1.0.0 adds reproducibility scaffolding, golden tests, scenario definitions, and a lightweight runner, but does **not** claim a newly measured success rate unless `evals/results/v1.0.0-*.csv` is produced by an actual evaluation run.

## Current public summary

| Scenario | With skill | Without skill | Source |
|---|---:|---:|---|
| convex_qp + normal | 99.8% | ~91% | v0.9.3 summary |
| non_convex + adversarial | 96.8% | ~71% | v0.9.3 summary |
| safe_rl + near_infeasible | 99.1% | ~68% | v0.9.3 summary |
| mixed_bayes + adversarial | 96.0% | ~60% | v0.9.3 summary |
| natural_lang + degenerate | 95.2% | ~55% | v0.9.3 summary |

Measured aggregate: **96.78%**. Target for future releases: **98.5%**.

## Directory structure

```text
evals/
  scenarios/       # JSONL scenario definitions
  results/         # CSV summaries and manual review sheets
  ablation/        # FIX-specific ablation summaries
  run_eval.py      # lightweight deterministic checklist runner
```

## Running the lightweight checker

The included runner does not call an LLM. It validates scenario file structure and expected-behavior fields so eval data stays consistent.

```bash
python evals/run_eval.py
```

For real model evaluation, use the JSONL scenarios as prompts, collect model outputs, and manually or programmatically score against the `must` and `must_not` criteria.
