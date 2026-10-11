---
id: research-copy-voice-pass-2026-10-10
purpose: Every user-facing string in socialus-web reviewed against the laid-back, no-slang voice and the people's-platform positioning, ranked by how many people see it. Report only; nothing in socialus-web has changed.
layer: research
status: draft
authored: Claude agent, 2026-10-10, at Don's request (voice-dictated)
---

# Copy voice pass: laid-back, plain, the people's platform (2026-10-10)

**Report only.** No copy in `socialus-web` has changed. Read against `socialus-web` `main` at `3315ec8`. After Don approves, a later pass applies these. Path: well-worn for the plain-voice cleanup (the same plain, human, no-slang approach as [Mailchimp's voice and tone guide](https://styleguide.mailchimp.com/voice-and-tone/), [Apple's HIG on writing](https://developer.apple.com/design/human-interface-guidelines/writing) and [Monzo's tone of voice](https://monzo.com/tone-of-voice/)). The tagline and ownership lines touch locked copy and legal exposure, so they need dated `DECISIONS.md` lines (see *Decisions this needs*).

## The short version

- **Reviewed:** about 1,369 user-facing strings across 266 files (counts are approximate; they come from reading each file, not a perfect parser). **Flagged:** about 287 strings, grouped into 178 changes below.
- **The app is already close.** Most copy is plain and short. The work is mostly (a) saying the new positioning where people first meet the name, (b) one error voice instead of about thirty, (c) removing em dashes, (d) turning flat promises into "we currently don't", and (e) retiring leftover vendor-era pages.
- **Ranked by reach.** Sections run from what every visitor sees (front door, sign in) down to what only operators see. Within a section, the most-seen strings come first (T1 everyone, T2 most members, T3 people who run a Page, T4 operators).

### The five biggest changes

1. **Say the tagline and ownership where people first meet the name.** Site title, search and share description, share image, footer and the landing headline become "SocialUs: the people's platform", and "near you" goes. (Section 1.)
2. **Put "built for the people, owned by the members" on About and the signup screen**, without any promise about money, and move flat claims on data and selling to "we currently don't". (Sections 1 and 3.)
3. **One error voice.** About 31 different failure lines, some showing developer prefixes like `report.create:` and `group.update:` to members, become "That didn't go through. Mind trying again?" or a plain one-line fix. (Sections 6 and 7, plus the error lines inside every other section.)
4. **An em dash sweep, led by the browser tab.** Every page title and shared link ends in "— SocialUs" today. It becomes "| SocialUs". About 40 strings in all carry an em dash. (Section 1, and throughout.)
5. **Absolutes become "we currently don't".** Flat "never", "nothing else, ever", "no charge" and "gone for good" lines on signup, onboarding, the waitlist, Privacy and the delete-Page sheet. "Never extractive" stays as the one allowed "never". (Sections 3, 9, 10.)

## Decisions this needs

Both are Don's calls on the record (not legal questions). Neither blocks the later copy pass, but the pass should not ship the tagline before they are written down.

1. **The tagline replaces the locked name line.** `voice-and-tone.md` locks "A local discovery and community-building platform." as the name line (with the subhead). This pass proposes "SocialUs: the people's platform." as the headline and title. It needs a dated `DECISIONS.md` line. The subhead ("Find the local, the quirky, the one of a kind, and the people behind it.") stays.
2. **"We currently don't…" replaces "never" and "always" in copy.** Today the voice file says state things as fact, no promises. This pass keeps that, and adds the "currently" form for data, selling and placement claims. It also drops "near you" from the front door (still banned while there is one metro). It needs a dated line, and `voice-and-tone.md` §§ 1 and 3 updated on Don's say so (agents edit that file only when told to).

## For socialus-legal

Not questions for Don. Nothing in the app promises dividends, payouts, earnings or returns to members. These are the places that touch promises or hard guarantees, so counsel can look before the new wording ships:

- Item 1.20 (`src/lib/landing-copy.ts`): "Owned by the members" is new on a public page. It makes no promise about money, but counsel should confirm it reads safely next to the settled ruling that members are the investors and the only people paid out.
- Item 1.23 (`src/lib/landing-copy.ts`): Forward-looking structural commitments (public benefit corporation, member body, a "lock" on the mission). They read as promises about future governance; counsel should check them before they go public.
- Item 1.24 (`src/lib/landing-copy.ts`): Hard statement about who can invest, written next to the ruling that members are the investors and the only people paid out. Counsel should confirm the wording does not imply a return.
- Item 3.2 (`src/components/onboarding/OnboardingFlow.tsx`): Privacy promise about the zip code. Matches the Privacy page, which has the same "never shown" sentence; counsel should confirm both together.
- Item 3.4 (`src/lib/copy.ts`): Privacy promise about phone numbers; same as the Privacy page ("seen only by operators").
- Item 3.10 (`components/explore/MetroNotCoveredPanel.tsx`): Hard guarantee about how an email address is used ('nothing else, ever'). Confirm with socialus-legal that 'We currently don't use this address for anything else' is accurate.
- Item 5.6 (`lib/unclaimed/samples.ts`): Sample posts show invented discounts attributed to real, unclaimed businesses. They are labeled 'Sample' and 'not a real offer', but counsel should confirm the label is enough.
- Item 9.1 (`src/lib/text-pages.ts`): This changes a stated privacy commitment. Counsel should approve the new wording before it goes live; the page is still a draft.
- Item 9.2 (`src/lib/text-pages.ts`): Same: a data-handling commitment about the automated review. Counsel should approve.
- Item 10.1 (`src/app/join/page.tsx`): Says "There is no charge to create a Page" twice. "No fee" language was retired by ruling (SocialUs takes transaction income). Counsel should confirm it is out.
- Item 10.2 (`src/app/join/page.tsx`): Second "no charge" card. Same as above.
- Item 10.36 (`components/group/edit/PageSettings.tsx`): Says deleted Pages are 'gone for good' after 14 days: a hard guarantee about data. Confirm retention matches before promising it.
- Retired surface (`components/RecruitmentGrid.tsx`): 'No charge to create a Page' reads as a no-fee promise; SocialUs takes transaction income and 'no fee' language is retired.

Also for counsel: the live copy already says members are owners in spirit ("a member body", "owned by", "belongs to"). The proposals use "owned by the members" and nothing about money. Please confirm that phrase sits safely next to the settled ruling that members are the investors and the only people paid out.

## Updated voice guide

This replaces § 3 of `voice-and-tone.md` once approved. Everything else in that file still applies.

**Who we are.** SocialUs: the people's platform. Built for the people and owned by the members. Internal direction only, not copy and not a promise: see `reclaim-standing-rule-2026-10-10.md`. We do not use the word "socialism" in copy.

**How we sound.** Relaxed, plain, unhurried. A friendly person in Sacramento talking, not a brand. The California ease comes from rhythm and word choice (short, easy, no rush), never from slang.

| Do | Don't |
|---|---|
| Short, easy sentences with contractions. "Have a look." "No rush." | Slang: stoked, dude, rad, gnarly, vibes, epic, legit, surf puns. |
| Invite, don't push. "Come on in." "Mind trying again?" | Hype and urgency. "Don't miss out." "Hurry." "Now!" |
| Say what it is plainly. "Built for the people, owned by the members." | Any promise of dividends, payouts, earnings, profit or returns. |
| For data, selling and ads, say "we currently don't…". | Absolutes: "never", "always", "guaranteed", "no fees". The one allowed "never" is "never extractive". |
| Own errors calmly and say what to do next. | Form-speak: "Invalid input", "Submit", "must be", "is required". |
| One light touch per screen at most. Most strings need none. | Warmth or jokes on errors, safety, reports, legal, and sign-in screens. Those stay plain. |
| Keep the house rules: no em dashes, people are never a category, no "near you" with one metro, no zero counts on someone's own work. | Vendors, customers, sellers, makers, creators. Corporate words: utilize, leverage, onboarding, users, content. |

| Instead of | Say |
|---|---|
| Submit | Post it |
| Invalid email | That doesn't look like an email address. |
| Your number is never shown to anyone. | We currently don't show your number to anyone. |
| Something went wrong. Try again. | That didn't go through. Mind trying again? |
| Working… | One sec… |
| Updates arrive in the app, never in your inbox. | Updates show up in the app, not in your inbox. |
| Terms — SocialUs | Terms \| SocialUs |

## What to change, ranked by who sees it

Each change gives where it lives, what it says now, what it should say, and why. Line numbers are against `3315ec8` and are approximate for multi-line strings. Items marked *For socialus-legal* are repeated in the list above.

## 1. Front door, landing, About, and page titles

26 changes · reach T1, T2

**1.1.** `src/app/layout.tsx:27` · Search result and every shared link (site description) · *T1*
- Now: Find and support the people near you. Meet your neighbors, trade what you make, volunteer where it's needed, and share an idea before you build it.
- Change to: SocialUs is the people's platform. Meet your neighbors, trade what you make, lend a hand where it's needed, and try an idea out before you build it.
- Why: Most-read string in the product. Drops "near you" (banned with one metro) and says what it is. Its code comment says wording is the PM's call.

**1.2.** `src/app/layout.tsx:33` · Browser tab and search title for the whole site · *T1*
- Now: SocialUs
- Change to: SocialUs: the people's platform
- Why: Puts the tagline where most people first meet the name. Needs the dated DECISIONS.md line (see voice guide).

**1.3.** `src/app/og-default/route.tsx:16` · Preview image shown when a Page without a photo is shared · *T1*
- Now: Find and support the people near you.
- Change to: SocialUs: the people's platform.
- Why: Same fix as the site description: no "near you", and the tagline is the whole point of the card.

**1.4.** `src/app/about/page.tsx, terms/page.tsx, privacy/page.tsx, rules/page.tsx, landing/about/page.tsx, lib/groups/share-metadata.ts, app/g/[handle]/page.tsx, app/p/[...slug]/page.tsx` · Browser tab titles and shared-link titles (About, Terms, Privacy, The rules, every Page, every "Not found") · *T1*
- Now: Terms — SocialUs  /  Not found — SocialUs  /  {Page name} — SocialUs
- Change to: Terms | SocialUs  /  Not found | SocialUs  /  {Page name} | SocialUs
- Why: Em dashes are banned everywhere. One pattern, about a dozen files; every shared Page link carries it.

**1.5.** `src/components/shell/SiteFooter.tsx:24` · Footer on desktop, every page · *T1*
- Now: © SocialUs
- Change to: © SocialUs, the people's platform
- Why: Footer is the quiet place for the tagline on every screen.

**1.6.** `src/lib/landing-copy.ts:8` · /landing hero headline (preview, noindex, not linked yet) · *T1*
- Now: A local discovery platform, for the people.
- Change to: SocialUs: the people's platform.
- Why: This is the tagline Don gave. Replaces the locked name line, so it needs a dated DECISIONS.md line first (the file's own comment says so).

**1.7.** `src/lib/landing-copy.ts:11` · /landing three verb lines · *T1*
- Now: Find what’s good near you, and get found.
- Change to: Find what’s good where you live, and get found.
- Why: "Near you" is banned while there is one metro; "where you live" is the wording About already uses.

**1.8.** `src/lib/landing-copy.ts:13` · /landing three verb lines · *T1*
- Now: Shape your community, and help build what comes next.
- Change to: Help build what comes next. It’s built for the people and owned by the members.
- Why: Puts the ownership idea on the front door in plain words, with no promise about money.

**1.9.** `src/lib/landing-copy.ts:15` · /landing secondary button and link to the About page · *T1*
- Now: How we’re different
- Change to: About SocialUs
- Why: "How we're different" reads as a "why us" section, which the house rules rule out.

**1.10.** `src/lib/landing-copy.ts:50` · /landing "Want to be found?" paragraph · *T1*
- Now: People searching for what you do find you by what you do, not by what you paid. Nobody buys their way to the top here.
- Change to: People searching for what you do find you by what you do, not by what you paid. We currently don’t sell placement.
- Why: Swaps a flat absolute for the "we currently don't" phrasing.

**1.11.** `src/lib/landing-copy.ts:58` · /landing members line · *T1*
- Now: Other apps call you users. We call you members. We’re in this together, and this is for us.
- Change to: Other apps call you users. We call you members, because this belongs to the people in it. We’re in this together.
- Why: Says the ownership idea once, plainly. "Belongs to" is not a promise about money.

**1.12.** `src/lib/landing-copy.ts:69` · /landing waitlist note under the email box · *T1*
- Now: We’re opening one community at a time. You’ll hear from us when yours is ready, and that’s all we use your email for.
- Change to: We’re opening one community at a time. We’ll let you know when yours is ready. We currently use your email for that and nothing else.
- Why: Keeps the promise honest and time-bound instead of absolute.

**1.13.** `src/lib/landing-copy.ts:76` · /landing waitlist email error · *T1*
- Now: That does not look like an email address.
- Change to: That doesn’t look like an email address.
- Why: Contraction; same tone as the other error lines.

**1.14.** `src/lib/copy.ts:28` · Signup and onboarding "what this app is" line · *T1*
- Now: This is a community building app. It was made for good and decent people to find, connect with and support other good and decent people. We are here to build a better future together.
- Change to: SocialUs is the people's platform, built for the people and owned by the members. [Don's 2026-10-01 line follows, unchanged.]
- Why: Don's words stay. One line above them carries the tagline on the first screen a new member sees.

**1.15.** `app/m/[handle]/{e,p,s}/[slug]/page.tsx and app/m/[handle]/page.tsx:22 / 22 / 22 / 15 (title), 25 (title)` · Browser tab title of a member's event, product, service page and of Not found · *T1*
- Now: Not found — SocialUs / ${title} — SocialUs
- Change to: Not found | SocialUs / ${title} | SocialUs
- Why: Em dash in page titles.

**1.16.** `app/g/[handle]/page.tsx:30` · Browser tab title when a Page isn't found · *T1*
- Now: Not found — SocialUs
- Change to: Not found | SocialUs
- Why: Em dash.

**1.17.** `app/p/[...slug]/page.tsx:73, 76, 93, 96, 113, 116, 130, 133, 141, 145, 151, 152` · Browser tab titles for items, venues and places · *T1*
- Now: Not found — SocialUs / ${product.title} — SocialUs / Place not found — SocialUs / ${venue.label} — SocialUs
- Change to: Not found | SocialUs / ${product.title} | SocialUs / Place not found | SocialUs / ${venue.label} | SocialUs
- Why: Em dashes in every title.

**1.18.** `lib/groups/share-metadata.ts:25, 32` · Browser tab title and link preview for a shared Page · *T1*
- Now: ${title} — SocialUs
- Change to: ${title} | SocialUs
- Why: Em dash.

**1.19.** `src/lib/landing-copy.ts:85` · /landing/about page title · *T2*
- Now: How we’re different
- Change to: About SocialUs
- Why: Same reason as the landing button.

**1.20.** `src/lib/landing-copy.ts:93` · /landing/about "What this is for" third paragraph · *T2*
- Now: SocialUs is never extractive. It doesn’t sell your data. It doesn’t sell placement. It doesn’t keep you scrolling. It makes its money in plain ways, from what happens on it, and keeps what it needs to run.
- Change to: SocialUs is never extractive. We currently don’t sell your data or sell placement, and we don’t keep you scrolling. It makes its money in plain ways, from what happens on it, and keeps what it needs to run. It’s built for the people and owned by the members.
- Why: "Never extractive" is the one allowed "never". The rest moves to "currently". Adds the tagline idea (built for / owned by) without any promise about money. Note: we do collect data (name, email, zip, a phone check), so copy never says we collect none. No public statement about how data is used yet; that is internal direction.
- For socialus-legal: "Owned by the members" is new on a public page. It makes no promise about money, but counsel should confirm it reads safely next to the settled ruling that members are the investors and the only people paid out.

**1.21.** `src/lib/landing-copy.ts:115` · /landing/about "What we're building" closing line · *T2*
- Now: Each of these lands when it’s ready, not on a date.
- Change to: Each one shows up when it’s ready, not on a date.
- Why: "Lands" is product-team vocabulary.

**1.22.** `src/lib/landing-copy.ts:119` · /landing/about section title · *T2*
- Now: How the company grows up
- Change to: How the company takes shape
- Why: "Grow" is on the hustle-word list.

**1.23.** `src/lib/landing-copy.ts:127` · /landing/about company steps (last two) · *T2*
- Now: A member body, so people have a real say in what happens where they live. / A structure that locks the mission in, so this can’t be sold out from under the people on it.
- Change to: Owned by the members: a member body, so people have a real say in what happens where they live. / A structure that keeps the mission in place, so this can’t be sold out from under the people on it.
- Why: Names the ownership step in plain words.
- For socialus-legal: Forward-looking structural commitments (public benefit corporation, member body, a "lock" on the mission). They read as promises about future governance; counsel should check them before they go public.

**1.24.** `src/lib/landing-copy.ts:130` · /landing/about investors paragraph · *T2*
- Now: We don’t take money from traditional investors. No venture capital, no private equity. This stays grassroots, and it’s built for the small shop, the one-person operation, and the group with twelve people in it.
- Change to: We currently don’t take money from venture capital or private equity. This stays grassroots, and it’s built for the small shop, the one-person operation, and the group with twelve people in it.
- Why: Flat "don't" becomes "currently don't". Drops "traditional investors" because members are the investors (a settled ruling), so the line stays accurate.
- For socialus-legal: Hard statement about who can invest, written next to the ruling that members are the investors and the only people paid out. Counsel should confirm the wording does not imply a return.

**1.25.** `src/lib/landing-copy.ts:139` · /landing/about "Who this is set up for" last paragraph · *T2*
- Now: Other apps call you users. A user is someone a product is done to. A member is someone it belongs with. We’re in this together, and this is for us.
- Change to: Other apps call you users. A user is someone a product is done to. A member is someone it belongs to. We’re in this together.
- Why: "Belongs to" carries the owned-by-members idea. "Belongs with" is vague.

**1.26.** `src/lib/text-pages.ts:22` · /about page (live today, one paragraph) · *T2*
- Now: This is a community building app. It was made for good and decent people to find, connect with and support other good and decent people. We are here to build a better future together.
- Change to: SocialUs is the people's platform. Built for the people, owned by the members. [Don's 2026-10-01 paragraph stays below, unchanged.]
- Why: The paragraph is Don's ruled wording, so it is kept. The tagline and the ownership line go above it so the live About page says the new thing.


## 2. Sign in and sign up

13 changes · reach T1, T2

**2.1.** `src/components/auth/EmailFirstSignup.tsx:175` · "Check your email" screen after asking for a sign-in link · *T1*
- Now: We sent a sign-in link to {email}. Click it to finish — no password needed.
- Change to: We sent a sign-in link to {email}. Tap it to finish. No password needed.
- Why: Em dash out, easier verb.

**2.2.** `src/components/auth/EmailFirstSignup.tsx:189` · "Confirm your email" screen · *T1*
- Now: We sent a confirmation link to {email}. Confirm it, then come back to finish setting up.
- Change to: Open the link we sent to {email}, then come back and finish setting up.
- Why: Plainer, one verb less.

**2.3.** `src/components/auth/EmailFirstSignup.tsx:84` · Email box error on sign-in and sign-up (also MagicLinkForm.tsx:33) · *T1*
- Now: Enter a valid email address.
- Change to: That doesn't look like an email address.
- Why: "Valid" is form-speak. Same line used on the landing waitlist.

**2.4.** `src/components/auth/EmailFirstSignup.tsx:92` · Catch-all error on sign-up (also OnboardingFlow.tsx:77) · *T1*
- Now: Something went wrong. Try again.
- Change to: That didn't go through. Mind trying again?
- Why: Uses the house error line so every error sounds the same.

**2.5.** `src/components/auth/EmailFirstSignup.tsx:102` · Password error when making a password · *T1*
- Now: Password must be at least 8 characters.
- Change to: Passwords need at least 8 characters.
- Why: Softer, same information.

**2.6.** `src/components/auth/EmailFirstSignup.tsx:112` · Error when an email already has an account · *T1*
- Now: You already have an account — enter your password.
- Change to: Looks like you already have an account. Enter your password to sign in.
- Why: Em dash out; friendlier first half.

**2.7.** `src/components/auth/EmailFirstSignup.tsx:252` · Button while sign-in or sign-up is working (also line 315, PhoneVerifyStep) · *T1*
- Now: Working…
- Change to: One sec…
- Why: Plain, a little more human.

**2.8.** `src/components/auth/EmailFirstSignup.tsx:327` · Link under the password box · *T1*
- Now: Sign in with a magic link instead
- Change to: Email me a sign-in link instead
- Why: "Magic link" is jargon, and MagicLinkForm already says "Email me a link instead". One name for one thing.

**2.9.** `src/components/AuthGateModal.tsx:52` · Prompt shown to a signed-out visitor who taps something that needs an account · *T1*
- Now: We email you a link — no password, takes 30 seconds.
- Change to: We'll email you a link. No password, and it only takes a minute.
- Why: Em dash out; drops a timing claim we can't back.

**2.10.** `src/lib/auth/requires-account.ts:51` · "Sign in to get updates" prompt · *T1*
- Now: Updates arrive in the app, on your account — never in your inbox.
- Change to: Updates show up in the app, not in your inbox.
- Why: Drops "never" and the em dash.

**2.11.** `src/lib/auth/requires-account.ts:68` · "Sign up to see the map" prompt · *T1*
- Now: The map is for members, so what is on it stays with the people here.
- Change to: The map is for members, so what's on it stays with the people here.
- Why: Contraction only.

**2.12.** `src/components/AuthGateModal.tsx:56` · Same prompt, second link · *T2*
- Now: Are you a business owner? Create a Page for your business →
- Change to: Run a business? Start a Page for it.
- Why: Shorter and avoids a person-category question.

**2.13.** `src/lib/auth/requires-account.ts:58` · "Sign in to report this" prompt · *T2*
- Now: An account lets us slow down someone reporting the same business over and over. It is not an identity check.
- Change to: An account lets us slow down anyone reporting the same business over and over. It's not an identity check.
- Why: Contraction; keeps the safety tone plain.


## 3. Onboarding and metro waitlist

15 changes · reach T1, T2

**3.1.** `src/components/onboarding/OnboardingFlow.tsx:108` · "Where are you, and why?" step (metro not open yet) · *T1*
- Now: We are not everywhere yet. Tell us where you are and we will tell you where it stands.
- Change to: We're not everywhere yet. Tell us where you are and we'll tell you where things stand.
- Why: Contractions.

**3.2.** `src/components/onboarding/OnboardingFlow.tsx:175` · Help line under the zip box · *T1*
- Now: It decides your metro. It is never shown to anyone.
- Change to: It picks your metro. We currently don't show it to anyone.
- Why: Moves a "never" to "we currently don't" and softens "decides".
- For socialus-legal: Privacy promise about the zip code. Matches the Privacy page, which has the same "never shown" sentence; counsel should confirm both together.

**3.3.** `src/components/onboarding/OnboardingFlow.tsx:92` · "You're in Sacramento" confirmation · *T1*
- Now: Your zip code decided this. You can change it any time from your account.
- Change to: Your zip code picked this. You can change it anytime from your account.
- Why: Lighter verb.

**3.4.** `src/lib/copy.ts:30` · Phone check step · *T1*
- Now: Everyone here is a real person. We'll text you a code to check. Your number is never shown to anyone.
- Change to: Everyone here is a real person. We'll text you a code to check. We currently don't show your number to anyone.
- Why: "Never" to "currently don't".
- For socialus-legal: Privacy promise about phone numbers; same as the Privacy page ("seen only by operators").

**3.5.** `src/components/metro/MetroWaitlistStep.tsx:58` · Error when joining a metro waitlist · *T1*
- Now: That did not go through. Try again?
- Change to: That didn't go through. Mind trying again?
- Why: House error line.

**3.6.** `src/lib/signup/profile.ts:35` · Error on the 18+ checkbox · *T1*
- Now: Please confirm you are 18 or older.
- Change to: Please confirm you're 18 or older.
- Why: Contraction.

**3.7.** `components/explore/MetroNotCoveredPanel.tsx:61` · Metro waitlist role choices · *T1*
- Now: I’m looking for what’s nearby
- Change to: I’m looking for what’s on here
- Why: 'nearby' banned; people-category framing via role split.

**3.8.** `components/explore/MetroNotCoveredPanel.tsx:122` · Metro waitlist error · *T1*
- Now: That did not go through. Try again?
- Change to: That didn't go through. Mind trying again?
- Why: Guide's error wording; no stiff 'did not'.

**3.9.** `components/explore/MetroNotCoveredPanel.tsx:191` · Metro waitlist confirmation · *T1*
- Now: Done — you’re counted in ${metro.name}.
- Change to: Done. You're counted in ${metro.name}.
- Why: Em dash.

**3.10.** `components/explore/MetroNotCoveredPanel.tsx:219-220` · Metro waitlist email field note · *T1*
- Now: One message, if this metro opens. That is the only thing this address is used for — nothing else, ever.
- Change to: We'll send one message if this metro opens. We currently don't use this address for anything else.
- Why: Absolutes 'nothing else, ever' and an em dash; data claim uses the 'We currently don't' form.
- For socialus-legal: Hard guarantee about how an email address is used ('nothing else, ever'). Confirm with socialus-legal that 'We currently don't use this address for anything else' is accurate.

**3.11.** `components/explore/MetroNotCoveredPanel.tsx:176` · Metro waitlist intro · *T1*
- Now: You can’t browse here yet. Telling us you’re here is what decides where it opens next.
- Change to: You can't browse here yet. Telling us you're here helps us decide where to open next.
- Why: Softens a claim that implies a firm commitment about expansion.

**3.12.** `actions/metro/waitlist-join-anonymous.ts:76` · Leaving an email on the waitlist · *T1*
- Now: That does not look like an email address.
- Change to: That doesn't look like an email address.
- Why: Use the contraction.

**3.13.** `src/lib/metro/waitlist-standing.ts` · Popup after joining the waitlist for a metro that is not open · *T2*
- Now: This metro needs {n} more people before there is enough here to be worth showing you.
- Change to: We need {n} more people in {metro} before it's ready to open. We'll let you know.
- Why: "Worth showing you" sounds like a sales line; this says the same thing plainly. The notify promise matches the landing waitlist.

**3.14.** `src/lib/metro/waitlist-standing.ts` · Same popup, when enough people are in · *T2*
- Now: Enough people are here. A person reviews each metro before it goes live.
- Change to: There are enough people here. A person looks over each area before it opens.
- Why: Plainer words.

**3.15.** `lib/onboarding/interest-vocab.ts:13` · Interests picker · *T2*
- Now: Crafts & makers
- Change to: Crafts
- Why: 'makers' is a banned people-category word.


## 4. Explore (browse, map, search)

7 changes · reach T1, T2

**4.1.** `components/browse/BrowseSurface.tsx:299` · Explore with no results · *T1*
- Now: Nothing here yet — try another filter
- Change to: Nothing here yet. Maybe try a bit wider.
- Why: Em dash; matches house empty-state line.

**4.2.** `components/browse/BrowseSurface.tsx:201-205 (approx; error at 295)` · Explore load failure · *T1*
- Now: We couldn’t load ${metroName} just now. Try again in a moment.
- Change to: That didn't go through. Mind trying again in a moment?
- Why: Errors: own it and invite, per guide.

**4.3.** `components/explore/ExploreDock.tsx + ExploreFilterSheet/ExploreSearchBar:ExploreDock 60; ExploreSearchBar 86,115` · Screen-reader labels on Explore filter and area buttons · *T1*
- Now: Filter — filters applied / Open filters — filters applied / Area: ${label} — change it
- Change to: Filter, filters on / Open filters, filters on / Area: ${label}, tap to change
- Why: Em dashes in aria labels.

**4.4.** `components/explore/ExploreSearchBar.tsx:143` · Explore search box (screen-reader label) · *T1*
- Now: Search Browse
- Change to: Search Pages and posts
- Why: 'Browse' is product-team vocabulary; matches placeholder.

**4.5.** `components/explore/AreaPicker.tsx:208` · Choose your area sheet · *T1*
- Now: {n} more — search to narrow.
- Change to: {n} more. Search to narrow it down.
- Why: Em dash.

**4.6.** `components/explore/AreaPicker.tsx:160` · Choose your area sheet, neighborhoods heading · *T1*
- Now: Neighbourhoods in ${currentName}
- Change to: Neighborhoods in ${currentName}
- Why: British spelling; house copy is US English.

**4.7.** `components/SearchBar.tsx:141` · Map search box · *T2*
- Now: Search businesses...
- Change to: Search places
- Why: "Businesses" is a category word and the ellipsis reads as a trailing-off; check this is the live map before changing.


## 5. Pages, posts and places (public view)

20 changes · reach T1, T2, T3

**5.1.** `app/p/[...slug]/page.tsx:135` · Search and share description for a venue with no description · *T1*
- Now: ${venue.label} — a venue on SocialUs.
- Change to: ${venue.label} is a venue on SocialUs.
- Why: Em dash.

**5.2.** `app/p/[...slug]/page.tsx:289` · Place page body · *T1*
- Now: The curated landing for this place ships at b2 (places.md § T2). For now, you've confirmed the URL resolves and the place tree is wired.
- Change to: Nothing here yet. Have a look around Explore.
- Why: Release numbers and dev jargon on a public screen.

**5.3.** `components/OwnershipBadge.tsx:6, 8, 9` · Ownership badge on a business Page · *T1*
- Now: Worker or member owned / Competing against market consolidation / B Corp / Public Benefit Corporation
- Change to: Owned by its members / Independent, up against big chains / B Corp or Public Benefit Corporation
- Why: 'Workers' is off-guide, 'market consolidation' is jargon and a competitor stance, slash is stiff.

**5.4.** `lib/groups/resolve-page-placement.ts:79` · Fallback label on a Page's place on Explore · *T1*
- Now: a nearby neighbourhood
- Change to: a Sacramento neighborhood
- Why: 'Nearby' and British spelling.

**5.5.** `components/venue/VenuePublicPage.tsx:131` · Venue page section heading · *T1*
- Now: What's happening nearby
- Change to: Elsewhere in Sacramento
- Why: 'Nearby'.

**5.6.** `lib/unclaimed/samples.ts:40-67 (examples: 'This week only at {name}', 'Tonight only at {name}', 'Book it before it goes', 'available tomorrow only', 'while they last', 'for people nearby', 'Meet the maker night', 'Maker pop-up')` · Sample posts on unclaimed business Pages (each opens with 'Sample' and says it isn't a real offer) · *T1*
- Now: This week only at {name}: 15% off ... / Tonight only at {name}: one night's stay at a reduced rate. Message us today. / Last-minute opening ... Book it before it goes. / 10% off your first repair for people nearby. / Meet the maker night at {name}
- Change to: This week at {name}: 15% off ... / Tonight at {name}: one night's stay at a reduced rate. Message us today. / An opening at {name} this weekend: a cancellation freed up a room. / 10% off your first repair for people in the area. / Meet the people behind {name}
- Why: Urgency, 'nearby', 'maker', and British 'neighbour(s)' (use 'neighbors'). Applies across all 18 variants.
- For socialus-legal: Sample posts show invented discounts attributed to real, unclaimed businesses. They are labeled 'Sample' and 'not a real offer', but counsel should confirm the label is enough.

**5.7.** `components/item/ProductPublicPage.tsx:77` · Badge on a product · *T1*
- Now: Locally Made
- Change to: Keep the badge only where the Page owner makes the claim; otherwise "Made in Sacramento".
- Why: A claim about the product that nothing in the app verifies.

**5.8.** `components/item/ShareLinkButton.tsx:43` · Copying a link · *T1*
- Now: Copied!
- Change to: Copied.
- Why: Exclamation mark.

**5.9.** `components/group/FollowPageButton.tsx:75` · Error under Follow/Join · *T2*
- Now: That did not go through. Mind trying again?
- Change to: That didn't go through. Mind trying again?
- Why: Match the house line, use the contraction.

**5.10.** `components/venue/FollowVenueButton.tsx:62` · Error under Follow this venue · *T2*
- Now: Something went wrong.
- Change to: That didn't go through. Mind trying again?
- Why: Match the house error line.

**5.11.** `lib/groups/opening-hours.ts:23-31` · Error when saving opening hours · *T3*
- Now: Opening hours must be a week of days. / ${day}: times are HH:MM / ${day}: closing comes after opening / ${day}: hours must be a list
- Change to: Those hours didn't look right. Mind checking them? / ${day}: use a time like 9:00. / ${day}: closing needs to come after opening.
- Why: Jargon (HH:MM) and robotic phrasing.

**5.12.** `lib/groups/social-handles.ts:70, 151` · Hint under the Bluesky field and fallback error · *T3*
- Now: — a Bluesky handle looks like a domain / That does not look right
- Change to: (a Bluesky handle looks like a domain) / That doesn't look right.
- Why: Em dash and missing contraction.

**5.13.** `components/group/SocialHandleFields.tsx:46, 81` · Where else to find you (links form) · *T3*
- Now: Just your username — we'll build the link. / aria-label: {platform label} — ${field.prefix}
- Change to: Just your username. We'll build the link. / {platform label}, ${field.prefix}
- Why: Em dashes.

**5.14.** `components/group/OwnerBar.tsx:32` · Owner strip on a Page · *T3*
- Now: Your Page — only you see this
- Change to: Your Page. Only you see this.
- Why: Em dash.

**5.15.** `components/group/OwnerBar.tsx:37` · Owner buttons that open the post composer (also OwnerPanel.tsx line 24) · *T3*
- Now: Announce
- Change to: New post
- Why: 'Post' is the noun on a Page, and the verb should not differ from the Posts heading.

**5.16.** `components/group/OwnerPanel.tsx:24` · Owner panel button · *T3*
- Now: Announce
- Change to: New post
- Why: Same as the owner strip.

**5.17.** `components/group/PagePosts.tsx:686` · Post composer submit button · *T3*
- Now: Announce / Announcing
- Change to: Post it / Posting…
- Why: Guide's 'Submit -> Post it'.

**5.18.** `components/group/LocallyOwnedClaim.tsx:159, 175` · Locally Owned claim box on a Page owner's settings · *T3*
- Now: You haven't claimed Locally Owned yet — add your ZIP to display the badge. / Claimed local owner — ZIP on file: {claim.zip}.
- Change to: You haven't claimed Locally Owned yet. Add your ZIP to show the badge. / Claimed local owner. ZIP on file: {claim.zip}.
- Why: Em dashes.

**5.19.** `components/group/LocallyOwnedClaim.tsx:49, 59, 72` · Errors in the Locally Owned claim box · *T3*
- Now: Enter a 5-digit US ZIP code. / Could not save your ZIP. / Could not remove your claim.
- Change to: That doesn't look like a ZIP code. Mind checking it? / That didn't save. Mind trying again? / That didn't go through. Mind trying again?
- Why: Robotic error phrasing.

**5.20.** `components/OwnershipSelector.tsx:8, 24` · Ownership picker (appears unused outside the old sell walkthrough) · *T3*
- Now: This business is owned by its workers or members / Ownership Type
- Change to: This business is owned by its members / How it's owned
- Why: 'Workers'; title case label.


## 6. Errors (one shared voice)

9 changes · reach T1, T2, T3

**6.1.** `src/app/error.tsx, src/app/global-error.tsx:16` · Whole-page error screen · *T1*
- Now: Something went wrong / It's on our side. Try again in a moment.
- Change to: That didn't go through. It's on us. Mind trying again in a minute?
- Why: Uses the house error line. Stays plain (errors get no extra warmth).

**6.2.** `src/app/not-found.tsx:9` · Page not found · *T1*
- Now: We couldn't find that / It may have moved, or it may not be shared with you.
- Change to: Can't find that one. / It may have moved, or it may not be shared with you.
- Why: Already plain and kind; only a small ease tweak. Optional.

**6.3.** `app/create/actions.ts:33` · Create: What are you starting? (error) · *T2*
- Now: That didn't go through. Try again?
- Change to: That didn't go through. Mind trying again?
- Why: Match the house error line.

**6.4.** `actions/_lib/handler.ts:31` · Any action rejecting your input · *T2*
- Now: Invalid input for ${name}
- Change to: That didn't go through. Mind checking what you entered?
- Why: "Invalid" and an internal action name.

**6.5.** `app/_actions/location-actions.ts:56, 46, 211, 220` · Saving a Location while signed out, or when saving fails · *T3*
- Now: You must be signed in. / Something went wrong. Try again. / Could not save the new Location.
- Change to: Sign in first. / That didn't go through. Mind trying again? / That didn't go through. Mind trying again?
- Why: Stiff and robotic errors.

**6.6.** `app/_actions/location-actions.ts:96` · Adding a Location with no address · *T3*
- Now: A Location needs a real address or a neighbourhood — we never guess one.
- Change to: Add an address or a neighborhood so people can find it.
- Why: Absolute "never", em dash, British spelling.

**6.7.** `app/_actions/location-actions.ts:152` · Picking a place that cannot be found · *T3*
- Now: We could not find that place. Try searching for it again.
- Change to: We couldn't find that place. Mind searching again?
- Why: Stiff; add the invite.

**6.8.** `app/_actions/page-lifecycle-actions.ts:20` · Changing a Page while signed out · *T3*
- Now: You must be signed in.
- Change to: Sign in first.
- Why: Stiff; matches the Post composer ("Sign in first.").

**6.9.** `lib/media/upload-image.ts:37, 40, 47, 59, 75, 81, 94, 115` · Adding a photo that fails to process · *T3*
- Now: That file is too large to process. / This browser cannot process images. / That file is not a readable image. / Image encoding timed out. / Could not encode the image. / That photo is too large even after resizing. / it didn't reach our storage
- Change to: That file is too big. / This browser can't work with photos. / That file doesn't look like a photo. / That took too long. / We couldn't prepare that photo. / That photo is still too big after shrinking it. / It didn't reach us.
- Why: Technical wording ("encode", "process"). Each should end with a period so the picker can append its line.


## 7. Reporting and safety notices

17 changes · reach T1, T2

**7.1.** `app/report/actions.ts:30` · Report a problem form fails · *T1*
- Now: We couldn’t send that. Try again in a while.
- Change to: That didn't go through. Mind trying again?
- Why: House error line.

**7.2.** `components/member/YouNotices.tsx:66` · Answering a report notice failed · *T2*
- Now: That didn't go through. Please try again.
- Change to: That didn't go through. Mind trying again?
- Why: Drop stiff 'Please'.

**7.3.** `components/group/ReportSheet.tsx:58` · Error when a report fails to send · *T2*
- Now: That did not send. Try again?
- Change to: That didn't go through. Mind trying again?
- Why: Match the house error line.

**7.4.** `components/group/ReportSheet.tsx:70` · Report sheet subtitle · *T2*
- Now: This goes to a person, not a queue.
- Change to: A person reads this.
- Why: 'Queue' is product-team vocabulary.

**7.5.** `components/group/ReportControl.tsx:69, 70` · Report menu item on a Page or post · *T2*
- Now: Report to the operator
- Change to: Report this
- Why: 'Operator' is internal vocabulary; say what it does.

**7.6.** `components/group/ReportControl.tsx:98` · Confirmation after sending a report · *T2*
- Now: Thank you — that went to a person, and they'll take a look.
- Change to: Thanks. That went to a person, and they'll take a look.
- Why: Em dash.

**7.7.** `actions/report/create.ts:362` · Reporting a Page or Post, when you have many reports open · *T2*
- Now: report.create: you have a lot of reports open already — we will get to them before taking more
- Change to: You have a few reports waiting on us already. We'll get through those first.
- Why: Internal prefix shows to the member, em dash, stiff.

**7.8.** `actions/report/create.ts:367` · Reporting something you already reported · *T2*
- Now: report.create: you have already reported this one — we have it
- Change to: You already reported this one. We have it.
- Why: Internal prefix and em dash.

**7.9.** `actions/report/create.ts:307` · Reporting while signed out · *T2*
- Now: report.create: a signed-in member is required; anonymous reporting is out of v1
- Change to: Sign in first, then send your report.
- Why: Version jargon and internal prefix.

**7.10.** `actions/report/create.ts:318` · Sending a report with no words · *T2*
- Now: report.create: body must not be empty
- Change to: Add a few words about what happened.
- Why: Developer message; plain instruction instead.

**7.11.** `actions/report/create.ts:322` · Sending a report that is too long · *T2*
- Now: report.create: body must be ${BODY_MAX_LENGTH} characters or fewer
- Change to: Keep it to ${BODY_MAX_LENGTH} characters or fewer.
- Why: Developer message.

**7.12.** `actions/report/answer.ts:26, 41, 42, 44` · Answering a notice that something of yours was hidden · *T2*
- Now: report.answer: a signed-in member is required / not yours to answer / this one has been answered already / this one has closed
- Change to: Sign in first. / That one isn't yours to answer. / You've already answered this one. / This one has closed, so it can't be answered now.
- Why: Internal prefixes and stiff phrasing reach the poster.

**7.13.** `app/_actions/report-actions.ts:24` · Reporting or answering a notice while signed out · *T2*
- Now: You must be signed in.
- Change to: Sign in first.
- Why: Stiff; matches the other sign-in errors.

**7.14.** `lib/reports/notices.ts:11` · Notice that something of yours was hidden after a report · *T2*
- Now: Someone reported ${what} ${pageName} as "${categoryLabel(category)}", so we've hidden it while we take a look. Nothing is deleted.
- Change to: Someone reported ${what} ${pageName} as "${categoryLabel(category)}". We've hidden it while we take a look. It hasn't been deleted.
- Why: Splits one long sentence; "Nothing is deleted" reads as an absolute about data.

**7.15.** `lib/reports/categories.ts:12` · Report reasons list · *T2*
- Now: Sensitive content — children, animals and pets, or anyone who can't fend for themselves
- Change to: Sensitive content: children, animals and pets, or anyone who can't fend for themselves
- Why: Em dash.

**7.16.** `lib/admin/reason-codes.ts:65, 71, 77, 83` · Notice that your photo was taken down · *T2*
- Now: We took your photo down — it isn’t about a real place or business. (also: looks like someone else’s work; isn’t suitable for a neighbourhood app; shows someone who didn’t agree to be in it)
- Change to: We took your photo down. It isn’t about a real place or business. / ...It looks like someone else’s work. / ...It isn’t suitable here. / ...It shows someone who didn’t agree to be in it.
- Why: Em dashes; "neighbourhood" is British and "neighbourhood app" is product-speak.

**7.17.** `lib/admin/reason-codes.ts:86-91` · Notice that your post or Page was taken down · *T2*
- Now: We took it down — it targeted someone in a way that isn’t okay here. (harassment, threat, violence, nudity, sensitive, spam variants)
- Change to: We took it down. It targeted someone in a way that isn’t okay here. / ...It read as a threat to someone. / ...It shows or encourages violence. / ...It has nudity, which isn’t for here. / ...It has content we can’t host right now. / ...It read as spam.
- Why: Em dash in six notices; "while we're a small team" is an excuse that adds nothing.


## 8. You, Following, and member screens

14 changes · reach T2, T3

**8.1.** `components/follows/FollowingManager.tsx:172` · Following list, empty · *T2*
- Now: Nothing followed yet — start exploring.
- Change to: Nothing followed yet. Have a look around.
- Why: Em dash; invites rather than pushes.

**8.2.** `components/follows/FollowingManager.tsx; components/member/FollowMemberButton.tsx:FollowingManager 76, 88; FollowMemberButton 60` · Unfollow/follow/undo failed · *T2*
- Now: Something went wrong.
- Change to: That didn't go through. Mind trying again?
- Why: Vague error; guide wording. Note: real err.message from actions (e.g. 'member.follow: cannot follow yourself') can show instead, low reach.

**8.3.** `components/member/DefaultMetro.tsx:48` · You, Metro setting · *T2*
- Now: Couldn’t save. Try again.
- Change to: Couldn't save that. Mind trying again?
- Why: Guide's error wording.

**8.4.** `lib/types.ts:235,240 (REPORT_PILLARS labels Customers, Employees)` · Report form, what the report is about · *T2*
- Now: Customers / Employees
- Change to: People who shop here / People who work here
- Why: People-category words (customers); verify screen is live (used by ReportForm via PillarSelector).

**8.5.** `app/you/following/page.tsx:16` · Following page, browser tab title · *T2*
- Now: Following — SocialUs
- Change to: Following | SocialUs
- Why: Em dash in metadata.

**8.6.** `components/member/OwnPages.tsx:219` · Delete unfinished Page sheet · *T3*
- Now: “${discarding.name}” was never public. It’s gone for good.
- Change to: “${discarding.name}” hasn't been public. Deleting it can't be undone.
- Why: 'gone for good' is an absolute; say the fact plainly.

**8.7.** `app/you/sell/actions.ts:70` · Starting a Page while signed out (error) · *T3*
- Now: You must be signed in to start selling.
- Change to: Sign in first, then try again.
- Why: Stiff, and leans on selling; plain account wording.

**8.8.** `app/you/sell/gathering/actions.ts:36` · Hosting a gathering while signed out (error) · *T3*
- Now: You must be signed in to host a gathering.
- Change to: Sign in first, then try again.
- Why: Stiff "must"; plain account wording.

**8.9.** `app/you/sell/product/actions.ts:34` · Adding a product while signed out (error) · *T3*
- Now: You must be signed in to list a product.
- Change to: Sign in first, then try again.
- Why: Stiff "must"; "list" is marketplace wording.

**8.10.** `app/you/sell/service/actions.ts:34` · Adding a service while signed out (error) · *T3*
- Now: You must be signed in to list a service.
- Change to: Sign in first, then try again.
- Why: Stiff "must"; "list" is marketplace wording.

**8.11.** `app/you/sell/actions.ts:164` · After creating a Page (error) · *T3*
- Now: Your Page was created, but we could not resolve its address. Refresh /you to see it.
- Change to: Your Page is up, but we couldn't open it just now. You'll find it under You.
- Why: Shows a route path and "resolve"; not plain.

**8.12.** `app/you/sell/gathering/actions.ts:150` · After publishing a gathering (error) · *T3*
- Now: Your gathering was published, but we could not resolve its URL. Refresh /you to see it.
- Change to: Your gathering is up, but we couldn't open it just now. You'll find it under You.
- Why: Shows a route path and "URL" jargon.

**8.13.** `app/you/sell/product/actions.ts:135` · After publishing a product (error) · *T3*
- Now: Your product was published, but we could not resolve its URL. Refresh /you to see it.
- Change to: Your product is up, but we couldn't open it just now. You'll find it under You.
- Why: Shows a route path and "URL" jargon.

**8.14.** `app/you/sell/service/actions.ts:166` · After publishing a service (error) · *T3*
- Now: Your service was published, but we could not resolve its URL. Refresh /you to see it.
- Change to: Your service is up, but we couldn't open it just now. You'll find it under You.
- Why: Shows a route path and "URL" jargon.


## 9. Terms and Privacy

2 changes · reach T2

**9.1.** `src/lib/text-pages.ts:68` · /privacy, "who sees what" paragraph · *T2*
- Now: Your zip code is never shown to another member or to a visitor; it is used to place you in your metro, and you can change it from your account.
- Change to: We currently don't show your zip code to another member or to a visitor. It's used to place you in your metro, and you can change it from your account.
- Why: "Never" to "currently don't", plus a breath between two ideas. Privacy is plain-only, so no extra warmth.
- For socialus-legal: This changes a stated privacy commitment. Counsel should approve the new wording before it goes live; the page is still a draft.

**9.2.** `src/lib/text-pages.ts:70` · /privacy, "reported posts" paragraph · *T2*
- Now: We never send it names, emails or other member details. A person always decides.
- Change to: We currently don't send it names, emails or other member details. A person makes the call.
- Why: Same swap; "always" to a plain verb.
- For socialus-legal: Same: a data-handling commitment about the automated review. Counsel should approve.


## 10. Owners: creating, editing and joining

41 changes · reach T2, T3

| # | Where | Current | Proposed | Why |
|---|---|---|---|---|
| 10.1 | `src/app/join/page.tsx:50` · /join hero (a farmers-market pitch from the old model) | For vendors / Sell at a farmers market? Get a Page. / SocialUs helps the customers you meet at the market find you the other six days of the week. There is no charge to create a Page. | Start a Page / Run a shop or a group? Get a Page. / SocialUs helps people find you any day of the week. | Uses "vendors" and "customers" (banned), and "no charge" is retired language. Proposes plain words; if this page is going away, retire it instead. **Legal:** Says "There is no charge to create a Page" twice. "No fee" language was retired by ruling (SocialUs takes transaction income). Counsel should confirm it is out. |
| 10.2 | `src/app/join/page.tsx:79` · /join three benefit cards | Followable between markets: Customers who love what you made on Saturday can find you on Wednesday. / No charge to create a Page / Local-first audience: People on SocialUs already want to spend locally. You're not marketing to strangers — you're being introduced. | Easy to follow: People who liked what you made on Saturday can find you again on Wednesday. / [Card removed.] / People who keep it local: People here already like keeping it local. You're not pitching strangers. You're getting introduced. | Drops the no-charge card and the em dash; "customers" becomes "people". **Legal:** Second "no charge" card. Same as above. |
| 10.3 | `src/app/join/page.tsx:97` · /join four "How it works" steps | Create an account: Email and password. Takes 10 seconds. / Tell customers who you are: Your name, a tagline, what you make, and which markets you attend. About 90 seconds. / Your profile goes live: You're immediately in the feed, the map, and searchable by product. / Customers follow you: They get updates when you'll be at an upcoming market. No more 'I forgot your name.' | Sign up: Use your email. It takes a minute. / Tell people who you are: Your name, a line about what you do, and where to find you. / Your Page goes live: People can find it on Explore and the map. / People follow you: They get your updates in the app. No more "what was that stall called?" | Removes "customers", timing claims, and the paused "feed"; keeps the friendly last line. |
| 10.4 | `src/app/join/page.tsx:110` · /join buttons and share box | Sign up as a vendor → / Start my Page → / Share with another vendor / Know someone at the market who should be on here? Send them this link. | Sign up and start a Page / Start my Page / Share this page / Know someone who should be on here? Send them this link. | "Vendor" is a banned person-category; arrows are decoration. |
| 10.5 | `components/create/WhatAreYouStarting.tsx:44` · Create: What are you starting? (error) | That didn't go through. Try again? | That didn't go through. Mind trying again? | Match the house error line. |
| 10.6 | `actions/group/activate.ts:102, 125, 133, 136, 149-161, 178` · Publishing a Page (error shown if a check fails) | group.activate: group ${id} needs the member's agreement to the current rules ... / requires at least one tag to publish / requires where it is / requires a description / requires name | Rules: "Agree to the rules first, then publish." Tag: "Add a tag, then publish." Place: "Add where it is, then publish." Description: "Add a description, then publish." Name: "Add a name, then publish." | These read as developer strings; if they reach the screen (via ActionError message into BeforeYouPublish/walkthrough), members see ids and code paths. Put friendly text in the thrown message or map by code. |
| 10.7 | `actions/group/activate.ts:75-93, 188` · Publishing a Page (rare errors) | group.activate: group ... not found / is in lifecycle_state ... / self-bootstrap acting member is not permitted / no longer in draft state ... | That didn't go through. Mind trying again? | Internal wording would surface as raw text if not mapped. |
| 10.8 | `components/create/BeforeYouPublish.tsx:43` · Before you publish checklist (error) | That didn't go through. Try again? | That didn't go through. Mind trying again? | Match the house error line. |
| 10.9 | `components/composer/MultiStepComposer.tsx:148` · Any step of a composer (error) | Something went wrong. | That didn't go through. Mind trying again? | Match the house error line. |
| 10.10 | `components/composer/AddEntityDrawer.tsx:127` · Add a place drawer (error) | Something went wrong. | That didn't go through. Mind trying again? | Match the house error line. |
| 10.11 | `components/composer/MultiStepComposer.tsx:83` · Composer dialog (screen reader label default) | Multi-step composer | Create something | Product-team wording as the fallback label. |
| 10.12 | `components/sell/AddProductButton.tsx:44 (and AddServiceButton.tsx 44)` · Pick-up place list in the product/service composer | ${groupName} (anchor) | ${groupName} | "anchor" is internal jargon. |
| 10.13 | `components/sell/SellCta.tsx:101` · Place list on You (untitled place) | Untitled Location | Untitled place | Capital-L Location is product vocabulary. |
| 10.14 | `components/sell/SellWalkthrough.tsx:248-249, 260, 335, 635, 678` · Create a Page: where is it step | Title "Anchor Location"; "Pick or add an anchor Location"; review "Anchor Location:"; "Anchor Location options"; "+ Add a new Location"; drawer "Add a Location" | Title "Where is it?"; error "Pick a place or add one"; review "Place:"; aria "Place options"; "+ Add a new place"; drawer "Add a place" | "Anchor" and capital Location are jargon; same fix in the product, service and gathering composers (Pickup Location options, Center Location options, Add a Location, + Add a new Location). |
| 10.15 | `components/sell/SellWalkthrough.tsx:219, 242, 278` · Create a Page validation | "Pick one to carry on"; "A name is required"; "Add at least one word that describes what you do" | "Pick one first."; "Add a name."; "Add at least one word for what you do." | Shorter, less formal. |
| 10.16 | `components/sell/SellWalkthrough.tsx:286` · Create a Page: About step | A short public description visitors will see (optional). | A short description anyone can read (optional). | "visitors" treats people as a category. |
| 10.17 | `components/sell/SellWalkthrough.tsx:332` · Create a Page: review | Brand: | Name: | "Brand" is corporate; the step above asks for a name. |
| 10.18 | `components/sell/SellWalkthrough.tsx:714 (and ProductComposer 424, ServiceComposer 461)` · Add a place drawer validation | Choose a neighbourhood | Choose a neighborhood | Sacramento spelling. |
| 10.19 | `components/sell/GatheringComposer.tsx:122` · Host a gathering: kind step | Drop in anytime — no fixed schedule. | Drop in anytime. No fixed schedule. | Em dash. |
| 10.20 | `components/sell/GatheringComposer.tsx:238` · Host a gathering: When step (open meetup) | Open meetups have no fixed schedule — people drop in whenever. You can add specific times later from the gathering page. | Open meetups have no fixed schedule. People drop in whenever. You can add times later from the gathering page. | Em dash. |
| 10.21 | `components/sell/GatheringComposer.tsx:311` · Host a gathering: When step | Cost (optional — leave blank if free) | Cost (optional, leave blank if free) | Em dash. |
| 10.22 | `components/sell/GatheringComposer.tsx:182, 217-219, 341, 345, 349` · Host a gathering validation | "Pick what kind of thing this is"; "Title is required"; "Description is required"; "Pick a date and time"; "The first occurrence must be in the future"; "The end time is before it starts" | "Pick which kind it is."; "Add a title."; "Add a description."; "Pick a date and time."; "Pick a time that's still ahead."; "The end time needs to come after the start." | Stiff "required/must"; "occurrence" is jargon. Same "Title is required / Description is required" lines in ProductComposer 198-200 and ServiceComposer 162-164. |
| 10.23 | `components/sell/GatheringComposer.tsx:383` · Host a gathering: review | (no venue) | (no place yet) | "venue" is out of voice. |
| 10.24 | `components/sell/ProductComposer.tsx:233` · Add a product: Where is this made? step | Claim Locally Made provenance for this product. You can skip this and add it later from the product page. | Say where it's made if you like. You can skip this and add it later from the product page. | "Claim" and "provenance" are product-team words. |
| 10.25 | `components/sell/ProductComposer.tsx:241-244` · Add a product: Where is this made? body | The Locally Made claim (a Place picker for where this product is made) ships with the provenance flow. Skip this step to publish without the badge — you can claim it later. | This part isn't ready yet. Skip it for now and you can add it later. | Dev-speak ("ships with"), em dash, promises a future feature. |
| 10.26 | `components/sell/ProductComposer.tsx:276-278` · Add a product: review | Locally Made: (claimed) / (skipped) | Locally Made: added / not yet | Parenthesised states read like code. |
| 10.27 | `components/sell/ProductComposer.tsx:202, 225` · Add a product validation | Enter a price, or mark it free; Pick or add a pickup point | Add a price, or mark it free.; Pick a pickup spot or add one. | Slightly softer, matches the rest. |
| 10.28 | `components/sell/ServiceComposer.tsx:138` · Add a service: title placeholder | Piano lessons — 30 min | Piano lessons, 30 min | Em dash. |
| 10.29 | `components/sell/ServiceComposer.tsx:289` · Add a service: review | ${modelLabel} — ${state.rateDollars \|\| '(set)'} | ${modelLabel}, ${state.rateDollars \|\| '(set)'} | Em dash. |
| 10.30 | `components/sell/ServiceComposer.tsx:247, 259-261, 292` · Add a service: Service area step | Where do you offer this? Pick a center point and how far you travel.; Pick or add a center point; Enter how far you travel (miles); Center: | Where do you offer this? Pick a starting place and how far you travel.; Pick a place or add one.; Add how far you travel, in miles.; Starting place: | "center point" is map jargon. |
| 10.31 | `components/sell/ServiceComposer.tsx:182` · Add a service: Pricing step | Pricing model | How you charge | "model" is product-team wording. |
| 10.32 | `app/g/[handle]/edit/actions.ts:52` · Error when saving an edit while signed out | You must be signed in. | Sign in and try again. | Stiff. |
| 10.33 | `app/g/[handle]/edit/actions.ts:96` · Error when an edit fails to save | That didn't save. Nothing on your Page changed — try again. | That didn't save. Nothing on your Page changed. Mind trying again? | Em dash. |
| 10.34 | `actions/group/update.ts:116-226 (201, 226, 178)` · Edit errors shown to a Page owner (passed through by editPageAction) | group.update: enter a US phone number, like (916) 555-0142 / group.update: a Page needs at least one tag / group.update: that picture didn’t come from your uploads | Enter a US phone number, like (916) 555-0142. / A Page needs at least one tag. / That picture didn’t come from your uploads. | Code prefix leaks to people; strip it from messages meant to be read (same in update-draft.ts line 202, lifecycle.ts line 108). |
| 10.35 | `actions/group/lifecycle.ts:108` · Error when typing the wrong name to delete a Page | group.delete: the name typed does not match the Page name | That doesn't match the Page name. Mind checking it? | Code prefix and stiff. |
| 10.36 | `components/group/edit/PageSettings.tsx:109` · Delete Page confirmation | ${name} and its posts disappear for everyone right away. You can restore it from You until ${date}. After that, it's gone for good. | ${name} and its posts disappear for everyone right away. You can restore it from You until ${date}. After that, it can't be restored. | Absolute ('for good'); also a hard promise about data deletion. **Legal:** Says deleted Pages are 'gone for good' after 14 days: a hard guarantee about data. Confirm retention matches before promising it. |
| 10.37 | `components/group/edit/EditCards.tsx:119-121` · Values & badges card on the Edit Page | Coming soon / Soon you'll be able to show what you're about and what you stand for. | Not here yet. / A place to show what you're about and what you stand for. | Promise about a future we can't back yet. |
| 10.38 | `components/locations/LocationPlaceFields.tsx:130, 135, 175, 188, 267, 323, 361, 369` · Address and neighborhood fields (British spelling) | neighbourhood / neighbourhoods | neighborhood / neighborhoods | Sacramento audience; American spelling (also AreaPickMap.tsx line 78 and WhereFields.tsx lines 181, 253, 258, 269). |
| 10.39 | `components/locations/WhereFields.tsx:269` · Visitor note under 'Show only my neighborhood' | Visitors see ${value.area.name}, with its pin at the centre, not your address. | Visitors see ${value.area.name}, with its pin at the center, not your address. | American spelling (also LocationPlaceFields.tsx line 361). |
| 10.40 | `components/locations/AreaPickMap.tsx:78` · Map prompt in the location picker | Or tap your neighbourhood on the map. / Or tap a town on the map. | Or tap your neighborhood on the map. / Or tap a town on the map. | American spelling. |
| 10.41 | `components/media/PagePhotoPicker.tsx:54-55` · Photo upload fails on a Page | That photo didn't upload — ${err.message}. You can try again, or carry on without one. | That photo didn't upload. ${err.message} Mind trying again? You can also go on without one. | Em dash and "carry on" (British). |


## 11. Operator screens (admin)

4 changes · reach T4

| # | Where | Current | Proposed | Why |
|---|---|---|---|---|
| 11.1 | `app/admin/builders/BuilderContentControls.tsx:62, 63, 25, 32` · Operator builder-content screen | Every Page, Post, follow and membership the builder accounts made. Member-made content is never touched. Permanent. | Member-made content is left alone. This can't be undone. | Absolute "never" and "content"; staff only. |
| 11.2 | `app/admin/reports/ReportEntry.tsx:201, 224, 67` · Operator report review | Undo the ${x} — why? / Approve — why? / Reject — why? / That did not go through. | Undo the ${x}. Why? / Approve. Why? / Reject. Why? / That didn't go through. | Em dashes; low reach. |
| 11.3 | `app/admin/reports/ReviewQueue.tsx:84, 106, 362` · Operator review queue | That didn't go through. Try again? / AI: ... — ${reason} | That didn't go through. Mind trying again? / drop the em dash before the reason | Match house error line; low reach. |
| 11.4 | `app/admin/reports/PurgeList.tsx, app/admin/tags/TagReviewList.tsx:53, 34` · Operator purge and tag review | Something went wrong. / That did not save. Try again? | That didn't go through. Mind trying again? / That didn't save. Mind trying again? | House error line; low reach. |


## 12. Outside the repo

1 changes · reach T1

**12.1.** `Supabase dashboard (not in the repo)` · Sign-in email (magic link) and the text-message code · *T1*
- Now: [Not visible: the template lives in the Supabase dashboard, outside version control. voice-and-tone.md has the sample.]
- Change to: Subject: Here's your way in. / Body: Tap below to get back in. No password needed. / Button: Continue
- Why: It is the only email the app sends and nobody on the team can read it in review. The voice guide's sample already fits the new voice, so use it. Move the template into the repo (supabase/templates) so it is reviewed like the rest.


## Retired or paused surfaces (no rewrite proposed)

Still in the code, but not reachable or not maintained. They break the voice rules (vendor, customer, no-charge language). Retire them rather than rewriting.

| Where | What is wrong |
|---|---|
| `app/following/page.tsx:90, 95, 113, 107` · Old Following page (retired vendor model, still routed from You tab highlight) | Uses 'vendors' and market framing; says sign up on a sign-in link. |
| `components/EventCard.tsx:18` · Event card badge | People-category word 'Vendor'; component is unreferenced. |
| `lib/types.ts:206, 218, 228 (OWNERSHIP_TIERS)` · Ownership tier labels (unreferenced outside types.ts) | Uses 'workers' and competitor/monopoly framing; money-leaving-town implies economic claims. Dead code, delete rather than reword. |
| `components/RecruitmentGrid.tsx:15-72, 133, 165` · Home feed 'open spots' grid (paused Home feed) | People-category 'makers' and em dashes. Cheap to fix only if the feed returns. |
| `components/RecruitmentGrid.tsx:153, 166` · Home feed 'open spots' grid (paused Home feed) | 'No fee' language is retired and 'no charge' is an absolute. **Legal:** 'No charge to create a Page' reads as a no-fee promise; SocialUs takes transaction income and 'no fee' language is retired. |
| `components/feed/FeedEmptyState.tsx:15, 16, 28, h3` · Retired locality feed with nothing in it | "Near you", "nearby". Home `/` now redirects to Explore, so this is unreachable. |
| `components/feed/LocalityFeed.tsx:52, 80` · Retired locality feed header and fallback | "Nearby", "near", "locality" jargon. Unreachable. |
| `components/feed/MakeThisYoursBanner.tsx:13-15` · Retired sign-in banner on the feed | "Locality" jargon. Unreachable. |
| `components/feed/ScopePicker.tsx:26` · Retired area picker | Jargon in aria-label. Unreachable. |

## What this report did not cover

- **Emails and texts.** The sign-in email and the text-message code are Supabase dashboard templates, outside the repo, so nobody can review them. See the last section above for the proposed wording and the suggestion to move the template into `supabase/templates`.
- **Words held in the database.** Category names, tag lists, seed data and everything members write live outside the code and were not read.
- **Dev-only routes** (`app/(dev)`) and **internal strings** in `src/ontology` were left out on purpose. Admin screens are included at low priority.
- **Counts are approximate.** A script found about 2,300 candidate strings (about 1,500 after dropping code); four reviewers then read each file. The "reviewed" and "flagged" figures above are their tallies of distinct user-facing strings. `docs/copy-inventory.md` in `socialus-web` is the older Sept 15 inventory (584 strings) and is out of date.
- **Strings left alone on purpose.** 8 spots were judged already fine, developer-only, or part of a retired surface, and have no proposal.
