---
id: F076
title: A person outside an open market joins its waitlist
status: approved
horizon: now
rank: 90
gates: launch
date: 2026-09-14
concept: CO-0002
depends: [F059]
approved: 2026-09-14 — Don's ruling; threshold 50 creators / 250 patrons, gated on creators, shown as one combined 300
amended: 2026-11-12 — the waitlist join asks role and zip, and every market waits while SocialUs stays closed (3, 17); a waiting member is told by email only if they leave one. Earlier amendments: git log.
---
## Story

Someone in Boise signs up; their zip puts them in a market not open yet, so they join its waitlist. A popup shows where Boise stands: a number, and what is still needed. When Boise opens, it opens because enough people did this.

## Acceptance

1. Every US zip resolves to a market, open or waiting (F103). Nothing is picked from a list.
2. The zip decides which waitlist; the platform **never selects for them** (no IP, default, nearest match or shortlist).
3. **The waitlist join asks one question per screen, explaining SocialUs along the way:** what the person plans to do (multi-select: discover local businesses, groups and events; be found for a business, a class, a meetup), with being-found answers branching to a few detail screens; a name (never a legal name); a zip; a mobile number. Answers are staff-only, counted per market, and never stored as a type on a member. Storyboard: `planning/briefs/waitlist-join-journey-2026-11-12.md`.
4. **One person counts once in one market;** re-joining, re-visiting or a second device adds nothing.
5. Changing the zip moves the count to the new market, never doubled or stranded.
6. **Creator and patron counts are stored separately** per metro, and both are readable independently of what is displayed.
7. After joining, a **popup** shows a count and a message. Not a page, not a tab, not a new surface. **Everyone sees a count, anonymous submitter included** — it is the CACHED figure, never one read in response to the submission.
8. The popup shows **one combined number**, makers plus supporters, the same figure everywhere; the split never shows.
9. The message states what is still needed. **It never states or implies a date, a timeline, or a promise that the metro will open.**
10. A market is eligible to open only when **both** floors are met (F118: 100 makers, 1,000 supporters).
11. The thresholds are **configurable per metro** without a migration or a deploy.
12. Opening a metro is a deliberate act. **Crossing the threshold never opens a metro on its own.**
13. **Joining the waitlist creates no account and no password.**
14. **The response is identical whether or not that person was already on the list:** same words, status and number, because the number is the cached figure (criterion 7), not a function of the submission.
15. **The contact left is used to say the market opened, and for nothing else;** it is discarded once that invite is sent.
17. **While the PM keeps SocialUs closed, every zip joins a waitlist,** Sacramento included; reading stays open (F134).
[open-question owner=don raised=2026-11-12] How is the waitlist's mobile number handled: (A, recommended) verified by a texted code at join; (B) collected now and verified when the invite is accepted; (C) collected now, with invites by email only? Options and costs in the brief.

## Why

### The threshold

**Creators are the real gate:** a market full of patrons and empty of makers teaches a newcomer that SocialUs is empty. The member sees one combined number; the split is how the platform decides. Thresholds are per market and expected to move (F118 sets 100 and 1,000); criterion 9 keeps any number from becoming a promise of a date.

### Leaving an email, and the count

A live count would leak whether an address was already waiting, by differencing (found 2026-09-22 against Postgres). So the count is cached, at most an hour old and shared everywhere, and not a function of the submission (2026-09-23).

## Not this

A waitlist surface, a progress bar, a leaderboard, or a referral mechanic. Ranking or displaying who joined. Any use of a left address other than the one message criterion 15 permits. Opening a metro automatically. Charging for a place in line, or selling one.

