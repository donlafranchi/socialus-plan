---
id: what-member-journey
purpose: The loops Members move through, in four families, in priority order — each with who it's for, what it currently uses, and what's missing.
layer: what
status: active
reviewed: 2026-10-05
---

# Member journey

**What changed (2026-10-05):** Sharing and Trade are one family, **Exchange** — swapping, bartering, giving away, lending, trading skills or time, without dollars, then selling (Don: *"the Trade persona is more like exchange or transact without dollars"*); 13 loops in five families became 15 in four; each loop now says who it's for, its steps in the app currently, what's missing and its beta status; maker and provider "profiles" are Pages, since members have no type and no public profile.

Foundational north star, upstream of every system spec. The platform exists so people can take ownership of their economic and civic future together — not by being an online third place, but by making real-world third places findable, recurring, and economically consequential. It is deliberately not built to grow like Facebook: as communities mature, deeper infrastructure (banking, insurance, shared services) spawns into separate federated platforms rather than being absorbed. This platform stays the foundational coordination layer, indefinitely.

## What the loops currently run on

- **A Page is what anyone makes.** Its **purpose** comes first: **Gather**, **Sell**, **Offer a service or teach**, or **Be creative** (Don, 2026-10-05). Business or Social group is worked out from the purpose for listing, never picked as an identity.
- **A member has no type and no public profile** (2026-10-01). Someone who wants to be found or followed makes a Page. You is private.
- **A Post is what a Page says** — an update, or a dated one with a time and a place, with tags. **Currently only a Page's managers post on it.**
- **Follow** links a member to a Page. Delivering posts to followers is cut for beta; a followed Page's posts reach a signed-in reader on Explore (F059 criterion 2b).
- **There is currently no messaging between members**, and the platform handles no money.
- **Status** is `ROADMAP.md`'s: **beta** (in for 2026-10-30), **later** (wanted, after beta), **cut** (off the beta list, may return).

| # | Loop | Family | Page purpose | Status |
|---|---|---|---|---|
| 1 | Find your people | Gathering | Gather | beta |
| 2 | Float an idea | Gathering | — | later |
| 3 | Land here | Gathering | any | beta (partial) |
| 4 | Gather regularly | Gathering | Gather | beta (RSVP cut) |
| 5 | Give it away | Exchange | Gather, Be creative | beta path (weak); later |
| 6 | Swap or barter | Exchange | Gather, Be creative | beta path (weak); later |
| 7 | Ask, borrow, lend | Exchange | Gather | later |
| 8 | Trade skills or time | Exchange | Offer a service or teach | beta path (weak); later |
| 9 | Make and be found | Exchange | Sell, Be creative | beta |
| 10 | Follow what you love | Exchange | any | beta (delivery cut) |
| 11 | Find a local pro | Exchange | Offer a service or teach | beta (trust signals later) |
| 12 | Start something | Pooling | any | later |
| 13 | Pool resources | Pooling | — | later (far horizon) |
| 14 | Steward what we built | Pooling | any | beta (Page role); tooling later |
| 15 | Federate and spawn | Federation | — | later (far horizon) |

## Family 1 — Gathering (the civic on-ramp)

The lightest, most universal loops — no belief required, only the desire to be less alone in a place.

1. **Find your people.** *Who and why:* someone new to a hobby or a neighbourhood who wants a regular thing to belong to. A run club or a chess meetup is currently findable only by being there and asking.
   - **Currently:** opens Explore or the map, sees Gather Pages nearby, opens one (one shareable URL), follows it.
   - **Missing:** search over Pages (cut for beta); a quiet way to say "I'll come" (RSVP, cut).
   - **Beta.**
2. **Float an idea.** *Who and why:* someone thinking of starting something who doesn't know if anyone would come. One sentence, no commitment; interest says whether to start. **Nothing converts** *(2026-09-15)*: they make the Page themselves.
   - **Currently:** nothing to post it from — Wonder's substrate shipped, its composer did not.
   - **Missing:** the Wonder composer and page.
   - **Later.**
