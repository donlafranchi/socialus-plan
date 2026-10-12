---
id: growing-docs-audit-2026-10-12
purpose: Every doc that grows, across the five repos, measured. Principles for keeping docs few, current and clear. A plan (merge, generate, delete, refine) with A/B/C, and a proposed ruling.
layer: why
status: draft
last-updated: 2026-10-12
---

# Growing docs: audit and plan (2026-10-12)

Path: new territory. It changes what is maintained, what the generators read and two standing method rules, so the shape is a PM call. Nothing has moved yet.

## 1. Principles

1. **Fewest maintained docs.** A doc earns its place by being read by an agent to do work, and only one doc holds each kind of thing.
2. **Agent docs hold current understanding plus the why.** No history, no "was", no superseded text. Git is the history.
3. **Human docs are generated snapshots on request.** Nobody maintains them. A committed snapshot is allowed only when a workflow rebuilds it, such as a phone view.
4. **Every growing doc has a refinement loop:** a size budget, a trigger, and a named pass that condenses and clarifies it. A doc cannot grow past its budget without being refined.
5. **Refinement means clearer, not just shorter.** A refined doc states the current understanding better than the last version did.

## 2. Inventory

Sizes are from `origin/main` today. "2 wk" is the size on 2026-09-28. Commits are counts since then. Every repo was surveyed. Files under 6k and all fixtures are left out, except where a group adds up. `JOURNAL.md` and `product/products/` do not exist in any repo.

| Doc | Now | 2 wk | Commits | For | Reader | Verdict |
|---|---|---|---|---|---|---|
| plan `DECISIONS.md` | 273k | 172k | 77 | why + 7 other jobs (§3) | agent | **Refine** to principles ≤15k |
| plan `constraints/planning.md`, `code.md` | 45k + 37k | 3k + 4k | 68 / 58 | rulings that bind a tier | agent | Generated, keep; shrinks as rulings prune |
| plan `STATUS.md` | 25k | 16k | 85 | what is true now | human (phone) | Generated, keep (workflow) |
| plan `README.md` | 14k | 8k | 27 | front page | human | Generated, keep (workflow) |
| plan `DASHBOARD.md` + `dashboard/*.html` | 26k + 141k | 0 | 42 | per-area status | human | **Keep**: the PM's "where we are" view; gains a "Where we're going" section |
| plan `ROADMAP.md` | 20k | 8k | 26 | Now/Next/Later/Won't | human | **Retire** into the dashboard's "Where we're going" section |
| plan `handoff/` (latest, state/, capabilities) | 28k | 0 | — | shift state, what the app can do | Dispatch / human | Keep one `state` file, overwritten; capabilities on demand |
| plan `IMAGINE.md` | 26k | 14k | 12 | ideas with no shape | agent | Refine: budget 15k, ideas idle 60 days deleted |
| plan scenarios (53 files) | 231k | — | — | criteria for what's next | agent | Keep; budget 8k each; deleted on ship (already ruled) |
| plan `planning/research/` (15) | 340k | 0 | — | precedents, options | agent | Delete each note once ruled and its result has a home; 30-day age budget |
| plan `planning/briefs/`, `council/` | 78k | 0 | — | feature intake, council records | agent → PM | Brief becomes the scenario on approval and is deleted; council outcome becomes a ruling |
| plan loose `planning/*.md` (8 files) | ~80k | ~70k | — | open questions, drafts | agent | **Junk drawer**: place or delete |
| plan `product/` (38 files) | 325k | 240k | — | spine, systems, foundation, needs | agent | **Merge**: foundation's why goes into principles; budget each |
| plan `CLAUDE.md` | 14k | 11k | 15 | how to work here | agent | Refine: budget 8k; routing moves to the map |
| ops `process/LESSONS.md` | 29k | 15k | 29 | append-only failures | agent | **Refine**: each lesson folds into the rule it earned; file capped |
| ops `process/PIPELINE.md` + `PIPELINE-build.md` | 24k + 24k | 10k + 0 | 19 / 4 | how work moves | agent | Merge into one, budget 20k |
| ops `README.md` | 24k | 8k | 27 | front page | human | Generated (`regen-readme`), keep |
| ops `scores/`, `reports/`, `audits/` | 22k | 0 | — | trial scores, garden reports | human | Snapshot data; keep `history.tsv`, delete dated reports |
| web `build-log/` weekly + per-ticket (202 md) | 436k | ~380k | — | per-ticket build notes | nobody reads back | **Delete and stop.** The PR body is the record |
| web `build-log/reports/` (30 md + 30 json) | 502k | 0 | — | criterion reports | json: machine; md: human | Keep json (generated); md on demand |
| web `build-log/reviews/*.png` | 754k | 0 | — | review screenshots | human | Move to CI artifacts |
| web `INFRASTRUCTURE.md` | 31k | 31k | 4 | external services | agent | Refine: budget 12k |
| web `CLAUDE.md` | 13k | 8k | 12 | how to build here | agent | Refine: budget 8k |
| legal (11 files) | 77k | 0 | — | counsel track | counsel | Budgets only; its own rules |
| skills (46 files) | 167k | 84k | — | skills | agent | `author-skill` enforces a SKILL.md budget |

