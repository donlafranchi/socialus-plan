> **SETTLED — do not re-raise:** members are the investors and the only people paid out. "Ownership, not profit-share" is rejected. Legal/securities questions about this go to `socialus-legal` for counsel and never come back to the PM as a decision. SocialUs takes transaction income; any 'no fee' language is retired.

# Beta 11-06 · 12 days to freeze · criterion roll-up: 188/285 criteria met (66%), checked 97, reviewed 28, smoked 0, PM looked 0 across 34 features, 2 red, 0 reports stale · Issues closed 105/147 (alongside, not the headline) · updated 2026-10-18 07:44 PT

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
- Upcoming: Now: 20 being built · Next: 7 settled · Considering: 8 · Later: 60
- Needs your attention: 1 of 13: Start something without opening a shop (as a member, about 3 min)
- What to test: Next walk-through: 3 min, as a member. 0 of 22 done
- Accounts, keys and APIs: 6 to set up before beta
- Risks and deadlines: Freeze 2026-10-30 · 6 due soon
- Agent safety: 1 things agents removed or weakened

**How fast it feels: Amber** (0 member screen(s) red, 4 amber); slowest: Bottom nav → Explore [settled] 1540 ms, Explore card → Page [quick] 774 ms, Creator: own Page → edit [settled] 709 ms

## Your to-do (14)

- P1 · Look at the live report flow: make one test report · due 10-27
- P1 · Database safety call: A, B or C
- P2 · Reconnect the GitHub connector
- P2 · Outer counties: A, B or C
- P2 · Turn on Vercel Speed Insights (free tier)
- P2 · Sign up for Sentry (free)
- P2 · Look at the new Explore on your phone
- P2 · Quit and reopen the Claude app
- P2 · Cloudflare hash-check steps
- P2 · IP-purge switch: CONTENT_ORIGINS_PURGE_ENABLED=true
- P3 · AI shadow window: extend past 10-27, or end it · due 10-27
- P3 · The committee model-test plan
- P3 · Should members be able to mark a post as a deal or last-minute?
- P3 · Wording: 'we do not tolerate abusive content'

*Agents: the lanes are `python3 scripts/going.py --list now` (or next, considering, later); the criteria and areas are on the page.*
