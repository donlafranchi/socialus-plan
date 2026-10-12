---
id: decisions-audit-2026-10-12
purpose: What DECISIONS.md does today, by category, which other artifacts do the same job, and a proposed shape (A/B/C) where it becomes a short "why" layer with every other kind of item given one home.
layer: why
status: draft
last-updated: 2026-10-12
---

# DECISIONS.md audit (2026-10-12)

Path: new territory. It changes where rulings live and what the generators read, so the shape is a PM call. Nothing has moved yet.

## 1. What it is doing today

433 entries, 505 lines, ~267k characters. 408 are dated (290 from September, 118 from October); 25 are undated. Median entry ~490 characters, 47 run past 1,000, the longest 2,700. Counts below come from a keyword pass over every entry: each count is rough (±15%), and many entries fit two categories.

| Category | ~Entries | ~Chars | Example (line) | Who else already does this job |
|---|---|---|---|---|
| **Principles: the why** (undated, or tagged charter) | 20–30 | 5k | "The platform never rates, ranks, or labels a person" (473); "Wealth circulates; it is not extracted" (471) | `product/charter.md` (generated from these), `product/ABSOLUTES.md`, `product/foundation/` (model, value-test, policy, people-first, monetization, metrics, what-this-is). **Drift:** the same principle is stated in 3–5 places, in different words. |
| **Feature rulings** (what a feature does, dated) | ~180 | 90k | "The MSA is replaced. A market is a named set of whole counties…" (29); "The map pins Pages, not Items" (467) | Scenario criteria (`planning/scenario-F###.md`), the spine (`product/foundation/nouns.md`, `verbs.md`, `product/ui/surfaces.md`, which carry status per entry), `product/systems/`, and the code itself. `constraints/` is generated from these. **Drift:** a shipped scenario is deleted, so its ruling survives only here, while the spine restates the same rule. |
| **Copy and wording** | ~50 | 35k | The "market opened" email text (23); "say Page and post, not listing" (33); report-path copy edits (11) | `product/foundation/voice-and-tone.md`, `planning/research/copy-voice-pass-2026-10-10.md`, the strings in `socialus-web`. **Drift:** exact strings in a ruling go stale the day the code changes them. |
| **Scenario criteria and amendments** | ~40 | 26k | "F065 criterion 5 now says so" (16); "F093 criterion 8 amended…" (134) | The scenario file itself. **Overlap is total:** the ruling restates the criterion it changed. |
| **Process and method** | 30–75 | 22–50k | Pipeline guard trimmed, meta PRs self-merge (26); "cross-cutting documents are generated from markers" (190); "a document that must stay current gets a workflow, not a skill" (Build & stack) | `ops-pattern/process/` (PIPELINE, LIVING-DOCS, ABSOLUTES), `LESSONS.md`, each repo's `CLAUDE.md`. **Drift:** method lives in a product repo, so it does not travel to the next project. |
| **Security, data model, stack, accepted risk** | ~45 | 30k | Three `member_public_*` views are accepted risk (Build & stack); the stack row (Next.js + Supabase…) | `accepted-risks/*.json` (one file per risk, with review dates and a lint), `socialus-web` architecture notes and migrations. **Overlap:** every accepted-risk line has a JSON twin. |
| **Money, legal, organization** | ~20 | 14k | Members are the investors (37); transaction income (35); IP address kept one year (68) | `socialus-legal` (has its own `DECISIONS.md`), `product/foundation/monetization.md`, `product/systems/contributions.md`, and the SETTLED banner at the top of every `CLAUDE.md`. **Drift:** the investor position is in at least four places. |
| **Superseded or corrected, still present** | 35–40 | 28k | "One route: `_inbox/` → … *(Superseded by this revamp…)*" (490); "*(Superseded in part 2026-09-14…)*" inside a principle (474); "Correction: nothing gates selling" (465) | Nobody should: the 2026-09-27 ruling says superseded text is deleted and git holds it. These break that ruling. |

Two patterns cut across every category:

- **Provenance narrative.** ~146 entries spend words on who ruled and through which channel ("The PM, 2026-10-11, option A on plan #107, via Dispatch"). The Issue link already records that.
- **Half the file binds nothing.** 231 entries carry no `[binds …]` tag, so `constraints/` never shows them to an agent. The header already admits that rulings before 2026-09-21 are untagged.

**What the file is today:** a changelog of every PM call, plus a rationale store, a copy deck, a criteria patch list, a process manual and a risk register. Its stated job is "why it is that way". It does that job for about 20–30 entries, and the rest bury them.

## 2. Precedents

