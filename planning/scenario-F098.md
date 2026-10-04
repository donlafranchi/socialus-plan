---
id: F098
title: Home is rows that keep going, and an honest place to stop
status: draft
date: 2026-10-04
depends: [F059, F091, F093]
---
## Story

Sam opens SocialUs on a Friday evening with nothing planned. Home shows a row headed *Tonight*: a bluegrass set at a brewery, a group ride leaving the levee at seven. She swipes sideways for more, then scrolls down: *This weekend*, *New this week*, and a row of things she'd never have picked, a pottery open studio and a seed swap. No organization shows up twice in a row, and nothing moves until she touches it. A few rows later a card says *You've seen what's new this week*, and under it, *the ride you said you're going to is on tonight*. She taps it and gets the map. Below the card, a button offers older picks; nothing loads unless she asks.

## Acceptance

1. **Home at `/` shows rows in this order: Tonight, This weekend, New this week, then a wildcard row.** A row with nothing in it is absent. Every row is scoped to the active metro.
2. **Rows hold posts and Pages, and each row and card says what kind of thing it is** at the granularity the open question below settles. A business's sale and a group's ride don't share an unlabelled bucket.
3. **No organization appears in two adjacent cards of a row, or first in two consecutive rows.**
4. **Ordering uses time, place, the member's declared interests, curation and community response, and nothing else.** No input measures time spent, dwell, scroll depth or opens.
5. **Nothing plays, advances or opens on its own.** Cards open on a tap; rows arrive a few at a time as the member scrolls.
6. **When the new rows run out, a stop card reads "You've seen what's new this week".** Signed in, with things of theirs on tonight, it adds "things you saved are on tonight" and links to each; with none, that line is absent.
7. **Below the stop card, older picks appear only after a tap.** Nothing refills on its own.
8. **Each row's "Show all" opens Explore narrowed to that row's window or category.**
9. **The wildcard row draws from outside the member's declared interests**; signed out, from the whole metro.
10. **Signed out, Home follows F093:** withheld announcements show as its "Sign up to see what's happening" card, and the stop card's second line is absent.

## Not this

A vertical one-card-at-a-time feed. Ranking on behaviour read back at the member. Autoplay, streaks, pull-back notifications or break timers. A daily deck. Follower or going counts on cards. Distance readouts. Notifications of any kind; those are a separate scenario.

## Why

**New launch scope, 2026-10-04.** Don chose option B in `socialus-design/research/ENGAGEMENT-OPTIONS.md`: engaging, with stops where the research says they work, at a real end that turns into going somewhere. The windows reuse F091's *today / this week / this weekend*, computed the same way.

[open-question owner=don raised=2026-10-04] How granular are Home's row categories, so businesses and group events read as different things?
A) **Kind, then category (recommended):** label each row and card by Page kind (business, group, organization) and post kind (event or post), and theme rows on the categories Pages already declare at creation, e.g. *Group rides this weekend*, *Live music at local businesses tonight*. Uses data the composer collects; no new taxonomy to build or police.
B) A fixed category tree every Page picks from (~40 leaves, Yelp-style). More precise; new build, and a second vocabulary beside the tags.
C) Broad buckets (Events, Businesses, Groups). Cheapest; Don has ruled it out.

[open-question owner=don raised=2026-10-04] What does "things you saved" mean at launch? There is no save today.
A) **Events the member has responded to, via the launch RSVP (recommended).** No new verb. B) A heart on every card. New verb, new table, more scope. C) Posts from followed Pages. Follows aren't intent to go.

[open-question owner=don raised=2026-10-04] Do F091's time rows stay on Explore once Home carries them?
A) **Move them to Home (recommended):** Explore becomes the tool, list and map, as option B says. B) Both. Two surfaces answer one question.

Measure from launch: share of visits reaching the stop card, taps after it, return at 7 and 30 days; session length as a ceiling, not a goal (`product/foundation/metrics.md`). Counsel should confirm before launch that ranking on declared interests keeps Home outside California's SB 976 addictive-feed definition. [platform none]
