---
id: F131
title: Three short answers: what we built, where we are, what's next
status: approved
horizon: next
rank: 5
date: 2026-11-11
approved: 2026-11-11, the PM picked A of the three planning answers brief
depends: [F125, F127, F129]
---
## Story

*The PM, 2026-11-11, verbatim:* "these questions are for humans so need to be human scale length e.g. short and sweet. As an example my dashboard is way too long and unruly. I need to know what the next few things we need to do are."

The PM opens one page on his phone, or asks an agent. Three short answers: what we built and the point of each part; where we are (live, broken, in flight, waiting on him); and the next five things in order, each marked Code or You. An agent starting work asks the same three before touching anything.

## Acceptance

1. **Three calls:** the lookup tool answers `built`, `where` and `next`, each in 10 lines or fewer, plain words, no ticket numbers.
2. **What we built:** one line per area, only what is live, each with its point taken from the concept's why.
3. **Where we are:** live, broken, slow, in flight, launch blockers and waiting on the PM; broken comes from GitHub and Vercel, the rest from the store.
4. **What's next:** at most five things, in order, each with who; anything broken comes first, then what unblocks others, then the top of Now.
5. **Live state comes in:** a job writes GitHub's state (deploys, failing checks, open bugs, the nightly smoke and speed results, items waiting on the PM) into the store, so each answer is one call.
6. **Every line names its source;** a line nothing backs is not shown.
7. **One phone page** shows the same three answers, generated from the same calls, so a chat answer and the page never disagree.
8. **Retired after a week side by side:** the dashboard page, DASHBOARD.md and its script, handoff/state.md, handoff/capabilities.md and the launch reports; agent health checks become checks that open Issues.
9. **Orientation shrinks:** each repo's CLAUDE.md is about 40 lines and starts an agent with these three calls instead of reading files.

## Not this

History views ("where were we last Friday"): git holds that. Estimates or dates per feature.

## Why

- **Lives somewhere better?** No: the facts sit in the store and GitHub; nothing joins them in a few lines.
- **Only locals know?** No: it is how the platform is run.
- **Gets people together?** Indirectly: the PM spends minutes, not an hour, deciding what's next.
- **Stays fresh on its own?** Yes: generated from records and live state, never written by hand.
- **Who keeps it current?** The jobs and the store; nobody edits the answers.
- **Better as more people join?** Yes: every new person or agent asks the same three questions and gets the same answer.

**Path: new territory.** HumanLayer's 12-factor agents derive state from one event record, never a second copy ([12-factor agents](https://github.com/humanlayer/12-factor-agents)); Shape Up's hill charts show where work stands in a glance ([Shape Up](https://basecamp.com/shapeup/3.4-chapter-13)). Brief: planning/briefs/three-planning-answers-2026-11-11.md. [platform none]

## Rulings

- **2026-11-11 — The PM's planning questions get three short answers (what we built, where we are, what's next), each 10 lines or fewer, generated from the store and live state; they replace the dashboard.** The PM, picking A, for F131. [replaces none] [binds tiers=planning,code surfaces=knowledge,dashboard]
