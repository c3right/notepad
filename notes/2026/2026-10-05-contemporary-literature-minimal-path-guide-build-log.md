---
title: "阅读当代文学的最短经典路径：执行指南构建进展"
date: 2026-10-05
updated: 2026-10-05
status: working
type: research-note
topics:
  - contemporary-literature
  - reading-path
  - reading-guides
  - literary-criticism
keywords:
  - execution-guide
  - canonical-materials
  - reading-cards
  - A-B-C
  - Bridge-after-destination
source: "ChatGPT conversation | existing research notes"
language: zh-CN
---

# 阅读当代文学的最短经典路径：执行指南构建进展

## 一句话结论

Round 1–8 的开放式“找什么导读 / 解读材料”研究已完成。下一阶段不再横向扩张作品、理论或论文，而把累计研究结果收敛为：

> **普通读者可以直接照着执行的作品阅读 + A/B/C辅助材料指南。**

本文件从 2026-10-05 起持续记录这一“研究成果 → 用户执行指南”的构建过程。后续每完成一个 Step，都继续追加到本文件，不另建平行进展稿。

---

## 0. 当前基线与边界

### Authoritative sources

执行指南只从下列已完成成果中抽取、校准和组装，不重新设计“读什么”：

1. [导读与解读资料指南——研究设计与累积记录](./2026-10-05-contemporary-literature-minimal-path-guides-research.md)
   - 当前已完成 Round 1–8；
   - 包含 A/B/C 分层、时间预算、Rule A–AU、舞台实践校准、淘汰理由与 v0.10 变更日志；
   - 是“辅助材料研究”的主基线。

2. [基础包与升级包 v1.0](./2026-10-04-contemporary-literature-minimal-path-final-packages.md)
   - 是“读什么”的 authoritative package；
   - 不在执行指南阶段重新开放作品选择。

3. [作品路线与分叉地图推进记录](./2026-10-04-contemporary-literature-minimal-path-research-log.md)
   - 保存作品路线形成过程、Core / Branch / Later 等取舍依据；
   - 只在解释路线职责或发生冲突时回查。

4. [外国作品中文译本推荐 v1.0](./2026-10-04-contemporary-literature-foreign-translations-v1.md)
   - 负责译本、出版社、ISBN 与购买可行性；
   - 执行指南不重复重新研究译本，除非后续 QA 发现硬错误。

### 当前已冻结的方法原则

执行指南必须继承而不能静默回退的核心规则包括：

- **A/B/C 分层**
  - A = spoiler-light 阅读前最小背景；
  - B = 阅读后核心辅助；
  - C = 可选深入。
- **ROI first**：默认每部作品只保留真正改变阅读质量的最小材料。
- **Bridge-after-destination**：跨作品谱系桥梁原则上在第二端作品读完后再出现。
- **中文优先但不降质**：中文材料能等价覆盖职责时优先；不能时保留精准英文小范围。
- **戏剧必须同时检查文本职责与舞台实践职责**。
- **后续修订覆盖前版结论**：例如 Round 7 v0.9 优先于 v0.8 的被修订部分。
- **C层必须真正可选**：不能在文案上写“可选”，实际又让默认路线无法闭合。

### 本阶段明确不做

- 不新增文学史“必读经典”；
- 不开启 Round 9；
- 不为了填满时间预算而增加论文；
- 不把研究日志重新誊写成另一份长篇文献综述；
- 不重新争论译本，除非发现书目硬错误；
- 不把每个作品都强行配齐中文材料；
- 不在最终指南里保留研究过程中的所有淘汰候选。

---

# 1. 总体构建方案

整个“research log → execution guide”阶段分为 **5个 Step**。

| Step | 状态 | 核心任务 | 主要产出 |
|---|---|---|---|
| **1. Research → Canonical Data** | **COMPLETED** | 从Round 1–8抽取每个作品当前唯一有效结论，消解初版/修订版冲突，统一字段 | Canonical Materials Master Table |
| **2. 去重与跨节点整合** | **COMPLETED** | 处理共享材料、Bridge-after-destination、中文替代、B/C边界与重复职责 | 精简后的最终材料网络 |
| **3. 单作品执行卡** | **PENDING** | 把每个作品压成普通读者能直接照着执行的一张卡 | 全部作品 Reading Companion Cards |
| **4. 路线级组装** | **PENDING** | 组装基础包、升级包、桥梁出现时点、checkpoint与总预算 | 完整可执行路线 |
| **5. 对抗性验收与发布** | **PENDING** | 书目、教学、ROI、偏科与可执行性QA；冻结正式版本 | 最终指南 + 速查表 |

状态约定：

- PENDING：尚未开始；
- IN PROGRESS：正在处理；
- COMPLETED：该Step已完成并通过本阶段自检；
- 若后续QA推翻先前结论，不静默覆盖，在对应Step下新增 Revision 记录。

---

# 2. Step 1 — Research → Canonical Data

## 目标

把目前超过万行的累计研究文件，转换成：

> **“八轮研究结束后，每个作品到底最终选了什么”的唯一有效数据层。**

这一阶段本质是研究成果的数据清洗，而不是再次做文学研究。

## 任务范围

对所有基础节点、微节点和升级节点逐项抽取以下字段：

1. **作品 / 阅读单元**
2. **package身份**
   - Kernel；
   - 微节点；
   - Upgrade。
3. **路线职责**
4. **裸读最容易漏掉什么**
5. **A层**
   - 是否需要；
   - 材料；
   - 精确范围；
   - 时间；
   - 作用。
6. **B层**
   - B1 / B2；
   - 作者；
   - 标题；
   - 出处；
   - 年份；
   - 页码 / 章节；
   - DOI / ISBN / 稳定链接；
   - 时间；
   - 具体解决哪项职责。
7. **中文替代**
   - 等价替代；
   - 低门槛但信息较少；
   - 仅补充、不能替代。
8. **C层**
   - 材料；
   - 只在什么兴趣 / 问题下值得进入。
9. **默认辅助成本**
10. **Bridge**
    - 与前后哪个作品建立；
    - 在何时出现。
11. **最终职责卡修订**
12. **来源版本**
    - 例如：R7 v0.9覆盖R7 v0.8的哪些字段。

## 关键规则

### 2.1 只保留“当前有效值”

研究日志中的旧判断不会删除，但Canonical Data只保存：

> **当前应该给用户看的最终有效结论。**

例如：

- Round 7 v0.8：《哈姆雷特》“不建议预读”；
- Round 7 v0.9：改为Folger舞台物理微A层。

Canonical Data只记录：

> **有5–7分钟微A层。**

旧结论继续留在research log作为研究史。

### 2.2 不在这一步做文案美化

Step 1追求：

- 准确；
- 结构一致；
- 可检查；
- 可去重。

不追求：

- 好看；
- 简洁；
- 面向普通读者的最终措辞。

### 2.3 不重新搜索材料

原则上只回查已有研究结果。

只有出现以下情况才允许补查：

- 同一材料的作者 / 页码 / DOI 在不同Round记录冲突；
- 后续修订只写了结论却没有完整书目信息；
- 明显存在无法直接执行的缺字段。

这类补查属于：

> **bibliographic repair**

而不是重新打开候选池。

## Step 1完成标准

完成后必须能回答：

> 对任一作品，不再翻Round日志，也能唯一确定应该先读什么、后读什么、哪些材料只是可选、总共花多久。

### Step 1预期产出

> **Canonical Materials Master Table v1**

它将成为 Step 2–5 的唯一上游数据源。

---

# 3. Step 2 — 去重与跨节点整合

## 目标

把逐作品的Canonical Data进一步变成：

> **没有重复劳动、桥梁出现时机正确、默认路线真正最短的材料网络。**

## 任务范围

### 3.1 共享材料去重

检查：

- 同一篇论文是否被多个作品重复要求；
- 一篇谱系材料是否应该提升为shared B；
- 同一文学史职责是否可以一次解决。

已知典型类型包括：

- Chekhov → Hemingway → Carver共享谱系；
- 某些作家长短篇 / 基础—升级节点共享材料；
- 戏剧production史是否能跨作品承担相同背景职责。

### 3.2 Bridge-after-destination统一

逐条检查桥梁，例如：

- Faulkner → García Márquez；
- 《聊斋》→ 莫言；
- García Márquez / Faulkner → 莫言；
- 《安提戈涅》→《岛》。

每条Bridge必须明确：

- 前端作品；
- 后端作品；
- **何时出现**；
- 是否默认必读；
- 是否只给已读前端者。

### 3.3 中文替代分级

最终统一成三档：

- **A类：等价替代**
- **B类：低门槛替代，职责覆盖略窄**
- **C类：补充，不可替代核心**

避免research log里“替代 / 补充 / 中文低门槛材料”标准略有差异。

### 3.4 B/C边界压力测试

检查每一份C：

> 如果删除它，默认路线是否仍然闭合？

若否，它其实不是C，必须重新分类。

反过来，若B只提供很小增量，也应考虑降级。

### 3.5 时间预算重算

按去重后的实际阅读次数重新计算：

- 单作品成本；
- 单Round成本；
- 基础包；
- 升级包；
- 全路线。

不能简单把各卡时间相加，因为shared materials可能只读一次。

## Step 2完成标准

最终应该出现一张：

> **Final Materials Dependency Graph**

明确：

- 哪份材料属于单作；
- 哪份材料跨作品共享；
- 哪条桥梁什么时候触发；
- 哪些材料二选一而不是累加。

---

# 4. Step 3 — 单作品执行卡

## 目标

把研究人员使用的数据层转换成：

> **普通读者拿起来就能操作的阅读伴随卡。**

## 统一模板

### 作品名

**这一站为什么读**

1–2句说明路线职责。

**第一次裸读重点**

3–5个观察点，只告诉“看哪里”，尽量不提前告诉结论。

**阅读前**

二选一：

> 不建议预读，直接读作品。

或：

> 先读A：材料 + 精确范围 + 时间。

**读完马上读**

B1 / B2：

- 材料；
- 精确范围；
- 时间；
- 它具体帮你看见什么。

**中文替代**

只有存在真正合格替代时出现。

**先别急着读**

列最容易把路线拖厚或提前污染首读的材料类型。

**想深入再读**

C层，说明适用兴趣，而不是制造完成焦虑。

**这一站结束后应获得的能力**

一句迁移性结论。

**辅助成本**

只给默认路线。

## Step 3核心编辑原则

- 不把“裸读误区”写成考试标准答案；
- A层必须spoiler-light；
- B层解释“为什么读”，不写成长篇论文摘要；
- C层必须显著弱化视觉权重；
- 每张卡只保留会影响实际行动的信息。

## Step 3完成标准

随机抽任何一张作品卡，用户都无需再打开research log，就知道：

> **现在读什么 → 读到哪里 → 为什么读 → 要花多久 → 什么可以不读。**

---

# 5. Step 4 — 路线级组装

## 目标

把单卡重新装配为：

> **可以从第一页一路执行到底的完整课程 / 阅读路径。**

## 任务范围

### 5.1 基础包路线

提供最短主路径：

> 作品正文 + 必要A + 默认B。

并明确：

- 顺序；
- 微节点；
- shared materials；
- checkpoint；
- 累计辅助时间。

### 5.2 升级包插入规则

升级作品不全部堆到基础包结束后。

要按研究所得谱系判断：

- 哪些应紧邻基础节点；
- 哪些适合稍后回收；
- 哪些是真正独立扩展。

### 5.3 Bridge插入

把Step 2形成的Bridge真正放进路线。

### 5.4 Checkpoint设计

每个较大谱系结束后增加一个极短回顾，例如：

> 这三个节点之间，“现实”究竟发生了什么变化？

Checkpoint不增加新材料，只帮助把作品重新连接成骨架。

### 5.5 多种执行模式

至少形成：

1. **基础最短版**
2. **基础 + 升级版**
3. **兴趣分支版**

兴趣分支可包括：

- realism / modernism；
- narrative self-reflexivity；
- SF / speculative fiction；
- postcolonial / historical memory；
- Chinese modernity；
- drama / performance。

## Step 4完成标准

用户可以根据自己的时间与兴趣，选择一条模式后：

> **不再需要自己重新规划顺序。**

---

# 6. Step 5 — 对抗性验收与发布

## 目标

在冻结正式指南前，主动攻击整个成品。

### 6.1 Bibliographic QA

逐项核：

- 作者；
- 标题；
- 出处；
- 版本；
- 年份；
- 页码；
- DOI；
- ISBN；
- 稳定链接。

### 6.2 Pedagogical QA

逐卡检查：

- A层是否真的值得预读；
- 是否泄露首读体验；
- B层是否普通读者可完成；
- 英文难度是否被低估；
- 是否出现“名义可选、实际必读”的C层。

### 6.3 ROI QA

攻击：

> 有没有20–40分钟材料只贡献一句可以被更短材料完成的信息？

若有：

- 缩范围；
- 找已有短替代；
- 或降C。

不因为材料“经典”而保留。

### 6.4 Adversarial QA

至少从以下方向攻击：

- 是否过度现代主义中心；
- 是否西方中心；
- 中文文学是否被西方谱系解释吞掉；
- 类型文学是否被“纯文学化”；
- 戏剧是否偷偷重新按小说文本处理；
- postcolonial是否被压成主题；
- 理论术语是否重新替代具体机制；
- “伟大作家发明X”的单一起源神话是否死灰复燃。

