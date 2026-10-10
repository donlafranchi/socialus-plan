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

## Revised: one page, not six (the PM asked for light)

**Precedents, fetched 2026-10-10:** all three put mission, principles and commitments on **one page**.
- Wikipedia's [Five Pillars](https://en.wikipedia.org/wiki/Wikipedia:Five_pillars): five headed statements, including "no firm rules".
- The co-operative movement's [Statement on the Cooperative Identity](https://www.ica.coop/en/cooperatives/cooperative-identity): a definition, six values, seven principles. The closest match to members who are investors.
- Mozilla's [Manifesto](https://www.mozilla.org/en-US/about/manifesto/): a short mission, 10 one- or two-sentence principles, and a pledge.
Path: well-worn. Copy that shape.

**One doc, called the Charter.** (Not "foundation"; rename freely: Commitments, Our Promise.) About 40 lines, five sections:

| Section | Holds |
|---|---|
| Mission | One sentence on what we are for and for whom; the North Star |
| What we believe | The few principles we weigh decisions by (members first, look first, who benefits the many) |
| Promises to members | Surplus goes back; members are the investors and the only ones paid out; no outside capital; no selling member data |
| What we do and don't | The rules for how the platform treats a member (takedown, data privacy, opt-out default) and how we earn |
| Where to read more | Links, not copies: Voice guide, the ontology, the method |

**Cap:** at most 40 statements. If a regen would go over, it stops and asks which to merge. That is what keeps it light.

**Stays separate, not folded in:** `voice-and-tone.md` (a 190-line style guide for writers, not a statement), the spine and ontology (below), `DECISIONS.md` (the ledger the Charter is built from), method rules in `socialus-ops`.

## Is it a duplicate of the ontology?

No. They answer different questions and do not overlap.
- **Charter:** *why* and *what we stand for*. Nothing in it defines a noun.
- **Ontology** (`nouns.md`, `verbs.md`, `src/ontology/*`): *what exists* in the product (Member, Page, post) and how it connects. The Charter links to it and never restates it.
- Real duplication on the ontology side (`nouns.md` and `objects.ts` and `registry.json`) is already handled: the registry is generated from code.
- Where the Charter overlaps today is `goals.md` and `what-this-is.md` defining the product in prose; the Charter keeps one sentence and points to the ontology.

## Format (unchanged)

As-of date at the top. One line per statement, present tense, dated, newest wins, "we currently do / don't", the only "never" is "never extractive". No legal or entity detail, no personal names. A line with no ruling behind it is not written.

## Generated, not maintained

One skill, `regen-charter`: reads `DECISIONS.md` lines tagged `[charter: mission|belief|promise|rule]` (newest wins via `[replaces]`), rebuilds the page whole, shows the as-of date, opens a PR. Runs with the Friday launch report and on request. `goals.md` is deleted when it lands and its 8 citations repointed.

Build: tag the lines that belong (an agent pass; the PM spot-checks), write one skill, repoint citations, add a lint cap and a date-and-source check.

## Two things to know

1. **Owners vs investors.** The message said members are "the owners". The standing ruling says members are *the investors* and rejects "ownership". The drafts use **investors** until the PM says otherwise.
2. **Voice keeps its original text.** The founder's original voice text is kept verbatim as a source file, not in the generated doc.

## Decision for the PM

- **A (recommended):** one Charter page as above, one regen skill, `goals.md` retired.
- **B:** keep six separate docs (the earlier version of this note).
- **C:** the Charter, but keep `goals.md`'s name and make it the generated page.
