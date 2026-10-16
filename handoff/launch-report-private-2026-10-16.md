# Not yet, and how close

**Launch checklist: nothing DUE.** (Dated reminder below fires at entity setup or production launch.)

**Bottom line: beta (2026-11-06, freeze 2026-10-30) is about 3 weeks out and the risk is checks and reviews, not missing features.** 188 of 285 criteria are built (66%) across 34 of 34 features reporting, but only 93 are checked, 28 reviewed, 0 looked at by you. 8 features are red for an unmet launch-blocking criterion (F076, F078, F081, F082, F093, F100, F102, F103). [V: rollup.json 2026-10-16; the dashboard headline says "2 red", a different rule, see tuning notes]

**Your calls this week (at most 3):**
1. **Delete the 32 per-ticket files in `socialus-web/build-log/2026-W42/`?** A: delete (the criterion reports hold the evidence, the skill calls them retired). B: keep as history and exempt from doc checks. Recommend A.
2. **Keep or delete the two retired tombstones** `product/foundation/goals.md` and `role-language.md`? Rulings cite `role-language.md` by name. A: keep both. B: delete `goals.md` only (the Charter replaced it). Recommend B.
3. **Needs-pm Issues** (one line each): drop the "Recurring" filter (#827, recommend drop); drop the owner-panel switch (#831, recommend drop); "free" as a tag (#832, recommend a tag); remove the "Default metro" row for beta (#848, recommend remove); HUD token (#849).

## Table A: beta scope (launch-blocking, open)
| Item | State | Blocker | Owner |
|---|---|---|---|
| F081 signup checks (#851-857) | partly: 9 of 9 built, checks missing | agents | agent |
| F082 rules agreement (#839, #840) | partly: 9 of 9 built, guard and checks missing; rules wording is draft | agents; your wording | agent / you |
| F078/F080/F100/F102/F058 checks (#833-838) | partly: built, tests do not claim the criterion | agents | agent |
| F100 AI first pass (#486), F078 courtesy notice (#220) | open | Twilio, Cloudflare scanning (#641) | you |
| F103 market and zip (#848-850) | partly: 4 of 7 built | your two calls (#848, #849) | you |
| F076 zip check (#843), F093 (#844) | partly | agents | agent |
| Tap speed (#791) | open: tap-speed red today | agents | agent |
Source: open `launch-blocking` Issues, 2026-10-16 [V].

## Table B: wanted, not built, not overtaken
| Item | Why wanted | Size |
|---|---|---|
| F074 weekly series | owners post repeating events | large (1 of 8 built, off in production) |
| F064 asks for what is not built | learn demand | medium (0 of 5) |
| F104-F106 | on the roadmap | 0 of 5 each |
| F114 test member with history | testing freshness | 0 of 6 |
[V: reports]

**Verdict:** beta date holds if the 18 check/guard tickets and the two F103 calls land this week; biggest risk is that "built" outruns "checked and reviewed" (reviewed 28 of 285), plus Twilio and Cloudflare setup that only you can do.

**Criterion roll-up:** 188 of 285 met · 34 of 34 features reporting · 8 red · 0 of 22 phone journeys ticked (next: J13, J10, J07, J20). Gaps filed this run: about 35 Issues (#824-857), 7 needs-pm.

**Doc gardening:** 127 docs in scope, duplicates 0 (was 3), undated 63 (was 57; counting more files), no standard header 91, hand-written 83%. Mechanical headers merged in three repos.

**Next action for you:** answer the three calls above; approve or reject the two open `meta-change` PRs (socialus-ops #133, #134).

### Launch checklist

- Fires at entity setup (expected early 2027) or production launch (expected April-May 2027), whichever comes first: Register SocialUs with the NCMEC CyberTipline, switch off the manual form, enable Cloudflare CSAM scanning. (167 days to the date trigger.)

### Meta-layer trial (tuning the scores)

Why: "stick with this and keep improving it" (trial started 2026-10-10). Tracker: https://github.com/donlafranchi/socialus-ops/issues/89

**Trial health: on schedule.** 3 of 3 built scores read within the last 8 days: score-ci-health (2026-10-16); score-doc-drift (2026-10-16); score-gap-leakage (2026-10-16).

Meta PRs: 7 proposed, 5 approved and merged, 0 rejected, 2 open. Bookkeeping (renames, lists, counts) merged without the PM: 8.

Scores that moved: score-ci-health/scheduled_red: 0 (green) -> 1 (amber); score-ci-health/smoke_red_pct: 66.7 (red) -> 25.0 (none); score-doc-drift/drift_items: 11 (red) -> 97 (red); score-gap-leakage/closed_parent_unmet: 16 (red) -> 13 (red); score-gap-leakage/unchecked_built_pct: 74.5 (red) -> 52.7 (amber); score-gap-leakage/untracked_unmet: 21 (red) -> 23 (red)

Not built yet: `score-review-coverage`, `score-rework`, `score-pm-overrule`. Next: `score-review-coverage`, waiting on a PR-label scan; can start any time, needs `record-pm-review` in use for the PM-look half.

Tuning notes (2026-10-16):
- **Is each score measuring what it should? (false reds and misses, with examples)** **score-ci-health: overall red, mostly real.** `ci_main_fail_pct` 19.4% red: **mixed.** 26 of 134 runs on main failed. Three on 2026-10-16 were real and self-healed within the hour: `Vitest` failed on `src/lib/migrations/manifest.test.ts` (migration 20261016150052 landed without its manifest; fixed by #817), and run 38921301005 failed the "migrations applied to production" gate by design (it said apply first). Two on
- **What to adjust (threshold, source, formula)** Open: PR #133 (doc-drift reads the README's As-of line, skill count, `handoff/state.md`), PR #134 (gap-leakage excludes spec-conflict and retired, adds `closed_issue_unmet`). Both `meta-change`, left open for the PM. Not yet a PR: make the doc inventory and tend-docs exempt the same paths (`build-log/W\d`), once the PM rules on the build-log files. Not yet a PR: add `main_red_minutes` (time from a red main CI run to 
- **Which score to build next** `score-review-coverage`: a PR-label scan that can start now; no new dependency. (`score-rework` and `score-pm-overrule` wait on PM ticks: 0 of 285 criteria are PM-looked, 0 of 22 journeys ticked.)

Doc gardening (`tend-docs`, 2026-10-16): 127 docs in scope, 0 duplicate, 63 undated, 91 without the standard header, 0 broken links, hand-written share 83%.

Tuning review: 2026-10-24 (8 days). Each Friday: false reds and misses with examples, what to adjust, which score next.
