---
id: F136
title: Hyper-specific search connects members, and feeds a minimal front door and what producers learn
status: draft
concept: new
horizon: considering
rank: 7
date: 2026-11-15
depends: [F092, F119, F121, F134]
---
## Story

*The PM, 2026-11-15, verbatim:* "the most important thing is that we connect our members and help them connect with each other and that's kind of what this searches meant to empower"

Rae opens SocialUs in Sacramento for the first time. The front door is a search box and two things: this week's market story and what's on in the next seven days. She searches "cozy coffee with a patio, Midtown". A week later the front door still has three things, and one is the new café that opened near her searches. On You she sees her searches and clears one. Across town, a ceramics studio sees that "pottery class, evenings" was searched by more than ten people in Midtown this month, and adds a Thursday class. Nobody at the studio knows Rae was one of them.

## Acceptance

1. **Hyper-specific:** one search box understands place, item (what a place carries, F092 2026-11-13), time ("tonight", "this weekend", "open now") and vibe words ("cozy", "kid-friendly", "quiet"), alone or mixed, through the one search dictionary (`model.md` § Search is the filter).
2. **Timely first when time is asked:** a search with time words orders by what is happening soonest, ending soonest last; without them the existing order holds.
3. **Your searches, kept for you:** each signed-in member's searches are kept on their own profile; You lists them, newest first; one tap deletes one, one tap deletes all; a switch stops keeping them. It keeps the words searched and when, never where the member was standing (F105, F107); searches that reach a hidden signal's help (`signals.md`) are never kept. Nothing about them is shown to any other member or Page.
4. **Kept only as long as the PM rules** (brief call 1); older rows are deleted by a scheduled job, not hidden.
5. **Two switches, two jobs:** "Count my searches" (the anonymous market count, built) and the history switch above are separate; turning one off leaves the other.
6. **Producers see counts only:** a Page's managers see terms searched by at least ten different members in that market in the last 30 days, and the areas each came from only where that area alone clears ten; never who, never one person's searches, never a count below ten.
7. **The front door is minimal:** the search box, then at most three slots. A member with no history gets the market's story or did-you-know and what's on in the next seven days. A member with history gets at most one slot drawn from it.
8. **Slots come from a pool:** each slot is filled from F121's shelves-as-data, by simple rules (new or has history, day of week, time of day, what's timely). An empty slot is absent; nothing scrolls past the third.
9. **Visitors keep no history** (F134): their front door is the minimal one for a new member.
10. **Disclosed:** the Privacy page says searches are kept on the member's profile to tailor what they see, for how long, and how to see and delete them, before item 3 ships.

## Not this

