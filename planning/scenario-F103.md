---
id: F103
title: A market is a set of towns, and the zip decides which one a person is in
status: approved
gates: launch
date: 2026-10-11
depends: [F076, F081]
approved: 2026-10-11 — the PM: the MSA goes; a market is towns and county subdivisions; the zip decides the market and the home town. Split from the draft into F103–F106.
---
## Story

Priya in Davis signs up. Her zip is in Yolo County, and Yolo is in the Sacramento market, so she is in; nothing she sees says MSA, metro or miles. Her cousin in Marysville types a Yuba County zip: Yuba is its own waiting market, so the cousin lands on its waitlist, never a refusal, and is told it is Yuba County they are waiting for. A friend in South Lake Tahoe shares El Dorado County with Placerville, but the Tahoe basin is a different market, so the friend waits for Tahoe. When the operator moves a subdivision from one market to another, that is one row, and the next sign-up from it follows the row.

## Acceptance

1. **A market is a `region` row in the place tree whose members are whole counties and, where a county is split, county subdivisions.** Sacramento's at beta: Sacramento and Yolo counties whole, Placer minus its Tahoe subdivision, El Dorado minus its South Lake Tahoe subdivision. Every US county belongs to exactly one market; a county nobody has drawn into a named market is its own waiting market by default. Moving a county or subdivision between markets is one row, no deploy. **A market's counties may lie in more than one state (ruled 2026-10-12).**
2. **A zip resolves to exactly one market, deterministically:** zip → county (the national HUD-USPS crosswalk, largest residential share wins) → market; inside a split county, zip → county subdivision (the Census ZCTA relationship file, largest share wins) → market. The same zip always gives the same market. A zip the crosswalk does not know is refused with *"We don't recognize that zip, try again."*
3. **The zip decides, nobody picks.** A zip in an open market signs the person up into it. A zip in a waiting market puts them on that market's waitlist (F076) and names the market they are waiting for. No IP, no GPS, no default, no shortlist, no picker.
4. **Nothing member-facing reads the MSA or CSA.** An MSA code, where kept, is a column on the market row read by reports only. No surface shows the words MSA, CSA or metro.
5. **A member in an open market has a home town: the Census Place (city, town or CDP) their zip mostly lies in, or the county remainder where it lies in none**, resolved from the same files, re-resolved when the zip changes on `/you` (F081 criterion 4), stored on the member, never shown to another member. A member in a waiting market gets one the day it opens.

## Not this

A market drawn by population, density, drive time or behaviour. A list of markets to browse or pick from. Growing a market outward with buffers until a stray place falls in (parked 2026-09-30, now moot: every county is a market). Funds, payouts or fees. What Explore shows or how it orders (F104), where a member looks from (F105), what makes a Page local (F106).

## Why

- **Lives somewhere better?** No: who is in a market, and when it opens, exists nowhere else.
- **Only locals know?** Yes: that the Tahoe basin is not Sacramento, and Yuba-Sutter is its own place, is local knowledge the MSA gets wrong.
- **Gets people together?** Yes: a market opens only when makers and finders in one place both show up (F076).
- **Stays fresh on its own?** Yes: the waitlist counts move themselves; a market's county set changes rarely.
- **Who keeps it current?** The operator, one row per county or subdivision; Census TIGER yearly for boundaries; the HUD crosswalk quarterly, only if a zip is reported missing.
- **Better as more people join?** Yes: every sign-up moves a market toward opening.

**Path: new territory, ruled.** The PM approved replacing the MSA on 2026-10-11 (DECISIONS). This scenario replaces F081 criterion 8 (every zip → its MSA) and F076 criteria 1, 2 and 16 (every US metro selectable; metros ordered by waiting count): with the zip deciding, there is nothing to select and no list to order. The 2026-09-30 rulings that the metro for a zip is the MSA and that a member outside every seeded metro chooses one are superseded; "the zip is kept, nobody picks" (2026-09-30) stands and is now literal. F081 criterion 7 (no place the person did not give) holds: the home town is derived from the zip the person gave, the way the metro was.

**A state line is a political boundary, not a physical one (the PM, 2026-10-12).** So a market may cross it: the Tahoe basin can be one market with the Nevada shore (Douglas and Washoe counties), and Truckee's Nevada County is already the same side of the lake. This replaces the open question that offered A) discovery only, B) no, C) yes for everything. What changes with a state line is the law, not the market: whether money, entities or tax must be handled per state is a question for `socialus-legal` and counsel, and it does not come back to the PM as a decision. Nothing in this scenario moves money.

**Why every county is a market by default.** "Every US subdivision belongs to an open market or a waiting one" is only testable if the default needs no drawing. Counties tile the US with no gaps (`017_places.sql`); so the national data is zip → county, which F081 already named, and subdivisions are loaded only for a county an operator splits (Placer, El Dorado). Towns (Census Places) are loaded for open markets, when they open, which is what keeps the data job to days, not weeks. Craigslist does the same: a region per metro, the rest of a state as one site.

**Why subdivisions, not Places, as the market's grain.** A Census Place is the right home for a member and a Page (the town ring, F104), but a market needs enough people to clear a gate, and in most of the country only a county does. A county subdivision (a CCD in California) is the Census's own partition of a county, so Placer minus Tahoe is a set of rows, not a drawn line. [A: the exact CCD names for the Tahoe basin in Placer and El Dorado are verified against TIGER before seeding, not assumed.]

**Precedents.** Craigslist's hand-drawn regions give every address a home and open sites in batches; Nextdoor opens a neighbourhood only when founding members reach a count; the HUD-USPS crosswalk and the Census ZCTA relationship files are the standard free sources for zip → county and zip → subdivision. Conflict: Craigslist's unit is a region, Nextdoor's a neighbourhood; the market is the region, the rings (F104) carry the neighbourhood.

**Worked example, zip 95746 (Granite Bay).** County Placer; subdivision not in the Tahoe set; market Sacramento; home town Granite Bay CDP. Zip 96150 (South Lake Tahoe): El Dorado, the South Lake Tahoe subdivision, market Tahoe, waiting. Zip 95901 (Marysville): Yuba, no named market, so the Yuba County market, waiting.

**Where "local" is defined and read today, and the order of work:** `planning/research/local-inventory-2026-10-11.md`. **The model in four other places:** `planning/research/rings-stress-test-2026-10-11.md`.

[platform none]
