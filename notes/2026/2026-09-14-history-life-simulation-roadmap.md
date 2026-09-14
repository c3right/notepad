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
source: "ChatGPT conversation | web research"
language: zh-CN
---

# 历史人生模拟阅读项目：路线图与进展

> 本笔记只维护**讨论脉络、项目路线、阶段状态和下一步**。具体规范与实验结果另见：
>
> - [Decision Atom 正式字段表 v1](./2026-09-14-history-decision-atom-schema-v1.md)
> - [Decision Atom 软评分量表 v1](./2026-09-14-history-decision-atom-scoring-v1.md)
> - [第一次候选排序实验](./2026-09-14-history-decision-atom-ranking-experiment-1.md)

## 一句话结论

项目已经从“找一批有代入感的历史书”推进为一套可操作的筛选路线：

> **先定义历史人生模拟的基本单位 → 验证真实决策窗口与主体边界 → 建立Hard Gates → 建立M01—M10软评分 → 用真实候选排序 → 再从高优先级案例反推书籍与史料。**

当前已完成：

> 目标定义 → D/L/W三轨 → 原12类重构 → 两轮结构压力测试 → Decision Atom v1 → 第三轮实操编码测试 → M01—M10评分量表v1 → **第一次8候选排序实验**。

当前所在阶段：**筛选器v1已从“理论框架”进入“真实研究工作流”验证；下一步应做A档候选的Qualification Sprint，而不是扩大到几十上百个案例。**

---

# 1. 项目目标

宏观历史阅读主要解决：

> 世界如何运行？制度、结构、长期因果如何展开？

本项目解决另一条路径：

> **如果我是当事人，在那个时刻，只拥有他当时能够拥有的信息，我会怎么选？**

两条轨道：

- **宏观史：给地图。**
- **微观人生模拟：练驾驶。**

目标不是提炼成功学答案，而是扩充未亲身经历的人生样本，训练在不确定性、有限权限、组织关系、价值冲突、风险和时间压力下判断。

---

# 2. 路线如何收敛

## 2.1 从人物/书转向案例结构

最初想通过英雄、奸雄、中人物、小人物与人物传记建立“人生样本库”。很快发现：

- 人物和书籍近乎无限；
- 一本传记内部存在多个性质不同的选择；
- “哪些人物值得读”没有稳定筛选边界。

于是转向：**先定义反复出现的决策结构，再找历史中的高质量样本。**

## 2.2 原12类不再并列

逐类打磨后确认：

- 路径选择、下注、退出、授权、合作、谈判等属于**决策原型**；
- 弱势、成功、危机、结构巨变属于**情境状态**；
- 原则与现实属于**规范性维度**；
- 普通人属于**人物/决策单位尺度**。

因此放弃“12个并列盒子”。

## 2.3 D / L / W三轨

- **D — Decision**：如果我是他，此刻怎么办？
- **L — Life-course**：这个人几十年怎样一步步变化？
- **W — World**：活在这种具体历史生活环境中是什么感觉？

当前D轨已经形成较成熟工作流；L/W后续再单独建设。

## 2.4 D轨核心类型

当前工作版：

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

---

# 3. Decision Atom：D轨的最小单位

核心定义：

> **Decision Atom = 某个明确主体，在一个真实且仍开放的决策窗口内，基于当时可获得的信息，在两个以上现实可行方案之间，对一个核心问题作出具有实际后果的选择。**

人物、事件、一本书、一家公司、整段战争都不是Atom。

案例层级：

> **Case Field → Case Episode → Decision Atom → Case Packet**

材料另成一棵Sources树：书、论文、档案、日记、书信、会议记录等只承担 Background / Protagonist-Evidence / Narrative / Reveal-Review 等角色。

## 3.1 真实决策窗口

必须区分：

- Historical Event Node：著名历史节点；
- Decision Window：真实开放的决策窗口；
- Freeze Point：人为设置的模拟冻结点。

Freeze原则：

> **真实选择仍开放，但已接近且尚未跨过主要Commitment Threshold。**

## 3.2 主体边界

不能把国家、企业、家庭天然拟人化。需要区分：

