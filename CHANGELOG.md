# Changelog

All notable changes to lagrangian-skills are documented here.

## v1.0.0-complete — 2026-05-22

### Added
- Complete release manifest, installation guide, usage guide, quality gate, release notes, security policy, and contribution guide.
- JSON schemas for failure outputs, eval scenarios, and skill metadata.
- Release completeness validator: `scripts/check_release.py`.
- Golden test index and additional eval scenarios covering exact MIP halt, no-tool no-fabrication, and prompt injection.

### Changed
- v1.0.0 is now explicitly defined as a complete stable release rather than a near-complete packaging pass.


## [v1.0.0] — 2026-05-22

### Added
- Stable v1.0.0 package structure with `lagrangian/references/`
- `references/solver-routing.md` for classification-to-solver decisions
- `references/fix-catalog.md` for regression guard rationale and no-tool behavior
- `references/output-templates.md` for MINIMAL, STANDARD, VERBOSE, FAILED, and AWAITING_EXTERNAL outputs
- `references/failure-codes.md` for structured failure semantics
- `references/domain-patterns.md` for business-language-to-optimization mapping
- `references/examples.md` with representative expected behaviors
- `tests/golden/` behavioral regression cases
- `evals/scenarios/` JSONL scenario definitions
- `evals/results/` result summary and v1.0 regression template
- `evals/ablation/fix_ablation_summary.csv`
- `evals/run_eval.py` lightweight scenario-structure checker

### Changed
- Promoted metadata version to `1.0.0`
- Reorganized `SKILL.md` into a shorter executable core with references to detailed docs
- Clarified that v1.0.0 keeps the v0.9.3 measured benchmark summary and adds reproducibility scaffolding rather than claiming a new measured benchmark
- Strengthened exact-MIP boundary and no-tool behavior

### Fixed
- Removed remaining ambiguity around fake numerical results, posterior parameters, multi-start statistics, and cache hits
- Unified README, CHANGELOG, CLAUDE, evals, and archive wording around v1.0.0

---

## [v0.9.5] — 2026-05-22

### Added
- Capability-aware `Execution Modes`: `TOOL_AVAILABLE`, `NO_TOOL`, and `UNKNOWN_TOOL`
- Security guards against user/content prompt injection that attempts to disable KKT checks, routing, or Forbidden Behaviors
- Step 1 model normalization: variables, objective, equality/inequality constraints, bounds, units, and data sources
- Step 2 problem classification before solver routing
- Explicit no-fabrication rules for x*, multipliers, KKT residuals, cache hits, multi-start statistics, and success rates

### Changed
- Clarified MIP boundary: softenable OR/conditional constraints may use smooth approximation or case split; exact integer/MIP solving remains out of scope
- Replaced generic `success_rate` metadata with `measured_success_rate`, `target_success_rate`, and `eval_version`
- Changed session persistence wording to distinguish in-session reuse from platform-dependent cross-session memory/cache

### Fixed
- Typo in Step 3: `字桑` → `字段`
- Version/documentation mismatch across README, CLAUDE, and eval notes

---

## [v0.9.4] — 2026-05-07

### Changed
- `name` corrected from `lagrangian-core` → `lagrangian`
- Added `when_to_use` field with natural-language trigger examples
- Added `model: inherit` and `effort: high` frontmatter fields
- Description restructured: business-scenario lead, technical terms follow

---

## [v0.9.3] — 2026-05-01

### Added
- FIX-22 dual-layer adversarial protection for `non_convex+adversarial` saddle point traps
- Archive milestone snapshots

### Changed
- Repository renamed from `lagrangian-core-skill` → `lagrangian-skills`
- Skill directory renamed from `lagrangian-core/` → `lagrangian/`

### Fixed
- `non_convex+adversarial` success rate: 94.29% → 96.82% (+2.53pp)

---

## [v0.9.2] — 2026-05-01

### Added
- FIX-21v2 Halton quasi-random sequence for `non_convex+adversarial` multi-start

---

## [v0.9.1] — 2026-05-01

### Added
- FIX-19 Tikhonov regularization for `natural_lang+degenerate`
- FIX-23 dedicated strategies for `mixed_bayes_opt` pressure scenarios
- FIX-24 Step 7 degenerate scenario annotations

---

## [v0.9.0] — 2026-05-01

### Added
- COOP cross-skill protocol for Bayesian-optimization hybrids
- Session state persistence and incremental trigger words

---

## [v0.8.0] — 2026-04-30

### Added
- Output modes: MINIMAL / STANDARD / VERBOSE
- Shadow price folding and KKT cache fingerprint

---

## [v0.7.0] — 2026-04-28

### Added
- Safe RL + multi-objective routing
- FIX-16, FIX-17, FIX-18 guards

---

## [v0.5.0] — 2026-04-20

### Added
- Multi-start non-convex and structured failure output

---

## [v0.3.0] — 2026-04-10

### Added
- ADMM routing and sparse JSON channel

---

## [v0.1.0] — 2026-04-01

### Added
- Prototype: basic ALM + KKT verification
