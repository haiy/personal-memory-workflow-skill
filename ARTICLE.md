# 把个人记忆做成一个可安装的 Memory Skill

AI agent 真正难的不是“这一次回答得聪明”，而是下一次还能不能接住之前的工作。

如果每次都要重新解释项目结构、默认偏好、部署方式、输出格式、文件边界和历史决策，那么再强的模型也会像一个刚入职的新同事：反应快，但没有组织记忆。

我把自己的做法整理成了一个可安装的 skill：`personal-memory-workflow`。它不是为了保存所有聊天记录，而是为了让 agent 在新任务开始时知道该读哪里、该信什么、该重新验证什么、该把什么沉淀下来。

## 记忆不是越多越好

我最开始踩过的坑是：把 memory 理解成“保存更多历史”。但历史越多，问题越明显：

- 旧主题会污染当前任务。
- 过期事实会被当成当前状态。
- 大量日志和导出文件让真正重要的信息变得难找。
- 敏感信息和高噪音内容容易被错误沉淀。

后来我对 memory 的定义变了：

> Memory 不负责替代事实检查，它负责减少重复解释和找到正确入口。

也就是说，memory 应该告诉 agent：“这类任务通常怎么处理，项目入口在哪里，哪些规则要遵守，哪些事实容易过期。”  
但如果问题是“现在服务是否在线”“今天行情如何”“这个链接能不能打开”，那必须重新验证。

## 七层 memory 结构

我现在把个人 memory 分成七层。

第一层是固定规则层：用户偏好、输出语言、沟通方式、不要做什么、遇到某类请求默认怎么起手。

第二层是项目记忆层：每个项目都有自己的 `project-memory.md`，记录项目结构、当前进展、长期决策和已知坑。

第三层是任务日志层：复杂任务要有可回看的 Markdown，记录目标、路径、执行过程、验证结果和后续入口。

第四层是 skill 层：重复出现的流程不再只写说明，而是做成可安装 skill、脚本或 runbook。

第五层是环境记忆层：机器、服务、端口、部署拓扑、运行边界这类东西单独沉淀，避免每次重新摸环境。

第六层是索引发布层：重要文档、HTML 报告和可视化产物要有浏览入口或公开链接。

第七层是外部证据层：大文件、完整 transcript、数据库、原始日志、导出包保留在外部或 ignored artifact 目录，长期记忆里只写 manifest 和摘要。

这七层解决的是同一个问题：让记忆有边界，而不是变成一个什么都往里倒的仓库。

## 写入 memory 的判断

我通常用五个问题决定要不要写入：

1. 这件事会不会影响未来任务的默认做法？
2. 它是稳定知识，还是必须重新验证的实时状态？
3. 它是不是重复出现的流程？
4. 它有没有敏感信息或高噪音原文？
5. 它有没有可验证证据？

如果只是当前状态，就记录检查方式，不把结果当长期事实。  
如果是重复流程，就升级成 skill。  
如果是复杂任务，就写任务日志。  
如果是项目边界变化，就更新 project-memory。  
如果是用户明确纠偏，就更新规则。

这让 memory 从“存东西”变成了“管理未来工作方式”。

## 使用 memory 的正确姿势

一个任务开始时，我希望 agent 做的是：

1. 先查轻量规则索引。
2. 再判断当前任务属于哪个项目或 workflow。
3. 只读相关记忆，不全量加载历史。
4. 用 memory 找入口和风险。
5. 对 live state 重新验证。

这样做以后，agent 不再靠印象猜，也不会把所有历史塞进上下文。

## Chat rules 是 memory 的前门

我后来发现，很多“记忆问题”其实不是知识问题，而是协作默认问题。

比如：

- 报告要给链接。
- 复杂任务要写日志。
- 页面交付要验证。
- 最新状态要重新查。
- 用户说“以后默认这样”时，要把它写进规则。

这些不应该散落在项目文档里。它们更适合成为 chat rules。

chat rules 的设计要很轻：顶部有一个 Rule Index，列出关键词、触发场景和动作。每次任务开始，agent 先查这个轻量索引；只有命中时，才加载对应规则正文。

这样既能让偏好长期生效，又不会把一整本“行为手册”塞进上下文。

## Codex 需要一个全局入口

如果只是把 skill 放在目录里，它还不算真正进入工作流。真正关键的是 Codex 的全局设定。

我会在 `~/.codex/AGENTS.md` 里放一段很短的全局说明：

```markdown
- Use `~/mem` or `$MEMORY_REPO` as the private long-term memory repo.
- For complex tasks, write a short task log into the memory repo.
- Maintain `docs/projects/<project>/project-memory.md` for durable project context.
- Convert repeated workflows into installable skills under `skills/<skill-name>/`.
- At the start of each task, run chat-rule lookup if available.
- If the user corrects a default, update chat rules first.
- Treat memory as routing guidance, not proof of current state.
- Do not store secrets, full transcripts, databases, or bulky raw exports in long-term memory.
```

这一步的意义很大：它让 memory 不再是“想起来才用的工具”，而是每次任务启动时的固定动作。

## 真实效果

这套方法最明显的效果，是我不再需要反复讲“默认怎么做”。

报告和网页会自然带上链接与验证。  
项目会有长期入口。  
高频流程会逐渐变成 skill。  
敏感数据不会混进公开文档。  
大项目可以跨天继续，而不是每次从背景介绍开始。  
当用户说“以后默认这样”，这句话会变成可执行规则，而不是一次性的提醒。

这就是我理解的 agent memory：它不是让 AI 记住所有过去，而是让未来的工作更少浪费。

## 安装这个 skill

仓库里包含一个可安装的 Codex skill：

```bash
./skills/personal-memory-workflow/scripts/install.sh
```

默认会安装到：

```text
~/.codex/skills/personal-memory-workflow
```

如果你也在维护自己的长期文档仓库，可以把 `MEMORY_REPO` 指到你的仓库：

```bash
export MEMORY_REPO="$HOME/mem"
```

然后让 agent 在 memory 相关任务里使用这个 skill。

完整的 Codex 全局设定步骤见仓库里的 `docs/codex-global-setup.md`。

## 最后一条原则

我现在最常用的一句话是：

> Memory 负责少走回头路，事实检查负责现在到底是不是这样。

只要坚持这个边界，memory 就不会变成负担，而会变成 agent 真正开始“长期协作”的基础设施。
