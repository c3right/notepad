---
title: "ZgoCloud LA VPS：Clash v2.2-fixed 分流优化、DNS 警告与 iOS 流量监测全过程"
date: 2026-10-08
updated: 2026-10-08
status: evergreen
type: reference
topics:
  - vps
  - network-proxy
  - traffic-monitoring
  - ios-shortcuts
  - troubleshooting
keywords:
  - ZgoCloud
  - Clash Verge Rev
  - Mihomo
  - ZGO-LA Enhanced v2.2 fixed
  - MetaCubeX
  - Fake-IP
  - vnStat
  - Shadowrocket
  - iOS Shortcuts
source: "2026-08-23～24 ChatGPT 对话及用户提供的 ZgoCloud 控制台、Mihomo、iOS 快捷指令截图和 SSH 命令输出；2026-10-08 整理"
language: zh-CN
---

# ZgoCloud LA VPS：Clash 分流优化和 iPhone 流量查询完整复盘

> **日期和证据边界**：以下主要是 **2026-08-23～24** 的历史操作、配置建议和实际验证，整理于 2026-10-08，未在整理日重新登陆 VPS。另有 [已存在的 VPS 初始化、线路、IP 质量、sing-box REALITY 部署排障记录](./2026-10-08-zgocloud-la-vps-setup-validation.md)，本文与其并列、**不修改**原始文档。公开 GitHub 笔记绝不保存真实 UUID、REALITY Private Key、Public Key/Short ID 组合、SSH 凭据。

## 0. 一句话结论与归档入口

Windows Clash Verge Rev 2.5.2 + Mihomo 从大段手写域名收敛为 **ZGO-LA Enhanced v2.2 fixed**：AI 使用单组 MetaCubeX MRS rule-provider，部分海外网站依赖 GEOSITE 或显式规则，国内域名/IP 直连，未知站点默认 ZGO-LA；基础国内/海外出口实测通过。VPS 装了 **vnStat 2.10**，通过修正过的 **/usr/local/bin/zgo-traffic** 汇总 21 日至次月 20 日的 RX+TX，iPhone **快捷指令 → SSH → 文本 → 快速查看** 已成功显示分行报告。

**三份相互链接的历史材料**：

- [ZGO-LA Enhanced v2.2 fixed：完整去密 YAML](./2026-10-08-zgo-la-enhanced-v2.2-fixed.yaml) —— 独立保存，不含真实节点凭据；**不包含后来讨论但未确认实施的 IPv6 DNS 修改**。
- [最终 iPhone 友好版 zgo-traffic Python 脚本](./2026-10-08-zgo-traffic-ios.py) —— 归档当时的程序逻辑及历史修正，不代表现在 VPS 上的字节级最新版本。
- [原 VPS 初始化与 REALITY 排障总结](./2026-10-08-zgocloud-la-vps-setup-validation.md) —— 原样保留。

| 项目 | 2026-08 已有证据 / 状态 |
| --- | --- |
| Windows v2.2-fixed 启用 | **PASS**：用户确认 Clash Verge 配置加载 |
| Windows 海外流量 | **PASS**：IPinfo 出口 23.169.184.26、Los Angeles、AS8796 |
| Windows 中国流量 | **PASS**：IP138 显示中国电信公网 IP |
| Windows OpenAI、Claude、Gemini 等各应用 | **未逐项回归测试**；不能仅凭 IPinfo 推断所有 AI 分类均命中 |
| iOS Shadowrocket 原有分流 | **PASS**：海外 IPinfo ZGO、中国 IP138 本地电信 |
| vnStat eth0 采样、JSON | **PASS**：systemd running、自动识别 eth0、实际有 RX/TX 数据 |
| 计费报告修正 | **PASS**：修正单位后本周期约 1.42 GB，而不是误报 146.26 GB |
| iPhone SSH 快捷指令 | **PASS**：关闭 Shadowrocket 时连接成功、脚本返回结果 |
| iPhone 文字换行 | **PASS**：改成「文本→快速查看」后用户确认 |
| DeepSeek IPv6 DIRECT Warn 完全排除 | **未验收**：只有日志和建议修改，无后续验证 |
| 多个完整账期精确对账 | **未验收**：原始 vnStat 与平台计费仍可能有单位/统计差异 |

