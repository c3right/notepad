---
title: "历史人生模拟案例库：Decision Atom 正式字段表 v1"
date: 2026-09-14
updated: 2026-09-14
status: working
type: reference
topics:
  - history
  - decision-making
  - case-method
  - reading-path
  - historiography
keywords:
  - Decision Atom
  - historical decision case
  - decision window
  - freeze point
  - narrative contamination
  - case packet
  - D/L/W
source: "ChatGPT conversation"
language: zh-CN
---

# 历史人生模拟案例库：Decision Atom 正式字段表 v1

## 一句话结论

为了建立一种尽量关闭“上帝视角”的历史人生模拟阅读路径，D（Decision）类案例的最小基本单位应定义为 **Decision Atom（决策原子）**：**某个明确主体，在一个真实且仍然开放的决策窗口内，基于当时可获得的信息，在两个以上现实可行方案之间，对一个核心问题作出具有实际后果的选择。**

人物、著名事件、一本传记、一家公司乃至“一场危机”都不是 Decision Atom；它们最多只是案例矿区、材料来源或情境背景。

v1 的目标不是把所有可能字段都记录下来，而是建立一套足够严格、又不至于过度设计的结构，使后续人物与书籍筛选时能够提前挡住几类高成本误判：

- 名人 ≠ 好案例；
- 著名历史场面 ≠ 真实决策点；
- 一本好书 ≠ 一个案例；
- 国家/公司/家庭 ≠ 天然的单一决策者；
- 后人能想到的方案 ≠ 当时真实开放的方案；
- 知道结局 ≠ 唯一污染，成熟的“标准解释”往往污染更严重；
- 鲜活叙事材料 ≠ 决策信息集能够被可靠重建。

本表是在两轮分类压力测试后形成的工作版，适合开始第三轮测试，但暂不视为最终定稿。

---

## 1. 本项目中的层级：先把“案例”这个词拆开

后续检索必须先区分四个层次，否则非常容易把人物、事件、书和案例混在一起。

| 层级 | 名称 | 定义 | 示例式表达 |
|---|---|---|---|
| L0 | **Case Field / 案例矿区** | 一个值得继续开采的宽领域，通常跨度很大 | “某企业的数字化转型”“某人物的一生”“某次长期外交危机” |
| L1 | **Case Episode / 案例段** | 围绕一个持续问题、边界较清楚的一段历史过程 | “危机发生后一周内的应对过程” |
| L2 | **Decision Atom / 决策原子** | D类最小编码、准入与评分单位 | “在T窗口内，A究竟是否应批准/退出/授权/谈判……” |
| L3 | **Case Packet / 案例包** | 为阅读模拟人工制作的产品，而不是历史本体 | Background + Evidence + Freeze + Task + Reveal + Debrief |

另外还有完全独立的一棵“材料树”：书、论文、档案、日记、书信、会议记录等均属于 **Sources**，不属于上述案例层级。一个来源可以支持多个Atom；一个Atom也通常需要多个来源。

因此数据库逻辑上至少应区分：

> **Cases（历史决策情境） × Sources（材料） × Case–Source Relationship（材料在该案例中的角色）**

来源角色沿用四类：

- **B — Background**：只负责提供冻结点以前的制度、环境、人物关系和背景；
- **P — Protagonist / Evidence**：用于恢复当事人的信息、判断、选项和约束；
- **N — Narrative**：提供连续叙事与代入感；
- **R — Reveal / Review**：用于冻结点之后的结果揭示、长期后果和史学复盘。

---

# 2. Decision Atom 的正式定义

一个合格的 Decision Atom 应能够被写成下面一句标准句：

> **在〔真实决策窗口〕，〔视角主体〕面对〔一个核心决策问题〕；基于其当时可获得的〔信息集〕，至少存在〔A/B……〕两个现实可行方案，而选择将影响〔主要利害〕。**

如果一个候选情境无法稳定写成这句话，首先应怀疑：它可能仍然只是人物、主题、事件或案例矿区，而不是一个决策原子。

### 2.1 一个Atom应尽量保持四个“不变”

