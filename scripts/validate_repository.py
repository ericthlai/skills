#!/usr/bin/env python3
"""Validate deterministic repository invariants not covered by skills-ref."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
LOCAL_LINK = re.compile(r"\[[^]]*\]\(([^)]+)\)")
SKILL_PATH = re.compile(r"`((?:reference|references|scripts|assets)/[^`]+)`")
ABSOLUTE_PATHS = (
    re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+"),
    re.compile(r"/" + r"Users/[^/\s]+"),
    re.compile(r"/" + r"home/[^/\s]+"),
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def repository_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-co", "--exclude-standard", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return sorted({ROOT / item.decode() for item in result.stdout.split(b"\0") if item})


def validate_text_files(errors: list[str], files: list[Path]) -> None:
    for path in files:
        if path.is_symlink():
            continue
        data = path.read_bytes()
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(ROOT)
        if data.startswith(b"\xef\xbb\xbf"):
            fail(errors, f"{relative}: UTF-8 BOM is not allowed")
        if b"\r\n" in data:
            fail(errors, f"{relative}: CRLF line endings are not allowed")
        for pattern in ABSOLUTE_PATHS:
            if pattern.search(text):
                fail(errors, f"{relative}: host-specific absolute path detected")


def validate_links(errors: list[str], files: list[Path]) -> None:
    for path in files:
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        prose = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
        prose = re.sub(r"`[^`\n]*`", "", prose)
        for target in LOCAL_LINK.findall(prose):
            if "://" in target or target.startswith(("#", "mailto:")):
                continue
            target_path = target.split("#", 1)[0]
            if target_path and not (path.parent / target_path).exists():
                fail(errors, f"{path.relative_to(ROOT)}: missing local link {target}")


def validate_skills(errors: list[str]) -> None:
    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    names = {path.name for path in skill_dirs}
    for directory in skill_dirs:
        skill_file = directory / "SKILL.md"
        if not skill_file.exists():
            fail(errors, f"{directory.relative_to(ROOT)}: missing SKILL.md")
            continue
        text = skill_file.read_text(encoding="utf-8")
        frontmatter = text.split("---", 2)[1] if text.startswith("---") else ""
        description = re.search(r"^description:\s*(.+)$", frontmatter, re.MULTILINE)
        if description:
            referenced = set(re.findall(r"`([a-z][a-z0-9-]*)`", description.group(1)))
            for name in sorted(referenced - names):
                fail(errors, f"{skill_file.relative_to(ROOT)}: unshipped skill reference `{name}`")
        for target in SKILL_PATH.findall(text):
            if not (directory / target).exists():
                fail(errors, f"{skill_file.relative_to(ROOT)}: missing bundled file {target}")


def validate_manifests(errors: list[str]) -> None:
    plugin_path = ROOT / ".claude-plugin" / "plugin.json"
    marketplace_path = ROOT / ".claude-plugin" / "marketplace.json"
    try:
        plugin = json.loads(plugin_path.read_text(encoding="utf-8"))
        marketplace = json.loads(marketplace_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"plugin manifest error: {exc}")
        return
    entries = marketplace.get("plugins", [])
    if len(entries) != 1:
        fail(errors, "marketplace.json: expected exactly one plugin entry")
    elif entries[0].get("name") != plugin.get("name"):
        fail(errors, "marketplace and plugin names do not match")
    if entries and entries[0].get("source") != "./":
        fail(errors, "marketplace plugin source must be ./")

    eval_path = ROOT / "evals" / "routing-cases.json"
    try:
        corpus = json.loads(eval_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"routing corpus error: {exc}")
        return
    if corpus.get("status") != "unscored":
        fail(errors, "routing corpus must remain explicitly unscored")
    known = {path.name for path in SKILLS_DIR.iterdir() if path.is_dir()}
    case_ids: set[str] = set()
    for case in corpus.get("cases", []):
        case_id = case.get("id")
        if not case_id or case_id in case_ids:
            fail(errors, f"routing corpus: missing or duplicate case id {case_id!r}")
        case_ids.add(case_id)
        if not case.get("prompt") or not case.get("reason"):
            fail(errors, f"routing case {case_id}: prompt and reason are required")
        if case.get("expected_skill") not in known | {None}:
            fail(errors, f"routing case {case_id}: unknown expected skill")


def validate_generated_contract(errors: list[str]) -> None:
    agent_rules = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
    if "build output" not in agent_rules:
        fail(errors, "CLAUDE.md must identify the published skill tree as build output")
    if "UPSTREAM APPLICATION REQUIRED" not in contributing:
        fail(errors, "CONTRIBUTING.md must preserve the upstream-application marker")


def main() -> int:
    errors: list[str] = []
    files = repository_files()
    validate_text_files(errors, files)
    validate_links(errors, files)
    validate_skills(errors)
    validate_manifests(errors)
    validate_generated_contract(errors)
    agents = ROOT / "AGENTS.md"
    if not agents.is_symlink() or agents.readlink() != Path("CLAUDE.md"):
        fail(errors, "AGENTS.md must be a symlink to CLAUDE.md")
    if errors:
        print("Repository validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Repository validation passed for {len(files)} repository files.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
