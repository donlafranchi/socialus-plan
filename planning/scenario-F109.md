---
id: F109
title: Explore shows the top results per category, nearest first by rings, each card naming its town
status: draft
date: 2026-10-11
depends: [F104, F105, F107]
---
## Story

Marcus lives in Granite Bay. He searches coffee and sees ten cafes: Granite Bay's first, then Roseville's and Folsom's, then Auburn's to fill the ten. Each card says its town ("in Folsom") and nothing says how far it is. He searches hardware and sees five stores. He searches a home builder and sees the first twenty of the market, in ring order. Dana lives in a thin foothill town with no cafe; she still sees ten, from the nearest towns outward, not an empty page.

## Acceptance

1. **One question, one answer.** Explore, Home and search ask a single function, top(vantage, category), for the N results of a category, in F104's ring order: hood, then town, then market by town adjacency, then online. No surface decides N or order on its own.
2. **N lives in a config table.** One row per category and one default row. Starting guesses: 10 coffee, 20 restaurants, 5 hardware, and the default row for the rest. Changing a row changes behaviour with no deploy. Every starting value is marked "guess".
3. **Nearest first, by rings.** The N are the first N in ring order, so a thin town fills from the next towns outward. The page is not empty while the market holds a match. Past the market stays a later, labelled section.
4. **Each card shows its town** ("in Folsom"). No miles, minutes or hop count appears on any surface (2026-09-30 stands).
5. **The measure can change without the callers changing.** What "nearest" means sits inside top() and its own scenario; inputs and the output shape stay as they are.
6. **One event is logged when a member opens a Page from Explore:** the member id, the member's home town, the Page's town, the category and the rank in the list. Staff-side only: no member sees it, it is never shown member to member, and no coordinates or device location are stored. A member can opt out easily from You, and an opted-out member is not logged.
7. **Logged counts reach a person, not the table.** A staff report shows, per category, how many results members actually open past. Every count shows, however small; a low count carries "few opens, still a guess". Staff metrics carry no small-count suppression (DECISIONS 2026-10-09). A person edits the rows; nothing retunes itself (Next: tune N from the log).
8. **Top-N applies to the default vantage, the three rings.** A searched named place uses its own area type (F107), not top-N: Napa the town and Napa County are searched as what they are.

## Not this

Showing distance or time anywhere. Routing, isochrones or density tiers. A neighbouring-market section. N set per member. A config editor in the app: the operator edits rows. Self-tuning. Top-N on a searched place (F107 owns that). Changing the order inside a ring (F059 criterion 3).

## Why

- **Lives somewhere better?** Partly: Yelp and Google show a ranked list with distance; ours is a short list per kind of thing, each card naming its town, with no distance.
- **Only locals know?** Yes: how many coffee shops is the right list, and where the next town's ones start, is learned from where members go.
- **Gets people together?** Yes: a short list in the nearest towns is what a finder will actually go to.
- **Stays fresh on its own?** Mostly: rings change only when boundaries do; N is a handful of rows reviewed against the log.
- **Who keeps it current?** The operator, from the report, a few rows a quarter.
- **Better as more people join?** Yes: the starting guesses harden into observed numbers as opens accumulate.

**Path: new territory, ruled** (the PM, 2026-10-12, A: top-N per category, replacing the earlier depth-by-bands design). It logs member behaviour, which touches privacy and member trust; the PM ruled the log with the member id, staff-side, for members, with an easy opt-out ("We are tracking, just not for shareholder benefit"), consistent with the 2026-10-11 data ruling. Precedents: [Walk Score](https://www.walkscore.com/methodology.shtml) counts categories separately; Yelp and Google list nearest first and show distance, which 2026-09-30 refuses.

**Next:** tune N per category from the log; a person edits the rows.

[open-question owner=don raised=2026-10-12] Later: show driving time on each card once a routing service exists (OpenStreetMap with Valhalla or OpenRouteService), only if the 2026-09-30 no-distance ruling is lifted at that point. A) lift it then, for driving time only. B) keep no distance anywhere. Recommend B until a member asks for it.

[platform none]
