# Contributing

Issues and pull requests are welcome. Please describe the behavior being changed, why the current
instruction fails, and the smallest realistic case that demonstrates the difference.

## Generated skill files

The `skills/` tree is generated from canonical sources maintained outside this distribution
repository. A pull request may propose changes directly against a published `SKILL.md`, but it must
be marked **UPSTREAM APPLICATION REQUIRED**. A maintainer applies the change to the canonical source,
re-syncs the generated tree, and only then merges it. Merging an isolated generated-file edit would
allow the next sync to overwrite the contribution.

Root documentation, tests, CI configuration, and evaluation fixtures are maintained directly in
this repository.

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
