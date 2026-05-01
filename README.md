# lagrangian-core-skill

An opinionated [Agent Skill](https://agentskills.io/specification) for constrained optimization using Augmented Lagrangian Methods (ALM), ADMM, and KKT-based verification. Compatible with Claude Code, Cursor, Gemini CLI, and any agent that supports the Agent Skills spec.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-v0.9.3-blue.svg)](lagrangian-core/SKILL.md)
[![Success Rate](https://img.shields.io/badge/success%20rate-96.78%25-brightgreen.svg)](evals/)

## What this skill does

Most agents, when handed a constrained optimization problem, will attempt a solution without checking KKT conditions, verifying feasibility, or routing to the right solver. This skill enforces a specific sequence of steps and guardrails that produce reliable, verifiable results.

Key behaviors the agent won't do unprompted — but this skill enforces:

- Pre-flight feasibility check (LP relaxation) before any computation
- KKT condition verification with fingerprint caching (~85% hit rate)
- Halton quasi-random multi-start for non-convex problems (FIX-21)
- Dual-layer adversarial protection for saddle point traps (FIX-22)
- Cross-skill handoff for Bayesian-optimization hybrid problems (COOP)
- Structured failure output with minimum slack recovery suggestions
- Token-efficient output modes: MINIMAL / STANDARD / VERBOSE

## Quick install

### Claude Code

```bash
git clone https://github.com/Sliky1/lagrangian-core-skill.git /tmp/lagrangian-core-skill
mkdir -p ~/.claude/skills
cp -r /tmp/lagrangian-core-skill/lagrangian-core ~/.claude/skills/
```

### Other compatible agents

```bash
git clone https://github.com/Sliky1/lagrangian-core-skill.git /tmp/lagrangian-core-skill
cp -r /tmp/lagrangian-core-skill/lagrangian-core/ ~/.config/agents/skills/lagrangian-core/
```

## Skill

| Skill | Description |
|---|---|
| [lagrangian-core](lagrangian-core/) | Constrained optimization via ALM/ADMM/KKT. Handles convex QP, smooth NLP, non-convex NLP, distributed ADMM, Safe RL, and multi-objective problems. |

## Supported problem types

| Problem type | Solver | Notes |
|---|---|---|
| Convex QP / Smooth NLP | `standard_solver` | Baseline; KKT verified |
| Non-convex NLP | `ALM` (n_starts=10, Halton) | FIX-21v2 + FIX-22 dual-layer guard |
| Distributed | `ADMM` | Multi-agent consensus |
| Safe RL | ALM + gradient cosine guard | FIX-16 |
| Multi-objective | ALM + Pareto repair | FIX-17 |
| Bayesian-optimization hybrid | Cross-skill COOP | COOP-1/2/3 |
| Natural language / degenerate | ALM + Tikhonov regularization | FIX-19 |

## Version history

| Version | Date | Highlights |
|---|---|---|
| [v0.9.3](archive/v0.9.3/SKILL.md) | 2026-05-01 | **FIX-22** dual-layer adversarial protection (ensemble_vote + adaptive_trust_region); language optimization |
| [v0.9.2](archive/v0.9.2/SKILL.md) | 2026-05-01 | **FIX-21v2** Halton quasi-random multi-start |
| [v0.9.1](archive/v0.9.1/SKILL.md) | 2026-05-01 | **FIX-19** Tikhonov regularization; **FIX-23** mixed-Bayes pressure scenarios; UX batch disambiguation |
| [v0.9.0](archive/v0.9.0/SKILL.md) | 2026-05-01 | COOP cross-skill protocol; session state persistence; incremental re-parsing |
| [v0.8.0](archive/v0.8.0/SKILL.md) | 2026-04-30 | Output modes (MINIMAL/STANDARD/VERBOSE); shadow price folding; KKT cache |
| [v0.7.0](archive/v0.7.0/SKILL.md) | 2026-04-28 | Safe RL + multi-objective routing; FIX-16/17/18 |
| [v0.5.0](archive/v0.5.0/SKILL.md) | 2026-04-20 | Multi-start non-convex; structured failure output |
| [v0.3.0](archive/v0.3.0/SKILL.md) | 2026-04-10 | ADMM routing; sparse JSON channel |
| [v0.1.0](archive/v0.1.0/SKILL.md) | 2026-04-01 | Prototype: basic ALM + KKT |

## Evals

Benchmark results for the current skill version vs. no-skill baseline:

| Scenario | With skill | Without skill |
|---|---|---|
| convex_qp + normal | 99.8% | ~91% |
| non_convex + adversarial | **96.8%** | ~71% |
| safe_rl + near_infeasible | 99.1% | ~68% |
| mixed_bayes + adversarial | 96.0% | ~60% |
| natural_lang + degenerate | 95.2% | ~55% |

Full eval scenarios are in [evals/](evals/).

## Philosophy

This skill is **workflow-first and guardrail-heavy**. It doesn't just remind the agent that ALM exists — it enforces step ordering, input validation, solver routing, and output structure that agents skip when left to their own judgment.

Each FIX is a documented regression addressed by ablation experiment, not a heuristic tweak. All parameter choices (Halton threshold=0.010, proj_radius=0.10, cos_thresh=0.10) are backed by simulation data in [evals/ablation/](evals/ablation/).

Language conventions: technical identifiers and JSON are English; behavioral rules and guardrails are Chinese. This maximizes token efficiency and model attention weight on technical vocabulary simultaneously.

## License

MIT — see [LICENSE](LICENSE).