## Rulings
- **2026-11-12 — A member who signs up by mobile number in a waiting market is told it opened by email, and only if they leave one on the waiting screen (optional, one field, criterion 15's single use). We send no "it opened" text.** Sign-up is by mobile number now (F081, 2026-11-12) and Twilio Verify sends only sign-in codes, so a text would need a number of our own. Path: well-worn. [for now] [replaces none] [binds tiers=planning,code surfaces=waitlist,signup]
- **2026-11-12 — The waitlist collects a mobile number, a name (a first or display name, never a legal name), a zip and what the person plans to do, one question per screen, explaining SocialUs along the way. Plans are multi-select on two sides: discover (local businesses, groups, events) and be found (a business, a class, a meetup), and being-found answers branch into details about what they do. SocialUs stays closed, every zip waiting, until the PM opens a market; zip counts help decide where to launch.** The PM: *"I need a nice simple way for people to say what they're interested in a format that allows them to answer one question at a time and walk though some screens. The goal is to get a phone number and a name (don't ask for a legal name), a zip code and then what they plan on doing in the app. since nobody knows what the app is for or has little idea we need to somewhat inform them along the way. I want to discover, local businesses, groups, events... I have a business, teach a class, organize a meetup and want people to find me... Then ask the details about what they do etc."* Answers live on the waitlist entry, never as a type on the member (2026-09-14). Path: new territory (how the number is checked is the PM's pick). [for now] [replaces F076: The waitlist join asks a role (runs a business, store, shop, market or group; or looking for those) and a zip] [replaces 2026-11-12: Whether a person outside an open market is asked if they make or support is reopened, for the end-to-end design of the sign-up journey] [binds tiers=planning,code surfaces=waitlist,landing,signup build=none]
- **2026-10-25 — The "market opened" email stays, for the landing list (criteria 13–15 stand); a person opens a market with `scripts/market/open-market.ts`, which sends "SocialUs is open in {town or market}. See what's going on." and then discards each address it reached.** The PM, 2026-10-11, on `socialus-web` #616 (Resend, those words); rebuilt on markets 2026-10-25. It sends through the reminders' Resend sender: the key is set, `FOLLOW_EMAIL_FROM` (a verified sending domain) is not. [for now] [binds tiers=planning,code surfaces=waitlist,email,copy] Issue: #616.
- **2026-09-23 — The waitlist count comes back, CACHED rather than live, and metros sort by it.** *(#216, built in `socialus-web` #217)*. Don: *"how would anyone know about anybody elses emails with just a count? that seems a bit too over the top for privacy. Nobody would be able to know anything else except someone else somewhere else also found this site. they could have even chosen the wrong area. also it would be cool to sort those metros by number of people signed up."* **The oracle is real and the stakes are small** — what it discloses is *this address expressed interest in a local app before launch*, which does not justify removing something useful. **The fix depends on the mechanism:** the leak was never the number existing, it was the number being **recomputed and re-displayed in response to your own write**. Read it before the write and two submissions differ; read it after and a single probe differs — either way the figure is a function of what the reader just did. **A cached figure is not**, so criterion 14 is met by the number not moving rather than by there being no number. **One read serves every surface** — the popup and the picker's ordering — because a fresher number anywhere reopens what the cache closes, and **a sorted list is the strictest case since it exposes every metro at once**. **What the cache does not close, ruled acceptable and written down so nobody re-derives it as new:** after the window expires the figure refreshes, so in a metro where nothing else happened inside that window a person who submitted and waited could see it move by one and attribute that to themselves. No window length removes it — longer is rarer and staler, shorter is fresher and more attributable — and it is weakest where there is real demand and strongest in an empty metro, which is where the answer is least interesting. **F076 criteria 7, 8 and 14 are restated and criterion 16 is added.** **No migration:** `metro_polygons.creator_count`/`patron_count` are already maintained by the join handlers, so this is one cached read of two columns and the schema does not move. [for now] [binds tiers=code surfaces=waitlist] [replaces 2026-09-22: A live count cannot satisfy F076 criterion 14] [replaces 2026-09-21: same words, same status, same count]
- **2026-09-21 — Someone who picks a metro that is not open may leave an email to be told when it opens, without signing up.** Don's ruling, answering the open question `MetroNotCoveredPanel` already carried in a comment. It is F076 criteria 13-15. **The real change is to criterion 4's enforcement:** idempotency was carried by `member_id unique` and an anonymous entry has no member, so the key becomes the normalised email per metro. **That is a privacy consequence and not a constraint swap — a unique key on an address makes *is this address on the list* answerable by anyone who can reach the endpoint.** **The mitigation is stated rather than implied: the response must be identical either way** — same words, same status. **Hashing is not the answer here**: the address must be readable to send the one message permitted, so it is stored as an address. **The single permitted use is that one message**, after which it is discarded. [binds tiers=code surfaces=waitlist] [replaces F076: ~~Notifying people when a metro opens~~]
