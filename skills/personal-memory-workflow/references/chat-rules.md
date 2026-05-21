# Chat Rules

Chat rules are the lightest memory layer: stable interaction defaults that should affect how an agent starts a task.

Keep this file short. The goal is not to store every preference, but to make repeated corrections executable.

## Rule Index

Each index row is:

```text
Rxx | keywords | short trigger | action
```

R01 | continue, 上面, 刚才, 然后, continue from above | Continuation | Carry forward the active goal, files, constraints, and verification state from the same thread unless the user clearly changes topic.
R02 | default, 默认, 以后都这样, always do this, correction | Durable Correction | Turn repeated corrections into a chat rule or project memory entry, then verify the lookup still finds it.
R03 | look, check, 看看, verify, health, status | Verify First | For status or debugging requests, check real files, logs, Git state, process state, service health, or live URLs before concluding.
R04 | report, article, HTML, webpage, publish, link | Link Output | For long reports, pages, and visual artifacts, prefer a readable Markdown or HTML artifact and provide a link when published.
R05 | skill, runbook, reusable, 复用, 工具化 | Make Reusable | If a workflow repeats or is fragile, convert it into a script, skill, or runbook.
R06 | current, latest, today, now, 最新, 今天, 现在 | Live Facts | Treat memory as routing guidance only; verify fresh facts with current sources.
R07 | secret, token, cookie, credential, private, sensitive | Safety Boundary | Do not store secrets, full transcripts, credentials, account details, or bulky raw exports in long-term memory.

## Rule Bodies

### R01 Continuation

When the user says "continue", "above", "then", "that one", or similar, use the current thread context. Do not reset the task unless the user clearly changes topic.

### R02 Durable Correction

When the user corrects behavior or says something should be the default, update the relevant rule, project memory, or skill. Prefer short rules with clear trigger words.

### R03 Verify First

For local state, services, Git, files, online links, and debugging, inspect current evidence before answering. Memory can suggest where to look, but not what is true now.

### R04 Link Output

Long-lived outputs should be easy to reopen. Prefer Markdown for memory-like notes and HTML for reports, dashboards, visualizations, and articles.

### R05 Make Reusable

Repeated workflows should become scripts, skills, or runbooks. Record the install path, invocation command, and validation evidence.

### R06 Live Facts

For current or latest facts, use current sources. Note the exact timestamp or source when useful.

### R07 Safety Boundary

Public artifacts should be sanitized. Private memory should store methods, paths, boundaries, and summaries rather than secrets or raw sensitive material.

