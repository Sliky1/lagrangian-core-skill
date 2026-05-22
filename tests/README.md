# Golden Tests

These tests are behavioral regression cases for the Lagrangian skill. They are not executable unit tests by themselves; each file describes the input, required behavior, forbidden behavior, and pass criteria.

Use them when editing `lagrangian/SKILL.md` or any reference file.

Recommended review process:

1. Run the skill against each `tests/golden/*.md` input.
2. Compare the answer with required and forbidden behavior.
3. Record pass/fail in `evals/results/`.


## Complete v1.0 coverage

The golden suite must cover: convex solving/routing, infeasibility, ambiguity, OR/conditional softening, exact MIP halt, no-tool no-fabrication, prompt injection, and mixed Bayesian handoff. See `golden/INDEX.md`.