在同一Atom内部，下列四项应大体稳定：

1. **主问题不变**：从“是否进入”变成“是否退出”，应考虑拆分；
2. **核心主体不变**：决策权从创始人转到董事会，应考虑拆分；
3. **信息环境不发生质变**：关键情报到达后，可能已进入新Atom；
4. **可行方案集合不发生质变**：某方案因时间关闭、或新方案突然出现时，可能已形成新Atom。

这四条不是机械规则。若过度切碎会破坏连续反馈，应升一级组织成 Case Episode，并采用连续冻结（serial freeze）。

---

# 3. 字段分级：哪些必须填，哪些只在需要时填

为避免v1过度设计，字段分为四种：

| 等级 | 含义 |
|---|---|
| **H — Hard / 硬字段** | 缺失或无法通过时，不能进入D核心库；应继续研究、拆分，或转入L/W |
| **C — Core / 核心字段** | 合格Atom原则上都应填写，但个别历史材料可以明确记为“未知/不可重建” |
| **M — Module / 专属模块** | 仅对某些决策类型启用，如D5长期合作、N规范性困境 |
| **S — Score / 评分字段** | 不决定“是不是真案例”，用于决定是否值得优先投入阅读和研究成本 |

下面的字段表按实际筛选顺序排列，而不是按抽象理论排列。

---

# 4. A组：身份与案例边界

| ID | 字段 | 等级 | 记录要求 |
|---|---|---:|---|
| A01 | **Atom ID** | C | 稳定唯一编号；不要使用人物名作为唯一标识 |
| A02 | **Case Field** | C | 所属案例矿区，便于把同一人物/事件中的多个Atom组织起来 |
| A03 | **Case Episode** | C | 若属于连续过程，注明所属案例段；独立单点可为空 |
| A04 | **Atom Title** | C | 用“主体 + 时间 + 决策问题”命名，避免用结果命名 |
| A05 | **Core Decision Question** | **H** | 只能有一个主要问题；应能用“此刻我究竟要决定什么？”表达 |
| A06 | **Primary Decision Type** | C | D1—D7之一；N规范性困境在满足条件时可作为主类型 |
| A07 | **Secondary Tags** | C | 其他决策原型、危机、弱势等只做辅助标签，不与主类竞争 |
| A08 | **Simulation Mode** | C | 对Decision Atom固定为D；若更适合L/W，应在准入流程中分流 |

### 4.1 D类核心决策原型 v1

| 代码 | 名称 | 判断对象 | 核心问题 |
|---|---|---|---|
| **D1** | 路径选择与身份绑定 | 自己未来进入的轨道 | 我要进入哪条长期路径？ |
| **D2** | 高风险承诺与机会窗口 | 风险暴露程度 | 现在值得重仓吗？押多少？ |
| **D3** | 持续投入、转向与退出 | 已经投入的项目/事业 | 这件事还值得继续吗？ |
| **D4** | 识人、授权与制衡 | 代理人及其权限 | 这个人怎么用、给多少权？ |
| **D5** | 合作、承诺与关系变质 | 自主双方的持续关系 | 这段合作还能否维持、如何维持？ |
| **D6** | 对抗、谈判与让步边界 | 一场具体利益冲突 | 争什么、让什么、何时升级？ |
| **D7** | 角色退出、身份脱钩与权力交接 | 自身的位置 | 事情可以继续，但还应由我继续吗？ |
| **N** | 价值冲突、角色义务与底线选择 | 目标/义务本身 | 两种真实义务无法兼得时，我愿牺牲什么？ |

N与D1—D7不同：它既可以作为主案例，也可以是附着于任何D类型的横向规范性标签。

---

# 5. B组：真实决策窗口与Freeze

这一组是D类最重要的防伪字段。

## 5.1 三个概念必须分开

- **Historical Event Node / 历史事件节点**：签约、开战、辞职、宣布政策等后人常用日期；
- **Decision Window / 真实决策窗口**：多个方案仍然实际开放的一段时间；
- **Freeze Point / 冻结点**：案例制作者为模拟而选择停止提供后续信息的具体截面。

