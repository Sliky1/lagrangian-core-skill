---
name: lagrangian-core
description: >
  Lagrangian Core Skill v0.9.3 (current stable) — adds FIX-22 dual-layer adversarial
  protection (ensemble_vote detection + adaptive_trust_region projection) and language
  optimization (technical identifiers English, behavioral rules Chinese).
license: MIT
metadata:
  version: "0.9.3"
  stage: stable
  success_rate: "96.78%"
  token_budget: "<=1.13x"
---

> **This is the current stable version.** See [../../lagrangian-core/SKILL.md](../../lagrangian-core/SKILL.md) for the canonical copy.

# Lagrangian Core Skill — v0.9.3
# Token ≤1.13x | 成功率目标 98.5% | 文档 ≤150行

## 能力边界
支持: 凸QP | 光滑NLP | 非凸NLP | 分布式ADMM | Safe RL | 多目标
协同: 检测贝叶斯/统计成分→抛出子任务→合并结果
不支持: 纯贝叶斯 | 纯统计检验 | MIP → HALT
输出模式: MINIMAL(~0.10x,"只要数字") | STANDARD(~1.13x,默认) | VERBOSE(~1.55x,"展开计算")
业务语言翻译层默认关闭，"解释含义"时开启。

## 会话状态 [UX-2/3]
持久化: 问题定义 | 最优解x* | 约束列表 | 已澄清项 | KKT缓存 | 建模模板
增量触发词: 在上次|上次基础|新增约束|去掉约束|改为|调整为|放宽|收紧
→ 触发后只解析变化部分，复用其余，跳过全量Step 0。

## Step -1 — 预检 [LAT-1] (5项并行, ~60ms)
1. 变量类型  2. 约束可行性(LP松弛)  3. 问题规模  4. 量纲一致性  5. 混合问题(COOP-1)
任意HALT条件 → 立即停止，输出结构化错误码。

[FIX-19] natural_lang+degenerate:
Hessian条件数>1e6 → Tikhonov正则化(ε=1e-4)

[FIX-21v2] non_convex+adversarial起点:
Halton序列; thresh=0.010, window=3, abandon=majority_vote

[FIX-22] non_convex+adversarial双层防护:
Layer B (前置): ensemble_vote, quarantine=5 → safe_direction回退
Layer A (投影): adaptive_trust_region, proj_radius=0.10, restart_thresh=5
→ 连续5步目标值劣化 → 重启+下一Halton起点
独立触发，执行顺序B→A；非此场景不启用。

[FIX-23] mixed_bayes_opt压力场景:
near_infeasible → slack_buffer + staged注入
adversarial     → confidence_floor(0.6) + staged注入

[FIX-24] Step 7退化标注:
FIX-19 → "⚠️ 退化结构，已正则化(ε=1e-4)"
FIX-22 → "⚠️ 对抗性鞍点：双层防护已激活"
FIX-23 → "⚠️ COOP压力场景：{策略名}已激活"

## Step 5 — 求解路由
```
safe_rl+adversarial     → cos_thresh=0.10, window=20
safe_rl+near_infeas     → ratio_thresh=3.0, n_stages=6, stage_step=0.25
multi_obj+adversarial   → max_repair=3, repair_freq=10
non_convex+adversarial  → FIX-21v2 + FIX-22
natural_lang+degenerate → FIX-19
mixed_bayes+near_infeas → FIX-23(slack_buffer)
mixed_bayes+adversarial → FIX-23(confidence_floor)
non_convex+normal       → ALM(n_starts=10, warm_start=cache)
convex_qp/smooth_nlp    → standard_solver
distributed             → ADMM
```

## Forbidden Behaviors
❌ Steps 1-6输出自然语言 | ❌ Step 7输出JSON给用户
❌ 语言边界直接HALT | ❌ 多模糊点串行澄清 | ❌ 增量修改全量重解析
❌ JSON含默认值 | ❌ 不活跃约束默认展开 | ❌ 失败后输出散文
❌ 混合问题不触发COOP | ❌ COOP合并跳过domain_aware
❌ FIX-16: cos_thresh>0.20或window<15
❌ FIX-17: repair_freq<5
❌ FIX-18: stage_step>0.40或n_stages∉[5,7]
❌ FIX-19: 退化场景不加正则化
❌ FIX-21: non_convex+adv使用均匀随机起点或thresh>0.020
❌ FIX-22: non_convex+adv跳过双层防护（B层或A层缺一不可）
❌ FIX-23: mixed_bayes压力场景跳过专用策略
