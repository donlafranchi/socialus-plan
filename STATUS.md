> **SETTLED — do not re-raise:** members are the investors and the only people paid out. "Ownership, not profit-share" is rejected. Legal/securities questions about this go to `socialus-legal` for counsel and never come back to the PM as a decision.

# STATUS

> ## Generated 2026-10-07 · 16:05 UTC
>
> **Disposable. Regenerating replaces this file wholesale** — nothing here is
> hand-maintained, and a hand-edit is lost on the next run. `git log -p
> STATUS.md` is the history.
>
> **Refreshed by `.github/workflows/status.yml`** — on every push to `main`
> here, daily at 13:05 UTC, and on demand from the Actions tab (*status →
> Run workflow*), which works from a phone. It commits only when the content
> moved, so a new revision of this file is never a bare heartbeat. Locally:
> `bash scripts/status.sh`.
>
> **Derived from:** `scripts/state.sh` against `socialus-web` @ `origin/main`
> `325bce4` (2026-10-07); `accepted-risks/*.json`;
> `planning/scenario-*.md` frontmatter; `ROADMAP.md`.
>
> **Answers "where is this project", not "what tickets exist."** The ticket
> list is `gh issue list`, which is always right; this is not a copy of it.

Beta **2026-10-30**, one metro — a soft target for testing, not a hard deadline. 23 days out; feature freeze 2026-10-30, also soft. Production launch April–May 2027.

**21 of 26 approved and building scenarios are unverified** — no check is marked as discharging any
of their criteria. Unmarked is unverified, not verified. § Guard coverage.

**Native apps: 7 gaps for iOS, 6 for Android** — `PLATFORM-IOS.md`, `PLATFORM-ANDROID.md`.

## Scenarios, by status

| approved | building | draft | deferred |
|---|---|---|---|
| 22 | 4 | 20 | 1 |

**Building:**
- F060 (Someone starts something without opening a shop)
- F061 (Someone creates a Page worth showing people)
- F069 (A non-business Page resolves everywhere, and holding several is ordinary)
- F070 (Every Page has a face, even without a photo)

**`building` is frontmatter, not evidence** — nothing checks it against a
branch or a commit.

## In the code repo

**89 issues open** in `socialus-web`, 17 launch-blocking:
- #220 F078 · Flagged content hides itself on the agent's call, and the poster is told why
- #221 F080 · Pictures of children: the uploader confirms, nothing is pre-screened, a report hides at once
- #222 F081 · One signup for everyone: four fields, and the zip sets the metro
- #223 F082 · One self-attestation before a first Page, selling and hosting alike
- #246 bug · What one member can read about another: the signed-in half of #241, and four member tables open to anyone
- #328 change · One expanding control at the bottom of Explore: search, filter, metro, map
- #329 bug · The location pill at the top doesn't remember the member's metro
- #330 change · The map opens on the chosen metro, searches within it, and remembers it
- #337 bug · The owner's composer offers 'Who sees this: Anyone' on a private Page
- #363 change · Page kinds: Business, Group, Organization — chosen, changeable, and shaping the Page
- #475 change · Area markers for places without an exact address, and stacked pins spread apart
- #486 F100 · An AI reads every reported Post first, and a person still makes the call
- #487 F101 · One scannable page of flagged and reviewed Posts, decided in one tap
- #488 F102 · The poster answers first, report misuse is tracked, and the platform holds steady Tuesday to Thursday
- #489 change · About, Terms and Privacy pages live before the first signup
- #490 change · Error tracking in production
- #491 change · Removed photos are actually deleted from storage

**100 PRs merged in the last fortnight.** The newest five:
- #481 2026-10-07 bug #477: the builders wait for /you's list before deciding what to create
- #474 2026-10-07 bug #439: the remaining read paths of an archived or deleted Page answer only its managers
- #473 2026-10-07 bug #439: an archived or deleted Page reaches only its managers, by every path
- #472 2026-10-07 change #458 + batch: the Page tidy and contained; Edit page in five cards; pencils; Posts row; location, email and archived-Page fixes (migration)
- #471 2026-10-07 chore: the Browser job finds its merge base (every ready PR's Browser check fails)

