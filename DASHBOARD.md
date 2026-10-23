> **SETTLED — do not re-raise:** members are the investors and the only people paid out. "Ownership, not profit-share" is rejected. Legal/securities questions about this go to `socialus-legal` for counsel and never come back to the PM as a decision. SocialUs takes transaction income; any 'no fee' language is retired.

# Beta 11-06 · 7 days to freeze · criterion roll-up: 195/291 criteria met (67%), checked 116, reviewed 29, smoked 172, PM looked 0 across 34 features, 5 red, 1 reports stale · Issues closed 137/162 (alongside, not the headline) · updated 2026-10-23 10:04 PT

**The dashboard is a web page: [https://donlafranchi.github.io/socialus-plan/](https://donlafranchi.github.io/socialus-plan/)** (generated daily; also `dashboard/status-dashboard.html`). This file only points to it.

## The numbers

- 🟢 build: main CI passing
- 🟢 site: last deploy health run passed
- 🟢 migrations: repo and database agree (last drift check on main)
- 🔴 criteria 67%: 195 of 291 met, 5 launch-blocking unmet
- 🟡 waiting on you: 16 items; oldest wait not read yet
- 🟡 docs: 64 undated (target under 5)
- 🔴 agent safety: 1 flags
- Built since last look: 15 PRs merged, 65 criteria newly met, 24 lost, last 7 days, no look recorded yet
- Upcoming: Now: 20 being built · Next: 7 settled · Considering: 11 · Later: 62
- Needs your attention: 1 of 16: Fill in your Page: basics, address, tags and phone (as the owner of your test Page, about…
- What to test: Next walk-through: 3 min, as a member. 0 of 22 done
- Accounts, keys and APIs: 6 to set up before beta
- Risks and deadlines: Freeze 2026-10-30 · 6 due soon
- Agent safety: 1 things agents removed or weakened

**How fast it feels: Red** (8 member screen(s) red, 3 amber); slowest: Bottom nav → Explore [settled] 2405 ms, Explore card → Page (member) [quick] 1236 ms, Explore post card → Page post [quick] 1157 ms

## Your to-do (29)

- P1 · Run the F078 report test (closes #220) · due 10-27
- P1 · Founding circle: talk with 5 people outside the team who've tried SocialUs · due 11-06
- P1 · Database safety call: A, B or C
- P1 · Review the 8 grade card pass bars (and the weekly-email question)
- P1 · Read the notification wording
- P1 · Look at a Page's Products & services on socialus.org and approve the wording
- P1 · Turn on reminder emails
- P1 · Dark-site businesses: A or B
- P2 · Decide at 10-27: end or extend the AI shadow window · due 10-27
- P2 · Outer counties: A, B or C
- P2 · Turn on Vercel Speed Insights (free tier)
- P2 · Sign up for Sentry (free)
- P2 · Look at the new Explore on your phone
- P2 · Quit and reopen the Claude app
- P2 · Cloudflare hash-check steps
- P2 · IP-purge switch: CONTENT_ORIGINS_PURGE_ENABLED=true
- P2 · HUD account and token for web #849
- P2 · Try notifications on your iPhone
- P2 · Approve the search-sharing switch and the owner's "what locals searched" card
- P2 · Read the Remind me wording
- P2 · Register a HUD account and set the HUD token (web #849)
- P2 · Dark-site outreach: approve the channel and the copy
- P2 · Dark-site outreach: approve the 10-business pilot list
- P2 · Review the local creators idea (one page)
- P3 · The committee model-test plan
- P3 · Should members be able to mark a post as a deal or last-minute?
- P3 · Wording: 'we do not tolerate abusive content'
- P3 · Each month: the notifications review
- P3 · Add the Maidu Park market

*Agents: the lanes are `python3 scripts/going.py --list now` (or next, considering, later); the criteria and areas are on the page.*

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
