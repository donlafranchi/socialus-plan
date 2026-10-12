---
id: F081
title: Everyone signs up the same way, and the zip sets the market
status: approved
horizon: now
rank: 100
gates: launch
date: 2026-09-14
depends: [F076, F077]
approved: 2026-09-14 — the PM's ruling; legal name, email, zip, display name, zip suggests the metro
amended: 2026-10-11 — the PM (F103): the market replaces the metro and the MSA; criteria 3, 4, 7 and 8 restated; the zip still decides, nobody picks.
amended: 2026-09-30 — the PM: every US zip known before launch, an unknown one refused; the metro is the MSA; the zip is kept and changed on /you; every member is verified as a person, method open; no "we never sell" line, a placeholder about what the app is for instead. Story and criteria 1, 4 and 5 restated, 8 added. 2026-10-05 — the PM: an 18+ checkbox with a Terms link beside it joins signup; the legal name is seen only by operators. Criterion 1 restated.
---
## Story

Maya follows a neighbour's link and signs up. One screen: her legal name, her email, her zip, and the display name everyone else will see. The screen tells her what the app is for: good and decent people finding, connecting with and supporting each other. Her zip decides her metro, and the screen says which one — Sacramento — so she can see it rather than have it happen to her. Nothing is placed for her that she did not give. Nobody asks whether she is here to make things or find them — she is a member, and that is the whole question.

## Acceptance

1. **Signup collects legal name, email, zip and display name, plus a checkbox reading "I'm 18 or older and agree to the Terms" with the Terms link beside it, and verifies the email.** Every member is verified as a person; how is open (Why). No other field exists in the flow. The legal name, email and phone are seen only by operators (2026-10-05).
2. The zip is stored, and never rendered on any surface another member or visitor can reach — profile, listing, search, map.
3. **The zip determines the market** (F103 criterion 2), and the screen shows the person which market that is, by name. **Nothing else determines it** — not IP, not a pre-filled default, not a nearest match. *(Amended 2026-09-27: this read "the zip produces a shortlist… the person selects one"; the PM ruled the zip decides.)*
4. **Nobody picks a market at signup.** A member who moves changes their zip on `/you`, and their market and home town follow from it. It is not one-and-done.
5. The screen carries a line saying what the app is for, **and no line about not selling member information.** Placeholder, the PM's words ([public-is-draft]): *"This is a community building app. It was made for good and decent people to find, connect with and support other good and decent people. We are here to build a better future together."* It states no date, feature, or promise about the future.
6. No field, control, or string in signup asks or records whether the person makes things or finds them.
7. **Onboarding assigns no place the person did not give.** A member's home is the market and the town their zip determined (F103 criterion 5); no default place is written on their behalf, seen or unseen. *(Added 2026-09-27. Today `DEFAULT_HOME_PLACE_ID` sets every new member's home to a fictional city whose box sits inside Sacramento, which is why every member resolves to Sacramento.)*
8. **Every US zip resolves, before launch, through the national HUD-USPS crosswalk, to its county and so to its market** (F103 criterion 2). A zip the crosswalk does not know is refused with *"We don't recognize that zip, try again."* A person whose zip is in a waiting market joins its waitlist (F076); their zip is kept, to tell them when their market opens. *(Restated 2026-10-11; this read "to the MSA that contains it".)*
9. **Phone verification refuses a non-fixed VoIP number** (Google Voice and the like), checked with Twilio Lookup's Line Type Intelligence before the code is sent, with a plain message asking for a mobile number ([public-is-draft]). *(the PM, 2026-10-05; Path: well-worn, Twilio's own guidance on blocking VoIP at verification.)*

## Not this

Choosing the person-verification method, which is open. The waitlist popup and metro counts (F076). Storing anything derived from the zip beyond the metro it determined. A home place finer than the metro — local means the whole metro (F094). A street address — `product/systems/member.md` refuses one by default. Any line about not selling member information (2026-09-30). Covering zips outside every MSA, Yuba and Sutter among them: growing MSA boundaries is parked for a later scenario.

## Why

### The zip decides (2026-09-27)

