# STATUS

> ## Generated 2026-10-05 · 17:17 UTC
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
> `3492589` (2026-10-05); `accepted-risks/*.json`;
> `planning/scenario-*.md` frontmatter; `ROADMAP.md`.
>
> **Answers "where is this project", not "what tickets exist."** The ticket
> list is `gh issue list`, which is always right; this is not a copy of it.

Beta **2026-10-30**, one metro — a soft target for testing, not a hard deadline. 25 days out; feature freeze 2026-10-23, also soft. Production launch April–May 2027.

**18 of 23 approved and building scenarios are unverified** — no check is marked as discharging any
of their criteria. Unmarked is unverified, not verified. § Guard coverage.

**Native apps: 7 gaps for iOS, 6 for Android** — `PLATFORM-IOS.md`, `PLATFORM-ANDROID.md`.

## Scenarios, by status

| approved | building | draft | deferred |
|---|---|---|---|
| 19 | 4 | 20 | 1 |

**Building:**
- F060 (Someone starts something without opening a shop)
- F061 (Someone creates a Page worth showing people)
- F069 (A non-business Page resolves everywhere, and holding several is ordinary)
- F070 (Every Page has a face, even without a photo)

**`building` is frontmatter, not evidence** — nothing checks it against a
branch or a commit.

## In the code repo

**0 issues open** in `socialus-web`, none launch-blocking.

## Deferred on purpose — and therefore easy to forget

Ruled acceptable with a condition for looking again. The ruling itself is a
dated line in `DECISIONS.md`; the register is `accepted-risks/`.

**3 need a look now.**

- **observability: no error tracking in production** — **due in 11 days**
  - If forgotten: A runtime error for a real member is invisible. Nobody is paged, nothing is logged where anyone looks, and the first signal is a person giving up and not saying why. The DATABASE_URL outage went four months unnoticed for exactly this reason.
  - Look again if: ANY of: a member outside the team signs up; a bug is reported that nobody can reproduce; or 2026-10-16 passes with this still open.
- **ci: playwright suite exists but no workflow runs it** — **due in 11 days**
  - If forgotten: The end-to-end tests rot. Nobody runs them, they drift from the app, and the day someone needs them they no longer pass for reasons unrelated to the bug being chased — at which point they get deleted instead of fixed.
  - Look again if: ANY of: a regression reaches production that a browser test would have caught; the Playwright suite fails to run locally when someone next tries it; or 2026-10-16 passes with this still open.
- **storage: removed photo bytes stay fetchable by direct URL** — **due in 11 days**
  - If forgotten: A photo the operator removed stays downloadable, indefinitely, by anyone who has or can guess its storage URL. For ordinary bad content that is tolerable. For illegal content it is not, and 'we kept it so it could be reversed' is not a defensible answer to a regulator, a police request, or the person in the photo.
  - Look again if: ANY of: the first report of illegal content reaches the review queue; a member asks for their own photo to be actually deleted rather than taken down; a takedown demand arrives from outside the platform; or 2026-10-16 passes (two weeks before launch) with this still open.
- **data: two rows in public.places share the slug 'sacramento'** — review by 2026-11-30
  - If forgotten: A scoped link resolves to the wrong geography and nobody notices, because both answers look plausible. The heuristic makes it deterministic and therefore silent.
  - Look again if: ANY of: a member reports results from the wrong area; a third row appears with the same slug; a browse or scope read starts resolving places by SLUG rather than by id; or 2026-11-30 passes. (The T156 browse query rewrite landed 2026-09-19 and takes place and metro IDs, never slugs, deliberately — so that trigger did NOT fire and this stays a live tripwire for the next read that does.)
- **schema: reports.reviewed_at/reviewed_by_member_id/outcome duplicate report_decisions** — review by 2026-11-30
  - If forgotten: Two sources of truth drift. A write path that updates the decisions log and forgets the projection leaves a report invisible in the queue or double-counted against a reporter's cap, and the bug looks like a UI fault rather than a schema one.
  - Look again if: ANY of: a third writer of report_decisions appears; delegated reviewers land (more writers, more chances to drift); the queue shows a report whose status disagrees with its history; or 2026-11-30 passes.

