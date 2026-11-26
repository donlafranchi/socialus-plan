---
id: F030
title: A newcomer signs up, finishes onboarding and lands in the app
status: approved
horizon: now
rank: 105
date: 2026-11-26
approved: 2026-11-26, restated to match what is built; the removals it records are the PM's (2026-11-12, web #1301) and the dead-feed cleanup (web #1363)
depends: [F077, F081, F133, F134]
concept: CO-0041
---
## Story

A new resident of Oak Park opens SocialUs signed out and reads what any member with no relation to a Page reads (F134). They tap a heart; before anything saves, sign-in asks for their email. They are new, so they set a password, then fill one screen (legal name, display name, zip, an 18+ box), see their market, skip or pick a few interests, read the welcome once, and land in the app.

## Acceptance

1. **Signed out, no sign-up banner.** A visitor reads what a signed-in stranger reads (F134 criterion 1), and every write asks for sign-in first (F134 criterion 4). No "Make this yours" banner, no locality feed and no scope picker appear anywhere. *(Amended 2026-11-26: was "an anonymous visitor sees a locality feed with a 'Make this yours' CTA and a scope picker"; removed by the PM 2026-11-12, web #1301.)*
2. **Email first.** On sign-in, an email the app does not know goes to sign-up; one it knows asks for the password and signs the member in.
3. **Onboarding is one screen, then the market, then interests.** After sign-up the member sees one screen asking legal name, display name, zip and the 18+ box; then their market (or the waiting screen for a zip outside an open market); then an optional interests step. Each step saves when submitted, so backing out leaves what was given. *(Amended 2026-11-26: was three steps, profile · locality · interest tags.)*
4. **Lands in chat after the welcome.** At the end of onboarding the member sees the welcome screen once, then lands in the chat front door (2026-11-26). A member who came by a shared link lands where the link pointed instead. *(Amended 2026-11-26: was "lands on `/` with a populated locality feed"; the feed was removed, web #1301 and #1363. Today's build lands on Explore until the chat front door exists.)*
5. **One browser test walks it end to end:** sign-up with email and password, the onboarding screen, the market, skipping interests, the welcome, and the landing in 4. It is seen failing first against a build that lands anywhere else ([guard-proves-itself]).

*Retired 2026-11-26:* "an empty locality offers a one-tap widen". The empty feed and its widen control no longer exist (web #1363).

## Not this

Phone sign-up with a texted code (F081; it will change step 2's sign-up when it lands). Google or Apple sign-in (January, after the opening). The signed-out homepage's "is my town open?" box (the launch campaign). What the chat front door shows and how it is built (F119, F120, F136).

## Why

Rationale: the shipped F030 described a home feed and banner the PM removed on 2026-11-12, and three of its browser tests were retired with it (web #1363). Only unit tests now cover sign-up through onboarding, and sign-up is on the January 6 path, so the scenario is restated to what runs today and asks for one browser test of it. Precedents for landing a new member on the main browse surface after a one-time welcome: [Nextdoor](https://blog.nextdoor.com/meet-the-new-nextdoor), Airbnb (Explore after sign-up), Pinterest (home after picking topics, [help](https://help.pinterest.com/en/article/edit-your-home-feed)). [platform none]

*Answered 2026-11-26:* a new member lands in chat (`product/foundation/what-this-is.md` § Rulings, 2026-11-26).

## Rulings

- **2026-11-12 — The "Make this yours" banner and its sign-in button go away.** The PM, verbatim, after looking at F134 live: *"there's a sliver of html that says make this yours and a sign in button that needs to go away."* Built as web #1301; the dead feed it sat in was removed by web #1363. [for now] [replaces none] [binds tiers=planning,code surfaces=signed-out,signup build=none]
