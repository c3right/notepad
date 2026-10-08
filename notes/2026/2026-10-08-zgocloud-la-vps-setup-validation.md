---
title: "ZgoCloud 洛杉矶 $18/季度 VPS：选购、线路与 IP 质量检测、sing-box REALITY 部署排障、双端分流全记录"
date: 2026-10-08
updated: 2026-10-08
status: evergreen
type: reference
topics:
  - vps
  - network-proxy
  - self-hosting
  - ip-reputation
  - troubleshooting
keywords:
  - ZgoCloud
  - Los Angeles
  - Beijing Telecom
  - sing-box
  - VLESS
  - REALITY
  - XTLS Vision
  - Clash Verge Rev
  - Mihomo
  - Shadowrocket
source: "2026-08-21 至 2026-08-23 ChatGPT 对话中的用户实测、后台截图与命令输出；2026-10-08 整理；sing-box GitHub Issue #4290"
language: zh-CN
---

# ZgoCloud 洛杉矶 $18/季度 VPS：选购、检测、配置与排障全记录

> **历史复盘**：操作发生于 **2026-08-21～23（北京时间）**，整理于 2026-10-08。以下“已通过”指当时留下了对应测试输出，不表示在整理日重新检测。**仓库为公开仓库**：不保存真实 UUID、REALITY Private Key、密码、SSH 私钥或订阅凭据。公网 IP 和安装路径为用户要求保留的运维事实。

## 一句话结论

购买并配置了一台 ZgoCloud **洛杉矶 AMD/Intel VPS Starter（USD 18/季度）**，通过北京电信连接，部署 `sing-box 1.13.19` 的 **VLESS + REALITY + XTLS Vision / TCP 443**。节点的**服务端本机完整代理闭环**与**iOS Shadowrocket 实际海外出口**均通过；国内访问 IP138 显示电信，国外访问 IPinfo 显示 `23.169.184.26`。最关键的排障发现是：**`www.microsoft.com` 不能作为此次 sing-box REALITY 的有效握手目标，换成 `www.cloudflare.com` 后立即成功**；不是反复更换 UUID/密钥解决的。

## 1. 设备、费用与当前配置基线

| 项目 | 2026-08 实测/后台记录 |
| --- | --- |
| 供应商 | ZgoCloud |
| 产品 | **Los Angeles AMD/Intel VPS — Starter**（LA 9929 & CMIN2 中国优化线路；不要与同时看过的 `Los Angeles AMD ISP VPS — Specials — Starter` 混淆） |
| 价格 | **USD 18 / 季度**，折合 USD 6/月；此为下单时看到的价格，不保证后续新购或续费相同 |
| 资源 | 1 vCPU、2 GB RAM、30 GB NVMe |
| 带宽/流量 | 标称 **300 Mbps；1024 GB/月（约 1 TB）**，后台展示入站+出站共同计量 |
| 公网 IPv4 | `23.169.184.26`，网关 `23.169.184.1`，地址段 `23.169.184.0/24` |
| VPS 主机名 | `ai-la-01` |
| OS/虚拟化 | Debian GNU/Linux 12 Bookworm，x86_64，KVM/QEMU |
| 当时内核 | `6.1.0-52-amd64` |
| 服务端 | `sing-box 1.13.19`，systemd 服务名 `sing-box` |
| 协议 | VLESS + REALITY + `xtls-rprx-vision`，TCP 443 |
| **已验证的 REALITY SNI/handshake** | **`www.cloudflare.com:443`**（切勿回退到 `www.microsoft.com`） |
| Client Hello 指纹 | Chrome |
| VPS 时区 | `Asia/Shanghai`；NTP 同步已验证 |
| Windows 客户端 | Clash Verge Rev **2.5.2** / Mihomo；本地 YAML 文件方式 |
| iOS 客户端 | Shadowrocket **2.2.90 (3378)** / iOS 26.5；默认配置分流 |
| 使用目标 | AI（ChatGPT、Claude、Gemini 等）、YouTube 与常用受限海外网站走 Zgo；国内与明确可直连的网站 DIRECT；暂不混合其他机场自动选路 |

**身份参数的唯一真值位置（不得把实际值提交公共 Git 仓库）**：

