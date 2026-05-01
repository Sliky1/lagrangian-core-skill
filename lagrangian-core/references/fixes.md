# FIX Reference — lagrangian-core

Quick reference for all documented fixes and their parameter constraints.

| FIX | Scenario | Parameter | Value | Constraint |
|-----|----------|-----------|-------|------------|
| FIX-16 | safe_rl+adversarial | cos_thresh | 0.10 | ≤0.20 |
| FIX-16 | safe_rl+adversarial | window | 20 | ≥15 |
| FIX-17 | multi_obj+adversarial | repair_freq | 10 | ≥5 |
| FIX-18 | safe_rl+near_infeas | stage_step | 0.25 | ≤0.40 |
| FIX-18 | safe_rl+near_infeas | n_stages | 6 | ∈[5,7] |
| FIX-19 | natural_lang+degenerate | epsilon | 1e-4 | Tikhonov |
| FIX-21v2 | non_convex+adversarial | thresh | 0.010 | ≤0.020 |
| FIX-21v2 | non_convex+adversarial | window | 3 | — |
| FIX-21v2 | non_convex+adversarial | sequence | Halton | not uniform |
| FIX-22 | non_convex+adversarial | Layer B detect | ensemble_vote | — |
| FIX-22 | non_convex+adversarial | quarantine | 5 | — |
| FIX-22 | non_convex+adversarial | fallback | safe_direction | — |
| FIX-22 | non_convex+adversarial | proj_mode | adaptive_trust_region | — |
| FIX-22 | non_convex+adversarial | proj_radius | 0.10 | — |
| FIX-22 | non_convex+adversarial | restart_thresh | 5 | — |
| FIX-23 | mixed_bayes+near_infeas | strategy | slack_buffer+staged | — |
| FIX-23 | mixed_bayes+adversarial | strategy | confidence_floor(0.6)+staged | — |

## Ablation methodology

All parameters confirmed by ablation:
- N ≥ 2,000 simulations per config
- Primary score = success_rate × 0.70 − token_extra × 2.0
- Secondary score (sr-first) = success_rate × 0.85 − token_extra × 0.8
- Final benchmark: 20,000-call simulation per version

## Language conventions

| Content type | Language | Reason |
|---|---|---|
| Technical identifiers / algorithm names / parameter names | English | Training corpus is English; higher attention weight on technical vocabulary |
| JSON / code blocks | English | Format spec is English |
| Behavioral rules / Forbidden Behaviors | Chinese | Higher information density; no subordinate clause ambiguity |
| Numeric parameters (`thresh=0.010`) | English | Universal format |
