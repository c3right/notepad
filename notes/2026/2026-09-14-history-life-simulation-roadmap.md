---
title: "历史人生模拟阅读项目：路线图与进展"
date: 2026-09-14
updated: 2026-09-14
status: working
type: synthesis
topics:
  - history
  - decision-making
  - case-method
  - reading-path
  - historiography
keywords:
  - 人生模拟器
  - 代入式历史阅读
  - Decision Atom
  - Case Packet
  - D/L/W
  - 路线图
source: "ChatGPT conversation | web research"
language: zh-CN
---

# 历史人生模拟阅读项目：路线图与进展

> 本笔记只维护**讨论脉络、当前架构、阶段状态和下一步**。具体规则、实验和原型另见：
>
> - [Decision Atom 正式字段表 v1](./2026-09-14-history-decision-atom-schema-v1.md)
> - [Decision Atom 软评分量表 v1](./2026-09-14-history-decision-atom-scoring-v1.md)
> - [第一次候选排序实验](./2026-09-14-history-decision-atom-ranking-experiment-1.md)
> - [Qualification Sprint 1](./2026-09-14-history-decision-atom-qualification-sprint-1.md)
> - [首批 Case Packet Feasibility Mini-Design](./2026-09-14-history-case-packet-feasibility-mini-design-1.md)
> - [Starkloff Case Packet Prototype v0.1](./2026-09-14-history-case-packet-starkloff-v0.1.md)

## 一句话状态

项目已从“找一批有代入感的历史书”推进为一条可运行的研究/产品管线：

> **D/L/W定位 → Case Field切片 → Decision Atom → 主体/窗口/信息/选项审计 → Hard Gates → M01—M10排序 → Qualification Sprint → qualified案例 → B/P/N/R材料设计 → Packet Feasibility → Case Packet Prototype → 闭卷试读 → 迭代。**

当前已经完成第一份真正可阅读的产品：**Starkloff / St. Louis 1918 Case Packet Prototype v0.1**。

下一步暂不继续做IBM和Hirabayashi，而是先验证这份原型：

> **Reader Packet是否真的迫使读者在Freeze前形成自己的判断，而不是猜作者想要的“正确答案”。**

---

# 1. 项目目标

宏观历史轨解决：

> 世界如何运行？制度、结构、长期因果怎样展开？

本项目的微观轨解决：

> **如果我是当事人，在那个时刻，只拥有他当时能够拥有的信息，我会怎么选？**

因此：

- **宏观史：给地图。**
- **微观人生模拟：练驾驶。**

目标不是提炼成功学，而是扩充未亲历的人生样本，训练在不确定性、有限权限、组织关系、风险、身份与价值冲突中的判断。

---

# 2. 基本架构

## 2.1 D / L / W 三轨

- **D — Decision**：如果我是他，此刻怎么办？
- **L — Life-course**：这个人几十年怎样一步步变化？
- **W — World**：活在这种具体历史生活世界中是什么感觉？

当前D轨已形成完整工作流；L/W后续单独建设。

## 2.2 D轨核心类型

1. D1 路径选择与身份绑定
2. D2 高风险承诺与机会窗口
3. D3 持续投入、转向与退出
4. D4 识人、授权与制衡
5. D5 合作、承诺与关系变质
6. D6 对抗、谈判与让步边界
7. D7 角色退出、身份脱钩与权力交接

另有：

- **N：价值冲突、角色义务与底线选择**；
- 情境坐标：相对强弱、时间压力、环境变化、反馈状态、决策单位尺度、角色身份。

D2“高风险批准/授权/触发阈值”的边界已在Kelsey、Challenger、Starkloff等案例中重复出现，但暂不修改正式v1，等实际Packet反馈后再判断。

## 2.3 Decision Atom

> **Decision Atom = 某个明确主体，在一个真实且仍开放的决策窗口内，基于当时可获得的信息，在两个以上现实可行方案之间，对一个核心问题作出具有实际后果的选择。**

人物、事件、一本书、一家公司、整场战争都不是Atom。

层级：

> **Case Field → Case Episode → Decision Atom → Case Packet**

Sources独立管理，承担：

- B — Background
- P — Protagonist / Evidence
- N — Narrative
- R — Reveal / Review

核心防错原则：

- Historical Event Node ≠ Decision Window ≠ Freeze Point；
- Freeze位于选择仍开放、尚未跨过Commitment Threshold的位置；
- 国家、企业、家庭不能天然拟人化；
- 后人能想出的方案不能冒充当事人真实选项；
- Outcome Familiarity与Narrative Contamination分开；
- N型必须通过Normative Open-Conflict Test。

