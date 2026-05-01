---
name: lagrangian-core
description: Lagrangian Core Skill v0.9.0 — adds COOP cross-skill protocol, session state persistence, and incremental re-parsing.
license: MIT
metadata:
  version: "0.9.0"
  stage: stable
---

# Lagrangian Core Skill — v0.9.0
# Token ≤1.09x | 成功率 ~96.4%

## 能力边界
支持: 凸QP|光滑NLP|非凸NLP|分布式ADMM|Safe RL|多目标
协同: 检测贝叶斯/统计成分→抛出子任务→合并结果
不支持: 纯贝叶斯|纯统计检验|MIP → HALT
输出模式: MINIMAL(~0.10x) | STANDARD(~1.09x,默认) | VERBOSE(~1.50x)
业务语言翻译层默认关闭，"解释含义"时开启。

## 会话状态 [UX-2/3]
持久化: 问题定义|最优解x*|约束列表|已澄清项|KKT缓存|建模模板
增量触发词: 在上次|上次基础|新增约束|去掉约束|改为|调整为|放宽|收紧
→ 触发后只解析变化部分，复用其余，跳过全量Step 0。

## Step -1 — 预检 [LAT-1] (5项并行, ~60ms)
1. 变量类型  2. 约束可行性(LP松弛)  3. 问题规模  4. 量纲一致性  5. 混合问题(COOP-1)
任意HALT条件 → 立即停止，输出结构化错误码。

## Step 0 — 混合检测 + 批量澄清 [COOP-1]
贝叶斯信号词: 先验|后验|似然|贝叶斯|概率分布|prior|posterior|likelihood
统计信号词: 均值|方差|回归|相关系数|假设检验
→ 贝叶斯+优化: MIXED_BAYES_OPT → 抛出子任务(COOP-2)
→ 纯贝叶斯: HALT "请调用贝叶斯Skill"
批量澄清: ≥2个模糊点→合并单轮确认表(-0.12x)

## Step 3 — 稀疏JSON通道
```json
{"step":3,"type":"augmented_lagrangian",
 "formula":"L_ρ=f(x)+Σλ·h(x)+Σμ·g(x)+ρ/2·||h||²",
 "multipliers":{"lambda":[0.0],"mu":[0.0]},
 "penalty":{"rho_init":1.0,"update_rule":"×1.5 if ||h||>tol"}}
```

## Step 4 — KKT验证 + 缓存
指纹=(变量数, eq约束数, ineq约束数, 目标函数类型, 约束结构哈希); 命中率~85%

## Step 5 — 求解路由
```
safe_rl+adversarial     → cos_thresh=0.10, window=20
safe_rl+near_infeas     → ratio_thresh=3.0, n_stages=6, stage_step=0.25
multi_obj+adversarial   → max_repair=3, repair_freq=10
non_convex+adversarial  → ALM(n_starts=10, uniform_random)
natural_lang+degenerate → FIX-19(Tikhonov ε=1e-4)
non_convex+normal       → ALM(n_starts=10, warm_start=cache)
convex_qp/smooth_nlp    → standard_solver
distributed             → ADMM
```

## Step 6 — 影子价格
默认只输出活跃约束；其余折叠"[展开]"。

## Step 7 — 自然语言渲染
STANDARD: 最优解(一行) → 约束状态表(仅活跃) → 关键瓶颈(一句)
VERBOSE: STANDARD + Steps 3-6 JSON

## COOP-2/3 — 跨Skill协同
```json
{"status":"AWAITING_EXTERNAL",
 "subtask_for_external_skill":{"type":"bayesian_inference","input":"<子任务>",
   "output_format":{"posterior_params":"dict","confidence":"float 0-1"}},
 "merge_instruction":"posterior_params staged方式注入优化参数"}
```
基础合并: conf=soft_linear | unit_norm=domain_aware | conflict=conservative_min
压力覆盖: near_infeasible→slack_buffer | adversarial→confidence_floor(0.6)

## 失败处理
```json
{"status":"FAILED","error_code":"INFEASIBLE|BAD_PARAMS|AMBIGUOUS|SOLVER_FAIL|OUT_OF_SCOPE",
 "reason":"<一行>","recovery":"<修复建议或最小松弛量>"}
```

## Forbidden Behaviors
❌ Steps 1-6输出自然语言 | ❌ Step 7输出JSON给用户
❌ 语言边界直接HALT | ❌ 多模糊点串行澄清 | ❌ 增量修改全量重解析
❌ 混合问题不触发COOP | ❌ COOP合并跳过domain_aware
❌ FIX-16: cos_thresh>0.20或window<15
❌ FIX-17: repair_freq<5
❌ FIX-18: stage_step>0.40或n_stages∉[5,7]
