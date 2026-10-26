# Market resolution: which market does a town belong to? (2026-10-26)

**As of 2026-10-26** · Source: hand-written, research only · Path: well-worn for the method, new territory for Sacramento's reach (A/B/C below) · Maintained by: hand (the owner confirms on next edit)

**Bottom line: a sign-up never resolves a zip on the fly. A script assigns every town once, ahead of time: if it is within 60 minutes' drive of a market's hub, it goes to the nearest one; beyond that, it goes to a waiting region seeded by the government's commuting zones; regions under about 100,000 people merge with their nearest neighbour; and a short hand-written list (the Tahoe basin) overrides it. The result is stored in the market tables that already exist, so tens of thousands of zips collapse to a few hundred county subdivisions per state, which a person can check in one sitting. At sign-up the person sees their market and may pick another one within 75 minutes, and they count where they pick.**

**Don's one call:** how far the open Sacramento market reaches. **A (recommended):** it stays as ruled, and people in Vacaville, Yuba City, Lodi or Grass Valley may choose Sacramento at sign-up. **B:** it grows to everything within 60 minutes. **C:** it stays as ruled with no choosing in. Details in § 5.

Method: drive times are from OSRM (the free, open-source router behind many map apps), car profile, free-flow with no traffic, from downtown to downtown, pulled from OSRM's public demo server on 2026-10-26. Real Friday-evening times on I-80 and US-50 run longer. **V** = seen on 2026-10-26; **A** = from memory or estimated, not checked this session.

---

## 1. The ways to draw a market

**No method is right on its own. Drive time fits "local" best but needs hubs chosen first; the commuting zone is the best free, ready-made grouping but works in whole counties, so it cannot split the Tahoe basin from the foothills. Licensed TV markets (DMAs) cost money and draw for TV, not neighbours. The well-worn answer, used by Craigslist and by the federal statisticians themselves, is a blend: a grouping as the base, a person's judgment on the edges.**

| Method | Fits "local" | Upkeep | Where it breaks | Cost |
|---|---|---|---|---|
| Nearest hub by drive time, with a cap | best: it is how people actually travel | rerun when a hub is added | needs hubs chosen first; ties near the midpoint; mountain roads (Tahoe) | free (OSRM) |
| Drive-time Voronoi (every point to its nearest hub, no cap) | good near hubs, bad far away | same | with no cap, Bishop "belongs" to Carson City, 3¾ hours away | free |
| USDA ERS 2020 commuting zones | good: built from where people commute for work | the government updates it each Census | whole counties only: puts Placerville and South Lake Tahoe in **Reno**, and Chico in **Redding** | free (V) |
| ERS labor market areas | commuting zones merged until each has 100,000 people | same | the same county problem; the 100,000 floor is the useful idea | free (A) |
| Census metro areas (CBSA) and combined areas (CSA) | weak: built for statistics; Don retired them for members (2026-10-16) | yearly OMB updates | the combined Sacramento area takes in Truckee; the Bay Area's takes in Stockton and Modesto | free (A) |
| Nielsen TV markets (DMAs) | weak: drawn for TV signals and ad sales | Nielsen updates yearly | Sacramento's TV market runs from Modesto to Truckee | **licensed**: a paid Nielsen licence to use the boundaries (A) |
| Whole counties | weak in the mountains | none | El Dorado County runs from El Dorado Hills to South Lake Tahoe; Placer from Roseville to Tahoe City | free; what the code does today for waiting markets |
| HUD zip→county crosswalk | a lookup, not a method | quarterly | useful for PO-box zips the Census doesn't map | free, with a free sign-up token (A) |
| State lines | none | none | splits Lake Tahoe down the middle; F103 already ruled a market may cross a state line | free |

<details><summary>How others define regions (precedents)</summary>

