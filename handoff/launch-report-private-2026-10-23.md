# Not yet, and how close

**Launch checklist: nothing DUE.** Doc: https://claude.ai/artifact/SJu8gGy6EFpQHSJStGScTr
**Bottom line: beta (11-06) holds, but fresh reports found a regression: since the code sign-in (10-18) new members from You, a Page or the nav skip the profile step (#847, #1014).** 195 of 291 criteria met, 116 checked, 29 reviewed, 0 you looked at; 34 of 34 reporting; 5 red (F076, F081, F100, F102, F103) [V].

**Your call (1 of 3):** delete the 32 `build-log/2026-W42/` files? A delete, B keep and exempt. Recommend A. Queued: retired tombstones (delete); PIPELINE.md at 266% (split).

Beta scope [V]: agents: #847, #1014, #1005, #1017, #616, #686, #978. You: F100 (#486: Twilio, Cloudflare, key, 10-27 call), #220 test, #1015, #849, F102.7.

**Verdict:** about 2 weeks; risk is sign-up and review (29 of 291), then Twilio, Cloudflare, the report test.

**Next:** the call above; `pm-approved` on ops #133, #134, #142.

### Launch checklist

- Fires at entity setup (expected early 2027) or production launch (expected April-May 2027), whichever comes first: Register SocialUs with the NCMEC CyberTipline, switch off the manual form, enable Cloudflare CSAM scanning. (160 days to the date trigger.)

### Meta-layer trial (tuning the scores)

Why: "stick with this and keep improving it" (trial started 2026-10-10). Tracker: https://github.com/donlafranchi/socialus-ops/issues/89

**Trial health: on schedule.** 3 of 3 built scores read within the last 8 days: score-ci-health (2026-10-23); score-doc-drift (2026-10-23); score-gap-leakage (2026-10-23).

Meta PRs: 8 proposed, 5 approved and merged, 0 rejected, 3 open. Bookkeeping (renames, lists, counts) merged without the PM: 8.

Scores that moved: score-ci-health/ci_main_fail_pct: 19.4 (red) -> 32.2 (red); score-ci-health/ci_pr_first_run_fail_pct: 19.5 (none) -> 40.0 (none); score-ci-health/smoke_red_pct: 25.0 (none) -> 20.0 (none); score-doc-drift/drift_items: 97 (red) -> 96 (red); score-gap-leakage/closed_parent_unmet: 13 (red) -> 15 (red); score-gap-leakage/unchecked_built_pct: 52.7 (amber) -> 42.1 (amber); score-gap-leakage/untracked_unmet: 23 (red) -> 26 (red)

Not built yet: `score-review-coverage`, `score-rework`, `score-pm-overrule`. Next: `score-review-coverage`, waiting on a PR-label scan; can start any time, needs `record-pm-review` in use for the PM-look half.

Tuning notes (2026-10-23):
- **Is each score measuring what it should? (false reds and misses, with examples)** **score-ci-health: overall red; the headline metric is mostly a false red.** `ci_main_fail_pct` 32.2% red (was 19.4): **mostly false.** 37 of 115 finished CI runs on main failed. Reading every red run's failed steps (`gh api .../runs/<id>/jobs`): 23 failed *only* the step "Every migration here is already in the database", the production-migrations gate that fails by design until a merged migration is applied (runs 39
- **What to adjust (threshold, source, formula)** Open, `meta-change`, for the PM: PR #133 (doc-drift reads the README's As-of line, skill count and `handoff/state.md`); PR #134 (gap-leakage: retired and spec-conflict excluded, `closed_issue_unmet` added, and from today closed parents whose gaps all have open Issues not counted); **PR #142 (new): `ci_main_fail_pct` counts migration-gate-only runs apart** as an unbanded `ci_main_migration_gate`. Not yet a PR: `schedu
- **Which score to build next** `score-review-coverage`: a PR-label scan (`Reviewed by:`, `review-skipped`, `pm-reviewed`) that can start now; this week's roll-up shows the review column is where "built" outruns the method. `score-rework` and `score-pm-overrule` still wait on PM ticks (0 journeys ticked on #519).

Doc gardening (`tend-docs`, 2026-10-23): 132 docs in scope, 0 duplicate, 64 undated, 92 without the standard header, 0 broken links, hand-written share 83%.

Tuning review: 2026-10-24 (1 days). Each Friday: false reds and misses with examples, what to adjust, which score next.