**The PM reversed the 2026-09-14 shortlist-and-pick.** A zip is something the person told us, so a metro derived from it is not the platform choosing for them; what F076 criterion 2 forbids is choosing from something they did not give — IP, a default, a nearest match. **The unseen default place was the real violation**, and criterion 7 removes it.

**The metro is the MSA** (the PM, 2026-09-30): Sacramento is MSA 40900, not CSA 472. Yuba and Sutter are not their own MSA and are not covered at launch. A member whose zip is in no MSA can choose a metro to view; the value is kept for records and to tell them when their own MSA opens.

**The zip is kept** (the PM, 2026-09-30): *"How will we know what's going on in their area without it."* So criterion 2 stands, and changing the zip is how a member changes metro.

**Criterion 5's line ships as the placeholder, the PM's words** (2026-10-01). It may change any time after launch.

### Who sees a real name

**Out of scope 2026-09-30; revisit with legal counsel** (F077). Signup says nothing about showing legal names to anyone.

**A person is verified by a text-message code to their phone, at signup** (the PM, 2026-10-01). At signup because every member is verified (2026-09-30). Today the code has no phone field, email-only sign-in, and Supabase SMS switched off — that is the build.

**Legal facts live in a private repo.**

### Settled against F076

**F076 criterion 3 was amended 2026-09-14** so the make-or-find answer is a property of the waitlist entry, discarded when the metro opens — not an account field. Criterion 6 here and F076 criterion 3 now hold together.