### 6.5 发布层

QA通过后，冻结：

**正式完整版**

> 《阅读当代文学的最短经典路径：导读与解读资料指南 v1.0》

**速查版**

只保留：

- 阅读顺序；
- A/B材料；
- 范围；
- 时间；
- Bridge；
- 升级节点。

---

# 7. 阶段间依赖关系

Round 1–8 Research Log  
↓  
Step 1 Canonical Data  
↓  
Step 2 Dedup / Bridge / Dependency  
↓  
Step 3 Reading Companion Cards  
↓  
Step 4 Route Assembly  
↓  
Step 5 QA + Release  
↓  
Final Guide v1.0

原则上：

> **不要跨过上一步直接做下一步。**

原因：

- Step 1没清干净版本冲突，Step 3就会把旧结论写进卡片；
- Step 2没去重，Step 4的时间预算会虚高；
- Step 3没验证单卡可执行性，Step 4只会成为漂亮但难用的大纲；
- Step 5之前不能把任何中间稿称为正式v1.0。

---

# 8. 当前进度

截至 2026-10-05：

- Round 1–8导读 / 解读材料开放研究：**COMPLETED**
- Round 7深化复核v0.9：**COMPLETED**
- Round 8及v0.10：**COMPLETED**
- 执行指南总体构建方案：**RECORDED**
- Step 1：**COMPLETED**
- Step 2：**COMPLETED**
- Step 3：**PENDING**
- Step 4：**PENDING**
- Step 5：**PENDING**

下一实际动作：

> **Step 3 — 单作品执行卡：把Canonical Data与Dependency Graph压成可直接照着读的Reading Companion Cards。**

---



# 10. Step 1 — Canonical Materials Master Table v1

**状态：COMPLETED**

## 10.1 Step 1 的实际方法

Step 1没有重新打开候选池，而是把既有Round 1–8研究当作版本化数据源，完成四件事：

1. 以“基础包与升级包 v1.0”锁定作品全集与package身份；
2. 逐Round抽取当前有效的职责、裸读警戒、A/B/C、时间与Bridge；
3. 对后续修订执行“新版本覆盖旧字段、研究史不删除”；
4. 对少量缺失稳定入口做bibliographic repair，但不重新评选材料。

为了让Step 2能够真正去重，本次没有把完整书目反复塞进48行，而采用两层结构：

- **Node Master Index**：48个路线节点，只保存当前有效教学数据与Material ID；
- **Material Registry**：每份材料只登记一次，节点通过ID引用。

因此：

> Canonical Data是“唯一有效值层”，research log仍是“为什么得到这些值”的证据层。

---

## 10.2 覆盖审计

### 路线节点

| 类别 | 数量 | 说明 |
|---|---:|---|
| 基础包 B01–B33 | **33** | 与final-packages v1.0编号一一对应 |
| 升级包 U01–U15 | **15** | 与final-packages v1.0升级编号一一对应 |
| **总路线节点** | **48** | 全部已有canonical record |
| Shared / Bridge依赖 | 不计作品节点 | 单列，不制造“第49部作品” |

组合阅读单元继续保持组合，不为了表格整齐强行拆散：

- Chekhov《苦恼》+《带小狗的女人》；
- Borges固定四篇；
- Poe两篇；
- Carver两篇；
- 《聊斋》两篇；
- 鲁迅两篇；
- 《党费》+《百合花》；
- 余华《现实一种》+《活着》。

其中余华双节点虽然在package里是一个编号，但内部保留两份不同B，因为两篇承担不同阶段职责。

### 版本覆盖

- Round 1–6：分别以v0.2–v0.7完成态为有效值；
- Round 7：**v0.9覆盖v0.8发生修订的字段**，其余v0.8继续有效；
- Round 8：以v0.10为有效值；
- final-packages v1.0仍唯一决定“读什么”，guide research只决定“怎么配辅助材料”。

---

## 10.3 Node Master Index — 基础包 B01–B33

### A. 外国小说 B01–B14

| ID | 阅读单元 | Round | 最终职责 / 裸读警戒 | A | B | 替代 / C | 默认辅助成本 | Bridge / 版本 |
|---|---|---:|---|---|---|---|---:|---|
| **B01** | 巴尔扎克《夏倍上校》 | R1 | 社会不是背景而是法律、财产、婚姻、政权构成的制度系统；避免只读“弃夫悲剧” | — | R1-B01 | C：— | **10–15m** | Balzac→Flaubert由B02材料顺带建立；v0.2 |
| **B02** | 福楼拜《一颗简单的心》 | R1 | 叙述距离、细节选择、作者退场、同情/反讽暧昧；不把free indirect discourse当该篇唯一标准答案 | — | R1-B03 | C：R1-C01 | **10–15m** | R1-B03兼作Balzac→Flaubert桥；v0.2 |
| **B03** | Chekhov《苦恼》+《带小狗的女人》 | R1 | 弱事件、失败交流、心理转折、开放结局；“没情节”不是解释 | — | R1-B05 | 中文替代/补充：R1-ALT02 | **12–15m** | 完成B03→B12→B13后读R1-S01；v0.2 |
| **B04** | Woolf《达洛维夫人》 | R2 | 私人记忆、公共钟表时间、城市刺激与多意识之间的叙述路由；意识流≠心理描写 | — | R2-B01 | C：R2-C01 | **15–20m** | 后续B23、U13有Bridge-after-destination；v0.3 |
| **B05** | Kafka《变形记》 | R2 | 不可能事件与日常秩序并存；训练抵抗“虫=X”的唯一寓意钥匙 | — | R2-B02 | C：R2-C02 | **10–15m** | —；v0.3 |
| **B06** | Borges固定四篇 | R2 | 文本、作者、目录、分类和解释系统拥有world-making power；不是四个“脑洞概念” | — | R2-B03 | C：R2-C03 | **30–40m** | 四篇共用一份B；v0.3 |
| **B07** | Achebe《瓦解》 | R3 | 叙述世界的权限转换；Igbo语言/口述传统重构英语；不把前半当殖民到来前的背景铺垫 | — | R3-B01 | C：R3-C01 | **18–22m** | 若读U09，二者读完后追加R3-S01；v0.4 |
| **B08** | García Márquez《百年孤独》 | R3 | plural realities、不同truth/experience与历史记忆；magical realism≠现实+魔法 | — | R3-B02 | C：R3-C03 | **20–25m** | 已读U10者此时才读R2-S02；与U12可选R3-S02；v0.4 |
| **B09** | Morrison《宠儿》 | R3 | archive absence + literary archaeology + rememory + trauma time；幽灵不是可消解的“奇幻元素” | — | R3-B04 + R3-B05 | C：R3-C05 | **33–40m** | 两份B职责不同；v0.4 |
| **B10** | Ishiguro《别让我走》 | R4 | SF premise埋入realism/memoir/Bildungsroman，制度被normalization；“其实不是SF”是误读 | **禁止预解释SF设定** | R4-B08 + R4-B09 | C：R4-C04 | **25–32m** | spoiler-sensitive；v0.5 |
| **B11** | Poe《莫格街凶杀案》+《泄密的心》 | R4 | rational reconstruction vs unreliable confession，两种相反reader protocol；不做“唯一发明者”神话 | — | R4-B01 + R4-B02 | C：R4-C01 | **11–15m** | 奠基/crystallization措辞；v0.5 |
| **B12** | Hemingway《白象似的群山》 | R1 | 省略、对白、空间和重复制造权力/犹豫；省略≠寻找唯一隐藏答案 | **强烈不预读隐藏议题** | R1-B06 | — | **8–10m** | B03→B12→B13后读R1-S01；v0.2 |
| **B13** | Carver《你们为什么不跳个舞？》+《大教堂》 | R1 | 早期压缩→晚期再开放，防止Carver=固定minimalism | — | R1-B07 | 可选作者校准：R1-ALT03 | **10–12m** | B03→B12→B13后读R1-S01；v0.2 |
| **B14** | Le Guin《离开奥梅拉斯的人》 | R4 | psychomyth + compressed thought experiment + reader co-construction；不等于微缩world-building或功利主义投票题 | — | R4-B04 + R4-B05 | — | **10–15m** | 与U03明确区分thought experiment / world-building；v0.5 |

### B. 中文小说 B15–B24

| ID | 阅读单元 | Round | 最终职责 / 裸读警戒 | A | B | 替代 / C | 默认辅助成本 | Bridge / 版本 |
|---|---|---:|---|---|---|---|---:|---|
| **B15** | 《聊斋》：《促织》+《婴宁》 | R5 | 志怪—传奇资源、“异”强化现实、欲望/秩序；禁止proto-magical realism | — | R5-B01 + R5-B02 + R5-B03 | C：R5-C01 | **16–23m** | 读完B20才启动《聊斋》→莫言桥；v0.6 |
| **B16** | 鲁迅《狂人日记》+《阿Q正传》 | R5 | 语言/主体/社会批判同时发生的现代断裂；两种现代主体失败；翻译是构成性机制 | — | R5-B04 + R5-B05 | C：R5-C02 + R5-C03 | **20–27m** | —；v0.6 |
| **B17** | 张爱玲《倾城之恋》 | R5 | 物质细节承担interiority与有限agency；战争不自动使普通人升华 | — | R5-B07 + R5-B08 | — | **20–27m** | —；v0.6 |
| **B18** | 王愿坚《党费》+茹志鹃《百合花》 | R6 | 同一革命历史/伦理场中的两种文学中介：典型—见证—共同体 vs 日常—细节—抒情 | — | R6-B01 + R6-B02 | C：R6-C01 | **16–20m** | 不把《党费》扩张为整个十七年文学；v0.7 |
| **B19** | 余华《现实一种》+《活着》 | R6 | 从“虚伪形式/怀疑常识真实”到叙述权重新分配；不是先锋失败后退回现实主义 | — | 《现实一种》R6-B04；《活着》R6-B05 | 作者短校准R6-ALT01；C：R6-C03 + R6-C04 | **28–35m** | 双作品内部对照必须保留；v0.7 |
| **B20** | 莫言《红高粱》原始中篇 | R6 | 民间/家族/身体取得历史叙述权；外国影响是重新发现故乡的装置 | — | R6-B07 + R6-B08 | — | **16–20m** | R6-B08同时启动《聊斋》+Márquez/Faulkner→莫言桥；v0.7 |
| **B21** | 刘慈欣《流浪地球》 | R4 | engineering premise→epic scale→quasi-history→collective/civilization perspective；SF≠预测准确度 | — | R4-B10 + R4-B11 | — | **18–25m** | 不用电影替代小说；v0.5 |
| **B22** | 施蛰存《梅雨之夕》 | R5 | 都市基础设施、匿名交往与外来心理资源共同制造心理现代性；不等于“Freud案例” | — | R5-B06 | — | **12–15m** | —；v0.6 |
| **B23** | 白先勇《游园惊梦》 | R5 | Woolf技术 + 昆曲/《牡丹亭》/《红楼梦》+1949流亡记忆的重新组合 | — | R5-B09 | — | **15–20m** | 正式执行B04→B23 Bridge-after-destination；v0.6 |
| **B24** | 马原《冈底斯的诱惑》 | R6 | 1980年代“形式取得思想自主权”的历史节点；核心不是再次教学metafiction | — | R6-B03 | C：R6-C02 | **6–8m** | —；v0.7 |

### C. 戏剧 B25–B33

| ID | 阅读单元 | Round | 最终职责 / 裸读警戒 | A | B | 替代 / C | 默认辅助成本 | Bridge / 版本 |
|---|---|---:|---|---|---|---|---:|---|
| **B25** | Sophocles《安提戈涅》 | R7 | public conflict + civic institution + chorus as collective body；不压成“个人良知反国家” | R7-A01 + R7-A02 | R7-B01 | C：R7-C01 + R7-C02 | **35–42m** | v0.9覆盖v0.8 A层；后续B31再回看 |
| **B26** | Shakespeare《哈姆雷特》 | R7 | interiority as actor–character–audience relation；theatre作为truth-testing apparatus；不说“发明独白” | R7-A03 | R7-B02 + R7-B03 | C：R7-C03 | **28–37m** | v0.9新增微A并修正书目归属 |
| **B27** | Ibsen《玩偶之家》 | R7 | bourgeois interior as material social machine；创新是re-functioning，不是发明box set/fourth wall | — | R7-B04 | 可选短校准R7-ALT01；C：R7-C04 | **25–30m** | Ibsen→Chekhov共享比较；v0.9 |
| **B28** | Chekhov《樱桃园》 | R7 | weak overt action + ensemble + duration/subtext as performance variables + tragic/comic openness | — | R7-B05 + R7-B06 | 中文替代R7-ALT02；C：R7-C05 + R7-C06 | **25–30m** | Chekhov/Stanislavski=productive mismatch；v0.9 |
| **B29** | Brecht《母亲勇气和她的孩子们》 | R8 | historicized social causality + Gestus + spectator invited to judge；间离≠禁止情感 | — | R8-B01 + R8-B02 | production note R8-N01；C：R8-C01 | **27–33m** | audience response not guaranteed；v0.10 |
| **B30** | Beckett《等待戈多》 | R8 | duration as action + repetition-with-difference + body/prop choreography；荒诞标签不等于机制 | — | R8-B03 + R8-B04 | 中文补充R8-ALT01；C：R8-C02 | **35–42m** | stage directions/pause/silence按正文处理；v0.10 |
| **B31** | Fugard/Kani/Ntshona《岛》 | R8 | coerced body→rehearsing body→performing body；joint devising、double audience、embedded Antigone | R8-A01 | R8-B05 + R8-B06 | C：R8-C03 + R8-C04 | **29–38m** | 读完本剧才回看B25；作者必须三人共同记录；v0.10 |
| **B32** | Churchill《Cloud Nine》 | R8 | casting as embodied syntax + 100-year history/25-year aging + workshop-informed writing | — | R8-B07 + R8-B08 | production note R8-N02；C：R8-C05 | **25–33m** | workshop≠joint devising；v0.10 |
| **B33** | Pirandello《六个寻找作者的剧中人》 | R7 | theatre apparatus本身成为戏剧材料；actor/character/director/rehearsal/lighting/audience separation | — | R7-B07 + R7-B08 | C：R7-C07 | **18–22m** | v0.9补Worthen作者并把Lorch精确到首演章 |

