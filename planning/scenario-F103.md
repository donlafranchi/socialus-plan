---
id: F103
title: The Sacramento area replaces the Sacramento MSA, and a market opens on sign-ups
status: draft
date: 2026-10-11
depends: [F076, F081, F094]
---
## Story

Priya in Davis signs up. Her zip puts her in Yolo County, and Yolo is one of the counties in the Sacramento area, so she is in. Her Explore shows the whole area, as it does today; nothing says MSA, metro or miles, and the hood → town → area order stays. Her cousin in Marysville is not in yet: Yuba County is not in the area, so the cousin joins the Yuba-Sutter waitlist as someone who wants to find things, and a maker friend joins as someone who wants to make things. When enough of each have signed up, and the operator can afford it, a person opens Yuba-Sutter. Both had built their Pages already; the Pages appear that day.

## Acceptance

1. **A market is a named set of counties** (a `region` row in the place tree with county children), not an MSA or CSA polygon. Sacramento's set at beta is the same four counties as MSA 40900 (Sacramento, Placer, El Dorado, Yolo), so nobody who can sign up today loses access; adding a county is one row, no deploy.
2. **Who may sign up is decided by zip → county → open market** (HUD ZIP–County crosswalk, free). A zip in no open market reaches the waitlist for its county's market, never a refusal; every US county belongs to an open market or a waiting one.
3. **The three rings are the member's own:** hood (neighbourhood, where one exists), town (city, town or CDP), area (the market). Every surface that scopes by locality scopes to the area ring and orders hood → town → area → online. No miles, no distance, no "nearby" tighter than the area.
4. **A market opens by a person's act, never on its own,** once its waitlist has enough makers and enough finders (F076's split thresholds, per market, starting 50/250, tunable without a deploy) and the operator confirms it is affordable. The member sees one number and no date.
5. **A maker in a closed market can build a Page now.** It is absent from Explore until the market opens and appears the day it does. MSA/CSA survives only as a code on the market row for reports; nothing member-facing reads it.

## Not this

Rings sized by density, drive time or behaviour (data first, later). Agent-drafted Pages from a maker's website or social profile (new territory, its own scenario). Funds, payouts or fees (Later). Changing what a Page shows about where it is.

## Why

- **Lives somewhere better?** No: who is in a local market, and when it opens, exists nowhere else.
- **Only locals know?** Yes: which counties belong together is local knowledge the MSA gets wrong (Truckee, Yuba City, Tahoe).
- **Gets people together?** Yes: a market opens only when makers and finders in one place both show up.
- **Stays fresh on its own?** Yes: the waitlist counts move themselves; a county list changes rarely.
- **Who keeps it current?** The operator, one row per county; Census TIGER yearly for boundaries.
- **Better as more people join?** Yes: every sign-up moves a market toward opening.

**Path: new territory.** It replaces three live positions, and only the PM can: *"Local means the whole metro"* (2026-09-27, F094 draft) becomes *local means your area ring*; F081 criterion 8 (every zip resolves to its **MSA**) becomes zip → **county**; F076 criterion 1 (every US **metro** selectable) becomes every US **county** belongs to a market. The PM's direction, 2026-10-11: *"we don't need MSA for Sacramento either but we do want to limit who signs up and perhaps that's by the three rings … other metros can open whenever they get enough sign-ups and as long as we have funding to afford it."* Finders are people who come to find things, not Page followers; the waitlist already calls them patrons.

**What exists in `socialus-web` main (2026-10-11):** `metro_polygons.is_open`; `metro_waitlist` with creator/patron roles and per-metro thresholds, "eligible is not open", opening is a human act (F076); `zip_metro_crosswalk` at MSA grain with a one-line MSA→slug bridge in `src/lib/signup/zip-metro.ts`; `places` tree region/state/county/city/neighborhood with polygons for Sacramento, Yolo and Placer counties (El Dorado missing); `browse_feed(p_metro_id | p_place_id)` scoping to one polygon; members carry a primary-home Place; locations carry `place_id`. So the gate and the tree exist; what changes is the unit the gate and the feed read.

**Options for the beta (freeze 2026-10-30):**
- **A** Build before the freeze (2–3 days): area row with four counties, El Dorado polygon, zip→county table, signup gate and `browse_feed` read the area row. Risk: competes with F100–F102 for the last build days.
- **B (recommended)** Seed the data before beta (area row, El Dorado county, zip→county table) with no behaviour change, since the four counties equal MSA 40900 exactly; switch the gate and the feed in the first week after beta, inside one batched migration. Zero member-visible difference in beta, nothing foreclosed.
- **C** Rings-walk feed now (~1 week). Not before the freeze.

**Precedents:** Craigslist's hand-drawn regions give every address a home and open sites in batches; Nextdoor opens a neighbourhood only when founding members reach a count and shows progress to that neighbourhood alone; Kickstarter's all-or-nothing threshold is the same gate shape. Conflict: Craigslist's unit is a region, Nextdoor's a neighbourhood; the area is the market and the hood is the finest ring, so both fit.

**Why counties, not Census Places, as the market:** a Census Place is the right *home* for a member and a Page (criterion 3's town ring), but a market needs enough people to clear 50 makers, and in most of the country only a county does. Counties tile the US with no gaps (`017_places.sql` already says so). Colloquial areas (Tahoe-Truckee) are a set of counties or part-counties; the first one that needs a part-county decides the modelling.

[open-question owner=don raised=2026-10-11] May a market's county set cross a state line (Tahoe: El Dorado/Placer CA with Douglas/Washoe NV)? A) **Yes, for discovery only; money stays per state** — Explore works for Tahoe, legal stays simple (recommended). B) No; two markets, each waits on its own. C) Yes, for everything; needs counsel before the first payout.