著名事件节点不能自动被当作Freeze。

## 5.2 正式字段

| ID | 字段 | 等级 | 记录要求 |
|---|---|---:|---|
| B01 | **Window Start** | **H** | 当事人已意识到问题，且至少两个方案开始真实开放 |
| B02 | **Window End** | **H** | 由于承诺、行动或外部变化，其他主要方案开始实质关闭 |
| B03 | **Freeze Point** | **H** | 应处于窗口内，通常靠近但尚未越过主要承诺阈值 |
| B04 | **Commitment Threshold** | **H** | 哪一步之后逆转成本发生数量级上升：公开承诺、资金投入、调兵、签约、通知盟友等 |
| B05 | **Decision-Point Validity** | **H** | 冻结时如果主体改主意，历史路径是否仍有现实改变可能？若否，Freeze无效 |
| B06 | **Temporal Form** | C | S=单冻结；C=连续冻结；T=轨迹型。Decision Atom通常S；Episode可组织多个C |
| B07 | **No-action Status** | C | “不作为/维持现状”若作为方案，需证明当事人意识到问题且有真实行动窗口 |

### 5.3 五个硬检验

一个真实决策窗口至少要通过：

1. **Agency Test / 能动性**：主体的选择能否实质影响后续？
2. **Open Options Test / 开放选项**：是否真实存在两个以上现实方案？
3. **Information Boundary Test / 信息边界**：能否部分重建他当时知道、相信和不知道什么？
4. **Unresolvedness Test / 未决性**：Freeze时主要选择是否仍未实质锁死？
5. **Evidence Test / 证据**：问题、目标、约束与选项是否由史料约束，而非作者脑补？

需要区分三层：

> **真实存在的选择 ≠ 史料可重建的选择 ≠ 适合做模拟的选择。**

第一层不成立，不能称D案例；第二层太弱，通常转入L/W；第三层较弱时可保留为低优先级D候选。

---

# 6. C组：决策主体拓扑

重大历史选择常常不是“一个伟大人物单独决定”，也不能把国家、企业、家庭天然拟人化。主体字段的目标，是同时约束**权力边界、信息边界和责任边界**。

| ID | 字段 | 等级 | 记录要求 |
|---|---|---:|---|
| C01 | **Focal Actor / 视角主体** | **H** | Case Packet主要代入谁；信息集必须以此主体为边界 |
| C02 | **Formal Authority / 正式权力主体** | C | 制度上谁有权批准、否决或签字 |
| C03 | **Effective Decider(s) / 实际决策主体** | C | 谁实际上能改变方向；可与正式权力主体不同 |
| C04 | **Accountability / 责任归属** | C | 谁承担主要政治、法律、职业或个人后果 |
| C05 | **Decision Group / 决策共同体** | C | 参与形成方案和判断的核心成员；不要把内部异议压成一个声音 |
| C06 | **Veto / Constraint Holders** | C | 谁不能主动决定，但能否决、阻断或显著约束 |
| C07 | **Implementers** | C | 谁拥有足够执行自主性，使“怎么执行”可能形成第二Atom |
| C08 | **Action Locus / 行动权位置** | **H** | Direct / Recommend / Negotiate / Veto-Consent / Implement，可多选 |
| C09 | **Deciders** | C | 真正拥有该层决策权的人或群体 |
| C10 | **Affected Parties** | C | 承受重大后果但未必有同等决策权的人；家庭/组织案例尤其重要 |
| C11 | **Preference Heterogeneity** | C | 决策共同体内部目标差异：Low / Medium / High |
| C12 | **Focal Perspective Mode** | C | Single / Paired；D5及部分D6可采用顺序双视角 |

### 6.1 关于 Action Locus

中层行动者经常没有Direct权力，但仍有真实决策：

- **Recommend**：决定如何建议、反对、劝说、上报；
- **Negotiate**：在授权范围内决定如何代表组织交换条件；
- **Veto/Consent**：自己不能决定方向，但同意不可缺；
- **Implement**：上层路线已定，仍决定执行方式、节奏和解释空间。

这类Atom不能被错误改写成“如果你是国家/公司最高领导，你怎么办”。