---

## 10.4 Node Master Index — 升级包 U01–U15

| ID | 阅读单元 | Round | 最终职责 / 裸读警戒 | A | B | 替代 / C | 默认辅助成本 | Bridge / 版本 |
|---|---|---:|---|---|---|---|---:|---|
| **U01** | 巴尔扎克《高老头》 | R1 | 从制度缩影升级为巴黎社会网络、空间和上升路径；避免只读“不孝女/金钱腐蚀” | R1-A01 | R1-B02 | — | **30–43m** | 前置B01；v0.2 |
| **U02** | 福楼拜《包法利夫人》 | R1 | 长篇展开叙述距离、视角与free indirect style，现实主义→现代主义形式桥 | 已读B02则不再A | R1-B04 | 极短替代R1-ALT01；C：R1-C02 | **25–30m** | 前置B02；v0.2 |
| **U03** | Le Guin《黑暗的左手》 | R4 | anthropological world-building + observer revision；不缩成gender thought experiment | — | R4-B06 + R4-B07 | C：R4-C03 | **15–22m** | 与B14区分“压缩变量/系统扩散”；v0.5 |
| **U04** | 白先勇《台北人》全本 | R5 | 从单篇扩展为迁台群体的多主体历史/记忆世界；modernism作为历史主体性 | — | R5-B10 | — | **20–25m** | 前置B23；v0.6 |
| **U05** | 莫言《红高粱家族》全本 | R6 | 让原中篇生命神话进入更多矛盾，成为1980年代多话语“混杂现场” | — | R6-B09 | C：R6-C05 | **18–22m** | 前置B20；v0.7 |
| **U06** | 刘慈欣《三体》第一部 | R4 | scientific epistemology + Cultural Revolution + long-form cosmic unknown；禁止后两部后见污染 | — | R4-B12 + R4-B13 | 后两部理论全部deferred | **20–27m** | series-internal Bridge-after-destination；v0.5 |
| **U07** | Dostoevsky《地下室手记》 | R2 | 自相矛盾主体、想象听众与自由问题；说话形式不断拆毁理论 | — | R2-B04 | — | **20–25m** | 不进入完整Bakhtin；v0.3 |
| **U08** | Mary Shelley《弗兰肯斯坦》 | R4 | Gothic × experimental-science边界祖先；creation之后的responsibility | — | R4-B03 | C：R4-C02 | **25–30m** | 不写“唯一第一本科幻小说”；v0.5 |
| **U09** | Conrad《黑暗的心》 | R3 | anti-imperial insight与imperial/racial implication并存；现代主义叙述含混 | — | R3-B03 + R3-S01 | C：R3-C02 | **28–35m** | 必须已读B07；Achebe批评后置；v0.4 |
| **U10** | Faulkner《我弥留之际》 | R2 | 多重有限视角，让读者在冲突证词间拼世界；不是“15个叙述者所以难” | R2-A01 | R2-B05 | Bridge R2-S02后置 | **18–25m** | 读完B08才启动Faulkner→Latin America；v0.3 |
| **U11** | Vonnegut《五号屠场》 | R2 | trauma + metafiction + SF作为积极形式资源；不能用“创伤幻觉”消解科幻 | — | R2-B06 + R2-B07 | — | **35–45m** | 超级节点允许两份不同职责B；v0.3 |
| **U12** | Rushdie《午夜之子》 | R3 | personal memory + national history + narrator error + metafictional mediation；不是“印度版百年孤独” | R3-A01 | R3-B06 | C/Bridge：R3-S02 | **21–28m** | 与B08都读完才可选世界文学桥；v0.4 |
| **U13** | McEwan《赎罪》 | R2 | realism/modernism/metafiction重新服务强故事，并转化为叙事伦理 | — | R2-B08 | 中文替代R2-ALT01；C/Bridge：R2-C04 | **25–30m** | 严禁预讲后部结构；v0.3 |
| **U14** | 西西《我城》 | R5 | city as protagonist + everyday local-making + fluid locality；与流亡怀旧现代性区分 | — | R5-B11 | C：R5-C04 | **12–15m** | —；v0.6 |
| **U15** | Soyinka《死亡与国王的侍从》 | R8 | Yoruba ritual-performance grammar + transition + music/dance/acoustic narrative；殖民干预是catalyst而非唯一钥匙 | R8-A02 | R8-B09 + R8-B10 | 中文替代R8-ALT02；C：R8-C06 + R8-C07 | **39–49m** | Greek comparison必须后置；v0.10 |

---

## 10.5 Material Registry v1

说明：

- 这里只登记research log已经选中的材料，不重新增加候选；
- “route range”是执行指南真正要求读的范围，不一定等于全文；
- 未确认的出版元数据明确标为 QA，不推测；
- 语言 / 难度沿用research log判断；
- stable URL在Step 1定点修复到的，直接补入。

### Round 1

- **R1-B01 | B | Cathy Caruth, “The Claims of the Dead: History, Haunted Property, and the Law.”** Critical Inquiry 28.2 (2002), 419–441；route range **419–425**；DOI https://doi.org/10.1086/449047；10–15m；EN/中高。
- **R1-A01 | A | David Bellos, “Introduction,” Balzac: Old Goriot.** Cambridge UP, 1987 / online 2012, **pp.1–4**；DOI https://doi.org/10.1017/CBO9781139086790.003；5–8m；EN/低中。
- **R1-B02 | B | Peter Brooks, “Balzac Invents the Nineteenth Century.”** Realist Vision, Yale UP, 2008, **pp.21–39**；DOI https://doi.org/10.12987/9780300127850-003；25–35m；EN/中。
- **R1-B03 | B | James Wood，《小说机杼》“福楼拜和现代叙述”。** 黄远帆译，河南大学出版社，2015，ISBN 9787564919771，**pp.27–32**；10–15m；ZH/低中；公开节选 https://www.chinawriter.com.cn/n1/2019/1012/c404091-31395928.html 。
- **R1-C01 | C | 刘文瑾，《福楼拜的反讽与神圣——〈一颗简单的心〉中的“虚己”诗学》。** 《外国文学》2026(1), 51–63；DOI https://doi.org/10.16345/j.cnki.cn11-1562/i.2026.01.004；20–25m；ZH/中。
- **R1-B04 | B | Peter Brooks, “Flaubert and the Scandal of Realism.”** Realist Vision, Yale UP, 2008, **pp.54–70**；DOI https://doi.org/10.12987/9780300127850-005；25–30m；EN/中。
- **R1-ALT01 | B替代 | Mario Vargas Llosa / John King, “Flaubert, our contemporary.”** The Cambridge Companion to Flaubert, **pp.220–224**；DOI https://doi.org/10.1017/CCOL0521815517.014；约10m；EN。
- **R1-C02 | C | Dominick LaCapra, “Narrative Practice and Free Indirect Style.”** Madame Bovary on Trial, Cornell UP, **pp.126–149**；DOI https://doi.org/10.7591/9781501720017-007；40–50m；EN/高。
- **R1-B05 | B | James N. Loehlin, The Cambridge Introduction to Chekhov.** Cambridge UP, 2010；route range：《苦恼》**46–48**，《带小狗的女人》**99–102**；DOI全书 https://doi.org/10.1017/CBO9780511781278；12–15m；EN/中。
- **R1-ALT02 | 中文替代/补充 | 熊宗慧，《契诃夫的爱情与反叛》。** 现收入《带小狗的女士》，贵州人民出版社，2024，丘光译，ISBN 9787221176639，约**177–184**；仅覆盖《带小狗的女人》。
- **R1-B06 | B | Martin Scofield, “Ernest Hemingway.”** The Cambridge Introduction to the American Short Story, Cambridge UP, 2006；route range **139–140, 146–147**；DOI https://doi.org/10.1017/CBO9780511607257.014；8–10m；EN/中。
- **R1-B07 | B | Martin Scofield, “Raymond Carver.”** 同书Chapter 22；route range **226–230**；DOI https://doi.org/10.1017/CBO9780511607257.022；10–12m；EN/中。
- **R1-ALT03 | 可选作者校准 | 《雷蒙德·卡佛：保持简短》访谈。** 中国作家网；只读谈《大教堂》段；约5m；ZH；https://www.chinawriter.com.cn/n1/2021/0803/c404091-32180221.html 。
- **R1-S01 | Shared B | Daniel Just, “Varieties of Nothing: Understatement and Anticlimax in Chekhov, Hemingway, and Carver.”** Modern Philology 121.4 (2024), **425–446**；DOI https://doi.org/10.1086/729858；35–45m；EN/中高；必须在B03+B12+B13全部完成后读。

### Round 2

- **R2-B01 | B | Elaine Showalter，《对意识与现代性的探索：《达洛维夫人》的导读》。** British Library中文站；route range：开头至“小说构想”结束；15–20m；ZH/低中；稳定页 https://www.britishlibrary.cn/zh-cn/articles/introduction-to-mrs-dalloway/ 。
- **R2-C01 | C | Michael Whitworth, “Virginia Woolf and Modernism.”** The Cambridge Companion to Virginia Woolf, Cambridge UP, 2000, **146–163**；DOI https://doi.org/10.1017/CCOL0521623936.008；30–35m；EN/中高。
- **R2-B02 | B | 范捷平，《床上百无聊赖中想到的〈变形记〉》。** 原收《德国文学散论》，南京大学出版社；route range：讨论文类/寓言/多重解释至结尾；10–15m；ZH/低中；稳定转载 https://www.sinobook.com.cn/comment/newsdetail.cfm?iCntno=22010 ；**年份/页码待Step 5 QA**。
- **R2-C02 | C | Vivian Liska, “The Beetle and the Butterfly: Nabokov’s Lecture on Kafka’s The Metamorphosis.”** Kafka after Kafka, 2019, **143–154**；DOI https://doi.org/10.1017/9781787444201.009；20–25m；EN/中高。
- **R2-B03 | B | Steven Boldy, “Fictions Part I: The Garden of Forking Paths (1941).”** A Companion to Jorge Luis Borges, 2009, **71–104**；只按四个固定篇目小标题跳读；DOI https://doi.org/10.1017/9781846157059.007；30–40m；EN/中。
- **R2-C03 | C | Efraín Kristal, “Jorge Luis Borges’s Fictions and the Two World Wars.”** Jorge Luis Borges in Context, Cambridge UP, 2020, **35–42**；DOI https://doi.org/10.1017/9781108635981.006；12–15m；EN/中。
- **R2-B04 | B | Deborah Martinsen, “Freedom and Polyphony: Notes from Underground.”** Fyodor Dostoevsky: A Very Short Introduction, OUP, 2024, Chapter 3, **from p.45**；DOI https://doi.org/10.1093/actrade/9780198864332.003.0003；20–25m；EN/中。
- **R2-A01/R2-B05 | A+B同源 | Robert W. Hamblin, As I Lay Dying: The Oprah Book Club Lectures.** Center for Faulkner Studies, Southeast Missouri State University；A只读“Viewpoint”第一小段3–5m；B读“Stream of Consciousness”“Viewpoint”“The Problem of Language”15–20m；EN/低中；**稳定入口待Step 5 QA**。
- **R2-S02 | 条件Bridge | Emron Esplin, “Faulkner and Latin America; Latin America in Faulkner.”** William Faulkner in Context, Cambridge UP, 2015, **270–278**；DOI https://doi.org/10.1017/CBO9781107279438.037；15–20m；EN/中；在U10+B08之后。
- **R2-B06 | B1 | 田俊武，《“时空旅行”、解构“时空旅行”与创伤叙事的互文性建构——论库尔特·冯尼古特的〈五号屠场〉》。** 《外国文学》2017(1), **117–124,159**；15–20m；ZH/中。
- **R2-B07 | B2 | Amanda Wicks, “‘All This Happened, More or Less’: The Science Fiction of Trauma in Slaughterhouse-Five.”** Critique 55.3 (2014), **329–340**；DOI https://doi.org/10.1080/00111619.2013.783786；20–25m；EN/中。
- **R2-B08 | B | Judith Seaboyer, “Realist Legacies.”** The Cambridge Companion to Ian McEwan, Cambridge UP, 2019, **150–164**；DOI https://doi.org/10.1017/9781108648516.011；25–30m；EN/中。
- **R2-ALT01 | 中文替代 | 付昌玲，《论〈赎罪〉的叙事诗学建构》。** 《东岳论丛》2021, 42(5), **106–112,192**；DOI https://doi.org/10.15981/j.cnki.dongyueluncong.2021.05.011；12–15m；ZH/中；覆盖文学史职责较窄。
- **R2-C04 | C/Bridge | Thom Dancer, “Limited Modernism.”** The Cambridge Companion to Ian McEwan, **165–180**；DOI https://doi.org/10.1017/9781108648516.012；25–30m；EN/中高；U13读完后可回看B04。

