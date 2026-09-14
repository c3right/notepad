---
title: "历史人生模拟案例库：第一次候选排序实验"
date: 2026-09-14
updated: 2026-09-14
status: working
type: research-note
topics:
  - history
  - decision-making
  - case-method
  - reading-path
  - historiography
keywords:
  - Decision Atom
  - candidate ranking
  - hard gates
  - scoring rubric
  - blind simulation
source: "ChatGPT conversation | web research"
language: zh-CN
---

# 历史人生模拟案例库：第一次候选排序实验

> 本实验优先按已落盘的两份规则执行：
>
> - [Decision Atom 正式字段表 v1](./2026-09-14-history-decision-atom-schema-v1.md)
> - [Decision Atom 软评分量表 v1](./2026-09-14-history-decision-atom-scoring-v1.md)
>
> 实验过程中不因个案“看起来精彩”而临时修改 Hard Gates 或 M01—M10；候选阶段只打 Provisional Score。若实验结束后发现规则边界问题，单独报告，不在中途改尺子。

## 一句话结论

第一次真正排序后，筛选器开始产生预期效果：**低知名度、窗口清楚、史料可恢复的案例被推到前面；著名英雄/灾难故事即使极有戏剧性，也会因为叙事污染、主体不清、真实选项不足或背景成本过高而后移甚至退出D轨。**

本轮8个新候选的“下一步研究投入优先级”暂排为：

1. **Max Starkloff：1918年圣路易斯是否实施全面公共场所关闭**
2. **Gordon Hirabayashi：1942年是否服从排除/迁移命令**
3. **IBM System/360：1961—1962年是否接受统一兼容产品线战略**
4. **Donner-Reed Party：1846年是否进入 Hastings Cutoff**
5. **Challenger：1986年 Morton Thiokol 管理层是否逆转“不发射”建议**
6. **Chiune Sugihara：1940年是否突破签证资格规则继续签发过境签证**
7. **Camp David：1978年最后阶段如何处理西奈定居点文字与程序妥协**
8. **Shackleton：1916年从 Elephant Island 乘 James Caird 求援——当前切法暂不作为D类优先案例**

这里的排序是“**下一单位研究时间投在哪里最划算**”，不是历史重要性排名，也不是十项分数机械求和。

---

# 1. Scoring Context

本轮固定上下文，不对单个案例临时改尺：

```yaml
reader_baseline: "受过本科程度教育、有基本中外历史框架、不是专题专家的中文成年读者"
library_snapshot: "v0-calibration"
scoring_stage: "provisional"
```

`v0-calibration` 包含前几轮已经用于校准规则的样本（如 Kelsey、Atlantic Telegraph、古巴导弹危机等），但尚未建立正式长期候选池。M10“样本新增价值”相对于这一状态判断。

## 排序原则

1. 先检查 Hard Gates；明显不是Atom的，不靠高软分救回来。
2. M01、M02若暂低于3，不进入当前优先建设队列。
3. 不求总分；主要看四种画像：闭卷模拟、深度复盘、人生迁移、案例库补洞。
4. 对尚未qualified的高潜候选，可以排在“优先深挖”，因为排序对象是研究投入，而不是已经做好的Packet。
5. 高知名度案例允许保留，但如果M09很低，不优先作为第一批“关闭上帝视角”案例。

---

# 2. 总表

记法：`4M` = 4分 / Medium confidence。

