---
id: pm-cockpit-2026-10-12
purpose: Inventory every human-facing view across the five repos, research how agent-led teams give one person one control view, and design one generated PM cockpit. Extends growing-docs-audit-2026-10-12.
layer: why
status: ruled
last-updated: 2026-10-12
---

# One cockpit for the PM

**The PM looks in nine places today, and they disagree: three launch dates, and three different counts of what waits on the PM.** This proposes one generated page, the dashboard grown into a cockpit: a big checklist with every detail folded, built only from agent docs and GitHub, never hand-kept. Agents keep as many single-purpose docs as they need; the cockpit is the only thing the PM has to read.

**Ruled B (2026-10-13):** the dashboard becomes the one cockpit, and the colour page stays as a second rendering of the same data. Every other PM view folds in or retires.

Path: new territory. It retires views the PM uses and decides what a public page may show about accounts and money.

## The picture

**Agents write many small docs that each do one job. A generator reads them and GitHub, then writes one page for the PM. Guards that agents can't edit check the agents.**

<details><summary>Details</summary>

```
agent docs (scenarios, rulings, reports, risks, UAT journeys) ─┐
GitHub (Issues, PRs, CI, rulesets, migrations check) ──────────┼─► generator ─► the cockpit (one page, phone-first)
guards agents can't edit (rulesets, protected paths, CI) ──────┘                 ▲ every repo README links here
```

- **Agent side:** unlimited single-purpose docs, each with a budget (already ruled 2026-10-12).
- **Generator:** the existing dashboard script, extended. It reads; it never asks an agent to report.
- **Cockpit:** eight sections, each a bold one-liner, then a folded checklist. When all is well it is almost empty, the way an airliner's "dark cockpit" lights only what is wrong.
- **Safety:** the agent-safety panel compares GitHub now against the last look, so an agent can't hide what it removed.

</details>

## What changed since you last looked

**Ruled B; nothing built yet.** This extends the docs audit (ruled A): that one cut what agents maintain; this one cuts what the PM reads.

## 1. What the PM reads today

**Nine views show overlapping facts, and they already contradict each other.**

<details><summary>Details</summary>

| View | Shows | Generated? | Overlaps |
|---|---|---|---|
| Dashboard (md) | Beta date, criteria met, UAT next, waiting on you, lost since last look, Now/Next/Considering/Later, per-area roll-up, data problems | Yes, daily and at handoff | Everything below |
| Dashboard colour page (html) | The same, tappable | Yes | The dashboard, entirely |
| Plan README | "Launch 2026-10-30, 16 days left", Built/Building/Next lists, risks due | Yes, daily | Dashboard roadmap; **conflicts with the dashboard's "Beta 11-06, 18 days to freeze"** |
| STATUS | Scenarios by status, CI, open questions (31 waiting on the PM), guard coverage, doc age | Yes, daily | Dashboard waiting (6), deferred, roadmap |
| Handoff state | Running sessions, the PM's open calls | Written each shift | Dashboard waiting — **a third count** |
| Capabilities | What the app can and can't do | On request | Criterion reports |
| `[for now]` review list | Rulings to revisit at release | Yes | Rulings inline |
| UAT Issue (phone checklist) | Next 4 of 17 walk-throughs | Yes, re-ranks on tick | Dashboard UAT lines |
| "PM: keys to add" Issue | Moderation key, Twilio, phone provider | Hand-kept | Infrastructure doc env list |

Also read by the PM now and then, all hand-kept or one-off: the infrastructure doc's unticked production checklist (hosting plans, backups, error tracking, uptime), the legal repo's launch plan (accounts, spending caps), the ops README (the method), the doc-garden report, the criterion audit, the charter, research and briefs.

**Where the contradictions come from:** each view reads its own source for the same fact. Dates come from three places; "waiting on you" from four (the dashboard, STATUS markers, handoff, `needs-pm` Issues). The dashboard also can't read the skills repo's PRs, so skill changes never reach "waiting".

