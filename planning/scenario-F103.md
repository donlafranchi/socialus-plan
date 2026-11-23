---
id: F103
title: A market is a set of towns, and the zip decides which one a person is in
status: approved
horizon: now
rank: 80
gates: launch
date: 2026-10-11
concept: CO-0002
depends: [F076, F081]
approved: 2026-10-11 — the PM: the MSA goes; a market is towns and county subdivisions; the zip decides the market and the home town. Split from the draft into F103–F106.
---
## Story

Priya in Davis signs up. Her zip is in Yolo County, and Yolo is in the Sacramento market, so she is in; nothing she sees says MSA, metro or miles. Her cousin in Marysville types a Yuba County zip: Yuba is its own waiting market, so the cousin lands on its waitlist, never a refusal, and is told it is Yuba County they are waiting for. A friend in South Lake Tahoe shares El Dorado County with Placerville, but the Tahoe basin is a different market, so the friend waits for Tahoe. When the operator moves a subdivision from one market to another, that is one row, and the next sign-up from it follows the row.

## Acceptance

1. **A market is a `region` row in the place tree whose members are whole counties and, where a county is split, county subdivisions.** Sacramento's at beta: Sacramento and Yolo counties whole, Placer minus its Tahoe subdivision, El Dorado minus its South Lake Tahoe subdivision. Every US county belongs to exactly one market; a county nobody has drawn into a named market is its own waiting market by default. Moving a county or subdivision between markets is one row, no deploy. **A market's counties may lie in more than one state.**
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

**Path: new territory, ruled.** The PM approved replacing the MSA on 2026-10-11. This replaces F081 criterion 8 and F076 criteria 1, 2 and 16 (every metro selectable, ordered by waiting count): the zip decides, so nothing is selected or ordered. The 2026-09-30 MSA and pick-a-metro rulings are superseded; F081 criterion 7 holds, since the home town derives from the zip the person gave.

**A state line is a political boundary, not a physical one,** so a market may cross it: the Tahoe basin can be one market with the Nevada shore (Douglas and Washoe counties). What changes with a state line is the law, not the market (see Rulings).

**Every county is a market by default:** "Every US subdivision belongs to a market" is testable only if the default needs no drawing. Counties tile the US (`017_places.sql`), so the national data is zip → county; subdivisions load only for a county an operator splits, and towns only when a market opens.

**Why subdivisions, not Places, as the market's grain.** A Census Place is the right home for a member and a Page (F104), but a market needs enough people to clear a gate, and a county subdivision (a CCD in California) is the Census's own partition, so Placer minus Tahoe is rows, not a drawn line. [A: the Tahoe CCD names are verified against TIGER before seeding.]

**Precedents.** Craigslist opens hand-drawn regions in batches; Nextdoor opens a neighbourhood at a founding count. The market is the region; the rings (F104) carry the neighbourhood.

**Research:** `planning/research/local-inventory-2026-10-11.md`, `planning/research/rings-stress-test-2026-10-11.md`.

[platform none]

## Rulings
- **2026-11-22 — The town launch is the Sacramento area, the market as it stands in the data (the 2026-10-27 drive-time reach), for about 2027-01-01, run as one launch campaign: the chat-search homepage, sample prompts that teach what SocialUs is for, whether a person's market is open, emails to vendors and patrons, and "Find us here" stickers; more may join it.** The PM, verbatim: *"this is the town launch. I'm thinking the sacramento area and for January 1 or so."* His campaign words, the story map (JY-LAUNCH), its conditions (CN-0001 to CN-0016) and the cut line: `planning/briefs/sacramento-launch-campaign-2026-11-22.md`. Production stays April–May 2027. [for now] [replaces 2026-11-06: The beta market is Northern California, not Sacramento.] [binds tiers=planning,code surfaces=launch,markets,waitlist,landing build=none]
- **2026-11-23 — The town launch is cut B: must-haves only, open Wednesday 2027-01-06 as a beta, after a private dry run with a few invited testers the week of 2026-12-28.** Stickers, item tags and Google/Apple sign-in follow in January; AI chat, values and the blue dot, the pulse map and floating wishes later. The PM, verbatim: *"B."* then *"Approve launch B"*, on `planning/briefs/sacramento-launch-campaign-2026-11-22.md` (CO-0070, JY-LAUNCH). This sets the date and cut for the 2026-11-22 ruling above; its "about 2027-01-01" yields. [for now] [replaces none] [binds tiers=planning,code surfaces=launch,markets,waitlist,landing build=none]
- **2026-10-11 — The zip lookup switches to zip → county → market now, inside `socialus-web` #569 and #568; no MSA build comes first.** The PM, 2026-10-11, option A on plan #107, since the MSA is replaced (F103) and building it first would be thrown away. [replaces none] [binds tiers=planning,code surfaces=signup,places,waitlist] Issue: #569.
- **2026-10-12 — A market may cross a state line. Whether money, entities or tax must be handled per state is a question for `socialus-legal` and counsel, and does not come back to the PM as a decision.** The PM, 2026-10-12, replacing the open question that offered discovery-only, no, or yes-for-everything. Because a state line is a political boundary, not a physical one, and the Tahoe basin spans one. Scenario: F103. [for now] [replaces none] [binds tiers=planning,code surfaces=markets,places build=none]
- **2026-10-27 — Sacramento grows to its 60-minute drive-time reach now (adds Yuba City, Marysville, Vacaville, Dixon, Grass Valley, Nevada City; Lodi and the Tahoe parts stay elsewhere). The method is approved; the F076 goals are 100 makers / 1,000 supporters per market.** The PM ("B", plan #223); web #1101, output reviewed as a diff first. [for now] [replaces none] [binds tiers=planning,code surfaces=sign-up build=none]
