---
id: F127
title: Versions are plans of feature slices that can change without breaking
status: approved
horizon: next
rank: 1
date: 2026-11-10
approved: 2026-11-10, the PM: "yes to the versions proposal"
depends: [F125, F126]
---
## Story

*The PM, 2026-11-10, verbatim:* "how we could use this knowledge store to track what we're building and what we aren't for any particular version and do so in a way that isn't brittle or doesn't allow us to pivot. We are always adjusting our plans in big ways and small all of the time."

The PM decides the next version is about getting sellers paid, and moves card pre-orders in and the seller dashboard out. The store keeps the plan as it was this morning and as it is now, with the why: the outcome changed from "more Pages" to "first sales". When card payments become ready, the parked pre-order slice shows up on its own.

## Acceptance

1. **A feature has slices,** smallest to full, each a record with its own horizon (now, next, later), rank, and the conditions (F126) it waits on.
2. **A version is a record:** the outcomes it is for, an appetite, and links to the slices it includes and the ones it leaves out; each leave-out has a reason and, where one exists, the condition that brings it back.
3. **No feature or slice carries a date;** a version may.
4. **A change of plan is a new version of the plan,** with a why naming the outcome that changed; the earlier plan stays readable.
5. **One call each:** what a version held on any date, and what changed between two dates, with the whys.
6. **Left out is not forgotten:** a left-out slice is listed again when its condition is met or the outcome it served changes.
7. **Today's plan comes in:** each scenario becomes a feature with one slice carrying its horizon and rank, so the dashboard's Now / Next / Later reads from the store.
8. **Nothing breaks:** the dashboard and `STATUS.md` are generated from the store after a week side by side with today's generators.

## Not this

Estimates or dates per feature. Burndown charts. Building any feature's slices (that is each feature's own work).

## Why

- **Lives somewhere better?** No: roadmap tools hold dates and boxes; none holds why a plan changed, tied to the conditions a slice waits on.
- **Only locals know?** No: this is how the platform remembers what it chose to build and not to.
- **Gets people together?** Indirectly: a plan that bends instead of breaking keeps the features members need moving.
- **Stays fresh on its own?** Yes: plans are versioned, and left-out slices come back when their condition or outcome changes.
- **Who keeps it current?** The PM decides what is in each version; agents record it with the why and keep slices linked to conditions.
- **Better as more people join?** Yes: more teams plan from one source, and every pivot leaves a readable trail.

**Path: well-worn.** Shape Up's betting table bets on shaped work each cycle and keeps no backlog ([Shape Up](https://basecamp.com/shapeup/2.2-chapter-08)); Now, Next, Later roadmaps drop dates ([ProdPad](https://www.prodpad.com/blog/invented-now-next-later-roadmap/)). Stage 2 of the F125 store. [platform none]

## Rulings

- **2026-11-10 — A version is a plan of feature slices, with what it leaves out and why; changing the plan writes a new version of it with its why, never an edit.** The PM, for F127. [binds tiers=planning,code surfaces=knowledge,roadmap] [always]
