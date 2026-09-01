# Scout — Research Sweep, Discipline & Type Checklists

Read this for any `scan` or `work-up`. (A `think`-depth input never needs this file.)

## Contents
- Research sweep (A–D)
- Analysis discipline (non-negotiable)
- Type checklists

## Research sweep

> A work-up is not "done" after one pass. Find what a diligent analyst would. **The user should rarely have to hand you a source you could have found yourself.** Snippets are a map, not the territory — open the pages.

**A. Mine provided materials FIRST.** Fully extract every artifact the user gave — links, decks, PDFs, emails, agenda, screenshots. If one won't load (too large / gated / JS-rendered), **route around it**: search its title, fetch the vendor's equivalent page, or find the same template elsewhere. Never abandon a provided artifact after one failed fetch.

**B. Source sweep — FETCH primary pages.**
- **company / vendor:** the target's OWN site (home, about/leadership, product, use-cases, industries, clients/case studies, pricing, news/blog) + third-party (reviews: G2/Capterra/Gartner; funding/size: Crunchbase/CB Insights/Owler; recent news; named competitors).
- **ai-tool:** repo + docs (stars, license, release recency, security/data), pricing, vendor claims, independent reviews/benchmarks, alternatives.
- **concept / article:** the original source + its strongest critics + independent corroboration.

**C. People sweep.** For EVERY named individual (attendees, leadership, authors): role/title, background, public talks/writing, and what they personally sell or advocate. Name anyone you could NOT verify — never invent a role.

**C2. Widen the lens (anti single-source bias).** Don't synthesize from the target's own framing alone — gather an independent critic/skeptic, a customer/user, and a competitor's angle. (STORM's perspective-guided research: multiple viewpoints produce depth; one pass through the brochure produces a sales sheet.)

**D. Two waves + a completeness gate.** Wave 1: broad sweep across B + C. Then STOP and write *what's still uncovered and what questions remain.* Wave 2: targeted fetches to close gaps. Repeat until covered or dry — then synthesize. Hand broad fan-out to a research sub-agent rather than fetching every page yourself. A `scan` fetches the 2-3 most important primary pages; only `work-up` runs the full sweep + gate.

## Analysis discipline (non-negotiable)
- **Cite every factual claim.** Tag each source `[primary]` / `[secondary]` / `[vendor]`.
- **SIFT + score each load-bearing source.** Stop · Investigate source · Find independent coverage · Trace to origin. Rate 1-5: authority, traceability, corroboration, recency, incentive/bias, specificity. Record in the source ledger.
- **Two-source rule.** No HIGH confidence unless load-bearing claims have ≥2 credible *independent* sources or one strong primary. Else cap confidence and say why. Unverifiable → `[unverified]`.
- **Never fabricate** a source, stat, star count, funding figure, role, or quote.
- **Mandatory RISK / red-flag section.** Never return only the upside.
- **Pre-mortem** (work-up adoption call): "It's 6 months later and this failed — why?" (3-4 bullets).
- **ACH** (contested build-vs-buy): 2-3 competing options scored by what *disconfirms* each.
- **Key Assumptions Check** (Heuer/Pherson SAT): list the assumptions the call rests on and challenge each — "what if this is wrong?" — noting what would break.
- **Data-handling gate** (any vendor/tool touching our data): opt out of training? DPA available? data residency? — two+ "no" on a customer-data use → flag and pause for sign-off.
- **High-stakes → devil's advocate** (SAT): argue the *opposite* recommendation in 2-3 bullets; if hard to refute, lower confidence or widen options.
- `scan` skips pre-mortem / ACH / KAC / devil's-advocate: 3-5 cited takeaways + one risk line.

## Type checklists
- **ai-tool** — what it does; maturity (GitHub stars/cadence, funding, release recency); pricing/licensing; security & data handling (*where does our data go?*); integration fit with the stack actually in use; top 2-3 alternatives; adoption signals; risks.
- **company / vendor** — business model; market position; funding/size; **leadership + the specific people in the room (people sweep)**; **their actual proposal / deck / offering**; named customers (especially in *our* niche, not just marquee logos); competitors; **relevance to us** (client/vendor/partner/competitor); **what's additive vs. what we already do or can build in-house**; risks.
- **concept / framework** — origin & author; core claim; evidence base; **criticisms / where it fails**; adoption; how it applies to our work.
- **article-video** — thesis; source/author credibility; key claims; corroborating AND contradicting evidence; takeaways.
- **raw-thought** — usually `think`-depth (no research). If decision-bearing: the clarified decision question; what we'd have to believe; the closest existing internal topic note.
