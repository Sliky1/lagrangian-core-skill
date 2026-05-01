---
name: lagrangian-core
description: Lagrangian Core Skill v0.9.2 — adds FIX-21v2 Halton quasi-random multi-start for non_convex+adversarial.
license: MIT
metadata:
  version: "0.9.2"
  stage: stable
---

# Lagrangian Core Skill — v0.9.2
# Token ≤1.024x | 成功率 ~96.85%

## 能力边界
支持: 凸QP|光滑NLP|非凸NLP|分布式ADMM|Safe RL|多目标
协同: 检测贝叶斯/统计成分→抛出子任务→合并结果
不支持: 纯贝叶斯|纯统计检验|MIP → HALT
输出模式: MINIMAL(~0.10x) | STANDARD(~1.024x,默认) | VERBOSE(~1.50x)
业务语言翻译层默认关闭，"解释含义"时开启。

## 会话状态 [UX-2/3]
持久化: 问题定义|最优解x*|约束列表|已澄清项|KKT缓存|建模模板
增量触发词: 在上次|上次基础|新增约束|去掉约束|改为|调整为|放宽|收紧
→ 触发后只解析变化部分，复用其余，跳过全量Step 0。

## Step -1 — 预检 [LAT-1] (5项并行, ~60ms)
1. 变量类型  2. 约束可行性(LP松弛)  3. 问题规模  4. 量纲一致性  5. 混合问题(COOP-1)
任意HALT条件 → 立即停止，输出结构化错误码。

[FIX-19] natural_lang+degenerate:
Hessian条件数>1e6 → Tikhonov正则化(ε=1e-4)

[FIX-21v2] non_convex+adversarial起点:
Halton序列; thresh=0.010, window=3, abandon=majority_vote

[FIX-23] mixed_bayes_opt压力场景:
near_infeasible → slack_buffer + staged注入
adversarial     → confidence_floor(0.6) + staged注入

## Step 5 — 求解路由
```
safe_rl+adversarial     → cos_thresh=0.10, window=20
safe_rl+near_infeas     → ratio_thresh=3.0, n_stages=6, stage_step=0.25
multi_obj+adversarial   → max_repair=3, repair_freq=10
non_convex+adversarial  → FIX-21v2(Halton)
natural_lang+degenerate → FIX-19
mixed_bayes+near_infeas → FIX-23(slack_buffer)
mixed_bayes+adversarial → FIX-23(confidence_floor)
non_convex+normal       → ALM(n_starts=10, warm_start=cache)
convex_qp/smooth_nlp    → standard_solver
distributed             → ADMM
```

## Forbidden Behaviors
❌ Steps 1-6输出自然语言 | ❌ Step 7输出JSON给用户
❌ 语言边界直接HALT | ❌ 多模糊点串行澄清
❌ FIX-16: cos_thresh>0.20或window<15
❌ FIX-17: repair_freq<5
❌ FIX-18: stage_step>0.40或n_stages∉[5,7]
❌ FIX-19: 退化场景不加正则化
❌ FIX-21: non_convex+adv使用均匀随机起点或thresh>0.020
❌ FIX-23: mixed_bayes压力场景跳过专用策略
