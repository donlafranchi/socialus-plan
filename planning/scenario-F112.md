---
id: F112
title: Explore gives every Page its turn, and marks what is new since the last visit
status: draft
horizon: next
rank: 125
date: 2026-10-12
depends: [F059, F104]
---
## Story

A member opens Explore on Monday and the bakery that led on Saturday is further down; a cheese maker who has not led all week is near the top. The top of the list is never two cards from one Page. A line partway down reads "New since you were here", and everything above it is newer than their last visit. On Tuesday a different lens row leads. Nothing they opened, lingered on or scrolled past changed any of it.

## Acceptance

1. **Order stays place, then time.** F104's ring bands, then the recency bands #558 built (2, 7 and 30 days, then older), decide the order exactly as today. Everything below acts only inside one ring band and one recency band.
2. **Fair turns.** Inside a band, Pages with the fewest showings in the vantage's market over the last 7 days come first; the session seed (#558) breaks ties. A Page's posts share its count.
3. **Showings are counted per Page per day, with no member id**, in a table like `map_mix_log`. Nothing per member is stored for this criterion.
4. **No repeats.** No two adjacent cards come from one Page. On the first screen a Page leads at most one lens row.
5. **The leading lens row rotates by the day** from the curated set (F059 criterion 4), the thin-row discipline (2026-09-17) unchanged.
6. **"New since you were here"** divides what is newer than the member's last visit from the rest. The last-visit time is kept in the reader's own browser, signed in or out; the server stores no visit. No divider on a first visit or when nothing is new.
7. **Same session, same order.** Refresh, back and pagination keep the order (#558 holds).
8. **Nothing reads attention or payment.** No open, dwell, scroll or click count enters any criterion here.

## Not this

"Not seen yet" first per member (option B in the research note: needs a ruling and a Charter line change). Learning from opens or clicks (option C: needs a Charter change). Ranking by interests on Explore. Popularity or trending. Distance.

## Why

- **Lives somewhere better?** No: a local list that gives every maker a turn is nowhere else.
- **Only locals know?** No; it makes what locals posted visible in turn.
- **Gets people together?** Yes: more businesses get seen, so more doors get walked through.
- **Stays fresh on its own?** Yes: that is the point; counts roll over daily.
- **Who keeps it current?** Nobody: no table to tune.
- **Better as more people join?** Yes: more Pages to rotate through.

**Path: well-worn.** Precedents: fair exposure summed over many rankings (Biega et al., SIGIR 2018, https://arxiv.org/abs/1805.01788); Front Porch Forum's no-algorithm, place-and-cadence digest (https://en.wikipedia.org/wiki/Front_Porch_Forum); Airbnb's less-alike neighbouring results (https://arxiv.org/abs/2210.07774). Replaces only #558's random tie-break inside a band, so the Charter's "currently order by where and how recent" holds. Research: `planning/research/explore-freshness-and-learning-2026-10-12.md` § 1.

[platform none]
