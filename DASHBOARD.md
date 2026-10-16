> **SETTLED — do not re-raise:** members are the investors and the only people paid out. "Ownership, not profit-share" is rejected. Legal/securities questions about this go to `socialus-legal` for counsel and never come back to the PM as a decision. SocialUs takes transaction income; any 'no fee' language is retired.

# Beta 11-06 · 14 days to freeze · criterion roll-up: 188/285 criteria met (66%), checked 93, reviewed 28, smoked 127, PM looked 0 across 34 features, 2 red, 3 reports stale · Issues closed 102/144 (alongside, not the headline) · updated 2026-10-16 10:04 PT

**The dashboard is a web page: [https://donlafranchi.github.io/socialus-plan/](https://donlafranchi.github.io/socialus-plan/)** (generated daily; also `dashboard/status-dashboard.html`). This file only points to it.

## The numbers

- 🔴 build: main CI failing or unread
- 🟢 site: last deploy health run passed
- 🟢 migrations: repo and database agree (last drift check on main)
- 🔴 criteria 66%: 188 of 285 met, 2 launch-blocking unmet
- 🟡 waiting on you: 13 items; oldest wait not read yet
- 🟡 docs: 63 undated (target under 5)
- 🔴 agent safety: 1 flags
- Built since last look: 15 PRs merged, 54 criteria newly met, 18 lost, last 7 days, no look recorded yet
- Upcoming: Now: 20 being built · Next: 7 settled · Considering: 8 · Later: 59
- Needs your attention: 1 of 13: Start something without opening a shop (as a member, about 3 min)
- What to test: Next walk-through: 3 min, as a member. 0 of 22 done
- Accounts, keys and APIs: 6 to set up before beta
- Risks and deadlines: Freeze 2026-10-30 · 6 due soon
- Agent safety: 1 things agents removed or weakened

## Your to-do (8)

- P1 · Accepted risks review (three due 10-16) · due 10-16
- P2 · Make one test report on a Page you own · due 10-23
- P2 · Reconnect the GitHub connector
- P2 · Outer counties: A, B or C
- P2 · Turn on Vercel Speed Insights (free tier)
- P2 · Sign up for Sentry (free)
- P3 · Look at the new Explore on your phone
- P3 · The committee model-test plan

*Agents: the lanes are `python3 scripts/going.py --list now` (or next, considering, later); the criteria and areas are on the page.*

### Meta-layer trial (tuning the scores)

Why: "stick with this and keep improving it" (trial started 2026-10-10). Tracker: https://github.com/donlafranchi/socialus-ops/issues/89

**Trial health: on schedule.** 3 of 3 built scores read within the last 8 days: score-ci-health (2026-10-16); score-doc-drift (2026-10-16); score-gap-leakage (2026-10-16).

Meta PRs: 7 proposed, 5 approved and merged, 0 rejected, 2 open. Bookkeeping (renames, lists, counts) merged without the PM: 8.

Scores that moved: score-ci-health/scheduled_red: 0 (green) -> 1 (amber); score-ci-health/smoke_red_pct: 66.7 (red) -> 25.0 (none); score-doc-drift/drift_items: 11 (red) -> 97 (red); score-gap-leakage/closed_parent_unmet: 16 (red) -> 13 (red); score-gap-leakage/unchecked_built_pct: 74.5 (red) -> 52.7 (amber); score-gap-leakage/untracked_unmet: 21 (red) -> 23 (red)

Not built yet: `score-review-coverage`, `score-rework`, `score-pm-overrule`. Next: `score-review-coverage`, waiting on a PR-label scan; can start any time, needs `record-pm-review` in use for the PM-look half.

Tuning notes (2026-10-11):
- **Is each score measuring what it should? (false reds and misses, with examples)** `closed_parent_unmet` 16 features, red: **partly false.** 6 of the 16 are scenario Issues in the beta milestone closed with unmet criteria (F081, F082, F099, F101, F102, F080: the real leakage the roll-up audit named). The others are shipped features whose scenario was retired, with criteria reconstructed from git history (F044, F045, F046: 2 to 6 of 5 to 9 met). Those criteria may have been overtaken by newer ruling
- **What to adjust (threshold, source, formula)** Split `closed_parent_unmet` into beta-milestone Issues (the PM's concern) and retired-scenario features (informational), the same split the audit makes. Exclude SPEC-CONFLICT criteria from `untracked_unmet`, and count them as their own metric once the reports mark the status field. Consider dropping `unchecked_built_pct` here and reading it from the roll-up's Checked count instead, so two places do not define it. The
- **Which score to build next** `score-review-coverage`: a PR-label scan that can start now.

Doc gardening (`tend-docs`, 2026-10-16): 127 docs in scope, 0 duplicate, 63 undated, 91 without the standard header, 0 broken links, hand-written share 83%.

Tuning review: 2026-10-24 (8 days). Each Friday: false reds and misses with examples, what to adjust, which score next.