### Round 3

- **R3-B01 | B | Chinua Achebe, “The African Writer and the English Language.”** Things Fall Apart: A Casebook, OUP, 2003, **55–66**；DOI https://doi.org/10.1093/oso/9780195147636.003.0002；18–22m；EN/中。
- **R3-C01 | C | Jarica Linn Watts, “‘He does not understand our customs’: Narrating orality and empire in Chinua Achebe’s Things Fall Apart.”** Journal of Postcolonial Writing 46.1 (2010), **65–75**；DOI https://doi.org/10.1080/17449850903478189；18–22m；EN/中高。
- **R3-B03 | B | Pericles Lewis, “Heart of Darkness.”** Yale Modernism Lab；8–10m；EN/低中；https://campuspress.yale.edu/modernismlab/heart-of-darkness/ 。
- **R3-S01 | Shared B | Chinua Achebe, “An Image of Africa: Racism in Conrad’s Heart of Darkness.”** Massachusetts Review 18.4 (1977), **782–794**；JSTOR https://www.jstor.org/stable/25088813 ；20–25m；EN/中；B07+U09都读完后。
- **R3-C02 | C | Ian Watt, “Conrad’s Heart of Darkness and the critics.”** Essays on Conrad, Cambridge UP, 2000, **85–96**；DOI https://doi.org/10.1017/CBO9780511485343.005；18–22m；EN/中。
- **R3-B02 | B | Steven Boldy, “One Hundred Years of Solitude by Gabriel García Márquez.”** The Cambridge Companion to the Latin American Novel, Cambridge UP, 2005, **258–269**；DOI https://doi.org/10.1017/CCOL0521825334.015；20–25m；EN/中。
- **R3-C03 | C | Michael Wood, “Invisible Ink.”** Gabriel García Márquez: One Hundred Years of Solitude, Cambridge UP, 1990, **56–75**；DOI https://doi.org/10.1017/CBO9780511620492.007；30–35m；EN/中。
- **R3-A01 | A | Marina MacKay, “Salman Rushdie, Midnight’s Children (1981).”** The Cambridge Introduction to the Novel, Cambridge UP, 2010, **172–175**；DOI https://doi.org/10.1017/CBO9780511781544.021；6–8m；EN/低中。
- **R3-B06 | B | 李胜伟，《〈午夜之子〉中的历史真相：对后现代自恋叙事的一种解读》。** 《北京第二外国语学院学报》2016, 38(6), **104–114**；15–20m；ZH/中；https://journal.bisu.edu.cn/CN/Y2016/V38/I6/104 。
- **R3-S02 | 可选共享Bridge | Michael Bell, “García Márquez, magical realism and world literature.”** The Cambridge Companion to Gabriel García Márquez, 2010, **179–195**；DOI https://doi.org/10.1017/CCOL9780521867498.013；25–30m；EN/中高；B08+U12之后。
- **R3-B04 | B1 | Toni Morrison, “The Site of Memory.”** Inventing the Truth, 2nd ed., Houghton Mifflin, 1995, full 83–102；route range **90–93**；8–10m；EN/中。
- **R3-B05 | B2 | Claudine Raynaud, “Beloved or the shifting shapes of memory.”** The Cambridge Companion to Toni Morrison, Cambridge UP, 2007, **43–58**；DOI https://doi.org/10.1017/CCOL052186111X.004；25–30m；EN/中。
- **R3-C05 | C | Jean Wyatt, “Dislocating the Reader: Slave Motherhood and The Disrupted Temporality of Trauma in Toni Morrison’s Beloved.”** The Cambridge Companion to Literature and Psychoanalysis, Cambridge UP, 2021, **90–106**；DOI https://doi.org/10.1017/9781108763691.007；30–35m；EN/高。

### Round 4

- **R4-B01 | B1 | Peter Thoms, “Poe’s Dupin and the power of detection.”** The Cambridge Companion to Edgar Allan Poe, 2002, full 133–147；route range章首；DOI https://doi.org/10.1017/CCOL0521793262.009；7–10m；EN/中。
- **R4-B02 | B2 | U.S. National Park Service, “Edgar Allan Poe and His Tales of Horror.”** route range first-person/unreliable narrator/Tell-Tale Heart段；4–5m；EN/低；https://www.nps.gov/articles/poe-horror.htm 。
- **R4-C01 | C | Alistair Rolls, “Moving Fergus Hume’s The Mystery of a Hansom Cab and Breaking the Frame of Poe’s ‘The Murders in the Rue Morgue’.”** Criminal Moves, Liverpool UP, 2019, **45–59**；route range章首起源讨论；10–15m；EN/中。
- **R4-B03 | B | Charlotte Gordon, “Frankenstein.”** Mary Shelley: A Very Short Introduction, OUP, 2022, Chapter 3, **33–52**；DOI https://doi.org/10.1093/actrade/9780198869191.003.0003；25–30m；EN/低中。
- **R4-C02 | C | Jay Clayton, “Frankenstein’s futurity: replicants and robots.”** The Cambridge Companion to Mary Shelley, 2003, **84–100**；DOI https://doi.org/10.1017/CCOL0521809843.006；25–30m；EN/中。
- **R4-B04 | B1 | Ursula K. Le Guin, introductory note to “The Ones Who Walk Away from Omelas.”** The Wind’s Twelve Quarters, 1975, **275–276**；3–5m；EN/低。
- **R4-B05 | B2 | Sarah Wyman, “Reading Through Fictions in Ursula Le Guin’s ‘The Ones Who Walk Away from Omelas’.”** ANQ 25.4 (2012), **228–232**；DOI https://doi.org/10.1080/0895769X.2012.720854；7–10m；EN/中。
- **R4-B06 | B1 | Tom Shippey, “Introduction: Serious Issues, Serious Traumas, Emotional Depth.”** Hard Reading, Liverpool UP, 2016, route range **182–184**；5–7m；EN/中。
- **R4-B07 | B2 | 陈榕，《厄休拉·勒古恩〈黑暗的左手〉中的世界主义》。** 《名作欣赏》2015(14)；route range Ekumen/冷战/沟通部分；10–15m；ZH/低中；https://www.chinasf.com/main/documentdetail.php?DocumentID=2761 。
- **R4-C03 | C | Ursula K. Le Guin, “Is Gender Necessary? Redux.”** Dancing at the Edge of the World, Grove, 1989, **7–16**；15–20m；EN/中。
- **R4-B08 | B1 | Jay Clayton, “Clones and Other Sorrows (Kazuo Ishiguro).”** Literature, Science, and Public Policy, Cambridge UP, 2023, Chapter 9, **182–197**；route range章首至“Time and Sorrow”前；DOI https://doi.org/10.1017/9781009263504.014；18–22m；EN/中。
- **R4-B09 | B2 | Neil Gaiman & Kazuo Ishiguro, “Breaking the Boundaries Between Fantasy and Literary Fiction.”** The New Republic, 7 Jun 2015；route range Never Let Me Go问题至Ishiguro“liberated”段；7–10m；EN/低；**稳定URL待Step 5 QA**。
- **R4-C04 | C | Doug Battersby, “Ishiguro and Genre Fiction.”** The Cambridge Companion to Kazuo Ishiguro, 2023, **138–151**；DOI https://doi.org/10.1017/9781108909525.013；25–30m；EN/中。
- **R4-B10 | B1 | 《〈流浪地球〉作者刘慈欣：科幻作家不可能预测未来》。** 中国作家网，2019；只读“能否预测未来”回答；3–5m；ZH；**稳定URL待Step 5 QA**。
- **R4-B11 | B2 | 杨琼，《科幻文学史诗性的呈现——以〈流浪地球〉为中心》。** 《中国当代文学研究》2019(2), 起始**210**；route range“叙事跨度”“群体与个体叙事”及结论；15–20m；ZH/中；https://www.chinawriter.com.cn/n1/2019/0403/c426230-31012019.html 。
- **R4-B12 | B1 | 王静静，《论刘慈欣〈三体〉中的“文革”叙事》。** 《小说评论》2016(3), **170–175**；12–15m；ZH/中。
- **R4-B13 | B2 | 宋明炜、金雪妮译，《在崇高宇宙与微纪元之间：刘慈欣论》。** 《当代文坛》2021(1), **200–209**；route range开头及“刘慈欣与新浪潮”前段；8–12m；ZH/中；https://www.chinawriter.com.cn/n1/2021/0202/c404080-32019994.html 。

### Round 5

- **R5-B01 | B1 | 《全球研究视域下的〈聊斋志异〉》。** 中国社会科学网 / 《中国社会科学报》，2025；只读“揭示《聊斋志异》中‘异’的精髓”；7–10m；ZH/低；https://www.cssn.cn/skgz/bwyc/202501/t20250103_5830640.shtml 。
- **R5-B02 | B2 | 马振方，《〈聊斋〉如何揭露官场黑暗？》。** 中国文化研究院，2019-12-12；只读《促织》部分；3–5m；ZH；https://chiculture.org.hk/sc/china-five-thousand-years/2733 。
- **R5-B03 | B3 | 陈建华，《评〈异史氏〉｜北美汉学界的“晚明时刻”》。** 《上海书评》/澎湃，2023；route range李惠仪“欲望与秩序”及《婴宁》几段；6–8m；ZH/中；**稳定URL待Step 5 QA**。
- **R5-C01 | C | Wai-yee Li, Enchantment and Disenchantment: Love and Illusion in Chinese Literature.** Princeton UP, 1993；Liaozhai相关“Late Ming Moment”；默认不计时。
- **R5-B04 | B1 | 鲁迅，《〈呐喊〉自序》。** route range“铁屋子”对话至《狂人日记》附近；5–7m；ZH；**公开稳定URL待Step 5 QA**。
- **R5-B05 | B2 | Ann Huss, “The Madman That Was Ah Q: Tradition and Modernity in Lu Xun’s Fiction.”** The Columbia Companion to Modern East Asian Literature, 2003, **385–394**；15–20m；EN/中；JSTOR章节稳定入口 https://www.jstor.org/stable/10.7312/most11314.70 。
- **R5-C02 | C | Xiaobing Tang, “Lu Xun’s ‘Diary of a Madman’ and a Chinese Modernism.”** PMLA 107.5 (1992), **1222–1234**；DOI https://doi.org/10.2307/462876；22–28m；EN/高。
- **R5-C03 | C | 季进, “Literary Translation and Modern Chinese Literature.”** The Oxford Handbook of Modern Chinese Literatures, 2016, **521–530**；DOI https://doi.org/10.1093/oxfordhb/9780199383313.013.26；用于translation-as-constitutive。
- **R5-B06 | B | 王爱松，《施蛰存的三篇小说与现代都市文化空间》。** 原刊《福建论坛（人文社会科学版）》2012(4)；后收《对话性阅读与批评》，广东人民出版社2014, ISBN 9787218092898, **123–130**；12–15m；ZH/低中；南京大学稳定页 https://njucml.nju.edu.cn/59/d3/c22619a350675/page.htm 。
- **R5-B07 | B1 | 张爱玲，《关于〈倾城之恋〉的老实话》。** 初载《海报》1944-12-09；全文5–7m；ZH；澎湃稳定转载 https://www.thepaper.cn/newsDetail_forward_22844075 。
- **R5-B08 | B2 | Keru Cai, “The Proximity Effect: Agency and Isolation in Eileen Chang’s ‘Love in a Fallen City’.”** Concentric 48.1 (2022), **59–84**；route range **59–69**优先；DOI https://doi.org/10.6240/concentric.lit.202203_48(1).0003；15–20m；EN/中。
- **R5-B09 | B | 李奭学，《括号的诗学——从吴尔芙的〈戴洛维夫人〉看白先勇的〈游园惊梦〉》。** 《中国文哲研究集刊》28 (2006), **149–170**；route range **149–153 + 166–168**；15–20m；ZH/中。
- **R5-B10 | B | 山口守，《白先勇小说中的现代主义——〈台北人〉的记忆与乡愁》。** 《台湾文学学报》14 (2009), **1–17**；20–25m；ZH/中。
- **R5-B11 | B | Dorothy Tse Hiu Hung / Natascha Bruce trans., “The Flâneur/Flâneuse and the Multiple ‘I’s of the ‘Local’ in Xi Xi’s I City.”** Chinese Literature Today 8.1 (2019), **50–57**；DOI https://doi.org/10.1080/21514399.2019.1605254；12–15m；EN/中。
- **R5-C04 | C | 謝曉虹，《城市漫遊者及「我－們」的「本土」：重讀西西〈我城〉》。** 《思与言》56.2 (2018), **73–113**；45–60m；ZH。

