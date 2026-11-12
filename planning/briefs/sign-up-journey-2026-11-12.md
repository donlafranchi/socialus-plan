---
id: brief-2026-11-12-sign-up-journey
status: awaiting-approval
size: M
path: new territory
criteria:
  - A person goes from the landing page or a shared link to their first useful screen on a 390px phone in no more than eight screens, every one in terracotta and the Aime font.
  - The question of whether someone makes, sells, organizes or teaches, or finds and supports, is asked once, after the phone check, never on the sign-up form and never on the waiting screen.
  - Each answer leads to a different first screen; "just look around" is always offered and is never a lesser path.
  - No role, answer or person type is stored on the member; maker and supporter counts come from what people do (a Page started or claimed; a verified member in the market).
  - A member can take the other path at any time from You, with nothing to undo.
  - No supporter is findable or trackable by anyone outside, signed in or out; a Page owner chooses which contact details show while starting or claiming the Page.
---

# The sign-up journey, end to end

**As of 2026-11-12** · Source: F081, F076, F118, F085, F134, the 2026-11-12 rulings, the product analytics brief (2026-11-11), the screenshots on socialus-web branch `landing-signup-pass-screenshots` (live socialus.org and local, 390px) · Maintained by: hand (brief; deleted at 30 days or once ruled and placed)

*The PM, 2026-11-12:* "As far as the make or support question from sign-up, I want that to be part of the focus for how we design this sign up journey. It needs to be more fully designed end to end."

**Bottom line: ask the make-or-support question once, right after the phone check, as two doors and a "just look around" link; let the door choose the first screen and store nothing, and count makers and supporters from what they do.**

## What is true today (from the screenshots)

- The front page is terracotta and Aime; every sign-up screen after it is navy and a system font, and the first one says "Sign in to SocialUs".
- The sign-up form asks legal name, display name, zip and the 18+ box, under the older placeholder paragraph, not the ruled line.
- The waiting screen still asks "Are you here mainly to make, sell or organize, or find and support them", which the 2026-11-12 ruling removes.
- After the phone check comes "What are you into?" (interests), then Explore; nothing ever points a maker toward a Page.

## Rulings this design must hold

- Sign-up carries the front page's look; its line is "Locals, finding and supporting locals." (2026-11-12).
- The sign-up form and the waiting screen ask nothing about making or finding (2026-11-12). This brief asks after sign-up is done, so it holds; if the PM meant "never in the journey at all", option C is the one that fits.
- One kind of member; "patron" is never stored; being a creator comes from a later step plus what the member made (2026-09-14, always).
- Visitors read everything; writes ask for sign-in first and finish after (F134).
- Privacy (the PM, 2026-11-12): Page owners decide which contact details show; patrons are never findable or trackable by outsiders, signed in or out.
- Headline pending: "SocialUs, for the people" (word being chosen), with "A place for locals to find and support locals, wherever you are, wherever you go" under it. It sits on the landing page; the sign-up line stays the ruled one.

## The journey, screen by screen (option A, 390px)

**0. Arrive.** Two doors in. The landing page's "Join SocialUs", or a shared link that opens a post or Page readable signed out (F134). A tap on heart, follow or going opens a sheet: "Join to save this. It takes a minute." The tap completes after sign-up.

```
+----------------------------------+
| SocialUs              [ Join ]   |
|                                  |
|   SocialUs, for the people       |
|   A place for locals to find     |
|   and support locals, wherever   |
|   you are, wherever you go       |
|                                  |
|        [ Join SocialUs ]         |
|        ( Look around first )     |
+----------------------------------+
```

**1. Email.** One screen for new and returning people; the title says Join, not Sign in.

```
+----------------------------------+
|            SocialUs              |
|  Join SocialUs                   |
|  Locals, finding and supporting  |
|  locals.                         |
|  Email  [ you@example.com     ]  |
|        [ Email me a code ]       |
|  Already a member? Same box.     |
+----------------------------------+
```

**2. Email code.** Six boxes, paste-friendly, "Send it again" after 30 seconds. A returning member goes straight to where they were.

**3. Who you are.** Legal name (only our team sees it), display name (what neighbours see), zip, the 18+ box. As the zip is typed, one line under it names the market: "You're in Northern California." An unknown zip gets "We don't recognize that zip, try again."

```
+----------------------------------+
|  Tell us who you are             |
|  Legal name   [             ]    |
|   Only our team sees this.       |
|  Display name [             ]    |
|   What your neighbours see.      |
|  Zip          [ 95816       ]    |
|   You're in Northern California. |
|  [ ] I'm 18 or older and agree   |
|      to the Terms                |
|          [ Continue ]            |
+----------------------------------+
```

**3b. Waiting screen (zip outside an open market).** The journey ends here, kindly. One number, no question, no date.

```
+----------------------------------+
|  We're not open in Portland yet  |
|  {count} people there are waiting.|
|  We'll email you when it opens,  |
|  and for nothing else.           |
|  Meanwhile, look around:         |
|     [ See what's on near us ]    |
+----------------------------------+
```

