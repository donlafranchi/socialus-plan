# Where "local" is defined and how it works — inventory (2026-10-11)

For F103 (draft). Read from `socialus-web` main `ea48b0c` and `socialus-plan` main today. Nothing here is a ticket; when F103 is approved, Code turns the **Change** rows into Issues. Supersedes F094's 2026-09-27 scope table for this purpose.

## 1. Definitions of "local" that exist, newest first
| Where | Says | Under F103 |
|---|---|---|
| DECISIONS 2026-10-11 (two lines) | money comes back to the community where it was generated; owner chooses, badge follows; the metro rulings were scaffolding, rings are the method | the definition |
| DECISIONS 2026-10-04 | the local-owner badge's area is the whole MSA | **replace**: owner local by the ladder **and** give-back to the business's town |
| DECISIONS 2026-09-30 ×3 | the metro for a zip is the MSA; "near you" out, "in Sacramento" stands in; "local" means where a thing is, not who may see it | first two **replace** (zip → subdivision → area; vantage copy); third **stands** |
| DECISIONS 2026-09-29 | the metro determines "local"; zip is only the lookup | **replace** |
| DECISIONS 2026-09-27 | "local" means the whole metro | **replace** on approval; stands for the code until then |
| F094 (draft) | local means the whole metro, with a scope table | **retire**; F103 replaces it |
| F081 crit. 3, 4, 7, 8 | zip determines the **metro**; every zip resolves to its **MSA** | **amend** to town/subdivision and area |
| F076 crit. 1, 2, 16 | every US **metro** selectable; metros ordered by waiting count | **amend** to markets (areas) |
| F049 (draft) | hood + metro pick at signup | **retire**; superseded twice already |
| F059 | Explore scopes to a metro (crit. 6); ranking by neighbourhood band ruled out | **amend**: scopes to the vantage's area, ordered by adjacency |
| `surfaces.md` § Metro is the feed's vantage point, § Distance is out, § A Member picks a hood and a metro | metro vantage; no miles; hood → metro → wider → online | proposed lines already added; **rewrite** on approval, "Distance is out" **stands** |
| `business-jurisdiction.md` | locality evidence is a ZIP; the test is same MSA | proposed line added; **rewrite** the test on approval |
| `voice-and-tone.md` § Rules | no "near you" or "nearby" while there is one metro; say "in Sacramento" | **amend**: say the vantage's town or area by name; still no "near you" as scoping |
| `planning/values-badges-draft.md` | Locally owned borrows AMIBA's test (≥50% owned by area residents) | **amend**: add the give-back condition |
| `socialus-design/research/BADGES-VALUES-KINDS-PLAN.md`, `screens/owner-page-spec.md` | badge section, kind line | **note** the two-condition badge; no mockup change until badges return |

