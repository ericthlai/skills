# Decide before you build

Three agent skills for the part of the work that happens before any code exists: deciding whether a
thing should be built at all, deciding exactly what it is, and researching one named option to a
verdict you can act on.

They are packaged for [Claude Code](https://claude.com/claude-code) and follow the
[Agent Skills specification](https://agentskills.io/specification). A compatible host needs
filesystem access; the complete `pressure-test` and `scout` workflows also need access to current
external sources.

## Example

*Condensed `/pressure-test` example:*

> **Idea:** Build a custom parser to validate every `SKILL.md` before release.
>
> **Call: ADOPT** — use `agentskills validate` from the official `skills-ref` package for
> specification checks; build only the small repository-specific checks it does not own.
>
> **Why:** the [Agent Skills specification](https://agentskills.io/specification) already names
> `skills-ref` as its reference validator, and its
> [source repository](https://github.com/agentskills/agentskills) is Apache-2.0 licensed. Rebuilding
> frontmatter and naming validation would create a second interpretation of the standard.
>
> **Smallest sufficient version:** run the reference validator in CI, then add deterministic checks
> for this repository's manifests, local references, byte-order marks, and line endings.
>
> **Out of scope:** a new general-purpose validation framework.

## Why these three

Most planning skills stop at shared understanding. These do two things such skills usually skip:

- **They search outside before concluding.** An answer built only from the files on your machine
  looks rigorous while carrying the same blind spot as a guess. `pressure-test` refuses to say
  "build it" until prior art has actually been looked for.
- **They preserve decisions when persistence is authorized.** A consequential decision that lives
  only in a conversation is easy for the next session to contradict; the skills can record it in the
  host repository without treating an advisory request as permission to mutate files.

## Install

```
/plugin marketplace add ericthlai/skills
```

```
/plugin install hanlin-skills@hanlin
```

Or drop any single skill folder from `skills/` into `.claude/skills/` in your project, or into
`~/.claude/skills/` for every project.

One thing worth knowing: **`grilling` is a common name.** Installed as a plugin it is namespaced, so
it cannot clash with a same-named skill from another collection. Copied by hand into
`.claude/skills/`, it can — rename the folder if you already have one.

## The three skills

| skill | use it when | ends with |
|---|---|---|
| **`pressure-test`** | The idea itself is on trial. "Should I build this?", "talk me out of this", "does something already do this?" | An `ADOPT`, `BUILD`, `NOT NOW`, or `KILL` call, recorded when authorized — never "it depends" |
| **`grilling`** | The build is decided; what to build is not. Before any net-new build, architecture choice, or multi-file change | Shared understanding, plus an authorized cross-session handoff when needed |
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

## Portability and authority

The skills use relative paths and do not assume a project layout. They follow the host's own write
rules: an explicit request or existing repository policy must authorize persistence. When a durable
record is authorized, an existing project convention wins over creating another documentation tree.

## Validation

CI validates every skill against the Agent Skills specification and checks repository-specific
invariants such as manifest syntax, local references, line endings, and generated-output markers.
The routing cases in [`evals/routing-cases.json`](evals/routing-cases.json) document intended skill
boundaries; they are an unscored corpus, not a claim of model-level accuracy.

## How this was built

I designed the three-skill split, routing boundaries, verdict vocabulary, and human-decision gates.
AI coding tools assisted with drafting and implementation; I own the design, review, validation, and
release decisions. Automated checks validate package structure and deterministic invariants, while
behavioral quality still requires evaluation in the host model.

## Attribution

The design-tree / frontier / rounds model in `grilling`, and the fog-of-war and out-of-scope shape in
its multi-session section, build on the `grilling` and `wayfinder` skills in
[`mattpocock/skills`](https://github.com/mattpocock/skills) (MIT). The prose here is original; the
scaffolding of those ideas is theirs and worth reading directly.

## License

MIT. See [LICENSE](LICENSE). Contributions are welcome; see
[CONTRIBUTING.md](CONTRIBUTING.md).