- **Craigslist** ([sites list](https://www.craigslist.org/about/sites), V): hand-drawn regions named by people, not data. Northern California and Nevada: sacramento, sfbay, **reno / tahoe**, **gold country**, humboldt county, mendocino county, **yuba-sutter**, chico, redding, stockton, modesto, susanville, klamath falls, elko. You post to one site; you may browse any. Closest precedent to what we need, and it puts Tahoe with Reno.
- **ERS commuting zones** ([ERS](https://www.ers.usda.gov/data-products/commuting-zones-and-labor-market-areas), V): 598 zones covering every county, contiguous, rebuilt from 2020 commuting data. The 2020 assignments for this area are listed in § 2.
- **Nextdoor** ([help](https://help.nextdoor.com/), A): your verified address puts you in one hand-drawn neighbourhood and you can't change it; a neighbourhood launches once enough founding members join. Locks home, which is right for money and wrong for looking (already noted in `product/systems/places.md`).
- **Uber and Lyft** ([Uber cities](https://www.uber.com/global/en/cities/), [Lyft cities](https://www.lyft.com/rider/cities), A): a market is an operations zone drawn by hand; riders are never assigned, the phone's location decides. Drivers sign up to one market.
- **Eventbrite** (A): no assignment at all; city pages ("events in Sacramento") plus a location you can change and a distance.
- **Patch** ([Patch California](https://patch.com/california), A): one site per town; a reader follows as many towns as they like and gets one email.
- **Meetup and Facebook Marketplace** (A): a location plus a radius the person picks.

</details>

## 2. Fifteen towns that don't fit neatly

**Drive time and commuting zones agree on most towns. They disagree in four places, and in each the drive time is closer to how people live: Placerville (commuting zone says Reno), Chico (says Redding), Fairfield and Vacaville (the Bay Area or Sacramento, a near tie), and South Lake Tahoe (Carson City 49 minutes, Truckee 74). Bishop and Crescent City are too far from anything to belong to a market and become waiting regions of their own.**

Hubs below are each market's downtown; Tahoe's is Tahoe City, the middle of the lake. Minutes are OSRM free-flow (V on the demo server; real times longer). "Rec" is the outcome under the recommended rule and option A.

| Town | Nearest hubs (minutes) | Commuting zone 2020 | Metro (CBSA / CSA) | Craigslist | Rec |
|---|---|---|---|---|---|
| Arcata / Eureka | Eureka 14; Redding 166; Santa Rosa 282; Sacramento 343 | Eureka | Eureka-Arcata (A) | humboldt county | **Humboldt** (waiting) |
| South Lake Tahoe | Carson City 49; Tahoe City 53; Truckee 74; Reno 88; Sacramento 137 | Reno | Sacramento metro (A) | reno / tahoe | **Lake Tahoe** (ruled); may choose Reno–Carson |
| Truckee | Tahoe City 23; Reno 40; Carson 72; Sacramento 119 | Sacramento | Truckee-Grass Valley, in Sacramento's combined area (A) | reno / tahoe (A) | **Lake Tahoe**; may choose Reno–Carson |
| Grass Valley / Nevada City | Sacramento 75; Truckee 73; Chico 97 | Sacramento | as Truckee | gold country (A) | waiting **Nevada County foothills**; may choose Sacramento |
| Placerville | Sacramento 55; Tahoe 84 (S. Lake) | **Reno** | Sacramento metro | gold country (A) | **Sacramento** (already ruled) |
| Stockton | Stockton 0; Modesto 40; Sacramento 57 | Stockton | Stockton, in the Bay Area's combined area (A) | stockton | **Stockton–Modesto** (waiting) |
| Lodi | Stockton 21; Sacramento 46 | Stockton | as Stockton | stockton (A) | **Stockton–Modesto**; may choose Sacramento |
| Vacaville | Sacramento 43; Oakland 60; SF 69 | San Francisco–Oakland | Vallejo, in the Bay Area's combined area (A) | sfbay (A) | waiting **Solano**; may choose Sacramento |
| Fairfield | Oakland 52; Sacramento 53; SF 61 | San Francisco–Oakland | as Vacaville | sfbay (A) | waiting **Solano**; may choose Bay Area or Sacramento |
| Napa | Oakland 55; Santa Rosa 58; SF 64; Sacramento 74 | San Francisco–Oakland | Napa, in the Bay Area's (A) | sfbay (A) | **Bay Area** (North Bay when it splits) |
| Chico / Oroville | Chico 0 / 30; Redding 91 / 114; Sacramento 109 / 83 | **Redding** | Chico (A) | chico | **Chico** (waiting) |
| Yuba City | Sacramento 53; Chico 63 | Sacramento | Yuba City, in Sacramento's (A) | yuba-sutter | waiting **Yuba–Sutter**; may choose Sacramento |
| Jackson (Amador) | Stockton 67; Sacramento 73 | Stockton | none (A) | gold country (A) | waiting **Mother Lode**; may choose Stockton–Modesto or Sacramento |
| Sonora | Modesto 74; Stockton 88; Sacramento 140 | Stockton | Sonora (A) | gold country (A) | waiting **Mother Lode**; may choose Stockton–Modesto |
| Ukiah | Santa Rosa 75; SF 146; Sacramento 177 | Ukiah | Ukiah (A) | mendocino county | **Mendocino–Lake** (waiting) |
| Modesto | Modesto 0; Stockton 38; Sacramento 91 | Stockton | Modesto (A) | modesto | **Stockton–Modesto** (waiting) |
| Crescent City | Eureka 111; Redding 258 | Crescent City | Crescent City (A) | humboldt (A) | **Humboldt** (Del Norte is too small alone, so it merges) |
| Bishop | Carson City 224; S. Lake Tahoe 236; Reno 262 | **Bakersfield** | Bishop (A) | none nearby (A) | waiting **Eastern Sierra**, remote; may choose any market |

<details><summary>2020 commuting zones for Northern California and Nevada (V, from the ERS file)</summary>

- **Sacramento:** Sacramento, Yolo, Placer, Nevada, Sutter, Yuba, Colusa
- **Reno:** Washoe, Carson City, Douglas, Lyon, Storey, Churchill, Mineral, **El Dorado**, Alpine
- **San Francisco–Oakland:** San Francisco, Alameda, Contra Costa, Marin, San Mateo, **Solano, Napa**, Sonoma
- **San Jose:** Santa Clara, Santa Cruz, Monterey, San Benito
- **Stockton:** San Joaquin, Stanislaus, Merced, Amador, Calaveras, Tuolumne
- **Redding:** Shasta, **Butte**, Tehama, Glenn, Trinity
- **Eureka:** Humboldt · **Crescent City:** Del Norte · **Ukiah:** Mendocino, Lake · **Susanville:** Lassen, Plumas, Sierra
- **Bakersfield:** Kern, **Inyo, Mono** · **Klamath Falls (OR):** Siskiyou, Modoc · **Elko:** Elko and five rural Nevada counties

El Dorado in Reno, Butte in Redding and Inyo in Bakersfield are the three that a drive-time check overturns.

</details>

<details><summary>More towns checked (OSRM minutes)</summary>

| Town | Minutes | Rec |
|---|---|---|
| Incline Village, NV | Tahoe City 33; Carson 41; Reno 56 | Lake Tahoe |
| Gardnerville, NV | Carson 26; Reno 64; Tahoe City 85 | Reno–Carson |
| Susanville | Reno 104; Chico 140; Redding 142 | Susanville area is ~56,000 people, so it merges with its nearest region, Reno–Carson |
| Colusa | Chico 69; Sacramento 80 | merges with Chico |
| San Andreas | Stockton 71; Modesto 95; Sacramento 97 | Mother Lode |
| Merced | Modesto 49; Stockton 84 | Stockton–Modesto |
| Fort Bragg | Sacramento 256 (coast road, nothing closer among hubs) | Mendocino–Lake |
| Davis | Sacramento 21 | Sacramento |

</details>

**On Don's three examples.** Arcata is not Redding's or the Bay Area's: it is 2¾ hours from Redding and every source (commuting zone, Craigslist, metro area) treats Humboldt as its own place. South Lake Tahoe is closer to Carson City (49 minutes) than to Truckee (74), which supports Don's instinct; F103 already ruled the Tahoe basin one market, and the choice at sign-up lets anyone in South Lake who lives toward Carson pick Reno–Carson. Truckee is 23 minutes from Tahoe City and 40 from Reno, so it is Tahoe's, with Reno as its choice.

## 3. The roll-up: tens of thousands of zips to a few dozen markets

**The trick is not to assign zips. Sign-up already asks for the town; a zip only helps find it. Towns sit in county subdivisions (about 400 in California and a few dozen in Nevada, A), and the market tables that already exist (F103) are built from whole counties and county subdivisions. So a script assigns subdivisions, a person reads a few hundred rows, and every zip follows.**

**The rule, in order:**

1. **Hubs.** The largest town in each 2020 commuting zone is a hub, plus any town of 50,000 or more that is over 60 minutes from every other hub (that is how Chico becomes a hub apart from Redding). A market may have more than one hub: Reno and Carson City; Stockton and Modesto; San Francisco, Oakland, San Jose and Santa Rosa. Lake Tahoe's hub, Tahoe City, is by ruling.
2. **Within 60 minutes:** each subdivision goes to the market of its nearest hub. If two hubs from different markets are within 10 minutes of each other, the commuting zone breaks the tie (Fairfield goes to the Bay Area), and the row is flagged for a person to look at.
3. **Beyond 60 minutes:** the subdivisions of one commuting zone that are left over form a waiting region together (Amador, Calaveras and Tuolumne become the Mother Lode).
4. **Too small:** a waiting region under about 100,000 people merges into the nearest region within 2 hours, because 1,000 supporters is 1% of 100,000 people, and the government uses the same 100,000 floor for its labor market areas. Nothing within 2 hours, and it stays a remote region of its own (Bishop).
5. **Overrides** win over all of the above: a short hand-kept list, each line naming its ruling (the Tahoe basin, F103).
6. **An open market's edge moves only by a ruling.** The script proposes; it never moves a town in or out of an open market on its own. A town the rule would add to an open market (Vacaville, Yuba City) instead becomes a waiting region, with the open market offered as its choice (§ 4).

<details><summary>How it is stored and run</summary>

- **No new table.** The script writes `market_members` rows, the table F103.1 already made: a county whole when all its subdivisions agree, a county subdivision row where they don't (El Dorado: the county to Sacramento, the South Lake Tahoe subdivision to Lake Tahoe). A county with no row is still its own waiting market by rule, so the script only ever adds clarity.
- **Overrides** live beside the script as a small text file, one line each with its reason and ruling date.
- **A town to market:** the places table already knows each town's county subdivision; `market_key()` answers.
- **A zip to a town:** the Census ZCTA-to-place relationship file (free), taking the town with the largest share of the zip's people, and the person confirms the town at sign-up. A PO-box zip has no Census area, so it falls back to HUD's zip-to-county crosswalk, or the person just types the town.
- **Each row records how it was placed** (nearest hub, commuting zone, merged, override) and its minutes, so the review is reading a table, not redoing the maths.
- **Reruns** happen when a hub is added or Don rules on an edge, never on a timer. The script's output is a diff a person approves.

</details>

<details><summary>Cost</summary>

- **OSRM is free and open source.** Run it on the Mac from a free OpenStreetMap extract of California and Nevada (Geofabrik): roughly 8–16 GB of memory and half an hour to prepare, then a few hundred subdivisions times a few dozen hubs takes seconds (A). A whole-country run fits on a rented machine for an hour, a few dollars.
- **The public OSRM server** is for light use only; this research used it for about 400 pairs. Bulk runs belong on our own copy.
- **Paid alternatives** (Google Distance Matrix, Mapbox Matrix) charge per pair and add nothing for a one-off precompute.
- **Commuting zones, Census files and HUD's crosswalk are free.** Nielsen's TV markets are the only licensed option, and we don't need them.

</details>

<details><summary>How waiting regions merge and split as they grow</summary>

- **Merge at drawing time only:** the 100,000 floor in step 4. Later merges are a ruling, not a script decision.
- **Split before listing when a region is far bigger than the goal.** The Bay Area has about 7.7 million people (A); 1,000 supporters would open all of it at once from one corner. Split it into the parts Craigslist already uses (San Francisco and the Peninsula, East Bay, South Bay, North Bay) before it appears on the Open page. A rough test: split when each part would itself have over a million people and their hubs are more than 45 minutes apart.
- **An open market never splits on its own:** a split would close part of it. It splits only by a ruling.
- **Lake Tahoe is below the floor** (the basin and Truckee are roughly 60,000 to 70,000 residents, A). It stands by ruling, because visitors and second homes make it a place of its own; it is the one exception to step 4, and it is listed in the overrides.

</details>

## 4. "You choose": the person picks their market

**At sign-up the person sees the market their town resolved to and may pick a different one whose hub is within 75 minutes, at most three choices. They count where they choose. Precedents: Craigslist lets you post where you like; Patch lets you follow several towns; Nextdoor's lock is the one we avoid.**

- **The screen:** their town, the market it resolved to, and up to two nearby alternatives, closest first. A Truckee resident sees Lake Tahoe, with Reno–Carson offered. A Vacaville resident sees Solano, with Sacramento and the Bay Area offered. (The words here are placeholders; the copy is Don's.)
- **Counting:** a person counts once, toward the market they chose; changing their choice moves their count. This fits F118 (a supporter is a member "whose town it is, by zip or by choosing it").
- **Choosing an open market gets the person in now.** A Vacaville resident who picks Sacramento uses the full app today. The cost: their count leaves Solano, so fringe regions fill more slowly. That is the trade in option A.
- **The 75-minute list stops gaming:** nobody in Sacramento can pick Humboldt to push its count.
- **Pages don't choose.** A maker's Page goes to the market its location is in, because Explore is scoped by where things are. Only people choose.
- **Looking elsewhere is not choosing.** Typing South Lake Tahoe to browse for the day is the vantage (F105) and changes nothing about home or counts.
- **Stored as** the chosen market on the member, empty when they kept the resolved one; counts read the choice first.

## 5. Recommendation and Don's call

**Recommended: drive time proposes, commuting zones group the far towns, county subdivisions store it, a short override list settles the exceptions, and the person chooses among nearby markets. The method is well-worn and agents can build it without a further ruling. Sacramento's reach is Don's call.**

**Don's call: how far does the open Sacramento market reach?**

- **A. As ruled, and nearby people may choose Sacramento (recommended).** Sacramento stays Sacramento and Yolo counties, Placer and El Dorado without their Tahoe parts. Yuba–Sutter, Solano and western Nevada County are their own waiting regions (Lodi is Stockton–Modesto's); anyone there may pick Sacramento at sign-up and get in. Keeps today's F118 story (Vacaville is waiting) and the "you choose" ethos. Trade-off: those regions fill more slowly.
- **B. Sacramento grows to its 60-minute reach now.** Adds Yuba City, Marysville, Vacaville, Dixon and, by the merge, Grass Valley and Nevada City; roughly 400,000 more people (A). Lodi still goes to Stockton, which is nearer. Matches the 45–60 minute area Don asked Explore to cover on 2026-10-13. Trade-off: F118's Vacaville story changes, and those towns never get their own opening.
- **C. As ruled, no choosing in.** Fringe towns wait for their own region. Cleanest counts. Trade-off: someone 43 minutes from Sacramento can't use it.

**The first markets and waiting regions in Northern California and Nevada, under the rule:**

| Market or region | Status | What's in it | People (approx., A) |
|---|---|---|---|
| Sacramento | **open** | Sacramento and Yolo; Placer and El Dorado minus their Tahoe parts | 2.2 million |
| Lake Tahoe | waiting (ruled, F103) | the Tahoe basin in both states, plus Truckee | 60–70 thousand |
| Reno–Carson | waiting | Washoe, Carson City, Douglas and Lyon (not the lake shore), Storey; Susanville area merged | 650 thousand |
| Bay Area | waiting, split into four before listing | the nine Bay counties, less Solano under A | 7.7 million |
| Stockton–Modesto | waiting | San Joaquin, Stanislaus, Merced | 1.6 million |
| Chico | waiting | Butte, with Colusa merged | 230 thousand |
| Yuba–Sutter, Solano, Nevada County foothills | waiting (under A) | as named | 180, 450, 85 thousand |
| Redding, Humboldt (with Del Norte), Mendocino–Lake, Mother Lode | waiting | as named | 230, 165, 160, 140 thousand |
| Eastern Sierra | remote | Inyo and Mono | 32 thousand |

<details><summary>A rough map</summary>

```
            Crescent City ─┐
                           Humboldt ·········· Redding
                                                 │ 91
            Mendocino–Lake                     Chico ───────────── Susanville → Reno–Carson
                 │ 75                            │ 63
             Santa Rosa                     Yuba–Sutter         Nevada Co. foothills
                 │                               │ 53               │ 75        Truckee ─23─ Tahoe City
           BAY AREA ── 52 ── Solano ── 43 ── SACRAMENTO (open) ─────┘            │ 53    │ 40
          (4 parts)                              │ 46 Lodi        ─55─ Placerville   South Lake ─49─ Carson City ─ Reno
                                            Stockton–Modesto ── 67 ── Mother Lode
                                                                                    Eastern Sierra (Bishop), remote
```

Numbers are free-flow drive minutes between the towns on each line.

</details>

**What happens next, if Don picks A:** an agent opens a well-worn Issue in `socialus-web` for the script and the override file, its output reviewed as a diff before any row lands; the sign-up choice screen goes through Don for its words.