## 1. 固定基线：本篇不再改 REALITY

| 项目 | 已核实的历史配置 |
| --- | --- |
| 供应商/型号 | ZgoCloud Los Angeles AMD/Intel VPS Starter |
| 套餐 | 1C / 2GB / 30GB NVMe / 300Mbps / 1024GB 每周期 |
| IP / OS / 网卡 | 23.169.184.26；Debian 12 Bookworm；eth0 |
| 服务端 | sing-box 1.13.19；VLESS + REALITY + xtls-rprx-vision，TCP 443 |
| REALITY handshake / SNI | **www.cloudflare.com**，Chrome 指纹；此前 Microsoft handshake 曾失败 |
| Windows | Clash Verge Rev 2.5.2；Mihomo；单份独立 Local YAML |
| iOS | Shadowrocket 2.2.90 (3378)，自带 default.conf；全局路由选择「配置」，不是全局「代理」 |
| 目标 | AI 固定 ZGO-LA；国内 DIRECT；普通海外主要用 ZGO；目前不做机场+VPS 双出口 |

当前 UUID 以 VPS /etc/sing-box/config.json 为准，Public Key/Short ID 需与服务器配置匹配，/root/reality-client.txt 是辅助客户端记录；历史示例不能当作实时有效凭据。

## 2. Windows Clash 规则方案的演化和取舍

### 2.1 借鉴 Shadowrocket default.conf，但不照抄数百条规则

原 iOS default.conf 的重要特性不是“国外一律代理”，而是以下顺序：**特殊海外服务代理 → 明确适合直连的国内/海外服务 DIRECT → LAN/CN 直连 → FINAL,PROXY**。Windows 最早增强版曾为 OpenAI、Claude、Google/YouTube、GitHub、Reddit、X、Telegram、Meta，以及各类中国站点、Apple、Microsoft、学术出版/软件下载手写几十到上百条 DOMAIN-SUFFIX/DOMAIN-KEYWORD。

这套规则已经体现需求，但有三个长期问题：手写 AI 域名易漏新域名；诸如 DOMAIN-KEYWORD,google、整个 microsoft.com/DIRECT、challenges.cloudflare.com/PROXY 等过宽规则易误伤；大量国内域名与 GEOSITE,CN 重复。

