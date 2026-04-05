#!/usr/bin/env python3
"""QA Agent — Independent quality reviewer for the Ologos ecosystem.

Usage:
    python3 agent.py <file_or_dir> [file_or_dir ...] [--issue ISSUE_REF] [--provider PROVIDER] [--model MODEL]

Examples:
    python3 agent.py ops/                          # Review entire ops/ directory
    python3 agent.py ops/README.md skills/qa.md    # Review specific files
    python3 agent.py qa-agent/ --issue '#17'       # Review with issue reference
    python3 agent.py ops/ --provider gemini --model gemini-2.5-flash  # Use Gemini
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

# Add qa-agent/ to path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent))

import config
import validator


def load_system_prompt() -> str:
    """Load the QA review system prompt + QA skill as context."""
    prompt = config.QA_PROMPT_PATH.read_text()
    if config.QA_SKILL_PATH.exists():
        skill = config.QA_SKILL_PATH.read_text()
        prompt += f"\n\n---\n\n# Reference: Quality Assurance Skill\n\n{skill}"
    return prompt


def gather_files(paths: list[str]) -> dict[str, str]:
    """Read all files from the given paths (files or directories). Returns {path: content}."""
    files = {}
    for p in paths:
        path = Path(p)
        if path.is_file():
            try:
                files[str(path)] = path.read_text()
            except (UnicodeDecodeError, PermissionError):
                files[str(path)] = f"[binary or unreadable file]"
        elif path.is_dir():
            for f in sorted(path.rglob("*")):
                if f.is_file() and not f.name.startswith("."):
                    try:
                        files[str(f)] = f.read_text()
                    except (UnicodeDecodeError, PermissionError):
                        files[str(f)] = f"[binary or unreadable file]"
        else:
            print(f"Warning: {p} not found, skipping", file=sys.stderr)
    return files


def build_user_prompt(files: dict[str, str]) -> str:
    """Build the user prompt from file contents."""
    parts = ["# Files to Review\n"]
    for path, content in files.items():
        parts.append(f"## {path}\n```\n{content}\n```\n")
    parts.append(
        "\nReview all files above against the QA standards. "
        "Return your assessment as the specified JSON structure."
    )
    return "\n".join(parts)


def write_log_entry(log_entry: dict, model_name: str, issue_ref: str | None):
    """Append the QA log entry to ops/qa_log.json."""
    log_path = config.OPS_DIR / "qa_log.json"
    log_data = json.loads(log_path.read_text())

    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    entry_type = log_entry.get("type", "artifact_review")
    entry = {
        "id": f"{now}-{entry_type}-qa-agent",
        "timestamp": now,
        "model_used": model_name,
        **log_entry,
    }
    if issue_ref:
        entry["related_issue"] = issue_ref

    log_data["entries"].append(entry)
    log_path.write_text(json.dumps(log_data, indent=2) + "\n")
    return entry["id"]


def main():
    parser = argparse.ArgumentParser(description="QA Agent — MOSA model-agnostic quality reviewer")
    parser.add_argument("paths", nargs="+", help="Files or directories to review")
    parser.add_argument("--issue", default=None, help="Related issue reference (e.g., '#17')")
    parser.add_argument("--provider", default=None, help="Model provider override (openai, gemini)")
    parser.add_argument("--model", default=None, help="Model name override")
    parser.add_argument("--dry-run", action="store_true", help="Print prompts without calling model")
    parser.add_argument("--no-log", action="store_true", help="Skip writing to ops/qa_log.json")
    args = parser.parse_args()

    if args.provider:
        import os
        os.environ["QA_AGENT_PROVIDER"] = args.provider
    if args.model:
        import os
        os.environ["QA_AGENT_MODEL"] = args.model

    # Load prompt and files
    system_prompt = load_system_prompt()
    files = gather_files(args.paths)
    if not files:
        print("No files found to review.", file=sys.stderr)
        sys.exit(1)

    user_prompt = build_user_prompt(files)
    print(f"Reviewing {len(files)} file(s)...", file=sys.stderr)

    if args.dry_run:
        print("=== SYSTEM PROMPT ===")
        print(system_prompt[:500] + "..." if len(system_prompt) > 500 else system_prompt)
        print(f"\n=== USER PROMPT ({len(user_prompt)} chars, {len(files)} files) ===")
        for path in files:
            print(f"  {path}")
        sys.exit(0)

    # Call model
    adapter = config.get_adapter()
    print(f"Using model: {adapter.model_name}", file=sys.stderr)

    try:
        raw_response = adapter.review(system_prompt, user_prompt)
    except RuntimeError as e:
        print(f"Model API error: {e}", file=sys.stderr)
        sys.exit(1)

    # Validate response
    try:
        result = validator.validate(raw_response)
    except ValueError as e:
        print(f"Validation failed: {e}", file=sys.stderr)
        print(f"Raw response:\n{raw_response}", file=sys.stderr)
        sys.exit(1)

    # Output report
    print(json.dumps(result, indent=2))

    # Log to ops/
    if not args.no_log:
        entry_id = write_log_entry(result["log_entry"], adapter.model_name, args.issue)
        print(f"\nLogged to ops/qa_log.json: {entry_id}", file=sys.stderr)

    # Exit code based on verdict
    if result["verdict"] == "fail":
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
