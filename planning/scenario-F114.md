---
id: F114
title: A test member with six weeks of history, for testing freshness and learning
status: approved
horizon: now
rank: 85
date: 2026-10-12
depends: []
approved: 2026-10-12 — the PM: option A, a separate test account in production with about six weeks of made-up history on real Pages, usable on the PM's phone; its activity counts nowhere and one call wipes it.
---
## Story

The PM signs in on a phone as a test member who has lived in the Sacramento market for six weeks: interests, follows, RSVPs and saves already there, all on real Pages. A second test member with no history shows what a newcomer sees. Nothing either does shows up in a count, a report or a Page's numbers. When testing is done, one call removes both histories and nothing else.

## Acceptance

1. **Two test accounts in production**, flagged as builders (`builders`, `scripts/builders.ts`): *Settled* (with history) and *Newcomer* (none). Each signs in with an address the PM controls, set in private env; no address or real name in the repo.
2. **Settled's home** is a zip in the Sacramento market whose home town has unclaimed Pages.
3. **History, written by `scripts/test-profile.ts`** (dry run unless `--apply`; dates spread over the 42 days before the run; re-runnable without duplicates), against real Pages only, using what exists today:
   - 6 declared interests across the lens axes (food, music, outdoors, makers, wine, free things);
   - 15 Page follows, a third outside the home town;
   - 10 RSVPs (6 past, 4 upcoming, from 3 or more towns) and 8 saves.
   Each later signal (the F109 open log, searches, seen, photo and video opens) gets its own block in the script in the same PR that builds that signal.
4. **Counts nowhere**: none of either account's activity appears in staff counts, reports, the F109 report or a Page's numbers. A test proves it for every count and log that exists, and each new count or log carries the same exclusion in the PR that adds it.
5. **One-call wipe**: `test-profile.ts --wipe` removes both accounts' history and touches no other account's content, including other builders' (a test proves it). Running the script again rebuilds the history.
6. **A checklist in the Issue** says what to try on the phone and what to expect.

## Not this

The operator account. Fake Pages. Seeding other members' history. Any learning beyond what F113 rules.

## Why

- **Lives somewhere better?** No: a test fixture.
- **Only locals know?** No.
- **Gets people together?** Indirectly: freshness and learning get tested on real data before members see them.
- **Stays fresh on its own?** Re-run the script; dates are relative to the run.
- **Who keeps it current?** Nobody between runs.
- **Better as more people join?** No.

**Path: new territory, ruled** (writes to production). Research: `planning/research/explore-freshness-and-learning-2026-10-12.md` § 4.

[platform none]

## Rulings
- **2026-10-12 — The PM's test profile is option A: a separate test account in production, with about six weeks of made-up history on real Pages, usable on the PM's phone. Its activity counts nowhere (counts, reports, Page numbers) and one call wipes it.** The PM, 2026-10-12, on #137. Because testing on real data from a phone must not touch the operator account or any number staff read. [for now] [replaces none] [binds tiers=planning,code surfaces=builders,metrics,privacy build=none]