- Focal Actor
- Formal Authority
- Effective Decider(s)
- Decision Group
- Veto / Constraint Holders
- Implementers
- Action Locus
- Deciders
- Affected Parties

中层人物即使没有最终拍板权，也可能存在真实Decision Atom，例如 Recommend / Negotiate / Veto-Consent / Implement。

## 3.3 叙事污染

必须区分：

- Outcome Familiarity：知道后来结果；
- Narrative Contamination：已经被预装“这件事应该怎样理解”。

主要污染：结果泄露、因果预装、人格/道德标签、目的论、回忆性重构。

因此“关闭上帝视角”需要同时控制：

> **主体边界 + 时间边界。**

---

# 4. 三轮压力测试

## 4.1 第一轮：找结构漏洞

样本：古巴导弹危机、华盛顿1783辞职、刘大鹏、柯达数字化。

主要发现：

- 著名事件节点不等于真实决策点；
- 人物/事件/书不能直接等同于案例；
- 决策主体必须拆解；
- 除结果熟悉外，还存在更强的叙事污染。

## 4.2 第二轮：压主体、家庭、关系、价值

样本：何如璋与琉球交涉、弗兰克一家藏匿、卡内基—弗里克、雅格施泰特。

新增：

- Action Locus；
- Deciders ≠ Affected Parties；
- D5/部分D6允许Paired Focal Perspective；
- N型需要Normative Open-Conflict Test。

## 4.3 第三轮：拿v1实际编码

样本：Kelsey、Boeing 747、Stiles/Horr/Bonney家庭书信、Atlantic Telegraph 1865。

主要结果：

- v1能够拒绝“故事很好但还不是Atom”的材料；
- Option Evidence Grade能阻止后人虚构选项；
- 主体字段并不冗余；
- Source Hindsight与Information Reconstructability不能合并；
- D2出现“高风险批准/放行”边界问题，但当时没有立刻改规则。

---

# 5. 软评分量表v1

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

关键规则：

- 每项0—5，使用0/3/5锚点；
- 每项附H/M/L置信度；
- Candidate只能打Provisional Score；
- M08/M09/M10注明Reader Baseline与Library Snapshot；
- **M01 ≥ 3 且 M02 ≥ 3** 才进入优先建设队列；
- 不设总分，按案例画像判断。

四种画像：

- 闭卷模拟型
- 深度复盘型
- 人生迁移型
- 案例库补洞型

详见：[软评分量表v1](./2026-09-14-history-decision-atom-scoring-v1.md)。

---

# 6. 第一次真正的候选排序实验

本轮固定已落盘规则，不因个案精彩临时移动尺度。8个新候选：

1. Max Starkloff / St. Louis 1918
2. Gordon Hirabayashi 1942
3. IBM System/360 1961—1962
4. Donner-Reed / Hastings Cutoff 1846
5. Challenger / Thiokol 1986
6. Chiune Sugihara 1940
7. Camp David 1978最后阶段定居点文字
8. Shackleton / James Caird 1916（当前切法）

## 6.1 当前研究投入排序

### A档：优先Qualification Sprint

1. **Starkloff**：窗口清楚、低污染、背景成本低，最像第一批闭卷Packet。
2. **Hirabayashi**：个人/N型、家庭受影响、身份与价值冲突；重点补Freeze前材料以核N-Gate。
3. **IBM System/360**：商业/技术D2价值高；重点锁定真正批准主体、窗口、替代方案。
4. **Donner-Reed**：普通移民家庭与路线选择价值高；重点重建Fort Bridger集体决策拓扑。

### B档：保留但后置

- **Challenger**：Decision Atom几乎范本级，但M09接近0；作为深度复盘/控制样本，而非第一批闭卷案例。
- **Sugihara**：中层官员价值很强，但英雄叙事污染高，N-Gate和Freeze前同时代材料还需加强。
- **Camp David**：D6、多视角、史料透明度都强，但背景负担极高且官方记录存在会谈缺口，适合成熟期高阶案例。

### C档：当前Atom停止投入

