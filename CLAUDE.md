> **SETTLED — do not re-raise:** Wealth circulates here; it is never extracted. The many benefit, not a few — the only test any money decision must pass. Any mechanism that passes it is open; who is paid what, ownership and incorporation stay open. Detail: `product/foundation/monetization.md`.

# SocialUs — planning repo (`socialus-plan`)

Local discovery app: buy, sell, trade, gather. Sacramento beta opens 2027-01-06; production April–May 2027. This repo holds SocialUs's decisions, scenarios and roadmap — what's next to build. App code lives in the sibling repo `socialus-web` (Vercel deploy on push to main; Supabase project `socialus-db`); palette, screens, mockups and design research in `socialus-design`. **The method — how agents work, the process absolutes, the pipeline, the lessons — is `ops-pattern`**, a sibling checkout; paths written `ops-pattern/…` are there. Which folder holds what: `~/.claude/CLAUDE.md` § The repos.

## Always on (every session)

**Talking to the PM**
- Bullets, one line each. Status first, the next ask last. No preamble, recap or narrating.
- One topic, one answer. Explain only when asked, and then in one sentence.
- Plain words; ticket numbers only in brackets after.
- Options as A/B/C with one-line trade-offs and a recommendation. End with the next action.

**Deciding**
- the PM decides ideas, what is in each version, and words and look-and-feel. You decide the rest, record it and report it.
- Look first: name 2–3 precedents with links. Well-worn path: decide and build. New territory (touches a ruling, legal or privacy exposure, money or member trust): A/B/C before building.
- Newer wins: build to the newer record and retire the older in the store. A `[direction replaces=…]` ruling (`git grep '\[direction'`) retires older ones about what it replaces on sight, one line on what each becomes; never member protections. Never ask the PM which is true.
- Never re-raise: SocialUs is built for the primary benefit of its members. Members are not investors, owners or payees, and no return is promised; legal goes to counsel, never the PM. Wealth circulates, it is never extracted.

**Never break**
- Deploys to main, destructive migrations, deleting data and rewriting history ask the PM first. Until the first real member signs up, you may apply migrations yourself, in order, confirming each.
- Anything public is a draft until the PM says otherwise.
- A check isn't trusted until it has been seen rejecting bad input.
- Nothing a member contributes goes live without a report-and-takedown path.
- Member data is never shown beyond what the member chose.
- A ruling is recorded once, with its date and why.

**Where things go:** files live only in the PM's repos. Code answers "how"; the store answers "what is live and why". Anything else: the table below.

## When to ask the store

The knowledge store is the MCP server at `socialus.org/api/knowledge/mcp` (tools: `live`, `search`, `get`, `history`, `as_of`, `precedents`, `why`, `concept`, `how`, `review_method`, `upkeep`, `propose`).

| When | Ask the store |
|---|---|
| Starting work in an area | `live` for each concern touched (pages, posts, explore-and-map, search-and-ranking, onboarding, notifications and the like) |
| Deciding something not covered | `precedents`, then `search`. No well-worn path means A/B/C. |
| Touching schema, RLS, auth or migrations | `live` for security and privacy, plus `how` building |
| Opening or merging a PR | `how` reviewing and `how` shipping |
| Planning, or writing a scenario or ticket | `how` planning |
| Writing words members will read | `live` words-and-voice, and landing-and-announcements for those pages |
| Reports, moderation, user content, AI reading content | `live` moderation-and-reports and child-safety |
| Money, fees, payments | `live` fees-and-income and payments. Legal goes to counsel. |
| CI, deploys, speed, errors | `live` ci-and-deploys, performance, errors, uptime-and-alerts |
| Two live records conflict, or "why is it this way" | `get`, `history`, `why`. Build to the newer, then `propose` retiring the older with the reason so one remains. A refusal is kept as a flag for the PM. |
| "What did we decide back then", or how an idea changed | `as_of`, `concept` |
| Judging a new tool or method | `review_method` |
| Writing or trimming docs | `how` docs |

If the store can't be reached, say so and work from the repo docs.

**Where we are:** `STATUS.md` (generated) and `python3 scripts/going.py --list now`.

## Where truth lives

