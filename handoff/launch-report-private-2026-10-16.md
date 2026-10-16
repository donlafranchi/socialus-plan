# Not yet, and how close

**Launch checklist: nothing DUE.**
**Bottom line: beta (2026-11-06) holds if the check tickets land; the risk is "built" outrunning "checked and reviewed".** 188 of 285 built, 93 checked, 28 reviewed, 0 you looked at; 34 of 34 features reporting; 8 red (F076, F078, F081, F082, F093, F100, F102, F103). Wanted, unbuilt: F074, F064, F104-F106, F114.

**Your calls (2):**
1. Delete the 32 per-ticket files in `socialus-web/build-log/2026-W42/`? A delete (reports hold the evidence), B keep. Recommend A.
2. Needs-pm: #827, #831 drop (recommend); #832 "free" as a tag; #848; #849.

**Table A: beta scope (open launch-blocking) [V]**
| Item | State | Blocker | Owner |
|---|---|---|---|
| Checks and guards on 11 features (#833-844, #851-857) | built, untested | none | agent |
| F100 AI first pass (#486), F078 notice (#220) | open | Twilio, Cloudflare (#641) | you |
| F103 market and zip (#848-850) | 4 of 7 | your two calls | you |
| Tap speed (#791) | red today | none | agent |

**Verdict:** about 3 weeks; risk is review (28 of 285), Twilio, Cloudflare.

**Next:** the 2 calls; meta-change PRs ops #133, #134.

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
