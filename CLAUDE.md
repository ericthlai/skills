# Contributing to this repo

Rules for editing this repository, not instructions for the skills themselves.

## This repository is the source of truth

The skills are edited here, directly. Change `skills/<name>/SKILL.md` (or a file it bundles) and
open a pull request. There is no separate upstream copy and no sync step: what is merged to `main`
is the published version. Outside contributors follow the same path; see `CONTRIBUTING.md`.

## `AGENTS.md` is a symlink to this file

Recorded in git as mode `120000`. Editing one edits both, which is the point — two copies of the same
rules drift, and nothing warns you when they do.

## Maintenance

**Changing an existing skill.** Edit `skills/<name>/SKILL.md` in place, run the validation commands
in `CONTRIBUTING.md`, and open a pull request.

**Adding a skill.** Write and actually use it on a real task first — a skill that has not survived
one does not belong in a published collection. Then add its folder under `skills/` and check three
things before opening the pull request:

1. Its `name:` frontmatter matches its directory name exactly, and it has a `description:`. Both are
   required by the `skills` CLI even though Claude Code is laxer.
2. It references no skill, sub-agent, file, or directory that this repository does not ship. A name
   that resolves to nothing is worse than a sentence describing the handoff in plain English.
3. It decides where it writes rather than assuming a layout — see the portability note in the README.

CI enforces the first of those, and two further things a reader is likely to miss:

- **The frontmatter must actually parse as YAML.** A bare `: ` inside an unquoted value makes the
  loader throw *"mapping values are not allowed in this context"* and the skill silently fails to
  load. Checking that `name:` and `description:` are *present* does not catch it; presence is not
  validity. `agentskills validate` parses the frontmatter and fails on it. Reword the sentence or
  quote the whole value.
- **No UTF-8 BOM.** Three bytes in front of the opening `---` and the frontmatter stops parsing.
  `scripts/validate_repository.py` rejects them. Save files as UTF-8 without a BOM:
  `Set-Content -Encoding UTF8` adds one in Windows PowerShell 5.1 but not in PowerShell 7, a bug
  that would appear only on one of the two consoles.

**Descriptions are routing text.** A skill's `description:` is always loaded into the agent's
context, so keep it in English and tight; every extra trigger phrase costs every reader attention.

Skills stay **flat** at `skills/<name>/`. Bucketing into category folders forces every path to be
hand-enumerated in `plugin.json`; flat needs no enumeration at all.

**Versioning.** `version` lives in `.claude-plugin/plugin.json` and nowhere else. It was briefly
duplicated in `marketplace.json`, which is two writers for one number and would have gone stale on the
first bump.

**What does not go in here**

- Personal, client, or company names. Anything host-specific. Any absolute path from a private
  machine. The public validator scans the whole repository, not just `skills/`, for the known
  patterns it can detect. It is not a guarantee that other confidential content can never be
  committed, so review the diff before pushing.
- A parallel `docs/` tree mirroring every skill. At this size the README sections do that job:
  `skills/` is what the agent reads, this file and the README are what a human evaluating the repo
  reads.
- Release automation, model-coupled eval runners, or per-platform manifests for other agents, until
  there is a change cadence that needs them. The small routing corpus is intentionally unscored.