- `/etc/sing-box/config.json`：当前 VLESS 用户 UUID、REALITY Private Key、监听与握手参数。
- `/root/reality-client.txt`：当时手动保留的 **Public Key / Short ID / SNI / Flow** 客户端参数备忘（建议权限 `600`）。这份文件是**辅助记录**，以后若修改服务端配置必须同时更新；不是自动生成的权威源。
- Windows 本机 `zgo-ai-la.yaml` 和 iOS 的 ZGO-LA 节点保存相应客户端字段。

## 2. 为什么购买这款，而不是其他候选

目标是为固定 AI 账号寻找**长期不变的美国出口**，优先考虑北京电信到美国的可用性、IP 信誉与维护成本，而不是指纹浏览器或多账号隔离。曾比较 Zgo 的 TRI、ISP Specials、云悠 4837 ISP 等：部分候选缺货，部分虽然名称包含 “ISP / 双 ISP”，但商品说明指出 IP 仍托管在数据中心、不同风控数据库识别不一致、可能存在地理定位漂移，甚至明确不支持因该类因素退款。不能把商品标题里的“ISP”直接理解为家庭住宅出口。

实际选择的 **$18/季度 LA AMD/Intel VPS Starter** 与当时看到的 **$58/年 LA AMD ISP Specials Starter** 是**不同系列**，后者页面示例为 1 GB RAM、10 GB NVMe、500 GB/月，不应混记为本机配置。最终以购买后 VirtFusion 后台的 **2 GB / 30 GB / 1024 GB / 300 Mbps** 为准。

## 3. 初始化与基础连通性（2026-08-21～22）

### 3.1 VirtFusion 初始化

后台初见状态 `Awaiting Setup`，建机时选择 **Debian 12 (Bookworm) Minimal**，主机名 `ai-la-01`，Swap **512 MB**；管理员首次采用密码登录，未预置 SSH Key。随后后台状态变为 `RUNNING`，安装任务 `Build 100% COMPLETE`。机型页显示公网 IPv4、300 Mbps 速率、1024 GB 配额及入/出站统计。后台 DNS resolver 展示为 `1.1.1.1` 与 `8.8.8.8`。

**安全欠账**：当时账户页截图显示 Two-factor Authentication 为 OFF；这是**2026-08 历史状态**，是否后来开启未知。初始 root 密码 SSH 登录成功，应优先改为 SSH 公钥认证，确认可用后再禁用密码登录；VPS 控制台也应启用 2FA。**不要为了加固在尚无 SSH Key 的情况下直接禁用密码登录**，以免锁死。

### 3.2 Windows（北京电信）至 VPS

早期四包 ping 平均约 **152 ms**，随后 100 包长测的原始统计：

~~~text
ping -n 100 23.169.184.26
Packets: Sent=100, Received=100, Lost=0 (0%)
Minimum=152ms, Maximum=211ms, Average=156ms
~~~

长测多数样本落在 **152～159 ms**，少量短时突发到 170～211 ms。只能代表该时间窗口的 ICMP 表现，**不能由此保证所有晚高峰、TCP/UDP、持续大流量都一样稳定**。

`tracert 23.169.184.26` 的去程看见 `202.97.42.6`、多个 `59.43.*` 地址（电信 CN2 相关路由特征），第 14 跳到达目标，目标延迟约 152 ms。部分中间跳 `*` 超时属于路由设备不回应探测的常见情况，**不能直接视为端到端丢包**。

服务端 `traceroute -n 202.97.42.6` 返回方向曾见 `210.14.*`、`218.105.*`、`210.78.*`、`202.97.*`，呈现经联通精品网/9929 相关地址段、再接电信的迹象。因此当时概括为**去程疑似 CN2、回程疑似经 9929 后进电信**；这是单次 traceroute 的**线路推断**，不是完整时段 SLA 或逐跳运营商归属的严格证明。

### 3.3 SSH 与系统状态

Windows PowerShell 首次访问：

~~~powershell
ssh root@23.169.184.26
~~~

曾出现正常的首次 SSH host-key 信任提示，并以密码登录成功。首次出现的新主机指纹应与控制台可信信息核验后接受；当时接受动作本身不代表已经做过独立带外核验。

核实命令（仅供以后复检）：

