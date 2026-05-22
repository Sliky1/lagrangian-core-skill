# Case 04 — OR constraint that may be softened

## Input
预算100万元，项目A和项目B至少要满足一个达到30万元，但可以接受近似连续优化，不要求整数精确解。请给建模方式。

## Expected classification
`mip_or_discrete` but softenable.

## Required behavior
- Identify OR/disjunctive constraint.
- Offer smooth approximation or case split.
- State that exact integer solution is not being claimed.

## Forbidden behavior
- Do not return `OUT_OF_SCOPE` immediately if the user accepts approximation.
- Do not claim exact MIP optimum.
