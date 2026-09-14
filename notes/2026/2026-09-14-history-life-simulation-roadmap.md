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
  - D/L/W
  - 路线图
  - 案例筛选
  - 评分量表
source: "ChatGPT conversation | web research"
language: zh-CN
---

# 历史人生模拟阅读项目：路线图与进展

> 本笔记只维护**讨论脉络、项目路线、阶段状态和下一步**。具体规范另见：
>
> - [Decision Atom 正式字段表 v1](./2026-09-14-history-decision-atom-schema-v1.md)
> - [Decision Atom 软评分量表 v1](./2026-09-14-history-decision-atom-scoring-v1.md)

## 一句话结论

项目已经从“找一批有代入感的历史书”推进为：**先建立一套尽量关闭上帝视角的历史人生模拟案例筛选系统，再去规模化筛人物、案例与书。**

当前已完成：

> 目标定义 → D/L/W三轨 → 原12类重构 → 两轮结构压力测试 → Decision Atom v1 → 第三轮实操编码测试 → **M01—M10软评分量表v1**。

当前所在阶段：**筛选器的第一版已经基本闭环；下一步做第一次真正的候选排序实验，并优先按已落盘规则执行，而不是边做边改标准。**

---

# 1. 项目目标

此前的世界史、中国史阅读框架主要解决宏观问题：

> 世界/中国历史如何运行？制度、结构、长期因果怎样展开？

本项目解决另一条路径：

> **如果我是当事人，在那个时刻，只拥有他当时能够拥有的信息，我会怎么选？**

两条轨道的关系：

- **宏观史：给地图。**
- **微观人生模拟：练驾驶。**

目标不是寻找古人的“标准答案”，而是扩充自己未亲身经历的人生样本，训练在信息不完备、关系变化、利益冲突、价值冲突、风险和时间压力下的判断。

---

# 2. 路线怎样一步步收敛

## 2.1 从“人物/书”转向“案例结构”

最初直觉是通过英雄、奸雄、中人物、小人物和人物传记建立“人生案例库”。随后发现：

- 人物和书籍近乎无限；
- 一本传记内部包含很多性质不同的选择；
- “某某值得读”无法形成稳定筛选器。

因此第一次转向：**不先选人物、不先选书，而先找可重复出现的决策结构。**

## 2.2 原12类不再并列

最初12类包括路径选择、弱势求存、下注、止损、识人、合作、谈判、原则、成功、危机、退出、普通人等。

逐项打磨后确认，它们不在同一层级：

- 路径选择、下注、退出、授权、合作、谈判：决策原型；
- 弱势、成功、危机、结构巨变：情境状态；
- 原则与现实：规范性维度；
- 普通人：人物/决策单位尺度。

因此放弃“12个并列盒子”。

## 2.3 D / L / W 三轨

为了避免把所有微观史都硬切成“决策题”，确立：

- **D — Decision**：如果我是他，此刻怎么办？
- **L — Life-course**：这个人几十年怎样一步步变化？
- **W — World**：活在这种具体历史生活环境中是什么感觉？

当前设计最深入的是D轨；L/W后续再单独建设。

## 2.4 D轨核心决策原型

当前工作版：

1. **D1 路径选择与身份绑定**
2. **D2 高风险承诺与机会窗口**
3. **D3 持续投入、转向与退出**
4. **D4 识人、授权与制衡**
5. **D5 合作、承诺与关系变质**
6. **D6 对抗、谈判与让步边界**
7. **D7 角色退出、身份脱钩与权力交接**

另有：

- **N：价值冲突、角色义务与底线选择**，既可作主案例，也可作为横向规范性维度；
- 情境坐标：相对强弱、时间压力、环境变化、反馈状态、决策单位尺度、人物角色。

---

# 3. 两轮结构压力测试

## 第一轮

样本：

- 古巴导弹危机
- 华盛顿1783年辞职
- 刘大鹏
- 柯达数字化转型

主要暴露：

- 谁才是真正的决策主体；
- 结局熟悉之外还有更强的“叙事污染”；
- 著名历史节点不等于真实决策点；
- 人物/事件/书不能直接等同于案例；
- “高层/中层/普通人”过于粗糙。

## 第二轮

样本：

- 何如璋与琉球交涉
- 弗兰克一家进入藏匿状态
- 卡内基—弗里克合作关系
- 弗朗茨·雅格施泰特的价值困境

进一步形成：

