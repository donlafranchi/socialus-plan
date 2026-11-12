# Your to-do list

Everything only you can do: set-up, accounts, calls and reviews, now and before launch. App features are not here; ask an agent "what's next" for those.

Agents keep this list. When you finish something, say so and the line is deleted; git keeps the history. Steps live behind each link, never here.

## Focus: the landing page and the waitlist

The PM, 2026-11-12: get the landing page out with a "Join the waitlist" button that asks whether someone runs a business, store, shop, market or group or is looking for those, plus their zip; review the whole join journey before it's built; stay closed until everything is set up. Your part, in order:

1. **Pick how the waitlist checks the mobile number.** A (recommended): a texted code when they join, about 7 cents each. B: checked only when they accept the invite. C: number unchecked, invite by email. Then hand the storyboard to your copywriter for imagery. [Brief and storyboard](planning/briefs/waitlist-join-journey-2026-11-12.md)
2. **Pick the landing headline (parked by you 2026-11-12).** A (recommended): "SocialUs, for the people." B: "SocialUs, a platform for the people." C: "SocialUs, by the people, for the people." Under it: "A place for locals to find and support locals, wherever you are, wherever you go."
3. **Add socialus.org to Resend.** For the urgent-report alert, and the waitlist invite only if you pick C. Free tier: 100 a day. [Steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#6-transactional-email)
4. **Write the positive posting reminder:** one line that encourages good, decent posts. A marked placeholder holds its place.
5. **Walk the waitlist on your phone** at the live socialus.org link agents send, signed in as operator, and say what felt wrong. Only you and builders see it until you approve.
6. **Pick the Northern California counties (A, B or C),** now or once waitlist counts come in. [Options](planning/research/northern-california-2026-11-06.md)
7. **Open a Twilio account and create a Verify service (no number to buy).** The waitlist needs it if you pick A or B. [Steps](https://github.com/donlafranchi/socialus-web/issues/707)

Later, not now: whether reported or repeat accounts are asked for a photo ID.

Agents' part: the waitlist journey built behind the flag, one live link per screen; screening every post before it publishes (in shadow first); the safety line and its ⓘ on the number screen.

## Everything else, in order

1. **Run the report test with three accounts.** Proves the AI first read on reports. [Steps](https://github.com/donlafranchi/socialus-web/issues/220)
2. **Decide the one-strike policy.** How we treat people trying to get over. [Options](planning/research/one-strike-2026-11-06.md)
3. **Open the remaining accounts:** Sentry (error alerts; the code is built and waits for its key), Vercel Speed Insights, a free HUD account (web #849), Cloudflare image safety (child-safety scanning no longer needs an NCMEC account, so it can go on now), and a free UptimeRobot account with two monitors so you hear when the site is down ([steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#12-uptime-monitoring)). Also file the private Supabase support ticket.
4. **Make your Mac's knowledge key** (`gh workflow run knowledge-keys.yml -R donlafranchi/socialus-web -f action=add -f agent=mac`), then Keychain and `~/.zshrc`.
5. **Talk with 5 people who have tried SocialUs.** Real evidence for the next calls. [Plan](planning/research/founding-circle-2026-10-21.md)
6. **Review three small PRs:** edit link, meet-up seeding, shelves. [First one](https://github.com/donlafranchi/socialus-web/pull/1071)
7. **Read the wording waiting for you:** decency lines, Remind me, search card. [Wording](planning/research/rules-review-2026-10-25.md)
8. **React to ideas:** scouts, artists, outer counties, outreach. [Ideas](planning/research/local-creators-2026-10-21.md)

Low priority: in Cloudflare, delete the leftover Worker named socialus-plan-dashboard.

## Before launch (production, April to May 2027)

| When | What | Why |
|---|---|---|
| Early 2027 | **Form the company (LLC).** Specifics live in socialus-legal. | Commercial hosting terms, child-safety registration and card payments all need it |
| After the company, by 2027-04-01 | **Register with the NCMEC CyberTipline** and switch off the manual form. [Runbook](https://github.com/donlafranchi/socialus-ops/blob/main/runbooks/staff-safety.md) | Required reporting; the beta uses the public form, which can't take images |
| From 2027-03-01 | **Re-review paid tools now that budget opens:** feature flags, GitHub and Vercel plans. [Runbook](https://github.com/donlafranchi/socialus-ops/blob/main/runbooks/go-live-paid-tools.md) | We built our own until there was money |
| Two weeks before launch, or sooner if a load test shows a plan limit | **Upgrade Vercel to Pro** ($20 a month per person). [Steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#1-hosting-and-cdn) | The free plan forbids commercial use |
| Two weeks before launch, or sooner if a load test shows a plan limit | **Upgrade Supabase to Pro** ($25 a month), spend cap on. [Steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#2-database-and-auth) | Free pauses after a quiet week; Pro adds daily backups |
| Two weeks before launch | **Mapbox production key,** locked to socialus.org. [Steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#4-maps-and-geocoding) | A key anyone can copy bills you |

About $48 a month in all at launch, before usage.
