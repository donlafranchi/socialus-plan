---
id: brief-2026-11-10-knowledge-store-stage-1
status: approved
size: M
path: new territory
criteria:
  - Every live ruling on the import date is a decision record with its date, words, concern and tags, and the store's export of constraints/code.md matches the hand-built one line for line.
  - The store refuses to retire a decision without a link to the record that replaced it.
  - No change rewrites a record in place; every change writes a history row naming the person and the agent.
  - A key scoped to one department cannot read another department's internal records (the test is seen failing first).
  - A build loop gets the live decisions for one concern in one call, and for moderation the answer is under 2,000 tokens.
  - Every search that finds nothing is logged as an unanswered question.
  - A nightly export writes the store to this repo by PR, and constraints/code.md is generated from the store.
  - The store's own login can reach only the store's schema; a query from it against any app table is refused.
  - For any decision, one call returns every version it has had and the chain of decisions it replaced and was replaced by.
  - One call answers "what was live on a given date" for any concern.
  - Every decision, pattern, correction and philosophy has a why; the store refuses one without.
  - A correction is served to every agent alike, whatever the model; the model it was seen in is evidence, never a filter.
  - The platform's why can be read as it stood on any past date, and each change to it names the decisions or signals that prompted it.
  - A record marked settled cannot be proposed for change by any agent; the attempt is refused and logged.
  - Every decision recorded after the flip names the principles or patterns it applies, or says none; one call lists every live decision that applies a given pattern, with the ones that depart from it.
---

# Knowledge store, stage 1

**As of 2026-11-10** · Source: the PM's direction in one session, 2026-11-10; counts read from `socialus-plan`, `socialus-web` and Supabase that day · Maintained by: hand (brief; deleted once ruled and placed, 30 days)

**Bottom line: one database becomes the single place every decision, concern and ontology entry lives, with a status instead of deletion, an audience on every record, and one lookup tool every agent uses. Stage 1 moves what exists today and serves our own agents only; the public side is designed here and built in stage 2.**

## What the PM decided (2026-11-10)

Recorded here as context. They become dated rulings in the scenario this brief turns into, once approved.

1. A database is the source of truth for decisions, features, questions, risks and the ontology, across every concern of the platform. Git keeps a nightly export for history and review.
2. Outside agents are served from a published snapshot of public records, never from the live store.
3. Departments to start: building, finance, telemetry and bugs, communications, trust and safety, legal. Any later department is a new value, not a redesign.

Also settled the same day: nothing in the store is written for one model or agent. Many models will use it over time, and each new one differs from the last, so every record says what is true or wanted, never which agent it is for. Also settled in the same session: an overturned decision is kept with status `retired` and a pointer to what replaced it (the architecture-decision-record practice), instead of being deleted. An agent never has permissions of its own: it acts for a person and sees at most what that person sees.

## The PM's two calls (2026-11-10)

1. **Where the store lives:** inside `socialus-db` for now, in its own schema with its own database login that can reach that schema and nothing else; it moves to its own Supabase project before any outside team gets access or the public side goes live, whichever comes first. The lookup tool never uses the app's service key. Moving is a copy of the schema and one connection setting, because agents only ever talk to the tool.
2. **Replaced decisions from the past:** live decisions only. A replaced one is rebuilt from git history when someone asks for it.

Everything else below is an agent decision under the decision rights, reported here.

## What stage 1 builds, and what it leaves out

| In stage 1 | Later |
|---|---|
| The store, its schema and access rules | Features, criteria, questions and risks as records (stage 2; features point at their scenario files until then) |
| Decisions and principles moved in, the ontology mirrored in | The public snapshot and the public lookup tool (stage 2) |
| Departments and concerns | Sign-in for people and teams beyond the PM (stage 3) |
| One lookup tool for our own agents, one key per agent | Members' own agents, with consent (stage 4; needs its own scenario) |
| Nightly export to this repo; `constraints/code.md` generated from the store | Retiring the hand-written ruling sections (after a week side by side) |

## Who can see what (all stages; stage 1 builds the first two rows)

| Agent | Acts for | Sees | Can do |
|---|---|---|---|
| Operator | the PM | everything | decide anything |
| Team, by department | a staff member in a department | public records and their department's internal records | record well-worn decisions; propose new-territory ones |
| Member, signed in | a person who sells, organizes or looks for things | public and member records, their own data, data of Pages and events they run | act in the app as that person |
| Visitor | a person without an account | public records and public app content | read |
| Outside agent | a person, through another company's AI | as a visitor; with the person's sign-in and consent, that person's member access and no more | read |

