# Your to-do list

Everything only you can do: set-up, accounts, calls and reviews, now and before launch. App features are not here; ask an agent "what's next" for those.

Agents keep this list. When you finish something, say so and the line is deleted; git keeps the history. Steps live behind each link, never here.

## Focus: the landing page and early sign-up

The PM, 2026-11-12: get "the landing page and early sign-up workflow dialed in while we wait to launch." Your part, in order:

1. **Set up Twilio for the phone check.** The sign-up phone check can't run without it; it also unblocks posting without a Page. [Steps](https://github.com/donlafranchi/socialus-web/issues/707)
2. **Pick what a visitor without an account can see** (A, B or C, in chat). Decides what the landing page and a shared link show before sign-up.
3. **Pick the Northern California counties (A, B or C).** Decides which zips open at sign-up and which join the waiting list. [Options](planning/research/northern-california-2026-11-06.md)
4. **Add socialus.org to Resend,** so sign-up emails come from our own address. [Steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#6-transactional-email)
5. **Sign up on your phone as a stranger would,** from socialus.org, once the agents' pass below is merged, and say what felt wrong.

Agents' part: a pass over the landing page and sign-up, end to end, listing every gap; the landing page and the join page rewritten to the one-line message ruled 2026-11-06; fixes for the well-worn gaps, and anything new brought to you as A/B/C.

## Everything else, in order

1. **Create the write token** (`KNOWLEDGE_WRITE_TOKEN`, contents and pull requests read and write, on socialus-plan and socialus-ops). Turns on your three answers page and the nightly packs.
2. **Create the backup key,** then start the first backup and its restore test. Until then the nightly backup fails and opens a bug each night. [Steps](https://github.com/donlafranchi/socialus-web/issues/1259)
3. **Run the report test with three accounts.** Proves the AI first read on reports. [Steps](https://github.com/donlafranchi/socialus-web/issues/220)
4. **Decide the one-strike policy.** How we treat people trying to get over. [Options](planning/research/one-strike-2026-11-06.md)
5. **Open the remaining accounts:** Sentry (error alerts; the code is built and waits for its key), Vercel Speed Insights, a free HUD account (web #849), Cloudflare image safety, and a free UptimeRobot account with two monitors so you hear when the site is down ([steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#12-uptime-monitoring)). Also file the private Supabase support ticket.
6. **Make your Mac's knowledge key** (`gh workflow run knowledge-keys.yml -R donlafranchi/socialus-web -f action=add -f agent=mac`), then Keychain and `~/.zshrc`.
7. **Talk with 5 people who have tried SocialUs.** Real evidence for the next calls. [Plan](planning/research/founding-circle-2026-10-21.md)
8. **Review three small PRs:** edit link, meet-up seeding, shelves. [First one](https://github.com/donlafranchi/socialus-web/pull/1071)
9. **Read the wording waiting for you:** decency lines, Remind me, search card. [Wording](planning/research/rules-review-2026-10-25.md)
10. **React to ideas:** scouts, artists, outer counties, outreach. [Ideas](planning/research/local-creators-2026-10-21.md)

Low priority: in Cloudflare, delete the leftover Worker named socialus-plan-dashboard.

## Before launch (production, April to May 2027)

| When | What | Why |
|---|---|---|
| Early 2027 | **Form the company (LLC).** Specifics live in socialus-legal. | Commercial hosting terms, child-safety registration and card payments all need it |
| After the company, by 2027-04-01 | **Register with the NCMEC CyberTipline,** switch off the manual form, turn on Cloudflare child-safety scanning. [Runbook](https://github.com/donlafranchi/socialus-ops/blob/main/runbooks/staff-safety.md) | Required reporting; the beta uses the public form, which can't take images |
| From 2027-03-01 | **Re-review paid tools now that budget opens:** feature flags, GitHub and Vercel plans. [Runbook](https://github.com/donlafranchi/socialus-ops/blob/main/runbooks/go-live-paid-tools.md) | We built our own until there was money |
| Two weeks before launch, or sooner if a load test shows a plan limit | **Upgrade Vercel to Pro** ($20 a month per person). [Steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#1-hosting-and-cdn) | The free plan forbids commercial use |
| Two weeks before launch, or sooner if a load test shows a plan limit | **Upgrade Supabase to Pro** ($25 a month), spend cap on. [Steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#2-database-and-auth) | Free pauses after a quiet week; Pro adds daily backups |
| Two weeks before launch | **Mapbox production key,** locked to socialus.org. [Steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#4-maps-and-geocoding) | A key anyone can copy bills you |

About $48 a month in all at launch, before usage.
