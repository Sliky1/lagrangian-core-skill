# Usage Guide

## What this skill is for

Use this skill when the user asks for constrained optimization, resource allocation, budget allocation, bottleneck analysis, shadow-price interpretation, feasibility diagnosis, or Lagrangian/KKT reasoning.

## Typical user requests

- "预算有限，怎么分配收益最高？"
- "这些约束是不是可行？"
- "哪个约束最卡脖子？"
- "请写出拉格朗日函数和 KKT 条件。"
- "没有求解器时，先帮我建模和说明求解方案。"

## Required response discipline

1. Normalize variables, objective, constraints, and bounds.
2. Classify the problem type.
3. Route to an appropriate method.
4. Verify feasibility/KKT when a numeric answer is claimed.
5. Return structured failure when information is missing or the problem is out of scope.
6. Never invent numerical results in `NO_TOOL` mode.

## Recommended output modes

- `MINIMAL`: direct result or failure reason.
- `STANDARD`: result, active constraints, bottlenecks, and limitations.
- `VERBOSE`: full model, derivation, KKT, routing, and interpretation.