Member access comes from a person's relation to a Page (owns it, organizes the event), not from a role on the account, because `product/foundation/nouns.md` rules that a member has no stored type. Every request is logged with both the person and the agent.

## The record

One table holds every kind. Each row is one thing an agent can quote and cite.

| Field | What it holds |
|---|---|
| `id` | stable: `D-0001` for decisions; existing ids (`F094`) kept for features |
| `kind` | philosophy, pattern, decision, correction, feature, criterion, question, risk, noun, verb, link |
| `concern` | the part of the platform it belongs to (below) |
| `answer` | the record in one line, written to be quoted |
| `why` | the reason, required for philosophies, patterns, decisions and corrections; versioned, and the part that keeps being refined (below) |
| `strength` | `absolute`, `rule` or `guideline` (below) |
| `enforced_by` | the check, lint or test that enforces it, when one does |
| `status` | per kind, below |
| `audience` | public, members, department, operators |
| `departments` | one or more, when the audience is a department |
| `owner` | the person accountable |
| `decided_by`, `decided_on` | who decided and when; an agent's well-worn decision names the agent and the person it acts for |
| `path` | well-worn or new territory |
| `scope` | what it governs: `product` (true of the platform whoever builds it) or `process` (how we work, people and agents alike) |
| `holds` | `always` or `for now`, as the `[always]` and `[for now]` tags mark today |
| `until` | for `for now`: the condition that ends it, in words, linked to a record when there is one ("a second metro") |
| `settled` | true when the PM has said do not re-raise; agents may read it, never propose changing it |
| `as_of` | when it was last confirmed true |
| `source` | where it came from: file and line, PR, Issue |

Beside it: `links` (from, to, type: replaces, implements, governs, depends on, guards, relates, applies, departs from, corrects, explains; each marked stated or inferred), `history` (every version in full, append-only, with when it became true and stopped being true, person, agent, reason), `refs` (GitHub Issues and PRs, Vercel, alerts: the store links to the trackers, it does not copy them), and `unanswered` (every search that found nothing).

## History, lookups across decisions, and the PM's patterns

**History of one decision.** `history` keeps a full copy of the record at every version, with the time it became true and the time it stopped (`valid_from`, `valid_to`), plus who changed it, through which agent, and why. Two questions follow from that: "show me every version of this decision" and "what did we believe about Explore on 1 October". The `replaces` links form a chain, so one call walks a decision back to the first version of the idea and forward to whatever replaced it.

**Across decisions.** Four ways in, combinable in one call: fields (concern, department, status, dates, who decided, well-worn or new territory), exact words, meaning (pgvector), and the links between records, followed as many hops as asked.

**Four kinds hold the PM's thinking**, from widest to narrowest:

- `philosophy`: what the platform values and why it exists. The 23 lines in `PRINCIPLES.md`, the soul and the defaults come in as these.
- `pattern`: a rule of thumb that shows up across many decisions, such as "say only what we must" or "the member before the business".
- `decision`: one ruling, with its date.
- `correction`: a guard against a failure that has been seen in how the work gets done, such as "won't was written as *we will never*" or "a doc restated the schema". It names the failure, never who made it. Each time it is seen again, the store logs the date, an example and, as plain evidence, which model and version produced it. A correction applies to every agent alike. It is retired when the failure has not been seen for three monthly reviews, and one that keeps recurring is turned into a check.

**How strict each one is** is a separate field, because kind and strictness are different questions:

- `absolute`: never broken. It must pass the four-harms test in `socialus-ops` `process/ABSOLUTES.md`; today's absolutes come in as these.
- `rule`: must hold; breaking it is a defect, and a check enforces it where one can (`enforced_by`).
- `guideline`: the default. An agent may depart from it when it can say why, and the departure is logged as `departs_from` with that reason. Most of today's rulings are guidelines, as the absolutes file already says.

Every decision links to what it rests on, with one of two link types:

- `applies`: this decision follows that philosophy or pattern.
- `departs_from`: this decision is an exception, with the reason.

That turns the why into something an agent can count and follow, not just read:

