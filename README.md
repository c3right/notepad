# notepad

一个用于长期保存“小发现、小产出、小结论”的远端笔记仓库。内容可以来自 ChatGPT 会话、临时研究、阅读整理、决策备忘、方法框架等；目标不是保存聊天记录，而是保存**以后值得再次找到并使用的成果**。

## 快速入口

- [INDEX.md](./INDEX.md)：全部笔记的人工可读目录
- [AGENTS.md](./AGENTS.md)：新增/更新内容时必须遵循的存储与整理规则
- [_templates/note.md](./_templates/note.md)：标准笔记模板
- [`notes/`](./notes/)：按年份存放的正式笔记

## 当前目录结构

```text
notepad/
├── README.md
├── AGENTS.md
├── INDEX.md
├── _templates/
│   └── note.md
└── notes/
    └── YYYY/
        └── YYYY-MM-DD-ascii-kebab-slug.md
```

采用“**时间为主存储键 + YAML 元数据标签 + 根目录索引**”的方式，而不是按单一主题分文件夹。原因是很多小产出天然跨学科、跨主题；时间路径稳定，主题则通过 `topics`、`keywords` 和 `INDEX.md` 检索。

## 基本原则

1. 保存提炼后的可复用成果，默认不保存原始聊天全文。
2. 一条正式笔记对应一个相对独立、以后值得找回的成果。
3. 新笔记必须包含标准 YAML 元数据，并加入 `INDEX.md`。
4. 同一主题的后续完善优先更新已有笔记，避免重复堆积。
5. 区分事实、解释、建议、假设和待核验信息。
6. 本仓库是公开仓库，不保存密码、隐私、敏感记录或机密内容。

完整规则见 [AGENTS.md](./AGENTS.md)。
