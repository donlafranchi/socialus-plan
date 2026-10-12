---
id: F109
title: Explore reaches as far as each kind of thing is worth the trip, set in one table and tuned by where members go
status: draft
date: 2026-10-11
depends: [F104, F105, F107]
---
## Story

Marcus lives in Granite Bay. He searches coffee: Granite Bay, Roseville and Folsom, and it stops there; Auburn's cafes are not in the list. He searches a home builder: the whole market, in order. Dana lives in a thin foothill town with no cafe. She searches coffee and sees one labelled section, "Further out", with the nearest ones, not an empty page. Nothing says how far anything is.

## Acceptance

1. **One question, one answer.** Explore, Home and search ask a single function, reach(vantage, category), for how far a category goes. It returns F104's bands in order, with a flag on the ones that fall under "Further out". No surface decides reach on its own.
2. **A config table holds the numbers.** One row per category and one default row: how many bands deep results show, the fewest results wanted, and a ceiling. Changing a row changes behaviour with no deploy. Every starting value is marked "guess" in the row.
3. **Depth is counted in F104's bands, never shown.** No miles, minutes or hop count on any surface (2026-09-30 stands).
4. **Too few inside the depth: the next bands appear under "Further out".** The page is never empty while the market holds any match. Nothing widens silently. Past the market stays a later, labelled section.
5. **Uncapped categories show the whole market in order** (builders, contractors and other made-to-order work are the starting guess).
6. **The measure can change without the callers changing.** Swapping adjacency for travel-time bands later is a change inside reach() and its own scenario; the inputs and the shape of the output stay as they are.
7. **One event is logged when a member opens a Page from Explore:** the member's home town, the Page's town, the category and the band depth between them. Towns and a number only: no member id, no coordinates, no vantage (F105 criterion 3 stands), no device location.
8. **Logged counts reach a person, not the table.** An operator-only report shows, per category, the depth that covers most observed opens. Every count shows, however small; a low count carries the marker "few opens, still a guess". Nothing is hidden below a minimum: staff metrics get no small-count suppression (DECISIONS 2026-10-09: privacy has two levels, strict member to member, staff get the data they need under roles and permissions), and a row holds towns and a number, no member id. A person edits the row. Nothing retunes itself.
9. **reach() applies to the default vantage, the three rings.** When a member searches a named place, results use that place's own area type (F107), not reach depth: Napa the town and Napa County are searched as what they are, with no "Further out" section.

## Not this

Showing distance or time anywhere. Routing, isochrones or density tiers (F104 ruled no density band; travel time is the next scenario, behind the same function). A neighbouring-market section. Reach set per member. A config editor in the app: rows are edited by the operator. Self-tuning. Reach depth on a searched place (F107 owns that). Changing the order inside a band (F059 criterion 3).

## Why

- **Lives somewhere better?** No: Yelp and Google show everything within a radius; what is worth the trip for each kind of thing, learned from the people who live there, is nowhere else.
- **Only locals know?** Yes: a cafe is a ten minute question and a builder is a fifty minute one, and the foothills and the valley answer both differently.
- **Gets people together?** Yes: what shows first is what a finder will actually go to.
- **Stays fresh on its own?** Mostly: adjacency changes only when boundaries do; the table is a handful of rows reviewed against the report.
- **Who keeps it current?** The operator, from a report, a few rows a quarter; nobody edits a boundary.
- **Better as more people join?** Yes: the first guesses harden into observed depths as opens accumulate.

**Path: new territory.** It narrows F104's "the scope is the whole market" for categories with a depth, and it logs member behaviour, which touches privacy and member trust. A/B/C below.

**Why bands now, minutes later.** F104's order is already a count of towns crossed, so the first version needs no routing. When it is wrong (mountains, lakes, a freeway that makes a far town near), the fix is a better measure inside reach(), with free inputs: OpenStreetMap roads with Valhalla or OpenRouteService for travel-time areas, Overture or OSM places to count supply per category, Census population for density, H3 cells to precompute [A: none verified for this stack]. The config table and the log do not change.

**Precedents.** [Walk Score](https://www.walkscore.com/methodology.shtml) weights amenities by travel time and counts categories separately; [USDA Food Access Research Atlas](https://www.ers.usda.gov/data-products/food-access-research-atlas/) uses different distance standards for urban and rural tracts; Yelp and Google rank by distance within a radius and show it. Conflict: all three show miles or minutes, which 2026-09-30 refuses; bands carry the same idea unseen.

[open-question owner=don raised=2026-10-11] Do we log town pairs from beta day one? A) **Log from day one: home town, Page town, category, band depth, no member id** (recommended: the table has nothing to learn from until it runs; no personal data in the row). B) Log nothing until after beta: safest, but the first quarter of learning is lost. C) Log with a member id so reach can be per member: richer, and the kind of tracking the platform refuses.

[platform none]
