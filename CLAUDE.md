# CLAUDE.md

## Project overview

**lagrangian-core-skill** is an Agent Skill for constrained optimization using Augmented Lagrangian Methods. Each version is a self-contained SKILL.md file following the [Agent Skills spec](https://agentskills.io/specification).

## Repo structure

```
lagrangian-core-skill/
├── lagrangian-core/            # Current skill (v0.9.3)
│   ├── SKILL.md                # Main skill instructions
│   └── references/             # Parameter reference, FIX notes, ablation summaries
├── archive/                    # Historical versions
│   ├── v0.1.0/SKILL.md
│   ├── v0.3.0/SKILL.md
│   ├── v0.5.0/SKILL.md
│   ├── v0.7.0/SKILL.md
│   ├── v0.8.0/SKILL.md
│   ├── v0.9.0/SKILL.md
│   ├── v0.9.1/SKILL.md
│   ├── v0.9.2/SKILL.md
│   └── v0.9.3/SKILL.md         # same as lagrangian-core/SKILL.md
├── evals/                      # Eval scenarios and ablation data
│   ├── scenarios/              # 10 test scenarios (problem_type × stress)
│   ├── ablation/               # FIX-16~23 ablation CSVs
│   └── results/                # 20k simulation benchmark results
├── CHANGELOG.md
├── LICENSE
└── CLAUDE.md                   # This file
```

## Development conventions

### Skill structure
Every version follows the Agent Skills spec:
- `SKILL.md` with YAML frontmatter (name, description, license, metadata)
- Description must be agent-neutral

### Language conventions
| Content type | Language | Reason |
|---|---|---|
| Technical identifiers (algorithm names, parameter names) | English | Training corpus is English; higher attention weight |
| JSON / code blocks | English | Format spec is English |
| Behavioral rules / Forbidden Behaviors | Chinese | Higher information density; no subordinate clause ambiguity |
| Numeric parameters (thresh=0.010) | English | Universal format |

### FIX protocol
Every parameter change must be backed by an ablation experiment:
- Define parameter space
- Simulate N≥2000 per config
- Score = success_rate × 0.70 − token_extra × 2.0 (or domain-specific weighting)
- Document winning config in SKILL.md as `[FIX-XX]`
- Add Forbidden Behavior constraint to prevent regression

### Testing
- Benchmark: 20,000-call simulation per version
- Target: overall success rate ≥ 98.5%
- Token budget: ≤ 1.13x baseline
- Current (v0.9.3): 96.78% overall, 96.82% on non_convex+adversarial
