> **SETTLED — do not re-raise:** members are the investors and the only people paid out. "Ownership, not profit-share" is rejected. Legal/securities questions about this go to `socialus-legal` for counsel and never come back to the PM as a decision. SocialUs takes transaction income; any 'no fee' language is retired.

# Beta · beta runs until April 2027 · criterion roll-up: 215/324 criteria met (66%), checked 132, reviewed 32, smoked 59, PM looked 0 across 37 features, 2 red, 10 reports stale · Issues closed 147/170 (alongside, not the headline) · updated 2026-10-30 12:38 PT

**The dashboard is a web page: [https://donlafranchi.github.io/socialus-plan/](https://donlafranchi.github.io/socialus-plan/)** (generated daily; also `dashboard/status-dashboard.html`). This file only points to it.

## The numbers

- 🟢 build: main CI passing
- 🟢 site: last deploy health run passed
- 🟢 migrations: repo and database agree (last drift check on main)
- 🔴 criteria 66%: 215 of 324 met, 2 launch-blocking unmet
- 🟡 waiting on you: 18 items; oldest wait not read yet
- 🟡 docs: 64 undated (target under 5)
- 🔴 agent safety: 1 flags
- Built since last look: 15 PRs merged, 86 criteria newly met, 25 lost, last 7 days, no look recorded yet
- Upcoming: Now: 21 being built · Next: 9 settled · Considering: 13 · Later: 61
- Needs your attention: 1 of 18: Fill in your Page: basics, address, tags and phone (as the owner of your test Page, about…
- What to test: Next walk-through: 3 min, as a member. 0 of 23 done
- Accounts, keys and APIs: 6 to set up before beta
- Risks and deadlines: 0 due soon
- Agent safety: 1 things agents removed or weakened

**How fast it feels: Red** (4 member screen(s) red, 2 amber); slowest: Bottom nav → Explore [settled] 2336 ms, Explore post card → Page post [quick] 1239 ms, Explore card → Page (member) [quick] 1043 ms

## Your to-do (1)

- P1 · Review the one-page rules list (wording only)

*Agents: the lanes are `python3 scripts/going.py --list now` (or next, considering, later); the criteria and areas are on the page.*

## Meta-layer trial

### Meta-layer trial (tuning the scores)

Why: "stick with this and keep improving it" (trial started 2026-10-10). Tracker: https://github.com/donlafranchi/socialus-ops/issues/89

**Trial health: on schedule.** 3 of 3 built scores read within the last 8 days: score-ci-health (2026-10-30); score-doc-drift (2026-10-30); score-gap-leakage (2026-10-30).

Meta PRs: 9 proposed, 5 approved and merged, 0 rejected, 4 open. Bookkeeping (renames, lists, counts) merged without the PM: 8.

Scores that moved: score-ci-health/ci_main_fail_pct: 32.2 (red) -> 25.9 (red); score-ci-health/ci_pr_first_run_fail_pct: 40.0 (none) -> 37.7 (none); score-ci-health/smoke_red_pct: 20.0 (none) -> 0.0 (none); score-doc-drift/drift_items: 96 (red) -> 37 (red); score-gap-leakage/unchecked_built_pct: 42.1 (amber) -> 37.4 (amber); score-gap-leakage/untracked_unmet: 26 (red) -> 29 (red)

Not built yet: `score-review-coverage`, `score-rework`, `score-pm-overrule`. Next: `score-review-coverage`, waiting on a PR-label scan; can start any time, needs `record-pm-review` in use for the PM-look half.

Tuning notes (2026-10-30):
- **Is each score measuring what it should? (false reds and misses, with examples)** **score-ci-health: overall red; the headline red is last week's burst leaving the window, and the one real miss is in the smoke count.** `ci_main_fail_pct` 25.9% red (was 32.2): **mostly false, and dated.** 30 of 116 finished CI runs on main failed. Reading every red run's failed steps (`gh api .../runs/<id>/jobs`): 22 failed *only* "Every migration here is already in the database", all between 2026-10-16 18:00 and 1
- **What to adjust (threshold, source, formula)** Open, `meta-change`, for the PM: **PR #151 (new): scheduled runs listed per workflow**, so the smoke window is whole (0 of 5 becomes 2 of 14; the band finally applies). PR #142: the migration gate counted apart. PR #134: gap-leakage excludes retired and spec-conflict and adds `closed_issue_unmet`. PR #133: doc-drift reads the README's standard header, the skill count and `handoff/state.md`. Four PRs now wait; #133 an
- **Which score to build next** `score-review-coverage`, unchanged, and it got more urgent: the roll-up's Reviewed column is 28 of 252 (11%), `review-pr-bundle` was retired on 10-26 (#1097, skills #44) in favour of a second-session GitHub review under `REVIEW.md`, and #1075 says a mechanical review check returns "when the reviewer has its own GitHub identity". A score that counts, per merged PR touching `src/app`, `src/components`, `src/actions` or

Doc gardening (`tend-docs`, 2026-10-30): 145 docs in scope, 0 duplicate, 65 undated, 94 without the standard header, 1 broken links, hand-written share 84%.

**Tuning review is due (2026-10-24):** for each score, is it measuring what it should (false reds and misses, with examples), what to adjust (threshold, source, formula), and which score to build next.
