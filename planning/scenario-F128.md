---
id: F128
title: How we work lives in the store, so any method can be checked against it quickly
status: draft
horizon: considering
rank: 2
date: 2026-11-10
depends: [F125]
---
## Story

*The PM, 2026-11-10, verbatim:* "What I'm looking for is a way for me to ask, how does our Dev Ops work? Or point a new method I've learned about at that question and have an agent review the new method against our patterns without the agent having to do a full blown research project. this is especially important as LLM based development is new and changing rapidly. I want to be able to adapt as quickly as the field evolves."

The PM reads about a new way to run coding agents and pastes the link. In one short session an agent lists what the method claims, and for each: we already do this, we do the opposite on purpose and why, we have a gap, or it clashes with a philosophy. It ends with one experiment worth trying and how it would be measured. On another day the PM does the same from the Claude app, with the night's pack loaded into a project, and gets the same kind of answer.

## Acceptance

1. **Every rule of how we work is a record:** each rule in `socialus-ops` `process/` and the repos' `CLAUDE.md` files comes in with scope process, its why, the dated failure behind it as evidence, its strength, and the check or workflow that enforces it.
2. **Ask how something runs:** "how does our DevOps work" (or review, planning, the agent loop, decisions, words) returns a short answer built from live records, each line linked to its record and its enforcing check.
3. **Drift shows itself:** a nightly job flags any practice whose enforcing check or workflow no longer exists in the repo.
4. **Review a method in one session:** given one link or pasted text, an agent lists its claims (at most 15) and for each says: we do this, we do the opposite on purpose, a gap, or a clash with a philosophy, each citing the record; it ends with one recommended experiment. It reads only the given material and the store, with no web research.
5. **Every practice has a ring:** adopt, trial, assess or hold; moving a ring writes a new version with its why.
6. **Experiments are records:** the practice changed, the baseline, the measure, the verdict date and the verdict (keep, fix, revert); the single-loop plan's changes come in as the first ones.
7. **The monthly upkeep reads them:** practices not confirmed in 90 days and experiments past their verdict date are listed for the PM.
9. **Packs for a chat project:** every night the store writes three Markdown packs of how we work to a folder in `socialus-ops`, ready to add to a Claude Project such as "code good": *brief* (philosophies, top patterns, one line per area of the work; about 3,000 tokens), *working* (every live practice with its why, strength, ring and enforcing check; about 15,000) and *full* (adds the dated failures, experiments and their verdicts, and ring history). Each pack opens with its date and size, and a fourth file holds the review-a-method steps from criterion 4, so a chat review follows the same procedure as an agent.
8. **Docs follow the store:** after a week side by side, `socialus-ops` `process/` docs are generated from the records.

## Not this

Keeping the packs in sync with the Claude Project by hand (the project reads the folder; how it syncs is checked first, assumed today). Choosing which new methods to read. Changing any practice (each change is its own experiment). A web crawler.

## Why

- **Lives somewhere better?** No: method docs elsewhere describe their own way of working, not ours with its reasons.
- **Only locals know?** No: this is the platform's own way of working.
- **Gets people together?** Indirectly: a method that adapts fast builds what members need sooner.
- **Stays fresh on its own?** Yes: drift is flagged nightly, and stale practices and overdue experiments surface monthly.
- **Who keeps it current?** Agents record practices and experiments as they change them; the PM rules on rings and experiment verdicts.
- **Better as more people join?** Yes: every new team asks the same store how we work, and every method review adds evidence.

**Path: well-worn.** Thoughtworks' Technology Radar rings practices adopt, trial, assess and hold, and moves them with a written reason ([Thoughtworks](https://www.thoughtworks.com/radar/faq)). The method repo already makes every rule carry its dated "because". Stage 2 of the F125 store. [platform none]
