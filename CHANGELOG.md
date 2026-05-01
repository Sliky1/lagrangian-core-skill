# Changelog

All notable changes to lagrangian-skills are documented here.

## [v0.9.3] — 2026-05-01

### Added
- **[FIX-22]** Dual-layer adversarial protection for `non_convex+adversarial` saddle point traps
  - Layer B (pre-detection): `ensemble_vote`, `quarantine=5`, `safe_direction` fallback
  - Layer A (projection): `adaptive_trust_region`, `proj_radius=0.10`, `restart_thresh=5`
  - Confirmed by ablation: 60 configs × 2000 simulations per scheme
- `archive/` milestone snapshots: v0.1.0, v0.3.0, v0.5.0, v0.7.0, v0.8.0, v0.9.3

### Changed
- Repository renamed from `lagrangian-core-skill` → `lagrangian-skills`
- Skill directory renamed from `lagrangian-core/` → `lagrangian/`
- Language optimization: technical identifiers 100% English, behavioral rules Chinese
- Removed explanatory Chinese comments from solver routing table (no execution value)
- Compressed FIX-22 block annotations; doc reduced from 4,021 → 3,920 chars

### Fixed
- `non_convex+adversarial` success rate: 94.29% → **96.82%** (+2.53pp)
- Global token impact: +0.006x (FIX-22 affects only 2.9% of calls)

---

## [v0.9.2] — 2026-05-01

### Added
- **[FIX-21v2]** Halton quasi-random sequence for `non_convex+adversarial` multi-start
  - Replaces uniform random: `thresh=0.010`, `window=3`, `abandon=majority_vote`
  - Ablation confirmed: Halton+thresh=0.010 beats uniform by +1.4pp

### Fixed
- `non_convex+adversarial` success rate: 92.9% → 94.3% (+1.4pp)

---

## [v0.9.1] — 2026-05-01

### Added
- **[FIX-19]** Tikhonov regularization for `natural_lang+degenerate` (Hessian cond>1e6, ε=1e-4)
- **[FIX-23]** Dedicated strategies for `mixed_bayes_opt` pressure scenarios
- **[FIX-24]** Step 7 degenerate scenario annotations
- UX batch disambiguation: ≥2 ambiguous points → single-round confirmation table (-0.12x)
- Incremental re-parsing: delta-only on incremental triggers

### Fixed
- `natural_lang+degenerate`: 85.6% → **95.2%** (+9.6pp)
- `mixed_bayes+near_infeasible`: 87.4% → **97.6%** (+10.2pp)

---

## [v0.9.0] — 2026-05-01

### Added
- COOP cross-skill protocol (COOP-1/2/3) for Bayesian-optimization hybrids
- Session state persistence (problem definition, x*, constraint list, KKT cache)
- Incremental trigger words with delta-only re-parsing

---

## [v0.8.0] — 2026-04-30

### Added
- Output modes: MINIMAL / STANDARD / VERBOSE
- Shadow price folding; KKT cache with 5-tuple fingerprint
- Business language translation layer (off by default)

---

## [v0.7.0] — 2026-04-28

### Added
- Safe RL + multi-objective routing
- **[FIX-16]** Gradient cosine similarity guard
- **[FIX-17]** Pareto repair frequency guard
- **[FIX-18]** Stage step guard

---

## [v0.5.0] — 2026-04-20

### Added
- Multi-start non-convex (n_starts=10, uniform random)
- Structured failure output with recovery suggestions

---

## [v0.3.0] — 2026-04-10

### Added
- ADMM routing for distributed problems
- Sparse JSON channel (Step 3)

---

## [v0.1.0] — 2026-04-01

### Added
- Prototype: basic ALM + KKT verification
