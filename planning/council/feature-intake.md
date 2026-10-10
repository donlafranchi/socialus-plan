---
id: feature-intake
title: Feature intake council (V0)
status: draft
date: 2026-10-10
owner: Don
---

# Feature intake

Turns "someone wants to do X" into one **Feature Brief** a builder can execute with no questions. Runs **before** a scenario is written.

Not a debate. Every role fills its own section in parallel and a chair merges them. Not the beta-scope council (`2026-10-07-beta-mvp.md`), which decides *what ships*; this decides *how one thing is shaped*.

Same machinery and shared lens as `socialus-ops/process/council-roles.md`: roles in parallel on a cheap model, chair on the strongest, Round 1 only at V0.

## Input

One sentence: **"[who] can [outcome] when [situation]."**

- If the request names a *mechanism* (three options, filter chips, a ranking), strip it and keep the goal. The council chooses the mechanism.
- PM context at the top, or say "none given": hard dates, hours available, runway, and **what leaves scope if this enters**.

## Stage 0: Facts brief (chair, before any role speaks)

Check, then tag every line **verified** (read in the repo this run) or **assumed**:

- What exists in `socialus-web` main, and in the spine (`nouns.md`, `verbs.md`, `surfaces.md`).
- What a ruling forbids: `DECISIONS.md`, `ROADMAP.md` § Won't, `IMAGINE.md`, `goals.md`.
- Open questions in `STATUS.md` that touch it.
- **Prerequisites**: anything the feature needs that has no noun, verb or surface yet is a *prerequisite*, listed first, never a task inside the feature.

## Stage 1: Roles (parallel, 200 words max each)

Each role: **Needs** (what it must be true for them), **Cost** (effort or harm to them), **Veto** (the one thing that stops it), **One risk**.

| Role | The one job | Veto |
|---|---|---|
| Person | The member the feature is for. Moment of use, job to be done, what makes them bail. | Anything that makes them wait, scroll or guess. |
| Maker | The Page owner or venue who supplies the content. What they must enter, how much effort, what is in it for them. | More than two new fields, or paid reach. |
| Money | Who pays, who earns, when. Fee, grant-fund flow, nothing. Not "payer": it can be the member, a venue, or the community fund. | Visibility sold, or a cut that grows with dependence (goals promise 3). |
| Architect | Data, events, reads and writes needed vs what exists. Names every missing noun, verb, surface. | Anything that needs a second source of truth. |
| Developer | Order of work, hours (estimate, labelled), what ships first, what is independently shippable. | A first slice that is not shippable alone. |
| Tester | Pass/fail criteria written before building, including every empty state. | A criterion that is not binary. |
| Operator | Day 2: runs unattended Tue to Thu, cost, failure, cold start in one metro, what breaks at 10 users. | Anything needing a person midweek (except child safety). |
| Guardian | Checks `goals.md` promises, privacy, third-party statements about Pages, inference the discovery doc refuses, outward CTAs, voice rules. | Any promise broken. Blocks, does not advise. |
| Scout | Prior art: who solved it, what failed, what to copy, what extracts. Says which precedents were looked up this run vs recalled. | None. Advises only. |

### Shared lens (from council-roles.md, unchanged)
- Bootstrapped, member-funded, no outside capital, no paid acquisition at scale.
- Settled, never re-raised: members are the investors; SocialUs takes transaction income on member commerce; legal goes to counsel.
- Operator is away Tue to Thu.

### Prior art every Scout checks
- Amazon PR/FAQ: write the launch note first; if it reads weak, stop.
- Shape Up pitch: appetite, rabbit holes, no-gos.
- Jobs-to-be-done: the person's actual situation, not their feature request.
- Story mapping: smallest slice that crosses the whole journey.
- Local-discovery precedent (Meetup, Eventbrite, Nextdoor, Yelp, Google Business Profile): copy what works, skip what extracts.
- Multi-agent crews (MetaGPT, ChatDev, CrewAI): role handoffs, not their code.

## Stage 2: Chair merge, always three sizes

Each size states: **what ships, hours (estimate), uses only existing data? (y/n), what it proves, what it leaves out, the trigger to move up.**

- **Smallest**: hours to a day, existing data only, answers "does anyone want this?".
- **Right-sized**: the recommended default, with its prerequisites named.
- **Full**: the whole vision, and the specific rulings and data that unlock it.

Chair also states: which Stage 0 lines were assumed, which role dissented, and what the PM context changed.

## Stage 3: Clean-execution gates (the Brief is not ready until all are yes)

1. Prerequisites listed, each with an owner.
2. Every criterion binary, written before tickets.
3. **Every list defines its zero state**: what clears the bar now, and when nothing does, a refine question or an invitation. Never pad. (Pattern already ruled in F091 criteria 3 and 4.)
4. Copy for every state, to `voice-and-launch-copy.md` rules.
5. Guardian: no promise broken, or the conflict is named for Don.
6. A kill criterion: the number that says stop.
7. One metric tied to `place-connection-metrics.md`, so we learn whether it worked.
8. Tickets for the recommended size only, each independently shippable.
9. Anything assumed in Stage 0 that a ticket depends on is verified first, as ticket 1.

## Output

- Feature Brief (`feature-brief-template.md`), one page.
- Three-size plan.
- Tickets, recommended size only.
- Questions for Don as labelled A/B/C, only ones he alone can answer.
- Scope line: what leaves if this enters, or "After beta".

## Tiers

- **V0 (now)**: this file as one prompt, nine headings, a person or one agent runs it, output read by hand.
- **V1**: roles as parallel agents, each writes its section; Guardian blocks on promise conflicts.
- **V2**: a second round only where roles disagree; disagreements reach Don as A/B/C.
- **V3**: Brief auto-generates the query shape, UI states and tests; live metrics feed back into the next intake.

## How to judge this process

Back-test: run an already-built scenario and a ticket that stalled, compare to what happened. First results are in `2026-10-10-intake-worked-runs.md`.
