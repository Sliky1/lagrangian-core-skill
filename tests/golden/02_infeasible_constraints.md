# Case 02 — Infeasible constraints

## Input
有100万元预算。A项目至少投70万元，B项目至少投50万元，同时A+B不能超过100万元。请给最优分配。

## Expected classification
`convex_qp` or linear program with infeasible constraints.

## Required behavior
- Detect infeasibility.
- Return structured `FAILED` with `INFEASIBLE`.
- Explain minimum relaxation direction: either increase budget to at least 120万元 or reduce minimum allocation total by at least 20万元.

## Forbidden behavior
- Do not output an allocation that violates constraints.
- Do not silently drop a constraint.
