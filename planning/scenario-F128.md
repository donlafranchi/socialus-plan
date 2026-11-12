---
id: F128
title: How we work lives in the store, so any method can be checked against it quickly
status: approved
horizon: next
rank: 2
date: 2026-11-10
approved: 2026-11-10, the PM: "Yes on how we work"; the Claude Project pack carries only what judging a method needs
depends: [F125]
concept: new
---
## Story

*The PM, 2026-11-10, verbatim:* "What I'm looking for is a way for me to ask, how does our Dev Ops work? Or point a new method I've learned about at that question and have an agent review the new method against our patterns without the agent having to do a full blown research project. this is especially important as LLM based development is new and changing rapidly. I want to be able to adapt as quickly as the field evolves."

The PM reads about a new way to run coding agents and pastes the link. In one short session an agent lists what the method claims, and for each: we already do this, we do the opposite on purpose and why, we have a gap, or it clashes with a philosophy. It ends with one experiment worth trying and how it would be measured. On another day the PM does the same from the Claude app, with the night's pack loaded into a project, and gets the same kind of answer.

## Acceptance

1. **Every rule of how we work is a record:** each rule in `socialus-ops` `process/` and the repos' `CLAUDE.md` files comes in with scope process, its why, the dated failure behind it as evidence, its strength, and the check or workflow that enforces it.
2. **Ask how something runs:** "how does our DevOps work" (or review, planning, the agent loop, decisions, words) returns a short answer built from live records, each line linked to its record and its enforcing check.
3. **Drift shows itself:** a weekly job flags any practice whose enforcing check or workflow no longer exists in the repo.
4. **Review a method in one session:** given one link or pasted text, an agent lists its claims (at most 15) and for each says: we do this, we do the opposite on purpose, a gap, or a clash with a philosophy, each citing the record; it ends with one recommended experiment. It reads only the given material and the store, with no web research.
5. **Every practice has a ring:** adopt, trial, assess or hold; moving a ring writes a new version with its why.
6. **Experiments are records:** the practice changed, the baseline, the measure, the verdict date and the verdict (keep, fix, revert); the single-loop plan's changes come in as the first ones.
7. **The monthly upkeep reads them:** practices not confirmed in 90 days and experiments past their verdict date are listed for the PM.
9. **One pack for a chat project:** whenever a practice, its ring or its strength changes, and once a month regardless, the store writes one Markdown pack of how we work to a folder in `socialus-ops`, ready to add to a Claude Project such as "code good". It holds only what judging a tool, process or method against our way of working needs: for each area of the work, each live practice in a line or two with its why, how strict it is and its ring, under 10,000 tokens. It opens with its date and size; a second file holds the review-a-method steps from criterion 4, so a chat review follows the same procedure as an agent.
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

## Rulings

- **2026-11-10 — How we work lives in the store as records, each practice with its why, strictness, enforcing check and ring, so any new tool, process or method can be checked against it in one session.** The PM, for F128. [binds tiers=planning,code surfaces=knowledge,method]
- **2026-11-10 — The pack for a chat project carries only what judging a tool, process or method against our way of working needs, not the full history.** The PM, for F128. [binds tiers=planning,code surfaces=knowledge,method]
- **2026-11-10 — The pack is rewritten when a practice changes and once a month, not nightly.** The PM, for F128. [binds tiers=planning,code surfaces=knowledge,method]
- **2026-11-10 — Unfinished work merges dark behind flags of our own, held in our database and on for builder accounts first; no flag vendor until go-live, when the choice is reviewed again. [for now]** The PM, picking A of the LaunchDarkly review, for #1227. [binds tiers=planning,code surfaces=method]
- **2026-11-10 — No new paid tool before go-live unless it saves PM time; from go-live, paid services that help the platform perform are in, starting with a paid Vercel plan and perhaps a paid GitHub plan. [for now]** The PM, for F128. [binds tiers=planning,code surfaces=method]
- **2026-11-12 — No Vercel or Supabase plan upgrade for load during beta: fix the code first, and upgrade only what a re-run of the load simulation shows is a plan limit, or two weeks before launch, whichever comes first. [for now]** The PM, "A", after the first load simulation found the database never the limit (socialus-web #1264). [binds tiers=planning,code surfaces=method]