研究中参考了社区帖子与规则库：[linux.do AI 专用落地节点](https://linux.do/t/topic/2406439)、[sing-mix 简化规则和 DNS](https://linux.do/t/topic/1906273)、[AI 规则与 Clash Verge 扩展脚本](https://linux.do/t/topic/1516742)、[MetaCubeX meta-rules-dat](https://github.com/MetaCubeX/meta-rules-dat) 和 [Mihomo 配置文档](https://wiki.metacubex.one/)。论坛只是方案来源，仍以本地加载和实际分流验证为准。此时北京电信到 ZGO 的节点已稳定，**暂不做链式代理或复杂双出口**。

### 2.2 v2.1：减少手写规则，但首次导入失败

v2.1 将 AI 分流移至四个 MetaCubeX MRS rule-provider：openai、anthropic、google-gemini、category-ai-chat-!cn；把大量国内显式域名交给 GEOSITE,CN 和 GEOIP,CN，并使用较多 GEOSITE 服务分类。DNS 从简单 CN 国内解析/普通国外 DoH 扩展为 Fake-IP + respect-rules + direct-nameserver + proxy-server-nameserver。

用户导入后出现配置校验错误。截图只有 GeoSite 加载中间日志，没有最后 Fatal 诊断行。后续认为 category-ai-chat-!cn 文件名选择有问题，或个别 GeoSite tag 本地不可用，**但最终失败点并未通过完整 Fatal 日志唯一证实**。故只记录 v2.1 未通过，不能把推测写成已定位的单一根因。

### 2.3 v2.2-fixed：最后一次获得实测 PASS 的 Windows 基线

- 从四个 AI provider 减少为一个 MetaCubeX 的 **category-ai-!cn.mrs**，24 小时更新；
- 仍用 GEOSITE/google、youtube、github、twitter、telegram、facebook 和 CN；
- Reddit、Wikipedia、Discord、Dropbox、LinkedIn 等恢复显式 DOMAIN-SUFFIX，降低本地 GeoSite 分类依赖；
- Copilot 两个域名与 Hugging Face 在 AI/海外分类优先层；
- 不把整个 Microsoft / Apple 直接放行，DIRECT 保留较窄的 Windows Update、Apple CDN、AMD、JetBrains 等例外；
- 原有 VLESS/REALITY 443、SNI www.cloudflare.com、Chrome 指纹、Vision 不变；
- 最后以中国域名/IP DIRECT 和 MATCH,PROXY 兜底。

**实际路由树：**

~~~text
本机/LAN                          DIRECT
AI MRS + Copilot 补丁              PROXY → ZGO-LA
Google/YouTube/GitHub/X 等         PROXY → ZGO-LA
少量 Windows 更新/软件服务         DIRECT
DOMAIN-SUFFIX,cn + GEOSITE,CN      DIRECT
GEOIP,CN                           DIRECT
MATCH                              PROXY → ZGO-LA
~~~

实际配置取自[独立 YAML 归档](./2026-10-08-zgo-la-enhanced-v2.2-fixed.yaml)。其中的 DNS 主结构如下，**不是另一份要覆盖使用的完整文件**：

~~~yaml
ipv6: false
dns:
  enable: true
  ipv6: false
  enhanced-mode: fake-ip
  fake-ip-range: 198.18.0.1/16
  respect-rules: true
  nameserver:
    - https://1.1.1.1/dns-query
    - https://8.8.8.8/dns-query
  direct-nameserver:
    - https://dns.alidns.com/dns-query
    - https://doh.pub/dns-query
  proxy-server-nameserver:
    - 223.5.5.5
    - 119.29.29.29
~~~

用户随后报告 Windows 正常加载，IPinfo 为 ZGO 出口、IP138 为中国电信，**基础分流 PASS**。此前 iOS Shadowrocket default.conf 也做到了海外美国、国内电信两个出口，但 **iOS 和 Windows 并没有共享同一 YAML**。

### 2.4 8 月 24 日：DeepSeek IPv6 DIRECT 告警，仍是开放项

用户在 Mihomo Warn 中观察到：

~~~text
[TCP] dial DIRECT (match GeoSite/CN)
127.0.0.1:56928 --> hif-dliq.deepseek.com:443
dial tcp [2407:c080:802:1ce8:...]:443:
connectex: A socket operation was attempted to an unreachable network.
~~~

能确定的是：DeepSeek 域名命中 GEOSITE,CN 直连，底层拨号却拿到了 IPv6 目标，Windows 在当次网络环境无 IPv6 可达路由。**这不说明 ZGO-LA 的 REALITY 服务出错**。旧配置已有顶层 ipv6:false 及 dns.ipv6:false，因此可能涉及 DIRECT 解析、缓存或应用侧地址，不能单凭 Warn 确认 DNS 的唯一失误点。

历史对话曾建议将 nameserver 和 direct-nameserver 的 DoH URL 后加 DNS 选项 #disable-ipv6=true，并在 Clash Verge「订阅→编辑本地 YAML→保存/重启」应用。**用户没有提供已保存的修改内容和 Warn 消失的结果**，所以本次归档**明确仍保存原始 v2.2-fixed**，不混入未确认的 DNS 改法；日后应先核验 Mihomo 的有效配置、解析实际路径和核心版本。

## 3. 为什么不模拟机场订阅的套餐显示

Clash Verge 上机场显示“已用/总流量/到期日”，通常来自远程 HTTP 订阅响应提供的 subscription-userinfo metadata。当前 ZGO 是 Windows 本地 YAML，**并没有订阅服务器**。为一个人的单节点维护 HTTPS 订阅站点、认证、统计接口和更新服务，收益低于成本。

最终选择 **VPS 安装 vnStat → 脚本生成报告 → iPhone SSH 快捷指令读取**。不引入 Web 面板、新公网端口，不改 sing-box/REALITY，不需要登录网页后台查询每次用量。

## 4. ZgoCloud 流量计费口径：来自后台截图的判断

用户展示 ZgoCloud/VirtFusion 已登录页面：

| 字段 | 当时后台读数 |
| --- | --- |
| Inbound / DATA RECEIVED | 约 1.13～1.14 GB |
| Outbound / DATA TRANSMITTED | 约 141 MB |
| Total / Used | 约 1.27～1.28 GB |
| Total allowance | 1024 GB |
| 当期日期 | 2026-08-21 ～ 2026-09-20 |

从“合计≈入站+出站”，可以判断**后台此实例的用量展示为双向 RX+TX**，不应只拿 TX 或 VPS 下载量作为 1TB 套餐已用。一次代理下载在 VPS 视角通常同时产生网站→VPS 的 RX、VPS→客户端的 TX，单方向用户下载量可能接近两次计量。网卡还会统计系统更新等其他网络流量。

**时间必须按 21 日→次月 20 日切换，而不是自然月**；vnStat 自带 -m 不能直接代表当前计费周期。要以服务商页面为最终剩余额度依据。

## 5. Debian 12 安装 vnStat 2.10：已执行步骤与结果

用户通过 Windows PowerShell SSH root 登录 VPS，执行：

~~~bash
apt update && apt install -y vnstat
systemctl enable --now vnstat
systemctl status vnstat --no-pager
ip -br addr
vnstat
vnstat --json
~~~

实际安装包为 Debian 12 的 **vnstat 2.10-2**。systemd 显示 active (running)、enabled，启动日志显示自动添加接口 eth0：

~~~text
No interfaces found in database, adding available interfaces...
Interface "eth0" added with 1000 Mbit bandwidth limit.
Monitoring (1): eth0 (1000 Mbit)
~~~

eth0 的地址为 23.169.184.26/24。上面的 1000 Mbit 只是 vnStat 的监控配置限值，**不意味着 ZgoCloud 套餐从 300Mbps 升速**。

刚安装时提示 Not enough data available yet，JSON rx/tx 都为 0：这是正常的统计起点；vnStat 不能追溯安装前的流量。后来已采样：

~~~text
Database updated: 2026-08-23 11:35:00
eth0 since 2026-08-23
rx: 72.28 MiB
tx: 69.26 MiB
total: 141.54 MiB
~~~

常用查询：

~~~bash
vnstat            # 概览
vnstat -m         # 自然月，不等于套餐周期
vnstat -d         # 按日
vnstat -h         # 小时
vnstat -l         # 实时
vnstat --json     # 供程序读数
systemctl status vnstat --no-pager
~~~

## 6. zgo-traffic：两次问题与最后的脚本设计

### 6.1 SSH 中长 heredoc 粘贴损坏，改走 PowerShell scp

起初试图一次粘贴 cat > /usr/local/bin/zgo-traffic <<'EOF' ... EOF 长 Python 脚本，用户反馈尾部不正确。随后改成先在 Windows 下载脚本文件，再从 PowerShell 上传：

~~~powershell
scp "$HOME\Downloads\zgo-traffic-ios" root@23.169.184.26:/root/zgo-traffic-ios
ssh root@23.169.184.26
~~~

VPS 内执行：

~~~bash
mv /root/zgo-traffic-ios /usr/local/bin/zgo-traffic
chmod +x /usr/local/bin/zgo-traffic
zgo-traffic
~~~

历史文件先后为 zgo-traffic、zgo-traffic-v1.1、zgo-traffic-ios；**VPS 最终执行路径始终是 /usr/local/bin/zgo-traffic**。用户确认最后一版已正常执行。

### 6.2 单位 bug：JSON bytes 误作 KiB

首次 Python 脚本将 vnstat --json 的 rx/tx 当 KiB（除以 1024²），导致明显错误：

~~~text
错误结果：
RX 74.83 GB
TX 70.15 GB
历史修正 1.28 GB
已用 146.26 GB / 1024 GB
预计周期 1511.34 GB
~~~

与 vnStat 终端仅约 141 MiB 的观察矛盾。正确解释是 **vnStat JSON v2 rx/tx 的值是 bytes**。修正除以 **1024³** 后，用户实际输出：

~~~text
ZGO-LA 流量
状态：正常
计费周期：08/21 – 09/20
RX：0.076 GB
TX：0.069 GB
历史修正：1.28 GB
已用：1.42 GB / 1024 GB
剩余：1022.58 GB
使用率：0.14%
周期第 3/31 天
完整采样：0 天
预计周期：采样不足（至少 3 个完整统计日）
~~~

这个“GB”是**历史脚本打印标签**，但实际 bytes / 1024³ 严格说是 **GiB**，可能与商家后台的十进制 GB 产生偏差。初始 1.28GB 为安装前服务商页面的**近似手工补正**，仅用于 2026-08-21～09-20 周期，后续周期自动归零；脚本不访问 ZgoCloud 的官方实时 API。

随后也修复了短短数分钟数据就按整月线性预测、误提示超额的问题：至少需要 3 个先前采样日才显示预计周期（但见下方预测精度限制）。

### 6.3 最后一版专为 iPhone 竖向显示

用户希望手机弹窗清楚，最后将原本终端等宽排版改为：

~~~text
ZGO-LA 流量

🟢 正常

📅 计费周期
08/21 ～ 09/20
第 3 / 31 天

📊 本周期已用
1.45 GB / 1024 GB
0.14%

📥 接收
0.089 GB

📤 发送
0.071 GB

💾 剩余
1022.56 GB

📈 周期预测
采样不足
满 3 个完整统计日后开始预测
~~~

这里是当时接近最终结果的示例读数，不是 2026-10-08 实时读数。首周期 offset 仍参与计算，但在手机主界面隐藏。代码归档见 [zgo-traffic-ios.py](./2026-10-08-zgo-traffic-ios.py)。

## 7. iOS 快捷指令：连接失败和换行压扁怎么解决的

### 7.1 第一次 SSH 不通

新建快捷指令「ZGO 流量」，动作为：

- 「通过 SSH 运行脚本」：主机 23.169.184.26；端口 22；用户 root；当时选择密码认证；脚本内容只有 /usr/local/bin/zgo-traffic。
- 「显示结果」：显示上一步 Shell 脚本结果。

起初提示无法与 SSH 服务器连接；而 Windows PowerShell 的 SSH 可正常登陆。**关闭 Shadowrocket 后，用户随后确认快捷指令成功执行**，故存在 Shadowrocket 分流/转发影响 VPS 自身 SSH 的可能。

曾建议为 VPS 的 23.169.184.26/32 添加 DIRECT 例外以避开潜在回环，**用户决定暂不动规则**。所以不能把“已经在 Shadowrocket 和 Clash 加了 DIRECT 例外”写成事实；也不能仅凭关 Shadowrocket 后成功，就断言代理回环已经严格证明。

### 7.2 第二次问题：脚本有换行，但「显示结果」显示为一大段

最初即使服务器端改成手机竖向输出，iOS 的「显示结果」仍把多行压扁。实际解决来自**替换快捷指令输出动作**：

~~~text
① 通过 SSH 运行脚本
   /usr/local/bin/zgo-traffic
            ↓
② 文本
   插入动态变量「Shell脚本结果」，不打额外文字
            ↓
③ 快速查看（Quick Look）
   输入选上一步「文本」
~~~

用户最后截图显示各段正确分行并明确回复“好了” —— **这一流程有实际成功证据**。可以选择另加主屏幕图标，但没有已添加的确认材料。

### 7.3 安全方面没有强行扩展

虽然查的是流量、没有敏感业务内容，快捷指令**root 密码认证仍属于 VPS 最高权限凭据**。曾讨论使用 SSH Key，用户选择暂不做，因此当时**没有完成 SSH Key、禁密码登录、非 root 只读账号等安全加固**。这是已知安全欠账，不能把它说成完成项。VPS 管理口 22 在此前就已存在，没有因流量监测新增公网服务端口。

## 8. 维护与恢复

**Windows Clash**：在 Clash Verge「订阅」找到本地 v2.2-fixed，编辑/启用 YAML。正式部署时以当前 VPS 参数填充去密归档里的 UUID、Public Key、Short ID，**切勿将实际值提交到公开 GitHub**。仍保持 REALITY SNI www.cloudflare.com。验证顺序：配置能加载 → provider/GeoSite 正常 → IPinfo 美国 VPS → IP138 国内电信 → AI 应用与 DNS 实际行为。不能仅凭成功导入宣称 AI 所有域名都正确分流。

**VPS**：

~~~bash
vnstat
vnstat --json
zgo-traffic
systemctl status vnstat --no-pager
~~~

如需从本仓库脚本恢复，将 [Python 归档](./2026-10-08-zgo-traffic-ios.py) 先上传 VPS，例如 /root/zgo-traffic-ios.py，然后执行：

~~~bash
install -m 755 /root/zgo-traffic-ios.py /usr/local/bin/zgo-traffic
zgo-traffic
~~~

**iPhone**：保持 SSH 脚本动作 → 文本动态变量 → 快速查看。连接失败应先记录 Shadowrocket 开关与连接网络状态，再分析路由/22 端口/SSH 认证，不要因此修改已验证工作的 REALITY 密钥。

## 9. 限制与未决事项

1. **首次账期只是近似**：vnStat 从 8/23 11:27 开始计量，8/21～当时的 1.28GB 仅据 ZgoCloud 后台作 offset。下个周期才有望完整覆盖。
2. **GiB vs GB**：代码把 bytes/1024³ 的结果标作 GB，1024GB 总量亦未证明与商家单位精确一致；对账应先统一单位和更新时间。
3. **vnStat 每日记录保留期**：脚本逐日累加 21→次月20，最长需要覆盖 **31 天**；应检查 vnStat 日历史保留数量，确保至少超过最长周期，最好设 60～90 天。未验证就不要断言月末完全不丢历史日。
4. **预测样本不足**：虽加“三个完整日”门槛，脚本实际按“日期早于今天的采样天数”计算，首次采样日可能不是全天。因此预计周期只是参考，不是严格的官方额度预测。
5. **后台并非脚本实时数据源**：vnStat 监控整张 eth0，含代理及其他网络使用；不能借此分解 YouTube 或 AI 单应用流量。
6. **DeepSeek IPv6 Warn**：8/24 DNS 调整是建议而非已完成修复，归档中没有采用；遇同样日志需先看实际生效配置与 DNS/IPv6 链路。
7. **SSH/风控**：root 密码登录、控制台 2FA、SSH Key、IPQS 与 AI 平台长期风控表现皆非本次监测功能的已验证成果。
8. **未来第二出口**：仅在观察完整计费周期，证实 YouTube/普通海外业务让 1TB 不够后，再考虑 AI→ZGO、其他海外→旧机场；目前不需要。

## 10. 时间线

| 时间（北京时间） | 过程与结果 |
| --- | --- |
| 2026-08-23 | 对照 Shadowrocket default.conf、linux.do，提出 v2.1 精简配置 |
| 2026-08-23 | v2.1 在 Windows 导入失败；最后 Fatal 内容未保留 |
| 2026-08-23 | v2.2-fixed 收为单 AI MRS、减少 GeoSite tag 风险 |
| 2026-08-23 | Windows 配置通过；IPinfo ZGO 美国、IP138 电信直连 **PASS** |
| 2026-08-23 | ZgoCloud 面板见 RX+TX、1024GB、21→20 账期 |
| 2026-08-23 11:27 | Debian 安装 vnStat 2.10-2，自动监测 eth0 |
| 2026-08-23 11:35 | vnStat 已有 141.54 MiB 双向采样 |
| 2026-08-23 | 长 here-doc 粘贴损坏，改用 PowerShell scp 上传 Python |
| 2026-08-23 | Python 首版把 bytes 当 KiB：误报 146.26GB，改正后约 1.42GB |
| 2026-08-23 | iOS 快捷指令 SSH 首次失败，关闭 Shadowrocket 后成功 |
| 2026-08-23 | 输出经「文本→快速查看」恢复分行，用户确认完成 |
| 2026-08-24 | DeepSeek DIRECT IPv6 unreachable Warn，提出 DNS 修正但无后续实测 |
| 2026-10-08 | 新笔记、v2.2-fixed YAML 与 iOS Python 脚本各自独立落盘，历史归档 |

## Revision log

- 2026-10-08：首次独立整理后续 Windows 规则优化及手机流量监测的过程、结果与未验证边界；原初始化笔记不改。