- **Precedent.** "Every live decision that applies *say only what we must*, and the two that depart from it." This is a library of the PM's own case law.
- **Deduction.** For a new question, the tool returns the closest past decisions grouped by the patterns they apply, with counts and exceptions. The agent then answers: "by your pattern X, 14 decisions and 1 exception, this would be Y." A strong pattern of the PM's counts as a well-worn path, next to the outside precedents in the decision rule. Patterns that conflict, or no pattern at all, make it new territory.
- **Drift.** Patterns cited only by retired decisions; decisions in one concern applying opposite patterns; new decisions that cite nothing. Each shows where the thinking moved or a new pattern is forming.
- **New patterns.** When three or more decisions give the same reason without a pattern, an agent proposes one. Philosophies and patterns are the PM's to approve, because they are ideas. Until then they stay proposed and count for nothing.

**Who sees them.** Philosophies, patterns and corrections start with audience `operators`: the PM and the agents acting for him. Any of them can later be made public, one at a time.

## The why is the living part

Every philosophy, pattern, decision and correction carries a why, and the store refuses one without. The answer to "what" changes rarely; the why is what gets refined, as the platform and the times change. It is never static.

- **Each why is versioned.** Rewording a why writes a new version with the date, who proposed it, who approved it, and the evidence: the decisions, exceptions or signals that prompted it. Old versions stay readable.
- **Whys chain upward.** A decision's why rests on a pattern, a pattern's on a philosophy. A decision whose why rests on nothing is the first sign a pattern is missing.
- **The platform's why** is one record at the top: a short statement of why SocialUs exists and what it values, written from the live philosophies. When a philosophy changes, a new version of the platform's why is proposed with it. "Why did we exist, as we said it, in March 2027" is one query. A public version follows when the public side is built.
- **What prompts a refinement.** Exceptions piling up against a pattern (its why is incomplete). The PM overturning agents' calls in one area (the why was misread). A correction that keeps recurring (a why is missing). Questions the store could not answer. A why not confirmed in six months. Later, members' agents asking why and not accepting the answer.
- **Who refines.** An agent drafts the new wording with its evidence. The PM approves any change to a philosophy, a pattern or the platform's why, because those are ideas. An agent may sharpen a single decision's why when it cites evidence, and the history shows it.
- **When.** A monthly why review lists every prompt above, with drafts. It replaces today's principle-sharpening pass, which rewords `PRINCIPLES.md` by hand and leaves the old wording only in git.

**The import.** The 800 live decisions get `applies` links inferred by meaning, marked `inferred`, so a wrong guess is visible and cheap to fix. From the flip on, a new decision names its links when it is recorded, or says "none".

**Statuses.** Philosophy, pattern, decision and correction: proposed, live, retired. Feature: draft, approved, building, shipped, dropped. Question: open, answered. Risk: open, accepted, closed. Noun, verb, link: live, coming, refused, retired. A record is never deleted; `retired` and `dropped` keep it findable.

## Departments and concerns

A concern is the unit an agent asks about; each belongs to one department. Seeded from today's area labels and the 30 most used `surfaces=` tags, merged where they name the same thing.

| Department | Concerns to start |
|---|---|
| Building | explore and map, Pages, posts, sign-in and you, sharing and links, search and ranking, onboarding, uploads, notifications, the ontology |
| Finance | fees and transaction income, payments (none yet; the concern exists so its first decision has a home) |
| Telemetry and bugs | performance, uptime and alerts, errors, CI and deploys |
| Communications | words and voice, emails, landing and announcements |
| Trust and safety | moderation and reports, privacy, security, child safety |
| Legal | terms, consent, data retention, counsel's open items |

## Stress tests (2026-11-10)

Real decisions from this repo, and what each asks of the store. "Fixed" means the field or link above was added because of it.