- **Shackleton / James Caird当前切法**：史料、代入和后果都强，但“出海求援 vs 原地等待”未必是真正有张力的两个现实方案；GATE-2/M03失败风险高。转L/W或重新切更早决策窗口。

完整实验见：[第一次候选排序实验](./2026-09-14-history-decision-atom-ranking-experiment-1.md)。

## 6.2 本轮验证了什么

1. **Hard Gates优先于软评分。** 戏剧性不能救一个没有真实开放选项的案例。
2. **M08/M09会真正改变排序。** Camp David、Challenger因背景成本/叙事污染后移；Starkloff等陌生案例上升。
3. **M10不是“冷门奖励”。** 新颖性必须是结构补洞，而不是单纯陌生。
4. 筛选器已经开始产生“低知名度但更适合本项目”的结果，方向符合预期。

## 6.3 D2边界问题已重复出现

Kelsey、Challenger、Starkloff先后出现同构结构：

> 决策者不是“自己重仓”，而是判断**是否授权/批准/触发一个低可逆、高下行风险的系统状态**。

这使D2“高风险承诺与机会窗口”可能偏窄。观察候选的新名称是：

> **D2 高风险承诺、授权与放行阈值**

当前仍**不修改正式v1**。至少再经过A档Qualification Sprint或更多同构样本后再决定，避免因三四个案例就过度改模型。

---

# 7. 当前项目架构

> **D / L / W**
> ↓
> **若为D：从Case Field切出Decision Atom**
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
> **候选排序 / Qualification Sprint**
> ↓
> **从案例反推书籍与史料**
> ↓
> **制作Case Packet**
> ↓
> **实际闭卷试读与复盘**

始终保持：

> **先筛案例，再筛书；书是材料，不是案例。**

---

# 8. 总体Phase状态

| Phase | 内容 | 状态 |
|---|---|---|
| 1 | 目标定义、D/L/W、初始分类 | 已完成 |
| 2 | 两轮结构压力测试；Decision Atom、窗口、主体、污染 | 已完成 |
| 3 | Decision Atom v1实操编码测试 | 已完成 |
| 4 | M01—M10软评分量表v1 | 已完成 |
| 5 | 第一次真实候选排序实验 | **已完成** |
| 6 | A档候选Qualification Sprint | **下一步** |
| 7 | 建立首批qualified案例池；从案例反推书籍/史料 | 未开始 |
| 8 | 制作第一批Case Packet并实际闭卷试读 | 未开始 |
| 9 | 校准后扩展D库，并开始系统建设L/W | 未开始 |
| 10 | 扩展为长期案例库/阅读路线 | 未开始 |

---

# 9. 下一小步：Qualification Sprint

不立即扩大到几十个候选。先用最少研究成本解决A档四个案例各自最大的阻塞点：

1. **Starkloff**：核1918年10月6—8日同时代报纸/卫生年报与市长授权链；确认Freeze和主体拓扑。
2. **Hirabayashi**：寻找决定之前的日记、书信或同时代记录；验证N-Gate与真实选项。
3. **IBM System/360**：定位SPREAD报告被管理层接受的具体时间、正式/实际决策者及真实替代方案。
4. **Donner-Reed**：重建Fort Bridger前后的家庭/领导者实际决策机制；避免把整个车队拟人成一个主体。

Sprint的停止条件：

> 如果四个中至少2—3个能稳定成为qualified Atom，且M01/M02≥3，就不再继续理论设计，正式进入“从案例反推书与史料、制作第一批Case Packet”。

如果A档普遍卡在同一Hard Gate，则回头修规则；否则不再为了边缘例外扩字段。

---

## Revision log

- **2026-09-14**：建立路线笔记；记录前两轮压力测试与Decision Atom v1形成过程。
- **2026-09-14**：完成第三轮实操编码测试；确认v1基本可操作。
- **2026-09-14**：建立M01—M10软评分量表v1；明确不求总分、使用Confidence与案例画像。
- **2026-09-14**：完成第一次8候选排序实验；形成A/B/C行动队列，下一步转入A档Qualification Sprint；D2“授权/放行阈值”进入观察名单但暂不修改v1。