~~~bash
hostnamectl
cat /etc/os-release
ip -br addr
ip route
timedatectl
~~~

历史结果：`eth0` 为 `23.169.184.26/24`，默认路由 `via 23.169.184.1`，Debian 12 / KVM。最初未安装 `curl`，后来已能使用；确切安装命令在保留记录中缺失，**不补造操作历史**。

系统曾先显示 `System clock synchronized: no`、`NTP service: n/a`；处理后显示 `System clock synchronized: yes`、`NTP service: active`，时间区为 `Asia/Shanghai`。REALITY 连接涉及时间窗口检查，应保持时间准确；无需为了“假装美国机器”强行把服务器系统时区改成洛杉矶。

## 4. VPS 所在地、出口链路、AI 网站响应检测

### 4.1 IP 归属数据库

从 VPS 自己执行：

~~~bash
curl -4 ipinfo.io
curl -4 https://ifconfig.co/json
~~~

两者都返回公网 IP `23.169.184.26`，国家 US，城市 Los Angeles，ASN **AS8796**；IPinfo 的组织字段为 **FASTNET DATA INC**，公司/资源主体的其他数据库记录涉及 **NexusWave Technologies LLC**。历史响应的定位坐标约 `34.0522,-118.2437`，属数据库代表坐标，**并非物理机柜地址**。

### 4.2 直接网络和 TLS 排查

先从 VPS 直接访问多个可用的 HTTPS 目标：

~~~bash
for host in www.microsoft.com www.apple.com www.cloudflare.com; do
  echo "===== $host ====="
  curl -o /dev/null -sS \
    -w 'HTTP=%{http_code} CONNECT=%{time_connect}s TLS=%{time_appconnect}s TOTAL=%{time_total}s\n' \
    "https://$host/"
done
~~~

三站当时 `HTTP=200`；TCP 建连约 4～8ms，TLS 建立约 40～52ms；`openssl s_client -tls1_3` 也显示 TLS 1.3 与 `Verify return code: 0 (ok)`。**但普通 TLS 正常不意味着域名适合作为 REALITY handshake destination**（见第 6 节）。

直接 `curl -I` 三个 AI 站点的历史结果：

| 目标 | HTTP | 正确解释 |
| --- | --- | --- |
| `chatgpt.com` | 403；`cf-mitigated: challenge` | Cloudflare 对 CLI 请求的挑战，**不能据此判定 VPS IP 被 OpenAI 封锁** |
| `claude.ai` | 403；`cf-mitigated: challenge` | 同样是 CLI 被挑战，**不能据此推导浏览器是否能正常登录** |
| `gemini.google.com` | 200 | 首页 HEAD 请求正常，但**不等于已验证登录、模型推理及付费功能** |

这里只证明 VPS 到目标站的部分应用层连通性，不能作为所有 AI 账号长期不触发风控的保证。

## 5. sing-box 服务端部署的已证实过程

初次检查：

~~~text
sing-box version 1.13.19
systemctl status sing-box
Active: inactive (dead)
Loaded: ... disabled
~~~

`sing-box 1.13.19` 已安装，但服务尚未启用。初始 `ss -lntup | grep ':443'` 无输出。配置文件通过 Bash heredoc 粘贴时曾出现 **`EOF } "tag": "direct"` 一类错乱**，属于终端长文本粘贴损坏；随后修正后通过：

~~~bash
sing-box check -c /etc/sing-box/config.json
echo "EXIT=$?"           # 观察到 EXIT=0
systemctl enable --now sing-box
systemctl status sing-box --no-pager
ss -lntp | grep ':443'
~~~

当时回显 `Active: active (running)`，且 `inbound/vless[vless-reality-in]: tcp server started at [::]:443`；`ss` 确认 sing-box 在 TCP 443 监听。**内核启动 / 端口监听只是第一关，不能证明 REALITY 握手成功。**

### 5.1 服务端有效配置结构（去密示意）

以下是复现结构，不是原样备份；具体 UUID、私钥、Short ID 应从**当前 VPS 真值**读取：

