---
name: personal-memory-workflow
description: Use when the user asks to create, update, install, or apply a personal memory workflow, including project-memory files, task logs, communication rules, reusable skills, environment memories, memory inventory, and deciding what to retrieve, write, verify, or keep out of long-term memory.
---

# Personal Memory Workflow

Use this skill to turn current work into durable, reusable memory, and to use existing memory without letting stale context override live facts.

## Defaults

These paths can be adapted per user or overridden through environment variables:

- Memory repo: `${MEMORY_REPO:-$HOME/mem}`
- User skill dir: `${MEMORY_SKILLS_DIR:-$HOME/.codex/skills}`
- Project memories: `docs/projects/<project>/project-memory.md`
- Skills: `skills/<skill-name>/SKILL.md`
- Environment memories: `environment/memories/<name>/memory.md`
- Chat rules: this skill's `references/chat-rules.md`, or a customized copy in the memory repo.
- Task artifacts: `environment/tasks/` or ignored artifact directories, with summaries in docs.

If the request is about live status, newest data, prices, repo state, service health, running processes, or online links, treat memory as routing guidance only and verify current facts with tools.

## Start Of Task

1. Run chat-rule lookup for the latest user request when available:
   ```bash
   python3 ~/.codex/skills/personal-memory-workflow/scripts/rule_lookup.py "<latest user request>" --topic "<short topic>"
   ```
2. Check the real workspace state before editing:
   ```bash
   git -C "${MEMORY_REPO:-$HOME/mem}" status --short --branch
   ```
3. Read only the relevant project memory, task log, skill, or reference file. Do not load the whole memory repo.
4. When uncertain whether a fact has drifted, verify it directly instead of answering from memory.

## Choose The Memory Target

- **Communication rule**: user corrects a default, complains about repeated behavior, says "以后都这样", "默认", "directly", or asks to change interaction rules.
- **Project memory**: project structure, current state, durable decisions, recurring paths, known traps, or next-step context for a named repo/project.
- **Task log**: complex requirement breakdown, implementation record, research synthesis, validation evidence, or anything that should be replayable later.
- **Skill**: repeated workflow, fragile command sequence, installation recipe, reusable tool, or runbook.
- **Environment memory**: machine, service, endpoint, credential boundary, deployment topology, or operational state that should guide future work.
- **HTML/report index**: final report, visual analysis, dashboard, webpage, or artifact that should be browsable later.
- **External artifact only**: large raw logs, full transcripts, databases, credentials, binaries, private account details, and bulky downloaded exports. Keep only manifest, path, summary, and safety boundary in the memory repo.

## Writing Pattern

Keep durable memory short, factual, and actionable:

1. State the date, task, and scope.
2. Record exact paths, commands, output links, and validation evidence.
3. Separate stable knowledge from live facts that must be rechecked.
4. Include privacy boundaries: what is deliberately not stored.
5. Add the entry to the relevant `project-memory.md` if it changes future project context.
6. For larger changes, stage only relevant files and create a local commit when consistent with user instructions.

Avoid storing raw secrets, full chat transcripts, noisy logs, large CSV/JSONL files, virtual environments, dependencies, databases, downloaded media, or generated build output.

## Chat Rule Pattern

Use chat rules for stable interaction behavior, not project facts.

1. Edit the `Rule Index` first: rule id, keywords, short trigger, and action.
2. Keep the rule body short and operational.
3. If a rule applies only to one project, write it to that project memory instead.
4. If a rule implies a repeated workflow, also update or create a skill.
5. After editing, test lookup:
   ```bash
   python3 ~/.codex/skills/personal-memory-workflow/scripts/rule_lookup.py "user-like test query" --topic "topic"
   ```

## Retrieval Pattern

Use memory to find the right entrance, not to skip verification:

1. Identify likely project/domain from the latest request.
2. Read `docs/index.md` or the relevant `docs/projects/<project>/project-memory.md` when the user asks for memory inventory or prior workflow.
3. Search with `rg` for specific paths, terms, task names, services, or artifacts.
4. Prefer original task logs or source files over secondhand summaries when exact evidence matters.
5. For "current/latest/now/today" questions, use memory only to choose tools and then verify live state.

## Skill Creation Pattern

When turning a memory workflow into an installable skill:

1. Create `skills/<skill-name>/SKILL.md` with concise YAML frontmatter and a short procedural body.
2. Put detailed background in `references/` only if it will be loaded conditionally.
3. Put deterministic helpers in `scripts/`.
4. Add `agents/openai.yaml` with a display name, short description, and default prompt when supported by the host app.
5. Validate with the host skill validator if one exists.
6. Install by symlinking or copying into the user skill directory. Prefer symlink for locally maintained skills.
7. Update the memory repo's project memory with the new skill and installation status.

## Output Contract

When you finish a memory task, report:

- The files created or updated.
- Whether current facts were verified, and how.
- Any local commit hash if one was created.
- Any install command or installed skill path if applicable.

## References

- `references/memory-workflow-baseline.md`: distilled baseline for personal memory workflows.
- `references/chat-rules.md`: starter chat rules and rule maintenance pattern.
