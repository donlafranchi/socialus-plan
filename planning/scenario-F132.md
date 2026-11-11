---
id: F132
title: Story maps in the store, so every item sits in the bigger picture and new ideas show where they fit
status: approved
horizon: next
rank: 6
date: 2026-11-11
approved: 2026-11-11, the PM: "A, write the scenario and start the build"
depends: [F125, F126, F127, F130]
concept: new
---
## Story

*The PM, 2026-11-11, verbatim:* "it would be ideal if the Knowledge store built these as queryable items where smaller items build up to bigger items and when I want to add or edit an item we get the more full picture. This could also work for new features upcoming features in that we figure out where they fit, and how they could fit in a larger story or pattern and that way when I'm thinking about planning something new, we can see how it could or couldn't fit based on what we have built and what we need to build in order to make it work."

The PM has an idea for holiday specials. He asks where it fits. The answer: under "Find out" in the journey "a neighbour finds something happening this weekend and goes", next to "see this weekend nearby"; it stands on posts with a time, which are built; it needs a "special" kind of post first; nothing it clashes with.

## Acceptance

1. **Patton's structure, as records:** a journey (the map), its activities left to right, the user tasks under each activity in order, and the details under each task top to bottom by priority; each item knows its parent.
2. **Up and down in one call:** asking about any item returns its place (journey, activity, task), what sits around it, and what it is made of.
3. **Slices cut across the map:** a release slice (F127) is a line across one journey named by its outcome; every task shows which slices include it and whether it is built.
4. **Editing shows the picture:** a proposed change to an item returns the journey around it, the slices and features it touches, and what is built or not around it, before it is decided.
5. **Where does this fit:** given a new idea in plain words, one call names the journey, activity and task it would sit under (or "no journey yet"), what built items it stands on, what must be built first, and any philosophy or decision it clashes with.
6. **Today comes in:** the walk-throughs in `planning/uat-journeys.json` become journeys; each existing feature is placed on the task it serves; IMAGINE's ideas (CO-0003 to CO-0043) are placed where they would fit, or marked "no journey yet".
7. **The first map is real:** "a neighbour finds something happening this weekend and goes" loads with its activities, tasks, details and two slices, matching the 2026-11-11 research note.
8. **Short answers:** each answer fits a phone screen, in plain words, no ticket numbers.

## Not this

Drawing the map as a picture (later, on the phone page). Estimates. Rewriting any feature's scope.

## Why

- **Lives somewhere better?** No: maps on sticky notes or whiteboards don't know what is built or decided.
- **Only locals know?** No: it is how the product is planned.
- **Gets people together?** Yes: journeys are about people getting out and meeting, and the map keeps that story whole.
- **Stays fresh on its own?** Yes: built state comes from slices and checks; ideas are placed as they arrive.
- **Who keeps it current?** Agents place items and propose edits; the PM rules on journeys and slices.
- **Better as more people join?** Yes: a new person sees the whole story in one call instead of reading.

**Path: well-worn.** Jeff Patton's user story mapping: backbone of activities and tasks, details below, release slices across ([Patton Associates](https://jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf)); Alistair Cockburn's goal levels name the altitudes ([Cockburn](https://alistaircockburn.com/Unifying%20us%20uc%20sm.pdf)). Research: planning/research/story-mapping-and-roles-2026-11-11.md. [platform none]

## Rulings

- **2026-11-11 — Planning follows Jeff Patton's user story mapping, held in the store as records where smaller items build up to bigger ones, so any item shows its place and a new idea shows where it fits.** The PM, picking A, for F132. [binds tiers=planning,code surfaces=knowledge,roadmap]
