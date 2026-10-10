---
id: intake-worked-runs
title: Feature intake, three worked runs
status: draft
date: 2026-10-10
---

# Worked runs

Facts tagged **verified** were read this run (scenario text, issue text, `IMAGINE.md`, `STATUS.md`). **Assumed** means not checked. Hours are estimates. Precedents are recalled, not looked up this run.

## Run 1: back-test on a built scenario, F091 "What's happening, today and this week"

Built: issue #257 closed 2026-10-02, `HappeningRows.tsx` on main. STATUS shows 3 of 7 criteria covered by a check (verified); whether the code meets the rest is assumed.

| What happened | Which role would have caught it at intake |
|---|---|
| Approved assuming the queries exist; on 2026-09-20 found `browse_feed` live but called by nothing | Architect, Stage 0 reads and callers |
| Signed-out today row needed a time window the withheld-cards call lacks; raised as an open question at ticket time (2026-09-30) | Architect and Guardian, before approval |
| Series de-dupe (criterion 6) specified before recurring posts existed; no check covers it | Developer (order of work) and Tester |
| Good: hide-when-empty and stem-hides rule | Already the zero-state gate |

Verdict: three late surprises, all Stage 0 findings.

## Run 2: re-run of a stalled ticket, #57 "What's on, time and category query"

Open since 2026-09-12, now milestone After beta (verified from the issue).

- **Stage 0 would have returned three blockers on the day it was written**: no announcement table existed (grep of migrations, per the issue itself), filter chips on the results surface were ruled out (design-language principle 10), and the issue never said whether it served Home or Browse.
- **Council verdict**: stop. Prerequisite (posts) belongs to a different ticket; do not ticket the query on top of it.
- **Today**: posts and the F091 rows now exist, so most of #57 is likely superseded. The typed-text half probably belongs to the answering strategy in `AGENT-ANSWERING.md` (not read this run; verify). Suggest: close #57 or reduce it to whatever F091, F092 and the answering layer leave out.

## Run 3: the weekend planner prompt

**Goal:** a member with no time to research can see what is worth doing near them this weekend, matched to their mood, the weather and a budget.

The original prompt returns exactly three plans in chat. In the app the mechanism is a live list: show whatever clears the bar now, or say nothing does.

### Facts
| Fact | Status |
|---|---|
| Time rows incl. *this weekend*, hidden when empty (F091) | verified (scenario text; built per #257) |
| Filter in a modal, not beside results (F092, design-language 10) | verified (referenced in F091 and #57) |
| Imported venue events (F096) | draft with open questions |
| Tags are creator-owned; nothing lets a member say anything about a Page they do not own | verified (`IMAGINE.md`) |
| No review noun; star ratings are Won't | verified (`IMAGINE.md`) |
| Price per person on a post | assumed missing |
| Weather read | assumed missing |
| Mood concept | assumed missing |
| Price history to define "worth it / steep" | assumed missing |

### Prerequisites
- A ruling on members writing about Pages they do not own (blocks "worth it / steep" as a judgment). Owner: Don.
- Price on a post (a field), if price is shown. Owner: builder.

### Roles
| Role | Needs | Veto | Risk |
|---|---|---|---|
| Person | A yes in under a minute for this weekend | A padded or generic list | Chat-shaped three-plan output does not survive in a list |
| Maker | Tag pet-friendly, outdoor, price; two fields at most | More than two new fields | Venues will not tag unusual events they do not know qualify |
| Money | Free to the member; no paid placement | Sponsored "worth it" labels | Venue-paid ranking collides with promise 3 and "visibility isn't sold" |
| Architect | Start time (exists), tags (exist), price field, weather read, mood proxy | A second source of truth for price | Mood has no data; do not infer it from behaviour |
| Developer | Smallest reuses the F091 weekend row | A first slice that needs the review system | Weather-ordered ranking conflicts with F091 "ranking by anything but time" |
| Tester | Binary: weekend row shows only posts inside the weekend window, tagged items filter exactly | A criterion like "feels relevant" | Zero-state copy is untested without a quiet-weekend fixture |
| Operator | Weather call that fails closed; stale posts expire | A person needed midweek | Cold start: few posts in one metro makes most weekends empty |
| Guardian | Creator-declared tags only; no "we promise"; outward CTAs | Computed "worth it / steep" is a third-party judgment on a Page | Mood from behaviour is close to what the discovery doc refuses |
| Scout | Date and category filters (Eventbrite, Meetup); attribute tags (Yelp, Google Business Profile); $ tiers instead of computed value | None | Segmented review surfaces with no reviews advertise a promise the data cannot keep |

### Three sizes
| | Smallest | Right-sized (recommended) | Full |
|---|---|---|---|
| Ships | F091 *this weekend* row plus creator tags (pet-friendly, outdoor) in the F092 modal, zero-state defined | Adds optional price per person on posts, a price filter, creator-declared mood tags (active, relaxed, social) | Weather-aware ordering and computed "worth it / steep" against local price norms |
| Hours (estimate) | under 8 | 20 to 40 | 80+ |
| Existing data only | yes | no, needs a price field | no, needs price history and member statements |
| Proves | Do people open a weekend row at all? | Do tags and price narrow it usefully? | Whether a segmented value signal is worth its density |
| Leaves out | Price, mood, weather, value labels | Weather, value labels | Nothing |
| Trigger to move up | Weekend row opened by a meaningful share of weekly users (threshold unset; a guess until a baseline exists) | Enough priced posts in one metro that a label can be computed | Ruling on third-party statements, plus density |

### Zero states
| State | What shows |
|---|---|
| Options clear the bar | The row, soonest first |
| Nothing clears the filter | Refine question: "Nothing like that this weekend. Want to see everything on?" |
| Nothing at all | The row is absent; the invitation sits where it would be: "Nothing created near you yet this weekend. Be the first." |

### Gates
- Prerequisites owned: ruling (Don), price field (builder).
- Kill criterion: if few Sacramento weekends have a non-empty row for four weeks after beta (number a guess), do not build Right-sized.
- Metric: gathering density and showing up (attended vs RSVP) from `place-connection-metrics.md`.
- Tickets for Smallest only; Right-sized waits on beta data.

### For Don
- A) Ship Smallest after beta (recommended).
- B) Ship Smallest in beta; names what leaves the freeze.
- C) Hold until the third-party-statements ruling.

**Scope line:** After beta unless B.

## What this says about the process
- The council earns its keep at Stage 0: all three F091 surprises and all three #57 blockers were verifiable facts, not opinions.
- Roles that did real work: Architect, Guardian, Operator. Scout added the least on these runs.
- Not yet tested: a run by separate parallel agents. These runs were done by one pass over all nine headings (V0).