**What it adds up to:** planning-repo docs went from about 0.7MB to 1.5MB in two weeks. The web build log went from 0.4MB to 1.7MB. The docs that grew fastest are the ones no rule makes shrink: DECISIONS, research, the build log, LESSONS and the dashboard.

## 3. DECISIONS.md, by category

433 entries, ~267k characters, sorted by a keyword pass. Counts are rough (±15%).

| Category | ~Entries | Belongs in |
|---|---|---|
| Principles, the why | 20–30 | stays: this is the file's real job |
| Feature rulings, dated | ~180 | rulings file, pruned on ship (A), or inline on the scenario/spine (B) |
| Copy and wording | ~50 | `voice-and-tone.md` for rules, the code for strings |
| Scenario criteria patches | ~40 | the scenario |
| Process and method | 30–75 | ops `process/` |
| Security, stack, accepted risk | ~45 | `accepted-risks/*.json`, the code |
| Money, legal, org | ~20 | the legal repo, principles |
| Superseded, still present | 35–40 | deleted (breaks the 2026-09-27 ruling today) |

About 146 entries spend words on who ruled and how. About 231 carry no `[binds]` tag, so no agent sees them through `constraints/`.

## 4. Plan

**Maintained: about ten kinds of agent doc.** Principles (`DECISIONS.md`), rulings, the product spine plus systems, scenarios, `IMAGINE.md`, `UNPLACED.md`, accepted-risk JSON, method (`process/`), one `CLAUDE.md` per repo, `SKILL.md` files. Every other doc is generated or deleted.

**Merge**
- `product/foundation/` (14 files) → principles in `DECISIONS.md` (the why) and the spine (the what). `model.md` stays as the source principles answer to, within its budget.
- `PIPELINE.md` + `PIPELINE-build.md` → one file. `LIVING-DOCS.md` patterns → the map, plus one line each on the lint that enforces them.
- `LESSONS.md` → each lesson becomes the "because" on the process rule it earned. What remains is capped at 10k.