- **Architecture Decision Records** ([Nygard](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions)): one immutable, dated record per decision, superseded and never edited. This is what DECISIONS.md is now, and why it grows without limit.
- **Principles that sharpen** ([Amazon Leadership Principles](https://www.amazon.jobs/content/en/our-workplace/leadership-principles), [GitLab values](https://handbook.gitlab.com/handbook/values/)): a short list, reworded in place as it is tested, where examples and operating detail sit under each value. This is the layer the PM is asking for.
- **Decision lives with the thing it governs** ([Python PEPs](https://peps.python.org/pep-0001/), [Rust RFCs](https://github.com/rust-lang/rfcs)): the feature's own document carries its decision, and the index is generated.
- **Triage inbox that must drain** ([Linear Triage](https://linear.app/docs/triage), GTD inbox-to-zero): every item is accepted, merged, declined or snoozed, and nothing lives there.

## 3. Proposed shape

In every option, DECISIONS.md becomes **principles only**: 15–30 entries, each a short statement, "because …", and a "sharpened YYYY-MM-DD" date. A principle is reworded in place as rulings test it, the old wording is pruned, and git holds it. Each feature ruling cites the principle it serves by slug (`[serves no-person-ranking]`), so what has sharpened a principle can be generated rather than kept by hand. The Charter keeps generating from the principles tagged charter.

Every option also gives these one home each: **copy** goes to `voice-and-tone.md` for rules and the code for strings (a scenario criterion when the PM rules a string). **Criteria** go to the scenario. **Process** goes to `ops-pattern/process/`. **Accepted risk** goes to `accepted-risks/*.json`. **Legal and entity** go to `socialus-legal`. **Superseded lines** are deleted.

What differs is where **dated feature rulings** live:

- **A — A separate rulings file.** `RULINGS.md` takes the dated feature rulings with their `[binds]` and `[replaces]` tags. A ruling is deleted once its scenario ships and the spine or the code states it. `markers.py` reads `RULINGS.md` in place of `DECISIONS.md`. *Trade-off: smallest change to the generators and a clean split, but it is still a list, and it only stays short if pruning on ship is enforced by lint.*
- **B — Rulings dissolve into their homes.** Each ruling becomes an inline `[ruling YYYY-MM-DD binds…]` marker on the scenario or spine entry it governs. `constraints/` is generated by scanning the whole repo, and no rulings file exists. *Trade-off: truest to "a fact lives inline at one place", with nothing left to grow, but it is the biggest migration (~180 entries), and shipped scenarios are deleted, so every ruling needs a spine home first.*
- **C — One file, sorted and pruned.** Keep DECISIONS.md with a Principles section on top and rulings below. Strip provenance, superseded lines, copy, criteria and process out. *Trade-off: cheapest, maybe 40% shorter, but the principles are still buried under a growing list, which is the problem raised.*

**Recommendation: A.** It is the simplest option that delivers a short, sharpening "why" file now. It keeps every generator working with a one-path change. It also leaves B open later, since rulings can drain into the spine as their scenarios ship.

### The junk drawer

- **Where:** `socialus-plan/UNPLACED.md`, one dated line per item: `- 2026-10-12 — <what> [unplaced raised=YYYY-MM-DD owner=planning|code]`. This holds thoughts and loose items. Loose *files* keep going to `~/Projects/agent-temp`, which is untracked.
- **How items leave:** every item goes to one of five places: (1) its home on the map, (2) an open-question marker where its answer will land, (3) `IMAGINE.md` if it is an idea with no noun, verb or surface, (4) an Issue, or (5) deleted. The line is then removed. It is never copied, and never kept with a "moved" note.
- **What stops it growing:** the lint fails on any item older than 14 days, the same mechanism as accepted-risk `review_by`. The 5am/5pm handoff drains it. A cap of 20 lines fails the lint too.
- **First tenants:** today's loose top-level `planning/*.md` files (`ITEMS-QUESTION.md`, `ONE-MODEL.md`, `STALENESS.md`, `VOCABULARY-PROPOSAL.md`, `search-dictionary-draft.md`, `values-badges-draft.md`) are a de facto junk drawer and get placed first.

### Where the PM's ask meets existing rulings

- **Compatible:** "authored docs are pruned, not annotated" (2026-09-27). A principle that sharpens is reworded and pruned, not given amendments.
- **Compatible:** "cross-cutting docs are generated from markers". The Charter, constraints and "what has sharpened this principle" stay generated.
- **Conflict, needs the PM:** the DECISIONS.md header says "a ruling's words are not edited". Principles that "gain clarity over time" need exactly that edit. Recommendation: the no-edit rule stays for dated rulings, and principles are explicitly rewritable.
- **Conflict, small:** the 2026-09-09 amendment allows machine-generated data files but bars hand-kept indexes. `UNPLACED.md` is a hand-kept list. It stays within the rule only because the lint drains it, and it is a waiting room, not a record of what is true.
