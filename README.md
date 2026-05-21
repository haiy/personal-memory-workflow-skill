# 把个人记忆做成一个可安装的 Memory Skill

> 这不是一个“聊天记录备份”方案，而是一套让 AI agent 能跨任务、跨项目、跨天继续工作的个人 memory 工作流。

很多人在用 AI 工具时会遇到同一个问题：每次开新对话，都要重新解释项目在哪里、默认怎么做、哪些坑不要踩、哪些文件不能动、哪些结果要验证。上下文窗口越来越长，但真正能稳定复用的上下文并没有变多。

我做这个 `personal-memory-workflow` skill 的目标，就是把这些反复解释的部分变成一套可安装、可执行、可维护的工作流。

## 核心判断

好的 memory 不是“记得越多越好”，而是让下一次工作少走回头路。

它应该回答：

- 这次任务应该先读哪里？
- 哪些规则是稳定默认？
- 哪些项目状态值得长期保存？
- 哪些事实必须重新验证？
- 哪些内容不该进入长期记忆？
- 什么时候应该把一个流程升级成 skill 或 runbook？

所以这个 skill 的基本原则是：

> Memory 负责找到入口和减少重复解释，verification 负责确认现在到底是不是这样。

## 分层结构

我把个人 memory 分成七层，而不是把所有内容堆进一个文件。

| 层级 | 放什么 | 作用 |
| --- | --- | --- |
| 固定规则层 | 用户偏好、沟通规则、输出默认、协作边界 | 让 agent 开局知道基本行为 |
| 项目记忆层 | 项目结构、进展、决策、已知坑 | 下次继续同一项目时不用从零解释 |
| 任务日志层 | 复杂需求拆解、执行记录、验证结果 | 让重要工作可回看、可复跑 |
| Skill 层 | 高频流程、脆弱命令序列、可复用 runbook | 把经验变成可执行能力 |
| 环境记忆层 | 服务、机器、端口、部署拓扑、运行边界 | 避免每次重新摸环境 |
| 索引发布层 | 文档入口、HTML 页面、manifest、公开链接 | 让记忆可浏览、可引用 |
| 外部证据层 | 大文件、原始日志、数据库、完整导出 | 保留证据，但不污染长期仓库 |

这种结构的关键是边界清晰：长期记忆保存“方法、路径、决策、边界和摘要”，不保存噪音和敏感原文。

## 写入规则

一个信息是否应该进入 memory，我会用下面的判断：

1. **会不会影响未来任务的起手式？**  
   会，就应该写进规则、项目记忆或 skill。

2. **是不是只对当前时刻成立？**  
   如果是服务状态、价格、行情、运行进程、Git 状态，就只记录检查方法，不把当前值当永久事实。

3. **是不是重复出现的流程？**  
   如果同一套步骤会用三次以上，就应该考虑做成脚本、skill 或 runbook。

4. **是不是敏感或高噪音材料？**  
   凭据、完整聊天记录、大型日志、数据库、大 CSV、导出包不进入长期仓库，只记录 manifest、路径和处理边界。

5. **有没有验证证据？**  
   对交付结果，尽量记录测试、截图、health check、HTTP 状态、文件路径或 commit。

## 使用方式

这个 skill 在任务开始时做四件事：

1. 先识别当前请求是否命中已有规则或项目。
2. 只读取相关的 project-memory、task log、skill 或 reference，不全量加载记忆库。
3. 用 memory 找入口、找风险、找过去的决策。
4. 对 live state 重新验证，比如服务是否在线、链接是否能打开、Git 是否干净、数据是否最新。

它避免两个常见极端：

- 不靠模型“凭印象”复述旧事实。
- 也不把所有历史都塞进上下文，制造旧主题污染。

## Chat Rules：把纠偏变成可执行规则

`chat rules` 是最轻的一层 memory。它不记录项目事实，而是记录稳定的协作方式。

适合写成 chat rule 的内容包括：

- “以后默认这样”
- “不要每次都问，直接做”
- “报告必须给链接”
- “页面交付要验证能打开”
- “最新状态必须查 live”
- “这种流程要做成 skill”

仓库里带了一个 starter：

```text
skills/personal-memory-workflow/references/chat-rules.md
```

查询脚本：

```bash
python3 ~/.codex/skills/personal-memory-workflow/scripts/rule_lookup.py \
  "把这个流程做成 skill，以后默认这样" \
  --topic "memory workflow"
```

维护规则时先改顶部 `Rule Index`，再补规则正文。这样 agent 开局只需要读轻量索引，命中后再读具体规则。

## 实际效果

这套工作流带来的变化很直接：

- 新任务启动更快，因为项目入口和默认规则已经写清楚。
- 交付更完整，因为报告、网页、服务和脚本会附带验证证据。
- 用户偏好能长期生效，而不是每次口头提醒。
- 大项目能跨天继续，不需要重新解释项目背景。
- 研究、归档、部署、网页实现等高频动作可以逐步沉淀成 skill。
- 记忆库本身更干净，因为大文件、凭据、完整 transcript 和噪音日志不会直接进库。

## 什么时候触发这个 skill

适合这些场景：

- “把这个记到 memory”
- “以后默认这样”
- “给这个项目写 project-memory”
- “这套流程做成 skill”
- “看看我之前怎么做的”
- “这个要不要进长期记忆”
- “整理一下现在有哪些记忆入口”

## 安装

把仓库 clone 到本地后执行：

```bash
./skills/personal-memory-workflow/scripts/install.sh
```

默认会 symlink 到：

```text
~/.codex/skills/personal-memory-workflow
```

如果你想复制安装而不是 symlink：

```bash
./skills/personal-memory-workflow/scripts/install.sh --copy
```

## Codex 全局设定

安装 skill 只是第一步。要让它在每次 Codex 任务开始时生效，需要把它接到 Codex 全局说明里。

创建或更新：

```text
~/.codex/AGENTS.md
```

推荐加入：

```markdown
- Use `~/mem` or `$MEMORY_REPO` as the private long-term memory repo.
- For complex tasks, write a short task log into the memory repo.
- Maintain `docs/projects/<project>/project-memory.md` for durable project context.
- Convert repeated workflows into installable skills under `skills/<skill-name>/`.
- At the start of each task, run the chat-rule lookup if available:
  `python3 ~/.codex/skills/personal-memory-workflow/scripts/rule_lookup.py "<latest user request>" --topic "<short topic>"`
- If the user corrects a default or says "always do this", update chat rules first, then the relevant project memory or skill.
- Treat memory as routing guidance, not proof of current state. Recheck live facts, services, links, Git status, and current data.
- Do not store secrets, credentials, full transcripts, databases, or bulky raw exports in long-term memory.
```

更完整的步骤见：

[Codex Global Setup](docs/codex-global-setup.md)

## 配置自己的 memory repo

默认约定可以通过环境变量覆盖：

```bash
export MEMORY_REPO="$HOME/mem"
export MEMORY_SKILLS_DIR="$HOME/.codex/skills"
```

你也可以直接修改 skill 里的路径约定，让它适配自己的文档仓库。

## 公开版与私人版

这个仓库是公开版，刻意做了泛化：

- 不包含私人凭据。
- 不包含完整聊天记录。
- 不包含本机绝对路径。
- 不绑定某一个私人服务域名。

真正落地时，建议在自己的 private memory repo 中维护项目记忆、任务日志和环境记忆；公开仓库只保留通用方法、skill 模板和可分享的文章。