---

# 3. 已完成的验证

## 3.1 三轮压力测试

**第一轮**：古巴导弹危机、华盛顿1783辞职、刘大鹏、柯达数字化。主要解决真实决策点、案例基本单位、主体边界和叙事污染。

**第二轮**：何如璋、弗兰克一家、卡内基—弗里克、雅格施泰特。加入Action Locus、Deciders ≠ Affected Parties、Paired Focal Perspective、Normative Open-Conflict Test。

**第三轮**：Kelsey、Boeing 747、Stiles/Horr/Bonney家庭书信、Atlantic Telegraph 1865。验证v1可以拒绝“故事很好但还不是Atom”的材料，并确认Option Evidence Grade、主体字段、Source Hindsight等实际有用。

## 3.2 Hard Gates与软评分

Hard Gates判断“它是不是可靠的Decision Atom”；M01—M10判断“值不值得现在投入研究和制作成本”。

M01—M10：Information Reconstructability、Evidence Transparency、Decision Tension、Multi-perspective Potential、Consequence Traceability、Life Transfer Value、Immersion Potential、Background Efficiency、Blind-Simulation Value、Sample Novelty。

规则：0—5分、0/3/5锚点、H/M/L Confidence；M01/M02至少3才进优先建设队列；不机械求总分。

---

# 4. 第一次候选排序实验

8个新候选：Starkloff、Hirabayashi、IBM System/360、Donner-Reed、Challenger、Sugihara、Camp David、Shackleton/James Caird。

主要结果：

- 低知名度、高可重建、低污染案例会上升；
- Challenger史料优秀但闭卷价值低，更适合深度复盘；
- Camp David背景成本高而后置；
- Shackleton当前切法被Hard Gate挡住，说明戏剧性不能替代真实决策张力。

---

# 5. Qualification Sprint 1

## Starkloff / St. Louis 1918

**Qualified。** 重切为：

> Starkloff是否从10月6日仍偏向病例隔离/有限措施，升级为10月7日主动推动全市学校、娱乐场所与公共集会关闭。

## Gordon Hirabayashi / 1942

**Qualified；N-Gate Confidence = Medium。**

同时代声明强力证明Christian / democratic / civil-liberty obligation；家庭团聚与原本准备随迁主要由后来第一人口述支持，因此Packet必须明确标记Retrospective Evidence。

## IBM System/360 / Vin Learson 1962

**Qualified after re-cut。** 重切为：

> 1962年1月初，Vin Learson面对SPREAD最终报告时，是否把统一兼容New Product Line正式设为IBM开发方向并要求组织执行。

## Donner-Reed

Fort Bridger原Atom被否决；重切到Little Sandy后边缘Qualified，但Freeze前信息世界大量依赖后见回忆，后置。

---

# 6. 首批 Packet Feasibility

| 案例 | Verdict | 主要理由 |
|---|---|---|
| **Starkloff 1918** | **GREEN / Build #1** | Freeze清楚、同时代P材料强、背景可压缩、人物结局污染低 |
| **IBM / Learson 1962** | **GREEN- / Build #2** | SPREAD原报告提供罕见内部材料，但技术/组织背景较重 |
| **Hirabayashi 1942** | **AMBER-GREEN / Build #3** | 人生与N型价值高，但关键家庭义务与内心未决性部分依赖later recollection |

Packet层新发现两类风险，暂不改Decision Atom v1：

1. **Analogical Contamination**：现代同构事件会预装历史判断；
2. **Source-Metadata Leakage**：later recollection的来源年份本身也可能泄露未来。

处理原则：**宁可牺牲少量盲模拟纯度，也不牺牲证据透明度。**

---

# 7. Starkloff Case Packet Prototype v0.1

**状态：已完成，可进入首次闭卷试读。**

原型结构：

> 角色与1918背景 → 窄时间线 → 当时可见证据 → 已知/未知清单 → Freeze Task → Decision Card → 折叠Reveal → 决策质量/结果质量分离 → 研究者审计。

### 核心编辑选择

