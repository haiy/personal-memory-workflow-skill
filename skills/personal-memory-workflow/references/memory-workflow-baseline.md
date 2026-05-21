# Personal Memory Workflow Baseline

This reference distills a practical memory workflow into reusable operating rules.

## Core Idea

The memory system is not a chat backup. It is a long-term work system for reducing repeated explanation, preserving project context, and making future agent sessions start from the right entrance.

## Stable Layers

| Layer | Purpose | Typical Location |
| --- | --- | --- |
| Fixed rules | User defaults, communication behavior, boundaries | `AGENTS.md`, communication rules |
| Project memory | Project structure, progress, decisions, traps | `docs/projects/<project>/project-memory.md` |
| Task log | Complex decomposition, execution record, validation | `docs/projects/.../YYYY-MM-DD-*.md` |
| Skill | Repeatable workflow or fragile command sequence | `skills/<skill-name>/SKILL.md` |
| Environment memory | Machines, services, endpoints, topology | `environment/memories/<name>/memory.md` |
| Index/publishing | Browseable docs, HTML links, manifests | `docs/index.md`, `docs/html-archive/` |
| External artifact | Large or sensitive raw evidence | ignored artifact dirs or private paths |

## Effective Defaults

- Long-lived preferences and repeated corrections should become rules or skill instructions.
- Chat rules should be indexed first, then expanded only when the rule body is needed.
- Long reports and visual artifacts should usually become Markdown or HTML, with links when published.
- Repeated procedures should become scripts, skills, or runbooks.
- For local status, service status, Git status, current data, and online links, verify live state before concluding.
- Do not store sensitive details in memory; keep methods, paths, boundaries, and manifests.

## Useful Heuristic

Memory answers "where should I look and what should I avoid repeating?"

Verification answers "is it true right now?"

Do both when the answer depends on live state.

## Codex Global Hook

For Codex, the memory workflow becomes reliable when a short global instruction tells the agent to:

1. Use a private memory repo for durable context.
2. Run chat-rule lookup at the start of each task.
3. Update chat rules when the user corrects defaults.
4. Verify live facts rather than trusting memory.
5. Keep secrets and bulky raw artifacts out of long-term memory.
