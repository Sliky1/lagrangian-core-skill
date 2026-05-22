# Output Templates

## MINIMAL success

```text
答案: x* = <value>; 目标值 = <value>; 主要瓶颈 = <active constraint>
```

If no numerical solve happened:

```text
答案: 需要计算环境；当前只能给出模型与求解方案，不能给出数值最优解。
```

## STANDARD success

```markdown
## 结论
- 最优解/推荐方案: ...
- 可行性: ...
- 目标值: ...

## 活跃约束与瓶颈
| 约束 | 状态 | 影子价格/边际含义 | 说明 |
|---|---|---:|---|
| ... | active | ... | ... |

## 可信度与限制
- 已验证: ...
- 未验证/限制: ...
- 使用的保护策略: FIX-...
```

## VERBOSE success

Use STANDARD plus:

1. normalized model,
2. classification,
3. Lagrangian form,
4. KKT/feasibility checklist,
5. solver route,
6. shadow-price interpretation,
7. sensitivity or counterfactual analysis when requested.

## FAILED

```json
{
  "status": "FAILED",
  "error_code": "AMBIGUOUS",
  "reason": "缺少预算上限和目标函数定义",
  "recovery": "请补充预算、变量范围、收益函数或成本函数"
}
```

## AWAITING_EXTERNAL

```json
{
  "status": "AWAITING_EXTERNAL",
  "subtask_for_external_skill": {
    "type": "bayesian_inference",
    "input": "Estimate posterior parameters for uncertain demand.",
    "output_format": {"posterior_params": "dict", "confidence": "float 0-1"}
  },
  "merge_instruction": "Inject posterior parameters by staged update with confidence floor."
}
```
