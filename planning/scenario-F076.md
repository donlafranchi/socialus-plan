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
amended: 2026-11-12 — sign-up by mobile number: a waiting member is told by email only if they leave one; criterion 3 reopened. Earlier amendments: git log.
---
## Story

Someone in Boise signs up; their zip puts them in a market not open yet, so they join its waitlist. A popup shows where Boise stands: a number, and what is still needed. When Boise opens, it opens because enough people did this.

## Acceptance

1. Every US zip resolves to a market before launch (F103 criterion 2): every county is in an open market or a waiting one, so a person cannot reach a state with no market. Nothing is selected from a list.
2. A person whose zip is in a waiting market joins that market's waitlist; the zip decides which (F103 criterion 3). The platform **never selects for them**: no IP-derived market, no pre-filled default, no nearest match, no shortlist. A market derived from the person's own zip is not a selection made for them.
3. **Open:** whether the waitlist entry asks if the person makes or supports waits on the sign-up journey design (2026-11-12).
4. Joining is idempotent: **one person counts once in one metro, whether they signed up or only left an email.** Re-signup, re-visit or a second device does not increment anything.
5. Changing the selected metro moves that person's count from the old metro to the new one, leaving neither double-counted nor stranded.
6. **Creator and patron counts are stored separately** per metro, and both are readable independently of what is displayed.
7. After joining, a **popup** shows a count and a message. Not a page, not a tab, not a new surface. **Everyone sees a count, anonymous submitter included** — it is the CACHED figure, never one read in response to the submission.
8. The popup shows **one combined number** — creators plus patrons, against 300. The 50/250 split does not appear in it. **The same figure the metro picker orders by**, and the same figure everywhere: a second, fresher number on any surface reopens what criterion 14 closes.
9. The message states what is still needed. **It never states or implies a date, a timeline, or a promise that the metro will open.**
10. A metro is eligible to open only when it has **at least 50 creators and at least 250 patrons**. Meeting the combined 300 with fewer than 50 creators does not make it eligible.
11. The thresholds are **configurable per metro** without a migration or a deploy.
12. Opening a metro is a deliberate act. **Crossing the threshold never opens a metro on its own.**
13. **A person who picks a metro that is not open can leave an email address to be told when it opens, without creating an account.** No password, no name, no second step. Signing up stays available and is not the price of being told.
14. **The response is identical whether or not that address was already on the list** — same words, same status, **and the same number**. A person who submits twice cannot tell that they had already submitted, and neither can anyone else. **This is met by the number not being a function of the submission**, not by there being no number: the count shown is a cached figure, at most an hour old, shared with the metro picker's ordering, and a submission does not move it.
15. **An address left this way is used to say that the metro opened, and for nothing else.** Not marketing, not a newsletter, not a second message about something else. It is discarded when the metro opens and the message has been sent.
16. ~~Metros are ordered by how many people are waiting.~~ *Struck 2026-10-11: there is no list of markets to order, since the zip decides. The cached figure shows for the person's own waiting market and at a waiting vantage (F105 criterion 4), and criterion 14 still governs it.*

## Why

### The threshold, and why it is split

**50 creators and 250 patrons. Gated on the creators. Displayed as one combined 300.**

**A combined-only gate can be satisfied by 495 patrons and 5 creators** — which opens a metro with nothing in it. A newcomer's first lesson would be that SocialUs is empty. **Creators are what make Browse non-empty, so creators are the real gate.** Patrons are the reason opening is worth doing; creators are the reason it is possible.

**The member sees one number because Don asked for one number.** A popup with a count and a message stays a popup with a count and a message. The split is how the platform decides; 300 is what the person reads.

**These are starting values and are expected to move.** Criterion 11 makes them per-metro, since dense and thin metros need different floors. **Nothing about the number is a commitment to the member** — criterion 9 is the guard: the message says what is needed, never when it will arrive.

### Leaving an email, and the count

Uniqueness on an email makes *is this address already waiting?* answerable, so the response is identical either way (criterion 14). Any truthful live count leaks that by differencing, whether read before or after the write (found 2026-09-22 by running the handler against Postgres while the mocked test stayed green). Don, 2026-09-23: the count comes back, **cached** (at most an hour old, shared with every surface that shows it), so it is not a function of the submission. After the window it can move by one; ruled acceptable. Hashing the address would cost the one message criterion 15 permits and is not used.

## Not this

