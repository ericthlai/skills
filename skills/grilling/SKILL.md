---
name: grilling
description: Reach shared understanding before building, by asking only the questions that are answerable right now and answering the rest yourself. Use before any net-new build, architecture or technology choice, multi-file mutation, or work that will span sessions — and whenever the user says "grill me" or pushes back that a plan was written without knowing what it was for. Also use as the framing step of a plan-then-build pipeline, which needs a goal and an observable success definition but does not say how to elicit them. Do not use for a lookup, one reversible edit, or a task whose done-condition is already stated. Here the build is already decided; whether it should exist at all is `pressure-test`.
---

# Grilling

Eliminate the hidden decisions before acting. Not "ask a lot of questions" — a structured process
whose finish line is **shared understanding**, and whose main discipline is *not* asking most of
them.

The failure this exists to stop: a plan gets written, reviewed, and approved, and only then does it
emerge that nobody established what it was for. Every phase in it was reverse-engineered from
defects that happened to be visible. That has already occurred here.

## 1. Separate facts from decisions. This is the whole economy of the thing.

**A fact is your job.** Anything discoverable from the filesystem, source, git history, config,
`--help`, a probe, the running system, or the public web. Retrieve it. Never spend a question on it.

Asking *"which database does this use?"* when `package.json` answers it turns the user into a search
engine and spends the scarcest resource in the session — their attention — on the cheapest possible
work.

**A decision is his.** A trade-off, a preference, a risk ranking, what users should experience,
whether a cost is acceptable, which requirement actually matters.

Before every question, ask: *could I find this out?* If yes, go find it. Run the fact-gathering in
the background while you ask about decisions — the two do not queue behind each other.

**A decision already recorded is a fact, not a question.** When `pressure-test` closed this idea
first, the file it wrote already says what the call was and why. Read it
before the first question and treat that as settled — re-asking it is the same waste as asking what
a config file answers. What it does not say is what exactly gets built; that is this skill's
frontier, and where it starts.

## 2. Build the design tree, then ask only its frontier

Decisions depend on decisions. Do not ask *"which identity provider?"* before *"do we need
authentication?"* is settled — the answer would be conditional on an assumption that is still open.

The **frontier** is every decision whose prerequisites are already resolved. Those, and only those,
can honestly be answered now.

```
A resolved
├── B unresolved      ← frontier
│   └── D depends on B
└── C unresolved      ← frontier
    └── E depends on C
```

Ask B and C. Not D and E.

A fact still being researched is an **unsettled prerequisite**: what depends on it waits, what
does not depend on it is asked now. Research blocks its own branch, never the conversation.

## 3. Work in rounds

1. Compute the frontier.
2. Ask **every** question on it, in one batch.
3. Give your recommended answer to each, with the cost of the alternative.
4. Stop. Wait.
5. Incorporate the answers, and recompute — new answers open branches that were invisible before.

One batch per round matters: what a decision-maker wants is **one approval per major task, not
stepwise sign-off**. A round is a batch. Four rounds of four questions is fine; sixteen questions one
at a time is the thing they object to.

Generating one giant questionnaire up front is the opposite error. The next useful question is
usually unknowable until the previous answer exists.

## 4. Every question carries your recommendation

A menu is an abdication. They own the decision; they should not have to reason from zero to make it.

Give the question, your recommended answer, and what the alternative buys and costs. When one
option is clearly right, say so plainly rather than manufacturing balance.

## 5. Done means the frontier is empty and they agree

Not "I have asked enough". Every reachable branch visited, no unresolved prerequisite, no
assumption still carrying downstream consequences silently.

Then a human gate, which is separate: **you** believe understanding is complete, **they** confirm it.
Understanding and execution are different phases and the boundary between them is theirs to cross.

## 6. Write down what the answers settle

An answer that stays in the conversation is an answer the next session will contradict — that has
happened here, on a verdict this system had already reached. Decisions with durable consequence go
wherever this repository keeps durable knowledge — including the ones that are hard to reverse,
surprising without context, or involved a real trade-off. Capture at the moment it crystallises, not
later. (Until 2026-08-27 this sentence pointed at a directory that did not exist, which is the same
failure one level up: verify a home is real before aiming a rule at it. And the file `pressure-test`
writes is not that home — it holds why an idea was pursued at all, not what this skill settles.)

## 7. When the frontier outlives the session

Sections 1–6 assume one conversation: compute the frontier, empty it, done. A build spanning
sessions breaks that — the frontier is still populated when the context runs out, and nothing here
holds it. `STATE.md` carries one `next action`, not a graph of open questions.

So write the tree beside the work, in a dated working file next to it. If the project keeps a
cross-session state file — a `STATE.md`, or whatever this repository calls it — point at the working
file from there, because that is what the next session reads first. If there is none, say plainly in
your closing message where the working file is, and move on: its absence is not a problem to solve
from inside this skill.

Four headings:

- **Open** — the live frontier, each question carrying your recommended answer.
- **Settled** — questions already closed, one line of answer each. This is what stops the next
  session re-asking: an Open section that just shrinks reads as amnesia, and re-asking a settled
  question is §1's most expensive failure arriving by a different door. Durable decisions still go to
  the repository's durable-knowledge home per §6; this is the local record of what *this build*
  chose, not a second home for what that owns.
- **Not yet sharp** — in scope and coming, but not yet phraseable. The test is whether you can
  *state* the question precisely now, not whether you can answer it; a sharp question belongs in
  Open even while blocked. Do not pre-slice a patch into questions — it may become several, or none.
- **Out of scope** — past the done-condition. Scope, not sharpness, lands a thing here, and it never
  graduates back: the done-condition fixes the boundary, so reopening it is a new effort.

Resolving a question moves it from Open to Settled with its answer, and clears what stood behind it:
move whatever has become sharp into Open, and delete the fog patch it came from rather than leaving
it in both places.

**Mark every open question HITL or AFK.** AFK you resolve alone — a fact, a probe, a document. HITL
resolves only through the live exchange, and *answering a HITL question yourself has broken it*.
That is the failure that looks most like progress.

**The don't-build boundary may never live in a file this session writes.** §5's human gate is the
boundary; a working file cannot move it, whatever the file says. This section's shape is drawn from
`wayfinder` in `mattpocock/skills` (MIT), which got exactly this wrong: its map's own agent-written
Notes could override its "plan, don't do" default, and a reported session granted itself execution
licence that way.

## The ways this fails

- **Premature implementation** — acting while a branch is still open.
- **Premature questioning** — asking something whose answer depends on an unsettled prerequisite.
- **User as search engine** — asking what you could have retrieved. The most common and the most
  expensive.
- **Recommendation abdication** — presenting choices without taking a position.
- **Silent assumption** — a branch never surfaced, so it becomes an implementation choice nobody
  made.
- **Standing in for the decision-maker** — answering a HITL question yourself and recording it as
  settled. Distinct from a silent assumption: the branch *was* surfaced, then closed by the wrong
  party.

---

*Attribution: the design-tree / frontier / rounds model in §2–§4 builds on the `grilling` skill in
[`mattpocock/skills`](https://github.com/mattpocock/skills) (MIT), and §7's fog-of-war and
out-of-scope shape comes from that repo's `wayfinder`. §1's facts-versus-decisions economy, §6, §7's
Settled section and human-gate rule, and the failure list are additions.*