## Rulings
- **2026-10-11 — Phone verification's VoIP check is built now against a mocked Twilio Lookup and kept behind `PHONE_VERIFICATION_REQUIRED` until Don enables Lookup (Line Type Intelligence) at a computer; about $0.008 per lookup is acceptable.** The PM, 2026-10-11, option A on `socialus-web` #570 (F081 criterion 9). The refusal itself is the 2026-10-05 ruling. [replaces none] [binds tiers=planning,code surfaces=signup,verification] Issue: #570.
- **2026-10-11 — A new visitor's area is guessed from their IP and confirmed with "Is this your area?"; on no, or no guess, we ask for the zip ("Your zip helps us find your area."). The confirmed area or the zip decides the path: an open market goes straight in with a "Change area" link, and any other area gets the "SocialUs isn't in your area yet" screen with the waitlist (F076). No market is picked silently. We store the zip for the member's benefit, with an easy opt-out.** The PM, 2026-10-11, on `socialus-web` #588, replacing his earlier zip-first call that day. Because a guess the person confirms is theirs, not ours. "Open market" means zip → county → market (F103). [replaces none] [binds tiers=planning,code surfaces=signup,onboarding,waitlist] Issue: #588.
- **2026-10-05 — Phone verification refuses non-fixed VoIP numbers (Google Voice and the like), checked with Twilio Lookup Line Type Intelligence, with a plain message asking for a mobile number.** Path: well-worn, Twilio's own guidance. Scenario: F081. [binds tiers=planning,code surfaces=signup,verification]
- **2026-10-01 — The footer links to About, Terms and Privacy pages, all in launch scope.** Don's design decision 8. None of the three exists in the app today, so all three are **new launch scope**. Privacy must disclose collecting legal names, verified phones and verified emails; Terms and Privacy ship as plain-language drafts; F081 carries the detail. [replaces F081: What must it say, and must it be live before the first signup?] [binds tiers=planning surfaces=footer,legal,copy]
- **2026-10-01 — We disclose member data only in response to valid legal process: court orders, subpoenas and legal emergencies. Counsel finalises the wording.** Don said yes to the recommendation. The law reaches further than a court order, and a promise to refuse a valid subpoena may not be one we can keep. F081 criterion 1 restated. [replaces 2026-09-30: and is currently handed over only under a court order] [replaces F081: are currently handed over only under a court order] [binds tiers=planning,code surfaces=privacy,legal,copy build=none]
- **2026-10-01 — Terms and Privacy ship as plain-language drafts, marked as drafts, before counsel reviews them; counsel reviews after launch.** Don said yes to the recommendation. There is no counsel today, and an honest plain draft is better than no page. Answers F081's counsel question. [binds tiers=planning surfaces=legal,copy,footer]
- **2026-10-01 — The signup line ships as written: "This is a community building app. It was made for good and decent people to find, connect with and support other good and decent people. We are here to build a better future together."** Don: *"A."* No longer placeholder; he may change it after launch. Answers F081's question. [replaces none] [binds tiers=planning,code surfaces=signup,copy]
- **2026-10-01 — A member is verified as a person by a text-message code to their phone, at signup.** Don: *"Text message code."* At signup because every member is verified as a person (2026-09-30). Answers F081's question; `socialus-web` #222. [replaces none] [binds tiers=planning,code surfaces=signup,identity]
- **2026-09-30 — Every member is verified as a person, to discourage anonymous behaviour. The method is open.** Don. Phone is one candidate; the options and their timing are in F081. [binds tiers=planning,code surfaces=signup,identity]
- **2026-09-30 — The zip is kept. Nobody picks a metro: the zip decides it at signup, and a member who moves changes their zip on `/you` and the metro follows.** Don: *"How will we know what's going on in their area without it."* **Reverses his same-day answer that the zip is discarded**, which was not recorded; the 2026-09-14 "the zip is stored and is never peer-visible" stands. We currently show it to nobody and scope nothing member-facing by it: surfaces scope to the metro. Answers F081's override question and F094's zip question. F081 criterion 4 and F094 criterion 5 restated. [replaces 2026-09-29: the zip is used once, not retained as a locality attribute] [replaces 2026-09-27: zips the crosswalk lacks (it holds Sacramento only)] [binds tiers=planning,code surfaces=signup,onboarding,you,locality]
- **2026-09-30 — Every US zip is known before launch, and an unrecognised zip gets "We don't recognize that zip, try again."** Don, on #222. The national HUD-USPS zip crosswalk is launch scope (flagged, not cut), which closes Cowork's question on #222. F081 criterion 8 added. [binds tiers=planning,code surfaces=signup,onboarding]
- **2026-09-30 — Signup does not say "we never sell". It says what the app is for.** Don: don't bring it up; say what we do. Everything in the app is for the benefit of its members. **Placeholder copy, Don's words** ([public-is-draft]): *"This is a community building app. It was made for good and decent people to find, connect with and support other good and decent people. We are here to build a better future together."* Don rejected the draft real-names line; where that disclosure lives now is open in F081. This rules on copy only: `goals.md` promise 3 and `monetization.md` are untouched. `voice.md`'s no-sale sample is removed. F081 story and criterion 5 restated. [replaces 2026-09-14: "We don't sell your information" becomes published signup copy.] [binds tiers=planning,code surfaces=signup,copy]
- **2026-09-27 — Onboarding stops silently assigning a place.** Don's ruling on `socialus-web` #222. No shortlist, no pick. A metro derived from the person's own zip is not the platform choosing for them; **what stays forbidden is choosing from something they did not give** — a pre-filled default, a nearest match, an IP guess the person has not confirmed — and F076 criterion 2 is annotated to say so. **The real violation was `DEFAULT_HOME_PLACE_ID`**: every new member's home was set, unseen, to a fictional city whose box sits inside Sacramento, which is why every member resolves there. F081 criterion 3 restated and 7 added: **a member's home is a metro, and nothing finer is written for them.** [binds tiers=planning,code surfaces=signup,onboarding] [replaces 2026-09-14: A zip suggests a shortlist of metros; the person still picks]
- **2026-09-14 — Everyone signs up the same way, as a member; "patron" is not an account type and is never stored.** Becoming a creator is a separate, later step, and creator status derives from having completed it plus what the member has authored. Preserves `DECISIONS.md` "one word for a person," `role-language.md` rule 3, and `nouns.md`'s "no type, tier, or stored role" rather than reversing any of them. See F081, F082.
- **2026-09-14 — Signup collects legal name, email and zip, and nothing more without a stated reason.** The zip is stored and is never peer-visible. Extends F077's legal-name-and-email floor; the stated reason for the zip is metro suggestion. See F081.
- **2026-09-14 — Patron signup and the become-a-creator step ship at launch.** Don's direction; nothing was removed to make room, and neither scenario is approved yet.
