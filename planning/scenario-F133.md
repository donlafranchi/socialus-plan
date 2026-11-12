---
id: F133
title: Usage counts kept in our own database, so the PM sees who comes back, what they use and where they drop off, with nothing leaving the platform
status: approved
horizon: now
rank: 6
date: 2026-11-12
approved: 2026-11-12, the PM: "A A" (the second A is analytics)
depends: []
concept: new
---
## Story

*The PM, 2026-11-11:* asked for "load testing and ... other app telemetry type things"; analytics came back as options because it touches member data. *2026-11-12:* picked A, count it ourselves.

The PM opens the dashboard on a Monday. He sees that of the 40 members who joined three weeks ago, 22 came back last week; that Explore and posts are used most and groups least; and that most people who start sign-up finish it, but few make a first post. No outside company saw any of it, and a member who turned sharing off on You is in none of the numbers.

## Acceptance

1. **Coming back:** members active each week, by the week they joined, for the last 12 weeks.
2. **What they use:** per day, how many members used each part of the app (posts, Explore, Pages, groups, the map, search, Ask), counted at most once per member per part per day.
3. **Where they drop off:** per week, how many reached each step of sign-up, a first follow and a first post.
4. **Counts only:** no member id, email, IP address or precise location is stored beside any count; dedupe keys are one-way hashes deleted within 8 days, as map taps do.
5. **Nothing leaves:** no usage data is sent to any outside service, and nothing is added to a member's page load beyond what the app already sends.
6. **One switch:** a member who turns sharing off on You is never counted, using the switch that already covers search and map taps; builders are never counted.
7. **On the dashboard:** staff see the three answers on the PM's dashboard; nobody else can read the counts.
8. **Counting starts before the first invited cohort arrives.**

## Not this

Charts beyond the three answers. Session replay, heatmaps, click paths of one member. Any outside analytics tool (Vercel Web Analytics may be added later as its own decision).

## Why

- **Lives somewhere better?** No: an outside tool would answer these by keeping a history of each person, which our data principle and our error-tracking bar refuse.
- **Only locals know?** No: it is how the app is run.
- **Gets people together?** Yes: it shows whether people come back to meet and trade, so the app is tuned toward that.
- **Stays fresh on its own?** Yes: counts are written as members use the app and read straight onto the dashboard.
- **Who keeps it current?** Agents; the PM reads the dashboard.
- **Better as more people join?** Yes: the counts get more useful with more members, and no one is more exposed by it.

**Path: new territory.** The same pattern as our own map-tap and search-demand counts; Plausible counts visitors with a hash whose salt is deleted daily and sets no cookies ([Plausible data policy](https://plausible.io/data-policy)). Brief: planning/briefs/product-analytics-2026-11-11.md. [platform none]

## Rulings

- **2026-11-12 — Product analytics are counts kept in our own database, with no member id beside them and nothing sent to an outside service; a member who turns sharing off on You is never counted. The count tables are launch preparation, an exception to the 2026-11-06 build freeze, so the first members are counted.** The PM, picking A ("A A"), for F133. [binds tiers=planning,code surfaces=metrics,privacy,data,dashboard]