### 6.2 Paired Focal Perspective

D5以及部分D6允许使用配对双视角，但不是把双方情报一次性合并成上帝视角。正确形式是：

> A视角Freeze → A作答 → B视角Freeze → B作答 → Joint Reveal

这样才能同时保留信息不对称与关系互动。

---

# 7. D组：当时信息集

这一组决定案例是否真的关闭上帝视角。

| ID | 字段 | 等级 | 记录要求 |
|---|---|---:|---|
| D01 | **Known Facts** | **H** | 截至Freeze，视角主体已知且可合理视为事实的信息 |
| D02 | **Beliefs / Assessments** | C | 主体的判断、概率估计、世界模型；不能与事实混写 |
| D03 | **Known Unknowns** | C | 主体明确知道自己不知道什么 |
| D04 | **False / Misleading Information** | C | 当时相信、后来证明错误的信息；这是历史事实，不能因为后知而删除 |
| D05 | **Unavailable Information** | C | 后来很重要、但Freeze时没有证据表明主体能够知道的信息 |
| D06 | **Information Sources** | C | 信息来自谁、什么渠道、可靠性如何 |
| D07 | **Information Asymmetry** | C | 其他关键主体掌握哪些Focal Actor没有的信息 |
| D08 | **Reconstructability Level** | **H** | 对主体信息集的可重建程度；若低到只能靠心理脑补，不进入D核心库 |

### 7.1 一个关键规则

Case Packet可以充分提供T以前的背景，但不得因为某条信息后来证明关键，就在Freeze前异常突出它。否则即使没有泄露结果，也已经通过“注意力分配”泄露答案。

---

# 8. E组：选项集合与可行性

| ID | 字段 | 等级 | 记录要求 |
|---|---|---:|---|
| E01 | **Perceived Option Set** | **H** | 当事人实际感知或有强证据表明处于考虑范围的方案 |
| E02 | **Option Evidence Grade** | **H** | A=明确被考虑；B=强证据推定；C=后世可想象。C不得与A/B等权进入Freeze |
| E03 | **Feasibility Constraints** | **H** | 权限、资源、制度、时间、技术等是否允许方案真实执行 |
| E04 | **Status Quo / Inaction Option** | C | 若“不行动”是选择，需验证它不是后人虚构 |
| E05 | **Reversibility** | C | 各方案可逆性：高/中/低；与承诺阈值呼应 |
| E06 | **Later-Reconstructed Options** | C | 后人认为“其实还可以……”的方案，原则上放到Reveal而非Freeze |

优先让读者基于信息自行形成方案；若必须列选项，不应把“正确答案”写得明显更精细，从而制造选择题式泄题。

---

# 9. F组：目标、利害与约束

| ID | 字段 | 等级 | 记录要求 |
|---|---|---:|---|
| F01 | **Stated Goals** | **H** | 主体当时明确追求什么 |
| F02 | **Inferred Goals** | C | 只能由行为和结构推定的目标，必须与明示目标分开 |
| F03 | **Primary Stakes** | **H** | 失败/成功会实质影响什么：生命、权力、现金、关系、声誉、主力、合法性等 |
| F04 | **Hard Constraints** | C | 主体不能轻易改变的制度、资源、物理和时间限制 |
| F05 | **Soft Constraints** | C | 声誉、习惯、身份、组织文化、政治压力等可变但代价高的限制 |
| F06 | **Downside Capacity** | C | 主体实际能承受多大损失；D2尤其重要 |
| F07 | **Option Value / Future Freedom** | C | 某方案会保留还是封闭未来行动空间；D1/D2/D3尤其重要 |

---

# 10. G组：情境坐标

这些不是主分类，不应与D1—D7竞争；它们描述“同一种决策在什么环境下发生”。

