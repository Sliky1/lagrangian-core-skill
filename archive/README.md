# Archive

Historical milestone snapshots of the `lagrangian` skill. Each directory contains the `SKILL.md` as it existed at that version.

These are read-only reference copies. For the current skill, see [`../lagrangian/`](../lagrangian/).

## Versions

| Version | Stage | Key changes |
|---------|-------|-------------|
| [v0.1.0](v0.1.0/SKILL.md) | prototype | Initial ALM implementation; basic KKT verification; convex QP + smooth NLP only |
| [v0.3.0](v0.3.0/SKILL.md) | beta | Added ADMM for distributed problems; sparse JSON output channel; KKT fingerprint cache |
| [v0.5.0](v0.5.0/SKILL.md) | beta | Added Safe RL (FIX-16), multi-objective Pareto (FIX-17), staged infeasibility (FIX-18); token output modes MINIMAL / STANDARD / VERBOSE |
| [v0.7.0](v0.7.0/SKILL.md) | beta | Halton multi-start for non-convex (FIX-21); session state persistence (UX-2/3); shadow price collapsing (TOK-12) |
| [v0.8.0](v0.8.0/SKILL.md) | beta | Tikhonov regularization for degenerate NLP (FIX-19); token budget locked to ≤1.13x; batch clarification (UX-2b/2c) |
| [v0.9.3](v0.9.3/SKILL.md) | stable | Dual-layer adversarial protection (FIX-22); COOP-1/2/3 Bayesian handoff; FIX-23 mixed-Bayes pressure; FIX-24 degradation labels |
