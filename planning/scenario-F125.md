---
id: F125
title: Every decision, pattern and why lives in one store that every agent asks
status: approved
horizon: now
rank: 1
date: 2026-11-10
approved: 2026-11-10, the PM: "Approved" (size M, brief `planning/briefs/knowledge-store-stage-1-2026-11-10.md`)
depends: []
---
## Story

*The PM, 2026-11-10, verbatim:* "if a decision gets overturned, then we can set the status of that decision to retired or archived or whatever and now any new agent all they have to do is look up any decision or feature or record by its status." Then: "every rule, pattern or a decision needs a 'why' and that is the part that we continue to refine. It will always be evolving and should inform 'the platforms why' based on what is current for the time."

A build agent picks up a moderation Issue. Instead of reading every ruling, it asks the store for the live decisions on moderation and gets a short list, each with its why, how strict it is, and what it follows. A month later the PM overturns one; the old decision stays findable as retired and points at the newer one, and the pattern it followed shows one more exception.

## Acceptance

Stage 1: our own agents only, inside `socialus-db` in its own schema.

1. **Live decisions moved in:** every live ruling on the import date is a decision record with its date, words, concern, departments and tags, and the store's export of `constraints/code.md` matches the hand-built one line for line.
2. **Nothing is deleted:** the store refuses to retire a decision without a link to the newer record, and no change rewrites a record in place; every change writes a history row naming the person and the agent.
3. **A why on everything that needs one:** the store refuses a philosophy, pattern, decision or correction without a why.
4. **History in one call:** for any decision, one call returns every version and the chain of older and newer decisions; one call returns what was live for a concern on a given date.
5. **Kind and strength apart:** every record has a kind (philosophy, pattern, decision, correction, and the rest in the brief) and a strength (absolute, rule, guideline).
6. **Model-neutral:** no record names an agent or model as its audience; a correction is served to every agent alike, and the model it was seen in is stored only as evidence.
7. **Settled stays settled:** a record marked settled cannot be proposed for change by any agent; the attempt is refused and logged.
8. **Departments wall off:** a key scoped to one department cannot read another department's internal records, and the store's own login reaches no table outside its schema and no more than the public key does (the full wall comes with the move to the store's own project).
9. **One concern, one call:** a build loop gets the live decisions for one concern in one call; for moderation the answer is under 2,000 tokens.
10. **Precedent:** one call lists every live decision that applies a given pattern, with the ones that depart from it; links inferred at import are marked inferred.
11. **The platform's why** can be read as it stood on any past date, and each change to it names the evidence that prompted it.
12. **Unanswered questions are kept:** every search that finds nothing is logged.
13. **Git keeps a copy:** a nightly export writes the store to this repo by PR, and `constraints/code.md` is generated from it after a week side by side.
14. **The stress tests pass:** the tests in the brief run as the store's test suite, each seen failing first.

## Not this

The public snapshot and public lookup tool (stage 2). Features, questions and risks as records (stage 2). Sign-in for teams (stage 3). Members' own agents (stage 4, its own scenario). Rebuilding decisions that were replaced before the import. Any change to the app's member-facing screens.

## Why

- **Lives somewhere better?** No: no catalog or notes tool holds decisions with their whys, strictness, history and access by role in one place we control (Backstage, Notion and Linear were weighed in the brief).
- **Only locals know?** No: this is the platform's own memory; it serves the agents and people who build for locals.
- **Gets people together?** Indirectly: later stages let members' agents answer what's on and why, straight from the source.
- **Stays fresh on its own?** Yes: retired records keep their history, the monthly why review drafts refinements, and unanswered questions and for-now decisions surface by query.
- **Who keeps it current?** Agents record decisions through the lookup tool as they work; the PM approves philosophies, patterns and the platform's why.
- **Better as more people join?** Yes: more teams and agents read one source instead of hundreds of files, and more questions sharpen the whys.

**Path: new territory**, ruled by the PM on 2026-11-10. Design, precedents and stress tests: the brief. Issues in `socialus-web`. [platform none]

## Rulings

- **2026-11-10 — A database is the source of truth for decisions, philosophies, patterns, corrections and the ontology, across every concern of the platform; git keeps a nightly copy for history and review.** The PM, for F125. [binds tiers=planning,code surfaces=knowledge]
- **2026-11-10 — An overturned decision is kept with status retired and a pointer to the newer one, never deleted. [always]** The PM, for F125. [binds tiers=planning,code surfaces=knowledge]
- **2026-11-10 — Outside agents are served from a published snapshot of public records, never from the live store. [for now]** The PM, for F125. [binds tiers=planning,code surfaces=knowledge]
- **2026-11-10 — The departments to start are building, finance, telemetry and bugs, communications, trust and safety, and legal; a later department is a new value, not a redesign.** The PM, for F125. [binds tiers=planning,code surfaces=knowledge]
- **2026-11-10 — The store starts inside `socialus-db` in its own schema and login, and moves to its own Supabase project before any outside team gets access or the public side goes live.** The PM, for F125. [binds tiers=planning,code surfaces=knowledge]
- **2026-11-10 — Only live decisions move in; an older one is rebuilt from git history when someone asks for it.** The PM. [binds tiers=planning surfaces=knowledge]
- **2026-11-10 — Nothing in the store is written for one model or agent; many models will use it, and each record says what is true or wanted, never which agent it is for. [always]** The PM, for F125. [binds tiers=planning,code surfaces=knowledge]
- **2026-11-10 — Every philosophy, pattern, decision and correction carries a why; the why is versioned and refined as the platform and the times change, and it informs the platform's own why.** The PM, for F125. [binds tiers=planning,code surfaces=knowledge]
- **2026-11-10 — For stage 1 the store's login reaches no table outside its schema and no more than the public key does; the full wall comes with the move to the store's own project.** The PM, picking A, for F125. [binds tiers=planning,code surfaces=knowledge] [for now]
- **2026-11-10 — The cloud sessions' key reaches every department but not the PM's right to decide: agents read and propose, the PM rules; this holds until a second person shares deciding. [for now]** The PM, picking A, for #1219. [binds tiers=planning,code surfaces=knowledge]
- **2026-11-11 — Documents stop being the record: knowledge lives in the store, the documents that remain only orient an agent and say where to look, and the PM asks any kind of question through an agent that searches the store instead of reading documents.** The PM: "the goal of all of this is to move away from documents as record keeping and to allow agents to easily search a store of knowledge without having to read entire documents." For F125. [binds tiers=planning,code surfaces=knowledge,method]
