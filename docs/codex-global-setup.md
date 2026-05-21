# Codex Global Setup

This is the minimal way to make the memory workflow active at the start of Codex tasks.

## 1. Clone The Public Skill

```bash
mkdir -p ~/code
git clone https://github.com/haiy/personal-memory-workflow-skill.git ~/code/personal-memory-workflow-skill
```

## 2. Install The Skill

Symlink install:

```bash
~/code/personal-memory-workflow-skill/skills/personal-memory-workflow/scripts/install.sh
```

Copy install:

```bash
~/code/personal-memory-workflow-skill/skills/personal-memory-workflow/scripts/install.sh --copy
```

## 3. Choose A Private Memory Repo

Use any private repo or local folder as the actual memory store:

```bash
mkdir -p ~/mem
export MEMORY_REPO="$HOME/mem"
```

For a persistent shell setting, add this to your shell profile:

```bash
export MEMORY_REPO="$HOME/mem"
export MEMORY_SKILLS_DIR="$HOME/.codex/skills"
```

## 4. Add Codex Global Instructions

Create or update:

```text
~/.codex/AGENTS.md
```

Recommended global instructions:

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

If your Codex setup also uses `~/.codex/instructions.md`, keep it short and point to `~/.codex/AGENTS.md` or duplicate only the most important global defaults.

## 5. Add Chat Rules To Your Memory Repo

Copy the starter rules:

```bash
mkdir -p "$MEMORY_REPO/skills/personal-memory-workflow/references"
cp ~/code/personal-memory-workflow-skill/skills/personal-memory-workflow/references/chat-rules.md \
  "$MEMORY_REPO/skills/personal-memory-workflow/references/chat-rules.md"
```

Then maintain the top `Rule Index` first. Keep each rule short and test lookup after editing:

```bash
python3 ~/.codex/skills/personal-memory-workflow/scripts/rule_lookup.py \
  "以后所有报告都要给链接" \
  --topic "report output"
```

## 6. Smoke Test

```bash
python3 ~/.codex/skills/personal-memory-workflow/scripts/rule_lookup.py \
  "把这个流程做成 skill，以后默认这样" \
  --topic "memory workflow"
```

Expected result: at least the durable correction and reusable workflow rules should match.

