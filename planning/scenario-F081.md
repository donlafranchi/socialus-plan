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
amended: 2026-11-12 — the PM: sign up by mobile number and the anti-bot layers (1, 9, 11–16); the line and look (#1271; 5, 6, 10); the safety line (17); make-or-support moves to the waitlist (6).
---
## Story

Maya follows a neighbour's link, signs up with Google, adds her mobile and its code, her first name and zip, and sees the zip put her in Sacramento.

## Acceptance

1. **Signup starts with Google or Apple (how is open, Why), collects a US mobile number, verified by a texted code (Twilio Verify), then a name (never a legal name), zip, what they plan to do and an "I'm 18 or older and agree to the Terms" checkbox, Terms linked.** No other field exists. Phone and email are seen only by operators.
2. The zip is stored and never shown to another member or visitor.
3. **The zip determines the market** (F103), named on the screen. **Nothing else does:** no IP, default or nearest match.
4. **Nobody picks a market at signup.** A member who moves changes their zip on `/you`, and their market follows.
5. The screen carries the line *"Locals, finding and supporting locals."* to say what the app is for, and no line about not selling member information; no date, feature or promise.
10. **Sign-up looks like the front page:** the same terracotta colour and the Aime font.
6. What they plan to do is asked once, on the waitlist (F076); an invited person never answers it twice.
7. **Onboarding assigns no place the person did not give.** Home is the zip's market and town (F103).
8. **Every US zip resolves, before launch, through the national HUD-USPS crosswalk, to its county and so to its market** (F103). An unknown zip is asked again; a waiting market's zip joins its waitlist (F076).
9. **Only a real mobile number signs up.** Before any code, Twilio Lookup must return `mobile`; any other type gets a plain line asking for a mobile, and nothing is sent. A Lookup outage lets it through.
11. **One account per number:** a number on an account signs in to it, never makes a second; a banned number (F102) makes none.
12. **Cloudflare Turnstile guards the number screen,** checked on the server before anything is sent.
13. **Rate limits before any text:** per number, IP and number range, configurable without a deploy; over a limit, a plain wait line and nothing sent.
14. **Codes go only to US numbers** (Verify Geo Permissions), with Fraud Guard on.
15. **A member stays signed in for months on a device** (`member.md`).
16. **SocialUs says "Every member is a real person with a real phone."** and never claims no bots.
17. **The number screen carries the soft line and, behind its ⓘ only, the police line** (ruling 2026-11-12); the Terms say the same.

## Not this

The waitlist (F076). Anything from the zip beyond its metro. A home finer than the metro (F094). A street address (`member.md`).

## Why

**Sign up with a mobile number (2026-11-12).** The PM: *"The point is to have something on people that helps us know who they are so we don't have to police as much if a person can't post anonymously."* A real mobile costs a bot farm money. Evidence: `planning/research/phone-sign-up-2026-11-12.md`.

[open-question owner=don raised=2026-11-12] How do Google and Apple sign-in fit with the required mobile number and email? A/B/C in `planning/briefs/waitlist-join-journey-2026-11-12.md`.

## Rulings
- **2026-11-12 — Google and Apple sign-in are the primary way in; a real mobile number is still required at sign-up, and email is for signing in again.** The PM: *"add Google Auth and Apple Auth for this as well as that should be primary. … We are using mobile numbers instead of email for sign up and then email can be used for repeated sign in."* How the three fit is open (Why). Path: new territory. [for now] [replaces none] [binds tiers=planning,code surfaces=signup,sign-in,identity] Issue: #1280.
- **2026-11-12 — Two layers at sign-up: a soft line, "SocialUs is a place where we look out for one another.", with an ⓘ; behind the ⓘ only, "Your number is tied to everything you post. Illegal content is reported to police." The Terms say the same.** The PM: *"I want to assume good behavior and not plant the idea in peoples minds … this is a place where we look out or one another period."* Path: new territory. [always] [replaces none] [binds tiers=planning,code surfaces=signup,copy,terms] Issue: #1280.
- **2026-11-12 — Sign up with a US mobile number and a texted code, not an email; email is optional, added later on You. Sign-up collects a mobile number, a name (a first or display name, never a legal name), a zip and what the person plans to do, and nothing more without a stated reason.** The PM: *"instead of asking people to sign up with email we ask them to sign up with their mobile number"*, then *"The goal is to get a phone number and a name (don't ask for a legal name), a zip code and then what they plan on doing in the app."* A name people go by is enough: the verified number is what ties a person to what they post. Path: well-worn. [for now] [replaces 2026-11-12: Sign up with a US mobile number and a texted code, not an email; email is optional, added later on You. Signup collects mobile number, legal name, zip and display name] [replaces 2026-09-14: Signup collects legal name, email and zip] [replaces 2026-10-01: A member is verified as a person by a text-message code] [binds tiers=planning,code surfaces=signup,sign-in,identity,waitlist] Issue: #1280.
- **2026-11-12 — Only real mobile numbers sign up: Twilio Lookup must say `mobile`; one account per number.** The PM: *"isn't there a way to prevent e-phone numbers?"* Path: well-worn. [for now] [replaces 2026-10-05: Phone verification refuses non-fixed VoIP numbers] [replaces 2026-10-11: Phone verification's VoIP check is built now] [binds tiers=planning,code surfaces=signup,verification] Issue: #1280.
- **2026-11-12 — Codes go through Twilio Verify on Twilio's own senders: no number to buy, no 10DLC registration; our own number only if we send texts that are not codes or want branded sending.** The PM: *"does this mean I don't need to buy a twilio number?"* Path: well-worn. [for now] [replaces none] [binds tiers=planning,code surfaces=signup,verification,alerts] Issue: #707.
- **2026-11-12 — Sign-up guards: Verify Fraud Guard, US-only Geo Permissions, Turnstile, and rate limits per number, IP and number range.** The PM: "Yes to everything"; limits are agents' calls. Path: well-worn. [for now] [replaces none] [binds tiers=planning,code surfaces=signup,verification,abuse] Issue: #1280.
- **2026-11-12 — Positioning: "Every member is a real person with a real phone." We never claim zero bots.** The PM: *"we can position this as eliminating Bots"*, then *"I like this approach."* Path: new territory. [always] [replaces none] [binds tiers=planning,code surfaces=landing,signup,copy] Issue: #1280.
- **2026-11-12 — The sign-up line saying what the app is for is "Locals, finding and supporting locals."** The PM, "A"; the soul's words. Path: new territory. [for now] [replaces F081: The signup line ships as written] [binds tiers=planning,code surfaces=signup,copy] Issue: #1271.
- **2026-11-12 — Sign-up carries the front page's look: terracotta and the Aime font.** The PM, "A". Because sign-up looked like a different app from the front page (#1271). Path: new territory. [for now] [replaces none] [binds tiers=planning,code surfaces=signup,look] Issue: #1271.
- **2026-10-11 — A new visitor's area is guessed from their IP and confirmed with "Is this your area?"; on no, or no guess, we ask for the zip ("Your zip helps us find your area."). The confirmed area or the zip decides the path: an open market goes straight in with a "Change area" link, and any other area gets the "SocialUs isn't in your area yet" screen with the waitlist (F076). No market is picked silently. We store the zip for the member's benefit, with an easy opt-out.** The PM, 2026-10-11, on `socialus-web` #588, replacing his earlier zip-first call that day. Because a guess the person confirms is theirs, not ours. "Open market" means zip → county → market (F103). [replaces none] [binds tiers=planning,code surfaces=signup,onboarding,waitlist] Issue: #588.
- **2026-10-01 — The footer links to About, Terms and Privacy pages, all in launch scope.** Don's design decision 8. None of the three exists in the app today, so all three are **new launch scope**. Privacy must disclose collecting legal names, verified phones and verified emails; Terms and Privacy ship as plain-language drafts; F081 carries the detail. [replaces F081: What must it say, and must it be live before the first signup?] [binds tiers=planning surfaces=footer,legal,copy]
- **2026-10-01 — We disclose member data only in response to valid legal process: court orders, subpoenas and legal emergencies. Counsel finalises the wording.** Don said yes to the recommendation. The law reaches further than a court order, and a promise to refuse a valid subpoena may not be one we can keep. F081 criterion 1 restated. [replaces 2026-09-30: and is currently handed over only under a court order] [replaces F081: are currently handed over only under a court order] [binds tiers=planning,code surfaces=privacy,legal,copy build=none]
- **2026-10-01 — Terms and Privacy ship as plain-language drafts, marked as drafts, before counsel reviews them; counsel reviews after launch.** Don said yes to the recommendation. There is no counsel today, and an honest plain draft is better than no page. Answers F081's counsel question. [binds tiers=planning surfaces=legal,copy,footer]
- **2026-09-30 — The zip is kept. Nobody picks a metro: the zip decides it at signup, and a member who moves changes their zip on `/you` and the metro follows.** The PM: *"How will we know what's going on in their area without it."* Reverses his same-day answer that the zip is discarded. Surfaces scope to the metro; the zip is shown to nobody (F094). [for now] [replaces 2026-09-29: the zip is used once, not retained as a locality attribute] [replaces 2026-09-27: zips the crosswalk lacks (it holds Sacramento only)] [binds tiers=planning,code surfaces=signup,onboarding,you,locality]
- **2026-09-30 — Every US zip is known before launch, and an unrecognised zip gets "We don't recognize that zip, try again."** Don, on #222. The national HUD-USPS zip crosswalk is launch scope (flagged, not cut), which closes Cowork's question on #222. F081 criterion 8 added. [binds tiers=planning,code surfaces=signup,onboarding]
- **2026-09-30 — Signup does not say "we never sell". It says what the app is for.** The PM: don't bring it up; say what we do. Its placeholder copy gave way to the 2026-11-12 line (F081 criterion 5). [for now] [replaces 2026-09-14: "We don't sell your information" becomes published signup copy.] [binds tiers=planning,code surfaces=signup,copy]
- **2026-09-27 — Onboarding stops silently assigning a place.** The PM's ruling on `socialus-web` #222. Forbidden is choosing from something the person did not give (a default, a nearest match, an unconfirmed IP guess); the real violation was `DEFAULT_HOME_PLACE_ID`. [binds tiers=planning,code surfaces=signup,onboarding] [replaces 2026-09-14: A zip suggests a shortlist of metros; the person still picks]
- **2026-09-14 — Everyone signs up the same way, as a member; "patron" is not an account type and is never stored.** Becoming a creator is a separate, later step, and creator status derives from having completed it plus what the member has authored. Preserves `DECISIONS.md` "one word for a person," `role-language.md` rule 3, and `nouns.md`'s "no type, tier, or stored role" rather than reversing any of them. See F081, F082. [always]
