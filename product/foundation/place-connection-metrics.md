---
id: why-place-metrics
purpose: How we grade a place and find the people in it who lack connection. Research-backed metrics, how each is measured in the app, and what to do when one is low.
layer: why
status: later
last-updated: 2026-11-01
owns:
  - place-grade
  - connection-metrics
  - intervention-map
---

# Place connection metrics

> **Later: revisit at 250 signups in the market or when RSVP/attendance ships.** (Don, 2026-11-01)
>
> Stale, fix when revisited:
> - "neighbor-help" and other "neighbor" wording → **locals** (Don, 2026-10-31).
> - The small-number floor (Guardrails, "minimum counts") protects members; it does **not** apply to staff readouts.
> - "The place" / "a place" here means **the market: the 60-minute reach** (plan #223 ruling B), not a town.

Serves the north star in goals.md (Member Flourishing). Premise: people like where they live when they have good connections to others and somewhere to gather. This file turns that into numbers.

## Research basis (verified in this conversation's research)

- Gallup/Knight "Soul of the Community": about 28,000 residents (later 43,000) across 26 ordinary mid-size US cities. Top drivers of attachment: social offerings, openness, aesthetics. Education also mattered. These beat the economy, safety, and leadership.
- Social offerings includes arts and culture, community events, nightlife, a good place to meet people, and whether people care about each other. It was the top driver in all 26 communities in 2010.
- Openness = how good a place is for different groups (seniors, minorities, families with kids, gays and lesbians, college graduates, immigrants).
- Aesthetics = parks, trails, green space, walkable streets, historic neighborhoods. Not only scenery.
- Higher attachment tracked with faster local GDP and population growth (correlation, not proven cause).
- Lewicka's 40-year review (about 400 papers): time lived in a place and strength of local ties are the strongest predictors of attachment. Neighborhood-level attachment dips in big cities, not in small towns.
- Scannell & Gifford: attachment has three parts: the person, the place, the process. Measured as feeling (affect), meaning (cognition), and behavior.
- Relph (1976): "placelessness" = landscapes that are standardized and disconnected from their context. Distinctiveness is the opposite.

Assumed, not verified: that these survey findings carry over to app-derived signals. Treat every threshold below as a starting guess until we have a baseline.

## Three layers

- Person (private to the person, never public, never sold)
- Place (aggregate, public to members of that place)
- Outcome (does connection actually rise)

## Layer 1: Person metrics

Purpose: spot people who lack connection so the app can offer a way in. Never a public score. Never shown to other members. Never used to rank or gate anyone.

| Metric | Measures | Signal in app | Basis |
|---|---|---|---|
| Local ties | People nearby they've met in person | Mutual meetups attended, mutual groups | Lewicka: ties predict attachment |
| Tie depth | Repeat contact vs one-offs | Same people met 2+ times | Lewicka |
| Time in place | Tenure | Account-stated years at area | Lewicka |
| Showing up | Behavior component | Meetups attended vs RSVPs | Scannell & Gifford |
| Creating | Participation beyond consuming | Listings, groups, asks created | Goals: "people can do more" |
| Reciprocity | Gives and receives | Trades, volunteering both directions | Social offerings: people care |
| Isolation flag | Little or no local contact over a window | Zero meetups, zero messages sent | Gap detection |
| Felt belonging (survey) | Affect and cognition | 2 to 3 question pulse, optional | Scannell & Gifford |

Rule: a person is never shown a "0" or a low score (see voice-and-launch-copy.md). The isolation flag only triggers a gentle outward nudge.

## Layer 2: Place metrics (the grade)

| Metric | Measures | Signal in app | Basis |
|---|---|---|---|
| Gathering density | Things to show up to | Meetups, markets, classes per 1,000 residents per month | Social offerings |
| Gathering variety | Not just one type | Categories active (arts, food, volunteer, trade, sport, learning) | Social offerings (arts and culture) |
| Meet-new-people ease | Is it easy to meet someone | Share of events with a first-timer attendee | "Good place to meet people" |
| Caring | Do people look out for each other | Volunteer asks filled, time to first response | "People care about each other" |
| Openness | Welcome across groups | Mix of ages, tenure, groups at events; first-timer return rate | Openness driver |
| Third-place count | Regular gathering spots | Venues hosting 3+ recurring events | Aesthetics + social offerings |
| Green and walkable access | Parks, trails, walkable core | Events at parks/trails; map data on walkable meetup venues | Aesthetics |
| Distinctiveness | Local, quirky, one of a kind | Share of listings from local makers vs chains | Relph (placelessness) |
| Local economy loop | Money stays | Share of transactions member-to-member in-area | Goals promises 1, 6 |
| Newcomer integration | Do new arrivals connect | Share of accounts under 6 months with 3+ ties | Lewicka (time + ties) |
| Network density | Webbing, not hubs | Share of members in the largest connected cluster; ties per member | Social capital |
| Dependence on one organizer | Fragility | Share of events run by top 3 organizers | Resilience (design guess) |
| Education and learning | Classes, teaching, skill trades | Teach/learn listings per 1,000 | Gallup education driver |
| Attachment (survey) | The outcome Gallup measured | Pulse: "I'd recommend living here," "I feel I belong here" | Gallup/Knight |

Place grade: score each metric against a target, then roll up to the three Gallup drivers (social offerings, openness, aesthetics) plus ties and distinctiveness. Show the drivers, not one blended number, so a place sees what to fix.

## Layer 3: Outcome metrics

- Median local ties per member, trend by quarter.
- Isolation rate (share with no local contact in 90 days), trend by quarter. Should fall.
- Newcomer integration rate, trend.
- Attachment pulse, trend, compared with Gallup-style baseline.
- Member Flourishing tie-in: do members with more ties also report more time and money to live? (hypothesis, test it)
- Sustainability tie-in: share of community fund spent on the lowest-scoring drivers.

## Intervention map: low metric, what to do

| If this is low | Do this |
|---|---|
| Gathering density or variety | Seed events; prompt local makers and organizers to start one; lower the effort to host |
| Meet-new-people ease | First-timer friendly events; "bring someone" prompts; small-group formats |
| Caring | Surface volunteer asks; quick-response nudges; neighbor-help formats |
| Openness | Events aimed at under-served groups; check where bounce-offs happen |
| Third places | Recruit venues; fund recurring events in them from the community grant fund |
| Green and walkable | Park/trail meetups; map walkable venues first |
| Distinctiveness | Promote local makers; highlight what's unique to the area |
| Newcomer integration | Welcome pairing; "start here" meetups for the first 90 days |
| Network density | Introduce across clusters; cross-group events |
| Organizer dependence | Co-host tools; recruit and back a second tier of organizers |
| Person isolation flag | One outward invitation (a nearby meetup), never repeated pressure |

## Guardrails

- Privacy: person-level data stays private. We don't sell it. No public individual scoring.
- No dark patterns: the goal is people in the same room, not time in the app. Measure showing up, not scrolling.
- Small places: suppress any aggregate that could identify an individual (minimum counts before a number is shown).
- Don't grade a place against a mountain town. Compare each place to its own trend and to peers of similar size.
- Honesty: Gallup's findings are correlations from 26 cities. Our metrics are a design built on them.

## Open decisions

- Who sets targets: staff, members, or both?
- Are the attachment pulse questions in the product or an outside survey?
- Does the grade appear on a public place page, or only to the place's members?
- Minimum count before a place metric is shown.

## Sources

- Gallup/Knight Foundation, Soul of the Community (2008 to 2010): news.gallup.com/poll/144476
- Knight Foundation findings summary: knightfoundation.org/articles/discovering-what-ties-people-to-where-they-live
- Lewicka, "Place attachment: How far have we come in the last 40 years?" (Journal of Environmental Psychology)
- Scannell & Gifford, "Defining place attachment: A tripartite organizing framework" (Journal of Environmental Psychology)
- Relph, Place and Placelessness (1976)
