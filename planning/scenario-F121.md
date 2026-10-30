---
id: F121
title: Shelves are data, and we try several to learn which ones help
status: draft
horizon: considering
rank: 3
date: 2026-10-30
depends: [F098, F119]
---
## Story

*The PM, 2026-10-27, verbatim:* "How could we A/B test this? So I'm thinking we should try a few and the first one is next 7 days of things to do. Then categories of things to buy like home sales or makers events. But even these are too broad. I'd also like seasonal things like Halloween is coming up so Halloween themed things. And we're entering fall so garden things for fall. A lot of these categories overlap too But we want to make sure people know about things before they happen. I also want tours to be based on a persons interests." Then: "Yeah. Let's try various categories." ("Tours" is read as shelves.)

Maya opens SocialUs on a Monday in November. First come the farm stand and run club she follows, then a quiet line, then *Next 7 days*, *Garage and estate sales this weekend*, *Getting ready for Thanksgiving* and *Because you like gardening*. The pie pre-order she saw under Thanksgiving doesn't show again further down. Each week Don's dashboard shows which shelves people tapped and saved from, and which to keep, move up or retire.

## Acceptance

1. **Followed first, everywhere:** every view (Home's shelves, Explore, a search, an ask) opens with the timely items it matches from Pages and people the member follows, then one quiet end line, then everything else that matches. No end line when that block is empty.
2. **A shelf is a row of data, not code:** a name, a query (post kind, Page collection, tags, member interest, date window, season dates), a lead time, an order inside, a place (fixed slot or rotating), and an on/off. Adding, renaming or retiring one is a data change that needs no deploy.
3. **Upcoming only:** a dated item qualifies only before it ends and once it starts within its shelf's lead time. An undated post leaves at its shelf life (#230 table); Pages stay.
4. **Each item shows once per screen:** shelves fill top to bottom, and an item goes in the first shelf it qualifies for.
5. **An empty shelf is absent**, and a shelf shows about 10 to 12 items and a quiet "See all" text link to its full list (a deep link from the F119 registry).
6. **The starting shelves**, under the followed shelf, are the list Don approves in this PR: *Next 7 days*; at least three things-to-buy shelves narrower than "home sales" or "maker events"; the current seasonal shelf; and up to three interest shelves per member.
7. **Interest shelves come from the interests a member declared on You**, one shelf per interest, three at most; none for a signed-out visitor. They appear on Home and the wide-open ask, never on Explore, which isn't ranked by a member's interests.
8. **Seasonal shelves run by date:** each has a start and end (Thanksgiving Nov 2–28, 2026, through Small Business Saturday; then a holiday shelf Nov 29–Dec 24), and turns itself on and off with no one touching it.
9. **A season calendar, kept by an agent:** a scheduled run keeps the season list six weeks ahead and switches dates. A season whose shelf name isn't on Don's approved list is drafted and sent to Don; it doesn't go live without his yes.
10. **Rotation, not a fixed order:** the followed shelf and *Next 7 days* stay first; the remaining shelves rotate order per member per day, so each spends about equal time in each position. The order holds still within a day.
11. **Shelf-level counts:** for each shelf and week: impressions (shelf at least half on screen for a second), taps (a card opened), and saves (a thumbs up, add to calendar, or follow).
12. **Logging follows F089 and the search-demand rules:** no member id stored with a count, the existing logging opt-out on You stops it, raw rows are deleted after 30 days, and test and builder accounts never count.
13. **A weekly shelf scoreboard on the PM's dashboard:** each shelf's impressions, tap rate, save rate, and a verdict: *too little data*, *keep*, *move up* or *retire*.
14. **Promote and retire rules:** a shelf is judged only with at least 200 impressions from at least 10 members in 14 days. Two judged weeks in a row at the top save rate means *move up*; two in a row under half the median means *retire*. Seasonal shelves end by date and aren't retired. Verdicts are proposals; Don rules on the shelf list.

## Not this

Bandits or learned shelf order (later, with more members). Learned interest shelves (F113). Paid or promoted shelves (Discover). Chips, pills or a tab bar of shelf names. The card anatomy and post kind field (#230 §5, its own ticket). Home's stop card and older picks stay in F098.

## Why

- **Lives somewhere better?** No: big apps have shelves, but none of them shows what's on locally this week from people you chose to follow.
- **Only locals know?** Yes: the sales, seasons and makers are local; the shelves only sort them.
- **Gets people together?** Yes: *Next 7 days* and lead times put events in front of people before they happen.
- **Stays fresh on its own?** Yes: items leave at their end or shelf life, seasonal shelves switch by date, and the agent keeps the calendar.
- **Who keeps it current?** The shelf table; members' posts fill it, an agent keeps the season dates, and Don keeps the list and words.
- **Better as more people join?** Yes: more posts fill narrower shelves, and more impressions make the scoreboard judge sooner.

**Path: well-worn** for the method; the shelf list and every shelf name are Don's (words). Research: `planning/research/explore-shelves-and-shelf-life-2026-10-27.md` (#230). Precedents:
- Rows as data, ranked per member: Netflix, [Learning a Personalized Homepage (2015)](https://gwern.net/doc/www/netflixtechblog.com/2f5717e8bbdc98d2caf5c7a972359fbb7e7c0b28.html); App Store and Play edit shelves daily ([Apple HIG: collections](https://developer.apple.com/design/human-interface-guidelines/collections)).
- Bandits need traffic: Spotify's home shelves use a bandit at hundreds of millions of users (McInerney et al., "Explore, Exploit, and Explain", RecSys 2018). At beta size, rotating order is the fair test: it spreads position bias evenly (Joachims et al., "Accurately Interpreting Clickthrough Data", SIGIR 2005), so plain rates compare.
- Followed first, then wider: Instagram's "You're all caught up" (2018), without its ads or "can't hide".
- Seasonal collections by date: Etsy and Pinterest seasonal hubs, Eventbrite holiday collections.

**Starting shelves for Don to approve or rename** (names are drafts):

| Shelf | Query | Lead time |
|---|---|---|
| Next 7 days | events, openings, market days | 7 days |
| Garage and estate sales this weekend | sale posts, Fri–Sun | 5 days |
| Makers' markets and craft fairs | market days, maker events | 14 days |
| Fresh from the farm | farm Pages' posts, farm stands | 7 days |
| Getting ready for Thanksgiving (Nov 2–28) | pre-orders, pies, turkeys, Small Business Saturday | season dates |
| Fall in the garden | garden, nursery and plant-sale posts | 14 days |
| Free this week | the Free tag | 7 days |
| Kids and families this weekend | Pages and posts tagged for families | 5 days |
| Because you like {interest} | the member's declared interest | 14 days |
| Count me in | open Wonders | until sign-up closes |
| New here | Pages created in the last 30 days | — |

Seasons kept after Thanksgiving: the holidays (Nov 29–Dec 24), New Year (Dec 26–Jan 1), Valentine's (Feb 1–14), spring garden (Mar 1–Apr 30). Halloween (Oct 31) has passed.

Overlap: *Garage sales* and *Free* share items; first-shelf-wins and rotation together mean each shelf gets its fair turn at those items.

[platform none]

## Rulings
- **2026-10-30 — Every view opens with the timely items it matches from the Pages and people the member follows, then one quiet end line, then widens to everything else that matches. No chips or pills.** The PM, relayed 2026-10-30, from his notes of 2026-10-27 and research #230. Following is the member's own choice, like a declared interest; it never favours a Page for its follower count. [for now] [replaces none] [binds tiers=planning,code surfaces=home,explore,search,following build=none]
- **2026-10-30 — Timely posts leave the shelves and lists at a shelf life set by kind (#230 §4); they stay on their Page under Past and in search. Shelf life is when a post ends; staleness (the 2026-09-15 90 days) is when a Page goes quiet, and still only sorts last.** The PM, relayed 2026-10-30. [for now] [replaces none] [binds tiers=planning,code surfaces=home,explore,posts build=none]
- **2026-10-30 — Shelves are rows of data, tested by rotating their order per member per day and judged on a weekly scoreboard, not by a bandit, until traffic supports one.** Decided by the agent (well-worn: Netflix rows as data; rotation over bandits at small scale). Don rules on the list and the names. [for now] [replaces none] [binds tiers=planning,code surfaces=home,explore,metrics build=none]