</details>

## 2. How others do it (2025–26)

**Every agent tool now gives one list of agent work grouped by "needs you" first; none gives project health. Ops and aviation fill that gap: show only what's abnormal, page only for what's urgent.**

<details><summary>Details</summary>

V = read the source and it says so. A = search snippet or inference only.

| Precedent | What they do | We take |
|---|---|---|
| [Anthropic: harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) (V) | A progress file and a feature list with a pass flag per feature; git as history; "unacceptable to remove or edit tests" | Feature list with pass flags = our criterion roll-up. Make "no removed tests" a checked guard, not an instruction |
| [Anthropic: building effective agents](https://www.anthropic.com/engineering/building-effective-agents) (V) | Humans are checkpoints at blockers, not observers | Cockpit lists only what waits on the PM |
| [Claude Code best practices](https://code.claude.com/docs/en/best-practices) (V) | Hooks and CI enforce "zero exceptions" rules; instructions only advise | Safety panel reads CI and rulesets, never agent self-reports |
| [Claude Code agent view](https://code.claude.com/docs/en/agent-view) (V) | Sessions grouped Needs input → Ready for review → Working → Done; needs-input on top | "Needs your attention" first after health |
| [GitHub Copilot mission control](https://github.blog/changelog/2025-10-28-a-mission-control-to-assign-steer-and-track-copilot-coding-agent-tasks/) (V) | One view of agent sessions; the PR is the unit | Built-since-last-look is merged PRs |
| [Linear agent](https://linear.app/docs/linear-agent) (V); health On track/At risk/Off track (A) | Agent drafts status with progress, risks, next steps; a person sets health | Health lights computed from rules, PM can override |
| [Factory missions](https://docs.factory.com/missions/running-app.md) (V) | Milestones, live progress, cost on the same screen | Cost belongs in risks once there is a monthly bill |
| [Google SRE monitoring](https://sre.google/sre-book/monitoring-distributed-systems/) (V) | Few signals; interrupt only for urgent and actionable | 5–6 lights, no more |
| [SRE error budgets](https://sre.google/workbook/implementing-slos/) (V) | Freeze rule written down before it's needed | Freeze triggers are a later PM ruling, not built here |
| Dark cockpit ([Lean](https://www.lean.org/the-lean-post/articles/the-dark-cockpit-what-aviation-can-teach-lean-leaders/), A) | Normal shows nothing; a lit light means look | All-clear sections collapse to one green line |
| NASA go/no-go poll ([launch status check](https://en.wikipedia.org/wiki/Launch_status_check), A) | Any single no-go holds the launch | Launch readiness as go/no-go lines |
| [METR on reward hacking](https://metr.org/blog/2025-06-05-recent-reward-hacking) (V) | Models edited tests and graders; "don't cheat" prompts barely helped | Safety signals must come from places agents can't edit |
| [GitHub rulesets](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets), [CODEOWNERS](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) (V) | Block force push, protect paths, require owner review | Tests, CI config and guards as protected paths |
| ["The standup is lying"](https://tianpan.co/blog/2026-06-26-the-standup-is-lying-coordinating-work-when-agent-fleets-run-overnight) (V, a blog) | Track artifacts, not intentions; measure how long work waits on human judgement | "Oldest wait" as a health light |
| [GitHub generated release notes](https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes), [Release Please](https://github.com/googleapis/release-please) (V) | Changelog built from PR titles and labels | No hand-written changelog; PR titles are it |
| [Addy Osmani](https://addyosmani.com/blog/future-agentic-coding/), [Simon Willison](https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/) (V) | Code is cheap; the PR and tests are the checkpoint; human attention is the scarce part | The cockpit protects attention: one ask at a time |

Not found: anything specific from Thoughtworks or Steve Yegge; Linear's health levels and Devin's wiki weren't readable.

</details>

### Drop, keep, adapt

**Drop what reports on people; keep what checks work; adapt what assumed humans would remember.**

<details><summary>Details</summary>

| Human-era practice | Verdict | Instead |
|---|---|---|
| Daily standup | Drop | Built since last look, generated |
| Story points, burndown, velocity | Drop | Criteria met; oldest wait on the PM |
| Hand-kept status report, weekly email | Drop | The cockpit |
| Hand-written changelog, build log | Drop (build log already ruled) | PR titles and bodies |
| Sprint board as the PM's view | Drop | Now/Next/Considering/Later, generated |
| Hand-kept checklists in docs (production setup, account setup) | Drop | One Issue per setup item, read into the cockpit |
| Issues and PRs | Keep | Still the unit of work |
| Human review and UAT | Keep | One journey at a time |
| Release go/no-go | Keep | Launch readiness lines |
| Red/amber/green health | Adapt | Computed from rules, never a person's opinion |
| Retrospective | Adapt | Safety panel plus overrule rate |
| Roadmap | Adapt (done) | Four fixed lanes, generated |

</details>

## 3. The cockpit

**One page: the existing dashboard file and its daily build, reshaped into eight sections in this order. Each opens with a bold line; the checklist under it is folded. A section with nothing wrong is one green line.**

<details><summary>Details: each section, what it shows, where it reads from</summary>

| # | Section and its bold line | Checklist items | Reads (exists ✓ / to build ✗) |
|---|---|---|---|
| 1 | **Where we are** — "Beta in N days · 🟢 build · 🟢 site · 🟡 criteria 60% · 🔴 3 safety flags" | One light per signal: main CI, live site, migrations applied, criteria met, oldest wait on the PM, agent safety, docs within budget | CI results ✓, migrations check ✓, criterion roll-up ✓, docs budgets ✓, deploy health ✗ not read yet, one date source ✗ |
| 2 | **Built since last look** — "12 PRs merged, 9 criteria newly met, nothing lost" | Merged PRs grouped by feature, plain titles; criteria newly met | PRs ✓, criterion snapshot diff (lost-since-last-look) ✓ but its snapshot isn't saved yet ✗, "last look" marker ✗ |
| 3 | **Upcoming** — "Now: 19 being built · Next: 7 settled" | Now/Next/Considering/Later | Roadmap generator ✓ |
| 4 | **Needs your attention** — "1 of 9: the next one" | The next item in full (A/B/C or link + 3 steps); the rest as a count, folded | Dashboard waiting ✓, open-question markers ✓, `needs-pm` Issues ✓, briefs ✓; one ranking across all four ✗, skills-repo PRs ✗ |
| 5 | **What to test** — "Next walk-through: 3 min, as a member" | Journeys with tick boxes, next first | UAT journeys and the phone Issue ✓ |
| 6 | **Accounts, keys and APIs** — "2 to set up before beta" | One line per item: what, why, by when, done? | Keys Issue ✓ (hand-kept); production checklist in the infrastructure doc ✗ hand-kept; legal account setup ✗ private |
| 7 | **Risks and deadlines** — "Freeze 10-30 · 2 risks due this week" | Dates, accepted risks with review dates, tripwires, launch-checklist triggers | Accepted risks ✓, launch checklist ✓, tripwire markers ✓; one date source ✗ |
| 8 | **Agent safety** — "All clear" or "3 things agents removed" | Since last look: rulings or tags removed, tests deleted or skipped, criteria lost, guards or CI changed, migrations not applied, rulesets changed | Partly ✓ (below) |

**Two rules for the whole page:** the one ask is in section 4 only; everything else is a fact or a tick box. The page is public, so private items (legal accounts, money) show as a count with "in the private repo", never their content.

**"Since last look":** the PM ticks one box on a pinned Issue after reading the page; a workflow records the time (the UAT Issue already works this way). Untouched for 7 days, it falls back to 7 days.

</details>

### The agent-safety panel

**Flags anything that disappeared or got weaker since the last look, read from GitHub, never from what the agents say they did.** Precedent: METR found prompts don't stop agents editing tests; checks they can't edit do.

<details><summary>Details</summary>

| Flag | Today | To build |
|---|---|---|
| Rulings removed or `[always]`/`[for now]`/binds tags dropped | Lint blocks a scenario deleted with its rulings | Count of tags and rulings now vs last look; any drop listed |
| Tests deleted, skipped, quarantined | `.only` blocked in CI; quarantine list checked for stale entries | Test-file and test-count diff; new `.skip`, `skipIf`, quarantine entries listed |
| Features lost | Lost-since-last-look compares criteria | Save its snapshot so it actually compares (today: "nothing to compare yet") |
| Guards, lint or CI changed | A label tripwire on guard-file PRs | Any PR touching CI, lint, guard or test-helper files listed with its approval |
| Migrations not applied | Required check on the web repo | Show the check's state as a light |
| Rulesets weakened | Rulesets on web and plan | Daily read of rulesets; any change flagged. Ops repo has none: add one |
| Checks that pass without running | One database test reads green when skipped | Count tests skipped for missing setup |

</details>

### Per-repo views: fold in

**One cockpit in the plan repo; every repo's README opens with one line linking to it.** The PM leans toward one doc, and the facts already cross repos.

<details><summary>Details: what retires</summary>

| View | Becomes |
|---|---|
| Dashboard colour page (html) | Stays: a second rendering of the cockpit, built from the same data in the same run |
| Plan README's roadmap and dates | A five-line front page linking to the cockpit |
| STATUS | Agent-facing feed (guard coverage, open questions); off the PM's list |
| Handoff state | Dispatch's own file; its open calls come from the cockpit |
| "PM: keys to add" Issue, production checklist, account checklist | One Issue per item, labelled for setup; the cockpit lists them |
| Capabilities, criterion audit, doc-garden report, doc inventory | Agent-facing or on request |
| UAT phone Issue | Stays: it's the tick-box surface section 5 reads |
| Ops README (the method) | Stays: it explains how we work, not status |

</details>

## 4. The agent side

**Agents keep as many single-purpose docs as they need, each with a budget; the cockpit adds no new maintained doc, only generator work.**

<details><summary>Details: what to build, smallest first</summary>

1. One date source for freeze, beta and launch, read by every generator (fixes the three-date conflict).
2. One "needs your attention" queue merging the four sources, ranked by what unblocks most agent work, nearest deadline breaking ties; fix the skills-repo read.
3. Setup items as labelled Issues; the infrastructure and legal checklists move into them (legal ones as private-repo Issues, counted only).
4. Save the criterion snapshot so "lost" and "built since last look" compare; add the "last look" tick.
5. The safety diff: tags, rulings, tests, skips, guard and CI files, rulesets; a ruleset on the ops repo.
6. Health lights from CI, deploy health and the migrations check.
7. Trim the plan README once the cockpit holds its facts; the html page renders the same eight sections.

Each lands as its own PR with a check seen failing first.

</details>

## The call (ruled B, 2026-10-13)

**A — The dashboard becomes the one cockpit.** Eight sections, everything else folds in or retires, READMEs link to it. *Trade-off: most clarity; the colour page and the README's lists go away.*

**B — Cockpit plus the colour page (chosen).** As A, but keep the tappable html as a second rendering of the same data. *Trade-off: nicer on a big screen; two views to keep in step.*

**C — New cockpit beside today's views.** A separate summary page; dashboard, STATUS and README stay as they are. *Trade-off: least change; the PM keeps reading several pages that can disagree.*

## The ruling

```
- **2026-10-13 — The PM reads one generated cockpit: the dashboard, in eight sections, with the colour page as a second rendering of the same data.** [for now] Every repo's README links to it; other PM views fold in or become agent-facing; nothing in it is hand-kept, and the agent-safety panel reads GitHub, not agent reports. Because nine PM views disagreed on dates and on what waited on the PM (2026-10-12). Rationale: planning/research/pm-cockpit-2026-10-12.md.
```
