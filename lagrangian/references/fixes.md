# FIX Reference

Compatibility note: this file is kept for older links. The canonical v1.0.0 reference is `fix-catalog.md`.

| FIX | Scenario | Parameter | Value / guard |
|---|---|---|---|
| FIX-16 | safe_rl+adversarial | cos_thresh | 0.10, never >0.20 |
| FIX-16 | safe_rl+adversarial | window | 20, never <15 |
| FIX-17 | multi_obj+adversarial | repair_freq | 10, never <5 |
| FIX-18 | safe_rl+near_infeasible | stage_step | 0.25, never >0.40 |
| FIX-18 | safe_rl+near_infeasible | n_stages | 6, must be in [5,7] |
| FIX-19 | natural_lang+degenerate | epsilon | 1e-4 Tikhonov when Hessian condition number >1e6 |
| FIX-21v2 | non_convex+adversarial | sequence | Halton, not uniform random |
| FIX-21v2 | non_convex+adversarial | thresh | 0.010, never >0.020 |
| FIX-21v2 | non_convex+adversarial | window | 3 |
| FIX-22 | non_convex+adversarial | Layer B | ensemble_vote, quarantine=5, safe_direction fallback |
| FIX-22 | non_convex+adversarial | Layer A | adaptive_trust_region, proj_radius=0.10, restart_thresh=5 |
| FIX-23 | mixed_bayes+near_infeasible | strategy | slack_buffer + staged injection |
| FIX-23 | mixed_bayes+adversarial | strategy | confidence_floor(0.6) + staged injection |
| FIX-24 | degenerate/adversarial output | disclosure | Step 7 must mention active protection strategy |

## Evidence policy

The public package includes summary evidence in `evals/results/v0.9.3-summary.csv` and ablation summaries in `evals/ablation/`. Raw simulation data is not included unless separately added. Do not claim a fresh measured benchmark without adding new result files.