**Human views (ruled A, 2026-10-12): the PM wants "where we are" and "where we're going", plus an app storyboard.**
- **Where we are:** the existing dashboard (`regen-dashboard`), unchanged.
- **Where we're going:** a new dashboard section generated by `scripts/dashboard.py` from approved and draft scenarios, ordered by a `rank` field in their frontmatter, with open Issue milestones beside them: Now, Next and Later. Refusals ("Won't") are already rulings. `ROADMAP.md` is then deleted, so no roadmap doc is maintained. Path: well-worn. Roadmap views generated from tracked work are the norm: [GitHub Projects roadmap layout](https://docs.github.com/en/issues/planning-and-tracking-with-projects/customizing-views-in-your-project/customizing-the-roadmap-layout), [Linear roadmaps](https://linear.app/docs).
- **App storyboard:** every routed screen at 390px, one strip per area, as each persona sees it, built on request and never committed. It reuses what exists: `evals/screens/capture.spec.ts` (`SCREENS_WIDTHS=390`, every route in `routes.ts`, every persona) for the pictures, and the `scripts/builders/storyboard.ts` renderer (screenshots in order, one caption each, plain HTML) for the page. It is published as a private page or kept as the nightly CI artifact. A copy storyboard for a draft copy PR is the same view narrowed to the changed routes (`scripts/changed-routes.ts`), so copy storyboards stop being committed into `planning/research/storyboards/`. Precedents: screen snapshots generated per build, never hand-kept: [Storybook](https://storybook.js.org/docs), [Chromatic](https://www.chromatic.com/docs/), [Percy](https://percy.io).

**Generate (on request, or by workflow where a phone needs it)**
- Committed by workflow: STATUS, the READMEs, constraints, PLATFORM-*, the Charter, the dashboard.
- On request only, never committed: the app storyboard, capabilities, criterion reports (md), the launch report.

**Delete**
- web `build-log/` per-ticket notes, then stop writing them.
- Superseded DECISIONS lines.
- Research, briefs, council and exploration notes once ruled and placed.
- Retired tombstones (`goals.md`, `role-language.md`).
- Dated score reports.
- Review PNGs, moved to CI artifacts.

**Refinement loop**

| Part | What |
|---|---|
| Budget | Each maintained doc declares `budget:` (KB) in its frontmatter, defaulted by class in the map. Dated notes carry an age budget. |
| Lint | `scripts/budgets.py` in `lint.sh`. Warns at 80%, fails at 100% or past the age budget. It fails `UNPLACED.md` at 14 days or 20 lines. It is seen failing on a fixture first. |
| On-write rule | A PR that adds to a doc at 80% condenses that doc in the same PR (one in, one out). |
| Weekly refine pass | `tend-docs` takes on budgets: for each doc over 80%, or touched 10+ times since its last refine, it rewrites the doc to current understanding plus why, deletes history, merges duplicates, opens one PR per doc, and brings the PM only judgement calls. It runs Friday with the existing weekly skills. `regen-decisions` becomes "sharpen principles". `trim-product-docs` keeps its why-only sweep. |
| Measure | A line in STATUS for maintained bytes and count, by repo, week over week. `score-doc-drift` stays the accuracy check. |

**Junk drawer:** `socialus-plan/UNPLACED.md`, one dated line per item. Loose files keep going to `~/Projects/agent-temp`. **Exit rule:** each item goes to its home on the map, an open-question marker, `IMAGINE.md`, an Issue, or deletion. The line is then removed, never copied. The lint fails after 14 days or 20 lines, and the handoff drains it. Its first tenants are the eight loose `planning/*.md` files.

**Map:** `socialus-ops/process/WHERE-THINGS-GO.md` (companion PR). Each repo's `CLAUDE.md` points to it instead of carrying its own routing.

## 5. The call (ruled: A, 2026-10-12)

- **A — Core plus budgets (recommended).** About ten kinds of maintained agent doc, each with a budget and the weekly refine pass. Human docs are generated: committed only where a workflow rebuilds them for the phone (STATUS, README), and everything else on request. Merges and deletes as above. *Trade-off: most of the reduction for moderate migration, and the phone view keeps working.*
- **B — Strict on-demand.** As A, but no human doc is ever committed; STATUS and README are built only when asked. *Trade-off: fewest files, but the phone view on GitHub goes away and every status check costs a run.*
- **C — Budgets only.** Keep today's docs, add budgets and the refine pass, with no merges, deletes or generation changes. *Trade-off: least disruption, but the count stays high and history keeps living in the build log and LESSONS.*

## 6. Proposed ruling (draft, for the PM's yes)

```
- **2026-10-12 — Docs hold current understanding and its why, never history, and the fewer the better.** Agent docs are the only maintained docs; each has a size budget the lint enforces and a weekly refine pass that condenses and clarifies it, and no doc grows past its budget unrefined. Human docs are generated snapshots on request, committed only where a workflow rebuilds them. Git is the only history. Principles in DECISIONS.md are reworded in place as they sharpen; dated rulings are not. Because docs that only grew buried what was true: DECISIONS.md reached 273k and the build log 1.7MB in weeks. Rationale: `planning/research/growing-docs-audit-2026-10-12.md`. (tags on landing: replaces none; binds tiers planning,code, surfaces process,docs)
```

## 7. Where this meets existing rules

- **Compatible:** "authored docs are pruned, not annotated" and "cross-cutting docs are generated from markers" (2026-09-27). This plan extends both to every doc, with a budget to enforce them.
- **Conflicts, the ruling above settles them:**
  - The DECISIONS.md header says a ruling's words are never edited, but principles must sharpen in place.
  - `LIVING-DOCS.md` exempts `LESSONS.md` from pruning, and ops `CLAUDE.md` calls it append-only. Both are history the PM no longer wants.
  - The web `CLAUDE.md` requires a build-log file per ticket.
  - The planning `CLAUDE.md` names `ROADMAP.md` as hand-sequenced; it is retired into the dashboard.
- **Small:** `UNPLACED.md` is a hand-kept list, which the 2026-09-09 "no registers" amendment bars. It stays within that rule only because the lint drains it.
