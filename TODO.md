# Your to-do list

Everything only you can do: set-up, accounts, calls and reviews, now and before launch. App features are not here; ask an agent "what's next" for those.

Agents keep this list. When you finish something, say so and the line is deleted; git keeps the history. Steps live behind each link, never here.

## Focus: open Sacramento as a beta, Wednesday January 6, 2027

The PM, 2026-11-23: "B." then "Approve launch B". Must-haves only; a private dry run with a few invited testers the week of Dec 28; stickers, item tags and Google/Apple sign-in follow in January; AI chat, values and the blue dot, the pulse map and floating wishes come later. [Brief](planning/briefs/sacramento-launch-campaign-2026-11-22.md) Your part, in order:

1. **By Nov 29: four steps that gate the build.**
   - **Twilio:** open an account and create a Verify service (no number to buy). Phone sign-up can't text a code without it. [Steps](https://github.com/donlafranchi/socialus-web/issues/707)
   - **Resend:** add socialus.org. Waitlist invites, the vendor and patron emails and the urgent-report alert go by email. Free tier: 100 a day. [Steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#6-transactional-email)
   - **Supabase Pro** ($25 a month), spend cap on: free pauses after a quiet week and has no daily backups. [Steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#2-database-and-auth)
   - **Alert steps:** finish monitoring (Sentry, Vercel spend, UptimeRobot), item 3 under "Everything else" below.
2. **By Nov 26: hand your copywriter the words:** the homepage (your 11-21 draft [copy brief](planning/briefs/homepage-copy-brief-2026-11-21.md) and [intent brief](planning/briefs/homepage-intent-brief-2026-11-21.md)), the sample prompts, the "is my town open?" answers, the first vendor and patron email wave, and the waitlist storyboard. [Storyboard](planning/briefs/waitlist-join-journey-2026-11-12.md) Words back by Dec 11; you approve by Dec 15. Launch B assumes the homepage's first slice is rules only (A); [brief](planning/briefs/town-before-it-opens-2026-11-21.md).
3. **By Dec 4: walk the waitlist on your phone:** [socialus.org/join/waitlist](https://socialus.org/join/waitlist), signed in as operator, and say what felt wrong. Then apply the one migration that keeps name, number, zip and plans with each entry: `gh workflow run apply.yml -R donlafranchi/socialus-web --ref 1299-waitlist-answers -f confirm=apply` (phone: Actions → Apply migrations → Run workflow → branch `1299-waitlist-answers` → type `apply`).
4. **By Dec 4: pick where the Sacramento market ends** (E recommended: the hour you ruled 10-27, not built yet). [Brief](planning/briefs/sacramento-market-edges-2026-11-23.md) Same day: **ask counsel whether the beta Terms and Privacy hold for real sign-ups** before the company exists. The question is written up in your legal repo.
5. **By Dec 15: the Mapbox production key,** locked to socialus.org. [Steps](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#4-maps-and-geocoding) Same day: **say where the three landing pictures came from** (town square, main street, park, from your 2026-10-31 concept): no source or licence is recorded, so commercial-use rights are unverified; and **write the positive posting reminder,** one line that encourages good, decent posts (a marked placeholder holds its place).
6. **By Dec 18: say who watches the report queue in opening week,** and how fast.
7. **Week of Dec 28: the private dry run** with a few invited testers, not the waitlist.
8. **Wednesday Jan 6: Sacramento opens** as a beta.

In January, after opening: approve and order the stickers (new spend); join the Apple Developer Program ($99 a year, your exception to "no new paid tool before go-live") and set up Google and Apple sign-in (a free Google Cloud client and Sign in with Apple; agents send the steps).

Later, not now: whether reported or repeat accounts are asked for a photo ID.

Agents' part, all milestoned for Jan 6: phone sign-up, new accounts start small, screening every post before it publishes (in shadow first), the safety package, the launch-blocking checks, the rules-only homepage with "is my town open?", sample prompts, the invite send and the first email wave.

## Everything else, in order

1. **Run the report test with three accounts.** Proves the AI first read on reports. [Steps](https://github.com/donlafranchi/socialus-web/issues/220)
2. **Decide the one-strike policy.** How we treat people trying to get over. [Options](planning/research/one-strike-2026-11-06.md)
3. **Finish monitoring (about 20 minutes, computer).** [Detail](https://github.com/donlafranchi/socialus-web/blob/main/INFRASTRUCTURE.md#11-error-tracking)
   - **Sentry, check what was sent unscrubbed (11-16 to 11-26):** for ten days error reports went out without the email, phone and search-term scrubbing (fixed now). In Sentry, Issues → socialus-web → last 14 days: open each issue first seen since 11-16; if its URL or message shows an email, phone number or someone's search words, tick it and Delete. Then Project Settings → Security & Privacy → turn on Data Scrubber and Use Default Scrubbers. Or sign in to Sentry in the app's browser pane and tell an agent to do the check.
   - **Vercel, spend alert:** vercel.com → team socialus → Settings → Billing → Spend Management → set **$60**, notifications on, leave "Pause production deployments" **off** → Save.
   - **UptimeRobot (free account):** two keyword monitors, every 5 minutes: `https://www.socialus.org/api/health/db` must contain `"ok":true`, and `https://www.socialus.org/auth/login` must contain `name="email"`. Alerts by email (the free plan). For your phone: in your mail app, mark UptimeRobot's sender as VIP so its emails notify you. Free to try: UptimeRobot's own phone app, which says it works on the free plan with push alerts. Then Status Pages → New → add both monitors → Save, and send the page's link to an agent so it goes in the app's help text.
   - **Previews, your call (Pro lifted the build cap):** A) keep them off (now); B) previews only for PRs marked for your look, each pointed at a test database, about 3 cents a build (recommended: you see UI before it is live, members' data stays out of it); C) previews for every PR, the same, more builds.
4. **Open the remaining accounts:** a free HUD account (web #849) and Cloudflare image safety (child-safety scanning no longer needs an NCMEC account, so it can go on now). Also file the private Supabase support ticket.
5. **Talk with 5 people who have tried SocialUs,** after the landing page and sign-up are live (the PM, 2026-11-12). Real evidence for the next calls. [Plan](planning/research/founding-circle-2026-10-21.md)
6. **Read the wording waiting for you:** decency lines, Remind me, search card. [Wording](planning/research/rules-review-2026-10-25.md)
7. **After the waitlist: pick the reward for bringing people in, how new kinds of business are welcomed and the map pins.** [Brief](planning/briefs/unmet-search-and-welcome-2026-11-12.md)
8. **React to ideas:** scouts, artists, outer counties, outreach. [Ideas](planning/research/local-creators-2026-10-21.md)
9. **After the waitlist and the chat-first first slice: shop by your values and the blue dot, pick the first slice.** [Brief](planning/briefs/shop-by-your-values-2026-11-21.md)

Low priority: in Cloudflare, delete the leftover Worker named socialus-plan-dashboard.

## Before launch (production, April to May 2027)

| When | What | Why |
|---|---|---|
| January 1, 2027 | **Form the company (LLC).** Specifics live in socialus-legal. | Commercial hosting terms, child-safety registration and card payments all need it |
| After the company, by 2027-04-01 | **Register with the NCMEC CyberTipline** and switch off the manual form. [Runbook](https://github.com/donlafranchi/socialus-ops/blob/main/operations/staff-safety.md) | Required reporting; the beta uses the public form, which can't take images |
| From 2027-03-01 | **Re-review paid tools now that budget opens:** feature flags, GitHub and Vercel plans. [Runbook](https://github.com/donlafranchi/socialus-ops/blob/main/operations/go-live-paid-tools.md) | We built our own until there was money |

Vercel Pro is on since 2026-11-16 ($20 a month). About $48 a month in all at launch, before usage.
