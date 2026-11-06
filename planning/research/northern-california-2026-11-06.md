# Northern California market and Explore order: research, 2026-11-06

Research only, read from `socialus-web` origin/main on 2026-11-06. Nothing in the app changed. It serves two rulings: the Explore order (F091) and the beta market (F103). Delete this note once both are ruled and placed.

## Explore against "this week, then later, then Pages"

**Mostly on order already. The exception is the main list under the shelves, which mixes Pages and posts by last update.**

| Surface | Today | Matches? |
|---|---|---|
| Shelves (signed in) | Updates from your Pages (14 days), then Next 7 days, then about 16 themed shelves that rotate daily. "Plan ahead: next month" is one of the rotating shelves | Nearly: "later" has no fixed place |
| Member posts | Rows by kind, below the shelves | n/a |
| Main list | Up to 6 lead items (tonight or this weekend, or new Pages; Pages only when nothing is new), then Pages and posts mixed, `updated_at desc`, shuffled within 2, 7 and 30-day bands | No |
| "What's happening today / this week / this weekend" rows | Shown only with the posts-only filter on | n/a |
| Signed out | Pages only, plus sign-in cards for Pages that posted | No "this week" |
| Search, grouped | Today, Next 7 days, This weekend, Coming up, then Pages by kind, then posts by kind | Yes |
| Search, "Show as one list" | Server order (match, then last update), Pages mixed in | No |

**Refinement-sized fixes (a reorder, no new control):**
1. Shelves: pin "Plan ahead: next month" at order 3 (`20261101200000_shelves.sql:93`), and optionally put Next 7 days first.
2. Main list: posts first, then Pages, keeping each one's order (`BrowseSurface.tsx:256-261`); take Pages out of the lead fallback (`lead.ts:93-95`).
3. Search's one-list view: time-ordered posts first, Pages last (`BrowseSurface.tsx:314-320`).

**Bigger than a reorder, so held by the freeze unless Don says otherwise:** sorting the main list by start time instead of last update (the session shuffle, #557, would go). Showing the "What's happening" rows by default would repeat the Next 7 days shelf.

**Replaced:** "everything mixed: Pages and posts together" (Don, 2026-10-16, #876). **Open:** where undated posts (news, sales) go (F091 marker).

## Where "Sacramento" is the market

**The name lives in two data rows and one constant, but Northern California as one market means adding counties, not only a rename.**

- **Data.** `markets` row `sacramento`, named "Sacramento": Sacramento, Yolo, Placer and El Dorado, less Tahoe (`20261012020000_markets.sql:68,77`). `metro_polygons` "Sacramento-Roseville, CA" (`031_metro_polygons.sql:135`), whose box was stretched to Stockton; Explore shows its name ("Results in …"). The ZIP crosswalk seed labels about 190 ZIPs to the Sacramento metro.
- **Code that keys on the slug.** `feed-metro.ts:18` (`DEFAULT_METRO_SLUG`), `zip-market.ts:11`, `boundaries.yml:14`, `scripts/boundaries/metros.ts:43`, about 10 market tests. Renaming the display name touches none of them; changing the slug touches all of them plus the metro cookie and saved links. **Recommend: keep the slug, change the name.**
- **Members see it.** Landing (`home-landing.ts:7`, "launching first in", "Starting in", "Not in Sacramento?"); `/open` (`open/page.tsx:27`); where-a-Page-is copy and placeholders (`page-where.ts:52,55`, `WhereFields.tsx`, `where-save.ts:51`); `RecruitmentGrid.tsx` (6 lines); staff metrics. None on `/join`, metadata, share titles or emails. All of it is copy, so it waits for Don's copy pass.
- **Assumes the city.** `unclaimed/load.ts:35,42` rejects Pages "outside the Sacramento area"; `unclaimed/plan.ts:113-119` puts a bare town in Sacramento County; the metrics pin to the city (`staff_roles_and_metrics.sql:106`). Map centres sit on Sacramento (`AreaPickMap.tsx:18`, `WhereFields.tsx:33`), which is fine for a Northern California default.
- **Seeding.** About 307 hits in 28 files in `scripts/unclaimed`, mostly data; `THEMES.md` lists anchor towns and 11 counties loaded.
- **Tests and evals.** 41 test files, 17 eval files, 96 `src` test files mention it, mostly as fixture addresses. Real city slugs (`sacramento-ca`) are the city and stay.
- **Plan docs.** F048, F049, F081, F093, F095, F103, F114, F115, the landing copy files, two briefs, `voice-and-tone.md`'s "in Sacramento" example, and generated constraints. Each changes when its ruling or copy changes, not before.

## Seeded Pages by county (364 in the ledger)

| County | Pages | In today's market |
|---|---|---|
| Sacramento | 133 | yes |
| Yolo | 53 | yes |
| Placer | 51 | yes |
| El Dorado | 27 | yes |
| Solano | 32 | waiting |
| Nevada | 27 | waiting |
| San Joaquin | 17 | waiting |
| Amador | 12 | waiting |
| Sutter | 6 | waiting |
| Yuba | 3 | waiting |
| Colusa | 2 | waiting |
| Tahoe (El Dorado) | 1 | Tahoe, waiting |

100 seeded Pages (27%) are in counties that sign-up still treats as waiting markets, though Explore shows them. #787 closed on Don's 2026-10-16 call: Pages within 45 to 60 minutes of Elk Grove, Davis, Lincoln, Auburn and El Dorado Hills. The 2026-10-27 drive-time ruling (#1101) would add Solano, Nevada, Sutter and Yuba, and is not built.

## Proposed boundary

- **A (recommended): the 11 counties already seeded and shown.** Sacramento, Yolo, Placer and El Dorado (less Tahoe), plus Solano, Nevada, Sutter, Yuba, Amador, Colusa and San Joaquin. Tahoe stays its own market. It matches what Explore already shows, so no seeded Page sits outside the market, and it is seven `market_members` rows. Those seven counties drop their own "open your town" goals.
- **B: the 2026-10-27 drive-time reach.** Adds Solano, Nevada, Sutter and Yuba; Amador, Colusa and San Joaquin stay waiting, and 31 seeded Pages stay outside.
- **C: wider (Napa to Redding, F115's wave 2).** Nothing is seeded there yet, and it stretches one beta's makers and goals thin.

Precedents: Craigslist names regions ("sacramento", "north bay") and draws them by hand; Nextdoor and Meetup open by area, not by a city's limits.
