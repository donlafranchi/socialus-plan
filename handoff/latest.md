# Handoff — 5pm, 2026-10-07

Built from GitHub, not from memory. Overwrite this file at each handoff. The day's per-area list is in `DASHBOARD.md` (Past 12h under each area); the colour view is `dashboard/status-dashboard.html`.

**Beta 11-06: 55 of 68 issues closed. Feature freeze 2026-10-30 (proposed). Beta 2026-11-06, open from the waitlist and signup, Sacramento only (council #1, option B).**

## Open launch-blockers
- **#220 F078** flagged content hides itself and the poster is told why; **#486 F100**, **#487 F101**, **#488 F102** (AI first pass in shadow, the Posts review page, poster answers first). Pieces of all four merged today (below); the issues stay open until their criteria are checked.
- **#246** what one member can read about another (the signed-in half; member tables).
- **#500** the overnight live smoke: **PR #511 is up and CLEAN.** The run (10:30 PT, production) had 55 passes and **one failure**: `ownerBusiness › root` timed out at 30s on `load` at 1280px. Production answered in 0.2–0.8s afterwards, nothing errored or leaked, and it could not be reproduced without the secret. #511 makes the smoke wait for the document, retry once and report a repeat as a problem. If the next overnight run shows the same screen timing out twice, it is a real slow page.

## Waiting on the PM
- **Sentry DSN (#490).** The code merged (#507) and is off until a person creates the free Sentry account and sets `SENTRY_DSN` and `NEXT_PUBLIC_SENTRY_DSN` in Vercel (Production), plus one email alert: `docs/error-tracking.md`. Counsel's Privacy text must list Sentry as a processor. Leave pay-as-you-go off.
- **#484 (tags, #286 + #287) is parked:** DIRTY, `human-review`, cut to After beta by the council. Do not merge it for beta.
- Placeholder copy to judge from today's PRs: the signed-out map sheet, the signup screen, the draft Terms and Privacy text, the purge page.
- Counsel owns the real legal text; each draft lists what counsel must supply (in `src/lib/text-pages.ts`, never rendered).
- The council's tripwires are still **proposed, pending PM**: photos off if #221/#220 are not merged and checked by 10-27; report path only if F100–F102 are not running in shadow by 10-30.

## What merged today, by area (2026-10-07)
- **explore-map:** #479 (Explore remembers the metro, opens on it, one bottom control, neighbourhood search), #482 (teardrop pin for addresses, translucent disc with a count for areas, stacked pins spread), #496 (signed-out Explore is list only; Map opens sign-up), #505 (Following row says Posts), #445 (shared links use www.socialus.org).
- **sign-in-you:** #497 (one signup screen, the zip decides the metro, About/Terms/Privacy drafts live).
- **moderation:** #483 (a sensitive-content report hides at once and texts the operator; each Page photo confirms no children), #494 (a per-metro hide bar, the poster told why), #495 (F100: AI reads each reported photo in shadow), #499 and #506 (reportable Posts, the poster answers first, reporter limits), #509 (F102: posts and uploads record where they came from, deleted after a year), #501 (a report decision failing in Postgres).
- **create-posts:** #492 (private Page composer, calendar stamp, post delete sheet), #493 (the rules agreed before every Publish), #498 and #502 (a post may carry one photo; the Page picture; per-image reports).
- **builders-seed:** #481 (builders wait for the list: the duplicate-Pages cause); **production cleanup done: 21 → 12 active Pages, the 9 copies archived**, backup in `agent-temp/backup-477-duplicate-pages-2026-10-07.json`.
- **ops:** #507 (error tracking, off until a DSN), #508 (a removed photo can be deleted for good: `/admin/reports/purge`, operator only), #510 (only main creates a Vercel deployment), #504 (required checks report on docs-only PRs).
- **Migrations applied to production today (in order):** `20261007170000` default metro, `…200000` signup fields, `…250000` photo purge (the others on main came from other lanes).

## Open PRs
- **#511** (#500 smoke fix): CLEAN, merge.
- **#484** (tags): parked, see above.

## Next shift
- Merge #511; watch the 10:30 overnight smoke.
- #443 member bug reports: only the in-app control, private table and scrub can be built without secrets; the GitHub issue creation and the triage Action need a GitHub token and an Anthropic key with a hard spend cap from the PM.
- #491 follow-up: wire post photos (#460) into purge (same bucket and policy).
- #222 follow-ups: the national zip crosswalk (only Sacramento's 126 zips resolve; other zips go to the waitlist step) and changing the zip on `/you`.
- Not done, and said so: Playwright was not run locally on any of today's PRs (Docker stack belongs to another lane); CI covers it. The Vercel deployment cap (100/day) was hit by branch pushes before #510.
- Machine note: `node_modules` in several worktrees had been replaced by a dangling symlink; re-seed with `cp -cR` from a healthy worktree before building.