| 候选 | Hard Gate初判 | 主型暂定 | M01 | M02 | M03 | M04 | M05 | M06 | M07 | M08 | M09 | M10 | 行动 |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| Starkloff / St. Louis 1918 | 强Candidate，接近qualified | D2边界 + 急性危机 | 4M | 4M | 4M | 4M | 4H | 5H | 4M | 5H | 5H | 4H | **优先深挖** |
| Hirabayashi 1942 | 强Candidate；N-Gate待进一步核实 | N（D1副标签） | 3M | 4H | 5M | 3M | 5H | 5H | 5H | 4H | 4H | 5H | **优先深挖** |
| IBM System/360 | Candidate；主体/接受窗口仍需钉死 | D2 | 3M | 3M | 4M | 4M | 5H | 5H | 3M | 3M | 3H | 5H | **优先深挖** |
| Donner-Reed / Hastings Cutoff | Candidate；集体主体拓扑待解 | D1 + D2 | 3M | 3M | 5M | 3M | 5H | 5H | 5H | 4H | 4H | 5H | **优先深挖** |
| Challenger / Thiokol 1986 | qualified级别很高 | D2边界 | 5H | 5H | 3H | 5H | 5H | 5H | 5H | 2M | 0H | 4H | **高价值复盘，非首批盲模拟** |
| Sugihara 1940 | Candidate；窗口/N-Gate需加强 | D2边界 + N | 3M | 4M | 4M | 3M | 5H | 5H | 5M | 4H | 2H | 4H | **保留候选** |
| Camp David 1978 final settlement wording | 可成Atom，但高成本且记录有缺口 | D6 | 3H | 5H | 5M | 5H | 5H | 4M | 4M | 1H | 2H | 3H | **后置深挖** |
| Shackleton / James Caird 1916（当前切法） | GATE-2可疑 | D2/D3候选，但更像L/W | 4H | 4H | 1M | 4M | 5H | 4H | 5H | 4H | 2H | 3H | **当前Atom停止投入；重新切片或转L/W** |

---

# 3. 候选1：Max Starkloff，圣路易斯，1918

## Atom暂定句

> 1918年10月初，在圣路易斯民间流感病例从零星迅速增加、附近军营已有大规模病例、但关闭学校与公共场所将造成巨大社会经济成本时，卫生专员 Max Starkloff 需要决定：继续以病例报告和个体隔离为主，还是推动并执行全市性关闭与集会禁令。

10月6日他公开认为强制性隔离并不实际；到10月7日病例继续上升，他召集市长、公共卫生、红十字、医院、学校与商业代表，会议中有人反对大规模关闭，最终决定实施全面限制。这给出了罕见的清晰“前一天仍未跨阈值—次日跨阈值”窗口。

资料线索：

- University of Michigan, *The American Influenza Epidemic of 1918: St. Louis*: https://www.influenzaarchive.org/cities/city-stlouis.html
- St. Louis Public Library 1918–1919 influenza collection: https://cdm17210.contentdm.oclc.org/digital/collection/influenza

## 为什么排第1

- Freeze容易锁定，Commitment Threshold清楚；
- 人物本身对普通读者陌生，M09高；
- 有同时代报纸、卫生部门年报，背景又不难压缩；
- 决策结构与现代组织/公共风险中的“何时从监测升级到强干预”高度同构；
- 不是伟人故事，且存在反对声音与经济成本，天然有张力。

当前最大问题只是：需要把10月6—8日的一手报纸、年报和授权链完整核一遍，再决定Focal Actor究竟写Starkloff个人还是Starkloff+市政决策共同体。

---

# 4. 候选2：Gordon Hirabayashi，1942

## Atom暂定句

> 1942年春，大学生 Gordon Hirabayashi 面对针对日裔居民的宵禁与强制排除/迁移命令，在服从法律与家庭共同迁移、公开拒绝并接受逮捕/诉讼、或以其他方式逃避执行之间，必须决定自己是否公开拒绝该命令。

现存1942年5月13日《Why I Refuse to Register for Evacuation》是极重要的同时代材料；国家档案保存其刑事案件文件，Densho则保存其后来对形成过程、家庭压力与信仰背景的详细口述。

资料线索：

- University of Washington 1942 statement: https://digitalcollections.lib.washington.edu/digital/collection/pioneerlife/id/21356/
- National Archives case record: https://www.archives.gov/seattle/highlights/gordon-hirabayashi
- Densho oral histories: https://ddr.densho.org/

## 为什么排第2

它几乎完美补足目前案例库最缺的维度：

- 非精英个人；
- 个人价值与国家命令冲突；
- 家庭是Affected Party但不是决定者；
- 决策的身份后果极强；
- 对中文普通读者结局并不高度熟悉。

它没有排第1，是因为如果把N作为Primary Type，就必须进一步证明：Freeze时“守法/家庭义务”与“良知/公民原则”仍在他本人内部真实竞争，而不是我们从后见材料替他构造道德困境。1942年声明已经是决定后的文本，N-Gate仍需向更早的日记/书信追。

