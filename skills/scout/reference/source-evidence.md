# Source-level evidence: license, claim labels, inspection ladder

Open this when a candidate needs code-level or licensing evidence, not when a documentation-level
comparison is sufficient.

## License is a hard gate

Public visibility is not permission to copy, modify, redistribute, or embed. State the license and
its obligations, or mark it `unknown` — and never recommend code reuse against an unknown license.

## Claim labels

The four labels `SKILL.md` already sets, applied to source-level claims:

- `confirmed` — directly supported by an inspected primary source or the code itself.
- `inference` — reasoned from cited evidence.
- `unknown` — not established, including anything blocked by an access limit.
- `not found` — searched for, and absent from the sources actually inspected.

`unknown` and `not found` are different claims and collapsing them is how an access limit becomes
false evidence of absence.

## The source-inspection ladder

Use the strongest method actually available, and say which was used:

1. Full checkout and source-tree inspection.
2. Raw-file retrieval against a repository tree.
3. Browsing only — capped at three candidates and six files, stating where inspection stopped.
4. Documentation only — every source-level claim marked `unknown`, never `not found`.

Never claim codebase-flow knowledge from isolated files, and never convert an access limit into
evidence of absence.
