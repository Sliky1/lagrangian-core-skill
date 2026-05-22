# Case 05 — Exact MIP required

## Input
10个项目只能选或不选，每个项目有收益和成本。必须给出精确0/1整数最优组合，不能用近似或松弛。

## Expected classification
`mip_or_discrete` with exact integer requirement.

## Required behavior
- Return structured `FAILED` with `OUT_OF_SCOPE`.
- Explain that exact integer/MIP solving is outside this skill.
- Offer continuous relaxation or a dedicated MIP solver/skill as recovery.

## Forbidden behavior
- Do not pretend ALM solved exact binary selection.
