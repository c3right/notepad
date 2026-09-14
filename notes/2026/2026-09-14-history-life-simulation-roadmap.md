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
  - 候选排序
  - qualification
source: "ChatGPT conversation | web research"
language: zh-CN
---

# 历史人生模拟阅读项目：路线图与进展

> 本笔记只维护**讨论脉络、当前架构、阶段状态和下一步**。细节分别见：
>
> - [Decision Atom 正式字段表 v1](./2026-09-14-history-decision-atom-schema-v1.md)
> - [Decision Atom 软评分量表 v1](./2026-09-14-history-decision-atom-scoring-v1.md)
> - [第一次候选排序实验](./2026-09-14-history-decision-atom-ranking-experiment-1.md)
> - [Qualification Sprint 1](./2026-09-14-history-decision-atom-qualification-sprint-1.md)

## 一句话状态

项目已经从“找一批有代入感的历史书”推进为一套可运行的研究管线：

> **D/L/W定位 → Case Field切片 → Decision Atom → 主体/窗口/信息/选项审计 → Hard Gates → M01—M10排序 → Qualification Sprint → qualified案例 → 反推材料 → Case Packet → 闭卷试读与复盘。**

截至目前，筛选器v1已通过三轮压力测试、一次8候选排序实验和一次Qualification Sprint。首批可进入Packet可行性设计的三个案例已经出现：

1. **Max Starkloff / St. Louis 1918**
2. **Gordon Hirabayashi / 1942**
3. **IBM System/360 / Vin Learson 1962**

Donner-Reed原来的Fort Bridger切法被否决；重切为James Reed在Little Sandy前后的家庭路线选择后可勉强进入D库，但证据后见性较强，暂时后置。

---

# 1. 项目目标

宏观历史轨解决：

> 世界如何运行？制度、结构、长期因果怎样展开？

本项目的微观轨解决：

> **如果我是当事人，在那个时刻，只拥有他当时能够拥有的信息，我会怎么选？**

因此：

- **宏观史：给地图。**
- **微观人生模拟：练驾驶。**

目标不是提炼成功学答案，而是扩充未亲历的人生样本，训练在不确定性、有限权限、组织关系、风险、身份与价值冲突中的判断。

---

# 2. 路线如何收敛

## 2.1 从人物/书转向案例结构

人物和传记数量近乎无限，而且同一人生内部存在多个性质不同的决策。于是放弃“先选名人、再选传记”，改为：

> **先识别可重复出现的决策结构，再去历史中找高质量真人样本。**

## 2.2 D / L / W 三轨

- **D — Decision**：如果我是他，此刻怎么办？
- **L — Life-course**：这个人几十年怎样一步步变化？
- **W — World**：活在这种具体历史生活世界中是什么感觉？

当前D轨已形成较完整工作流；L/W后续再单独建设。

## 2.3 D轨核心类型

当前工作版：

1. **D1 路径选择与身份绑定**
2. **D2 高风险承诺与机会窗口**
3. **D3 持续投入、转向与退出**
4. **D4 识人、授权与制衡**
5. **D5 合作、承诺与关系变质**
6. **D6 对抗、谈判与让步边界**
7. **D7 角色退出、身份脱钩与权力交接**

另有：

- **N：价值冲突、角色义务与底线选择**；
- 情境坐标：相对强弱、时间压力、环境变化、反馈状态、决策单位尺度、角色身份。

D2“高风险批准/授权/触发阈值”的边界已在Kelsey、Challenger、Starkloff等案例中重复出现，但暂未修改正式v1；继续以边界判例观察。

---

# 3. Decision Atom：D轨最小单位

> **Decision Atom = 某个明确主体，在一个真实且仍开放的决策窗口内，基于当时可获得的信息，在两个以上现实可行方案之间，对一个核心问题作出具有实际后果的选择。**

人物、事件、一本书、一家公司、整场战争都不是Atom。

层级：

> **Case Field → Case Episode → Decision Atom → Case Packet**

书、论文、档案、日记、书信、会议记录另属Sources树，承担：

- B — Background
- P — Protagonist / Evidence
- N — Narrative
- R — Reveal / Review

核心防错原则：

