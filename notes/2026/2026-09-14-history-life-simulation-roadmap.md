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
  - 案例筛选
  - qualification
source: "ChatGPT conversation | web research"
language: zh-CN
---

# 历史人生模拟阅读项目：路线图与进展

> 本笔记只维护**讨论脉络、当前架构、阶段状态和下一步**。具体规则与实验另见：
>
> - [Decision Atom 正式字段表 v1](./2026-09-14-history-decision-atom-schema-v1.md)
> - [Decision Atom 软评分量表 v1](./2026-09-14-history-decision-atom-scoring-v1.md)
> - [第一次候选排序实验](./2026-09-14-history-decision-atom-ranking-experiment-1.md)
> - [Qualification Sprint 1](./2026-09-14-history-decision-atom-qualification-sprint-1.md)
> - [首批 Case Packet Feasibility Mini-Design](./2026-09-14-history-case-packet-feasibility-mini-design-1.md)

## 一句话状态

项目已经从“找一批有代入感的历史书”推进为一条可运行的研究管线：

> **D/L/W定位 → Case Field切片 → Decision Atom → 主体/窗口/信息/选项审计 → Hard Gates → M01—M10排序 → Qualification Sprint → qualified案例 → B/P/N/R材料设计 → Case Packet Feasibility → Packet原型 → 闭卷试读与复盘。**

当前筛选器v1已通过三轮压力测试、一次8候选排序实验、一次Qualification Sprint，并完成首批三个qualified案例的Packet可行性设计。

下一步不再继续扩大候选池：**先把 Starkloff / St. Louis 1918 做成第一份可实际阅读的 Case Packet Prototype v0.1。**

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

当前D轨已形成完整工作流；L/W后续再单独建设。

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

D2“高风险批准/授权/触发阈值”的边界已在Kelsey、Challenger、Starkloff等案例中重复出现，但暂未修改正式v1；继续观察。

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

第一轮：古巴导弹危机、华盛顿1783辞职、刘大鹏、柯达数字化。主要解决真实决策点、案例基本单位、主体边界和叙事污染。

第二轮：何如璋、弗兰克一家、卡内基—弗里克、雅格施泰特。加入Action Locus、Deciders ≠ Affected Parties、Paired Focal Perspective、Normative Open-Conflict Test。

第三轮：Kelsey、Boeing 747、Stiles/Horr/Bonney家庭书信、Atlantic Telegraph 1865。验证v1可以拒绝“故事很好但还不是Atom”的材料，并确认Option Evidence Grade、主体字段、Source Hindsight等实际有用。

## 3.2 Hard Gates与软评分

Hard Gates判断“它是不是可靠的Decision Atom”；M01—M10判断“值不值得现在投入研究和制作成本”。

M01—M10：Information Reconstructability、Evidence Transparency、Decision Tension、Multi-perspective Potential、Consequence Traceability、Life Transfer Value、Immersion Potential、Background Efficiency、Blind-Simulation Value、Sample Novelty。

使用规则：0—5分、0/3/5锚点、H/M/L Confidence；M01/M02至少3才进优先建设队列；不机械求总分。

---

# 4. 第一次候选排序实验

8个新候选：Starkloff、Hirabayashi、IBM System/360、Donner-Reed、Challenger、Sugihara、Camp David、Shackleton/James Caird。

结果验证：

- 低知名度、高可重建、低污染案例会被推到前面；
- Challenger史料优秀但闭卷价值低，更适合深度复盘；
- Camp David背景成本高而后置；
- Shackleton当前切法被Hard Gate挡住，说明戏剧性不能替代真实决策张力。

---

# 5. Qualification Sprint 1

## 5.1 Starkloff / St. Louis 1918

**Qualified。** 重切为：

> Starkloff是否从10月6日仍偏向病例隔离/有限措施，升级为10月7日主动推动全市学校、娱乐场所与公共集会关闭。

## 5.2 Gordon Hirabayashi / 1942

**Qualified；N-Gate Confidence = Medium。**

1942年同时代声明强力证明Christian / democratic / civil-liberty obligation；家庭团聚与原本准备随迁主要由后来第一人口述支持，因此Packet必须明确标记Retrospective Evidence。

## 5.3 IBM System/360 / Vin Learson 1962

**Qualified after re-cut。** 重切为：

> 1962年1月初，Vin Learson面对SPREAD最终报告时，是否把统一兼容New Product Line正式设为IBM开发方向并要求组织执行。

## 5.4 Donner-Reed

Fort Bridger原Atom被否决；重切为James Reed在Little Sandy前后是否让家庭/车队离开传统Fort Hall路线，转向Fort Bridger并计划Hastings Cutoff。重切后边缘Qualified，但Freeze前信息世界大量依赖后见回忆，暂时后置。

---

# 6. 首批 Case Packet Feasibility Mini-Design

三个qualified案例均可产品化，但Packet可行性排序与qualification价值略有不同。

| 案例 | Packet Verdict | 主要理由 |
|---|---|---|
| **Starkloff 1918** | **GREEN / Build #1** | Freeze极清楚、同时代P材料强、背景可压缩、人物结局污染低 |
| **IBM / Learson 1962** | **GREEN- / Build #2** | SPREAD原报告提供罕见内部P材料；真实替代路线和组织异议可恢复，但技术/组织背景较重 |
| **Hirabayashi 1942** | **AMBER-GREEN / Build #3** | 人生与N型价值极高，但关键家庭义务与内心未决性部分依赖later recollection |

