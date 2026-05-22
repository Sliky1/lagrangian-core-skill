# lagrangian-skills


## v1.0.0 Complete Release Standard

This package is a complete v1.0.0 release. Completeness is defined by the presence of the core skill, reference docs, golden tests, eval scenarios, schemas, release notes, security policy, contribution policy, and a passing release validator.

Run:

```bash
python scripts/check_release.py
python evals/run_eval.py
```

Expected result: both commands pass with exit code 0.

A stable Agent Skill for constrained optimization using Augmented Lagrangian Methods (ALM), ADMM, KKT-style verification, infeasibility diagnosis, and capability-aware no-tool fallback. It is designed for agents that need to reason about budgets, capacities, safety limits, equality/inequality constraints, multi-objective trade-offs, and softenable logic constraints.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v1.0.0-blue.svg)](lagrangian/SKILL.md)
[![Measured Success Rate](https://img.shields.io/badge/measured%20success-96.78%25-brightgreen.svg)](evals/)
[![Target](https://img.shields.io/badge/target-98.5%25-lightgrey.svg)](evals/)

## What this skill does

Most agents can describe Lagrange multipliers, but often fail to normalize the model, verify feasibility, route the problem type correctly, or admit when a numerical solver is unavailable. This skill enforces a guarded workflow:

- model normalization before solver routing;
- feasibility, units, and mixed-problem prechecks;
- ALM/ADMM/KKT-style route selection;
- explicit no-fabrication rules for no-tool environments;
- structured failure outputs and recovery suggestions;
- cross-skill handoff for Bayesian-optimization hybrids;
- regression guards for known failure modes;
- security guards against task text that attempts to disable verification.

## Quick install

### Claude Code

```bash
git clone https://github.com/Sliky1/lagrangian-skills.git /tmp/lagrangian-skills
mkdir -p ~/.claude/skills
cp -r /tmp/lagrangian-skills/lagrangian ~/.claude/skills/
```

### Other compatible agents

```bash
git clone https://github.com/Sliky1/lagrangian-skills.git /tmp/lagrangian-skills
cp -r /tmp/lagrangian-skills/lagrangian/ ~/.config/agents/skills/lagrangian/
```

## Directory structure

```text
lagrangian-skills/
  lagrangian/
    SKILL.md
    references/
      solver-routing.md
      fix-catalog.md
      output-templates.md
      failure-codes.md
      domain-patterns.md
      examples.md
  tests/golden/
  evals/
    scenarios/
    results/
    ablation/
    run_eval.py
```

## Supported problem types

| Problem type | Behavior | Boundary |
|---|---|---|
| Convex QP / linear allocation | Standard solver or analytic KKT | Global optimum only if solved/proven |
| Smooth NLP | SQP/IPM/ALM route | Usually local optimum unless convexity proven |
| Non-convex NLP | ALM + Halton multi-start + FIX-22 guard | No global claim without proof |
| Distributed optimization | ADMM route | Residuals only if computed |
| Safe RL constraints | ALM / constrained policy route | FIX-16 and FIX-18 for pressure cases |
| Multi-objective | Weighted sum, epsilon constraint, Pareto repair | Preference required for a single final answer |
| Bayesian-optimization hybrid | COOP handoff | Posterior parameters are not fabricated |
| OR / conditional constraints | Smooth approximation or case split | Exact integer/MIP solution is out of scope |

## v1.0.0 release highlights

- Promoted the package to a stable v1.0.0 structure.
- Kept `SKILL.md` as the executable core and moved detailed material to `references/`.
- Added output templates, failure-code definitions, solver routing, domain-pattern translation, and examples.
- Added `tests/golden/` behavioral regression cases.
- Added `evals/scenarios/`, `evals/results/`, `evals/ablation/`, and `evals/run_eval.py` scaffolding.
- Preserved the measured public benchmark figure as inherited from v0.9.3 rather than inventing a new v1.0 benchmark.
- Strengthened no-tool and security wording: no fake optima, residuals, multipliers, cache hits, posterior parameters, or multi-start results.

## Evals

The included measured result remains the latest public benchmark summary from the v0.9.3 logic benchmark. v1.0.0 adds reproducibility scaffolding and regression tests, but does not claim a new measured result until a fresh model run is recorded in `evals/results/`.

| Scenario | With skill | Without skill |
|---|---:|---:|
| convex_qp + normal | 99.8% | ~91% |
| non_convex + adversarial | 96.8% | ~71% |
| safe_rl + near_infeasible | 99.1% | ~68% |
| mixed_bayes + adversarial | 96.0% | ~60% |
| natural_lang + degenerate | 95.2% | ~55% |

Run the scenario structure checker:

```bash
python evals/run_eval.py
```

## Why the skill is written in mixed Chinese and English

The skill uses Chinese for compact behavioral constraints and English for technical identifiers, JSON keys, algorithm names, and parameter names. This keeps the execution rules compact while preserving alignment with optimization terminology.

## License

MIT — see [LICENSE](LICENSE).
