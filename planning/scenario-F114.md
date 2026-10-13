---
id: F114
title: A test member with six weeks of history, for testing freshness and learning
status: draft
horizon: considering
rank: 135
date: 2026-10-12
depends: [F112, F113, F115]
---
## Story

The PM signs in on a phone as a test member who has lived in the Sacramento market for six weeks: follows, interests, RSVPs and searches already there. Explore leads with different Pages on two visits a day apart. Home suggests an interest from the history. They type Napa and see it is waiting. A second test member with no history shows what a newcomer sees. When testing is done, one call removes both.

## Acceptance

Not final until the PM picks where it lives (options below). Written to A:

1. **Two builder accounts in production** (`builders`, `scripts/builders.ts`): *Settled* (with history) and *Newcomer* (none). Signed in with a PM test address; no real name in the repo.
2. **Settled's home** is a zip in the Sacramento market with a home town that has wave 1 Pages (F115).
3. **History, written by `scripts/test-profile.ts`** (dry run unless `--apply`), spread over 42 days before the run, against real seeded Pages only:
   - 6 declared interests across the lens axes (food, music, outdoors, makers, wine, free things);
   - 15 Page follows, a third outside the home town;
   - 10 RSVPs: 6 past, 4 upcoming, from 3 or more towns;
   - 40 searches: repeats of 3 themes, plus 6 that find nothing;
   - 150 Explore opens, half in the 3 themes, half spread;
   - 120 photo and video opens across 30 Pages, weighted to 2 categories;
   - 2 pending interest suggestions (F113, if A).
4. **Builder rule holds**: none of it counts in staff counts, the F109 report or a Page's numbers, and `delete_builder_content()` removes it.
5. **A checklist in the Issue** says what to try and what to expect: two visits a day apart, with a card not seen yet leading (F112), a suggestion (F113), a deleted search, the learning switch off, a Napa vantage (F105 criterion 4), a staff preview of Napa (F115).

## Not this

The operator account. Fake Pages. Seeding other members' history. Any learning beyond what F113 rules.

## Why

- **Lives somewhere better?** No: a test fixture.
- **Only locals know?** No.
- **Gets people together?** Indirectly: freshness and learning get tested before members see them.
- **Stays fresh on its own?** Re-run the script; dates are relative to the run.
- **Who keeps it current?** Nobody between runs.
- **Better as more people join?** No.

**Path: new territory** (writes to production). Research: `planning/research/explore-freshness-and-learning-2026-10-12.md` § 3.

**For the PM (A/B/C):**
- A) **A separate production test account, seeded by script** (recommended): real data on the phone; its activity counts nowhere and is wiped in one call.
- B) **The PM's own account**: least setup; mixes test history into the operator account and staff counts.
- C) **Local persona only**: safest; no phone, no regional seed.

[open-question owner=don raised=2026-10-12] Where does the PM's test profile live: a separate production test account whose activity counts nowhere (A), the PM's own account (B), or local only (C)? Recommend A.

[platform none]
