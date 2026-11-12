---
id: F081
title: Everyone signs up the same way, and the zip sets the market
status: approved
horizon: now
rank: 100
gates: launch
date: 2026-09-14
depends: [F076, F077]
concept: new
approved: 2026-09-14 — the PM's ruling; legal name, email, zip, display name, zip suggests the metro
amended: 2026-11-12 — the PM: sign up by mobile number and the anti-bot layers (1, 9, 11–16); the line and look (#1271; 5, 6, 10).
---
## Story

Maya follows a neighbour's link and signs up. She types her mobile number and the texted code; no email, no password. Then one screen: her legal name, her zip, and the display name everyone else will see. The screen, in the front page's look, says what the app is for. Her zip decides her metro, and the screen says which one — Sacramento — Nobody asks whether she is here to make things or find them — she is a member, and that is the whole question.

## Acceptance

1. **Signup collects a US mobile number, verified by a texted code (Twilio Verify), then legal name, zip, display name and a checkbox reading "I'm 18 or older and agree to the Terms" with the Terms link beside it.** No email is asked; one may be added later on You, verified. No other field exists. Legal name, phone and email are seen only by operators (2026-10-05).
2. The zip is stored, and never rendered on any surface another member or visitor can reach — profile, listing, search, map.
3. **The zip determines the market** (F103 criterion 2), and the screen shows the person which market that is, by name. **Nothing else determines it** — not IP, not a pre-filled default, not a nearest match.
4. **Nobody picks a market at signup.** A member who moves changes their zip on `/you`, and their market and home town follow from it. It is not one-and-done.
5. The screen carries the line *"Locals, finding and supporting locals."* (the PM, 2026-11-12) to say what the app is for, **and no line about not selling member information.** It states no date, feature, or promise about the future.
10. **Sign-up looks like the front page:** the same terracotta colour and the Aime font (the PM, 2026-11-12).
6. [open-question owner=don raised=2026-11-12] How should sign-up ask whether someone is here to make or to support, end to end, and what does the market gate count?
7. **Onboarding assigns no place the person did not give.** A member's home is the market and the town their zip determined (F103 criterion 5); no default place is written on their behalf, seen or unseen.
8. **Every US zip resolves, before launch, through the national HUD-USPS crosswalk, to its county and so to its market** (F103 criterion 2). A zip the crosswalk does not know is refused with *"We don't recognize that zip, try again."* A person whose zip is in a waiting market joins its waitlist (F076); their zip is kept, to tell them when their market opens.
9. **Only a real mobile number signs up.** Before any code, Twilio Lookup must return `mobile`; any other type (Google Voice and TextNow are `nonFixedVoip`) gets a plain line asking for a mobile number ([public-is-draft]), and nothing is sent. A Lookup outage lets the number through.
11. **One account per number:** a number on an account signs in to it, never makes a second; a banned number (F102) makes none.
12. **Cloudflare Turnstile guards the number screen,** checked on the server before anything is sent.
13. **Rate limits before any text:** per number 1 a minute and 5 an hour, per IP 10 an hour, per first-six-digits range 20 an hour; configurable without a deploy. Over a limit: "Too many tries. Wait a few minutes and try again." ([public-is-draft]); nothing is sent.
14. **Codes go only to US numbers** (Verify Geo Permissions), with Fraud Guard on.
15. **A member stays signed in for months on a device,** texted again only on a new device or after signing out (`member.md`, 2026-11-12).
16. **Where SocialUs describes who is here, it says "Every member is a real person with a real phone."** It never claims there are no bots ([public-is-draft]).

## Not this

The waitlist popup and metro counts (F076). Storing anything derived from the zip beyond the metro it determined. A home place finer than the metro — local means the whole metro (F094). A street address — `product/systems/member.md` refuses one by default.

## Why

**Sign up with a mobile number (2026-11-12).** The PM: *"The point is to have something on people that helps us know who they are so we don't have to police as much if a person can't post anonymously."* A real mobile costs a bot farm money per account; an email costs nothing. Real SIMs can still be bought, so we never claim zero bots. Evidence: `planning/research/phone-sign-up-2026-11-12.md`.

Legal facts live in a private repo.

## Rulings
- **2026-11-12 — Sign up with a US mobile number and a texted code, not an email; email is optional, added later on You. Signup collects mobile number, legal name, zip and display name, and nothing more without a stated reason.** The PM: *"instead of asking people to sign up with email we ask them to sign up with their mobile number."* [always] [replaces 2026-09-14: Signup collects legal name, email and zip] [replaces 2026-10-01: A member is verified as a person by a text-message code] [binds tiers=planning,code surfaces=signup,sign-in,identity] Issue: #1280.
- **2026-11-12 — Only real mobile numbers sign up: Twilio Lookup must say `mobile`; one account per number.** The PM: *"isn't there a way to prevent e-phone numbers?"* [for now] [replaces 2026-10-05: Phone verification refuses non-fixed VoIP numbers] [replaces 2026-10-11: Phone verification's VoIP check is built now] [binds tiers=planning,code surfaces=signup,verification] Issue: #1280.
- **2026-11-12 — Codes go through Twilio Verify on Twilio's own senders: no number to buy, no 10DLC registration; our own number only if we send texts that are not codes or want branded sending.** The PM: *"does this mean I don't need to buy a twilio number?"* [for now] [replaces none] [binds tiers=planning,code surfaces=signup,verification,alerts] Issue: #707.
- **2026-11-12 — Sign-up guards: Verify Fraud Guard, US-only Geo Permissions, Turnstile, and rate limits per number, IP and number range.** The PM: "Yes to everything"; limits are agents' calls. [for now] [replaces none] [binds tiers=planning,code surfaces=signup,verification,abuse] Issue: #1280.
- **2026-11-12 — Positioning: "Every member is a real person with a real phone." We never claim zero bots.** The PM: *"we can position this as eliminating Bots"*, then *"I like this approach."* [always] [replaces none] [binds tiers=planning,code surfaces=landing,signup,copy] Issue: #1280.
- **2026-11-12 — The sign-up line saying what the app is for is "Locals, finding and supporting locals."** The PM, "A"; the soul's words. [replaces F081: The signup line ships as written] [binds tiers=planning,code surfaces=signup,copy] Issue: #1271.
- **2026-11-12 — Sign-up carries the front page's look: terracotta and the Aime font.** The PM, "A". [replaces none] [binds tiers=planning,code surfaces=signup,look] Issue: #1271.
- **2026-10-11 — A new visitor's area is guessed from their IP and confirmed with "Is this your area?"; on no, or no guess, we ask for the zip ("Your zip helps us find your area."). The confirmed area or the zip decides the path: an open market goes straight in with a "Change area" link, and any other area gets the "SocialUs isn't in your area yet" screen with the waitlist (F076). No market is picked silently. We store the zip for the member's benefit, with an easy opt-out.** The PM, 2026-10-11, on `socialus-web` #588, replacing his earlier zip-first call that day. Because a guess the person confirms is theirs, not ours. "Open market" means zip → county → market (F103). [replaces none] [binds tiers=planning,code surfaces=signup,onboarding,waitlist] Issue: #588.
- **2026-10-01 — The footer links to About, Terms and Privacy pages, all in launch scope.** Don's design decision 8. None of the three exists in the app today, so all three are **new launch scope**. Privacy must disclose collecting legal names, verified phones and verified emails; Terms and Privacy ship as plain-language drafts; F081 carries the detail. [replaces F081: What must it say, and must it be live before the first signup?] [binds tiers=planning surfaces=footer,legal,copy]
- **2026-10-01 — We disclose member data only in response to valid legal process: court orders, subpoenas and legal emergencies. Counsel finalises the wording.** Don said yes to the recommendation. The law reaches further than a court order, and a promise to refuse a valid subpoena may not be one we can keep. F081 criterion 1 restated. [replaces 2026-09-30: and is currently handed over only under a court order] [replaces F081: are currently handed over only under a court order] [binds tiers=planning,code surfaces=privacy,legal,copy build=none]
- **2026-10-01 — Terms and Privacy ship as plain-language drafts, marked as drafts, before counsel reviews them; counsel reviews after launch.** Don said yes to the recommendation. There is no counsel today, and an honest plain draft is better than no page. Answers F081's counsel question. [binds tiers=planning surfaces=legal,copy,footer]
- **2026-09-30 — The zip is kept. Nobody picks a metro: the zip decides it at signup, and a member who moves changes their zip on `/you` and the metro follows.** Don: *"How will we know what's going on in their area without it."* **Reverses his same-day answer that the zip is discarded**, which was not recorded; the 2026-09-14 "the zip is stored and is never peer-visible" stands. We currently show it to nobody and scope nothing member-facing by it: surfaces scope to the metro. Answers F081's override question and F094's zip question. F081 criterion 4 and F094 criterion 5 restated. [for now] [replaces 2026-09-29: the zip is used once, not retained as a locality attribute] [replaces 2026-09-27: zips the crosswalk lacks (it holds Sacramento only)] [binds tiers=planning,code surfaces=signup,onboarding,you,locality]
- **2026-09-30 — Every US zip is known before launch, and an unrecognised zip gets "We don't recognize that zip, try again."** Don, on #222. The national HUD-USPS zip crosswalk is launch scope (flagged, not cut), which closes Cowork's question on #222. F081 criterion 8 added. [binds tiers=planning,code surfaces=signup,onboarding]
- **2026-09-30 — Signup does not say "we never sell". It says what the app is for.** Don: don't bring it up; say what we do. Everything in the app is for the benefit of its members. **Placeholder copy, Don's words** ([public-is-draft]): *"This is a community building app. It was made for good and decent people to find, connect with and support other good and decent people. We are here to build a better future together."* Don rejected the draft real-names line; where that disclosure lives now is open in F081. This rules on copy only: `goals.md` promise 3 and `monetization.md` are untouched. `voice.md`'s no-sale sample is removed. F081 story and criterion 5 restated. [for now] [replaces 2026-09-14: "We don't sell your information" becomes published signup copy.] [binds tiers=planning,code surfaces=signup,copy]
- **2026-09-27 — Onboarding stops silently assigning a place.** Don's ruling on `socialus-web` #222. No shortlist, no pick. A metro derived from the person's own zip is not the platform choosing for them; **what stays forbidden is choosing from something they did not give** — a pre-filled default, a nearest match, an IP guess the person has not confirmed — and F076 criterion 2 is annotated to say so. **The real violation was `DEFAULT_HOME_PLACE_ID`**: every new member's home was set, unseen, to a fictional city whose box sits inside Sacramento, which is why every member resolves there. F081 criterion 3 restated and 7 added: **a member's home is a metro, and nothing finer is written for them.** [binds tiers=planning,code surfaces=signup,onboarding] [replaces 2026-09-14: A zip suggests a shortlist of metros; the person still picks]
- **2026-09-14 — Everyone signs up the same way, as a member; "patron" is not an account type and is never stored.** Becoming a creator is a separate, later step, and creator status derives from having completed it plus what the member has authored. Preserves `DECISIONS.md` "one word for a person," `role-language.md` rule 3, and `nouns.md`'s "no type, tier, or stored role" rather than reversing any of them. See F081, F082. [always]
