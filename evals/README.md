# Evals — lagrangian-core-skill

Benchmark results comparing skill vs. no-skill performance across key scenarios.

## Methodology

- 20,000 simulated calls per version
- Problem types: `convex_qp`, `smooth_nlp`, `non_convex`, `distributed`, `safe_rl`, `multi_obj`, `mixed_bayes_opt`, `natural_lang`
- Stress types: `normal`, `adversarial`, `near_infeasible`, `degenerate`, `high_dim`
- Metrics: success rate, token multiplier, latency (ms), quality score (0–5)

## v0.9.3 Overall Results

| Metric | v0.9.2 | v0.9.3 | Delta |
|--------|--------|--------|-------|
| Success rate | 96.85% | 96.78% | −0.07pp |
| Mean token | 1.024x | 1.029x | +0.005x |
| Mean latency | 413.7ms | 411.8ms | −1.9ms |
| Quality score | 4.692 | 4.714 | +0.022 |

## Key scenarios

| Scenario | With skill (v0.9.3) | Without skill | Gain |
|----------|--------------------|--------------|----- |
| convex_qp + normal | 99.8% | ~91% | +8.8pp |
| **non_convex + adversarial** | **96.8%** | ~71% | **+25.8pp** |
| safe_rl + near_infeasible | 99.1% | ~68% | +31.1pp |
| mixed_bayes + adversarial | 96.0% | ~60% | +36.0pp |
| natural_lang + degenerate | 95.2% | ~55% | +40.2pp |

## Version evolution

| Version | Success Rate | Token | Notes |
|---------|-------------|-------|-------|
| v0.1.0 | 91.0% | — | Prototype |
| v0.3.0 | 92.4% | — | +ADMM |
| v0.5.0 | 96.2% | — | +multi-start |
| v0.7.0 | 96.9% | 1.18x | +FIX-16/17/18 |
| v0.8.0 | 95.9% | 1.13x | +output modes |
| v0.9.0 | 96.4% | 1.09x | +COOP |
| v0.9.1 | 96.4% | 1.06x | +FIX-19/23 |
| v0.9.2 | 96.85% | 1.024x | +FIX-21v2 |
| **v0.9.3** | **96.78%** | **1.029x** | **+FIX-22** |

## Ablation data

Ablation CSVs for each FIX are available in `ablation/`.
Each CSV contains per-config simulation results (N=2,000 per row) used to select final parameters.