### Needs a look — not a claim that anything is wrong

*A commit naming a ticket is not proof the ticket is done: partial work
counts. Each row needs a look, not a close.*

- **#51 open, but T154 appears on main** — F059 · T154 · Browse reads Pages, not Items
- **#30 open, but T149 appears on main** — chore · T149 · Retire vendor routes for real
- **#16 open, but T126 appears on main** — F056 · T126 · Edit shop — image, description, values
- **#15 open, but T125 appears on main** — F057 · T125 · You gains a producer state

### Still on main, meant to be gone

- `/following` still present — src/app/following/page.tsx
- `members.maker_mode_enabled` still in the schema

## The ontology — what is declared

- **13 link types declared**, 11 built. Registry schema 2.
- **Declared but not built (2)** - the relationship is named and nothing writes it yet:
  - a Member supports a Page
  - an Announcement is at a Location
- **7 object types declared**: Member (live), Page (live), Item (live), Location (live), Place (live), Announcement (live), Tag (live).
- **Rejected as nouns (6)** - named so they stay rejected: Person, Creator, Organizer, Follower, Patron, Vendor.
- **37 handlers, of which 26 write no declared link.**
  Not a fault on its own - a handler may legitimately touch no relationship -
  but an undeclared link lives here if it lives anywhere:
  - builder.content_delete_all
  - builder.content_set_visible
  - group.archive
  - group.delete
  - group.member_join
  - group.member_leave
  - group.post_delete
  - group.post_edit
  - group.restore
  - group.unclaimed_claim
  - group.unclaimed_remove
  - group.unclaimed_restore
  - item.publish
  - member.business_jurisdiction.remove
  - member.business_jurisdiction.set
  - member.create
  - member.interests.add
  - member.place_interest.add
  - member.place_interest.remove
  - member.saved_search.remove
  - member.saved_search.restore
  - metro.waitlist_join
  - metro.waitlist_join_anonymous
  - report.create
  - report.decide
  - report.reverse

## What CI last said

- **`deploy-health.yml`** — success, 2026-10-05
  - Database reachable from the deployment: success
  - Ontology declarations still match the code: success
- **`ci.yml`** — failure, 2026-10-07
  - Lint, types, build: success
  - Unit tests: success
  - Migrations applied to production: failure
  - Which suites: success
  - Browser: success

## Measured, not estimated

- Copy: 584 strings across 118 files — source `docs/copy-inventory.md` on origin/main
- Routes on origin/main: 31
- Migrations on origin/main: 85

## Deferred on purpose — and therefore easy to forget

Ruled acceptable with a condition for looking again. The ruling itself is a
dated line in `DECISIONS.md`; the register is `accepted-risks/`.

**2 need a look now.**

- **observability: no error tracking in production** — **due in 9 days**
  - If forgotten: A runtime error for a real member is invisible. Nobody is paged, nothing is logged where anyone looks, and the first signal is a person giving up and not saying why. The DATABASE_URL outage went four months unnoticed for exactly this reason.
  - Look again if: ANY of: a member outside the team signs up; a bug is reported that nobody can reproduce; or 2026-10-16 passes with this still open.
- **storage: removed photo bytes stay fetchable by direct URL** — **due in 9 days**
  - If forgotten: A photo the operator removed stays downloadable, indefinitely, by anyone who has or can guess its storage URL. For ordinary bad content that is tolerable. For illegal content it is not, and 'we kept it so it could be reversed' is not a defensible answer to a regulator, a police request, or the person in the photo.
  - Look again if: ANY of: the first report of illegal content reaches the review queue; a member asks for their own photo to be actually deleted rather than taken down; a takedown demand arrives from outside the platform; or 2026-10-16 passes (two weeks before launch) with this still open.
- **data: two rows in public.places share the slug 'sacramento'** — review by 2026-11-30
  - If forgotten: A scoped link resolves to the wrong geography and nobody notices, because both answers look plausible. The heuristic makes it deterministic and therefore silent.
  - Look again if: ANY of: a member reports results from the wrong area; a third row appears with the same slug; a browse or scope read starts resolving places by SLUG rather than by id; or 2026-11-30 passes. (The T156 browse query rewrite landed 2026-09-19 and takes place and metro IDs, never slugs, deliberately — so that trigger did NOT fire and this stays a live tripwire for the next read that does.)
