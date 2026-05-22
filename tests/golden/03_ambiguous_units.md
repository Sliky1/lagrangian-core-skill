# Case 03 — Ambiguous units

## Input
A投入100，B投入20万元，总预算不能超过50，收益最大化。怎么投？

## Expected classification
`AMBIGUOUS` before optimization.

## Required behavior
- Detect mixed/unclear units.
- Ask for unit confirmation in one compact batch.
- Avoid assuming whether 100 means 元、万元、百分比、人数、小时, etc.

## Forbidden behavior
- Do not normalize units silently.
- Do not produce numerical optimum.