---

# 5. 候选3：IBM System/360，1961—1962

## Atom暂定句

> 1961年底，在IBM拥有多条彼此不兼容且各自成功的计算机产品线时，SPREAD团队提出以统一兼容架构取代既有产品体系；IBM高层必须决定是否接受这一方案，从而承担自我蚕食、巨额研发制造投入与组织重构风险。

SPREAD在1961年秘密工作并形成报告；Computer History Museum保存团队成员口述与项目资料，IBM资料也确认内部曾有激烈分歧、项目将替代既有产品线。

资料线索：

- Computer History Museum, SPREAD/System 360: https://www.computerhistory.org/revolution/mainframe-computers/7/162
- IBM System/360 history: https://www.ibm.com/history/system-360
- CHM oral history collections and IBM SPREAD report references.

## 为什么排第3

这是目前最有希望的商业/技术案例：D2清楚、后果可追踪、现代迁移价值极高，而且能显著增加案例库领域多样性。

暂不排更前的原因是GATE-4仍没完全钉死：到底以 Watson Jr.、Learson、SPREAD后的“IBM management”还是某个具体批准共同体为Focal Actor？同样，Freeze应放在SPREAD报告提交、管理层接受、还是资源承诺的哪一刻，也需进一步靠公司档案/口述锁定。

---

# 6. 候选4：Donner-Reed Party 与 Hastings Cutoff，1846

## Atom暂定句

> 1846年7月底，在 Fort Bridger，Donner-Reed Party 面对已知较稳妥的传统California Trail与 Hastings 宣称可节省数百英里的新捷径，需要决定是否把包括大量家庭成员在内的车队驶入尚未被重型马车充分验证的 Hastings Cutoff。

James Reed当时的文字显示他相信捷径可缩短里程，并获得Bridger的正面评价；同时已有James Clyman等人的警告，其他加州移民选择传统路线。

资料线索：

- National Park Service, Hastings Cutoff: https://www.nps.gov/places/hastings-cutoff.htm
- NPS, Donner-Reed Party: https://www.nps.gov/cali/learn/historyculture/donner-reed-party.htm
- PBS American Experience transcript, including Reed’s contemporary journal text.

## 为什么排第4

从“人生模拟器”角度，它非常强：普通移民家庭、路线选择、时间窗口、未经验证的捷径、专家/熟人相互矛盾的意见、家庭成员承担巨大后果。

最大风险是主体拓扑。不能简单写“Donner Party决定了”：九个家庭与单身成员并不等于一个同质决策者。若无法从日记、会议或家族材料恢复谁真正推动/同意路线选择，就会卡在GATE-4。因此它值得优先深挖，但目前不能直接制作Packet。

---

# 7. 候选5：Challenger，1986年1月27日 Thiokol 管理层逆转建议

## Atom暂定句

> 1986年1月27日晚，在Thiokol工程团队因低温和O-ring数据建议不要在既有经验温度范围之外发射、NASA方面强烈质疑该建议的情况下，Morton Thiokol管理层必须决定：维持“不建议发射”，还是在无法证明必然失败的情况下逆转建议并同意发射。

Rogers Commission保存了非常细的参与者、图表、会议时序与后续证词：初始工程建议明确为低于53°F不发射；管理层离线讨论后逆转，部分工程师持续反对。

资料线索：

- NASA Rogers Commission, Chapter 5: https://www.nasa.gov/history/rogersrep/v1ch5.htm

## 为什么只排第5

作为Decision Atom，它甚至比前四个更“干净”：M01/M02/M04几乎是范本级。

但本项目的目标不是只找“最容易教学的决策案例”。Challenger已经是工程伦理、组织失败和群体决策课程中的经典反例，名称本身几乎已经泄露结果与主流因果解释，因此 `M09=0`。它非常适合**深度复盘型**案例，也可作为检验Packet设计是否能抵抗后见偏差的“控制样本”，但不应占用第一批闭卷案例建设资源。

另一个值得注意的结果：它再次出现Kelsey式结构——主体不是“自己豪赌”，而是**是否给系统放行跨越高风险阈值**。

