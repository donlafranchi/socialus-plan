# What a map is for

**A map earns its place when someone is weighing several places at once and where they are matters to the choice. When the place is already chosen, the phone's maps app does the job better, and a Directions link is all we need. Route planning across errands belongs to Google and Apple Maps, not to us.**

**Your call:** what the map is in v1. A, B or C below. **Recommended: A**, the map stays on request as it is today, Directions hands off to the phone, and we build nothing new for maps before beta data says otherwise.

Research only: no rulings and no code. Path: new territory, because it touches the no-distance ruling and what Explore is.

## The picture

People open a map for one of three jobs:

1. **Choose:** "which of these, given where they are?" Lunch spots, tonight's events, a hardware store. This is your second case, and it is the most common.
2. **Get there:** "how do I reach this one place?" Directions. Everyone hands this to Google or Apple Maps, even Yelp and Airbnb.
3. **Sense the area:** "what's around here, is anything going on?" Exploring, travelling, judging how busy a place is. This is Discover's job, not Find's.

Your first case, **route planning across errands**, is a fourth job. Hardly any discovery app does it; people do it in Google Maps after choosing.

SocialUs today does 1 on request, does 2 by hand-off, and does a little of 3 (the area discs). That is the right shape. The open question is how much to spend on the map, not whether to rebuild it.

## 1. Why people use maps

**Your two cases are real, and choosing among options is by far the more common. There are four more worth naming: exploring an unfamiliar area, sensing whether anything is going on, finding someone who moves, and travelling. Meeting halfway, parking and multi-stop routes are niche, and the big maps apps already own them.**

<details><summary>Each use, how common it is, who does it best</summary>

Hard usage numbers are scarce. Yelp, Zillow and Airbnb don't publish their list-vs-map split, and no Baymard or Nielsen Norman study turned up in this search. What follows is inferred from how each product is built, which reflects their own data.

| Use | How common | Who does it best | Fits SocialUs? |
|---|---|---|---|
| **Choose among options by where they are** (your lunch case) | Very common: the main reason a search result has a map at all | Yelp, Google Maps, Airbnb, Zillow | Yes, on Find |
| **Get directions to the one I picked** | Universal, but it happens in the maps app | Google Maps, Apple Maps; everyone else hands off | Yes, by hand-off (built) |
| **Explore an unfamiliar area / travelling** | Common for travellers, rare at home | Airbnb, Google Maps "Explore", Apple Maps Guides | Yes, through the vantage (typing another town) |
| **"Is anything going on around me?"** (density, liveliness) | Occasional; strongest for events and nightlife | Snap Map heat, Google Maps "busy" areas, Eventbrite's map | Discover, later |
| **Clustering by neighbourhood** ("all of Midtown's stuff") | Common for housing and travel, less for daily errands | Zillow, Airbnb, Redfin | Partly: our area discs already do this |
| **Find someone who moves** (food truck, market stall, pop-up) | Small but important to locals | Instagram stories, Street Food Finder, market sites | Yes: a Page's where-and-when list with Directions (built) |
| **Route planning across several stops** (your errands case) | Real, but done after choosing, in the maps app | Google Maps (about 10 stops), Wanderlog, Circuit | No. Hand-off at most |
| **Meet halfway** | Niche; apps for it stay small | Standalone "meet in the middle" sites | No |
| **Transit and parking** | Tied to the trip, not the choice | Google Maps, Apple Maps, SpotHero | No: the maps app knows it |
| **Trails and outdoor routes** | The map is the product | AllTrails, Strava | No |

**Why route planning rarely sits inside discovery apps:** ordering stops needs roads, traffic, opening hours and turn-by-turn, which only the maps apps have. Discovery apps help you pick the stops, then hand them over. Google Maps accepts several stops in one link; Apple Maps' links take one destination, so a multi-stop hand-off works well only to Google.

</details>

## 2. How established apps use the map

**Nearly every discovery app is list-first with a map one tap away, and every one of them hands directions to Google or Apple Maps. The map is the main screen only where where-it-is is the product: homes, trails, stays. Event and community apps lean hardest on the list.**

<details><summary>App by app</summary>

