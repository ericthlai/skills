# Contributing

Issues and pull requests are welcome. Please describe the behavior being changed, why the current
instruction fails, and the smallest realistic case that demonstrates the difference.

## Where changes go

This repository is the source of truth. Skills, root documentation, tests, CI configuration, and
evaluation fixtures are all edited here: change `skills/<name>/SKILL.md` (or a file it bundles)
directly and open a pull request. There is no separate upstream copy and no sync step. Conventions
for new and changed skills are in [`CLAUDE.md`](CLAUDE.md).

## Validate a change

```bash
python -m pip install skills-ref==0.1.1
for skill in skills/*; do agentskills validate "$skill"; done
python scripts/validate_repository.py
```

For a behavior change, add or update a realistic routing case. The corpus documents intent; do not
record a pass rate unless the cases were actually run against a named host and model.

Do not include personal, client, or company information, credentials, environment files, or absolute
paths from a private machine.