| ID | 字段 | 等级 | 推荐值 |
|---|---|---:|---|
| G01 | **Relative Position / 相对位置** | C | Weak / Balanced / Strong |
| G02 | **Time Pressure / 时间压力** | C | Normal / Compressed / Acute Crisis |
| G03 | **Environmental Change / 环境变化** | C | Stable / Gradual / Structural Discontinuity |
| G04 | **Feedback Regime / 反馈状态** | C | Negative / Mixed / Positive / Unclear；用于识别失败惯性或成功惯性 |
| G05 | **Decision Unit Scale** | C | Individual / Dyad / Family / Team / Organization / Polity |
| G06 | **Actor Role / 社会角色** | C | 不强制高/中/低三分；记录实际身份，如官员、商人、农户、军官、家长、技术人员等 |

v1暂不继续细分“社会位置资本”，避免为了少数困难样本把体系过度复杂化。正式权力、行动权位置、资源约束和角色身份合起来，已能表达大多数差异。

---

# 11. H组：证据结构与材料后见性

| ID | 字段 | 等级 | 记录要求 |
|---|---|---:|---|
| H01 | **Primary Contemporary Evidence** | **H** | 同时代日记、书信、会议记录、报告、档案等支持哪些关键字段 |
| H02 | **Corroboration** | C | 是否有独立来源互证，尤其用于动机、选项和关系判断 |
| H03 | **Retrospective Evidence** | C | 自传、晚年回忆、战后调查、官方修史等必须单独标记 |
| H04 | **Source Hindsight Level** | C | P0=主要同时代；P1=同时代+后见互证；P2=主要依赖事后回忆；P3=严重依赖后世重构 |
| H05 | **Evidence Gaps** | C | 哪些关键字段无法可靠重建；不得用流畅叙事掩盖 |
| H06 | **Source Role Links** | C | 每条材料标记B/P/N/R角色 |

### 11.1 重要提醒

“最鲜活的一手声音”不等于“最关键决策者的决策证据”。家庭史、组织史尤其容易出现：日记写得最好的人并不是实际决策者。

---

# 12. I组：叙事污染与盲模拟可用性

必须区分：

- **Outcome Familiarity / 结果熟悉度**：读者知道后来发生什么；
- **Narrative Contamination / 叙事污染**：读者或材料已经预装“这件事应该如何理解”。

后者通常比前者更危险。

## 12.1 污染类型

| 代码 | 类型 | 典型表现 |
|---|---|---|
| **O** | Outcome leakage | 已知道谁赢、谁败、谁背叛 |
| **C** | Causal preloading | 已被告知“真正原因” |
| **M** | Moral/personality labeling | 英雄、奸雄、懦弱、昏庸、保守、冒进 |
| **T** | Teleology | 把后来结果写成一开始就注定 |
| **R** | Retrospective reconstruction | 后来的当事人/机构重新解释当时自己 |

## 12.2 正式字段

| ID | 字段 | 等级 | 记录要求 |
|---|---|---:|---|
| I01 | **Outcome Familiarity** | S | Low / Medium / High |
| I02 | **Narrative Contamination Level** | S | N0低污染；N1可控；N2高污染；N3高度神话化/标签化 |
| I03 | **Contamination Types** | C | O/C/M/T/R，可多选 |
| I04 | **Reader Contamination** | C | 教科书、影视、成语、管理寓言等读者预存解释 |
| I05 | **Source Contamination** | C | 回忆录、官方修史、胜利者叙述等材料污染 |
| I06 | **Packet Contamination Risk** | C | 案例制作者是否通过措辞、选材、排布、选项设计泄题 |
| I07 | **Blind-Simulation Suitability** | S | 适合盲模拟 / 适合半盲模拟 / 更适合复盘 |

### 12.3 Case Packet 去污染六条硬性编辑规则

1. Freeze之前不出现T之后的结果信息；
2. 尽量使用T时点可用的称谓、问题框架与知识；
3. 避免“英明、保守、冒进、昏庸、注定”等带答案的评价词；
4. 后来回忆材料必须显式标注其时间身份；
5. 不因某信息后来重要，就在Freeze前人为加粗或过度突出；
6. Reveal不等于“正确答案揭晓”：要区分实际选择、结果、偶然性、可控因素和史家不同解释。

N3并非“坏历史”，只是通常不适合作为第一梯队盲模拟，可转为复盘型案例。

---