~~~json
{
  "inbounds": [
    {
      "type": "vless",
      "tag": "vless-reality-in",
      "listen": "::",
      "listen_port": 443,
      "users": [
        {
          "name": "ai-main",
          "uuid": "<CURRENT_UUID>",
          "flow": "xtls-rprx-vision"
        }
      ],
      "tls": {
        "enabled": true,
        "server_name": "www.cloudflare.com",
        "reality": {
          "enabled": true,
          "handshake": {
            "server": "www.cloudflare.com",
            "server_port": 443
          },
          "private_key": "<CURRENT_PRIVATE_KEY>",
          "short_id": ["<CURRENT_SHORT_ID>"]
        }
      }
    }
  ],
  "outbounds": [
    { "type": "direct", "tag": "direct" }
  ]
}
~~~

原安装配置是否含其他字段（如 `max_time_difference`），以实际磁盘文件为准，不能把上述简化结构当作逐字备份。服务端自身对外继续 `direct` 是正常的：客户端→VPS 为加密代理隧道；VPS→目标网站则按服务器直出。

### 5.2 身份材料的变更历史和纪律

调试过程中发现早先在聊天中贴过 UUID，因此发生过**VLESS UUID 轮换**；随后误将旧客户端 Public Key/Short ID 与服务端更新后的值混淆，排查时又发生过多次 REALITY key pair 与 Short ID 轮换。**这些轮换最终并非故障根因**，但它们制造了“客户端与服务端当前值不一致”的额外变量。

正确运维原则：

1. 以**当前运行中的** `/etc/sing-box/config.json` 为准，记录每次 key/UUID 轮换的时间与相应客户端更新。
2. Private Key、UUID、密码不进公开仓库或聊天；Public Key/Short ID 虽为客户端必要配置，也避免在公开笔记里写入可直接连接的完整凭据组合。
3. 更换 REALITY key pair 必须配套更新客户端 Public Key；更换 Short ID 必须配套更新客户端；更换 UUID 必须配套更新所有 VLESS 客户端。
4. 有条件时先备份配置、检查 JSON/`sing-box check`，确认成功再重启；失败时保留可回滚版本。**不要把随机换 Key 当成首选排障办法**。
5. 保持 `/root/reality-client.txt` 与服务端同步，建议权限 `chmod 600`。

## 6. 最关键的排障：REALITY “invalid connection”

### 6.1 初始现象

Windows Clash Verge Rev 能加载 VLESS 节点，但延迟测试显示 **Timeout**。VPS `journalctl -u sing-box -f` 每次测试都出现（简化）：

~~~text
inbound/vless[vless-reality-in]: inbound connection from <client-ip>:<port>
TLS handshake: REALITY: processed invalid connection
~~~

明确说明：**客户端 TCP 已到达 VPS 的 443**，但 REALITY TLS 握手被拒；当时尚不能凭此证明一定是 UUID、密钥或地理网络问题。iOS 手工配置 Shadowrocket 后，偶尔能返回节点“测速延迟”，Google 网页仍打不开；仅 TCP 延迟有数字不是成功代理出网的证据。

被逐项核对的参数：`443`、`tls.server_name`、`reality.handshake`、`short_id`、`flow: xtls-rprx-vision`、Chrome 指纹、客户端 Public Key/Short ID、UUID、NTP。早先服务端 handshake/SNI 是 `www.microsoft.com`。

### 6.2 做决定性 sing-box→sing-box 闭环

为排除 Windows/iOS 客户端差异，在 VPS 另启**临时** sing-box SOCKS 入口 `127.0.0.1:10808`，出站直接用 VLESS + REALITY 访问本机 `127.0.0.1:443`。客户端配置引用当前 UUID、`/root/reality-client.txt` 中 Public Key/Short ID，TLS uTLS Chrome；配置检查 `EXIT=0`、SOCKS 监听成功。

首次测试：

~~~bash
curl --socks5-hostname 127.0.0.1:10808 -4 https://ipinfo.io
# curl: (97) Can't complete SOCKS5 connection ... (1)
~~~

临时客户端 `outbound/vless` 报 `EOF`；**同机服务端仍报 `REALITY: processed invalid connection`**。由此排除“只因为 Windows Clash 某个 UI/测速选项”这一解释，也说明基础网络不是该轮故障的决定因素。

### 6.3 查到特定实现兼容问题并只更换 handshake/SNI