- **How the system works:** the code in `socialus-web`. If the code can answer it, read the code, don't write it down.
- **Where each kind of thing goes:** `ops-pattern/process/WHERE-THINGS-GO.md` — one home per kind, budgets, generated vs maintained. Read it before writing any doc.
- **Why it is that way:** `PRINCIPLES.md` — the principles behind the Charter, few, reworded in place as they sharpen. Principles only: the lint names the home of anything else.
- **What was ruled:** under `## Rulings` in the scenario each ruling governs, moving verbatim to the spine or system doc when the scenario ships. One dated line per **live** ruling, words never edited; a superseded one is deleted and named in one `[replaces …]` tag on its replacement; git holds the rest.
- **What is decided but not built:** `planning/` scenarios with `status: approved` (their `horizon` and `rank` order them), and the socialus-web milestones.
- **Anything that spans the project** — open questions, which check guards which criterion, which ruling binds which tier, which risk is due — **is generated from inline markers, never maintained.** The pattern, and what it refuses: `ops-pattern/process/LIVING-DOCS.md`.
- **What is not yet decided:** an `[open-question owner=… raised=…]` marker, inline where the question was raised — in the file its answer will change. Never a list: the index is `STATUS.md` § Open questions, generated. Grammar, placement and what closes one: `ops-pattern/process/PIPELINE.md` § Open questions; `scripts/lint.sh` enforces it.
- **What might be built someday:** `IMAGINE.md`. Nothing there is a commitment. Scenarios may not cite it.
- **What the product is:** `product/foundation/model.md` — the PM's own statement of the model. Every other product document answers to it; where one disagrees, the other is the thing to fix.
- **The product model:** `product/` — nouns, verbs, surfaces, systems. Must match the code and `model.md`. If it doesn't, fix the doc in the same session you notice.
- **What may never be broken:** the knowledge store (strength: absolute), not a file.
- **How work moves, and what went wrong before:** `ops-pattern/process/` — `PIPELINE.md` (the five kinds), `LESSONS.md` (condensed, never just grown), `LIVING-DOCS.md` (the pattern behind the generated docs, and why authored docs are pruned). Only `process/SETUP.md` (standing up a second machine; read once per machine, never per session) lives here.
- **The tooling:** `scripts/` is vendored from `ops-pattern`. A change to how a marker, lint or generated view works is method: make it in `ops-pattern` first, then copy the file here in the same session.

**A concept lives in exactly one place.** Two documents describing the same thing is how this repo has failed before, so routing it is a rule, not a preference:

- **`product/` — nouns, verbs, surfaces — is the spine.** Every entry carries its own status, so one line holds both horizons: *"responses: thumbs up now, four states later."* **The future version of a thing is a status on its existing entry, never a second description somewhere else.**
- **`IMAGINE.md` is a waiting room, not a parallel library.** It holds only ideas that do not yet have a noun, a verb, or a surface.
- **When an idea acquires one, it moves into the spine and leaves `IMAGINE.md`.** Entries move out. They are never copied out — a copy is two descriptions, which is the thing this rule exists to prevent.

**`product/systems/` is depth, not a competing status.** Systems docs describe *how* a concept works. **They never state whether it ships.** The spine owns status; systems own detail. That is why they are not a fourth tracking layer and why the one-place rule does not make them redundant — they are not a second answer to the same question, they are the answer to a different one. A systems doc that starts declaring what ships has drifted, and the fix is to move that sentence to the spine, not to delete the doc.

**The test: does it have a shape — a noun, a verb, or a surface? Then the spine. If not, `IMAGINE.md`.** Worked example: *responses* have a noun and a verb, so the eventual four-state design is a status line on the response entry in `nouns.md`. *The Ticketmaster thesis* has none of the three — it is a claim about a market, not a shape — so it stays in `IMAGINE.md` until something about the product gives it one.

If a directory isn't listed here, don't read it. Anything not in the tree is not current — git history is the archive (`git log`, tag `archive-2026-09`).

## Generated files

`STATUS.md`, `README.md`, `constraints/` and `PLATFORM-*.md` are written by scripts and **committed by a workflow, not by a person**. A hand-edit to either is lost on the next run.