- **Action Locus**：Direct / Recommend / Negotiate / Veto-Consent / Implement；
- **Deciders ≠ Affected Parties**；
- D5及部分D6可使用 **Paired Focal Perspective**；
- 真正规范性困境需要 **Normative Open-Conflict Test**。

---

# 4. Decision Atom：D类的基本单位

两轮压力测试之后，确立：

> **Decision Atom = 某个明确主体，在一个真实且仍开放的决策窗口内，基于当时可获得的信息，在两个以上现实可行方案之间，对一个核心问题作出具有实际后果的选择。**

人物、著名事件、一本传记、一家公司都不是Atom。

案例层级：

> **Case Field → Case Episode → Decision Atom → Case Packet**

另外有独立的 Sources 材料树：书、论文、档案、日记、书信、会议记录等，只承担 Background / Protagonist-Evidence / Narrative / Reveal-Review 等角色。

## 4.1 真实决策窗口

必须区分：

- Historical Event Node：历史事件节点；
- Decision Window：真实决策窗口；
- Freeze Point：人为设置的模拟冻结点。

Freeze应位于：

> **真实选择仍开放、但接近且尚未跨过主要 Commitment Threshold 的位置。**

## 4.2 主体边界

重大案例不能把国家、公司、家庭天然拟人化，需要区分：

- Focal Actor
- Formal Authority
- Effective Decider(s)
- Decision Group
- Veto / Constraint Holders
- Implementers
- Action Locus
- Deciders
- Affected Parties

## 4.3 时间边界与叙事污染

必须区分：

- Outcome Familiarity：知道后来结果；
- Narrative Contamination：已经被预装“这件事应该怎样理解”。

主要污染：

- Outcome leakage
- Causal preloading
- Moral/personality labeling
- Teleology
- Retrospective reconstruction

因此“关闭上帝视角”需要同时控制：

> **主体边界 + 时间边界。**

完整字段规范见：[Decision Atom 正式字段表 v1](./2026-09-14-history-decision-atom-schema-v1.md)。

---

# 5. 第三轮压力测试：Decision Atom v1 实操编码

第三轮不再主要寻找新理论，而是验证：面对真实历史候选，能否按v1稳定完成：

> 切Atom → 识别主体 → 找窗口 → 重建信息 → 约束选项 → Hard Gates。

样本与结果：

| 样本 | 目的 | 当前判断 |
|---|---|---|
| Frances Oldham Kelsey审核Kevadon/沙利度胺 | 中层专业人员、Veto/Consent、英雄叙事污染 | **结构上可成为合格Atom**；D2边界继续观察 |
| Boeing 747，1966 | 高风险商业/技术承诺；检验“著名故事”能否切成Atom | **目前仅Candidate**；主体与真实替代方案证据不足 |
| Stiles/Horr/Bonney家庭书信 | 普通家庭、长期迁徙；检验“材料丰富≠已有案例” | **Case Field / L-W富矿，不是Atom** |
| Atlantic Telegraph Company，1865失败后再投入 | 低污染、D3、董事会集体主体 | **强Candidate，接近合格Atom**；Freeze仍需锁定 |

第三轮的关键结果：

1. **v1开始具备拒绝坏案例的能力。**
2. **Option Evidence Grade** 能阻止后人把分析上合理的方案冒充当时真实选项。
3. 主体字段并不冗余，尤其在组织与中层案例中直接影响Atom是否成立。
4. Source Hindsight 与 Information Reconstructability 不能合并。
5. 当前最大边界歧义在 Primary Decision Type，特别是Kelsey式“高风险批准/放行阈值”；暂不新增D8，先继续观察D2是否需要抽象化。
6. 没有发现必须立即删除的核心字段；继续加字段的边际价值已明显下降。

---

# 6. 软评分量表 v1

第三轮以后完成 M01—M10 的可操作评分量表：

1. M01 Information Reconstructability
2. M02 Evidence Transparency
3. M03 Decision Tension
4. M04 Multi-perspective Potential
5. M05 Consequence Traceability
6. M06 Life Transfer Value
7. M07 Immersion Potential
8. M08 Background Efficiency
9. M09 Blind-Simulation Value
10. M10 Sample Novelty

关键规则：

- 每项0—5分，使用 **0 / 3 / 5锚点**；
- `3` 表示合格基线；
- 每个分数附 **H/M/L Confidence**；
- Candidate阶段只能打 Provisional Score；
- M08/M09/M10必须注明 `reader_baseline` 与 `library_snapshot`；
- **M01 ≥ 3 且 M02 ≥ 3** 才进入优先建设队列；
- **不设总分**，避免“史料薄弱但戏剧性强”的案例被虚假抬高。