| Test | The decision | What the store must do | Result |
|---|---|---|---|
| A replacement chain | One market: Sacramento, then Northern California (2026-11-06) | `as_of` returns Sacramento for October and Northern California now; the old record points at the new one | holds |
| A guideline and a correction | "No promises: state things as fact" (`voice-and-tone.md`), and the seen failure of *won't* written as *we will never* | the guideline and the correction are separate records, linked by `corrects`; every agent gets both, whatever its model | fixed: kind `correction`, `strength` |
| The one never we keep | "Never extractive. [always]" (`PRINCIPLES.md`) beside the no-promises pattern | the pattern counts it as a named exception, not a conflict | holds: `departs_from` with its reason |
| Settled, do not re-raise | Members are the investors; legal questions go to counsel | no agent can propose changing it; questions route to legal | fixed: `settled`; legal is the owner department |
| A rule with an end condition | No "near you" until a second metro (2026-09-30) | list every for-now decision waiting on that condition when a second metro is ruled | fixed: `holds`, `until` |
| 412 durability tags | 284 `[for now]` and 128 `[always]` lines today | a review queue of for-now decisions not confirmed since the last release | holds with `as_of` |
| How strict | "Never extractive" (absolute), the email-code-only sign-in (a rule a test enforces), "plain words, one line" (a guideline) | an agent knows which it may depart from, and every departure is logged with its reason | fixed: `strength`, `enforced_by` |
| A why that changed | The market's why: a dense start in one city, then Northern California on 2026-11-06 | both whys readable with their dates and the evidence that moved it | fixed: versioned why with evidence |
| One decision, three departments | Transaction income, and "no fee" language retired | finance, legal and communications all see it; one record, not three | fixed: `departments` is a list |
| The same topic, two audiences | "Why can't I post a photo of my kids?" | a member's agent gets the rule and a short why; the moderation detail stays internal | holds: two records, linked by `explains`, different audiences |
| Deducing from patterns | New question: should a reminder email say "we'll never spam you"? | precedents under no-promises and say-only-what-we-must, with never-extractive as the only exception | holds: the agent proposes "We only send what you asked for" and cites them |
| An agent's call overturned | A well-worn decision an agent made for the PM, which the PM later reverses | the old record keeps who decided and through which agent; overturned agent calls are countable | holds |
| Two live rulings that disagree | Neither replaces the other ([newer-decision-wins] does not apply) | found by the drift query and raised as one open question | holds |

## How agents ask

One lookup tool (an MCP server) with few verbs:

- `search(question, concern?, kind?, status?)`: exact words, meaning (pgvector) and links, in one call, ranked; live before retired.
- `get(id)`: one record, its history and its links.
- `related(id, hops?)`: what it replaces, implements, governs, applies or departs from; one hop unless asked.
- `history(id)` and `as_of(concern, date)`: every version of one record; or what was live for a concern on a given date.
- `precedents(question)`: the closest live decisions, grouped by the philosophies and patterns they apply, with counts and exceptions.
- `why(id)`: the current why, its chain up to the platform's why, and every earlier wording with its evidence.
- `live(concern)`: every live decision and principle for one concern, in the order a builder needs them. This replaces reading all of `constraints/code.md`.
- `propose(record, reason)` and `decide(id)`: internal only. A well-worn decision may go straight to live with its precedents; a new-territory one stays proposed until the PM decides, as today.

The calling agent writes the answer from what these return; the tool runs no model of its own, so it costs nothing per question and cannot invent anything.

## Conditions (F126, approved 2026-11-10)

Fine-grained, never all or nothing: a condition has parts, a decision or feature waits on the part it needs, and the parent is computed from its parts. Scenario: `planning/scenario-F126.md`.

## Versions without brittleness: approved 2026-11-10, scenario F127 (stage 2)

The PM, 2026-11-10: "how we could use this knowledge store to track what we're building and what we aren't for any particular version and do so in a way that isn't brittle or doesn't allow us to pivot."

- **A feature has slices**, from smallest to full, as the brief template's three sizes already do. A slice is what a version takes in, and what a condition gates.
- **A version is a plan, not a box:** a record with the outcomes it is for and an appetite (how much it is worth), and links to the slices it `includes` and the ones it `leaves out`, each with a reason and, where there is one, the condition that brings it back.
- **No dates on features.** Horizon (now, next, later) and rank sit on the slice; a date, if any, sits on the version.
- **A pivot is a new version of the plan, never an edit.** It carries its why (which outcome changed), and the history keeps every earlier plan, so "what v1 looked like on 10 November" and "what changed since" are each one query.
- **Leaving something out is a record too.** It resurfaces on its own when its condition is met or the outcome it served changes, instead of sitting in a backlog.
- Precedents: Shape Up's betting table, which bets on shaped work each cycle and keeps no backlog ([Shape Up](https://basecamp.com/shapeup/2.2-chapter-08)); Now, Next, Later roadmaps without dates ([ProdPad](https://www.prodpad.com/blog/invented-now-next-later-roadmap/)).

## The public side, designed now, built in stage 2

