---
id: foundation-docs-recommendation
title: Foundation docs, a recommendation (nothing built)
status: draft
date: 2026-10-10
---

# Foundation docs: recommendation

**As of 2026-10-10. Recommendation only. Nothing is built until the PM picks A, B or C at the bottom.**

## What exists today [V: read this run]

`goals.md` (58 lines) mixes four things: the mission, the promises, a guideline tier, and two open questions. Its name says little. The same ground is also spread across:

| Holds | Where | Lines |
|---|---|---|
| Mission, what this is | `product/foundation/what-this-is.md`, `goals.md` | 40, 58 |
| How we think | `people-first.md`, `value-test.md`, `impact-diagnostic.md`, `policy.md` (all in `product/foundation/`) | 26, 42, 75, 51 |
| What the platform won't do to a member | `product/ABSOLUTES.md` | 26 |
| How we earn, what we measure | `monetization.md`, `metrics.md` | 28, 30 |
| How we sound | `voice-and-tone.md` | 190 |
| Rulings, one dated line each | `DECISIONS.md` | 391 lines |
| Parked ideas, the Won't list | `IMAGINE.md`, `ROADMAP.md` | 147, 114 |
| Per-tier rulings, generated | `constraints/code.md`, `constraints/planning.md` | 156, 183 |
| Agent instructions that restate rules | `CLAUDE.md` in plan, web, ops, and the global one | 120, 181, 53, 89 |
| Method rules (not product) | `socialus-ops/process/ABSOLUTES.md`, `PIPELINE.md` | 149, — |
| Rules in code and copy | `socialus-web/src/lib/creator-rules.ts`, `moderation/rules.ts` | — |

Problems: the same banner is pasted into 18 files; `goals.md` is cited by 8 files; "never" appears in rules where only "never extractive" is allowed; no doc says when it was last true.

## Proposed set: six docs in a new `foundation/` folder

| Doc | What goes in it | Comes from |
|---|---|---|
| **Mission** | What we are for and for whom; the sign and the elevator line; the North Star; how we know (what we measure and refuse to) | `goals.md`, `what-this-is.md`, `metrics.md` |
| **Philosophy** | How we weigh a decision: people first, the member-benefit test, the six questions, who benefits the few vs the many, the look-first decision rule | `people-first.md`, `value-test.md`, `impact-diagnostic.md`, the decision rule |
| **Rules** | What we currently do and don't do to a member: content takedown, data privacy, the opt-out default, who sees who | `ABSOLUTES.md`, `policy.md`, privacy lines in `DECISIONS.md` |
| **Promises to Members** | Surplus goes back to the community; members are the investors and the only ones paid out; no outside capital; no selling member data; fees favour no member | `goals.md` promises, `monetization.md`, `DECISIONS.md` |
| **How We Earn** | How the platform earns, the funding ladder, what the income plan sets | `monetization.md`, `DECISIONS.md` |
| **Voice** | How copy reads: words we use, words we retire, how we sound | `voice-and-tone.md` |

Left where they are: the spine (`nouns`, `verbs`, `model`, `systems/`, `ui/`) is schema and mechanics, not philosophy. Method rules (process absolutes, pipeline) stay in `socialus-ops`; Rules links to them. Entity and legal details stay in `socialus-legal` and appear nowhere here.

## How it is organised

```
socialus-plan/
  foundation/          six generated docs + an index  (read these)
  DECISIONS.md         the ledger every statement traces to (edit this)
  product/             spine and systems, unchanged
  IMAGINE.md  ROADMAP.md  unchanged
```
Each `DECISIONS.md` line gains one tag, `[about: mission|philosophy|rules|promises|earn|voice]`. That tag is how a ruling reaches its doc.

## Format

- Top of every doc: **As of YYYY-MM-DD**.
- Each statement: one line, present tense, dated, no hedging, the newest ruling wins. Example:
  - We currently take no outside capital. (2026-09-12)
  - Members are the investors and the only people paid out. (2026-10-07)
  - We currently take a share of transaction income on member commerce; the income plan sets the rate. (2026-10-07)
  - We currently don't sell member data. (2026-09-12)
  - We currently don't sell visibility by default. (2026-09-30)
- Voice: "we currently do / don't". The only "never" is "never extractive". No personal names, no legal or entity detail.
- A statement with no ruling behind it is not written. An open question is listed once, under "Open", with its date.

## Generated, not maintained

One regen skill per doc: `regen-mission`, `regen-philosophy`, `regen-rules`, `regen-promises-to-members`, `regen-how-we-earn`, `regen-voice`. Each rebuilds its doc whole from tagged `DECISIONS.md` lines (newest wins via `[replaces]`), shows the as-of date, and opens a PR. They run with the Friday launch report and on request. `goals.md` and the docs it absorbs are deleted once the new ones land; git is the archive; the 8 files that cite `goals.md` are repointed.

What the build would involve: tag the 391 lines (an agent pass, a PM spot-check), write six skills, repoint citations, add a lint check that every `foundation/` line has a date and a source.

## Two things to know

1. **Owners vs investors.** The message said members are "the owners". The standing ruling says members are *the investors* and rejects "ownership". The drafts use **investors** until the PM says otherwise.
2. **Voice keeps its original text.** The founder's original voice text is kept verbatim as a source file, not in the generated doc.

## Decision for the PM

- **A (recommended):** the new `foundation/` folder, six generated docs, `goals.md` retired, DECISIONS tagged, regen skills on the Friday run.
- **B:** same six docs, but inside `product/foundation/` (no new folder); only `goals.md` retired, the others stay as sources.
- **C:** three docs only: Mission and Philosophy, Rules and Promises, Voice.
