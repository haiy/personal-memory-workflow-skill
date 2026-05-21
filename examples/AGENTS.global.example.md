# Example Codex Global Instructions

- Use `~/mem` or `$MEMORY_REPO` as the private long-term memory repo.
- For complex tasks, write a short task log into the memory repo.
- Maintain `docs/projects/<project>/project-memory.md` for durable project context.
- Convert repeated workflows into installable skills under `skills/<skill-name>/`.
- At the start of each task, run the chat-rule lookup if available:
  `python3 ~/.codex/skills/personal-memory-workflow/scripts/rule_lookup.py "<latest user request>" --topic "<short topic>"`
- If the user corrects a default or says "always do this", update chat rules first, then the relevant project memory or skill.
- Treat memory as routing guidance, not proof of current state. Recheck live facts, services, links, Git status, and current data.
- Do not store secrets, credentials, full transcripts, databases, or bulky raw exports in long-term memory.

