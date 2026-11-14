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
amended: 2026-11-13 — the join journey brief approved; Join on the front page goes to the waitlist. Earlier amendments: git log.
---
## Story

Someone in Boise joins the waitlist and sees a number. Boise opens when enough have.

## Acceptance

1. Every US zip resolves to a market, open or waiting (F103). Nothing is picked from a list.
2. The zip decides which waitlist; **never IP, a default, nearest match or a shortlist.**
3. **The waitlist join is four or five screens:** plans (multi-select), a business page only for be-found picks, then name (never legal), zip, email, mobile on one page. Staff-only, counted per market, never a member type. Storyboard: the join-journey brief.
4. **One person counts once in one market;** re-joining or a second device adds nothing.
5. Changing the zip moves the count to the new market, never doubled or stranded.
6. **Creator and patron counts are stored separately** per market.
7. After joining, the finish shows the **cached** count and a message, never a figure read in response to the submission.
8. **One combined number**, makers plus supporters, the same everywhere; the split never shows.
9. The message says what is still needed, **never a date, a timeline or a promise to open.**
10. A market is eligible to open only when **both** floors are met (F118: 100 makers, 1,000 supporters).
11. Thresholds are **per market**, changed without a deploy.
12. **Crossing a threshold never opens a market on its own;** a person opens it.
13. **Joining the waitlist creates no account and no password.**
14. **The response is identical whether or not that person was already on the list:** same words, status and number (the cached figure, 7).
15. **The contact left is used to say the market opened, and for nothing else;** it is discarded once that invite is sent.
17. **While the PM keeps SocialUs closed, every zip joins a waitlist,** Sacramento included; reading stays open (F134).
18. **Email and mobile are asked, neither checked at join** (no Lookup, no code); the contact page says why ([public-is-draft]); the invite is by email; checks at sign-up (F081).

## Why

**Creators are the real gate:** patrons without makers look empty. One number, cached (2026-09-23).

## Not this

A progress bar, leaderboard or referral mechanic. Showing who joined. Other use of the contact (15). Auto-opening a market. Selling a place in line.