详见：[首批 Case Packet Feasibility Mini-Design](./2026-09-14-history-case-packet-feasibility-mini-design-1.md)。

## 6.1 Starkloff Packet设计要点

- Freeze：1918-10-07跨部门会议前/初始阶段，尚未提出并取得全市关闭路线同意；
- B：仅补流感、军营病例、市政权限和可用措施；
- P：10月6日有限措施公开立场、10月7日病例恶化、会议反对意见与权限结构；
- N：9月底→10月5→10月6→10月7的窄时间线；
- R：实际关闭、执行反弹/调整、后世城市比较研究；
- 最大污染：现代COVID经验造成的**Analogical Contamination / 类比污染**。

## 6.2 IBM Packet设计要点

- Freeze：SPREAD报告提交最高管理层、异议已经出现，但Learson尚未宣布接受执行；
- B：产品线不兼容、现有1400等成功产品、自我蚕食与客户迁移成本；
- P：1961-12-28 SPREAD Final Report、真实替代路线和组织异议；
- N：产品线冲突→SPREAD→报告→mixed reaction→Freeze；
- R：实际接受、成本失控风险、1964发布、长期收益与副作用；
- 最大污染：“bet the company / 伟大豪赌”商业寓言。

## 6.3 Hirabayashi Packet设计要点

- Freeze不能伪装成精确瞬间，应使用1942年5月上旬至约5月10日的**Freeze Window**；
- B：EO9066、Public Law 503、curfew、Seattle排除令、Gordon的身份和Quaker/CO背景；
- P：同时代法律/行为材料 + 明确标记的later first-person recollection；
- 关键处理：可设置 **Reconstructed Memory Card**，公开告诉读者这些家庭谈话和内心变化来自后来口述；
- R：拒绝登记与自首、1943最高法院、1980年代发现被压制材料、1987撤销定罪；
- 最大污染：英雄标签、后来法律平反，以及**Source-Metadata Leakage / 来源元数据泄露**。

## 6.4 本轮新增两个Packet层实现风险

暂不修改Decision Atom v1，只作为编辑规则观察：

1. **Analogical Contamination**：现代读者会把现代同构事件/争论投射到历史决策；
2. **Source-Metadata Leakage**：即使later recollection只讲Freeze前经历，标注“1999口述史”本身也泄露部分未来。

当前处理原则：宁可牺牲少量盲模拟纯度，也不牺牲史料透明度。

---

# 7. 当前项目架构

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
> **Case Packet Prototype**
> ↓
> 实际闭卷试读与复盘

始终保持：

> **先筛案例，再筛书；书是材料，不是案例。**

---

# 8. Phase状态

| Phase | 内容 | 状态 |
|---|---|---|
| 1 | 目标定义、D/L/W、初始分类 | 已完成 |
| 2 | 两轮结构压力测试；Atom、窗口、主体、污染 | 已完成 |
| 3 | Decision Atom v1实操编码测试 | 已完成 |
| 4 | M01—M10软评分量表v1 | 已完成 |
| 5 | 第一次真实候选排序实验 | 已完成 |
| 6 | A档候选Qualification Sprint | 已完成 |
| 7 | 首批qualified案例的Packet Feasibility Mini-Design | **已完成** |
| 8 | Starkloff Case Packet Prototype v0.1 + 首次闭卷试读设计 | **下一步** |
| 9 | IBM / Hirabayashi Packet；扩展D候选池；开始系统建设L/W | 未开始 |
| 10 | 扩展为长期案例库/阅读路线 | 未开始 |

---

# 9. 下一小步：Starkloff Case Packet Prototype v0.1

先只做一份，不同时开三份。

目标是第一次把规则变成真正可阅读的产品：

> **Background → Reader-visible Evidence → Neutral Narrative → Freeze Task → 独立封存的 Reveal / Debrief。**

原型完成后重点检查三件事：

1. 不看Reveal时，读者是否真的仍不知道“标准答案”；
2. Background是否足够进入1918年情境而不过量；
3. Reveal后能否明确区分**决策质量**与**结果质量**，而不是把“后来效果较好”直接反推成“当时决策必然正确”。

如果Starkloff原型工作，再按IBM、Hirabayashi顺序制作；如果产品层面失败，应先修Packet编辑方法，而不是继续增加案例数量。

---

## Revision log

- **2026-09-14**：建立路线笔记；记录前两轮压力测试与Decision Atom v1形成过程。
- **2026-09-14**：完成第三轮实操编码测试；确认v1基本可操作。
- **2026-09-14**：建立M01—M10软评分量表v1。
- **2026-09-14**：完成第一次8候选排序实验；形成A/B/C行动队列。
- **2026-09-14**：完成Qualification Sprint 1；Starkloff、Hirabayashi与重切后的IBM进入qualified；Donner-Reed重切后边缘qualified并后置。
- **2026-09-14**：完成三案Packet Feasibility Mini-Design；Starkloff=GREEN、IBM=GREEN-、Hirabayashi=AMBER-GREEN；下一步只制作Starkloff Case Packet Prototype v0.1。