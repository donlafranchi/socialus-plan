---
id: F107
title: A searched place is searched as what it is, a town or a county
status: draft
date: 2026-10-11
depends: [F104, F105]
---
## Story

Marcus's home is Granite Bay, so with nothing typed his Explore shows his three rings (F104). On a Saturday he types Napa. The suggestions list "Napa, town" and "Napa County, county" as two rows. He picks the town: he sees what is in the city of Napa. A week later he picks the county and sees what is anywhere in Napa County, Yountville and Calistoga included. Same word, two searches, two different sets of results.

## Acceptance

1. **With no place typed, search and Explore use the member's three rings** (F104). Nothing here changes the default.
2. **A typed place is searched as its own area type** (the place tree's `kind`: neighbourhood, city, county, region). A town returns what is in that town; a county returns what is anywhere in that county; a market (`region`) returns what is in the market. A town search does not widen to its county, and a county search does not narrow to its county seat.
3. **The same name at two area types shows as two suggestions, each labelled with its type** ("Napa, town", "Napa County, county"). The member picks; nothing is picked for them.
4. **Ring order applies only to a town or neighbourhood vantage** (F105 criterion 2). A county or market search returns that area as one set, ordered by F059's rules, with no town bands and no adjacency.
5. **A place in a waiting market** behaves as F105 criterion 4 says, whatever its area type.
6. **Nothing is stored.** The searched place is session state and part of the shared URL, as in F105 criterion 3.

## Not this

Drawing new areas or merging them for search. Distance or radius search. Saved searches. Changing what makes a Page local (F106).

## Why

- **Lives somewhere better?** Partly: Google Maps and Yelp resolve a typed place to one area; they do not separate a town from the county of the same name.
- **Only locals know?** Yes: that Napa the town and Napa County are different places to a local is local knowledge.
- **Gets people together?** Yes: a day trip to the county finds the winery event outside the town.
- **Stays fresh on its own?** Yes: it reads the place tree and stores nothing.
- **Who keeps it current?** Nobody; the place tree is the only input.
- **Better as more people join?** Yes: more Pages fill more area types.

**Path: new territory, ruled** (the PM, 2026-10-11, plan #107: default location is the three rings; a searched place uses its own area type). Revises F105 criterion 2 (re-centring always rebuilt the rings from a town). Precedents: [Google Maps](https://www.google.com/maps) and [Yelp](https://www.yelp.com) resolve "Napa" to one place for you; [Zillow](https://www.zillow.com) lists a city and its county as separate suggestions with a type label, which is the pattern here (not re-verified this session).

Backlog: not yet ticketed. Verify against `socialus-web` main which of the three rings Explore already builds before writing tickets (plan #107).

[platform none]