**4. Phone check.** "Everyone here is a real person. We'll text you a code. Your number is never shown to anyone." A non-mobile internet number gets a one-line ask for a mobile number.

**5. Phone code.** Six boxes; then straight on.

**6. What brings you here?** The question, asked once, here. Neither door is pre-selected. A small link under both skips it.

```
+----------------------------------+
|  Welcome, Maya.                  |
|  What brings you here?           |
| +------------------------------+ |
| | I make, sell, organize       | |
| | or teach                     | |
| | A business, maker, group,    | |
| | class or event               | |
| +------------------------------+ |
| +------------------------------+ |
| | I'm here to find and support | |
| | locals, and show up          | |
| +------------------------------+ |
|      Just look around for now    |
+----------------------------------+
```

**7a. Maker door: "Is your Page already here?"** One search box by name. A match offers "This is mine, claim it"; no match offers "Start your Page". Starting or claiming asks which contact details show (phone, email, site, socials, exact place or neighbourhood), each off until the owner turns it on.

```
+----------------------------------+
|  Is your Page already here?      |
|  [ Search your business name ]   |
|  > Plant Foundry, Midtown        |
|      [ This is mine, claim it ]  |
|  Not here?  [ Start your Page ]  |
|  You choose what contact info    |
|  shows. Nothing shows until you  |
|  turn it on.                     |
+----------------------------------+
```

**8a. Maker's first useful screen: their own Page,** with one prompt: "Post what's on this week." Followers count toward nothing they must chase.

**7b. Supporter door: "What are you into?"** Today's interests screen, kept, skippable. Only the member sees these.

**8b. Supporter's first useful screen: Explore, this week near them,** led by what matches their interests, with Follow and Going on every card. A line at the top: "Follow a few places and their news comes to you." Following and going show to a Page as counts, never as names to outsiders, and the member has no page anyone outside can find.

**Look around:** goes to Explore with no interests set; both doors stay on You.

**Changing it later.** Nothing was stored, so there is nothing to change. You always shows "Start or claim a Page" and "What you're into". A supporter who starts a Page becomes a maker by doing it; a maker who only follows things is a supporter too.

## How it feeds the open-your-town counts

- **Makers (creators):** a member in the market who started or claimed a Page. That is F118's own definition and the 2026-09-14 rule; a door tap is intent, not a count.
- **Supporters (patrons):** every phone-verified member whose zip is in the market.
- **Live gate (waitlist):** 50 creators and 250 patrons per market, shown as one number. **Dormant (open your town, behind a flag):** 100 makers and 1,000 supporters, two bars; same definitions, so nothing changes when the flag comes on.
- **Gap to know about:** in a waiting market, the 2026-11-12 ruling leaves only one number, so the 50 creator floor cannot be read there until people can start or claim a Page before their market opens. That is open-your-town work, not this journey.

## Precedents: the "which side are you" question

- **Etsy** ([sell on Etsy](https://www.etsy.com/sell)): one account for everyone; selling is a separate "open your shop" step any buyer can take later. Never asked at sign-up.
- **Airbnb** ([host your home](https://www.airbnb.com/host/homes)): one account; hosting is a separate flow and a switch in the menu. Guest is the default; nobody is asked.
- **Meetup** ([start a group](https://www.meetup.com/start/)): member sign-up asks interests; organizing is a separate "start a group" path, paid. Interests at sign-up, role later.
- **Nextdoor** ([business pages](https://business.nextdoor.com/)): neighbours verify an address; businesses claim a page in a separate flow. Two front doors.
- What they share: one account, the selling side is an action, not a type. None makes the person pick a side to get in. Option A keeps that and adds a fork that only routes.

## Options

- **A. Ask after the phone check, store nothing (recommended):** two doors and "just look around" pick the first screen; counts come from Pages started or claimed and verified members. Keeps every ruling, gives makers a path they lack today; one new screen.
- **B. Ask on the sign-up form and keep the answer:** the answer is a field on the member, counts read it, You lets them change it. Simplest counts; overturns the 2026-11-12 "no make-or-find question in sign-up" ruling and the 2026-09-14 never-stored rule, and self-reported makers inflate the creator count.
- **C. Never ask; infer from what they do:** everyone lands on interests then Explore; "Start or claim a Page" sits in the plus menu and on You. No new screen, no ruling touched; makers have to find their own way, which is the gap today.

## Calls that come with A

- **Words:** the two door labels and "just look around" are drafts for the PM.
- **Build freeze:** the fork and the "Is your Page already here?" screen are new screens; they need his yes as launch preparation. Applying the ruled look and line to screens 1 to 5 and removing the question from the waiting screen are already ruled and can go now.

**How A would be measured:** counts only, no member id beside them (the analytics brief, option A): how many people reach each screen from 1 to 8 and where they stop; the share taking each door and "look around"; of the maker door, how many start or claim a Page within 7 days; of the supporter door, how many follow a Page or tap Going in the first session and come back within 14 days.