A waitlist surface, a progress bar, a leaderboard, or a referral mechanic. Ranking or displaying who joined. Any use of a left address other than the one message criterion 15 permits. Opening a metro automatically. Charging for a place in line, or selling one.

## Rulings
- **2026-11-12 — A member who signs up by mobile number in a waiting market is told it opened by email, and only if they leave one on the waiting screen (optional, one field, criterion 15's single use). We send no "it opened" text.** Sign-up is by mobile number now (F081, 2026-11-12) and Twilio Verify sends only sign-in codes, so a text would need a number of our own. [for now] [replaces none] [binds tiers=planning,code surfaces=waitlist,signup]
- **2026-11-12 — Whether a person outside an open market is asked if they make or support is reopened, for the end-to-end design of the sign-up journey; until then nothing changes in the code, and the make/support gate (criterion 10, F118) waits on the same design.** The PM, verbatim: *"I want that to be part of the focus for how we design this sign up journey. It needs to be more fully designed end to end."* [for now] [replaces F076: A person outside an open market is not asked whether they are here to make, sell or organize, or to find and support; the waitlist counts one number.] [replaces F076: F076's make-or-find answer is a property of the waitlist entry, not the account, and is discarded when the metro opens.] [binds tiers=planning,code surfaces=waitlist,signup build=none]
- **2026-10-25 — The "market opened" email stays, for the landing list (criteria 13–15 stand); a person opens a market with `scripts/market/open-market.ts`, which sends "SocialUs is open in {town or market}. See what's going on." and then discards each address it reached.** The PM, 2026-10-11, on `socialus-web` #616 (Resend, those words); rebuilt on markets 2026-10-25. It sends through the reminders' Resend sender: the key is set, `FOLLOW_EMAIL_FROM` (a verified sending domain) is not. [for now] [binds tiers=planning,code surfaces=waitlist,email,copy] Issue: #616.
- **2026-09-23 — The waitlist count comes back, CACHED rather than live, and metros sort by it.** *(#216, built in `socialus-web` #217)*. Don: *"how would anyone know about anybody elses emails with just a count? that seems a bit too over the top for privacy. Nobody would be able to know anything else except someone else somewhere else also found this site. they could have even chosen the wrong area. also it would be cool to sort those metros by number of people signed up."* **The oracle is real and the stakes are small** — what it discloses is *this address expressed interest in a local app before launch*, which does not justify removing something useful. **The fix depends on the mechanism:** the leak was never the number existing, it was the number being **recomputed and re-displayed in response to your own write**. Read it before the write and two submissions differ; read it after and a single probe differs — either way the figure is a function of what the reader just did. **A cached figure is not**, so criterion 14 is met by the number not moving rather than by there being no number. **One read serves every surface** — the popup and the picker's ordering — because a fresher number anywhere reopens what the cache closes, and **a sorted list is the strictest case since it exposes every metro at once**. **What the cache does not close, ruled acceptable and written down so nobody re-derives it as new:** after the window expires the figure refreshes, so in a metro where nothing else happened inside that window a person who submitted and waited could see it move by one and attribute that to themselves. No window length removes it — longer is rarer and staler, shorter is fresher and more attributable — and it is weakest where there is real demand and strongest in an empty metro, which is where the answer is least interesting. **F076 criteria 7, 8 and 14 are restated and criterion 16 is added.** **No migration:** `metro_polygons.creator_count`/`patron_count` are already maintained by the join handlers, so this is one cached read of two columns and the schema does not move. [for now] [binds tiers=code surfaces=waitlist] [replaces 2026-09-22: A live count cannot satisfy F076 criterion 14] [replaces 2026-09-21: same words, same status, same count]
- **2026-09-21 — Someone who picks a metro that is not open may leave an email to be told when it opens, without signing up.** Don's ruling, answering the open question `MetroNotCoveredPanel` already carried in a comment. It is F076 criteria 13-15. **The real change is to criterion 4's enforcement:** idempotency was carried by `member_id unique` and an anonymous entry has no member, so the key becomes the normalised email per metro. **That is a privacy consequence and not a constraint swap — a unique key on an address makes *is this address on the list* answerable by anyone who can reach the endpoint.** **The mitigation is stated rather than implied: the response must be identical either way** — same words, same status. **Hashing is not the answer here**: the address must be readable to send the one message permitted, so it is stored as an address. **The single permitted use is that one message**, after which it is discarded. [binds tiers=code surfaces=waitlist] [replaces F076: ~~Notifying people when a metro opens~~]