## Rulings
- **2026-11-14 — The waitlist join journey is four or five screens: plans, a business page only for be-found picks, one contact page (name, zip, email, mobile last), the finish. Same data saved.** The PM: *"We can just ask all the business questions and the contact questions each on their own separate page."* [for now] [replaces 2026-11-13: The waitlist join journey is built as its brief's storyboard: one question per screen, Back everywhere, Skip on optional screens, a fast-then-slow segmented bar, each screen at its own address, builders-only until the PM walks it live] [binds tiers=planning,code surfaces=waitlist build=none]
- **2026-11-12 — No Google or Apple sign-in at the waitlist: the person types an email, a zip and a phone number, and nothing is created.** The PM: *"Ok, so we leave out the Auth until later."*: at the waitlist it would only save typing an email. Path: well-worn. [for now] [replaces none] [binds tiers=planning,code surfaces=waitlist,sign-in build=none]
- **2026-11-12 — The waitlist collects an email and a mobile number and checks neither at join: no Twilio Lookup, no texted code, no Twilio cost per join. The phone screen explains why we ask (it keeps out bots and spam; only real cell numbers, not internet numbers). The invite goes by email (Resend) when the market opens; Lookup and the code happen at sign-up. Counts padded by fake entries are accepted for now.** The PM: *"I don't want to spend 7 cents until the person is ready to join. … I don't care about padded numbers yet."* No cost until a person is ready to join; the check that matters runs at sign-up. Path: new territory (the PM's pick; option B of the brief, with an email for the invite). [for now] [replaces 2026-11-12: A member who signs up by mobile number in a waiting market is told it opened by email, and only if they leave one on the waiting screen] [binds tiers=planning,code surfaces=waitlist,signup,email build=none]
- **2026-11-12 — The waitlist collects a mobile number, a name (a first or display name, never a legal name), a zip and what the person plans to do, one question per screen, explaining SocialUs along the way. Plans are multi-select on two sides: discover (local businesses, groups, events) and be found (a business, a class, a meetup), and being-found answers branch into details about what they do. SocialUs stays closed, every zip waiting, until the PM opens a market; zip counts help decide where to launch.** The PM: *"…answer one question at a time and walk though some screens. The goal is to get a phone number and a name (don't ask for a legal name), a zip code and then what they plan on doing in the app. … we need to somewhat inform them along the way."* Answers live on the waitlist entry, never as a type on the member (2026-09-14). Path: new territory (how the number is checked is the PM's pick). [for now] [replaces F076: The waitlist join asks a role (runs a business, store, shop, market or group; or looking for those) and a zip] [replaces 2026-11-12: Whether a person outside an open market is asked if they make or support is reopened, for the end-to-end design of the sign-up journey] [binds tiers=planning,code surfaces=waitlist,landing,signup build=none]
- **2026-10-25 — The "market opened" email stays, for the landing list (criteria 13–15 stand); a person opens a market with `scripts/market/open-market.ts`, which sends "SocialUs is open in {town or market}. See what's going on." and then discards each address it reached.** The PM on #616 (Resend, those words); rebuilt on markets 2026-10-25. [for now] [binds tiers=planning,code surfaces=waitlist,email,copy] Issue: #616.
- **2026-09-23 — The waitlist count comes back, CACHED rather than live, and metros sort by it.** *(#216, built in `socialus-web` #217)*. Don: *"how would anyone know about anybody elses emails with just a count? that seems a bit too over the top for privacy. Nobody would be able to know anything else except someone else somewhere else also found this site. they could have even chosen the wrong area. also it would be cool to sort those metros by number of people signed up."* **The oracle is real and the stakes are small** — what it discloses is *this address expressed interest in a local app before launch*, which does not justify removing something useful. **The fix depends on the mechanism:** the leak was never the number existing, it was the number being **recomputed and re-displayed in response to your own write**. Read it before the write and two submissions differ; read it after and a single probe differs — either way the figure is a function of what the reader just did. **A cached figure is not**, so criterion 14 is met by the number not moving rather than by there being no number. **One read serves every surface** — the popup and the picker's ordering — because a fresher number anywhere reopens what the cache closes, and **a sorted list is the strictest case since it exposes every metro at once**. **What the cache does not close, ruled acceptable and written down so nobody re-derives it as new:** after the window expires the figure refreshes, so in a metro where nothing else happened inside that window a person who submitted and waited could see it move by one and attribute that to themselves. No window length removes it — longer is rarer and staler, shorter is fresher and more attributable — and it is weakest where there is real demand and strongest in an empty metro, which is where the answer is least interesting. **F076 criteria 7, 8 and 14 are restated and criterion 16 is added.** **No migration:** `metro_polygons.creator_count`/`patron_count` are already maintained by the join handlers, so this is one cached read of two columns and the schema does not move. [for now] [binds tiers=code surfaces=waitlist] [replaces 2026-09-22: A live count cannot satisfy F076 criterion 14] [replaces 2026-09-21: same words, same status, same count]
- **2026-09-21 — Someone who picks a metro that is not open may leave an email to be told when it opens, without signing up.** Don's ruling, answering the open question `MetroNotCoveredPanel` already carried in a comment. It is F076 criteria 13-15. **The real change is to criterion 4's enforcement:** idempotency was carried by `member_id unique` and an anonymous entry has no member, so the key becomes the normalised email per metro. **That is a privacy consequence and not a constraint swap — a unique key on an address makes *is this address on the list* answerable by anyone who can reach the endpoint.** **The mitigation is stated rather than implied: the response must be identical either way** — same words, same status. **Hashing is not the answer here**: the address must be readable to send the one message permitted, so it is stored as an address. **The single permitted use is that one message**, after which it is discarded. [binds tiers=code surfaces=waitlist] [replaces F076: ~~Notifying people when a metro opens~~]