A nightly job publishes every public, live record as a static snapshot on socialus.org, with an index file at the standard address (llms.txt) and a read-only public lookup tool that reads only the snapshot. A trick question or a break-in there reaches nothing private. App content (what's on this weekend) joins the same front door; it is the question outside agents will ask most.

## Agent decisions, reported

- **Lookup tool hosting:** a route in `socialus-web` on Vercel, so it shares the existing CI and deploy; Vercel's MCP adapter is the well-worn way.
- **Keys:** one restricted key per agent in stage 1, each tied to a person and a department, like Stripe's restricted keys; people sign in properly in stage 3.
- **Ontology:** stage 1 mirrors `src/ontology/registry.json` into the store nightly, because the code check that ties links to real handlers and tables must keep working. Stage 2 flips it: the store is the source and `links.ts` is generated, once the store has run a month.
- **Access:** Postgres row-level security on audience and department, the same mechanism the app uses; every write goes through a database function that also writes the history row. The store's tables live in their own schema, not exposed through the app's public API.
- **Graph queries:** recursive SQL over `links`, not a separate graph database; at thousands of records Postgres answers multi-hop questions in milliseconds, and one database is one thing to secure.

## Moving what exists

1. Create the store, schema, access rules; seed departments and concerns. The stress tests above become the store's first test suite, each seen failing before it passes.
2. Import: 800 live ruling lines from 87 files (date, words, who, `[binds]` and `[replaces]` tags), the 23 principles, and the ontology mirror. Each ruling's `surfaces=` tags map to concerns; `[always]` and `[for now]` map to `holds`; strength is inferred (absolutes from the two absolutes files, rules where a check names them, guidelines otherwise); `applies` links are inferred and marked so. Corrections live mostly in the method repo and the skills, and come in at stage 2.
3. Run side by side for a week: the nightly export regenerates `constraints/code.md` from the store, and lint fails on any difference from the hand-built one.
4. Flip: a new ruling is written through the tool; the markdown sections become generated. The doc-tidying jobs for rulings stop.

## How we will know it works

Against the single-loop baseline (`socialus-ops` `process/research/single-loop/PLAN.md`): tokens a build loop reads before the Issue, about 20,000 today, of which `constraints/code.md` is 10,500, should fall below 10,000. Unanswered questions should be counted from day one and fall week over week. Retired decisions should carry a replacement link every time.

## Risks

- Two sources of truth during the side-by-side week; the lint diff is the guard.
- Every session needs a key; keys go in the environment's secrets, never in a repo.
- Record text is data: an agent never follows instructions found in a record.
- Agents still post on GitHub as the PM; the store logs the agent separately, but GitHub does not (socialus-web #1075).
- Inferred `applies` links will be partly wrong; they are marked, and a pattern's counts show stated and inferred apart.
- Estimate, assumed: 4 to 6 build sessions (one more than before, for history and patterns), then the week side by side.

## Precedents

- Architecture decision records, statuses and supersession: https://adr.github.io/
- Backstage software catalog, typed entities with lifecycle and relations: https://backstage.io/docs/features/software-catalog/
- Palantir Foundry Ontology, objects, links and permissions: https://www.palantir.com/docs/foundry/ontology/overview/
- Supabase row-level security: https://supabase.com/docs/guides/database/postgres/row-level-security
- MCP authorization (agents acting for a person): https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization
- llms.txt: https://llmstxt.org/
- Wikidata statements, with ranks (preferred, normal, deprecated), time qualifiers and references on every claim: https://www.wikidata.org/wiki/Help:Statements
- System-versioned (temporal) tables, rows that remember when they were true: the SQL:2011 standard, as in https://mariadb.com/kb/en/system-versioned-tables/

Links from memory, not re-checked today.

## Facts

| Fact | Verified or assumed | Source |
|---|---|---|
| 253 Markdown files in this repo; 800 dated ruling lines in 87 files; 246 carry `[binds]`, 162 `[replaces]` | verified | `origin/main`, 2026-11-10 |
| 68 scenarios: 32 draft, 31 approved, 4 building, 1 deferred; 26 open-question markers | verified | same |
| Ontology: 7 object types, 24 links, 81 handlers | verified | `socialus-web` `src/ontology/registry.json` |
| 23 principles in `PRINCIPLES.md` | verified | `origin/main`, 2026-11-10 |
| Supabase organisation is on Pro with one project, `socialus-db` | verified | Supabase, 2026-11-10 |
| A second project costs about $10 a month | assumed | |
| A lookup tool shipped in a repo loads in cloud sessions | assumed; proved first in stage 1 | |
