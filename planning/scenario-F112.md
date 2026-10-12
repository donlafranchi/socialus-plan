---
id: F112
title: Explore leads with what a member has not seen yet, and gives every Page its turn
status: draft
horizon: next
rank: 125
date: 2026-10-12
depends: [F059, F104]
---
## Story

A member opens Explore on Monday and the bakery that led on Saturday has moved down; a cheese maker they have not been shown yet is near the top. The top of the list is never two cards from one Page. A line partway down reads "New since you were here". On Tuesday a different lens row leads. Signed out, a visitor still sees a different business lead each session, because every Page takes its turn.

## Acceptance

1. **Order stays place, then time.** F104's ring bands, then the recency bands #558 built (2, 7 and 30 days, then older), decide the order as today. Everything below acts only inside one ring band and one recency band. This is the tool side; the fun side's feed is a later design (research note § 2).
2. **Not seen yet first, signed in.** Inside a band, Pages the member has not been shown in the last 14 days [guess] come first.
3. **"Seen" is one row per member per Page** with the last time shown, expiring after 30 days. It is listed in "What SocialUs knows about you" (F113), and the learning switch stops it and deletes it. Staff-side under the 2026-10-09 ruling; no member sees another's.
4. **Fair turns.** Next, Pages with the fewest showings in the vantage's market over the last 7 days; the session seed (#558) breaks ties. The market count is per Page per day with no member id, like `map_mix_log`. Signed out, this and the seed are the whole rule.
5. **No repeats.** No two adjacent cards from one Page. On the first screen a Page leads at most one lens row.
6. **The leading lens row rotates by the day** from the curated set (F059 criterion 4); the thin-row discipline (2026-09-17) unchanged.
7. **"New since you were here"** divides what is newer than the last visit from the rest; no divider on a first visit or when nothing is new.
8. **Same session, same order.** Refresh, back and pagination keep the order (#558 holds).
9. **No attention or payment input.** No open, dwell, scroll or click count enters any criterion here.

## Not this

The fun side's feed, interest ranking or learning from opens (after beta, `IMAGINE.md` § Two sides). Popularity or trending. Distance.

## Why

- **Lives somewhere better?** No: a local list that gives every maker a turn is nowhere else.
- **Only locals know?** No; it makes what locals posted visible in turn.
- **Gets people together?** Yes: more businesses get seen, so more doors get walked through.
- **Stays fresh on its own?** Yes: that is the point; rows expire and counts roll over.
- **Who keeps it current?** Nobody: no table to tune.
- **Better as more people join?** Yes: more Pages to rotate through.

**Path: well-worn.** Precedents: impression discounting (Lee et al., LinkedIn, KDD 2014, https://slideshare.net/mitultiwari/impression-kdd); fair exposure summed over many rankings (Biega et al., SIGIR 2018, https://arxiv.org/abs/1805.01788); TikTok's no-same-creator-in-a-row rule (https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you). **Conflict, noted for the two-sides review:** not-seen-yet reads behaviour back at the member, against F059's 2026-09-12 ruling. Research: `planning/research/explore-freshness-and-learning-2026-10-12.md` § 1.

[platform none]
