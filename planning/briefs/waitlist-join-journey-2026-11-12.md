---
id: brief-2026-11-12-waitlist-join-journey
status: awaiting-approval
size: M
path: well-worn for the journey; the Google and Apple call is the PM's
criteria:
  - From socialus.org, a person joins the waitlist on a 390px phone one question per screen, with short explainer screens between, in terracotta and the Aime font.
  - Nothing is checked by Twilio at join (no Lookup, no texted code, no cost per join); the invite goes by email; Lookup and the code come at sign-up.
  - The journey collects exactly a name (first or display, never legal), a zip, an email, a mobile number, and what they plan to do (multi-select, two sides); being-found answers add up to two detail screens, both skippable.
  - Every screen has Back; optional screens have Skip; a segmented progress bar fills faster at the start, with no step count.
  - The mobile number is asked last, says why we ask (bots and spam; real cell numbers only), and carries "SocialUs is a place where we look out for one another." with its ⓘ.
  - Answers are staff-only, counted per market by side, never shown as names, never stored as a type on a member; the contact is used once, to say the area opened.
  - The finish shows the market's one cached number, the same whether or not the person already joined (F076.14), and no date.
  - The PM walks the whole journey on his phone at a live socialus.org link (builders-only flag) before anyone else sees it.
---

# The waitlist join journey

**As of 2026-11-12** · Source: the PM's two waitlist directions (2026-11-12), F076, F081, F118, F134, the privacy principle (#329), `planning/research/phone-sign-up-2026-11-12.md` · Maintained by: hand (brief; deleted at 30 days or once ruled and placed)

*The PM, 2026-11-12:* "I need a nice simple way for people to say what they're interested in a format that allows them to answer one question at a time and walk though some screens. The goal is to get a phone number and a name (don't ask for a legal name), a zip code and then what they plan on doing in the app. since nobody knows what the app is for or has little idea we need to somewhat inform them along the way."

**Bottom line: what they want to do first, then name, zip and email, and the phone number last. Eight screens to discover, eleven to be found. Nothing is checked or charged at join; the invite goes by email and the number is checked at sign-up. Your one remaining call: how Google and Apple sign-in fit with the number (recommended: Google or Apple first, then the number).**

## Decided: email and phone, checked at sign-up (the PM, 2026-11-12)

*"I don't want to spend 7 cents until the person is ready to join. We can ask for email and phone and explain "why phone" as this is to prevent bots and spam etc. … I don't care about padded numbers yet."*

- The waitlist asks an email and a mobile number. No Twilio Lookup, no texted code: zero Twilio cost per join.
- The invite goes by email (Resend) when the area opens. Its link opens sign-up, where Lookup (real mobiles only) and the code run (F081).
- Fake entries can pad the counts; accepted for now.
- The text-me consent box is dropped. If invite texts return, they need our own registered number and an unticked box: "Text me once when SocialUs opens near me. Msg & data rates may apply. Reply STOP to opt out, HELP for help. Not required to join." (draft)

## Your call: Google and Apple with the mobile number

*The PM, 2026-11-12:* "add Google Auth and Apple Auth for this as well as that should be primary. I am launching the landing page which includes the 'sign-up' journey next before talking to anyone. We are using mobile numbers instead of email for sign up and then email can be used for repeated sign in."

| | A. Google or Apple first, then the number (recommended) | B. Number first, Google or Apple after | C. Google or Apple only, number later |
|---|---|---|---|
| Sign-up | Tap Google or Apple; then the mobile number and its code, on the same account | Mobile number and code, as ruled; then "Next time, sign in with Google or Apple" | Tap Google or Apple; the number is asked before the first post |
| Signing in again | Google or Apple; an emailed code if neither (the email they came with) | The same three, once linked | Google or Apple only |
| One person, one number | Holds: no account without a verified mobile | Holds | Breaks until they post; bots can browse and pad counts |
| Drop-off | Lowest friction at the first tap; the number is still a step | Highest: the number comes first | Lowest |