### Round 6

- **R6-B01 | B1 | 郭帅，《王愿坚的意义》。** 《当代作家评论》2023(4)；route range开头“十七年文学”/短篇位置/史中寻诗与真实来源；8–10m；ZH/低中；**中国作家网稳定URL待Step 5 QA**。
- **R6-B02 | B2 | 茅盾，《谈最近的短篇小说》中论《百合花》部分。** 《人民文学》1958(6)；route range约2000字；8–10m；ZH/低。
- **R6-C01 | C | 吴辰，《茹志鹃的〈百合花〉及其周边》。** 中国作家网 / 《文艺报》，2018；15–20m；ZH。
- **R6-B03 | B | 《有意味的形式：先锋小说与1980年代文学思想转型》。** 中国作家网专题，2025；route range“二、立意在创新：形式即意义”中马原/吴亮部分；6–8m；ZH/低中；**稳定URL待Step 5 QA**。
- **R6-C02 | C | 吴亮，《马原的叙述圈套》。** 《当代作家评论》1987(3), **45–51**；15–18m；ZH/中。
- **R6-B04 | B | 余华，《虚伪的作品》。** 初刊《上海文论》1989(5)；后收《我能否相信自己》，人民日报出版社1999；route range **160–163**；8–10m；ZH/低中。
- **R6-C03 | C | 陈思和《中国当代文学史教程》“残酷与冷漠的人性发掘：《现实一种》”。** 默认不计时；**具体版本/页码待Step 5 QA**。
- **R6-B05 | B | 刘艳，《心理描写的嬗变：由“心理性”人物观到“功能性”人物观的叙事演变——以余华〈活着〉为例》。** 《山东师范大学学报（社会科学版）》2021, 66(5), **39–51**；DOI https://doi.org/10.16456/j.cnki.1001-5973.2021.05.004；20–25m；ZH/中。
- **R6-ALT01 | 可选作者校准 | 余华，《文学、时代和我的写作》访谈。** 中国作家网，2022；只读“是否往后撤退/回归现实主义”问答；3–5m；ZH；**稳定URL待Step 5 QA**。
- **R6-C04 | C | 叶立文，《论余华长篇小说叙事结构的历史演变》。** 《文学评论》2018；25–30m；ZH；**卷期/页码待Step 5 QA**。
- **R6-B07 | B1 | 曹霞，《如何“传统”，怎样“民间”》。** 中国作家网，2016；route range“二、‘民间’的激活：古典‘说书人’”中《红高粱》段；8–10m；ZH/中；**稳定URL待Step 5 QA**。
- **R6-B08 | B2/Bridge | 莫言，《我期盼下一个中国作家得诺贝尔文学奖》访谈相关段落。** 中国作家网，2018；route range《聊斋》/魏晋传奇/Marquez-Faulkner影响三段；8–10m；ZH/低；**稳定URL待Step 5 QA**。
- **R6-B09 | B | 王金胜，《莫言文学与“1980年代”——以〈红高粱家族〉为方法的研讨》。** 《中国现代文学研究丛刊》2020(9), **171–180**；18–22m；ZH/中。
- **R6-C05 | C | 丛新强，《论〈红高粱家族〉的“抗战”“情爱”与“历史观”》。** 默认C；**完整元数据待Step 5 QA**。

### Round 7 — v0.9有效值

- **R7-A01 | A0 | Diane J. Rayor, Introduction to Sophocles’ Antigone: A New Translation.** Cambridge UP, 2011, **xiii–xiv**；3–4m；EN/低。
- **R7-A02 | A1 | Simon Goldhill, “The audience of Athenian tragedy.”** The Cambridge Companion to Greek Tragedy, Cambridge UP, 1997, full 54–68；route range章首约5页；DOI https://doi.org/10.1017/CCOL0521412455.003；v0.9有效预算约7–8m；EN/中。
- **R7-B01 | B | Edith Hall, “The limits of free will: Oedipus the Tyrant and Antigone.”** Sophocles: A Very Short Introduction, OUP, 2025, Chapter 3, **30–51**；DOI https://doi.org/10.1093/actrade/9780192897800.003.0003；25–30m；EN/低中。
- **R7-C01 | C | Rosa Andújar, Playing the Chorus in Greek Tragedy, Ch.4 §4.3.3 “The Reticent Chorus in Sophocles’ Antigone.”** Cambridge UP, 2025, **261–273**；DOI全章 https://doi.org/10.1017/9781009653626.005；20–25m；EN/高。
- **R7-C02 | C | D. M. Carter, “The Political Reception of Greek Tragedy.”** The Politics of Greek Tragedy, 2007/08, **143–160**；DOI https://doi.org/10.5949/liverpool/9781904675501.003.0005；25–30m。
- **R7-A03 | A | Folger Shakespeare Library, “Shakespeare’s Theater: From the Folger Shakespeare Editions.”** route range public playhouse/thrust stage/audience/scenery段；5–7m；EN/低；https://www.folger.edu/explore/shakespeares-works/shakespeares-theater-from-the-folger-shakespeare-editions/ 。
- **R7-B02 | B1 | Michael Neill, “A Modern Perspective: Hamlet.”** Folger Shakespeare Library；route range revenge/interiority/soliloquy/hiddenness/Mousetrap前半；15–20m；EN/中；https://www.folger.edu/explore/shakespeares-works/hamlet/hamlet-a-modern-perspective/ 。
- **R7-B03 | B2 | “Hamlet in performance.”** Cambridge School Shakespeare: Hamlet, Cambridge UP, 2005, **270–275**；原作Shakespeare，版本编者Richard Andrews & Rex Gibson；DOI https://doi.org/10.1017/9780511862892.005；8–10m；EN/低。
- **R7-C03 | C | David Wiles, “Hamlet’s Advice to the Players.”** The Players’ Advice to Hamlet, Cambridge UP, 2020, **10–37**；DOI https://doi.org/10.1017/9781108689502.002；40–50m；EN/高。
- **R7-B04 | B | Nicholas Grene, “A Doll’s House: the drama of the interior.”** Home on the Stage, Cambridge UP, 2014, **14–36**；DOI https://doi.org/10.1017/CBO9781139939607.002；25–30m；EN/中。
- **R7-ALT01 | 可选短校准 | Sally Ledger, “Afterword: Ibsen Now.”** Henrik Ibsen, Liverpool UP, 2008, **65–67**；4–5m。
- **R7-C04 | C | Toril Moi, “First and Foremost a Human Being: Idealism, Theater, and Gender in A Doll’s House.”** Henrik Ibsen and the Birth of Modernism, OUP, 2006, Ch.7, **188–220**；DOI https://doi.org/10.1093/oso/9780199295876.003.0008；ISBN 9780199295876；45–60m；EN/高。
- **R7-B05 | B1 | James N. Loehlin, Introduction to Chekhov: The Cherry Orchard.** Cambridge UP, 2006, **1–8**；10–12m；EN/低中。
- **R7-B06 | B2 | Anatoly Smeliansky, “Chekhov at the Moscow Art Theatre.”** The Cambridge Companion to Chekhov, 2000, **29–40**；DOI https://doi.org/10.1017/CCOL0521581176.003；15–18m；EN/中。
- **R7-ALT02 | 中文低门槛替代B2 | 杨莉莉，《欧陆舞台上的契诃夫》。** 《PAR表演艺术杂志》第17期，1994-03；route range ensemble/listening、Stanislavski分歧、三种《樱桃园》舞台；12–18m；ZH/低中；https://par.npac-ntch.org/cn/article/doc/D99EPH3JCK 。
- **R7-C05 | C | Bella Merlin, “Which Came First: The System or ‘The Seagull’?”** New Theatre Quarterly 15.3 (1999), **218–227**；DOI https://doi.org/10.1017/S0266464X00013014；18–22m；EN/中。
- **R7-C06 | C | Arnold Aronson, “The scenography of Chekhov.”** The Cambridge Companion to Chekhov, **134–148**；DOI https://doi.org/10.1017/CCOL0521581176.012；25–30m；作为强解释而非中性事实。
- **R7-B07 | B1 | Mary Ann Frese Witt, “Metatheatre.”** Pirandello in Context, Cambridge UP, 2024, **163–169**；DOI https://doi.org/10.1017/9781108339391.027；8–10m；EN/中。
- **R7-B08 | B2 | W. B. Worthen, “The Fourth Wall.”** 同书, **170–178**；DOI https://doi.org/10.1017/9781108339391.028；10–12m；EN/中。
- **R7-C07 | C | Jennifer Lorch, “The first production: Teatro Valle, Rome, 9 May 1921, directed by Dario Niccodemi.”** Pirandello: Six Characters in Search of an Author, Cambridge UP, 2005, Ch.2, **31–43**；18–22m；EN/中；v0.9取代旧“Introduction pp.1–14”定位。

### Round 8

- **R8-B01 | B1 | Robert Leach, “Mother Courage and Her Children.”** The Cambridge Companion to Brecht, 2nd ed., Cambridge UP, 2006, **132–142**；DOI https://doi.org/10.1017/CCOL0521857090.009；15–18m；EN/中。
- **R8-B02 | B2 | Katja Frimberger, “‘Cultivating the Art of Living’: The Pleasures of Bertolt Brecht’s Philosophising Theatre Pedagogy.”** Studies in Philosophy and Education 41 (2022), 653–668；route range两个Mother Courage相关小节；DOI https://doi.org/10.1007/s11217-022-09852-6；12–15m；EN/中；Open Access。
- **R8-N01 | production note | David Barnett, “The Berliner Ensemble.”** Bertolt Brecht in Context, Cambridge UP, 2021, **105–112**；以及Berliner Ensemble历史说明 https://www.berliner-ensemble.de/stream-mutter-courage-und-ihre-kinder ；不增加默认时间。
- **R8-C01 | C | Laura Bradley, “Blindness and (In)Sight...”** Brecht and the Art of Spectatorship, OUP, 2025, Ch.6, **189–221**；40–50m；EN/高；用于intended vs actual spectatorship。
- **R8-B03 | B1 | Andrew K. Kennedy, “Waiting for Godot.”** Samuel Beckett, Cambridge UP, 1989, **24–46**；DOI https://doi.org/10.1017/CBO9780511659430.005；25–30m；EN/低中。
- **R8-B04 | B2 | Walter D. Asmus, “Beckett Directs Godot.”** On Beckett, Anthem Press, 2012, **209–217**；DOI https://doi.org/10.7135/UPO9780857285805.020；10–12m；EN/中。
- **R8-ALT01 | 中文补充 | 李言实，《贝克特戏剧在中国的影响和接受》。** 《戏剧》2020(3), **124–144**；只读“身体的复活”小节；5–8m；ZH/低；不能完全替代production evidence。
- **R8-C02 | C | Michael Worton, “Waiting for Godot and Endgame: theatre as text.”** The Cambridge Companion to Beckett, 1994, **67–87**；DOI https://doi.org/10.1017/CCOL0521413664.004；25–30m；EN/中高。
- **R8-A01 | A | Robben Island Museum, “Prison Period Overview.”** 只读1946–1970、1961–1991两段；4–6m；EN/低；https://www.robben-island.org.za/prison-period-overview/ 。
- **R8-B05 | B1 | Brian Crow & Chris Banfield, “Athol Fugard and the South African ‘workshop’ play.”** An Introduction to Post-Colonial Theatre, Cambridge UP, 1996, **96–111**；DOI https://doi.org/10.1017/CBO9780511627675.007；20–25m；EN/中。
- **R8-B06 | B2 | Zakes Mda, Introduction to John Kani’s Nothing but the Truth.** Wits UP, 2002, **v–ix**；5–7m；EN/低中；https://www.cambridge.org/core/books/abs/nothing-but-the-truth/introduction/9CF4AE4A2492D1BE7CB5E992AEB237E4 。
- **R8-C03 | C | Chitra Jayathilake, “Muselmann: Incarceration and the Mobilised Body...”** African Studies 77.4 (2018), **607–625**；DOI https://doi.org/10.1080/00020184.2018.1497289；25–30m；EN/高。
- **R8-C04 | C | Rush Rehm, “‘If You are a Woman’: Theatrical Womanizing...”** Classics in Post-Colonial Worlds, OUP, 2007, **211–227**；DOI https://doi.org/10.1093/acprof:oso/9780199296101.003.0013；20–25m；EN/中高。
- **R8-B07 | B1 | Caryl Churchill, “Introduction to Cloud Nine.”** Plays: One, Methuen, 1985, **245–248**；ISBN 9780413566706；5–8m；EN/低。
- **R8-B08 | B2 | Michael Patterson, “The strategy of play: Caryl Churchill’s Cloud Nine (1979).”** Strategies of Political Theatre, Cambridge UP, 2003, **154–174**；DOI https://doi.org/10.1017/CBO9780511486197.012；20–25m；EN/中。
- **R8-N02 | production note | Royal Court Living Archive, Cloud Nine.** 1979 original-production/casting facts；https://livingarchive.royalcourttheatre.com/plays/cloud-nine-2/ ；不增加默认时间。
- **R8-C05 | C | James M. Harding, “Cloud Cover: (Re)Dressing Desire and Comfortable Subversions in Caryl Churchill’s Cloud Nine.”** PMLA 113.2 (1998), **258–272**；DOI https://doi.org/10.2307/463364；20–25m；EN/高。
- **R8-A02 | A | Wole Soyinka, “Author’s Note” to Death and the King’s Horseman.** Methuen Drama Student Edition, 1998/后续重印，ISBN 9780413695505；4–6m；EN/中；极轻剧透。
- **R8-B09 | B1 | Brian Crow & Chris Banfield, “Wole Soyinka and the Nigerian theatre of ritual vision.”** An Introduction to Post-Colonial Theatre, Cambridge UP, 1996, **78–95**；DOI https://doi.org/10.1017/CBO9780511627675.006；20–25m；EN/中高。
- **R8-B10 | B2 | Martin Rohmer, “Wole Soyinka’s ‘Death and the King’s Horseman’, Royal Exchange Theatre, Manchester.”** New Theatre Quarterly 10.37 (1994), **57–69**；DOI https://doi.org/10.1017/S0266464X00000099；15–18m；EN/中。
- **R8-ALT02 | 中文替代B1 | 宋志明，《约鲁巴神话与索因卡的“仪式戏剧”》。** 《文艺研究》2019(6)；15–20m；ZH/中；稳定转载 https://www.sohu.com/a/326694383_745113 ；可替代R8-B09背景职责，不能替代R8-B10。
- **R8-C06 | C | Omofolabo Ajayi-Soyinka, “Words to choreograph: Ritual archetypes of/at Esu’s crossroads.”** Atlantic Studies 19.4 (2022), **546–565**；DOI https://doi.org/10.1080/14788810.2021.1872279；25–30m；EN/高。
- **R8-C07 | C | Ato Quayson, “Ritual Dramaturgy and the Social Imaginary in Wole Soyinka’s Tragic Theatre.”** Tragedy and Postcolonial Literature, Cambridge UP, 2021, **124–155**；DOI https://doi.org/10.1017/9781108921992.005；40–50m；EN/高；Greek comparison必须后置。

