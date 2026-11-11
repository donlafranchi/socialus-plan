# Your to-do list

Everything only you can do: set-up, accounts, calls and reviews, now and before launch. App features are not here; ask an agent "what's next" for those.

Agents keep this list. When you finish something, say so and the line is deleted; git keeps the history. Steps live behind each link, never here.

## Now, in order

1. **Set up Twilio for the phone check.** Unblocks posting without a Page and the sign-up phone check. [Steps](https://github.com/donlafranchi/socialus-web/issues/707)
2. **Create the write token** (`KNOWLEDGE_WRITE_TOKEN`, contents and pull requests read and write, on socialus-plan and socialus-ops). Turns on your three answers page and the nightly packs.
3. **Create the backup key,** then start the first backup and its restore test. Until then the nightly backup fails and opens a bug each night. [Steps](https://github.com/donlafranchi/socialus-web/issues/1259)
4. **Run the report test with three accounts.** Proves the AI first read on reports. [Steps](https://github.com/donlafranchi/socialus-web/issues/220)
5. **Decide the one-strike policy.** How we treat people trying to get over. [Options](planning/research/one-strike-2026-11-06.md)
6. **Open the remaining accounts:** Sentry (error alerts; the code is built and waits for its key), Vercel Speed Insights, Resend (add socialus.org), a free HUD account (web #849), Cloudflare image safety. Also file the private Supabase support ticket.
7. **Make your Mac's knowledge key** (`gh workflow run knowledge-keys.yml -R donlafranchi/socialus-web -f action=add -f agent=mac`), then Keychain and `~/.zshrc`.
8. **Talk with 5 people who have tried SocialUs.** Real evidence for the next calls. [Plan](planning/research/founding-circle-2026-10-21.md)
9. **Say "go" on the new message,** "Locals, finding and supporting locals". Unblocks the landing page and the join page.
10. **Pick the Northern California counties (A, B or C).** [Options](planning/research/northern-california-2026-11-06.md)
11. **Review three small PRs:** edit link, meet-up seeding, shelves. [First one](https://github.com/donlafranchi/socialus-web/pull/1071)
12. **Read the wording waiting for you:** decency lines, Remind me, search card. [Wording](planning/research/rules-review-2026-10-25.md)
13. **React to ideas:** scouts, artists, outer counties, outreach. [Ideas](planning/research/local-creators-2026-10-21.md)

Low priority: in Cloudflare, delete the leftover Worker named socialus-plan-dashboard.

## Before launch (production, April to May 2027)

| When | What | Why |
|---|---|---|
| Early 2027 | **Form the company (LLC).** Specifics live in socialus-legal. | Commercial hosting terms, child-safety registration and card payments all need it |
| After the company, by 2027-04-01 | **Register with the NCMEC CyberTipline,** switch off the manual form, turn on Cloudflare child-safety scanning. [Runbook](https://github.com/donlafranchi/socialus-ops/blob/main/runbooks/staff-safety.md) | Required reporting; the beta uses the public form, which can't take images |
| From 2027-03-01 | **Re-review paid tools now that budget opens:** feature flags, GitHub and Vercel plans. [Runbook](https://github.com/donlafranchi/socialus-ops/blob/main/runbooks/go-live-paid-tools.md) | We built our own until there was money |
| Two weeks before launch | **Upgrade Vercel to Pro** ($20 a month per person). [Steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#1-hosting-and-cdn) | The free plan forbids commercial use |
| Two weeks before launch | **Upgrade Supabase to Pro** ($25 a month), spend cap on. [Steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#2-database-and-auth) | Free pauses after a quiet week; Pro adds daily backups |
| Two weeks before launch | **Mapbox production key,** locked to socialus.org. [Steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#4-maps-and-geocoding) | A key anyone can copy bills you |

About $48 a month in all at launch, before usage.
