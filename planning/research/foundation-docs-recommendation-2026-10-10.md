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

**Closest match: Mozilla's Manifesto.** A mission-driven product written before any formal structure, to say what it stands for and invite contributors: a short mission, a handful of aspirational principles, a pledge. Those are guidelines, not binding rules, which is where SocialUs is (no members yet, no organization yet). Wikipedia's Five Pillars is the second match for how people behave on the platform. The co-op statement is the *later* match: its "member economic participation" and "concern for community" principles are the shape to move to when the organization is formed, not before.

**Timing rule:** the Charter is **guidelines until the organization is formed**. How members share in what the platform earns, and how they take part in running it, are listed as open and decided then. Nothing here names an entity type or legal term (those live in `socialus-legal`).

**Shape (Mozilla's):** Mission, Principles, Pledge. About 15 lines. Cap 40.

## Draft Charter (wording for the PM to approve; new copy goes to the PM first)

> **Charter**, as of 2026-10-10. Guidelines for now: we are early, with no members yet. We firm these up when the organization is formed.
>
> **Mission.** Everything serves people. We help regular people earn a decent living and afford to live well. (2026-09-12)
>
> **Principles**
> 1. We currently weigh each decision for the people using it first; if it doesn't help them, it doesn't ship. (2026-09-12)
> 2. We are never extractive: we don't take value from people without giving something back. (2026-09-12)
> 3. We currently want to succeed first, so we can help members, and to succeed together. (2026-10-04)
> 4. People can do more here. They don't have to. (2026-09-12)
> 5. We currently default to what people would expect socially about who sees what. (2026-09-30)
>
> **Pledge**
> - We currently don't sell member data. (2026-09-12)
> - We currently don't show a member's data beyond what they chose to show. (2026-09-16)
> - We currently put nothing a member contributes live without a report-and-takedown path. (2026-09-16)
> - We currently charge fees that serve the platform and its members and favour no member over another. (2026-09-30)
> - We currently take transaction income on member commerce, at a rate the income plan sets. (2026-10-07)
> - We currently take no outside capital. (2026-09-12)
>
> **Open until the organization is formed.** How members share in what the platform earns. How members take part in running it.
>
> Read more: Voice guide · the ontology · how we build.

Every line traces to a ruling (dates are the ruling's, from `DECISIONS.md`, `goals.md` and `ABSOLUTES.md`). Left out on purpose: the line that members are the investors and the only people paid out. The standing ruling says it, but the PM now says that is decided when the organization forms, so the draft does not state it. The SETTLED banner is a separate, standing ruling and is not touched here.

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

- **A (recommended):** approve this Mozilla-shaped draft as worded. Then I build: write it to `product/charter.md`, add `regen-charter` (rebuilds it from the rulings above and runs with the Friday report), retire `goals.md`.
- **B:** approve it, but also state "members are the investors and the only people paid out" now, as the standing ruling reads.
- **C:** change the wording; reply with edits and I re-draft.