---

## 10.6 Shared / Bridge Dependency Registry

这部分是Step 1最重要的数据清洗结果之一。它们不是“作品节点”，不能在最终路线中被重复计时。

| ID | 依赖关系 | 触发条件 | 默认/可选 | 作用 |
|---|---|---|---|---|
| **R1-S01** | Chekhov → Hemingway → Carver | B03+B12+B13全部完成 | **默认Shared B** | 用同一篇论文比较三种understatement/anticlimax，禁止“越来越少”的线性极简史 |
| **R3-S01** | Achebe ↔ Conrad | B07与U09都完成 | **U09默认成本内** | Achebe反向改变Conrad接受史；不在读Conrad前预装结论 |
| **R2-S02** | Faulkner → Latin America / García Márquez | U10+B08都完成 | **条件Bridge** | 只有读过两端才读，避免“影响史人名表” |
| **R3-S02** | García Márquez → Rushdie / world literature | B08+U12都完成 | **可选Bridge/C** | 校准magical realism全球扩散故事，不把Rushdie变“印度版百年孤独” |
| **B04→B23** | Woolf → 白先勇 | B04已在前，读完B23触发 | **B23默认材料本身即Bridge** | 证明localization≠imitation |
| **B15→B20** | 《聊斋》→莫言 | B20读完 | **B20默认材料内** | 本土传统必须后置重看，不能teleological |
| **B08/U10→B20** | García Márquez / Faulkner → 莫言 | B20读完；Faulkner只对已读U10者 | **B20默认/条件复用** | foreign influence作为重新发现本土的装置 |
| **B25→B31** | Antigone → The Island | B31读完 | **B31内部Bridge** | source text从intertext变成prison performance |
| **U06 series boundary** | 《三体》I → 后两部 | 尚未读后两部时禁止 | **deferred** | 后两部dark forest/cosmic sociology不得反向污染第一部 |

---

## 10.7 中文替代统一标记的“原始数据”状态

Step 2才会正式把中文替代统一分为A/B/C三档；Step 1只记录research log已经明确给出的替代性质。

当前可直接辨认：

### 明确“可替代但职责覆盖较窄”

- R1-ALT02：熊宗慧，只覆盖《带小狗的女人》，不能覆盖Chekhov双篇/谱系；
- R2-ALT01：付昌玲，可替Seaboyer做《赎罪》文本机制，但现实主义文学史覆盖较窄；
- R7-ALT02：杨莉莉，可替Smeliansky做《樱桃园》低门槛舞台史；
- R8-ALT02：宋志明，可替Crow/Banfield的Soyinka文化/仪式背景，但不能替Rohmer舞台实践。

### 明确“补充，不应替代默认核心”

- R1-ALT03：Carver作者访谈；
- R6-ALT01：余华作者访谈；
- R8-ALT01：李言实“身体的复活”小节；
- R7-ALT01：Ledger三页Ibsen舞台校准。

### 暂不赋予“等价替代”标签

截至Step 1：

> **没有材料被research log明确证明为与英文核心完全等价。**

Step 2将按职责覆盖而不是语言偏好正式分级。

---

## 10.8 Version Resolution Log

### Round 7必须覆盖的旧字段

1. **Antigone**
   - v0.8：Goldhill单A，32–40m；
   - v0.9：Rayor A0 + Goldhill A1 + Hall B，**35–42m**；
   - Canonical：采用v0.9。

2. **Hamlet**
   - v0.8：不预读，23–30m；
   - v0.9：Folger舞台物理A 5–7m + 原B1/B2，**28–37m**；
   - Canonical：采用v0.9。

3. **A Doll’s House**
   - 默认B不变；
   - C由泛指Moi精确到Chapter 7 pp.188–220；
   - “Ibsen发明box set/fourth wall”永久禁用。

4. **The Cherry Orchard**
   - 默认B1/B2不变；
   - 新增中文B2替代、Merlin历史铰链；
   - Aronson降为“强解释”而非中性史实；
   - 默认成本仍25–30m。

5. **Six Characters**
   - Worthen作者补全；
   - Lorch C从泛Introduction改为1921首演Chapter 2 pp.31–43；
   - 默认成本仍18–22m。

### 其他Round

Round 1–6、8没有同类“后版覆盖旧字段”的冲突；其职责卡修订已经在各Round末尾被本Step吸收。

---

## 10.9 Bibliographic Repair / QA Queue

Step 1只修复了“能在不重新研究候选的前提下迅速确认”的元数据。

### 本次已补稳定入口

- Elaine Showalter《达洛维夫人》导读：British Library中文稳定页；
- 范捷平《床上百无聊赖中想到的〈变形记〉》：南京大学出版社转载入口；
- 《全球研究视域下的〈聊斋志异〉》：中国社会科学网稳定页；
- 马振方《〈聊斋〉如何揭露官场黑暗？》：中国文化研究院稳定页；
- 王爱松《施蛰存的三篇小说与现代都市文化空间》：南京大学研究中心稳定页；
- 张爱玲《关于〈倾城之恋〉的老实话》：澎湃稳定转载；
- Ann Huss章节：JSTOR章节稳定入口；
- Keru Cai论文：DOI与59–84页元数据再次确认。

### 留到Step 5 Bibliographic QA，不在Step 1猜测

1. 范捷平《德国文学散论》的精确出版年、文章原始页码；
2. Hamblin Faulkner lectures的稳定永久入口与版本信息；
3. NPS / New Republic等网页材料的抓取日期是否需要进入最终指南；
4. 《流浪地球》刘慈欣访谈的稳定URL；
5. 陈建华《异史氏》评论稳定URL；
6. 鲁迅《〈呐喊〉自序》最终采用哪个公开稳定底本；
7. 郭帅、马原专题、余华访谈、曹霞、莫言访谈的稳定URL；
8. 陈思和教材具体版本/页码；
9. 叶立文、丛新强论文的完整卷期/页码；
10. 个别C层书章ISBN是否值得补全。

原则：

> **Step 1宁可标QA，也不根据记忆补一个看似完整但未核实的书目。**

---

## 10.10 时间预算一致性审计

### 基础包

沿用各Round去重后的默认预算：

| Round | 基础包辅助成本 |
|---|---:|
| R1 | 85–112m |
| R2 | 55–75m |
| R3 | 71–87m |
| R4 | 64–87m |
| R5 | 83–112m |
| R6 | 66–83m |
| R7 v0.9 | 131–161m |
| R8基础四节点 | 116–146m |
| **合计** | **671–863m = 11h11m–14h23m** |

R1的85–112m已包含R1-S01共享B一次，不可再次分摊后重复加总。

### 升级包

| Round | 升级辅助成本 |
|---|---:|
| R1 U01–U02 | 55–73m |
| R2 U07/U10/U11/U13 | 98–125m |
| R3 U09/U12 | 49–63m |
| R4 U03/U06/U08 | 60–79m |
| R5 U04/U14 | 32–40m |
| R6 U05 | 18–22m |
| R7 | 0 |
| R8 U15 | 39–49m |
| **合计** | **351–451m = 5h51m–7h31m** |

### 基础 + 全升级

> **1022–1314分钟 = 17小时02分—21小时54分。**

不计：

- 条件Bridge；
- 可选C；
- 中文补充若与默认B叠读；
- primary texts自身阅读时间。

这组数字在Step 2会因共享/替代关系再次做dependency-level重算，但当前没有发现Round总账与节点数据之间的硬冲突。

---

## 10.11 Step 1完成判定

Step 1完成标准逐项检查：

- [x] final-packages中的33个基础节点全部有canonical record；
- [x] 15个升级节点全部有canonical record；
- [x] 每个节点有当前有效职责 / 裸读警戒；
- [x] A是否存在已唯一确定；
- [x] 默认B已唯一确定；
- [x] 中文替代 / 补充已保留原始性质；
- [x] C层已登记；
- [x] 默认辅助成本已统一；
- [x] Bridge与触发时点已显式化；
- [x] Round 7 v0.8/v0.9冲突已解决；
- [x] 未确认书目信息未被猜测补齐；
- [x] 基础包与升级包时间总账闭合。

因此：

> **Canonical Materials Master Table v1 冻结，作为Step 2–5的唯一上游数据层。**

下一步：

> **Step 2 — 去重与跨节点整合。**

Step 2的重点不再逐书重新判断好坏，而是对Canonical Data做依赖分析：

1. 哪些材料实际上共享；
2. 哪些替代应二选一；
3. 哪些Bridge是条件触发；
4. 哪些C其实偷偷承担了必需职责；
5. 去重后最终默认路线的真实成本是多少。



# 11. Step 2 — Final Materials Dependency Graph v1

**状态：COMPLETED**

## 11.1 Step 2的核心结论

Step 2没有发现“研究阶段堆了大量可以直接删除的重复论文”。

相反，Round 1–8在研究过程中已经多次执行ROI stop rule、shared-B与Bridge-after-destination，因此真正需要优化的是：

> **材料之间的执行语义，而不是继续砍书目。**

最终把所有辅助材料关系冻结成六种边：

1. **CORE**：该节点默认必读A/B；
2. **SHARED**：一份材料服务多个节点，只读一次；
3. **TRIGGERED BRIDGE**：只有两端作品都进入所选路线后才自动触发；
4. **OPTIONAL BRIDGE**：两端都读过也仍然可选；
5. **OR / SUBSTITUTE**：二选一，绝不叠读；
6. **C / EVIDENCE-ONLY**：可支撑指南叙述，但不因此变成用户必读。

这一步最重要的方法修正是：

> **“研究证据源”与“读者作业”必须脱钩。**

一篇C层论文可以是我们写指南时的重要证据，却不意味着读者必须亲自读它。

---

## 11.2 Dependency Graph：正式执行语义

### Edge Type 1 — CORE

形式：

> Work → A（若有）→ Primary Text → B1/B2

规则：

- A只能在“预读收益 > 首读损失”时出现；
- B可以有两份，但必须解决不同职责；
- 同一节点的两份B若职责高度重合，Step 2必须降为OR，而不是累计。

压力测试结果：

> **现有默认双B / 三B节点均能证明职责不重合，不做进一步删除。**

典型：

- Morrison：Morrison “Site of Memory”回答“为什么必须这样写”；Raynaud回答“memory/rememory怎样在小说里运作”；
- Ishiguro：Clayton回答“SF如何被埋进现实主义表面”；Ishiguro/Gaiman回答“为什么作者必须跨genre boundary”；
- The Island：Crow/Banfield回答workshop theatre；Mda回答共同创作署名；
- Soyinka：Crow/Banfield回答ritual grammar；Rohmer回答实际演出中的non-verbal system。

---

### Edge Type 2 — SHARED：只付一次成本

#### S1. Chekhov → Hemingway → Carver