# 13. J组：D5“长期合作关系”专属模块

仅在D5或关系历史对决策构成核心影响时启用，不进入全局必填字段。

| ID | 字段 | 等级 | 记录要求 |
|---|---|---:|---|
| J01 | **Relationship History** | M | 合作如何建立、经历过哪些关键共同事件 |
| J02 | **Trust Stock** | M | 历史履约、失约、互相救援、伤害与修复 |
| J03 | **Mutual Dependence** | M | 双方各自依赖对方什么，依赖是否对称 |
| J04 | **Exit Costs** | M | 分手对双方分别意味着什么 |
| J05 | **Outside Options** | M | 是否存在现实替代伙伴、市场、政治盟友等 |
| J06 | **Commitment Structure** | M | 股权、婚姻、盟约、合同、声誉、共同资产等如何锁定双方 |
| J07 | **Signal Ambiguity** | M | 异常行为究竟可能是暂时摩擦、策略动作还是关系实质变质 |

D5最佳案例通常不是“A相信B，B后来背叛”，而是双方利益与权力结构逐渐变化，并可能出现“双方都认为自己先被背叛”的互动反馈。

---

# 14. K组：N“真正价值困境”专属模块

只有当价值冲突本身是主要决策对象，或构成重要横向维度时启用。

| ID | 字段 | 等级 | 记录要求 |
|---|---|---:|---|
| K01 | **Recognized Obligations** | M | 当事人本人认真承认哪些价值、角色和义务，而非后世替他附加 |
| K02 | **Conflict Structure** | M | 哪些义务无法同时满足 |
| K03 | **Normative Open-Conflict Test** | **M-H** | Freeze时至少两项义务是否仍对本人有真实约束，且优先级尚未解决？若否，不宜做N盲决策模拟 |
| K04 | **Moral Cost Bearers** | M | 坚持某项原则时，代价由谁承担，不能只记录当事人的自我牺牲 |
| K05 | **Identity Stakes** | M | 选择会如何影响“我认为自己是谁” |
| K06 | **Non-negotiables vs Preferences** | M | 哪些是真底线，哪些可能只是面子、声誉或群体压力 |
| K07 | **Moral Remainder** | M | 作出选择后是否仍保留不可消除的亏欠、遗憾或责任 |

一个“英雄行为”发生的日期不一定是好的N型Freeze。应尽量往前追到价值冲突仍真正未决的窗口。

---

# 15. L组：准入硬门槛

一个候选Atom进入 **D核心库** 前，至少通过以下七项。这里宁可严格分流，也不要为了丰富案例数量而降低标准。

| Gate | 硬门槛 | 失败后的处理 |
|---|---|---|
| GATE-1 | **案例已切成明确Atom**：不是人物/主题/书/整段兴衰史 | 继续切片 |
| GATE-2 | **真实选择存在**：至少两个当时现实可行方案 | 若只是遭遇，转L/W |
| GATE-3 | **真实窗口存在**：Freeze位于选择尚未实质关闭之时 | 重新寻找更早窗口；找不到则退出D |
| GATE-4 | **主体边界明确**：知道在代入谁、他实际能决定什么 | 重新划分主体或拆Atom |
| GATE-5 | **信息集可部分重建**：不是靠小说化心理补足 | 证据不足则降级D或转L/W |
| GATE-6 | **选项由史料约束**：后人构造的C级方案不能冒充当时选项 | 修正选项集合 |
| GATE-7 | **核心问题单一到足够有用**：内部若问题/主体/信息/选项发生质变 | 拆成多个Atom或上收Episode |

N型主案例另加：

> **GATE-N：Normative Open-Conflict Test必须通过。**

---

# 16. M组：软评分字段 v1

硬门槛判断“它是不是一个可靠D案例”；软评分判断“它值不值得优先做”。建议统一0—5分，但v1阶段先不机械加权。