3. **Land here.** *Who and why:* a newcomer who wants to know what's happening within walking distance this week — the highest-intent person this platform serves.
   - **Currently:** signed out, sees each Page's front door (name, picture, description) with posts withheld (F093); signs up with a zip, which sets the metro; signed in, sees What's happening by date.
   - **Missing:** posts in the signed-out view (withheld on purpose); Home rows (cut).
   - **Beta, partial.**
4. **Gather regularly.** *Who and why:* an organizer already convening something who wants it findable and persistent without running three apps for free.
   - **Currently:** makes a Gather Page, answers "How do people find you?", posts a dated Post with a weekly repeating series (F074); it shows in What's happening (F091) and on followers' Explore.
   - **Missing:** saying you're going (RSVP, cut); delivery to followers (cut).
   - **Beta.**

## Family 2 — Exchange (without dollars first, then selling)

Neighbors start recognizing each other as resources: giving away, swapping, bartering, lending, trading skills or time, and buying from each other. Many people want the dollar-free half, by Don's reading of online comments. **The platform currently handles no money, and that holds here:** a swap, a gift or an hour traded happens in person.

Precedents for the dollar-free half:
- **Buy Nothing** (https://buynothingproject.org/) — hyper-local gift groups, one per neighbourhood; give, ask, gratitude; no swaps or sales by rule.
- **Freecycle** (https://www.freecycle.org/) — local groups giving things away to keep them out of landfill; offer and wanted posts.
- **Bunz** (https://bunz.com/) — trading items for items, started in Toronto, with its own in-app currency (BTZ). The currency is a step SocialUs does not take.
- **Timebanks, such as hOurworld** (https://hourworld.org/) — an hour of anyone's help earns an hour of anyone else's; skills traded as time, not money.
- **Nextdoor's "For Sale & Free"** (https://nextdoor.com/for_sale_and_free/) — free items beside sale items in one neighbourhood feed, with a "Free" filter.

**A cheap beta path, using only what's in scope.** A member makes a Page with purpose Gather (a neighbourhood swap circle) or Be creative (their own), and posts what they're giving, swapping or lending, tagged **#free**, **#swap**, **#lend** or **#skillswap** (tags on posts are beta). Neighbours see them on Explore, tap a tag to see every Post carrying it, and follow the Page. **What makes it weak:** only a Page's managers can post on it, so a circle where every member posts — Buy Nothing's shape — needs member posting on a group Page; and there's no reply channel, so a Post has to say how to reach the person. **What would need new build:** member posting on a Gather Page; a reply or "I'd like this" on a Post, which needs messaging; marking a Post given or taken; for timebanks, an hours ledger. None of it is added to beta here.

5. **Give it away.** *Who and why:* someone with extra zucchini, a crib the kids outgrew, a box of tiles — who'd rather it go to a neighbour than a landfill.
   - **Currently:** posts it on their own Page or a swap circle's, tagged #free, saying where to pick it up or how to reach them.
   - **Missing:** member posting on a circle's Page; a reply; marking it taken.
   - **Beta path (weak); later for the rest.**
6. **Swap or barter.** *Who and why:* someone who'd trade sourdough starter for eggs, or a bike for a sewing machine, and doesn't want to sell.
   - **Currently:** a Post tagged #swap with what they have and what they'd take.
   - **Missing:** the same as loop 5; a reciprocity model is unruled (does the platform track balance, or stay pure gift?).
   - **Beta path (weak); later.**
7. **Ask, borrow, lend.** *Who and why:* someone who needs a truck for an hour or a ladder for a weekend, and the neighbour who has one. Give and take are one relationship in lived experience. The UI verbs are "Offer up" and "Ask" (2026-09-15).
   - **Currently:** a lender can post #lend on their own Page; an ask has nowhere to go without a Page.
   - **Missing:** Ask and Offer up, blocked on member-to-member messaging, not on the composer.
   - **Later.**
8. **Trade skills or time.** *Who and why:* someone who'd fix a bike for an hour of piano lessons — a timebank member, or anyone whose skills outrun their cash.
   - **Currently:** a Page with purpose Offer a service or teach, posting #skillswap.
   - **Missing:** an hours ledger, a timebank's core; it is not designed and touches the platform's no-money stance, so it needs a ruling first.
   - **Beta path (weak); later.**
9. **Make and be found.** *Who and why:* a maker or a small seller who wants neighbours to find them beyond one market day.
   - **Currently:** makes a Page — Sell, or Be creative for an artist — with a picture, where they are or the markets they're usually at, tags, and Posts for each batch or market.
   - **Missing:** individual product listings on a Page (later, postponed 2026-10-01); payments, which stay off-platform.
   - **Beta.**
10. **Follow what you love.** *Who and why:* a buyer or a regular who wants to find a good maker or a good circle again — the one early signal that matters: do people come back?
    - **Currently:** follows the Page; its Posts show on Explore when signed in.
    - **Missing:** delivery to followers (Bulletins, cut); a saved search (later).
    - **Beta.**
11. **Find a local pro.** *Who and why:* someone who needs a plumber, a vet or an accountant and wants the one their neighbour trusts, not the one who paid Yelp or Angi for visibility.
    - **Currently:** finds a Page with purpose Offer a service or teach, its phone and the neighbourhoods it works in (2026-09-30).
    - **Missing:** vouching (F095, later); search over Pages (cut). *Test every service-provider proposal against: would the trusted-neighbor pattern still operate under this?*
    - **Beta, partial.**

## Family 3 — Pooling (community ownership)

Members become stakeholders; capital is pooled, businesses founded, resources shared. Ownership concentration is the squeeze; collective ownership is the answer (the wealth-circulation absolute lives in `goals.md`). **The app is a finding mechanism** (2026-09-19): the organizing happens in real life, and where it needs a legal form, in entities formed outside the platform.

12. **Start something.** *Who and why:* someone with an idea that would grow the community's capacity — a tool library, a co-op grocery.
    - **Currently:** makes a Page and posts from it; there is no goal or Initiative object (2026-09-19).
    - **Missing:** Wonder to test interest first (loop 2); Encouragement and Pledge have no design.
    - **Later.**
13. **Pool resources.** *Who and why:* neighbours who together could buy what no household could alone — land, a building, a workshop's tools.
    - **Currently:** nothing on the platform.
    - **Missing:** everything; pledges would hand off to a partner CDFI, and the platform holds no funds for itself (Won't).
    - **Later, far horizon.**
14. **Steward what we built.** *Who and why:* the person who keeps a shared thing going — a garden's watering rotation, a tool library's checkouts. Shared resources fail more often from atrophied stewardship than outside pressure.
    - **Currently:** the managing role on a Page, which every non-business Page has.
    - **Missing:** shared schedules and inventory.
    - **Beta** for the role; **later** for the tooling.

## Family 4 — Federation (the spawn boundary)

15. **Federate and spawn.** *Who and why:* a community whose needs outgrow what this platform should try to do — real banking, shared bookkeeping and insurance, regional intelligence. The handoff to dedicated, separate, federated platforms, connected through identity and protocol, never absorbed. This is the platform's most important architectural commitment and the answer to "what stops this from becoming Facebook" — a platform trying to do banking, insurance, and gathering coordination all at once fails at all of them.
    - **Currently:** nothing. **Later, far horizon.**

## Why this order

Not a roadmap — a constraint on which loops can ship before which. Three gradients ascend together: **activation energy** (loop 1 asks nothing of a visitor; loop 15 requires a community that's already organized capital and founded businesses), **belief required** (loop 1 is pre-political; loop 13 requires believing pooled ownership is real), and **stake accumulated** (every loop produces an event in a Member's record — a follow, a Page made, a post — so by Pooling a Member's deeper participation is anchored in real history, not abstract willingness).

Each loop leans on the ones above it: pooling works because the community already knows each other through gathering and exchange. Skip Gathering and the platform is a directory; skip Exchange and pooling has no economic substrate. When a scenario advances a deeper-loop behavior without the upstream substrate earned, that's the pattern to push back on. **Beta currently covers Gathering, the selling half of Exchange, and a member's first step into Pooling (a Page they steward); the dollar-free half of Exchange has only the weak path above until members can post on a circle's Page and reply to each other.**