- **schema: reports.reviewed_at/reviewed_by_member_id/outcome duplicate report_decisions** — review by 2026-11-30
  - If forgotten: Two sources of truth drift. A write path that updates the decisions log and forgets the projection leaves a report invisible in the queue or double-counted against a reporter's cap, and the bug looks like a UI fault rather than a schema one.
  - Look again if: ANY of: a third writer of report_decisions appears; delegated reviewers land (more writers, more chances to drift); the queue shows a report whose status disagrees with its history; or 2026-11-30 passes.
- **unclaimed Pages: businesses' own photos shown without their permission** — review by 2026-11-30
  - If forgotten: A business finds its photo on a site it never agreed to and treats it as theft rather than a listing. One annoyed owner is a removal request; several, or one with a lawyer, is a copyright claim and a story about a platform that took local businesses' work without asking.
  - Look again if: ANY of: the first removal request or complaint about a photo; any takedown demand or legal letter; the listings grow beyond the first batch of 26 by automation (the daily job).

## Open questions

Every open-question marker, found by scanning — nobody maintains this list.
Oldest first. Rule and grammar: `ops-pattern/process/PIPELINE.md` § Open questions.


**Waiting on Don** (20)

- 33d · "Neighbours, not strangers or creators" vs. "everyone who posts is a creator." A) the north star's refusal is scoped to the word "creator" as a label only —… — [product/foundation/role-language.md:36](product/foundation/role-language.md#L36)
- 30d · Promise 1 — what "surplus returns to the community" actually means. A) a fixed percentage, decided annually by the founder. B) a member vote or board process… — [product/foundation/goals.md:48](product/foundation/goals.md#L48)
- 30d · The flourishing thresholds (40 discretionary hours/week, 1.5× adequacy margin). A) adopt as the literal north-star targets everywhere. B) keep them illustrat… — [product/foundation/metrics.md:18](product/foundation/metrics.md#L18)
- 25d · What triggers the LLM pass, and who approves its output? A) a scheduled job, proposals landing in a queue Don reviews. B) on demand, run when someone looks.… — [planning/scenario-F071.md:37](planning/scenario-F071.md#L37)
- 24d · How does the search dictionary grow? A) from tags creators create — every new tag is a word a real person chose for their own thing. B) from logged zero-resu… — [planning/scenario-F071.md:41](planning/scenario-F071.md#L41)
- 22d · Where do the premise strings live, given Don expects to update them often? Copy is inline in the components today — roughly 458 user-facing strings across 50… — [planning/scenario-F083.md:37](planning/scenario-F083.md#L37)
- 21d · Which noun does the paused ontology spike model first — Item or Page? The spike lives outside this repo, at `../socialus-ontology-spike/INTENT.md`. — [product/foundation/nouns.md:259](product/foundation/nouns.md#L259)
- 18d · What makes a thing "free", now that the free-things lens has nowhere to read from? Surfaced by the browse query rewrite (`socialus-web` T156, 2026-09-19), wh… — [planning/scenario-F059.md:46](planning/scenario-F059.md#L46)
- 18d · Which ten names are the collections, and does the picker suggest from a Page's tags? *(Narrowed 2026-09-19 — Don ruled membership is owner-set, so what is le… — [product/ui/surfaces.md:61](product/ui/surfaces.md#L61)
- 8d · Are the store apps the site in a native shell, or native screens on the same database? A) A shell around the site (Capacitor-style): every screen and server… — [product/ui/surfaces.md:64](product/ui/surfaces.md#L64)
- 7d · When "near me" returns, how does finding by neighbourhood fit "local = the whole metro" and "no distance shown"? A) A place filter the member types, not a ra… — [planning/scenario-F095.md:28](planning/scenario-F095.md#L28)
- 7d · What does "sends traffic back" mean on a card? A) The card's main action opens the venue's own event page; SocialUs keeps the summary. B) A secondary "from t… — [planning/scenario-F096.md:30](planning/scenario-F096.md#L30)
- 7d · How is a member-shared event marked until claimed? A) "Shared by a neighbour, not yet confirmed by the venue", with no RSVP until claimed. B) The same, with… — [planning/scenario-F096.md:32](planning/scenario-F096.md#L32)
- 7d · Does imported content follow relationship-based visibility and the signed-out front door like any announcement? A) Yes, exactly: an imported event is a publi… — [planning/scenario-F096.md:34](planning/scenario-F096.md#L34)
- 7d · What does the platform do when imported content breaks the sensitive-content ask (children, animals and pets, anyone who can't fend for themselves)? A) Repor… — [planning/scenario-F096.md:36](planning/scenario-F096.md#L36)
- 5d · Address-with-pin, neighbourhood list, or both, as recommended? Nothing is built until Don confirms. — [#315](https://github.com/donlafranchi/socialus-web/issues/315)
- 3d · How granular are Home's row categories, so businesses and group events read as different things? — [planning/scenario-F098.md:33](planning/scenario-F098.md#L33)
- 3d · What does "things you saved" mean at launch? There is no save today. — [planning/scenario-F098.md:38](planning/scenario-F098.md#L38)
- 3d · Do F091's time rows stay on Explore once Home carries them? — [planning/scenario-F098.md:41](planning/scenario-F098.md#L41)
- 1d · Should a private Page's post be able to reach anyone? The 2026-09-30 ruling says "A public announcement from a community-only or private group Page currently… — [#337](https://github.com/donlafranchi/socialus-web/issues/337)

**Cowork owes an answer** (3)

- 6d · Nothing opens an owner panel on Explore yet; what should, if anything? — [socialus-web src/components/browse/BrowseSurface.tsx:61](https://github.com/donlafranchi/socialus-web/blob/main/src/components/browse/BrowseSurface.tsx#L61)
- 2d · People by name: the spec shows followers by name to the owner (2026-09-30), while bug #246 closed member-field reads; this ships the count only until dispatc… — [#369](https://github.com/donlafranchi/socialus-web/issues/369)
- 1d · Badges are cut from beta, Locally owned included (DECISIONS 2026-10-06), but F037's eval still requires this claim card; retire F037 for beta or keep the car… — [socialus-web src/components/group/ShopPublicPage.tsx:394](https://github.com/donlafranchi/socialus-web/blob/main/src/components/group/ShopPublicPage.tsx#L394)

## Guard coverage

**21 of 26 approved and building scenarios are unverified — no check is marked
as discharging any criterion of theirs, so a contradiction in them cannot surface here.** Unmarked
is unverified, not verified: nothing says a check exists, and under `[guard-proves-itself]` that
counts as absent. A **partial** criterion has checks that cover only part of it, named with what
they leave out; parts never add up to covered. Full map: `python3 scripts/markers.py coverage`.

- **F059** · 0 of 12 covered · **partial: 5** · unclaimed: 1, 2, 2b, 2c, 3, 4, 6, 7, 8, 9, 10
- **F080** · 1 of 5 covered · unclaimed: 1, 2, 3, 4
- **F081** · 1 of 9 covered · **partial: 1, 5** · unclaimed: 2, 3, 4, 6, 8, 9
- **F091** · 3 of 7 covered · **partial: 1, 7** · unclaimed: 5, 6
- **F093** · 4 of 12 covered · **partial: 4, 5, 6, 8, 9** · unclaimed: 10, 11, 12
- **Unverified — no marked check at all** (21): F056, F057, F058, F060, F061, F063, F064, F065, F069, F070, F072, F074, F076, F077, F078, F082, F092, F099, F100, F101, F102

## Is `building` backed by code?

Each scenario whose frontmatter says `building`, against what names it in `socialus-web`: commits
and files on main, and branches. Frontmatter is a claim; this is the evidence.

- **F060** · 0 commits on main · 5 files naming it · 0 branches
- **F061** · 0 commits on main · 12 files naming it · 0 branches
- **F069** · **nothing in the code names it** — no commit, file or branch
- **F070** · 6 commits on main · 14 files naming it · 0 branches

## Gating launch — does each have an Issue?

Every scenario whose frontmatter says `gates: launch`, against the `socialus-web` Issues
naming it. Five approved gating scenarios once had none, and nothing noticed.

- **F058** (approved) · #62 closed, #61 closed, #13 closed, #12 closed
- **F076** (approved) · #194 closed, #193 closed, #77 closed
- **F078** (approved) · #220 open
- **F080** (approved) · #221 open
- **F081** (approved) · #222 open
- **F082** (approved) · #223 open
- **F093** (approved) · #252 closed, #215 closed
- **F100** (approved) · #486 open
- **F101** (approved) · #487 open
- **F102** (approved) · #488 open

**Rulings that bind code: 143.** Each names its Issue or scenario, or says it has nothing to build;
the lint fails one that does none of the three — the identity leaks sat eight days with no Issue.

- **2026-10-04** The palette is option A, "Anodised": a white base, navy `#24405A` for actions, and gold on — names #24405, **which is no `socialus-web` Issue or PR**
- **Nothing to build** (27), by their own tag: 2026-10-07 The beta is an open beta from the waitlist and signup, Sacra…; 2026-10-05 socialus-web is public, so its GitHub Actions minutes are fr…; 2026-10-05 Economy until beta: migrations are batched into fewer, stric…; 2026-10-05 Until the 2026-10-23 feature freeze there are no previews: o…; 2026-10-05 The accepted risk "the browser test suite never runs in CI" …; 2026-10-05 Before production (spring 2027) there is a staging site: a s…; 2026-10-05 voice.md and tone.md are merged into one file, product/found…; 2026-10-05 Moderation is designed to run unattended: one person operate…; 2026-10-05 Beta is 2026-10-30, a soft target for testing in one metro, …; 2026-10-04 The decision rule: look at 2–3 established precedents with l…; 2026-10-04 Builder agents fill the app daily with a varied roster of in…; 2026-10-04 Build rules for one machine: at most 2 changes building or t…; 2026-10-04 Before a PR is put in front of Don (needs-don), a separate r…; 2026-10-04 We need to be successful first to help our members, and we w…; 2026-10-02 Gatherings saved with the old 7-hour timezone error are thro…; 2026-10-01 Design tokens live in the app code as the single source of t…; 2026-10-01 We disclose member data only in response to valid legal proc…; 2026-09-30 Visibility currently defaults to social norms: what people w…; 2026-09-30 We are careful and supportive of our members, and we ask the…; 2026-09-30 The platform comes first, then its members, and every ruling…; 2026-09-30 Between members, we currently show a display name and avatar…; 2026-09-27 When a newer decision contradicts an older one, the newer on…; 2026-09-27 Cross-cutting documents are generated from inline markers, n…; 2026-09-27 Grep-built, never hand-kept: a fact lives inline where it is…; 2026-09-27 An open question is an inline marker where it was raised, no…; 2026-09-21 [guard-proves-itself] is the sixth process absolute: a check…; 2026-09-21 plainlanguage.gov governs user-facing copy, alongside voice.…

## Docs by review age

94 authored docs in `product/` and `planning/`; **0 not reviewed in 30 days**, and **91 carry no `reviewed:` date** (their age is their last commit, which any edit resets).
Reviewing one means reading it against `DECISIONS.md` and setting `reviewed:` in its frontmatter.

- `product/systems/places.md` — 28 days (last commit 2026-09-09)
- `product/systems/location.md` — 28 days (last commit 2026-09-09)
- `product/systems/action-layer.md` — 28 days (last commit 2026-09-09)
- `planning/scenario-F069.md` — 28 days (last commit 2026-09-09)
- `planning/scenario-F068.md` — 28 days (last commit 2026-09-09)
- `planning/scenario-F065.md` — 28 days (last commit 2026-09-09)
- `planning/scenario-F055.md` — 28 days (last commit 2026-09-09)
- `planning/scenario-F049.md` — 28 days (last commit 2026-09-09)
- `planning/scenario-F048.md` — 28 days (last commit 2026-09-09)
- `planning/search-dictionary-draft.md` — 24 days (last commit 2026-09-13)

## What this run could not verify

- **The 20 drafts.** Status alone does not say which are waiting
  on Don and which are simply unfinished.