An AI chat assistant that answers in conversation (later; F119's router is the cheap step already approved). A feed, infinite scroll, or ranking by engagement. Distance in ranking (`places.md` holds that for this version). A per-producer dashboard beyond the card that exists. Selling or sharing any of this.

## Why

- **Lives somewhere better?** No: Google and Yelp don't know a town's makers, groups and happenings, or what its own people are looking for.
- **Only locals know?** Yes: what people here want, and who here has it.
- **Gets people together?** Yes: it is the point. A search is a member asking; the answer is another member.
- **Stays fresh on its own?** Yes: slots draw from live posts and shelves; history expires on schedule.
- **Who keeps it current?** The shelf rules and the dictionary agent; the PM rules on names and the slot set.
- **Better as more people join?** Yes: more searches clear the floor, so producers learn more, and the dictionary grows.

**Path: mixed.** Well-worn: Google My Activity (see and delete one or all, auto-delete) for history; Etsy and Shopify search-term reports for producers; Google Trends and Popular times for withholding small counts; Netflix-style rows as data for slots (F121). New territory, the PM's: how long history is kept, and the launch slot set. Brief: `planning/briefs/hyper-specific-search-2026-11-15.md`. [platform none]

## Rulings

- **2026-11-15 — Search is hyper-specific: specific by location, by item, by vibe, or any mix; local is still true but not the defining word. Its purpose is to connect members and help them connect with each other.** The PM, verbatim: *"I don't know that it's a [hyper] local search although it is local but it's probably hyper specific and hyper specific can mean anything they can be location they can mean items that can mean vibes … the most important thing is that we connect our members and help them connect with each other and that's kind of what this searches meant to empower."* [for now] [replaces none] [binds tiers=planning,code surfaces=search,explore] Issue: #1329.
- **2026-11-15 — Search is high-powered and timely: what is happening now and soon, near the member, with what places carry leading.** The PM, verbatim: *"this needs to be high-powered … search and also timely."* [for now] [replaces none] [binds tiers=planning,code surfaces=search,explore] Issue: #1329.
- **2026-11-15 — Each member's searches are kept on their own profile to tailor what we show that member; they can see and delete them.** The PM, verbatim: *"that is supposed to be used to feed their personal profile so that we learn what to show them. They can ask us to delete it but we are collecting that … to give them a better user experience."* [for now] [replaces none] [binds tiers=planning,code surfaces=search,you,home,privacy] Issue: #1326.
- **2026-11-15 — Producers get what people searched for only in aggregate, "so many people searched for this in these areas", never who searched or any one member's searches.** The PM, verbatim: *"We're not gonna tell producers what each individual user search, but it should say such so many people search for this thing in these areas you know maybe you'd want to provide it for them that insight is what helps consumers, and producers in the market help each other."* [always] [replaces none] [binds tiers=planning,code surfaces=search,pages,insights,privacy] Issue: #1327.
- **2026-11-15 — The front door is minimal and stays minimal until a member has history; even tailored, it stays minimal. Less is more.** The PM, verbatim: *"our front door to the app to the user is fairly minimal and remains that way until users have some kind of history so we can tailor it to them and even when we do, it's minimal … we start with less less is more."* [for now] [replaces 2026-10-04: Home returns as rows that keep going] [binds tiers=planning,code surfaces=home,explore] Issue: #1328.
- **2026-11-15 — What the front door shows is a pool of many ideas that come and go, each used at different times for different reasons: what's new, deals, happenings, reminders, the market's story, did-you-know, tips. Not a fixed set of sections.** The PM, verbatim: *"we have many many ideas that can come and go where we used at different times for different reasons."* [for now] [replaces none] [binds tiers=planning,code surfaces=home,shelves] Issue: #1328.
- **2026-11-15 — The front door is a few slots filled from F121's shelves by simple rules (new member or has history, day and time, what's timely), never a feed.** Decided by the agent (well-worn: rows as data, F121; Google Discover and Yelp's home both fill a bounded set of modules), applying the PM's two rulings above. [for now] [replaces none] [binds tiers=planning,code surfaces=home,shelves] Issue: #1328.
- **2026-11-15 — A producer sees a searched term only when at least ten different members searched it in that market in the last 30 days, and an area only when that area alone clears ten; smaller counts are stored and withheld, never shown.** Decided by the agent: F089's floor of ten, now countable as distinct members from each member's own history; CDC WONDER suppresses counts under 10, and Google Trends shows small volumes as zero. It replaces the Page card's three-searches rule (web `page_search_demand`). [for now] [replaces none] [binds tiers=planning,code surfaces=search,pages,insights] Issue: #1327.
- **2026-11-15 — Keeping a member's search history and counting their searches anonymously are two switches; turning one off leaves the other. A signed-out visitor keeps no history.** Decided by the agent (well-worn: Google keeps Web & App Activity separate from aggregate Trends; Craigslist keeps nothing without an account). [for now] [replaces none] [binds tiers=planning,code surfaces=you,search,privacy] Issue: #1326.

[open-question owner=don raised=2026-11-15] How long is a member's search history kept before it is deleted on its own?
