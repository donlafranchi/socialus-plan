---
id: F105
title: A member looks from a typed place, and home stays the default
status: approved
horizon: next
rank: 20
date: 2026-10-11
depends: [F104]
approved: 2026-10-11 — the PM: the rings are a starting point, not a fence; the vantage is session state; a waiting market shows what is waiting, never hidden Pages.
---
## Story

Marcus is driving to Davis on Saturday. On Explore he types Davis into the place control, and Explore and Home re-centre: Davis first, then Woodland and Dixon, the rest of the Sacramento market after. He types South Lake Tahoe: Tahoe is waiting, so he sees how many are waiting there and how to be told when it opens, and no Pages. He closes the app. Next time, it opens on Granite Bay again, and nothing remembers that he looked.

## Acceptance

1. **The place control on Explore (today's area pill) accepts a typed place:** any town, county or market in the place tree, with suggestions as the member types. It shows the vantage's name, the home town by default. The search box stays "what"; the place control is "where".
2. **Choosing a place sets the vantage for the session, and a place is taken as the area type it is** (F107). A town or neighbourhood re-centres Explore and Home on it: the rings rebuild there (hood none, town the typed town, market its market) in F104's order. A county or market is looked at as that area, with no town band.
3. **Nothing about the member changes.** The vantage is session state: never written to the member row, never logged, never derived from IP or GPS. A new session opens at home. A shared link reopens the same vantage and search (F059 criterion 10), which is the URL, not storage.
4. **A vantage in a waiting market shows that market's cached waiting count and the tell-me-when-it-opens control** (F076 criteria 7 and 13), and no Pages or posts. A vantage in another open market shows that market in full.
5. **A visitor with no location is prompted to enter a location or choose a market, with an arrow pointing to the market selector.** Nothing is picked for them, whether one market is open or several.

## Not this

Saved places, a travel plan, or remembering the last vantage across sessions. A map that follows the device's location. Changing where a Page's give-back goes or whether it is local: both read the seller's town, never the viewer's vantage (F106). A list of markets to browse.

## Why

- **Lives somewhere better?** Partly: Yelp and Google Maps search "near" a typed place, but neither shows what only locals list.
- **Only locals know?** Yes, once the vantage is there: a visitor to Tahoe sees what Tahoe's makers listed.
- **Gets people together?** Yes: a day trip finds the market day and the pop-up where the member is actually going.
- **Stays fresh on its own?** Yes: it stores nothing, so nothing goes stale.
- **Who keeps it current?** Nobody; the place tree is the only input.
- **Better as more people join?** Yes: every opened market is one more place worth looking from.

**Path: new territory, ruled** (the PM, 2026-10-11: the rings are a starting point, not a fence). Answers `socialus-web` #588 (a visitor with no metro): with one open market it is the default; with more than one the visitor is asked, since the platform never picks from IP (F076 criterion 2, F081 criterion 3). The metro switcher and `MarketSelector` are replaced by the place control; the 2026-10-05 cut of "metro memory" stands, since nothing is remembered. `product/foundation/nouns.md` § Vantage.

**Precedents.** Yelp and Google Maps: a typed "near" place beside the search, current location as the default; Airbnb and Eventbrite put "Where" beside "What"; Nextdoor locks a member to home and shows nothing else. Conflict: Nextdoor's lock is right for money and wrong for looking; the vantage follows Yelp for looking and Nextdoor for home.

[platform none]

## Rulings
- **2026-10-12 — A visitor with no location is prompted to enter a location or choose a market, with an arrow pointing to the market selector.** The PM, 2026-10-12, answering the visitor-with-no-vantage question in plan #698/#699. Because nothing is picked silently (F103 criterion 3). [for now] [replaces none] [binds tiers=planning,code surfaces=explore,home,onboarding build=none]