| ID | 评分项 | 5分意味着什么 |
|---|---|---|
| M01 | **Information Reconstructability** | 能较精确恢复视角主体在Freeze时的信息世界 |
| M02 | **Evidence Transparency** | 关键结论可追溯到同时代材料，推断边界清楚 |
| M03 | **Decision Tension** | 多个方案在当时确实都合理，没有显而易见答案 |
| M04 | **Multi-perspective Potential** | 可通过独立材料恢复不同参与者的不同世界 |
| M05 | **Consequence Traceability** | 决策后果可追踪到足够长，并能区分短长期 |
| M06 | **Life Transfer Value** | 可迁移到现实人生，而非只依赖极特殊技术细节 |
| M07 | **Immersion Potential** | 利益、恐惧、关系、约束具体，容易进入驾驶舱 |
| M08 | **Background Efficiency** | 所需背景可压缩；较少前置阅读即可建立足够真实环境 |
| M09 | **Blind-Simulation Value** | 结局和标准解释陌生，适合真正闭卷式判断 |
| M10 | **Sample Novelty** | 相比现有案例，增加了新的角色、结构、结果或机制 |

### 16.1 暂不设总分

v1不建议直接将十项求和排序，因为存在两类不可简单互换的价值：

- 一个史料极强但高度著名的案例，可能Blind-Simulation低，却很适合深度复盘；
- 一个结局极陌生的案例，若信息集无法重建，也不能因为“新鲜”而排到前面。

先保留向量评分，等样本量足够后再观察是否需要分轨加权。

---

# 17. Decision Atom v1：最小录入卡

正式研究前，不要一开始填写全部字段。候选阶段先用下面的“最小录入卡”快速过滤，能显著降低检索成本。

```yaml
atom_id: ""
case_field: ""
episode: ""
title: ""

core_question: ""            # 此刻真正要决定什么？
primary_type: "D1-D7 | N"

focal_actor: ""
action_locus: []              # Direct / Recommend / Negotiate / Veto-Consent / Implement
formal_authority: ""
effective_deciders: []
affected_parties: []

window_start: ""
window_end: ""
freeze_point: ""
commitment_threshold: ""
decision_point_valid: true

known_information_summary: ""
information_reconstructability: "high | medium | low"

perceived_options:
  - option: ""
    evidence_grade: "A | B | C"
    feasible_at_freeze: true
  - option: ""
    evidence_grade: "A | B | C"
    feasible_at_freeze: true

primary_stakes: []
constraints: []

relative_position: "weak | balanced | strong"
time_pressure: "normal | compressed | acute"
environment_change: "stable | gradual | structural"

outcome_familiarity: "low | medium | high"
narrative_contamination: "N0 | N1 | N2 | N3"
source_hindsight: "P0 | P1 | P2 | P3"

hard_gate_status: "candidate | qualified | rejected | divert-to-L/W"
unresolved_questions: []
```

候选通过后，再展开完整主体拓扑、信息集、D5/N专属模块和十项软评分。

---

# 18. 完整研究记录模板

完整Atom建议按以下顺序写，而不是按史书时间线写：

1. **Atom Standard Sentence**：一句话确认谁、何时、问题、信息、选项、利害；
2. **Why this is an Atom**：为什么不是人物/事件/案例矿区；
3. **Subject Topology**：主体、权限、共同体、否决者、执行者、受影响者；
4. **Decision Window**：窗口起止、Freeze、承诺阈值；
5. **Information Boundary**：已知、判断、未知、错误信息、不可得信息；
6. **Option Set**：A/B/C级选项与可行性；
7. **Goals / Stakes / Constraints**；
8. **Context Coordinates**；
9. **Evidence Map**：每项判断由什么材料支持；
10. **Contamination Audit**；
11. **Special Module**：D5或N等；
12. **Hard-gate Decision**；
13. **Soft Scores**；
14. **Packet Design Notes**：若入选，怎样制作Freeze和Reveal。

---

# 19. Case Packet 与数据库记录必须分离

这是v1中一个容易被忽略的设计原则。

**研究数据库应尽量完整；实际给读者的Case Packet则应刻意不完整。**

数据库可以知道：

- 后来谁赢了；
- 对方实际掌握什么信息；
- 哪个情报是错的；
- 哪种解释后来成为主流；
- 哪些结果具有偶然性。

