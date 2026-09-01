# Decide before you build

Three agent skills for the part of the work that happens before any code exists: deciding whether a
thing should be built at all, deciding exactly what it is, and researching one named option to a
verdict you can act on.

They are written for [Claude Code](https://claude.com/claude-code) and work in any harness that
reads the Agent Skills format.

## Why these three

Most planning skills stop at shared understanding. These do two things such skills usually skip:

- **They search outside before concluding.** An answer built only from the files on your machine
  looks rigorous while carrying the same blind spot as a guess. `pressure-test` refuses to say
  "build it" until prior art has actually been looked for.
- **They end in a written call.** A decision that lives only in a conversation is one your next
  session will contradict. Every verdict goes to a file first, and the reply leads with its path.

## Install

```
/plugin marketplace add ericthlai/skills
```

```
/plugin install hanlin-skills@hanlin
```

Or drop any single skill folder from `skills/` into `.claude/skills/` in your project, or into
`~/.claude/skills/` for every project.

Two things worth knowing before you install:

- **`grilling` is a common name.** Installed as a plugin it is namespaced, so it cannot clash with a
  same-named skill from another collection. Copied by hand into `.claude/skills/`, it can — rename the
  folder if you already have one.
- **Triggers are bilingual.** The descriptions carry Chinese trigger phrases alongside the English
  ones on purpose, so the skills fire in either language. They are not leftovers.

## The three skills

| skill | use it when | ends with |
|---|---|---|
| **`pressure-test`** | The idea itself is on trial. "Should I build this?", "talk me out of this", "does something already do this?" | A written call: `ADOPT`, `BUILD`, `NOT NOW`, or `KILL` — never "it depends" |
| **`grilling`** | The build is decided; what to build is not. Before any net-new build, architecture choice, or multi-file change | Shared understanding, and for work spanning sessions, a decision file the next session can pick up cold |
| **`scout`** | One named tool, repo, vendor, or product needs researching to a recommendation | A sourced packet: recommendation first, then evidence, contrary evidence, and what would change the call |

They chain: `pressure-test` decides whether to proceed and hands to `grilling`; `grilling` hands one
named candidate to `scout` and uses what comes back. Each also works alone.

## What makes them behave differently

- **Facts are the agent's job; decisions are yours.** Anything discoverable from the filesystem,
  source, git history, `--help`, a probe, or the public web gets retrieved, never asked. Asking what
  a config file answers spends your attention on the cheapest possible work.
- **One batch of questions per round, each carrying a recommended answer.** A menu is an abdication.
  You own the decision; you should not have to reason from zero to make it.
- **Only answerable questions get asked.** Decisions form a tree, and only the frontier — the
  decisions whose prerequisites are already settled — can honestly be answered now.
- **Work too big for one session gets written down, including what is *not* yet askable.** A "not yet
  sharp" section holds questions you can tell are coming but cannot phrase precisely; the test is
  whether you can *state* the question now, not whether you can answer it.
- **Nothing gets built during any of it.** The gate between understanding and execution is yours to
  cross, and no file the agent writes can move it.

## Portability

These skills write files, so they have to decide where. On first use in a repository they settle the
location — preferring whatever convention the repository already has, then a relative default they
create — and record the answer in your `CLAUDE.md` or `AGENTS.md` so no later session asks again.
Nothing assumes a directory exists.

## Attribution

The design-tree / frontier / rounds model in `grilling`, and the fog-of-war and out-of-scope shape in
its multi-session section, build on the `grilling` and `wayfinder` skills in
[`mattpocock/skills`](https://github.com/mattpocock/skills) (MIT). The prose here is original; the
scaffolding of those ideas is theirs and worth reading directly.

## License

MIT. See [LICENSE](LICENSE).