## 2. Code that reads the metro or MSA as the unit (103 files match; the load-bearing ones)
| Path | Does | Under F103 |
|---|---|---|
| `supabase/migrations/031_metro_polygons.sql`, `resolve_home_metro()` | CSA polygon overlay; home metro from a point | **Change**: area row in `places` replaces the overlay; keep `csa_code`/`msa_code` as report columns |
| `025_zip_metro_crosswalk.sql`, `src/lib/signup/zip-metro.ts` (`MSA_METRO_SLUG` bridge) | zip → MSA → metro at signup | **Change**: zip → town/subdivision (Census ZCTA relationship files) → area |
| `20260914204920_metro_waitlist.sql`, `src/actions/metro/*`, `src/lib/metro/waitlist-*.ts`, `MetroWaitlistStep.tsx` | per-metro waitlist, thresholds, `is_open` | **Change**: key by area row; logic unchanged |
| `browse_feed(p_metro_id, p_place_id)` (`20260930230000_front_door_no_pins.sql`), `src/lib/feed/browse-feed.ts`, `src/lib/browse/scope.ts`, `src/lib/feed/feed-metro.ts` (`DEFAULT_METRO_SLUG`), `src/app/explore/load.ts`, `withheld-announcements.ts` | one polygon scope; metro resolution chain (requested → remembered → default → zip) | **Change**: scope to the vantage's area; order by town adjacency; vantage replaces the metro chain |
| `members.home_metro_id`, `members.default_metro_id`, `member.default_metro.set` | home and chosen metro | **Change**: home town already exists (primary-home Place); `default_metro_id` becomes the default vantage |
| `page_local_owner_badge()`, `zip_is_proximal_to_location()` (`20260930090000_registration_never_displayed.sql`, `024_member_business_jurisdictions.sql`) | same-MSA test | **Change**: same-town-or-area test plus give-back condition; badges are cut from beta so no deadline |
| `venue_nearby_items` (5 km), `venue_distance_meters` (`032_venue_distance.sql`), `VenuePublicPage.tsx` "What's happening nearby" | radius and distance | **Change → remove** (already F094's finding; venue pages are retired 2026-10-06) |
| `MarketSelector.tsx` (haversine 25 mi, "Near You"), `MarketPill.tsx`, `AreaPicker.tsx` "Choose your area", `ExploreSearchBar.tsx`, `src/lib/explore/place-label.ts` | metro picker and pill | **Change**: the pill becomes the vantage; `MarketSelector` **remove** |
| `src/components/cards/location.ts` (`neighbourhood: 'Nearby'`, `metro: 'Across the metro'`, `wider: 'Further out'`) | scale labels on cards | **Change** copy: name the town or area; Don's copy |
| `src/lib/metro/metro-time.ts`, `metro-week.ts`, `happening.ts` | one timezone, "the metro's time" | **Change** when the second area opens in another zone; Sacramento and Tahoe share one |
| `MetroNotCoveredPanel.tsx` "I'm looking for what's nearby", `landing-copy.ts` ("near you", "your area opens"), `layout.tsx`/`og-default` "the people near you", `HomeFeed.tsx`, `FeedEmptyState.tsx`, `useMapPages.ts` | copy | **Change** copy to the vantage's name; "near you" stays out as scoping |
| `OwnershipBadge.tsx`, `LocallyOwnedClaim.tsx`, `resolve-shop.ts` ("Claimed local owner", "not locally owned"), `types.ts` 'Local owner, national brand', `(dev)/card-gallery` | badge display and claim | **Change** when badges return: two conditions, "Says locally owned" wording stands |
| `src/lib/unclaimed/*` ("outside the metro", 'Local business') | unclaimed listings bounded by metro | **Change**: bounded by area |
| `scripts/build-metro-catalog.ts`, `scripts/boundaries/load.ts`, `src/app/api/boundaries/route.ts` | metro catalog and boundary serving | **Change**: areas and subdivisions from TIGER |
| `src/ontology/registry.json`, `objects.ts`, `links.ts` | ontology names metro | **Change**: add area, town, vantage |
| `evals/features/F035*`, `evals/fixtures/F037-claim.ts`, `evals/phase-1/members-augmentation.spec.ts` | tests assume metro | **Change** with their features |

**Stands as is:** `places` tree and geographies, `locations.place_id`, member primary-home Place, `member_location_affinities`, the floor of 10, "Distance is out", "local means where a thing is", the report path's per-metro hide bar (becomes per-area, same rule).

## 3. Order of work, when F103 is approved
1. Data only, no behaviour (beta-safe): area row, subdivision rows, zip → subdivision table, `csa_code` on the area row.
2. Gate and waitlist read the area row; `zip-metro.ts` becomes `zip-area.ts`.
3. Feed scope reads the vantage's area; adjacency table; order by hops.
4. Vantage: the pill accepts a typed place; session state.
5. Copy pass on the rows above (Don's words).
6. Retire `metro_polygons` readers; keep the codes for reports.
7. Badge, when badges return.
