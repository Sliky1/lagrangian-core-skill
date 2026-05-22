# Solver Routing

This table is normative for v1.0.0. Use it after Step 1 model normalization and Step 2 problem classification.

| Classification | Required checks | Route | Output rule |
|---|---|---|---|
| `convex_qp` | convexity, bounds, units | standard convex solver or analytic KKT | Report global optimum only if solved or analytically proven |
| `smooth_nlp` | differentiability, constraint qualification | SQP/IPM/ALM | Report local optimum unless convexity proven |
| `non_convex` | scale, bounds, saddle risk | ALM + Halton multi-start + FIX-22 guard | Never claim global optimum without proof |
| `distributed` | separability, consensus variable | ADMM | Report primal/dual residuals only if computed |
| `safe_rl` | safety constraint type, policy gradient availability | constrained policy optimization / ALM guard | Use FIX-16/FIX-18 in adversarial or near-infeasible cases |
| `multi_obj` | objective scales, preference weights | weighted sum, epsilon constraint, Pareto repair | Show trade-off interpretation, not single “best” unless preference given |
| `mixed_bayes_opt` | prior/posterior terms and optimization target | COOP handoff, staged injection | Do not fabricate posterior parameters |
| `mip_or_discrete` | whether continuous relaxation is acceptable | smooth approximation / case split / halt | Exact integer solution is out of scope |
| `out_of_scope` | task not constrained optimization | FAILED `OUT_OF_SCOPE` | Suggest relevant skill class |

## Near-infeasible routing

A problem is near-infeasible when strict feasibility is fragile, constraints have tiny slack, or a small data perturbation flips feasibility. When tools are available, compute minimal relaxation or slack-buffer sensitivity. Without tools, explain which constraints are likely in conflict and what data is required.

## No-tool routing

When no solver is available, do not route to a fake solver. Provide:

1. normalized mathematical model,
2. feasibility logic checks,
3. recommended solver and required inputs,
4. caveat that no numerical optimum has been computed.
