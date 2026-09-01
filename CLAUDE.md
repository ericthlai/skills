# Contributing to this repo

Rules for editing this repository, not instructions for the skills themselves.

## The skills here are a build output

The originals live in the author's private workspace. **Never edit a `SKILL.md` here and expect it to
survive** — the next sync regenerates this whole `skills/` tree from those originals and overwrites
anything changed in place.

The sync tooling itself is deliberately not published: it holds an absolute path on one machine and
names private directories, so it is gitignored. It refuses to complete if any host-specific string
reappears in the output, which is why a leak cannot ship quietly.

If you are reading this as an outside contributor: open an issue or a PR against the skill text and
it will be applied upstream, then synced back. Sorry for the indirection; a single source beats two
copies that drift.

## `AGENTS.md` is a symlink to this file

Recorded in git as mode `120000`. Editing one edits both, which is the point — two copies of the same
rules drift, and nothing warns you when they do.

## Maintenance

**Changing an existing skill.** Edit the original in the private workspace, run the sync, commit,
push. Never the copy here.

**Adding a skill.** Write and actually use it in the private workspace first — a skill that has not
survived a real task does not belong in a published collection. Then add its folder name to the
`$Skills` list in the sync script, sync, and check three things before pushing:

1. Its `name:` frontmatter matches its directory name exactly, and it has a `description:`. Both are
   required by the `skills` CLI even though Claude Code is laxer.
2. It references no skill, sub-agent, file, or directory that this repository does not ship. A name
   that resolves to nothing is worse than a sentence describing the handoff in plain English.
3. It decides where it writes rather than assuming a layout — see the portability note in the README.

Skills stay **flat** at `skills/<name>/`. Bucketing into category folders forces every path to be
hand-enumerated in `plugin.json`; flat needs no enumeration at all.

**Versioning.** `version` lives in `.claude-plugin/plugin.json` and nowhere else. It was briefly
duplicated in `marketplace.json`, which is two writers for one number and would have gone stale on the
first bump.

**What does not go in here**

- Personal, client, or company names. Anything host-specific. Any absolute path from a private
  machine. The sync refuses to complete if one reappears, and it scans the whole repository, not just
  `skills/` — an earlier version checked only `skills/` and a private path shipped in a root file.
- A parallel `docs/` tree mirroring every skill. At this size the README sections do that job:
  `skills/` is what the agent reads, this file and the README are what a human evaluating the repo
  reads.
- Release automation, eval harnesses, or per-platform manifests for other agents, until there is a
  change cadence that needs them.
