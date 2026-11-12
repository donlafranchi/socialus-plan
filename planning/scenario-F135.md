---
id: F135
title: Each run of a repeated routine keeps a dated history, so what changed and what to try next is one question
status: approved
horizon: next
rank: 6
date: 2026-11-12
approved: 2026-11-12, the PM picked A: "every run saves a dated record in the knowledge store, with the numbers, what broke first, what we changed after, and ideas for next time"
depends: [F125, F128]
concept: new
---
## Story

*The PM, verbatim:* "track what we've done in the past and have a more full history of what we've done in the past and what we could do at each iteration". Load testing first.

The load simulation runs again in January. Its record lands in the store on its own: the date, the commit, how many members it simulated, the numbers, what broke first, and the ideas the run left. The PM asks "how has load changed and what should we try next?" and gets, in one answer, November's run beside January's, the fixes merged between them, and the open try-next-time list.

## Acceptance

1. **A run is a record linked to its practice:** date, commit, membership size simulated, the numbers, what broke first, what changed after (linked PRs), and next ideas, each in its own field.
2. **Runs record themselves.** The routine writes its own record when it finishes, pass or fail; nobody types one. A run that ends without a record fails its workflow.
3. **What changed after links itself.** A PR that names the run (or its practice) in its body is linked to that run when it merges.
4. **Every practice carries a try-next-time list.** A run's next ideas join its practice's open list; an idea leaves the list only when a later run tried it (linked) or the PM drops it, with the date and why.
5. **Load simulation first.** `socialus-web` #1264 and the Actions "Load simulation" workflow write runs; its first result (in `socialus-ops` `process/PERFORMANCE.md`) is loaded as run one.
6. **Then the other three.** Tap-speed re-benchmarks, the monthly backup restore test and the method review write runs the same way, in that order.
7. **One call answers it.** "History of load simulation and what to try next" is one lookup-tool call: every run in date order with its numbers and what broke first, the changes between runs, and the open list.
8. **The monthly upkeep reads it:** a practice with no run in its expected interval, or a try-next-time idea open more than 90 days, is listed for the PM.

## Not this

Choosing what to try (that stays with the PM and the F128 experiments). New routines. A chart of the numbers (later, if the one-call answer is not enough). Backfilling runs older than the first load simulation.

## Why

- **Lives somewhere better?** No: today each run's result is a section in a doc or an Actions log that expires.
- **Only locals know?** No: it is how the platform is kept up.
- **Gets people together?** Indirectly: a platform that holds under load keeps people's plans working.
- **Stays fresh on its own?** Yes: the routine writes the record and the merged PR links itself.
- **Who keeps it current?** The routines; the PM only drops ideas.
- **Better as more people join?** Yes: every new contributor sees what was already tried and what is still open.

**Path: well-worn.** Load-testing tools keep each run as a dated record to compare against the last ([Grafana k6 Cloud](https://grafana.com/docs/grafana-cloud/testing/k6/analyze-results/compare-tests/)), and blameless post-incident reviews end with a tracked list of follow-ups ([Google SRE](https://sre.google/sre-book/postmortem-culture/)). Here the run sits on the F128 practice it belongs to, in the F125 store. [platform none]

## Rulings

- **2026-11-12 — Each run of a repeated routine saves a dated record in the knowledge store, linked to its practice, with the numbers, what broke first, what changed after and ideas for next time; runs record themselves, load simulation first.** The PM, picking A, for F135. [replaces none] [binds tiers=planning,code surfaces=knowledge,method]