sing-box 上游 Issue **[#4290](https://github.com/SagerNet/sing-box/issues/4290)** 记录：部分目标站点的 TLS ServerHello 带 `supported_groups` 扩展，会导致 REALITY inbound 拒绝连接，包含 CDN 背后的 `www.microsoft.com`；Issue 给出的可行替代目标包括 `www.cloudflare.com`。

这与**同机测试 + 微秒/毫秒级握手失败 + Microsoft 目标**的组合高度吻合。修复仅把服务端：

~~~text
tls.server_name                  = www.cloudflare.com
tls.reality.handshake.server     = www.cloudflare.com
tls.reality.handshake.server_port= 443
~~~

以及测试客户端的 `tls.server_name` 改为 `www.cloudflare.com`；**不再轮换 UUID、Private/Public Key 或 Short ID**。完成 `sing-box check` 与 `systemctl restart sing-box`，重新跑同机闭环：

~~~bash
curl --socks5-hostname 127.0.0.1:10808 -4 https://ipinfo.io
~~~

**成功返回**：

~~~json
{
  "ip": "23.169.184.26",
  "city": "Los Angeles",
  "region": "California",
  "country": "US",
  "org": "AS8796 FASTNET DATA INC"
}
~~~

VPS 日志出现：

~~~text
inbound/vless[vless-reality-in]: [ai-main] inbound connection to ipinfo.io:443
outbound/direct[direct]: outbound connection to ipinfo.io:443
~~~

**这是核心 PASS 证据**：REALITY TLS 握手、VLESS 用户认证、代理转发和 VPS 出口均成立。正式节点保留 `www.cloudflare.com`；临时测试进程应关闭，确认 10808 不再监听（测试配置可以安全保存供以后使用，限制访问权限）。

> **复盘教训**：普通 `curl` / `openssl` 对 `www.microsoft.com` TLS 1.3 成功，不能推出它适合作 REALITY 伪装目标；最初多次轮换 Key 也不是必要修复。首次配置最好先做一次“sing-box→sing-box 本机闭环”作为服务端基准。

## 7. 客户端配置与实际验证

### 7.1 Windows：Clash Verge Rev 2.5.2 / Mihomo

建立**Local（本地）**配置，而不是 Remote（要求订阅 URL）。在 Windows 上新建 `zgo-ai-la.yaml` → Clash Verge 的“订阅 → 新建 → 类型 Local → 选择文件”，导入为独立 `ZGO-LA` 配置，原 SnailLink/悠兔等订阅不必修改。

下面是**去密、可用作重新部署模板的核心 YAML**；填入的值必须与**现在**的服务端一致，不能直接用旧对话凭据。其分流结构是经过讨论后的推荐设计，**完整增强版 Windows YAML 在本轮保留的证据中尚没有成功上线/全面测试记录**：

~~~yaml
mixed-port: 7890
allow-lan: false
mode: rule
log-level: info
ipv6: false

proxies:
  - name: ZGO-LA
    type: vless
    server: 23.169.184.26
    port: 443
    uuid: "REPLACE_WITH_CURRENT_UUID"
    network: tcp
    udp: true
    tls: true
    flow: xtls-rprx-vision
    encryption: ""
    servername: www.cloudflare.com
    client-fingerprint: chrome
    reality-opts:
      public-key: "REPLACE_WITH_CURRENT_PUBLIC_KEY"
      short-id: "REPLACE_WITH_CURRENT_SHORT_ID"

proxy-groups:
  - name: PROXY
    type: select
    proxies:
      - ZGO-LA
      - DIRECT

rules:
  - DOMAIN-SUFFIX,local,DIRECT
  - IP-CIDR,10.0.0.0/8,DIRECT,no-resolve
  - IP-CIDR,100.64.0.0/10,DIRECT,no-resolve
  - IP-CIDR,127.0.0.0/8,DIRECT,no-resolve
  - IP-CIDR,172.16.0.0/12,DIRECT,no-resolve
  - IP-CIDR,192.168.0.0/16,DIRECT,no-resolve

  # 如果部署 GEO 规则，需确保当前 Mihomo 有可用的 geosite/geoip 数据。
  - DOMAIN-SUFFIX,cn,DIRECT
  - GEOSITE,CN,DIRECT
  - GEOIP,CN,DIRECT

  - MATCH,PROXY
~~~

这段**不包含完整 DNS 覆写**：真实 DNS 策略还受 Clash Verge 的全局配置、TUN、系统代理、Mihomo Geo 数据可用性、规则顺序影响。历史讨论曾给出 `fake-ip`、国内 AliDNS/腾讯 DNS、海外 Cloudflare/Google DoH 与 `nameserver-policy: geosite:cn` 的增强方案；但没有保留其上线验证结果，**不把建议说成已验证稳定配置**。亦应避免直接把 fake-ip 网段 `198.18.0.0/16` 加成强制 DIRECT 的过宽规则。

后续希望精细化时，沿用如下**优先级**：

1. 必要代理的 AI（OpenAI / Claude / Gemini / Copilot）与常见受限站点（Google / YouTube / X / Reddit 等）→ ZGO-LA；
2. 局域网、国内及**实测可直连**的部分海外网站（Microsoft 常规服务、部分学术出版站点等）→ DIRECT；
3. `GEOSITE,CN,DIRECT`、`GEOIP,CN,DIRECT` 兜底；
4. `MATCH,PROXY`，未知流量走 ZGO；
5. 后续有流量压力时才添加“AI 固定 ZGO，其余国外走机场”的第二出口。

规则**先后顺序重要**：例如 `copilot.microsoft.com` 的显式代理规则必须放在宽泛的 `microsoft.com,DIRECT` 前面。对“明确海外但直连”的清单，不能仅依据历史规则而永远假定可达。

**验收边界**：Windows 曾在 Microsoft SNI 下加载成功但 Reality 延迟 Timeout；Cloudflare SNI 修复后的 Windows 真实网页分流没有出现在保留的最终测试中，因此状态是**待客户端回归验证**，不可宣称 Windows 已最终 PASS。

### 7.2 iOS：Shadowrocket 2.2.90（3378）

在“添加节点”选择 VLESS：

| 字段 | 设定 |
| --- | --- |
| 地址/端口 | `23.169.184.26:443` |
| UUID | 当前服务器 UUID（不外传） |
| 加密 | 空 / none |
| 流控 | `xtls-rprx-vision` |
| 传输方式 | **`none`：该 App 界面解释为普通 TCP**，并非“没有传输” |
| TLS | 开启；允许不安全关闭 |
| SNI | **`www.cloudflare.com`** |
| Public Key / Short ID | 从当前 `/root/reality-client.txt` 核对 |
| 指纹 | Chrome |
| 多路复用 / TCP 快速打开 | 暂时关闭 |

改好 Cloudflare SNI 后，iPhone **实际代理访问成功**；节点列表曾显示约 **165 ms** 的延迟，但最终判断依据是实际出口，而不是单个延迟数字。

Shadowrocket 首页选中 **ZGO-LA**，**“全局路由”选“配置”而不是“代理”**；后者会让所有请求走美国。配置页选中 App 自带 `default.conf`（当时约 106.5 KB，数百条分流规则）；这并非我们新建的专用配置。所见尾部关键规则为：

~~~ini
# LAN
IP-CIDR,192.168.0.0/16,DIRECT
IP-CIDR,10.0.0.0/8,DIRECT
IP-CIDR,172.16.0.0/12,DIRECT
IP-CIDR,127.0.0.0/8,DIRECT

# China
GEOIP,CN,DIRECT

# Final
FINAL,PROXY
~~~

前面还包含大量 **已知需代理服务 PROXY** 与 **部分可直连海外网站 DIRECT**，不是“国外一律代理”。文件随 App 版本/默认配置机制变化，但不应假定它是每天自动在线更新的 GEO 清单。Windows 可借鉴其**“强制代理 → 显式直连 → CN 兜底 → 未知代理”**思路，不必机械复制几百条规则。

**已观察的 iOS 分流验收**：

| 测试 | 结果 |
| --- | --- |
| Safari/网页访问 `ipinfo.io` | 出口 **23.169.184.26**，Los Angeles / US |
| Safari 访问国内 `IP138` | 显示**中国电信 IP**，而非 Zgo 公网 IP |
| 结论 | 该时刻 iOS 的“国内 DIRECT / 海外 PROXY”两条链路都有证据 |

上述不是对所有国内/海外域名逐个验证；个别 DNS、CDN、企业网络、IPv6、QUIC 路径可能不同。

## 8. IP 质量与风险画像（2026-08-23 用户浏览器实测）

| 数据源 / 检查项 | 当时结果 | 限制 |
| --- | --- | --- |
| IPinfo | IP `23.169.184.26`，US / Los Angeles；`AS8796 FASTNET DATA INC`；`AS Type: ISP`；`Privacy: false`；Hosted domains 0 | “Privacy=false”仅代表该库没有触发对应标记，**不保证所有风控平台看不到 VPS/Proxy** |
| AbuseIPDB | **0 次报告；Abuse Confidence 0%**；资源主体 NexusWave Technologies LLC；Usage Type **Fixed Line ISP** | 无举报≠永远无滥用；数据库覆盖有限 |
| Scamalytics | **Low Risk；Fraud Score 0/100** | 文字明确称 **commercial server**、不是普通家庭连接；还说明**对本 IP 直接流量缺少可见性**，0 分部分基于相关网络的整体画像，不能夸大为独立实测零风险 |
| BrowserLeaks | HTTP 访问 IP 一致；IPv6 未检测到；WebRTC local/public 显示 n/a；Tor Relay 否；Usage Type Corporate/Business | “WebRTC n/a”只说明**该次浏览器测试未观察到泄漏**，不代表任何 App 或网络都绝不泄漏 |
| 地理库差异 | 多数为 Los Angeles；BrowserLeaks 曾示 Colorado/Boulder / America/Denver | 资源持有人注册地址/数据库映射可能不同；**不能据此断言物理服务器挪机房** |

**综合评价**：以 2026-08 的材料，适合**继续作为固定自用美国出口试用**，风险指标优于常见被大量滥用的代理，但“**信誉初看低风险**”与“**原生/住宅 IP**”是不同命题。此前聊天中的 **A-/A** 属于定性主观等级，**不是任何检测机构颁发的认证等级**。IPQualityScore（IPQS）当时尚无结果，OpenAI/Anthropic 账号长期使用风控表现也无长期观察材料。尽量保持单账号出口稳定，避免不必要的频繁换 IP。

## 9. 可直接复用的检查与维护命令

### 9.1 常规状态（不泄密）

~~~bash
hostnamectl
timedatectl
systemctl is-active sing-box
systemctl is-enabled sing-box
sing-box version
sing-box check -c /etc/sing-box/config.json
ss -lntp | grep ':443'
journalctl -u sing-box -n 50 --no-pager
curl -4 ipinfo.io
~~~

公网入口可复检 `23.169.184.26:443` TCP 可达；但**端口通不等于业务可用**。真正业务验证需通过客户端代理访问外网、与服务器日志对照。

### 9.2 最小化查看配置（不显示密钥）

~~~bash
python3 - <<'PY'
import json
with open("/etc/sing-box/config.json") as f:
    c=json.load(f)
i=c["inbounds"][0]
t=i["tls"]
r=t["reality"]
print("type:", i.get("type"))
print("port:", i.get("listen_port"))
print("server_name:", t.get("server_name"))
print("handshake:", r.get("handshake"))
print("short_id_count:", len(r.get("short_id", [])))
print("user_count:", len(i.get("users", [])))
PY
~~~

不要把完整 `/etc/sing-box/config.json` 原样提交 GitHub、分享给第三方或放进无脱敏日志。若确实要读取当前客户端 Public Key/Short ID，在**可信的个人终端**执行 `cat /root/reality-client.txt`，不要粘贴全部内容到公开仓库。

### 9.3 真正的端到端验收

1. 服务端 `systemctl status sing-box` 为运行，`sing-box check` 为成功；
2. 在可信客户端发起 VLESS/REALITY 请求，VPS 日志从“inbound connection”继续到 “inbound connection to <target>” / “outbound/direct”；
3. 通过代理访问 `https://ipinfo.io`，必须显示 `23.169.184.26`；iOS 国内站点同时应能验证 DIRECT；
4. 检查 ChatGPT/Claude/Gemini 真正网页或 App 使用是否正常；`curl -I` 的 Cloudflare 403 不是充分的封禁证据；
5. 测试 DNS/WebRTC/IPv6 泄漏、流量用量、较长时间多时段可用性。必要时重做低风险的同机 SOCKS 闭环。

## 10. 仍待完成或长期观察的事项

- **账号与系统加固**：确认 VPS 控制台 2FA，创建和测试 SSH Key，禁用 root 密码认证之前先保留可用回滚/控制台通道；按需做防火墙和自动更新策略。此处是建议，不能记成已执行。
- **Windows 验收**：Cloudflare SNI 修改后的 Clash Verge Rev 实际联网、DNS 分流、Geo 数据与系统代理/TUN 路径未留最终 PASS 证据。
- **AI 风控**：只能说节点能与目标网络通信；ChatGPT/Claude 长期登录/授权、Google 账号区域与 CAPTCHA 表现需使用观察，不靠一次数据库评分保证。
- **安全与数据**：VPS 每月 **1024 GB**、入站与出站合计计量；YouTube 和大文件下载可能显著消耗配额，观察 1～2 个完整计费周期后再决定是否与原机场双出口分流。
- **IP 质量更新**：IPQS 尚未测出最终值；AbuseIPDB/Scamalytics/IPinfo 随时间可能变化，若发生挑战增多可重新复核。
- **规则维护**：Shadowrocket 默认规则可作结构参考，但包含历史、小众、可达性变化的清单；不要假设所有国外学术站永远可直连，也不必盲目增加数千条规则。

## 11. 过程时间线（留给以后复盘）

| 时间（北京，约） | 关键事件 | 结果 |
| --- | --- | --- |
| 2026-08-21 | 购买 USD 18/季度 Starter，后台安装 Debian 12、建机 | `RUNNING`，2 GB/30 GB/1024 GB 配额确认 |
| 2026-08-21～22 | Windows ping/tracert、SSH 登录、IP 与归属检测、NTP 修正 | 网络与时钟基础 PASS；路由性质为推断 |
| 2026-08-22 | Microsoft/Apple/Cloudflare HTTPS/TLS 检查、AI 站点 HEAD 探测 | TLS 正常，AI 站点 CLI 响应按挑战/200 区分 |
| 2026-08-23 00:26 | sing-box 配置通过检查，systemd 启动监听 443 | 运行/监听 PASS |
| 2026-08-23 01:33～02:14 | Clash 与 Shadowrocket 握手问题，多轮检查与不必要的 key 轮换 | 仍有 `REALITY: processed invalid connection` |
| 2026-08-23 02:22 | 同机 sing-box→sing-box SOCKS 回环 | 失败，服务端同样报 REALITY invalid |
| 2026-08-23 02:33 | 从 `www.microsoft.com` 换为 `www.cloudflare.com` | 同机完整代理闭环 **PASS** |
| 2026-08-23 随后 | iOS 更新 SNI，Shadowrocket 用 `default.conf` 分流 | IPinfo 美国出口、IP138 电信直连 **PASS** |
| 2026-08-23 | IPinfo、BrowserLeaks、AbuseIPDB、Scamalytics | 低风险画像；商业机房性质明确 |
| 2026-10-08 | 根据历史用户输出整理本笔记 | 历史记录归档；**未重新实测 VPS** |

## 资料与证据入口

- [sing-box Issue #4290：REALITY inbound / supported_groups / Microsoft 目标兼容问题](https://github.com/SagerNet/sing-box/issues/4290)
- [IPinfo：23.169.184.26](https://ipinfo.io/23.169.184.26)
- [AbuseIPDB：23.169.184.26](https://www.abuseipdb.com/check/23.169.184.26)
- [Scamalytics 检测页](https://scamalytics.com/)
- [BrowserLeaks](https://browserleaks.com/ip)
- [sing-box 官方文档](https://sing-box.sagernet.org/)
- [Mihomo 配置文档](https://wiki.metacubex.one/)
- 一手证据：2026-08-21～23 用户提供的 Zgo/VirtFusion 截图、`ping/tracert/curl/openssl`、`systemctl/journalctl` 输出、iOS IP 检测与风控页面截图。原图未上传到此公开笔记仓库；保留的是可复用的测试结果与判断边界。

## Revision log

- 2026-10-08：首次整理 2026-08 完整部署与排障记录；区分已实测、技术推断与未验收项；对公开 GitHub 做凭据脱敏。