- **Why A:** it does what you asked (Google and Apple first) and keeps your anti-bot rule (a real mobile per person). Airbnb offers Google, Apple, phone or email at sign-up and asks a confirmed phone before booking ([Airbnb help](https://www.airbnb.com/help/article/221)); scooter apps on ATOM Mobility take Apple or Google, then still ask the phone at registration ([ATOM](https://support.atommobility.com/en/articles/10308367-how-to-enable-sign-in-with-apple-id-and-google-account)). Uber and Nextdoor are assumed similar, not checked.
- **What Google and Apple give us, and the privacy line:** we ask only for sign-in and an email, never contacts, photos or friends. Apple shares the name only on the first sign-in and may give a private relay email (Hide My Email) instead of the real one ([Apple](https://www.apple.com/au/legal/privacy/data/en/sign-in-with-apple/)); we accept either. A Google or Apple name only pre-fills "What should we call you?"; the person can change it. Which provider someone used is never shown to anyone. This keeps the 2026-11-12 principle that nobody can track the people who come to find and support.
- **How the three bind:** one account holds up to three ways in: Google, Apple, and the mobile number (Supabase identity linking, [docs](https://supabase.com/docs/guides/auth/auth-identity-linking)). The number is required and unique; Google and Apple attach to it. Linking a phone to a Google account is not a documented Supabase path yet, so the build note checks it first.
- **Apple costs $99 a year** (Apple Developer Program), a paid tool before go-live; the coordinating session is putting that exception to you separately. Once there is an iPhone app, Apple's rule 4.8 expects Sign in with Apple wherever Google sign-in is offered ([summary](https://vp0.com/blogs/apple-sign-in-required-rejection-fix-swiftui.md)).
- **Waitlist:** under A the join journey's last screens become "Continue with Google / Apple", then the number and its code (screens 9 and 10); the name screen (7) is pre-filled when Google or Apple gives a name.

## The order, and why

- **Intent first, email, then phone last.** Duolingo moved sign-up after the first lesson and gained about 20% daily users ([First Round](https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker)); Zuko ranks phone among the most-abandoned fields ([Zuko](https://www.zuko.io/blog/which-form-fields-cause-the-biggest-ux-problems)). Asked last, the number is a step toward something they've already chosen; email, a familiar field, goes just before it, so the invite contact is in hand even if someone stops at the phone.
- **Teach between questions, briefly.** Headspace asks why you came before anything else ([Appcues](https://goodux.appcues.com/blog/headspaces-mindful-onboarding-sequence)); Noom teaches throughout. No published proof that explainer screens lift completion, so each is one line and one picture, and the discover path gets only two.
- **Keep the questions few.** Typeform: past six questions, completion falls below half ([Typeform](https://www.typeform.com/blog/tips/survey-school-2-how-to-maximize-survey-response-rates)). Discover path: 5 answers. Be-found path: 2 more, both skippable.
- **Being found branches like Thumbtack's pro sign-up:** what you offer first, then the details ([Thumbtack pro center](https://pro-center.thumbtack.com/?p=21129)). Airbnb, Etsy and Nextdoor keep the provider side a later step on one account ([Airbnb](https://www.airbnb.com/host/homes), [Etsy](https://help.etsy.com/hc/articles/115015672808), [Nextdoor](https://business.nextdoor.com/en-us/blog/guide-to-claiming-your-nextdoor-business-page)); we ask it here only as interest, nothing is created.
- **Progress:** a segmented bar that fills faster early; a meta-analysis of 32 experiments found fast-then-slow bars cut drop-off and slow-then-fast raised it ([Villar et al.](https://research.google/pubs/where-am-i-a-meta-analysis-of-experiments-on-the-effects-of-progress-indicators-for-web-surveys/)). No "3 of 9": branching changes the count. Back on every screen, Skip only on optional ones ([NN/g wizards](https://www.nngroup.com/articles/wizards/)).
- **390px layout:** one question, a big answer area, the main button pinned at the bottom in thumb reach, 48px targets; `autocomplete="given-name"`, `inputmode="numeric" autocomplete="postal-code"`, `type="tel" autocomplete="tel"`, `autocomplete="one-time-code"`; any phone format accepted (Baymard: 89% type it differently from the form, [Baymard](https://baymard.com/blog/checkout-flow-average-form-fields)); the button rides above the keyboard ([Chrome](https://developer.chrome.com/blog/viewport-resize-behavior)).

## Storyboard (for the copywriter)

Copy is placeholder ([public-is-draft]); the imagery column is the copywriter's.

| # | Purpose | The one question, or what it teaches | Answer | Branch | Placeholder copy | Imagery | Image brief | Feeds |
|---|---|---|---|---|---|---|---|---|
| 1 | Arrive | What SocialUs is | Button | — | Headline (your pick) · "A place for locals to find and support locals, wherever you are, wherever you go." · **Join the waitlist** · Look around |  | Locals at a busy street market, warm, real faces | — |
| 2 | Teach | Everything local in one place | Next | — | "The bakery, the run club, Saturday's market, the pottery class. Find what's happening near you." |  | A phone-sized collage of local shops, a class, a meetup | — |
| 3 | Intent | What would you like to do here? | Multi-select chips, at least one | Any "be found" chip → 4; else → 7 | Discover: "Find local businesses and makers" · "Find groups and meetups" · "Find events and classes". Be found: "I have a business, shop or stall" · "I make or sell things" · "I teach a class" · "I organize a group or meetup" |  | Two hands meeting across a market table | Counts by side per market; later, the first screen after sign-up |
| 4 | Teach (be found) | Locals can find you | Next | — | "People nearby can find what you make, teach or organize." |  | A maker at work, seen from a customer's side | — |
| 5 | Detail (be found) | What kind of thing do you do? | Chips, multi | — | "Food and drink" · "Shop or market stall" · "Maker or artist" · "Classes and lessons" · "Services" · "Groups and meetups" · "Events" · Skip |  | Small icons per kind, hand-drawn | Variety per market (F118.9) |
| 6 | Detail (be found) | What's it called, and where can we see it? | Name (text) + one link, both optional | — | "Business or group name" · "Website or social link" · Skip |  | A shopfront sign being hung | Later: matched to an unclaimed Page at invite |
| 7 | Name | What should we call you? | Text, one field | — | "Your first name, or the name people know you by." |  | A name tag at a neighbourhood table | Invite greeting |
| 8 | Zip | Where are you? | 5 digits | Unknown zip → "We don't recognize that zip, try again." | "We open town by town. Your zip counts toward yours." |  | A simple map with one town lit | Where-to-launch counts (F076, F118) |
| 9 | Email | Where should we send your invite? | Email (`type="email" autocomplete="email"`) | Not an email → "That doesn't look like an email." | "We'll email you once, when SocialUs opens near you. Nothing else." |  | An envelope tucked under a café door | The invite (F076.15) |
| 10 | Phone | Your mobile number, and why we ask | Phone, any format | Nothing checked here | "Your mobile number keeps out bots and spam. Only real cell numbers work, not internet numbers." · "SocialUs is a place where we look out for one another. ⓘ" (ⓘ: "Your number is tied to everything you post. Illegal content is reported to police.") |  | A phone in a hand, outdoors | Checked at sign-up (F081); one account per number then |
| 11 | Done | You're on the list | — | — | "You're on the list for {market}." · "{N} locals are waiting there. When enough makers and neighbours join, we can open." |  | The same market, a little fuller | — |

**When the area opens:** one invite, by email. Its link opens sign-up (F081) with name, zip, number and plans carried in, so nothing is typed twice; there Lookup refuses non-mobiles and the code is texted. Someone who wants to be found lands on "Is your Page already here?" (claim or start); someone discovering lands on Explore, led by what they picked. The waitlist entry is then deleted; nothing becomes a type on the member.

## How you'll see it

Behind a flag on only for builders and you (F128's flags). Each screen has its own address, so every PR posts a live socialus.org link; signed in as operator on your phone you walk it on the real site. When you approve the words and look, it goes on for everyone. Build waits for your yes on this brief.

## What agents decided (well-worn)

- Name, not legal name: the verified number is what ties a person to their posts; a legal name adds friction and holds nothing the number doesn't (supersedes the legal name in F081 and the 2026-10-05 legal note).
- Zip, not address (Nextdoor's address check is for verified neighbours; a waitlist needs only the market).
- No place in line, no referral race (F076: no leaderboard, no referral mechanic).
- Closed means no sign-ups, not no reading: every zip waits, Sacramento included; reading stays open (F134).
- Today's code already has a waiting screen, a list and a cached count (F118, behind a flag); the build reworks them.

<details><summary>What changed today</summary>

- Morning: the make-or-support fork moved from after sign-up to the waitlist.
- Afternoon: the waitlist became one question per screen, multi-select plans on two sides, a name instead of a legal name, and the phone number instead of an email.

</details>