但Freeze前的Packet不能把这些全部给读者。

因此同一Atom至少存在两种信息视图：

### Research View

研究者全局视图，用于验证真实性、选项、史料和后果。

### Simulation View

视角主体在Freeze时可获得的信息视图，用于关闭上帝视角。

二者混写，是此项目最应避免的结构性错误之一。

---

# 20. v1明确暂不解决的事项

为了避免不断增加字段，以下问题暂不升级为全局结构：

1. **Contingency Activation / 备用方案启动**：已在普通家庭案例中出现，但样本还不够，不新增D8；
2. **社会位置的精细资本分层**：暂不把政治、经济、文化资本拆成独立轴；先依靠主体拓扑、角色和约束表达；
3. **D5关系状态的统一量化**：保留为专属模块，不对所有Atom强制；
4. **评分加权与总分**：待更多真实样本后再决定；
5. **最佳Case Packet长度与阅读节奏**：属于后续原型试读阶段；
6. **L/W正式字段表**：本版只解决Decision Atom，不能把D结构强行套到人生历程与生活世界材料上。

---

# 21. 与D/L/W总体路线的关系

本表只针对D轨。

- **D — Decision**：最小单位是 **Decision Atom**，必须有真实开放的决策窗口；
- **L — Life-course**：更适合使用 **Life Arc / 人生弧段**，不必强行寻找Freeze；
- **W — World**：更适合使用 **Situated World Slice / 情境化生活截面**，目标是进入一种生活世界，而不是做一道决策题。

一个人物或一本书可以同时是L/W的优质材料，并作为多个D Atom的“案例矿区”。不要因为D可操作性强，就把所有历史人生材料都改造成选择题。

---

# 22. 下一轮压力测试的使用方式

第三轮不应再“讨论完案例以后补字段”，而应严格反过来：

1. 先用最小录入卡编码；
2. 过七个硬门槛；
3. 只有通过后才展开完整字段；
4. 观察哪些字段经常无法填写、从不起作用或频繁重复；
5. 只有多个异质样本重复暴露同一缺陷，才修改v1。

也就是说，从这一版开始应提高“新增字段”的门槛，防止每遇到一个特殊案例就让体系膨胀。

---

# 23. 当前最重要的设计原则

可以把前两轮压力测试的成果压缩成九条：

1. **案例先于书**：先确定Decision Atom，再反推材料；
2. **决策对象决定主分类**：不是按人物身份或事件主题分类；
3. **真实决策窗口先于戏剧性时刻**：著名场面经常已经太晚；
4. **Freeze必须位于承诺阈值之前**；
5. **主体边界必须与信息边界一致**：不能让一个人拥有组织全体的知识；
6. **选项必须受史料约束**：后人想到的“妙计”不能偷偷进入当时选项集；
7. **结果与解释都可能污染模拟**：去污染不仅是“不要剧透”；
8. **Research View与Simulation View必须分离**；
9. **D不是全部**：无法形成高质量决策Atom的优质材料，应自然流向L/W，而不是被判为“低质量历史”。

---

## 与既有历史阅读框架的关系

本项目可视为既有宏观历史阅读路线的第二条轨道：

- [世界史阅读框架：25×6矩阵、双轨阅读与中文书目](./2026-09-10-world-history-reading-framework.md)：主要解决“世界如何运行”的地图问题；
- [中国史阅读框架：20×6矩阵与双轨书单](./2026-09-10-china-history-reading-framework.md)：主要解决中国史的结构与主线；
- **本Decision Atom体系**：主要解决“人在当时看不清未来时如何选择”的驾驶问题。

理想状态不是二选一，而是：

> **先用宏观史建立地图，再用微观案例进入驾驶舱；先在迷雾里做人，再走出迷雾复盘。**

---

## Revision log

- **2026-09-14 — v1**：在两轮分类压力测试基础上，首次整理为可操作的Decision Atom字段体系；吸收真实决策窗口、承诺阈值、主体拓扑、Action Locus、Deciders/Affected Parties、Paired Focal Perspective、叙事污染、D5关系模块与N规范性未决检验；暂不增加新的决策原型。
