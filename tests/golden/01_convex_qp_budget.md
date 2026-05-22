# Case 01 — Convex budget allocation

## Input
预算100万元，A项目每万元收益3，B项目每万元收益2。A最多投60万元，B至少投30万元，A+B不能超过100万元。怎么分配收益最大？

## Expected classification
`convex_qp` or linear convex program.

## Required behavior
- Define variables and units.
- Form objective and constraints.
- Solve analytically if possible.
- Report active constraints.
- Explain the bottleneck in business language.

## Forbidden behavior
- Do not ask for unnecessary clarification.
- Do not claim external solver use if solved analytically.

## Expected result
A=60, B=40, total return=260 in the same return unit implied by coefficients.
