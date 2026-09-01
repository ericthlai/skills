# Scout — Brief, Packet & Output Templates

## Step 3 deliberate brief (what the decision-maker sees at the checkpoint)
Recommendation first (BLUF / Pyramid):
```
## Scout: <thing> (<type>, <depth>)

**Decision question:** <the one decision this informs>
**Recommendation:** <one line — adopt / pilot / pass / watch / explore further>

**Options & trade-offs** (work-up only):
| option | pros | cons | best for |

**Key evidence:**
- <cited, credibility-tagged bullet>  [primary]

**Key assumptions:** <the beliefs this rests on>

**Risks / red flags:** <bullets; + pre-mortem if adoption>

**Confidence:** <0-100; HIGH needs the two-source bar> — **What would change my mind:** <signal>

**Open questions:** <or "none">

**Filing plan** (approve with the decision): internal topic file(s) to update or create · new entities · judgment candidates · what's archive-only.
```

## Canonical packet (`<packets-dir>/YYYY-MM-DD-<type>-<slug>.md`)
```markdown
---
type: ai-tool | company | concept | article-video | raw-thought
title: <name>
date: YYYY-MM-DD
status: researching | awaiting-decision | decided
depth: scan | work-up
confidence: <0-100>
decision: <one line, or "pending">
revisit: YYYY-MM-DD | none
sources: []
links: []   # [[knowledge-topic]], [[other-scout]]
---

## Decision question
## Recommendation
## Options & trade-offs   <!-- work-up: | option | pros | cons | best for | -->
## Key evidence (cited, credibility-tagged)
## Source ledger
<!-- | source | type [P]/[S]/[vendor] | link | key claim | quality 1-5 | bias/risk | -->
## Assumptions
## Risks / red flags
## Confidence & what would change my mind
## Open questions
## Decision log   <!-- decision · rationale · date · revisit -->
## Rounds (changelog)
- YYYY-MM-DD: initial scout
```

## Index row (`<packets-dir>/index.md`)
`| YYYY-MM-DD | type | [title](file.md) | depth | decision | confidence | revisit |`

## Canonical output shape by type
- **ai-tool** → decision memo (adopt / pilot / pass)
- **company / vendor** → relevance brief (engage / watch / pass)
- **concept / framework** → an internal explainer note (origin / claim / evidence / criticism / applicability)
- **article-video** → short note (takeaways + relevance + file or discard)
- **raw-thought** → (think-mode) a conversational reply; only a packet if it escalates

## Publish formats (Step 6, on request — generated from the packet)
- **team message** (principals): BLUF, 5-8 lines — recommendation, 2 risks, the ask. ≤200 words.
- **HTML one-pager** / **PPTX**: reuse the generated-view pattern.
