---
id: brief-2026-11-12-waitlist-join-journey
status: awaiting-approval
size: M
path: new territory (the contact the waitlist collects); well-worn for the rest
criteria:
  - From socialus.org, a person joins the waitlist on a 390px phone in four screens (landing, role, zip and contact, done), all in terracotta and the Aime font.
  - The role screen offers two choices, neither pre-selected - runs a business, store, shop, market or group; or looking for those - and nothing else is asked about the person.
  - Every US zip lands in a waiting market while the PM keeps SocialUs closed; an unknown zip gets "We don't recognize that zip, try again."
  - The answers are staff-only, counted per market by role, never shown as names, never sold; the contact is used only to say the person's area opened, then deleted.
  - The response and the count shown are the same whether or not the person already joined (F076 criterion 14).
  - When a market opens, each person on its list gets one invite whose link opens phone sign-up (F081) with zip and role carried in the link, so they never retype them, and lands each role on its own first screen.
  - The PM can walk the whole journey on his phone at a live socialus.org link before anyone else sees it.
---

# The waitlist join journey

**As of 2026-11-12** · Replaces the sign-up journey brief of the same day (#330) · Source: the PM's refocus (2026-11-12), F076, F081, F118, F134, the privacy principle (#329), `planning/research/phone-sign-up-2026-11-12.md` · Maintained by: hand (brief; deleted at 30 days or once ruled and placed)

*The PM, 2026-11-12:* "I want to get the landing page out to people and the landing page will have a Join a Waitlist button and then the join should allow users a couple of options for signup as either someone who runs a business, store, shop, market or group etc and then for someone who is looking for those things and then also a zip code. … This may also help us decide where to launch so we can stay closed until I get everything set up."

**Bottom line: four screens (landing, role, zip and contact, done), then one invite when your area opens that drops you straight into phone sign-up. Your one call: what contact the waitlist takes. Recommended: an email, confirmed by one tap.**

## Your one call: what contact the waitlist collects

- **A. Email, confirmed by one tap (recommended).** Invites go by email (Resend). Works now; no company needed. Robinhood, Superhuman and Instacart's "tell me when you deliver to my zip" did this. Fake emails are cheap, so only confirmed ones count, behind Cloudflare Turnstile. Resend's free tier sends 100 a day, so invites to a big market go out over a few days, or $20 a month lifts it.
- **B. Mobile number, verified by a texted code at join.** Every count is a real person with a real phone, the strongest signal for where to launch, and the same number becomes the account later. Clubhouse did this. About 7 cents a join, more friction at the door, and we still can't text the invite (Verify sends codes only), so the person must come back on their own or also leave an email.
- **C. Mobile number, invited by text.** The warmest invite, but texts that aren't codes need our own registered number and written consent to market by text (47 CFR 64.1200). Correction: a sole-proprietor registration needs no company (1 number, 1,000 texts a day to T-Mobile), so this is possible before the LLC, just slower and more paperwork.

Why A: it ships with the landing page, costs nothing, and the phone check still happens at real sign-up, where it matters. B is the upgrade if the counts look gamed.

## The journey, screen by screen (390px)

**1. Landing.** The headline you're choosing, the line under it, one button: **Join the waitlist**. "Look around" stays (visitors can read everything, F134).

**2. Who are you here as?** Two big buttons, neither pre-selected:
- "I run a business, store, shop, market or group"
- "I'm looking for local businesses, makers and groups"

Wording is yours; these are drafts.

**3. Where, and how we reach you.** Zip (one field), then the contact from your call. Turnstile runs unseen. If you're a maker, one optional field: "Your business or group name". A one-line privacy note: "Only our team sees this. We'll use it once, to tell you we've opened near you."

**4. You're on the list.** "We're not open in {market} yet." Then the market's count, one combined number, cached, the same for everyone (F076). What's still needed, never a date. With A: "Tap the link we just emailed to confirm."

**When the area opens.** One invite: "SocialUs is open in {market}." The link opens phone sign-up (F081: number, code, name, display name), with zip and role already filled in. A maker lands on "Is your Page already here?" (claim or start). A supporter lands on "What are you into?", then Explore. The waitlist entry is then deleted; the role is never saved on the member.

## How it helps decide where to launch

- A staff-only table: per market, makers and supporters waiting (confirmed only), and which kinds of makers.
- It feeds your county pick and the open-your-town thresholds (F118: 100 makers, 1,000 supporters). It never opens a market on its own (F076).
- One person counts once (one contact, one zip). Changing the zip moves the count.

## How you'll see it

- Built behind a flag that's on only for builders and you (the flag system shipped with F128). The public keeps today's landing page.
- Each screen has its own address, so every PR gives you a live socialus.org link to that step. Signed in as operator on your phone, you walk the whole journey on the real site.
- When you approve the words and look, the flag goes on for everyone. No screenshots.

## What agents decided (well-worn)

- **Ask the role at the waitlist, not after sign-up.** Faire runs separate sign-up paths for retailers and brands ([retailers](https://www.faire.com/support/retailers), [brands](https://www.faire.com/support/brands)), and Bird takes requests city by city ([Bird](https://help.bird.co/hc/en-us/articles/360031021531-Bring-Bird-to-your-City-University)). Your direction overrides the earlier "ask nothing on the waiting screen" ruling (newer wins).
- **The role is an answer on the waitlist entry, never a type on the member.** This keeps the 2026-09-14 [always] rule. Etsy and Airbnb keep one account and treat selling as an action ([Etsy](https://help.etsy.com/hc/articles/115015672808)).
- **Zip, not address.** Nextdoor's address check is for verified neighbors; a waitlist needs only the market ([Nextdoor](https://about.nextdoor.com/press-releases/the-worlds-largest-private-network-for-neighbours-officially-launches-in-canada)).
- **No place in line, no referral race.** Robinhood's line-jumping ([case study](https://www.prefinery.com/blog/referral-programs/robinhood/)) conflicts with F076's "no leaderboard, no referral mechanic."
- **Closed means no sign-ups, not no reading.** While you keep SocialUs closed, every zip, Sacramento included, joins a waitlist. Reading stays open per F134.
- **Today's code already has** the waiting screen, the email list, the cached count and a role question (built for F118, behind a flag). The build reworks these; it doesn't start fresh.

## Rulings this holds

F076 (one count per person, the same answer either way, the contact used once, no date), F081 (phone sign-up and its guards, the safety line on the number screen), the privacy principle (supporters can't be tracked; staff-only answers), F134 (visitors read everything), "Every member is a real person with a real phone" (said at sign-up, not promised at the waitlist).

<details><summary>What changed from the earlier sign-up journey brief</summary>

- The "what brings you here?" fork moves from after sign-up to the waitlist.
- The journey starts closed: every market waits until you open it.
- The earlier A/B/C (ask after sign-up, on the form, or never) is superseded by your direction. Its maker and supporter first screens carry over, now opened by the invite link.

</details>
