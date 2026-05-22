# Domain Patterns

Use this table to translate business wording into optimization structure.

| User wording | Optimization interpretation | Typical variables | Typical constraints | Suggested output |
|---|---|---|---|---|
| 预算怎么分最划算 | Maximize return under budget | allocation by project/category | total budget, min/max allocation | allocation + active budget bottleneck |
| 哪些投入最优先 | Rank by marginal return / shadow price | investment increments | budget/capacity | priority list + marginal benefit |
| 资源怎么排 | Resource scheduling/allocation | staff/time/equipment | capacity, deadlines, skills | feasible schedule or infeasibility diagnosis |
| 产能怎么配 | Production mix optimization | production quantities | capacity, demand, material | production plan + bottleneck resource |
| 既要公平又要效率 | Multi-objective optimization | allocation | fairness floor, total resource | Pareto trade-off or weighted result |
| 每个地区不能低于最低保障 | Lower-bound constraints | regional allocation | minimum service level | constraint status table |
| 至少满足一个条件 | OR constraint | binary-like logic or continuous proxy | disjunction | smooth approximation/case split; exact MIP halt |
| 安全阈值不能突破 | Safe constraint | policy/action/operation level | risk/safety bound | safe feasible recommendation |
| 哪个约束最卡脖子 | Shadow-price analysis | current optimum variables | active constraints | bottleneck ranking |
| 不可行怎么办 | Infeasibility repair | slack variables | relaxed constraints | minimal relaxation plan |

## Common objective choices

| Ambiguous target | Candidate formalization |
|---|---|
| 公平 | max-min, Gini minimization, variance minimization |
| 均衡 | minimize deviation from target ratio |
| 稳健 | maximize worst-case or add uncertainty buffer |
| 成本最低 | minimize cost subject to service constraints |
| 效益最高 | maximize benefit minus penalty terms |
