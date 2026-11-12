---
id: brief-2026-11-12-waitlist-join-journey
status: awaiting-approval
size: M
path: new territory (how the waitlist's number is checked); well-worn for the rest
criteria:
  - From socialus.org, a person joins the waitlist on a 390px phone one question per screen, with short explainer screens between, in terracotta and the Aime font.
  - The journey collects exactly a mobile number, a name (first or display, never legal), a zip, and what they plan to do (multi-select, two sides); being-found answers add up to two detail screens, both skippable.
  - Every screen has Back; optional screens have Skip; a segmented progress bar fills faster at the start, with no step count.
  - The mobile number is asked last, just before the finish, with "SocialUs is a place where we look out for one another." and its ⓘ beside it.
  - Answers are staff-only, counted per market by side, never shown as names, never stored as a type on a member; the contact is used once, to say the area opened.
  - The finish shows the market's one cached number, the same whether or not the person already joined (F076.14), and no date.
  - The PM walks the whole journey on his phone at a live socialus.org link (builders-only flag) before anyone else sees it.
---

# The waitlist join journey

**As of 2026-11-12** · Source: the PM's two waitlist directions (2026-11-12), F076, F081, F118, F134, the privacy principle (#329), `planning/research/phone-sign-up-2026-11-12.md` · Maintained by: hand (brief; deleted at 30 days or once ruled and placed)

*The PM, 2026-11-12:* "I need a nice simple way for people to say what they're interested in a format that allows them to answer one question at a time and walk though some screens. The goal is to get a phone number and a name (don't ask for a legal name), a zip code and then what they plan on doing in the app. since nobody knows what the app is for or has little idea we need to somewhat inform them along the way."

**Bottom line: what they want to do first, then name and zip, and the phone number last. Eight screens if they're here to discover, eleven if they want to be found. Your one call: whether we check the number with a texted code when they join. Recommended: yes (A), about 7 cents a person.**

## Your one call: the mobile number at join

| | A. Verify at join (recommended) | B. Collect now, verify at invite | C. Collect now, invite by email |
|---|---|---|---|
| What happens | Lookup (mobile only) and a texted code before "You're on the list" | Lookup only; the code comes when they accept the invite | Lookup only; one more screen asks an email for the invite |
| Cost per join | about $0.066 (Lookup $0.008 + Verify $0.058) | $0.008 | $0.008; Resend free to 100 emails a day |
| Counts for where to launch | real people, one per number | fake numbers can pad them | fake numbers can pad them |
| Drop-off | highest: a code to wait for | lower | an extra field |
| The "we're open" invite | a text, once we have our own registered number | same | an email, works now |

- **Texts that aren't codes need our own registered number** (Twilio: every A2P text from a 10-digit number must be registered; a toll-free number needs verification). Sole-owner registration works before the company exists: 1 number, 1,000 texts a day to T-Mobile.
- **They need written consent first,** so A and B carry one unticked box: "Text me once when SocialUs opens near me. Msg & data rates may apply. Reply STOP to opt out, HELP for help. Not required to join." (draft; [public-is-draft])
- **Why A:** you're staying closed until set up, so nobody is invited before the number exists, and verified counts are the ones worth deciding a launch on. Clubhouse verified phones at waitlist time; Hinge asks the number first because it is the login.

## The order, and why

- **Intent first, phone last.** Duolingo moved sign-up after the first lesson and gained about 20% daily users ([First Round](https://review.firstround.com/the-tenets-of-a-b-testing-from-duolingos-master-growth-hacker)); Zuko ranks phone among the most-abandoned fields ([Zuko](https://www.zuko.io/blog/which-form-fields-cause-the-biggest-ux-problems)). Asked last, the number is a step toward something they've already chosen.
- **Teach between questions, briefly.** Headspace asks why you came before anything else ([Appcues](https://goodux.appcues.com/blog/headspaces-mindful-onboarding-sequence)); Noom teaches throughout. No published proof that explainer screens lift completion, so each is one line and one picture, and the discover path gets only two.
- **Keep the questions few.** Typeform: past six questions, completion falls below half ([Typeform](https://www.typeform.com/blog/tips/survey-school-2-how-to-maximize-survey-response-rates)). Discover path: 4 answers plus the code. Be-found path: 2 more, both skippable.
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
| 9 | Phone | Your mobile number | Phone, plus the unticked text-me box | VoIP or landline → "Please use a mobile number." | "Your number is how you'll sign in. No passwords." · "SocialUs is a place where we look out for one another. ⓘ" (ⓘ: "Your number is tied to everything you post. Illegal content is reported to police.") |  | A phone in a hand, outdoors | One per person; the future account (F081) |
| 10 | Code (A only) | The 6-digit code | Code | Wrong code → "That code didn't match. Try again." | "We texted a code to {number}." |  | — (no image; keep it fast) | Verified count |
| 11 | Done | You're on the list | — | — | "You're on the list for {market}." · "{N} locals are waiting there. When enough makers and neighbours join, we can open." |  | The same market, a little fuller | — |

**When the area opens:** one invite. Its link opens phone sign-up (F081) with name, zip and plans carried in the link, so nothing is asked twice. Someone who wants to be found lands on "Is your Page already here?" (claim or start); someone discovering lands on Explore, led by what they picked. The waitlist entry is then deleted; nothing becomes a type on the member.

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
