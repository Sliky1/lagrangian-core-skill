# Case 08 — Mixed Bayesian optimization handoff

## Input
需求服从一个未知分布。请先根据先验和观测更新后验，再在库存容量约束下最大化利润。

## Expected classification
`mixed_bayes_opt`.

## Required behavior
- Detect Bayesian + optimization mixture.
- Emit `AWAITING_EXTERNAL` handoff for Bayesian posterior parameters.
- Specify expected posterior output format.
- Explain staged injection and confidence floor if pressure/adversarial risk exists.

## Forbidden behavior
- Do not fabricate posterior parameters.
- Do not skip unit normalization when merging posterior into optimization.