---

# 8. 候选6：Chiune Sugihara，1940

## Atom暂定句

> 1940年夏，在大量犹太难民请求经日本逃离、而日本外务省对过境签证有目的地手续与资金等资格要求的情况下，驻立陶宛领事杉原千畝需要决定：严格按资格条件签证，还是在不满足条件的情况下继续签发，使难民获得离开苏联控制区的路径。

日本外务省和USHMM资料确认存在签证资格要求、杉原突破部分要求大量签发、东京之后就此发电追问；大量实际签证也保存至今。

资料线索：

- Japan MOFA, “Visas for Life”: https://www.mofa.go.jp/files/100102645.pdf
- USHMM, Chiune Sugihara: https://encyclopedia.ushmm.org/content/en/article/chiune-sempo-sugihara

## 为什么只是保留候选

材料潜力强，身份又是中层官员，非常符合项目目标；但目前公开叙事高度英雄化，“Visas for Life”“Righteous Among the Nations”等后见标签会显著降低M09。

更重要的是，如果把它作为N型价值困境，需要找到Freeze之前的同时代材料，证明杉原本人当时确实在“外交服从/职业责任”与“人道义务”之间经历未解决冲突，而不是后世根据结果重构。现在更安全的做法是先按“受规则约束的签证授权决策”Candidate研究，N只做副标签。

---

# 9. 候选7：Camp David，1978年9月17日西奈定居点文字

## Atom暂定句

> 1978年Camp David峰会最后阶段，埃及要求撤除西奈以色列定居点成为和平条约前提，以色列则拒绝把这一要求直接写成同样形式；作为调停者，Carter需要决定如何设计最后的文字和程序，使双方都能接受而不让峰会在最后时刻破裂。

美国国务院FRUS修订版保存大量会前文件、工作文件、逐日摘要以及Samuel Lewis当时的手写笔记；9月17日的记录显示定居点问题是最后重大分歧之一，并最终通过关于Knesset表决的程序语言解决。

资料线索：

- FRUS 1977–1980, Vol. IX revised edition: https://history.state.gov/historicaldocuments/frus1977-80v09Ed2

## 为什么后置

从D6角度这是极优质的多行动者谈判案例；但FRUS编者明确说明，Carter与双方大量会议没有正式同时代会谈纪要，部分过程只能靠个人笔记、逐日摘要与后来的日记补足。

更现实的问题是M08：要理解“什么可以让、什么不能让”，读者必须理解1973年战争、242号决议、Sinai、West Bank/Gaza、Begin/Sadat各自国内政治约束等，背景成本非常高。它应当进入成熟案例库，但不适合第一批MVP。

---

# 10. 候选8：Shackleton 从 Elephant Island 驾 James Caird 求援

## 当前Atom句

> 1916年4月，在Endurance队员困于Elephant Island、无无线电且正常航路几乎不会经过该岛的情况下，Shackleton需要决定是否派出小艇横渡南大西洋前往South Georgia求援，还是继续留在岛上等待其他可能性。

多名队员日记、Shackleton本人记录和航海日志丰富，代入感极强。

资料线索：

- State Library of New South Wales, Hurley diary / Elephant Island: https://www.sl.nsw.gov.au/stories/marooned-on-elephant-island
- National Library of New Zealand, Worsley and McNeish journals: https://natlib.govt.nz/
- Library of Congress, Shackleton, *South*: https://www.loc.gov/item/20001604/

## 为什么当前停止D类投入

问题不是史料，而是 **GATE-2 / M03**。

现有材料反复强调：Elephant Island几乎没有被动获救可能，食物、冬季和庇护条件又恶化。因此“出海求援 vs 原地等待”可能不是两个同样现实的方案；故事非常英勇，却不等于Decision Tension高。

这正是筛选器应当拒绝的情况：**戏剧性、危险、领导力传奇都不能替代真实开放选项。**

后续有两个方向：

1. 重新切更早的Atom，例如在浮冰/小艇阶段选择目标岛屿；
2. 将其转为L/W：危机中的领导、群体生存和长期轨迹案例。

当前不因“故事太精彩”强行留在D核心库。

---

# 11. 排序后的三档行动队列

