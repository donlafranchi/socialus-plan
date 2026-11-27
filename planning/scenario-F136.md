---
id: F136
title: Hyper-specific search connects members, and feeds a minimal front door and what producers learn
status: draft
concept: CO-0063
horizon: considering
rank: 8
date: 2026-11-15
depends: [F092, F119, F121, F134]
---
Search widening by result count (hood → town → area → beyond, labelled, 10 results as the default) is ruled in `product/systems/rings.md`.

## Story

*The PM, 2026-11-15, verbatim:* "the most important thing is that we connect our members and help them connect with each other and that's kind of what this searches meant to empower"

Rae searches "cozy coffee with a patio, Midtown"; later her front door shows a new café near it. A pottery studio sees that over ten people in Midtown searched "pottery class, evenings" and adds one, never learning who.

## Acceptance

1. **Hyper-specific:** one search box understands place, item (what a place carries, F092 2026-11-13), time ("tonight", "this weekend", "open now") and vibe words ("cozy", "kid-friendly", "quiet"), alone or mixed, through the one dictionary.
2. **Timely when asked:** with time words, soonest first; without, the existing order.
3. **Your searches, kept for you:** each signed-in member's searches are kept on their own profile; You lists them, newest first; one tap deletes one, one tap deletes all; a switch stops keeping them. It keeps the words searched and when, never where the member was standing (F105, F107); searches that reach a hidden signal's help (`signals.md`) are never kept. Nothing about them is shown to any other member or Page.
4. **Kept only as long as the PM rules** (brief call 1); older rows are deleted by a scheduled job, not hidden.
5. **Two switches, two jobs:** "Count my searches" (the anonymous market count, built) and the history switch above are separate; turning one off leaves the other.
6. **Producers see counts only:** a Page's managers see terms searched by at least ten different members in that market in the last 30 days, and the areas each came from only where that area alone clears ten; never who, never one person's searches, never a count below ten.
7. **The front door is minimal:** the search box, then at most three slots. A member with no history gets the market's story or did-you-know and what's on in the next seven days. A member with history gets at most one slot drawn from it.
8. **Slots come from a pool:** each slot is filled from F121's shelves-as-data, by simple rules (new or has history, day of week, time of day, what's timely). An empty slot is absent; nothing scrolls past the third.
9. **Visitors keep no history** (F134): their front door is the minimal one for a new member.
10. **Disclosed:** the Privacy page says what is kept, for how long, and how to delete it, before item 3 ships.

## Not this

Chat that answers in conversation (later; F119 is the cheap step). A feed or engagement ranking. Distance in ranking (`places.md`). Selling or sharing any of it.

## Why

- **Lives somewhere better?** No: Google and Yelp don't know what a town's own people look for.
- **Only locals know?** Yes.
- **Gets people together?** Yes: the answer to a search is another member.
- **Stays fresh on its own?** Yes: slots read live shelves; history expires.
- **Who keeps it current?** Shelf rules and the dictionary agent.
- **Better as more people join?** Yes: more searches clear the floor.

**Path: mixed.** Well-worn: Google My Activity, Etsy and Shopify search reports, Google Trends, rows as data (F121). The PM's: how long history is kept, the launch slot set. Brief: `planning/briefs/hyper-specific-search-2026-11-15.md`. [platform none]

## Rulings

- **2026-11-27 — Themes in the store (F137) go ahead of hyper-specific search (F136); both stay behind the 6 January launch-blocking work.** The PM, verbatim: *"B"*, picking themes first. F137 is next, rank 7; F136 is considering, rank 8. [for now] [replaces none] [binds tiers=planning surfaces=roadmap]
- **2026-11-15 — Search is hyper-specific: specific by location, by item, by vibe, or any mix; local is still true but not the defining word. Its purpose is to connect members and help them connect with each other.** The PM, verbatim: *"I don't know that it's a [hyper] local search although it is local but it's probably hyper specific and hyper specific can mean anything they can be location they can mean items that can mean vibes … the most important thing is that we connect our members and help them connect with each other and that's kind of what this searches meant to empower."* [for now] [replaces none] [binds tiers=planning,code surfaces=search,explore] Issue: #1329.
- **2026-11-15 — Search is high-powered and timely: what is happening now and soon, near the member, with what places carry leading.** The PM, verbatim: *"this needs to be high-powered … search and also timely."* [for now] [replaces none] [binds tiers=planning,code surfaces=search,explore] Issue: #1329.
- **2026-11-15 — Each member's searches are kept on their own profile to tailor what we show that member; they can see and delete them.** The PM, verbatim: *"that is supposed to be used to feed their personal profile so that we learn what to show them. They can ask us to delete it but we are collecting that … to give them a better user experience."* [for now] [replaces none] [binds tiers=planning,code surfaces=search,you,home,privacy] Issue: #1326.
- **2026-11-15 — Producers get what people searched for only in aggregate, "so many people searched for this in these areas", never who searched or any one member's searches.** The PM, verbatim: *"We're not gonna tell producers what each individual user search, but it should say such so many people search for this thing in these areas you know maybe you'd want to provide it for them that insight is what helps consumers, and producers in the market help each other."* [for now] [replaces none] [binds tiers=planning,code surfaces=search,pages,insights,privacy] Issue: #1327.
- **2026-11-15 — The front door is minimal and stays minimal until a member has history; even tailored, it stays minimal. Less is more.** The PM, verbatim: *"our front door to the app to the user is fairly minimal and remains that way until users have some kind of history so we can tailor it to them and even when we do, it's minimal … we start with less less is more."* [for now] [replaces 2026-10-04: Home returns as rows that keep going] [binds tiers=planning,code surfaces=home,explore] Issue: #1328.
- **2026-11-15 — What the front door shows is a pool of many ideas that come and go, each used at different times for different reasons: what's new, deals, happenings, reminders, the market's story, did-you-know, tips. Not a fixed set of sections.** The PM, verbatim: *"we have many many ideas that can come and go where we used at different times for different reasons."* [for now] [replaces none] [binds tiers=planning,code surfaces=home,shelves] Issue: #1328.
- **2026-11-15 — The front door is a few slots filled from F121's shelves by simple rules (new member or has history, day and time, what's timely), never a feed.** Decided by the agent (well-worn: rows as data, F121; Google Discover and Yelp's home both fill a bounded set of modules), applying the PM's two rulings above. [for now] [replaces none] [binds tiers=planning,code surfaces=home,shelves] Issue: #1328.
- **2026-11-15 — A producer sees a searched term only when at least ten different members searched it in that market in the last 30 days, and an area only when that area alone clears ten; smaller counts are stored and withheld, never shown.** Decided by the agent: F089's floor of ten, now countable as distinct members from each member's own history; CDC WONDER suppresses counts under 10, and Google Trends shows small volumes as zero. It replaces the Page card's three-searches rule (web `page_search_demand`). [for now] [replaces none] [binds tiers=planning,code surfaces=search,pages,insights] Issue: #1327.
- **2026-11-15 — Keeping a member's search history and counting their searches anonymously are two switches; turning one off leaves the other. A signed-out visitor keeps no history.** Decided by the agent (well-worn: Google keeps Web & App Activity separate from aggregate Trends; Craigslist keeps nothing without an account). [for now] [replaces none] [binds tiers=planning,code surfaces=you,search,privacy] Issue: #1326.

[open-question owner=don raised=2026-11-15] How long is a member's search history kept before it is deleted on its own?