| App | Map's role | Directions |
|---|---|---|
| [Yelp](https://www.yelp.com) | List first on phone with a Map toggle; list and map side by side on desktop; each business page has a small map | Hands off to Maps |
| [Google Maps](https://maps.google.com) | The map is primary; a search shows a sheet of results over it; saved Lists let you collect places for a trip | Its own |
| [Airbnb](https://www.airbnb.com) | List and map side by side on desktop; map toggle on phone. In 2022 the map grew to about [40% of the screen](https://techcrunch.com/?p=906056). Airbnb ranks map pins differently from the list, because on a map attention doesn't fall off by position ([Airbnb engineering](https://techscoop.substack.com/p/how-airbnb-made-map-search-smarter)). Approximate area until booking | Hands off after booking |
| [Zillow](https://www.zillow.com) | Map is primary, list beside it; draw-your-own-area search | Hands off |
| [Eventbrite](https://www.eventbrite.com) | List first; map beside results on desktop web; per-event map | Hands off |
| [Meetup](https://www.meetup.com) | List of events by date; per-event location and map | Hands off |
| [Facebook Events](https://www.facebook.com/events) | List and feed; per-event map. Facebook [removed the map from Nearby Friends](https://techcrunch.com/2016/12/22/facebook-wave/) in 2016, keeping only neighbourhood-level location | Hands off |
| [Nextdoor](https://nextdoor.com) | Feed first; maps show your neighbourhood's boundary, not live items | Hands off |
| [Apple Maps Guides](https://support.apple.com/guide/iphone/use-guides-iph9f5a0e7c9/ios) | Curated lists of places shown on the map: the "saved list on a map" pattern | Its own |
| [AllTrails](https://www.alltrails.com) | Map is primary: the trail is the product | Its own, plus hand-off to the trailhead |

**Pattern:** where the item *is* a place to go once (a restaurant, a stay, a home), the map sits beside the list. Where the item is a time (an event, a post), the list leads and the map lives on the item. SocialUs is mostly the second kind.

**Small evidence on list vs map:** one [independent user study](https://medium.com/theuxblog/interactive-prototype-user-study-maps-vs-lists-c551edeccf68) found people preferred a plain list over a map for the same tasks, because the map shows more and is harder to scan. It is anecdotal, but it matches what the big apps chose.

</details>

## 3. What we have today

**The Explore map is built, on request only ("Show on map" since 2026-10-31), with pins for exact addresses and soft discs for areas. Pages show a small static map with a Directions link to the phone's maps app. No distance is shown anywhere. Keeping it costs a map provider bill once traffic grows and steady test and design upkeep.**

<details><summary>What it does</summary>

- **Explore:** a list; "Show on map" opens the map (post kinds change, 2026-10-31). Ruling from 2026-10-01 put list and map side by side at desktop width; the newer "map on request" change supersedes that in practice, and the record should say so.
- **What's on the map:** a tunable mix of upcoming events, new Pages, recently active Pages and curated picks (2026-10-05, revisit with beta data by 2026-11-15). Online items never appear. Signed out, no map at all.
- **Pins and discs (2026-10-07):** an exact public address is a teardrop pin; a place known only to its neighbourhood or town is a translucent disc with a count. The map's stated purpose in that ruling: "is anything going on around me", not precise location.
- **On a Page:** a readable static street map; tapping it opens our own map; **Directions** opens Apple Maps on iPhone and Google Maps elsewhere. Areas show a line of text, no pin. Pop-ups and market stalls show a where-and-when list, each stop with Directions. Page cards carry a Directions icon.
- **Privacy:** in public, location is coarse (2026-10-25); a member's precise location is never shown to another member.

</details>

<details><summary>The rulings that bound it</summary>

- **No distance is shown anywhere** (2026-09-30), and **no driving time is planned** unless members ask (2026-10-25, on F109). So "12 min away" is not allowed today; cards say the town ("in Folsom"), ordered nearest town first.
- **The only path to "how far is it" is the hand-off** to the phone's maps app (2026-09-03). That ruling calls the hand-off load-bearing.
- **Local is never a distance, a map or a metro** [always] (2026-10-16).
- **Find vs Discover** [always] (2026-10-12): Find is the tool, Discover is the fun. Explore is Find, "the tool, list and map" (2026-10-25).
- **A full-screen map as a destination** is deferred (surfaces doc).

</details>

<details><summary>What it costs to keep</summary>

- **Money:** the Explore map uses Mapbox; Mapbox's free web tier covers roughly the first 50,000 map loads a month, then charges per thousand ([pricing](https://www.mapbox.com/pricing); not re-checked today). "On request" keeps loads low; a map shown by default would multiply them. The Page map is a static image, which is cheaper.
- **Upkeep:** about 900 lines of map code across seven components, plus open checks on the list/map switch (F044, F059). Every new item type (post kinds, pop-up stops, areas) has to be taught to the map, and every privacy rule has to hold on it too.
- **Design weight:** pins, discs, clusters and the map mix are each a ruling someone has to tend.

</details>

## 4. Fit for SocialUs

**The map earns its place in three cases: choosing among nearby options on Find, a traveller looking from another town, and finding a Page that moves. Everywhere else a list naming the town plus a Directions link is better. Route planning is out of scope for v1.**

<details><summary>Where the map earns its place</summary>

- **Choosing on Find:** "coffee near me", "what's on tonight". The member compares a handful of options and where they are is part of the choice. The town name on each card answers most of it; the map answers the rest for people who think spatially.
- **A traveller's vantage:** someone looking from South Lake Tahoe doesn't know the towns' names, so "in Meyers" means nothing; a map does. This is the strongest argument for keeping the map, and it grows with each new market.
- **Pages that move:** a food truck or market stall's where-and-when list, each stop with Directions. Already built.
- **Later, on Discover:** "is anything going on" as a soft view of tonight's events by area. Fun, not a tool, and not needed for beta.

</details>

<details><summary>Where a list or a hand-off is better</summary>

- **Locals at home:** they know Folsom from Fair Oaks. "In Folsom", ordered nearest town first, does the job with less to scan.
- **Events and posts:** the time matters more than the place; the list by date leads, the place is one line on the card.
- **"How far is it?":** Directions to Google or Apple Maps. They know roads, traffic and parking; we would only be guessing. "12 min away" would read well, but it needs your ruling to reopen the no-distance and no-driving-time calls, and a routing service to compute it.
- **Meeting in person:** once two members agree on a place, the Page's address and Directions are all they need. Meeting halfway is out.

</details>

<details><summary>Is route planning in scope?</summary>

No, for v1. Ordering errand stops needs road and traffic data only the maps apps have, and no discovery app we looked at does it itself. The cheap version, if members ask: a member's saved Pages ("my errands Saturday") sent to Google Maps as one multi-stop route. Apple Maps links take one stop, so it would work best on Google. That is a feature for after beta, if at all.

Your "knowing where to find someone" case is covered: a Page's address or where-and-when list, then Directions. We don't need to provide the directions map ourselves, and the precedents say we shouldn't.

</details>

## 5. Options for the v1 map

**A keeps what's built and spends nothing new. B cuts the Explore map to save upkeep, at the cost of travellers. C makes the map a Discover feature and adds an errands hand-off, which is more to build before beta. Recommended: A.**

- **A. Keep the map on request, hand off Directions, build nothing new (recommended).** It matches Yelp and Eventbrite, keeps the traveller case, costs little because few people load it, and beta data can tell us whether anyone taps "Show on map".
- **B. Drop the Explore map; keep only the Page's static map and Directions.** Least upkeep and no map bill, but a traveller loses the one view that makes unfamiliar towns readable, and we'd likely rebuild it for new markets.
- **C. Push the map forward: a "what's on tonight" map on Discover, plus "send my saved places to Google Maps" for errands.** Closest to your route-planning idea, but it is new building before beta, the route works well only on Google, and Discover's design isn't settled.

<details><summary>What A asks of agents (no new rulings)</summary>

- Count "Show on map" taps and Directions taps per day, no member id, alongside the map mix count, so the 2026-11-15 map-mix review also answers "does anyone use the map?"
- Update the 2026-10-01 list-and-map-by-width ruling's record to say map-on-request replaced the side-by-side layout, so the two don't conflict.
- Leave route planning, minutes away and a Discover map in Considering until members ask.

</details>