\`\`\`text
B03 Chekhov
      \
B12 Hemingway ---> R1-S01 Daniel Just
      /
B13 Carver
\`\`\`

触发：

> B03 + B12 + B13全部完成之后。

性质：

> **默认SHARED B。**

成本：

> 35–45m，只读一次。

严禁：

- 在三张作品卡中各算一次；
- 提前在Chekhov后就读；
- 把它拆成三份“各自的极简主义说明”。

这条边已经包含在基础包671–863m总账内。

---

### Edge Type 3 — TRIGGERED BRIDGE：选了两端就自动触发

这是Step 2相对Step 1最重要的实质性修订。

#### T1. Achebe ↔ Conrad

\`\`\`text
B07 Things Fall Apart
          \
           -> R3-S01 Achebe, "An Image of Africa"
          /
U09 Heart of Darkness
\`\`\`

触发：

> B07 + U09均完成。

性质：

> **Triggered-default Bridge。**

状态：

- 已经被包含在U09的28–35m默认成本中；
- 不增加新的总预算；
- 绝不在Conrad首读前提前使用。

原因：

如果用户选择U09，《黑暗的心》的升级职责本身就包括：

> anti-imperial insight与imperial/racial implication可以同时成立，并让后来的Achebe反向改变Conrad接受史。

不读这篇会使U09职责缺一块。

---

#### T2. Faulkner → García Márquez / Latin American Boom

\`\`\`text
U10 As I Lay Dying
          \
           -> R2-S02 Esplin
          /
B08 One Hundred Years of Solitude
\`\`\`

触发：

> U10 + B08均完成。

**Step 1状态：条件Bridge，未计入全升级默认预算。**

**Step 2修订：升级为 Triggered-default Bridge。**

原因：

Round 2只是把它延后；
Round 3明确写：

> 如果已经读过《我弥留之际》，读完《百年孤独》以后“现在才读”。

它的目的不是兴趣扩展，而是兑现U10中：

> Faulkner作为现代主义地域/多视角中继，后来与Latin American Boom形成重要对话

这一升级职责。

因此执行规则改为：

> **不选U10：不读。  
> 选了U10并完成B08：读，15–20m。**

这使“全基础 + 全升级”的真实执行预算发生修订，见11.9。

---

### Edge Type 4 — EMBEDDED BRIDGE：桥梁已经藏在后端默认B里，不再另收费

#### E1. Balzac → Flaubert

- B01《夏倍上校》；
- B02《一颗简单的心》；
- R1-B03 James Wood本身已经比较Flaubert与Balzac式现实主义。

结论：

> 不另加“Balzac→Flaubert文学史”材料。

---

#### E2. Woolf → 白先勇

\`\`\`text
B04 Mrs Dalloway
      ↓
B23 游园惊梦
      ↓
R5-B09 李奭学
\`\`\`

R5-B09本身就是Bridge材料。

结论：

> B23的15–20m已经包含Bridge成本。

---

#### E3. 《聊斋》→莫言

\`\`\`text
B15 聊斋
   \
    -> B20 红高粱 -> R6-B08 莫言访谈
\`\`\`

R6-B08在后端同时调用：

- 《聊斋》；
- 魏晋传奇；
- García Márquez / Faulkner影响；
- “远离两座高炉”。

因此：

> 不再额外配“《聊斋》如何影响莫言”论文。

---

#### E4. García Márquez / Faulkner → 莫言

同一R6-B08完成。

但执行细节分层：

- 已读B08《百年孤独》：Márquez段有实际Bridge价值；
- 已读U10 Faulkner：Faulkner段也成为实际Bridge；
- 未读U10：不要求读者为了一个人名补Faulkner知识。

同一材料按读者已经走过的路线激活不同层次，不新增成本。

---

#### E5. Antigone → The Island

\`\`\`text
B25 Antigone
     ↓
B31 The Island
     ↓
回看：谁在监狱里扮演Antigone、演给谁看、身体承担什么风险？
\`\`\`

这里没有新增论文。

Bridge本身是一项：

> **post-reading comparison action**

而不是：

> “再读一篇影响研究”。

因此成本记为0外部材料分钟；Step 4将把它变成checkpoint。

---

### Edge Type 5 — OPTIONAL BRIDGE：即使两端完成仍可跳过

#### O1. García Márquez → Rushdie → world literature

材料：

> R3-S02 Michael Bell。

触发前提：

> B08 + U12均完成。

但仍然：

> **OPTIONAL。**

原因：

U12默认A+B已经能够完成：

- nation formation；
- Partition；
- narrator error；
- historical mediation。

Bell新增的是：

> magical realism怎样在世界文学中扩散、被重新编码，以及“magical realism”这个全球标签本身怎样变得混乱。

它提高谱系解释精度，但不决定《午夜之子》能否读懂。

成本：

> 25–30m，不计默认预算。

---

#### O2. Woolf → McEwan

材料：

> R2-C04 Thom Dancer, “Limited Modernism.”

触发：

> B04 + U13完成后。

性质：

> 可选回看，不是U13默认Bridge。

原因：

Seaboyer已经能完成《赎罪》的realist legacies职责；
Dancer增加的是更精确的Woolf/modernism回路。

---

### Edge Type 6 — DEFER / NEGATIVE DEPENDENCY

有些dependency的正确动作不是“加材料”，而是：

> **暂时禁止一类材料进入。**

#### D1. 《三体》第一部 → 后两部

在只完成U06时：

- dark forest；
- cosmic sociology；
- 《死神永生》后人类；
- trilogy总体政治哲学；

全部保持deferred。

只有真正读到后两部以后才开放。

这是：

> **series-internal Bridge-after-destination。**

---

## 11.3 Final Materials Dependency Graph v1

\`\`\`text
REALISM / SHORT STORY
B01 Balzac ──> B02 Flaubert
                 │
                 └─ R1-B03 已内嵌 Balzac→Flaubert bridge

B03 Chekhov ─┐
B12 Hemingway├──> R1-S01 Daniel Just [SHARED / DEFAULT / ONCE]
B13 Carver ──┘


MODERNISM / WORLD LITERATURE
B04 Woolf ───────> B23 Bai Xianyong
                    └─ R5-B09 [EMBEDDED BRIDGE]

U10 Faulkner ─┐
              ├──> R2-S02 Esplin [TRIGGERED DEFAULT]
B08 Márquez ──┘

B08 Márquez ──┐
              ├──> R3-S02 Bell [OPTIONAL]
U12 Rushdie ──┘

B07 Achebe ───┐
              ├──> R3-S01 "An Image of Africa" [TRIGGERED DEFAULT]
U09 Conrad ───┘


CHINESE / LOCALIZATION
B15 Liaozhai ───────────────┐
B08 Márquez ────────────────┼──> B20 Mo Yan
U10 Faulkner [if selected] ─┘       └─ R6-B08 [EMBEDDED]

B19 现实一种 ──> 活着
     [internal author trajectory; no extra bridge paper]


DRAMA
B27 Ibsen ──> B28 Chekhov
              [comparison is synthesized from existing B; no new reading]

B25 Antigone ──> B31 The Island
                  └─ post-reading re-performance checkpoint [0 external minutes]

U06 Three-Body I ──X──> later-volume theory
                      [DEFER until destination read]
\`\`\`

---

## 11.4 “同一本书/同一来源”不等于重复：Source Bundles

Step 2另识别出一类实际使用上很有价值、但不能误当“删减”的关系：

> **同一容器里的不同章节。**

这会降低找资料的摩擦，但不会自动降低阅读时间。

### Bundle A — Peter Brooks, Realist Vision

- R1-B02：Balzac；
- R1-B04：Flaubert。

价值：

> 若走U01+U02，只找一本到手即可。

但两章解决不同职责，不合并。

---

### Bundle B — Martin Scofield, The Cambridge Introduction to the American Short Story

- R1-B06：Hemingway；
- R1-B07：Carver。

价值：

> 同一书完成两个微节点。

不删，因为：

- Hemingway读省略/对白；
- Carver读战后短篇复兴与内部变化。

---

### Bundle C — Crow & Banfield, An Introduction to Post-Colonial Theatre

- R8-B05：South African workshop play / The Island；
- R8-B09：Soyinka / ritual vision。

若同时走B31+U15：

> 一书解决两个后殖民戏剧节点。

但两章代表完全不同的production grammar，不能共享成一章。

---

### Bundle D — Pirandello in Context

- R7-B07 Witt “Metatheatre”；
- R7-B08 Worthen “The Fourth Wall”。

两章连续，适合一次取得。

但：

> metatheatre机制 ≠ fourth-wall apparatus史。

仍保留两份B。

---

### Bundle E — The Cambridge Companion to Chekhov

- R7-B06 Smeliansky为默认；
- R7-C06 Aronson为深入。

取得同一本书不意味着C自动升级为必读。

---

## 11.5 Alternative / Substitute制度正式统一

为避免与“资料层A/B/C”混淆，替代等级写成：

- **Alt-A**：职责覆盖等价或为原核心的超集，可真正替换；
- **Alt-B**：能完成主要职责，但覆盖明显较窄；
- **Alt-C**：只能补充，不能替代。

替代关系一律使用：

> **OR**

而不是：

> **AND**。

除非明确标记“补充”。

---

### Alt-A — 等价 / 超集替代

#### U14《我城》：R5-C04中文原论文 ↔ R5-B11英文压缩版

Step 1把：

> 謝曉虹中文原论文（41页）

仅列作C。

Step 2重新检查出版关系后修订：

- 中文原论文：《思与言》56(2), 2018, pp.73–113；
- 英文版：Chinese Literature Today 8(1), 2019, pp.50–57；
- 英文发表页明确说明：
  > 它是较长文章的**abridged version**。

因此：

> **中文原论文在职责覆盖上是英文B的超集。**

最终分类：

- **R5-B11英文8页：默认B，12–15m，ROI最高；**
- **R5-C04中文全文：Alt-A，45–60m；**
- 两者**二选一，不叠读**。

这成为目前唯一明确的中文Alt-A。

它不是默认方案，只因为时间成本高约33–45分钟，而不是质量不足。

---

### Alt-B — 主要职责可完成，但有明确损失

#### U02《包法利夫人》

默认：

> R1-B04 Brooks，25–30m。

替代：

> R1-ALT01 Vargas Llosa / King，约10m。

损失：

- 能抓Flaubert的形式意识、narrator与现代小说；
- 但对Balzac/Flaubert现实主义内部差异及“scandal of realism”覆盖较窄。

执行：

> 时间极紧可替；不叠读。

---

#### B03 Chekhov双篇

默认：

> R1-B05 Loehlin，12–15m，覆盖两篇。

中文：

> R1-ALT02 熊宗慧，只覆盖《带小狗的女人》。

最终分类：

> **Alt-B-partial。**

也就是说：

- 英文障碍很高时可以作为低门槛入口；
- 但它**不能宣称完整替代B03**，因为《苦恼》与双篇谱系职责会丢失。

这是Step 2对Step 1“替代/补充”模糊表述的收紧。

---

#### U13《赎罪》

默认：

> R2-B08 Seaboyer，25–30m。

中文替代：

> R2-ALT01 付昌玲，12–15m。

外部元数据与摘要再次确认，其强项是：

- 多视角；
- Briony自我辩护；
- metafiction；
- reality/fiction关系。

损失：

> 对19世纪realism → modernism → post-realism的文学史链条覆盖较窄。

因此：

> **Alt-B，二选一。**

---

#### B28《樱桃园》B2

默认组合：

> Loehlin B1 + Smeliansky B2 = 25–30m。

中文路径：

> Loehlin B1 + 杨莉莉R7-ALT02 = 22–30m。

杨莉莉文章确实讨论：

- Chekhov / Stanislavski；
- modern directing；
- 不同欧洲production；
- 写实演技反思。

但它不是对1904 MAT / Chekhov史的等量替换。

因此：

> **Alt-B。**

优点是中文门槛低；
代价是历史证据密度略低。

---

#### U15 Soyinka的B1

默认：

> R8-B09 Crow/Banfield 20–25m + Rohmer B2。

中文替代：

> R8-ALT02 宋志明 15–20m + Rohmer B2。

宋志明能很好覆盖：

- Yoruba myth；
- ritual；
- tradition的提炼/重构；
- “反仪式”。

但它不能替代Rohmer关于：

- visual/acoustic pattern；
- music/dance；
- mise-en-scène；
- intercultural performance

的实际舞台证据。

最终：

> **宋志明 = R8-B09的Alt-B，不是整个U15 packet的替代。**

使用中文B1后：

> U15默认辅助可由39–49m降到约34–44m。

---

### Alt-C — 只能补充

以下全部保留为：

> **不要用来替掉默认B。**

1. R1-ALT03 Carver访谈  
   - 强在作者自述“《大教堂》更开放、更丰满”；
   - 不承担文学史位置。

2. R6-ALT01 余华访谈  
   - 强在纠正“前进/后退”线性观；
   - 不替代刘艳对90年代叙事结构的分析。

3. R7-ALT01 Ledger / Ibsen  
   - 只做3页舞台校准；
   - 不能替代Grene的interior-as-social-machine。

4. R8-ALT01 李言实 / Beckett  
   - “身体的复活”非常直观；
   - 但没有Asmus那种Beckett本人导演的production evidence。

---

## 11.6 C层压力测试

问题：

> **如果删掉每一份C，默认路线是否还能完成它承诺的核心职责？**

总体结论：

> **能。没有一份C需要整体晋升为所有读者默认B。**

但产生两个结构修订。

---

### 修订一：R5-C04《我城》从“纯C”改成“双重身份”

见11.5：

> **默认情况下它仍不是附加必读；  
> 若读者需要中文，则它是R5-B11的Alt-A。**

所以它的正确状态不是：

> C only

而是：

> **Alt-A / 若已读英文B则不再读。**

---

### 修订二：鲁迅节点的“translation-as-constitutive”从单作必达职责降为路线级context

Step 1的B16 canonical record包含：

> 翻译是现代中文文学的构成性机制。

但默认B：

- 《呐喊》自序；
- Ann Huss；

主要解决：

> 两种现代主体失败与传统/现代张力。

真正系统证明：

> translation与modern Chinese literature是symbiotic relationship

的是R5-C03季进。

外部核验也再次确认该章明确主张：

- 翻译不是简单语言转换；
- 它改变叙事结构、技术、文类与形式；
- 可以被视为modern Chinese literature的内部组成。

Step 2有两种选择：

A. 把季进10页升级成B16第三份默认B；  
B. 收紧B16用户必须完成的职责，把translation保留为**Round 5路线级context**，季进继续C。

ROI判断选择：

> **B。**

理由：

- 鲁迅双篇的核心节点职责是现代主体 / 语言 / 社会批判；
- 再加一份10页translation history会使单节点负担向文学制度史偏移；
- Rule V仍然必须保留在整个中文路线的解释框架里；
- Step 3卡片可用1–2句把这一研究结论告诉读者，但不要求读者亲自读季进。

这是本阶段第一次明确应用：

> **Evidence source ≠ reader assignment。**

因此不是删掉Rule V，而是改变它在用户产品中的呈现位置。

---

## 11.7 哪些C虽然不是作业，但会进入指南正文的“事实底座”

为了避免Step 3误把“C可选”理解成“指南不能使用它”，这里显式列出：

- R7-C01 Andújar：支持“chorus的不回应也可成为舞台行动”；
- R7-C05 Merlin：支持《海鸥》1896/1898与Chekhov/Stanislavski productive mismatch；
- R7-C07 Lorch：支持1921《六个寻找作者的剧中人》首演史；
- R8-C01 Bradley：支持Brecht预期观众≠实际观众；
- R8-C05 Harding：支持radical casting device≠guaranteed radical reception；
- R5-C03季进：支持translation-as-constitutive；
- R4-C03 Le Guin Redux：支持经典作品的历史局限与作者后来自我修正。

执行规则：

> Step 3可以把这些结论压成一两句“必要校准”；  
> 但只有读者对这个问题产生兴趣时，才把原论文列进C。

---

## 11.8 重复阅读审计：最终没有删除哪些材料，以及为什么

### 未删除：Morrison双B

不是重复：

- B1 = archive problem / literary archaeology；
- B2 = memory/rememory形式。

### 未删除：Ishiguro双B

不是重复：

- B1 = genre mechanism；
- B2 = author-side genre-boundary evidence。

### 未删除：Poe双B

分别服务两篇相反reader protocol，且总成本只有11–15m。

### 未删除：Omelas双B

- Le Guin note = idea genealogy / psychomyth；
- Wyman = reader co-construction。

总成本10–15m，继续保留。

### 未删除：Antigone双A

- Rayor = stage geometry / chorus physicality；
- Goldhill = civic spectatorship institution。

v0.9已经证明不重复。

### 未删除：Hamlet双B

- Neill = text/performance mechanism；
- “Hamlet in performance” = reception/production variability。

### 未删除：Brecht双B

- Leach = play/history/form；
- Frimberger = Gestus落到actor/prop。

### 未删除：Godot双B

- Kennedy = dramatic structure；
- Asmus = rehearsal/directing precision。

### 未删除：Cloud Nine双B

- Churchill = workshop process / authorship；
- Patterson = political stage strategy。

### 未删除：Soyinka双B

这是最不能为了减时误删的一组：

> ritual grammar + performance evidence

二者正好对应戏剧阶段的文本职责 / 舞台职责双轨。

---

## 11.9 去重后的最终时间预算

### 11.9.1 基础包

没有新的重复扣减。

原因：

- R1-S01已经只计一次；
- embedded Bridges都藏在现有B中；
- 其余双B经压力测试均不重复。

因此仍为：

> **671–863分钟 = 11小时11分—14小时23分。**

---

### 11.9.2 “单独看升级节点”的新增成本

若只把每个升级节点看成独立增量，不考虑路线条件触发：

> **351–451分钟 = 5小时51分—7小时31分。**

这个数字保留作为：

> “升级作品自身材料成本”。

---

### 11.9.3 真正执行“基础 + 全部15个升级”时

因为全升级一定同时包含：

- U10 Faulkner；
- B08 Márquez；

所以R2-S02 Esplin的Triggered Bridge自动生效：

> +15–20m。

因此Step 2修订全升级真实执行预算：

- 升级层实际新增：
  > **366–471分钟 = 6小时06分—7小时51分**
- 基础 + 全升级：
  > **1037–1334分钟**
  > **17小时17分—22小时14分**

这取代Step 1的：

> 17小时02分—21小时54分

作为“全路线真正执行”的预算。

Step 1数字仍可保留，其含义改为：

> **节点材料机械合计，不含条件触发Bridge。**

---

### 11.9.4 若再选择可选Márquez→Rushdie桥

R3-S02：

> +25–30m。

则完整路线为：

> **1062–1364分钟 = 17小时42分—22小时44分。**

但这不是默认正式预算。

---

## 11.10 替代路线的时间影响

这些数字不进入正式总预算，因为它们交换的是：

> 时间 / 语言门槛 / 职责覆盖。

| 节点 | 默认 | 替代 | 时间变化 | 代价 |
|---|---:|---:|---:|---|
| U02《包法利夫人》 | 25–30m Brooks | ~10m Vargas Llosa/King | **省15–20m** | 文学史覆盖变窄 |
| U13《赎罪》 | 25–30m Seaboyer | 12–15m 付昌玲 | **省13–15m** | realist-legacies链条变弱 |
| B28《樱桃园》 | 25–30m | 22–30m 中文B2 | **最多省约3m** | production-history密度略降 |
| U15 Soyinka | 39–49m | 34–44m 中文B1+英文B2 | **省约5m** | ritual background证据密度略降 |
| U14《我城》 | 12–15m 英文压缩 | 45–60m 中文原文 | **多33–45m** | 无质量损失，换取中文阅读 |

因此最终指南不能再写成：

> “中文替代 = 更省时间”。

实际有三种情况：

- 中文更短；
- 中文差不多；
- 中文更长但覆盖更完整。

---

## 11.11 Execution Rules E1–E6

这是Step 2形成的构建规则，不替代research log的Rule A–AU。

### E1 — Shared material is paid once

> 一份SHARED B在所有前置节点完成后读一次，不回填到每张卡重复计时。

---

### E2 — A bridge can be conditional but mandatory once triggered

> “条件”描述的是它何时出现，不等于出现以后仍然可有可无。

Faulkner→Márquez建立此规则。

区分：

- **Triggered-default Bridge**
- **Optional Bridge**

---

### E3 — Alternative means OR, not AND

若材料标：

> Alt-A / Alt-B

最终卡必须用：

> “二选一”

而不是：

> “中文读者可以再补一篇”。

否则所谓替代反而增加负担。

---

### E4 — Evidence source ≠ reader assignment

指南可以依赖学术材料形成可靠的一句话背景校准，而无需把每个证据源升级成读者作业。

适用于：

- translation；
- production history；
- reception history；
- 观众研究；
- 作者/导演分歧。

---

### E5 — Embedded bridge should stay embedded

如果后端B已经承担跨节点比较：

> 不再为了“体系完整”另配一篇影响研究。

适用：

- Balzac→Flaubert；
- Woolf→白先勇；
- 《聊斋》/Márquez→莫言。

---

### E6 — Procurement bundling is not intellectual deduplication

同一本Cambridge Companion / 同一专著中的不同章节：

> 可以一次找到、一次借阅；

但只有职责重复时才允许删阅读。

“找资料成本下降”不能伪装成“理解成本已经重复”。

---

## 11.12 Step 2完成后的Final Materials Dependency Graph摘要

### 默认共享一次

1. R1-S01 Chekhov/Hemingway/Carver。

### 条件触发后默认

2. R3-S01 Achebe/Conrad；
3. R2-S02 Faulkner/Márquez。

### 已内嵌，不新增时间

4. Balzac→Flaubert；
5. Woolf→白先勇；
6. 《聊斋》→莫言；
7. Márquez/Faulkner→莫言；
8. Antigone→The Island。

### 两端完成仍可选

9. Márquez→Rushdie；
10. Woolf→McEwan。

### 延后禁止

11. 《三体》第一部→后两部理论。

### 替代等级

- **Alt-A：1组**
  - 《我城》中文原论文 ↔ 英文压缩版；
- **Alt-B：5组**
  - 《包法利夫人》短替代；
  - Chekhov中文部分替代；
  - 《赎罪》中文替代；
  - 《樱桃园》中文B2替代；
  - Soyinka中文B1替代；
- **Alt-C：4组**
  - Carver作者访谈；
  - 余华作者访谈；
  - Ibsen短校准；
  - Beckett中文身体补充。

---

## 11.13 Step 2完成判定

- [x] Shared B全部显式化，且只计一次；
- [x] Bridge分成triggered-default / embedded / optional / deferred；
- [x] Faulkner→Márquez的触发语义纠正；
- [x] 中文/低门槛替代全部改成OR关系，不再默认叠读；
- [x] 找到1个真正Alt-A：《我城》中文原论文；
- [x] C层逐项压力测试，没有隐性“必须全员晋升”的C；
- [x] translation-as-constitutive从鲁迅单卡必达职责移到Round 5路线级context；
- [x] Source Bundle与真正内容去重分开；
- [x] 基础预算复核；
- [x] 全升级预算按Triggered Bridge重算；
- [x] Dependency Graph可以直接供Step 3制卡使用。

因此：

> **Final Materials Dependency Graph v1 冻结。**

下一步：

> **Step 3 — 单作品执行卡。**

Step 3不再判断“材料好不好”，而把：

> Canonical Node + Dependency Edge + Alternative Policy + Time

压成用户拿起来就能执行的Reading Companion Card。


# 9. Revision log


## 2026-10-05 — v0.3

完成Step 2 — 去重与跨节点整合。

主要更新：

1. 建立Final Materials Dependency Graph v1，定义CORE / SHARED / TRIGGERED BRIDGE / OPTIONAL BRIDGE / OR SUBSTITUTE / C-EVIDENCE六类执行边；
2. 确认研究阶段已有较强去重，Step 2的主要收益来自执行语义而不是继续删除论文；
3. 将Faulkner→García Márquez的R2-S02从“条件但预算外”修订为“条件触发后默认”，使全基础+全升级真实预算改为1037–1334分钟（17h17m–22h14m）；
4. Achebe↔Conrad保持Triggered-default且已包含于U09预算；
5. Márquez→Rushdie与Woolf→McEwan保持optional bridge；
6. 明确Balzac→Flaubert、Woolf→白先勇、《聊斋》/Márquez/Faulkner→莫言、Antigone→The Island为embedded bridge，不新增文献成本；
7. 替代制度统一为Alt-A / Alt-B / Alt-C，并强制执行OR而非AND；
8. 将謝曉虹《我城》中文原论文从纯C重新识别为R5-B11的Alt-A：英文8页版为原长文的abridged version；默认仍保留英文版因为ROI更高；
9. 鲁迅节点的translation-as-constitutive从单卡必达职责移为Round 5路线级context，季进继续C，确立“evidence source ≠ reader assignment”；
10. 建立Source Bundles，区分“获取成本去重”与“认知职责去重”；
11. Step 2状态更新为COMPLETED，下一步进入Step 3 Reading Companion Cards。




## 2026-10-05 — v0.2

完成Step 1 — Research → Canonical Data。

主要更新：

1. 将33个基础节点 + 15个升级节点全部归一化为48个canonical route records；
2. 建立Node Master Index与Material Registry两层数据结构，避免完整书目在多节点重复抄写；
3. 保留组合阅读单元，不为表格整齐拆散Chekhov/Borges/Poe/Carver/《聊斋》/鲁迅/《党费》+《百合花》/余华双节点；
4. 将Shared B与Bridge从作品节点中分离，建立Dependency Registry；
5. Round 7按v0.9覆盖v0.8发生修订的字段，其余Round按各自完成版本抽取；
6. 定点修复British Library、CSSN、中国文化研究院、南京大学、澎湃、JSTOR等稳定入口；未确认元数据显式进入Step 5 QA队列；
7. 基础包时间复核为671–863分钟（11h11m–14h23m）；升级包351–451分钟（5h51m–7h31m）；全基础+升级默认辅助1022–1314分钟（17h02m–21h54m），条件Bridge/C另计；
8. Step 1状态更新为COMPLETED；下一步进入Step 2依赖去重与Bridge整合。



## 2026-10-05 — v0.1

建立执行指南构建日志。

记录：

1. 五步收敛方案；
2. 每一步的任务边界、输入、产出和完成标准；
3. authoritative source关系；
4. 本阶段明确不做的事项；
5. 后续所有Step完成情况继续累计写入本文件。
