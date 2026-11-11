---
id: F130
title: A concept keeps one identity from first idea to what got built, with every change on a timeline
status: approved
horizon: next
rank: 4
date: 2026-11-11
approved: 2026-11-11, the PM picked A of the concepts brief
depends: [F125, F126, F127]
---
## Story

*The PM, 2026-11-11, verbatim:* "we will have a concept and begin work on it. as the concept emerges many changes emerge and what we originally thought we were going to do looks somewhat similar to the original but with many many changes."

The PM asks how posts got to where they are. One answer: Bulletins in April, cut in May, split in September, renamed Announcement then Post, follower delivery cut and brought back as push, each step dated, with his words and the change that did it.

## Acceptance

1. **One identity:** a concept is a record whose id never changes; its names are listed with dates and the ruling behind each, and a refused name stays as refused.
2. **Typed events:** each change is one event (idea, scoped, ruling, renamed, split, merged, cut, deferred, built, reversed) with a date, evidence (a plan commit, a criterion or a web PR) and the PM's words in their own field.
3. **Lineage holds:** split, merged and became links between concepts, scenarios and ideas still resolve after a file is deleted.
4. **Proven on real history:** Posts (from Bulletins) and Open your town load with the timelines in the 2026-11-11 brief, entry for entry.
5. **Ideas move in:** each of IMAGINE.md's ideas becomes a concept with status idea, and leaves IMAGINE.md once loaded.
6. **Scenarios join their concept:** a scenario names its concept in frontmatter, and the import links them; a scenario touched after this ships without one fails lint.
7. **One call answers it:** "how did this concept change and why" is one lookup-tool call.
8. **Drift is found:** a weekly check lists concepts whose built and ruled states disagree, and docs that still call something cut after it came back.

## Not this

Moving surfaces, systems, research notes, metrics or journeys into the store (later, one kind at a time). Editing old commits.

## Why

- **Lives somewhere better?** No: today the history is a git dig across two repos, and it breaks when a file is deleted.
- **Only locals know?** No: it is how the product is made.
- **Gets people together?** Indirectly: features stay true to their first intent.
- **Stays fresh on its own?** Yes: events come from rulings, scenario changes and merged PRs.
- **Who keeps it current?** The import and the drift check; the PM only rules.
- **Better as more people join?** Yes: every new contributor or agent can see why a thing is the way it is.

**Path: new territory.** Wikipedia keeps an article's whole history when the page is renamed ([Wikipedia](https://en.wikipedia.org/wiki/Help:Moving_a_page)); architecture decision records chain each decision to the one it supersedes ([ADR](https://adr.github.io/)). Neither follows one idea across names, splits and cuts. Stage 2 of the F125 store. [platform none]

## Rulings

- **2026-11-11 — A concept keeps one identity from first idea to what got built; renames, splits, cuts and returns are dated events on it, each with its evidence and the PM's words.** The PM, picking A, for F130. [binds tiers=planning,code surfaces=knowledge]