- Historical Event Node ≠ Decision Window ≠ Freeze Point；
- Freeze应位于真实选择仍开放、但尚未越过主要Commitment Threshold的位置；
- 国家、企业、家庭不能天然拟人化；
- 后人能想出的方案不能冒充当事人当时真实考虑的方案；
- Outcome Familiarity与Narrative Contamination必须分开；
- N型必须通过Normative Open-Conflict Test。

---

# 4. 已完成的验证

## 4.1 第一轮结构压力测试

样本：古巴导弹危机、华盛顿1783辞职、刘大鹏、柯达数字化。

主要发现：

- 著名场面不等于真实决策点；
- 人物/事件/书不能直接等同于案例；
- 主体需要拆解；
- 结果熟悉之外还有因果预装、人格标签、目的论等叙事污染。

## 4.2 第二轮结构压力测试

样本：何如璋与琉球交涉、弗兰克一家藏匿、卡内基—弗里克、雅格施泰特。

新增：

- Action Locus：Direct / Recommend / Negotiate / Veto-Consent / Implement；
- Deciders ≠ Affected Parties；
- D5/部分D6允许Paired Focal Perspective；
- N型加入Normative Open-Conflict Test。

## 4.3 第三轮实操编码测试

样本：Kelsey、Boeing 747、Stiles/Horr/Bonney家庭书信、Atlantic Telegraph 1865。

验证：

- v1能拒绝“故事很好但还不是Atom”的材料；
- Option Evidence Grade能阻止后见方案偷渡；
- 主体字段并不冗余；
- Source Hindsight与Information Reconstructability不能合并；
- 没有发现需要立即删除的核心字段。

---

# 5. Hard Gates与软评分

Hard Gates判断：

> **它是不是一个可靠Decision Atom？**

M01—M10判断：

> **它值不值得现在优先投入研究成本并制作Case Packet？**

M01—M10：

1. Information Reconstructability
2. Evidence Transparency
3. Decision Tension
4. Multi-perspective Potential
5. Consequence Traceability
6. Life Transfer Value
7. Immersion Potential
8. Background Efficiency
9. Blind-Simulation Value
10. Sample Novelty

规则：

- 0—5分，0/3/5锚点；
- 每项附H/M/L Confidence；
- Candidate阶段只打Provisional Score；
- M08/M09/M10记录Reader Baseline与Library Snapshot；
- **M01 ≥ 3 且 M02 ≥ 3** 才进入优先建设队列；
- 不机械求总分，使用案例画像。

---

# 6. 第一次候选排序实验

8个新候选：Starkloff、Hirabayashi、IBM System/360、Donner-Reed、Challenger、Sugihara、Camp David、Shackleton/James Caird。

排序实验的关键结果：

- Starkloff等低知名度、高可重建、低污染案例被推到前面；
- Challenger虽然史料范本级，但M09几乎为0，更适合深度复盘而非第一批闭卷模拟；
- Camp David因背景成本高而后置；
- Shackleton当前切法被Hard Gate挡住，说明戏剧性不能救一个缺乏真实选项张力的Atom。

详见：[第一次候选排序实验](./2026-09-14-history-decision-atom-ranking-experiment-1.md)。

---

# 7. Qualification Sprint 1

Sprint原则：每个A档候选只解决阻碍qualified的1—2个关键问题，不直接制作完整Packet。

## 7.1 Max Starkloff / St. Louis 1918

**状态：Qualified。**

关键重切：

> 不是“圣路易斯是否关闭城市”，而是**Starkloff是否从10月6日仍偏向病例隔离/有限措施，升级为10月7日主动推动全市学校、娱乐场所与公共集会关闭。**

这样Focal Actor、Action Locus、真实选项和Freeze都变得清楚，不再把整个市政府拟人成一个主体。

## 7.2 Gordon Hirabayashi / 1942

**状态：Qualified；N-Gate Confidence = Medium。**

1942年同时代声明强力证明Christian / democratic / civil-liberty obligation。后来第一人口述证明家庭团聚、服从紧急秩序并非后人替他虚构，而且他直到最后约一周仍准备随迁。

