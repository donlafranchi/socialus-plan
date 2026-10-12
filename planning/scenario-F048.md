---
id: F048
title: A member gets the address, not the mileage
status: draft
horizon: later
rank: 110
date: 2026-09-10
depends: []
---
## Story

A newcomer to Sacramento set her home to Oak Park. Scrolling the feed Tuesday evening, she finds Thursday's run at Drake's. The card tells her "2.3 mi" — measured from a centroid she never chose, to a venue whose coordinates are approximate. It answers nothing. Instead: no mileage anywhere. The venue's real address sits on the item page, actionable — a tap opens her phone's map app with the address as destination; on the web it's a copyable string.

## Acceptance

1. No distance number ("2.3 mi", "within 5 miles") renders anywhere in the app.
2. The filter sheet has no distance/radius control; an old `?distance=` link loads without error and drops the parameter.
3. An item's address opens the device's map app on tap (mobile) or is copyable (web).
4. An item with an Online location shows no address and no map pin.

## Not this

Ranking by the place hierarchy (a later scenario) — this only removes distance, it doesn't install the replacement. Whether the `sort` control's other options survive is undecided.

## Rulings
- **2026-09-30 — "Near you", "Browse nearby" and "mi away" come out. "In Sacramento" stands in until there is a second metro.** Don, answering F094. Placeholder until then ([public-is-draft]); `voice.md`'s samples follow. The app strings are a separate ticket. [binds tiers=planning,code surfaces=copy,explore,venue]
- **2026-09-30 — No distance is shown anywhere.** Don, on F094. The venue page's "X mi away" goes, with nothing in its place. **A Page has a location, or says where it usually shows up** (which farmers market, say). **A Page with no address is in the Pages directory and not on the map.** [for now] [binds tiers=planning,code surfaces=venue,map,pages]
- **2026-09-30 — There is no "near you" while there is one metro. Nearness is deferred until there is critical mass.** Don, on F094. [binds tiers=planning,code surfaces=copy,explore]
