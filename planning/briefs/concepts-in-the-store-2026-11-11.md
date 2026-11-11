---
id: brief-2026-11-11-concepts-in-the-store
status: awaiting-approval
size: M
path: new territory
criteria:
  - A concept keeps one id across every rename; its old names are listed with the date and the ruling that changed each, and refused names stay recorded as refused.
  - Each change to a concept's shape is an event of one type (idea, scoped, ruling, renamed, split, merged, cut, deferred, built, reversed) pointing at its evidence (a plan commit, a criterion, a web PR), with the PM's words in their own field.
  - Split, merge and became links survive the source file being archived or deleted.
  - The two traced concepts below load as concepts whose timelines match this brief entry for entry.
  - A check lists every concept whose built state and ruled state disagree.
---

# Concepts in the knowledge store

**As of 2026-11-11** · Source: a read of socialus-plan at origin/main (303 files) and the git history of socialus-plan and socialus-web, 2026-11-11 · Maintained by: hand (brief; deleted at 30 days or once ruled and placed)

*The PM, 2026-11-11:* "we will have a concept and begin work on it. as the concept emerges many changes emerge and what we originally thought we were going to do looks somewhat similar to the original but with many many changes."

**Bottom line: add one kind, the concept, with a stable id, a name history and a timeline of typed events; load the two concepts traced below and IMAGINE's 41 ideas first, then let scenarios become versions of their concept.**

## What the planning repo holds today

- 303 files, about 2.5 MB. About 530 KB is generated views and 270 KB is scripts; neither moves.
- Already fit existing kinds: 73 scenarios (features, about 537 criteria, about 354 rulings), principles and absolutes, nouns and verbs, accepted risks, 16 open questions.
- Need a new kind: IMAGINE's 41 ideas, 14 system docs, the screens list, 43 research notes, use cases, metrics, 26 phone walk-throughs, launch-checklist tasks.
- Should leave: design assets belong in socialus-design; the council intake belongs in socialus-ops; product/README.md and the briefings become queries; UNPLACED.md is empty.

## Two concepts as they actually changed

**Bulletins, then Announcement, then Post** (one id, three names)
- 2026-04-25 built: vendor bulletins with tracking (web 91fdacb2), before any plan doc.
- 2026-05-11 cut: the migrations were wiped (plan 993e447).
- 2026-06-29 split: "bulletin intelligence" spun off; still in IMAGINE.
- 2026-09-09 ruling: the table is `page_posts`, not `bulletins` (plan ff620da).
- 2026-09-13 split: one scenario became four, F072 to F075 (plan 348bc1e).
- 2026-09-20 cut: delivery to followers' feeds, to pay for recurrence (plan cd98014).
- 2026-09-21 renamed: Announcement; Bulletin refused as a noun (plan 3152305).
- 2026-10-01 renamed: Post (plan 3277f66). The PM: "an announcement is a post".
- 2026-10-18 built, reversed: push for followed Pages' new posts (web #930), ruled a week later.
- What survived: the intent, a Page reaching its followers, came back as push. The word, the table and the tracking did not. Two needs docs still say "Bulletins, cut".

**Open your town** (one id, three names)
- 2026-06-22 idea: communities unlock a market by meeting public thresholds, 50, 10 and 3 (plan 20b2c4d).
- 2026-09-07 cut: archived with the markets mechanic.
- 2026-09-14 scoped and built: a metro opens on 50 creators and 250 patrons (F076; web #86).
- 2026-10-11 scoped: a market opens on sign-ups, counties as the unit (F103).
- 2026-10-26 renamed and scoped: "Open your town", 100 and 1000 and three towns (F118); built early by mistake (web #1093).
- 2026-10-27 deferred: behind a flag until after soft launch.
- 2026-10-31 ruling: recognition only, no cash or perks.
- What survived: most of the June idea came back, with the numbers ten times larger and no organizer role. F118 does not link back to June.

## What the store needs

- **A concept record** that outlives its names, with each name dated and tied to the ruling that changed it.
- **Events** of one type each, with evidence and the PM's words, so the timeline above is a query instead of a git dig.
- **Shape versions** linked to the ruling that set them and the one they replaced, the way `[replaces …]` works today; parts can be cut and brought back separately.
- **Lineage links** (split, merged, became) that hold when a file is deleted.
- **A drift check:** built against ruled, and docs that still say cut after something came back.

## Options

- **A. Concepts first (recommended):** add the concept kind and events; load these two concepts and IMAGINE's 41 ideas as concepts with status idea; link scenarios to their concept as it is touched. Proves the model on real history; IMAGINE.md, now over its size limit, empties into the store.
- **B. Move everything at once:** all eight new kinds and every planning doc in one import. The repo shrinks fastest; the most to build and check before anything is proven.
- **C. IMAGINE only:** its ideas become records and nothing else changes. Smallest; leaves concept history in git.

**How A would be measured:** time to answer "how did this concept change and why" for a concept (a git dig of about 20 tool calls today against one query), and drift items found by the check.