- Freeze使用**操作性Freeze**：10月7日跨部门会议开始前后，而不虚构Starkloff私人心理改变的精确时刻；
- Freeze前完全隔离St. Louis最终死亡结果、后世“model city”标签、跨城市比较研究；
- 不使用“lockdown / flatten the curve / COVID-style restrictions”等现代高污染词汇；
- 不把会议反对者编造成有对白的人物；现有材料只能确认存在反对，不能完整恢复每个人的原话；
- Reveal明确区分实际选择、执行摩擦、后续调整、观察性结果研究和因果不确定性；
- 决策任务要求读者给出**政策范围、触发阈值、复核时间、权限路径、最大下行风险和信心度**，而不是简单选A/B。

### 当前史料缺口

v0.1仍不是史料精校版。v0.2前应优先补：

1. 1918-10-06 *St. Louis Globe-Democrat*原件；
2. 1918-10-07 *St. Louis Post-Dispatch*原件；
3. 1918-10-08 *St. Louis Globe-Democrat*原件；
4. Starkloff 1918–1919年度报告相关页；
5. Mayor / City Counselor / Board of Aldermen / Health Commissioner之间的正式授权关系。

详见：[Starkloff Case Packet Prototype v0.1](./2026-09-14-history-case-packet-starkloff-v0.1.md)。

---

# 8. 当前项目架构

> D / L / W
> ↓
> Case Field → Decision Atom
> ↓
> D1—D7 / N
> ↓
> 主体拓扑 + Action Locus
> ↓
> Decision Window + Freeze + Commitment Threshold
> ↓
> 当时信息集 + 现实选项 + Option Evidence Grade
> ↓
> 情境坐标 + 规范性维度
> ↓
> 证据结构 + 叙事污染审计
> ↓
> Hard Gates
> ↓
> M01—M10 + Confidence + 案例画像
> ↓
> 候选排序 → Qualification Sprint
> ↓
> qualified案例 → B/P/N/R材料设计
> ↓
> Packet Feasibility
> ↓
> Case Packet Prototype
> ↓
> **闭卷试读 → 用户行为反馈 → 编辑方法迭代**

始终保持：

> **先筛案例，再筛书；书是材料，不是案例。**

---

# 9. Phase状态

| Phase | 内容 | 状态 |
|---|---|---|
| 1 | 目标定义、D/L/W、初始分类 | 已完成 |
| 2 | 两轮结构压力测试；Atom、窗口、主体、污染 | 已完成 |
| 3 | Decision Atom v1实操编码测试 | 已完成 |
| 4 | M01—M10软评分量表v1 | 已完成 |
| 5 | 第一次真实候选排序实验 | 已完成 |
| 6 | A档候选Qualification Sprint | 已完成 |
| 7 | 首批qualified案例的Packet Feasibility | 已完成 |
| 8A | Starkloff Case Packet Prototype v0.1 | **已完成** |
| 8B | Starkloff首次闭卷试读与Prototype复盘 | **下一步** |
| 9 | IBM / Hirabayashi Packet；扩展D候选池；系统建设L/W | 未开始 |
| 10 | 扩展为长期案例库/阅读路线 | 未开始 |

---

# 10. 下一小步：首次闭卷试读

下一步原则上不先补v0.2史料，也不立刻写IBM。

先把v0.1当成产品实际使用一次，记录：

1. Freeze前是否已经让读者明显猜到作者期待“大范围关闭”；
2. Background是否太多/太少；
3. 读者是否认为至少两个现实方案都还讲得通；
4. Decision Card是否迫使读者说明自己的阈值、复核点和权限判断；
5. Reveal后是否出现明显Outcome Bias；
6. 哪些现代COVID经验在读者不自觉中被带入1918。

只有完成这一步，才能判断下一项工作是：

- 修Starkloff Packet编辑方法；
- 补史料做v0.2；
- 或确认方法可行，开始IBM Packet。

---

## Revision log

- **2026-09-14**：建立路线笔记；记录前两轮压力测试与Decision Atom v1形成过程。
- **2026-09-14**：完成第三轮实操编码测试；确认v1基本可操作。
- **2026-09-14**：建立M01—M10软评分量表v1。
- **2026-09-14**：完成第一次8候选排序实验；形成A/B/C行动队列。
- **2026-09-14**：完成Qualification Sprint 1；Starkloff、Hirabayashi、IBM进入qualified；Donner-Reed重切后边缘qualified并后置。
- **2026-09-14**：完成三案Packet Feasibility Mini-Design；Starkloff=GREEN、IBM=GREEN-、Hirabayashi=AMBER-GREEN。
- **2026-09-14**：完成第一份Starkloff Case Packet Prototype v0.1；下一步进入首次闭卷试读与产品层反馈。