## A｜优先投入下一轮深挖

### 1. Starkloff
最像第一批真正Case Packet：低污染、窗口清楚、背景便宜。

### 2. Hirabayashi
个人/N型和普通人维度极强；优先找Freeze之前的日记/书信，验证N-Gate。

### 3. IBM System/360
优先找SPREAD原报告、决策接受过程、Watson/Learson/管理委员会的主体结构。

### 4. Donner-Reed
优先查Fort Bridger前后不同家庭/领导者材料，先解决“到底是谁决定”的问题。

## B｜保留，但不是第一批闭卷Packet

### Challenger
几乎可直接做高质量复盘Packet，但盲模拟价值太低；作为控制样本保存。

### Sugihara
继续找同时代电报与决策前材料；在此之前不要把英雄叙事当作N型心理证据。

### Camp David
证据和多视角都强，但背景投入巨大；适合案例库成熟后做高阶D6。

## C｜当前Atom停止投入

### Shackleton / James Caird（当前切法）
不否定材料价值，只否定“当前这个切法是高张力D Atom”。转L/W或重新切窗口。

---

# 12. 本轮对规则的实际检验

## 12.1 Hard Gates有效，而且比评分更先产生价值

- Shackleton被GATE-2挡住；
- Donner/IBM被GATE-4提醒主体尚未切干净；
- Sugihara/Hirabayashi的N型使用被GATE-N约束；
- 没有出现“高M07/高戏剧性把不合格案例救回来”的现象。

## 12.2 M08与M09真正改变了排序

如果只看史料与历史重要性，Camp David和Challenger应在最前。

加入M08/M09后：

- Camp David因背景成本后移；
- Challenger因标准叙事几乎完全预装而后移；
- Starkloff、Donner这类相对陌生样本上升。

这说明量表在服务项目目标，而不是重复“历史名局排行榜”。

## 12.3 M10没有沦为“冷门奖励”

冷门本身不加分。Shackleton不冷门，仍因材料/代入强保留L/W价值；Donner和Hirabayashi的M10高，是因为它们填补“普通家庭/个人”“非Direct最高领导”“价值冲突”等结构空白，而不是仅仅因为较陌生。

---

# 13. 规则突破/偏离报告

本轮**没有在评分过程中突破已落盘Hard Gates或M01—M10定义**。

有两项刻意的实验设计偏离，但不是修改规则：

1. **故意放入一个很可能不是好D Atom的Shackleton候选**，验证筛选器是否敢把著名英雄故事挡出去；结果是能。
2. **故意放入一个M09接近0的Challenger经典案例**，验证“不求总分、按画像分流”是否真的有用；结果是它被保留为“深度复盘型”，但没有挤进首批闭卷建设队列。

实验结束后出现一个需要进入下一版规则观察名单的现象：

> **D2“高风险承诺与机会窗口”的抽象层级可能偏窄。**

Kelsey、Challenger、Starkloff连续出现同一结构：主体并非“自己重仓”，而是在决定**是否授权/批准/触发一个低可逆、高下行风险的系统状态**。如果后续再出现工程签字、药品审批、贷款放行、发射授权等同构样本，建议把D2重新命名或扩展为类似：

> **D2 高风险承诺、授权与放行阈值**

本轮不修改正式v1，以免测试过程中移动标尺。

---

# 14. 下一步建议

第一次排序实验已经完成了它的核心任务：不是建立大案例池，而是验证落盘规则能否真正改变研究优先级。

下一小步不宜立即扩到几十个候选。建议先对A档前四个做一次**“Qualification Sprint”**：每个只解决当前最关键的1—2个Hard Gate/低置信字段，不全面写Case Packet。

建议顺序：

1. Starkloff：核10月6—8日同时代材料与授权链；
2. Hirabayashi：找Freeze以前的日记/书信，核N-Gate；
3. IBM：锁定SPREAD报告被接受的具体主体、窗口与替代方案；
4. Donner-Reed：重建Fort Bridger路线选择的实际集体决策结构。

只有这四个里面出现至少2—3个真正qualified、且M01/M02稳定≥3，再进入“从案例反推书与史料、制作第一批Case Packet”的阶段。