四类案例画像：

- **闭卷模拟型**：M03/M07/M09高；
- **深度复盘型**：M01/M02/M03/M05高；
- **人生迁移型**：M06/M07高；
- **案例库补洞型**：M10高且基本质量合格。

第三轮样本校准显示：

- Kelsey：人生迁移 + 补洞 + 深度复盘；闭卷价值较低；
- Boeing 747：故事吸引力高，但M01/M02暂未过优先建设底线；
- Atlantic Telegraph 1865：闭卷、迁移、补洞都强，按本项目目标应优先于Boeing深挖。

完整规则见：[Decision Atom 软评分量表 v1](./2026-09-14-history-decision-atom-scoring-v1.md)。

---

# 7. 当前项目架构

> **模拟模式 D / L / W**
> ↓
> **若为D：先从Case Field切出Decision Atom**
> ↓
> **确定D1—D7 / N**
> ↓
> **主体拓扑 + Action Locus**
> ↓
> **Decision Window + Freeze + Commitment Threshold**
> ↓
> **当时信息集 + 现实选项集 + Option Evidence Grade**
> ↓
> **情境坐标 + 价值冲突**
> ↓
> **证据结构 + 叙事污染审计**
> ↓
> **Hard Gates**
> ↓
> **M01—M10 + Confidence**
> ↓
> **按案例画像与建设优先级排序**
> ↓
> **再从案例反推书与史料**
> ↓
> **制作 Case Packet 并试读复盘**

最重要原则仍然是：

> **先筛案例，再筛书；书是案例材料，不是案例本身。**

---

# 8. 总体路线与当前阶段

| Phase | 内容 | 状态 |
|---|---|---|
| 1 | 问题定义、D/L/W、初始情境分类 | 已完成 |
| 2 | 两轮结构压力测试；Decision Atom、窗口、主体、污染 | 已完成 |
| 3 | Decision Atom v1 实操编码测试 | 已完成 |
| 4 | M01—M10软评分量表v1 | **已完成** |
| 5 | 第一次候选排序实验 | **下一步** |
| 6 | 形成小规模高优先级候选池并深挖史料 | 未开始 |
| 7 | 从高分案例反推书籍/史料并制作Case Packet | 未开始 |
| 8 | 小规模试读（D/L/W混合）并校准 | 未开始 |
| 9 | 扩展为长期案例库/阅读路线 | 未开始 |

---

# 9. 下一小步：第一次真正的候选排序实验

下一步不再继续修改理论，也不预先追求“最好案例”。

建议只取 **6—8个故意多样的候选**，严格优先使用已经落盘的两份规则：

1. [Decision Atom 正式字段表 v1](./2026-09-14-history-decision-atom-schema-v1.md)
2. [Decision Atom 软评分量表 v1](./2026-09-14-history-decision-atom-scoring-v1.md)

实验流程固定为：

> 候选发现
> → 最小录入卡
> → Hard Gates初筛
> → Candidate / Qualified 才打 M01—M10暂定分 + Confidence
> → 不设总分
> → 分成三组：**优先深挖 / 保留候选并补证据 / 暂不投入或分流L-W**。

本轮重点不是“挑出最伟大的历史人物”，而是检验：

- 已落盘规则是否能稳定压过名气、戏剧性和个人直觉；
- 是否会自然把低史料/高故事性的候选降级；
- 是否会把低知名度但高史料、高闭卷价值的案例推到前面；
- 哪些字段或分数真正影响排序；
- 是否存在同一规则在多个样本上反复失效的情况。

**规则变更原则：**

> 单个新样本不触发改模。只有同一问题在多个候选上重复出现，才修改字段、D1—D7边界或评分锚点。

这样才能真正检验“筛选器”，而不是让筛选器追着案例跑。

---

## Revision log

- **2026-09-14**：建立路线笔记；记录前两轮压力测试与Decision Atom v1形成过程。
- **2026-09-14**：完成第三轮实操编码压力测试；确认v1基本可操作，记录D2“审批/放行阈值”边界问题。
- **2026-09-14**：完成M01—M10软评分量表v1；增加0/3/5锚点、H/M/L置信度、Scoring Context、可靠性底线与四类案例画像；下一步进入第一次候选排序实验，并明确优先使用已落盘规则。