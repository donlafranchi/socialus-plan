---
id: what-rings
purpose: Two different things called rings: where a market ends (market rings) and how far one person's search widens (search rings). Never confuse them.
layer: what
status: active
---

# Rings: two concepts, never one

The PM, 2026-11-23, verbatim: *"Let's separate these two concerns and one concern is a market opening and which consumers can also sign up. That is the market three ring and then the other three ring is search for a user or a person and the three ring search is that's how wide we go when we're trying to find a certain number of results for whatever they're looking for and then let's approve E for the market opening that way for the next market opening we can use the same parameters"*

| | Market rings | Search rings |
|---|---|---|
| Question | Where does a market end, and who may sign up when it opens? | How wide does one person's search go to find enough? |
| Centred on | The market's hub (a place, not a person) | The person's vantage: home by default, movable (F105) |
| Set | Once, ahead of time, by a script; changes only by a ruling | Per search, by result count |
| Units | Whole towns and county subdivisions | hood → town → area → beyond |
| Concept in the store | Market rings, linked to CO-0070 | Search rings, linked to F136 |
| Governs | F103 (the market), F076 (the waitlist), F118 (opening goals) | F104 (scope and order), F105 (vantage), F136 (search) |

## Market rings: the method

Approved for the Sacramento opening as option E of `planning/briefs/sacramento-market-edges-2026-11-23.md`: the 2026-10-27 one-hour method (`planning/research/market-resolution-2026-10-26.md`). Written as a method with parameters, so the next market opens on the same ones:

- **Hub size: 50,000.** A town of 50,000 or more, over an hour from every other hub, is a hub of its own; so is the largest town of each commuting zone.
- **Reach: one hour of free-flow drive time from the hub.** Each town goes to the market of its nearest hub within the hour.
- **A town nearer another hub goes there** (Lodi, Stockton and Fairfield are not Sacramento's).
- **Tie broken by commuting zone:** two hubs from different markets within 10 minutes of each other, the government's commuting zone decides (Fairfield goes to the Bay Area).
- **Small leftovers merge in:** a waiting region under about 100,000 people joins the nearest region within two hours (the corners of Sutter and Yuba merge into Sacramento).
- **Overrides win,** each naming its ruling: the Tahoe subdivisions stay their own market (F103).
- **An open market's edge moves only by a ruling.** The script proposes a diff; a person approves it.

For Sacramento: Sacramento, Yolo, Placer and El Dorado less Tahoe, plus Sutter, Yuba, Vacaville, Dixon and western Nevada County: 114 towns, 2.76 million people, 148 zips. The change to the member list is about six rows (`socialus-web` #1101). The edge decides which zip signs up and which waits, and which Pages show (a Page's own place inside the edge, wherever its maker lives, F104.4). Nobody sees minutes, miles, a ring or a list of markets.

[open-question owner=don raised=2026-11-23] Should people in towns within 75 minutes of the edge (Stockton, Lodi, Fairfield, Vallejo and more, about 48 towns) be asked once to join Sacramento or wait for their own town? The brief recommends the beta's second month, or 100 makers, whichever is first. Not approved: the zip decides, nobody picks (F103.3) stands.

## Search rings: how a search widens

A search starts at the person's vantage and widens ring by ring, hood → town → area → beyond, until it has found enough results for what they asked, each step labelled with a place name, never minutes or miles. A person can widen or narrow it by hand.

The agents' call, by precedent ([Yelp](https://www.yelp.com/) and Google Maps widen "near" results, [Airbnb](https://www.airbnb.com/) offers "expand your search"): **enough is 10 results** [A: 10, a Google or Yelp first page], the widening is automatic with the widest ring named on the results ("Showing Roseville and nearby"), and an empty answer says so rather than reaching further. Set in one place as data, tunable without a deploy.

## Rulings

- **2026-11-23 — Market rings and search rings are two separate concepts. A market's edge is the one-hour method with its parameters (hub 50,000; free-flow drive time from the hub; a town nearer another hub goes there; small leftovers merge in; tie broken by commuting zone; the Tahoe subdivisions stay their own), approved as option E for the Sacramento opening, so the next market opens on the same parameters.** The PM, verbatim, above, on `planning/briefs/sacramento-market-edges-2026-11-23.md` (CO-0070; web #1101). The wider consumer list is not approved (open question above). [for now] [replaces 2026-11-22: the market as it stands in the data (the 2026-10-27 drive-time reach), for about 2027-01-01] [binds tiers=planning,code surfaces=markets,places,sign-up,waitlist,launch build=none]
- **2026-11-23 — Search rings are per person, centred on their vantage (home by default): a search widens hood → town → area → beyond, labelled, until it finds enough results for what they asked.** The PM, verbatim, above. How many is "enough" and how it is labelled are the agents' call by precedent (above), noted in F136 and F104. [for now] [replaces none] [binds tiers=planning,code surfaces=search,places,explore build=none]
