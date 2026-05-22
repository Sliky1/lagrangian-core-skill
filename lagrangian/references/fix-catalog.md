# FIX Catalog

The FIX catalog records regression guards that must not be weakened without new eval evidence.

| FIX | Scenario | Guard | Why it exists | No-tool behavior |
|---|---|---|---|---|
| FIX-16 | `safe_rl+adversarial` | `cos_thresh<=0.10`, `window>=20` | Avoids unsafe policy-gradient updates when safety gradient conflicts with reward gradient | Explain required gradient cosine check |
| FIX-17 | `multi_obj+adversarial` | `max_repair=3`, `repair_freq>=10` | Prevents Pareto repair from oscillating or overfitting local front artifacts | Explain Pareto repair concept only |
| FIX-18 | `safe_rl+near_infeasible` | `stage_step<=0.40`, `n_stages∈[5,7]` | Introduces constraints gradually instead of shocking the optimizer | Describe staged relaxation schedule |
| FIX-19 | `natural_lang+degenerate` | Hessian condition number `>1e6` → Tikhonov `ε=1e-4` | Stabilizes ill-conditioned objectives parsed from vague natural language | State regularization would be required if degeneracy is confirmed |
| FIX-21v2 | `non_convex+adversarial` | Halton starts, `thresh=0.010`, `window=3`, `majority_vote` | Improves coverage and reduces random-start blind spots | Do not claim multi-start; recommend Halton initialization |
| FIX-22 | `non_convex+adversarial` | ensemble vote + quarantine + safe direction + trust region | Reduces saddle-trap and adversarial basin failures | Explain the two-layer guard, no fake statistics |
| FIX-23 | `mixed_bayes_opt` pressure | slack buffer or confidence floor `0.6` + staged injection | Prevents posterior uncertainty from destabilizing tight constraints | Request posterior params from external Bayesian skill |
| FIX-24 | degenerate/adversarial output | Step 7 must disclose active protection strategy | Makes hidden recovery logic auditable | Mention the proposed protection, not computed effects |

## Update policy

A FIX parameter may be changed only when the package includes either:

- a new `evals/results/` summary, or
- a clearly labeled experimental branch note stating that the value is provisional.