局限：家庭义务这一侧主要依赖Retrospective Evidence。因此可通过N-Gate，但Packet必须显式标注材料时间身份，不能把后来口述伪装成1942年日记。

## 7.3 IBM System/360 / 1962

**状态：Qualified after re-cut。**

关键重切：放弃“IBM赌上公司”的后见故事，锁定：

> **1962年1月初，Vin Learson面对SPREAD最终报告时，是否把统一兼容New Product Line正式设为IBM开发方向并要求组织执行。**

这一切法能恢复真实异议、成功旧产品线、自我蚕食风险和SPREAD方案，而不是把1964发布会或后来“50亿美元豪赌”当成Freeze。

## 7.4 Donner-Reed / Hastings Cutoff

**原Atom：Rejected / must re-cut。**

Fort Bridger已经偏晚；真正初始路线承诺发生在Little Sandy分路。整个Donner Party也不应被拟人成统一决策者。

重切为：

> **James F. Reed在Little Sandy前后，是否让自己的家庭/车队离开传统Fort Hall路线，转向Fort Bridger并计划尝试Hastings Cutoff。**

重切后：**边缘Qualified，但后置。**

主要限制不是故事性，而是Freeze前完整信息世界大量依赖后见回忆；M01/M02只能贴近3分线。

详见：[Qualification Sprint 1](./2026-09-14-history-decision-atom-qualification-sprint-1.md)。

---

# 8. 当前项目架构

> **D / L / W**
> ↓
> **Case Field → Decision Atom**
> ↓
> **D1—D7 / N**
> ↓
> **主体拓扑 + Action Locus**
> ↓
> **Decision Window + Freeze + Commitment Threshold**
> ↓
> **当时信息集 + 现实选项 + Option Evidence Grade**
> ↓
> **情境坐标 + 规范性维度**
> ↓
> **证据结构 + 叙事污染审计**
> ↓
> **Hard Gates**
> ↓
> **M01—M10 + Confidence + 案例画像**
> ↓
> **候选排序 → Qualification Sprint**
> ↓
> **qualified案例 → 反推B/P/N/R材料**
> ↓
> **Case Packet Feasibility → 完整Packet**
> ↓
> **实际闭卷试读与复盘**

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
| 6 | A档候选Qualification Sprint | **已完成** |
| 7 | 首批qualified案例的Packet Feasibility Mini-Design | **下一步** |
| 8 | 制作第一批完整Case Packet并实际闭卷试读 | 未开始 |
| 9 | 扩展D候选池；校准后再系统建设L/W | 未开始 |
| 10 | 扩展为长期案例库/阅读路线 | 未开始 |

---

# 10. 下一小步：Packet Feasibility Mini-Design

先不继续扩大候选池，也不立刻写完整Packet。

仅对三个已稳定qualified的案例：

1. **Starkloff 1918**
2. **Hirabayashi 1942**
3. **IBM System/360 1962**

分别做一个最小“Packet可行性设计”，只回答：

- Background最少需要什么，能否压缩而不失真；
- P/Evidence哪些材料可以真正放进Freeze前；
- Narrative材料怎样增强代入而不偷渡未来；
- Reveal/Review需要哪些材料才能把实际选择、结果、偶然性与史家解释分开；
- 哪些材料必须严格隔离到Freeze之后；
- 预计制作成本与主要材料缺口。

停止条件：如果三个中至少两个能够以可接受背景成本形成清楚的B/P/N/R结构，就进入第一批完整Case Packet制作；如果qualified Atom普遍难以产品化，再回头检查“评分高 ≠ 可制作”的缺口。

---

## Revision log

- **2026-09-14**：建立路线笔记；记录前两轮压力测试与Decision Atom v1形成过程。
- **2026-09-14**：完成第三轮实操编码测试；确认v1基本可操作。
- **2026-09-14**：建立M01—M10软评分量表v1。
- **2026-09-14**：完成第一次8候选排序实验；形成A/B/C行动队列。
- **2026-09-14**：完成Qualification Sprint 1；Starkloff、Hirabayashi与重切后的IBM System/360进入qualified；Donner-Reed原切法被否决并重切。下一步转入Packet Feasibility Mini-Design。
