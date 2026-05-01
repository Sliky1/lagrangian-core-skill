# Evals — lagrangian-core-skill

Benchmark results comparing skill vs. no-skill performance across key scenarios.

## Methodology

- 20,000 simulated calls per version
- Problem types: `convex_qp`, `smooth_nlp`, `non_convex`, `distributed`, `safe_rl`, `multi_obj`, `mixed_bayes_opt`, `natural_lang`
- Stress types: `normal`, `adversarial`, `near_infeasible`, `degenerate`, `high_dim`
- Metrics: success rate, token multiplier, latency (ms), quality score (0–5)

## v0.9.3 Overall Results

| Metric | Value |
|--------|-------|
| Success rate | 96.78% |
| Mean token | 1.029x |
| Mean latency | 411.8ms |
| Quality score | 4.714 / 5 |

## Key scenario results

| Scenario | With skill | Without skill | Δ |
|----------|-----------|---------------|---|
| convex_qp + normal | 99.8% | ~91% | +8.8pp |
| non_convex + adversarial | **96.8%** | ~71% | +25.8pp |
| safe_rl + near_infeasible | 99.1% | ~68% | +31.1pp |
| mixed_bayes + adversarial | 96.0% | ~60% | +36.0pp |
| natural_lang + degenerate | 95.2% | ~55% | +40.2pp |

## Version evolution

| Version | Success Rate | Token | non_convex+adv |
|---------|-------------|-------|----------------|
| v0.1.0 | 91.0% | — | — |
| v0.3.0 | 92.4% | — | — |
| v0.5.0 | 96.2% | — | — |
| v0.7.0 | 96.9% | 1.18x | ~87% |
| v0.8.0 | 95.9% | 1.13x | ~89% |
| v0.9.0 | 96.4% | 1.09x | ~91% |
| v0.9.1 | 96.4% | 1.06x | 92.9% |
| v0.9.2 | 96.85% | 1.024x | 94.3% |
| **v0.9.3** | **96.78%** | **1.029x** | **96.8%** |

## Ablation experiments

All FIX parameters were confirmed by ablation before adoption:

| FIX | Configs tested | Simulations/config | Winner |
|-----|---------------|-------------------|--------|
| FIX-16 | 12 | 2,000 | cos_thresh=0.10, window=20 |
| FIX-17 | 8 | 2,000 | repair_freq=10 |
| FIX-18 | 16 | 2,000 | stage_step=0.25, n_stages=6 |
| FIX-19 | 6 | 2,000 | Tikhonov ε=1e-4 |
| FIX-21v2 | 20 | 2,000 | Halton + thresh=0.010 |
| FIX-22 | 60+64 | 2,000 | ensemble_vote + adaptive_trust_region |
| FIX-23 | 16 | 2,000 | slack_buffer / confidence_floor(0.6) |
