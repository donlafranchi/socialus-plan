---
id: F104
title: Explore shows the whole market, ordered hood, town, market, online, with towns by adjacency
status: approved
date: 2026-10-11
depends: [F059, F103]
approved: 2026-10-11 — the PM: the three rings replace "local means the whole metro"; order, never distance; a Page in a waiting market is absent until it opens.
---
## Story

Marcus lives in Granite Bay. His Explore opens on Granite Bay's Pages and posts, then Roseville, Loomis and Folsom, which touch it, then Rocklin and Citrus Heights, then Auburn and Lincoln, and Davis and Placerville after those. Nothing says how far anything is. Tahoe City is in Placer County too, and it never appears: it is a different market. A potter in Kings Beach built her Page last month; nobody sees it in Explore until Tahoe opens, and the day it does she is there without lifting a finger.

## Acceptance

1. **Every surface that scopes by locality scopes to one market** (Explore list and map, Home, search results, unclaimed listings, the report queue's bar): the vantage's market (F105), the member's home market by default. No result from another market appears on these surfaces.
2. **Inside the market the order is hood → town → the rest of the market by adjacency → online.** The hood band holds Pages in the member's own neighbourhood, when the member has one; the town band the member's home town; then the towns that touch the member's town, then the towns that touch those, and so on. A county remainder counts as a town; a curated bridge table joins towns that face each other across a river or lake. Inside one band, F059 criterion 3's order (recency, community response) holds. Pages with no place in the market and marked online come last.
3. **No distance, no hop count and no "near you" is shown or filterable anywhere.** Locality on a card is the Page's neighbourhood or town name, nothing finer, nothing in miles or minutes (2026-09-30 stands).
4. **A Page's market is the market of its anchor Location's place; a Page with no Location takes its owner's home market.** A Page in a waiting market appears on no Explore, Home or search surface from any vantage until its market opens; on the day it opens it appears with no act by its owner.
5. **A member with no neighbourhood starts at the town band.** The hood band exists in the order and is empty for them; nothing in beta sets a member's neighbourhood.

## Not this

A wider or neighbouring-market section (its own scenario when a second market opens). Rings sized by density, drive time or behaviour. A neighbourhood picker for members. Changing what a Page shows about where it is, or the map's markers (2026-10-07). Distance, radius or "near me" of any kind.

## Why

- **Lives somewhere better?** No: an order by who is actually next to whom, across a market, is nowhere else.
- **Only locals know?** Yes: that Granite Bay faces Folsom across a county line, and Tahoe is not Sacramento, is how people there already live.
- **Gets people together?** Yes: the nearest towns come first, so what a member sees first is what they can reach.
- **Stays fresh on its own?** Yes: order within a band is recency; adjacency changes only when boundaries do.
- **Who keeps it current?** Census TIGER polygons yearly; the bridge table, a one-time human edit per market.
- **Better as more people join?** Yes: bands fill as makers join; nothing has to be widened by hand.

**Path: new territory, ruled.** Replaces F094 (draft, deleted; its scope inventory survives in `planning/research/local-inventory-2026-10-11.md`), F059 criteria 6 and 7 (restated: scoped to the vantage's market), and the 2026-09-27 ruling that local means the whole metro. "Local means where a thing is, not who may see it" (2026-09-30) stands: a Page's own settings still decide who may open it.

**Why order, not distance.** Adjacency is a count of towns crossed, computed once from TIGER Place polygons (`ST_Touches`, county remainders as the glue), never a mile. It never shows, so the no-distance ruling holds and no surface needs a radius. Dense places fill their first bands and never reach the far ones; sparse places run through the bands at once and stop at the market edge, because the scope is the whole market and the order does the rest (`planning/research/rings-stress-test-2026-10-11.md`). No density band, no floor logic.

**Why the hood band is empty in beta.** Signup collects legal name, email and zip (F081); no member has a neighbourhood, and a zip does not reliably give one. The slot stays so a Page's neighbourhood and a later member choice land in it without reordering anything.

**Precedents.** Nextdoor: own neighbourhood first, then "Nearby Neighborhoods", no miles; Craigslist: one region, nothing outside it; Yelp orders by a typed location's vicinity but shows miles, which is the part we refuse. Conflict: Nextdoor's unit is the neighbourhood, Craigslist's the region; the market is the scope and the hood the first band, so both fit.

[platform none]
