#!/usr/bin/env python3
"""Small chat-rule lookup helper for personal-memory-workflow."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def default_rules_path() -> Path:
    return Path(__file__).resolve().parents[1] / "references" / "chat-rules.md"


def parse_rule_index(text: str) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    in_index = False
    for line in text.splitlines():
        if line.strip() == "## Rule Index":
            in_index = True
            continue
        if in_index and line.startswith("## "):
            break
        if not in_index:
            continue
        match = re.match(r"^(R\d+)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*(.*)$", line)
        if match:
            rid, keywords, trigger, action = match.groups()
            rows.append(
                {
                    "id": rid.strip(),
                    "keywords": keywords.strip(),
                    "trigger": trigger.strip(),
                    "action": action.strip(),
                }
            )
    return rows


def score_rule(rule: dict[str, str], query: str, topic: str) -> int:
    haystack = f"{query} {topic}".lower()
    score = 0
    for keyword in [part.strip().lower() for part in rule["keywords"].split(",")]:
        if keyword and keyword in haystack:
            score += 2 if len(keyword) > 2 else 1
    if rule["trigger"].lower() in haystack:
        score += 3
    return score


def main() -> int:
    parser = argparse.ArgumentParser(description="Look up matching chat rules.")
    parser.add_argument("query", help="Latest user request")
    parser.add_argument("--topic", default="", help="Short topic label for ambiguous requests")
    parser.add_argument("--rules", default=str(default_rules_path()), help="Path to chat-rules.md")
    args = parser.parse_args()

    rules_path = Path(args.rules).expanduser()
    text = rules_path.read_text(encoding="utf-8")
    rules = parse_rule_index(text)
    scored = [
        (score_rule(rule, args.query, args.topic), rule)
        for rule in rules
    ]
    matches = [rule for score, rule in sorted(scored, key=lambda item: (-item[0], item[1]["id"])) if score > 0]

    print(f"rules_file={rules_path}")
    print(f"query={args.query!r}")
    print(f"topic={args.topic!r}")
    print(f"matches={len(matches)}")
    for rule in matches:
        print(f"{rule['id']}\t{rule['trigger']}\t{rule['action']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