## Open questions

Every open-question marker, found by scanning — nobody maintains this list.
Oldest first. Rule and grammar: `ops-pattern/process/PIPELINE.md` § Open questions.


**Waiting on Don** (18)

- 31d · "Neighbours, not strangers or creators" vs. "everyone who posts is a creator." A) the north star's refusal is scoped to the word "creator" as a label only —… — [product/foundation/role-language.md:34](product/foundation/role-language.md#L34)
- 28d · Promise 1 — what "surplus returns to the community" actually means. A) a fixed percentage, decided annually by the founder. B) a member vote or board process… — [product/foundation/goals.md:46](product/foundation/goals.md#L46)
- 28d · The flourishing thresholds (40 discretionary hours/week, 1.5× adequacy margin). A) adopt as the literal north-star targets everywhere. B) keep them illustrat… — [product/foundation/metrics.md:16](product/foundation/metrics.md#L16)
- 23d · What triggers the LLM pass, and who approves its output? A) a scheduled job, proposals landing in a queue Don reviews. B) on demand, run when someone looks.… — [planning/scenario-F071.md:37](planning/scenario-F071.md#L37)
- 22d · How does the search dictionary grow? A) from tags creators create — every new tag is a word a real person chose for their own thing. B) from logged zero-resu… — [planning/scenario-F071.md:41](planning/scenario-F071.md#L41)
- 20d · Where do the premise strings live, given Don expects to update them often? Copy is inline in the components today — roughly 458 user-facing strings across 50… — [planning/scenario-F083.md:37](planning/scenario-F083.md#L37)
- 19d · Which noun does the paused ontology spike model first — Item or Page? The spike lives outside this repo, at `../socialus-ontology-spike/INTENT.md`. — [product/foundation/nouns.md:254](product/foundation/nouns.md#L254)
- 16d · What makes a thing "free", now that the free-things lens has nowhere to read from? Surfaced by the browse query rewrite (`socialus-web` T156, 2026-09-19), wh… — [planning/scenario-F059.md:46](planning/scenario-F059.md#L46)
- 16d · Which ten names are the collections, and does the picker suggest from a Page's tags? *(Narrowed 2026-09-19 — Don ruled membership is owner-set, so what is le… — [product/ui/surfaces.md:61](product/ui/surfaces.md#L61)
- 6d · Are the store apps the site in a native shell, or native screens on the same database? A) A shell around the site (Capacitor-style): every screen and server… — [product/ui/surfaces.md:64](product/ui/surfaces.md#L64)
- 5d · When "near me" returns, how does finding by neighbourhood fit "local = the whole metro" and "no distance shown"? A) A place filter the member types, not a ra… — [planning/scenario-F095.md:28](planning/scenario-F095.md#L28)
- 5d · What does "sends traffic back" mean on a card? A) The card's main action opens the venue's own event page; SocialUs keeps the summary. B) A secondary "from t… — [planning/scenario-F096.md:30](planning/scenario-F096.md#L30)
- 5d · How is a member-shared event marked until claimed? A) "Shared by a neighbour, not yet confirmed by the venue", with no RSVP until claimed. B) The same, with… — [planning/scenario-F096.md:32](planning/scenario-F096.md#L32)
- 5d · Does imported content follow relationship-based visibility and the signed-out front door like any announcement? A) Yes, exactly: an imported event is a publi… — [planning/scenario-F096.md:34](planning/scenario-F096.md#L34)
- 5d · What does the platform do when imported content breaks the sensitive-content ask (children, animals and pets, anyone who can't fend for themselves)? A) Repor… — [planning/scenario-F096.md:36](planning/scenario-F096.md#L36)
- 1d · How granular are Home's row categories, so businesses and group events read as different things? — [planning/scenario-F098.md:33](planning/scenario-F098.md#L33)
- 1d · What does "things you saved" mean at launch? There is no save today. — [planning/scenario-F098.md:38](planning/scenario-F098.md#L38)
- 1d · Do F091's time rows stay on Explore once Home carries them? — [planning/scenario-F098.md:41](planning/scenario-F098.md#L41)

**Cowork owes an answer** (1)

- 4d · Nothing opens an owner panel on Explore yet; what should, if anything? — [socialus-web src/components/browse/BrowseSurface.tsx:61](https://github.com/donlafranchi/socialus-web/blob/main/src/components/browse/BrowseSurface.tsx#L61)

**Not scanned this run:** open `socialus-web` Issues — `gh` could not read them.

## Guard coverage

**18 of 23 approved and building scenarios are unverified — no check is marked
as discharging any criterion of theirs, so a contradiction in them cannot surface here.** Unmarked
is unverified, not verified: nothing says a check exists, and under `[guard-proves-itself]` that
counts as absent. A **partial** criterion has checks that cover only part of it, named with what
they leave out; parts never add up to covered. Full map: `python3 scripts/markers.py coverage`.

- **F059** · 0 of 12 covered · **partial: 5** · unclaimed: 1, 2, 2b, 2c, 3, 4, 6, 7, 8, 9, 10
- **F080** · 1 of 5 covered · unclaimed: 1, 2, 3, 4
- **F081** · 1 of 8 covered · **partial: 1, 5** · unclaimed: 2, 3, 4, 6, 8
- **F091** · 3 of 7 covered · **partial: 1, 7** · unclaimed: 5, 6
- **F093** · 4 of 12 covered · **partial: 4, 5, 6, 8, 9** · unclaimed: 10, 11, 12
- **Unverified — no marked check at all** (18): F056, F057, F058, F060, F061, F063, F064, F065, F069, F070, F072, F074, F076, F077, F078, F082, F092, F099

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

- **F058** · not checked — `gh` could not read Issues
- **F076** · not checked — `gh` could not read Issues
- **F078** · not checked — `gh` could not read Issues
- **F080** · not checked — `gh` could not read Issues
- **F081** · not checked — `gh` could not read Issues
- **F082** · not checked — `gh` could not read Issues
- **F093** · not checked — `gh` could not read Issues

**Rulings that bind code: 115.** Each names its Issue or scenario, or says it has nothing to build;
the lint fails one that does none of the three — the identity leaks sat eight days with no Issue.

- **Nothing to build** (19), by their own tag: 2026-10-05 Beta is 2026-10-30, a soft target for testing in one metro, …; 2026-10-04 The decision rule: look at 2–3 established precedents with l…; 2026-10-04 Builder agents fill the app daily with a varied roster of in…; 2026-10-04 Build rules for one machine: at most 2 changes building or t…; 2026-10-04 Before a PR is put in front of Don (needs-don), a separate r…; 2026-10-04 We need to be successful first to help our members, and we w…; 2026-10-02 Gatherings saved with the old 7-hour timezone error are thro…; 2026-10-01 Design tokens live in the app code as the single source of t…; 2026-10-01 We disclose member data only in response to valid legal proc…; 2026-09-30 Visibility currently defaults to social norms: what people w…; 2026-09-30 We are careful and supportive of our members, and we ask the…; 2026-09-30 The platform comes first, then its members, and every ruling…; 2026-09-30 Between members, we currently show a display name and avatar…; 2026-09-27 When a newer decision contradicts an older one, the newer on…; 2026-09-27 Cross-cutting documents are generated from inline markers, n…; 2026-09-27 Grep-built, never hand-kept: a fact lives inline where it is…; 2026-09-27 An open question is an inline marker where it was raised, no…; 2026-09-21 [guard-proves-itself] is the sixth process absolute: a check…; 2026-09-21 plainlanguage.gov governs user-facing copy, alongside voice.…

## What this run could not verify

- **The 20 drafts.** Status alone does not say which are waiting
  on Don and which are simply unfinished.