| File | Written by | Runs |
|---|---|---|
| `STATUS.md` | `scripts/status.sh`, wrapping `scripts/state.sh` and `scripts/markers.py` | `.github/workflows/status.yml` — push to `main`, daily 13:05 UTC, and *Actions → status → Run workflow*, which works from a phone |
| `README.md` | `scripts/view.sh` | the same workflow |
| `dashboard/status-dashboard.html` (PM's dashboard), `DASHBOARD.md` (pointer) | `scripts/dashboard.py`, reading `socialus-web` | `dashboard.yml` daily, and by hand at handoff |
| `constraints/planning.md`, `constraints/code.md` | `python3 scripts/markers.py constraints` | by hand after a ruling changes — `scripts/lint.sh` fails until it is run |
| `PLATFORM-IOS.md`, `PLATFORM-ANDROID.md` | `python3 scripts/markers.py platform`, from `[platform …]` markers | by hand after a marker changes — `scripts/lint.sh` fails until it is run |

**Nothing here asks you to remember to run anything**, because a refresh that depends on someone thinking of it goes stale. To refresh by hand anyway: `bash scripts/status.sh`.

## State

- A scenario's state is its frontmatter `status`: `draft` → `approved` → `building`. Shipped scenarios are deleted at sync.
- `gates: launch` in scenario frontmatter means the beta, so the frontmatter stays as written.
- A ticket's state is its Issue label in `socialus-web`. Tickets never live here.
- What is approved for build is the scenario frontmatter (`status: approved`) plus the Issues in `socialus-web`. There is no separate bridge document — one existed, restated both sources, and went wrong.

## Who does what

| Who | Owns | Never |
|---|---|---|
| the PM | rulings, judgment, domain knowledge — may open Issues in `socialus-web` directly | reads more than the dashboard unless he asks |
| Cowork — `scope-scenario` `review-draft-scenario` `sync-roadmap` `trim-product-docs` `plan-feature` | this repo: scenarios, STATUS, PRINCIPLES, `product/`; may open Issues in `socialus-web` | commits code to `socialus-web`; hand-edits `README.md` |
| Code — `write-tickets` `build-ticket` `run-feature-pipeline` | `socialus-web`: architecture notes, issues, code, PRs; branches, PRs and merges here too | writes scenarios, STATUS, ROADMAP or rulings here |

Code is the architect. Any ticket touching schema, RLS, or routes starts with a ≤20-line architecture note in the Issue. Cowork reviews it in a comment. the PM sees it only if they disagree.

## Commits

- Cowork commits its own doc changes here, on a branch. Message: `docs: what`.
- Code commits in `socialus-web`, branch per ticket. Who merges and when the PM looks: `ops-pattern/process/PIPELINE.md` § Who checks what. A merge to main there deploys to production.
- **Every change goes by branch and PR** *(2026-10-05)*: main requires the `lint` check (ruleset "main: merges when green"), so a direct push is rejected. Auto-merge is on: `gh pr merge --auto --squash` merges once lint passes. The STATUS workflow earns the same check on its own commits (`.github/workflows/status.yml`).
- Anything bigger than a doc touch-up goes by branch and PR here. **Whoever does the work merges it, Code or Cowork** — self-merge is fine, and needs no approval and no second reviewer.
- Never cross-commit (guideline — the repo split enforces it). Never rewrite history ([production-asks-don]).

## Sessions

Two sessions in one working tree collide (lesson 9).

- **Every session's cwd is its own worktree — never the repo root,** read-only sessions too: the one-session-per-cwd guard keys on cwd.
- **Worktrees live beside the repo, not inside it:** `../worktrees/{repo}/{branch}`.
- **A session that isn't committing uses `git --no-optional-locks status`.** Plain `git status` writes `.git/index.lock`, and a sandboxed session may leave it stale.

## Naming

Schema names are durable; UI labels translate them. The table is in `product/foundation/nouns.md`. Language is pro-competition, for all Americans — see `product/foundation/what-this-is.md`.

- **Issue title:** `F060 · T142 · plain name`. Bugs/changes/chores: `bug · plain name` (or `change ·`, `chore ·`), with `Scenario: F###|none` in the body.
- **Branch:** `f060-t142-slug`. **Commit:** `F060/T142: what`.
- **Bugs/changes/chores carry the Issue number, not a ticket number** — they have no `T###`. Branch `bug-36-slug`, commit `bug #36: what` (likewise `change-`/`chore-`). Process work has no Issue (`ops-pattern/process/PIPELINE.md`), so it dates instead: branch `process-YYYY-MM-DD-slug`, commit `docs: what`. Every branch name carries something unique that needs no central counter — dozens of agents must be able to name a branch without asking anything.
- **Provenance is git:** `git log --grep F060` is everything built for that scenario.
