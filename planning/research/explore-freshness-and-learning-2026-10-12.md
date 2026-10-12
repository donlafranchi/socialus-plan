# Explore freshness, learning about a member, a test profile and a regional seed (2026-10-12)

Asked for by the PM: show new and interesting things on every revisit, learn about a member from what they search for, build a test profile for the PM, and add businesses from Napa Valley to Truckee, South Lake Tahoe, Lodi, Yuba and Colusa. Draft scenarios: F112 (tool-side freshness, beta), F113 (what we learn), F114 (test profile), F115 (regional seed). The fun-side feed is designed here only, after beta, and is not a scenario.

**How sources are marked.** **[V]**: the page was read this session. **[S]**: only a search snippet or a secondary write-up was seen. **[A]**: assumed, verify before building. **[C]**: read in `socialus-web` main at `0e5ee14`.

## Two sides, and what conflicts

**The newer direction (the PM, 2026-10-12; `IMAGINE.md` § Two sides, `PRINCIPLES.md`):** the app has two sides. **The tool** is finding something specific, like Yelp: place and time order, and search. **The fun** is exploring with nothing in mind, more like Instagram or TikTok, and the algorithm is for that side. The fun side is after beta and not ready for council. Earlier stances that go against it are tagged `[for now]` and listed for review in `planning/research/two-sides-conflicts-2026-10-12.md`; none is treated as a blocker here.

**Conflicts this note touches** (noted, not resolved):
- Charter flip 1, "never by what holds your attention" and "Browse is complete, not ranked by your interests": the fun side ranks by interests and is engagement-aware (§ 2). The tool side keeps place and time.
- F059's 2026-09-12 ruling, "behaviour read back at the member may not": tool-side "not seen yet" (§ 1) and suggestions from behaviour (§ 3) read behaviour back at the member.
- F098 criterion 4, no input measures opens or dwell: the fun side's objective uses opens and saves; dwell stays out (§ 2).
- No pay-to-rank on the fun side is **assumed, not decided** (open question in the conflicts note).

**Rules still standing that this fits:** collect data to benefit members with an easy opt-out (2026-10-11); the F109 open log, staff-side with opt-out (2026-10-12); member to member strict, staff have access, no tools that target one member (2026-10-09); sharing opt-in and private by default (PRINCIPLES); no distance anywhere (2026-09-30); a Page in a waiting market on no surface until it opens (F104); members self-correct before staff work (2026-10-11); unclaimed Pages carry the business's own credited photo, the Unclaimed tag, claim and remove (2026-10-05).

**Already built [C].** PR #558 shuffles Explore once per session: four recency bands (2, 7 and 30 days, then older), and inside a band an order from a hash of a session cookie (`su_seed`) and the row id (`src/lib/browse/session-shuffle.ts`). Lenses are `recent | soonest | newest` plus tags and time rows. No "seen" tracking, no search log, no learning opt-out and no F109 open log exist yet. `member_interests` and `member_follows` read self-only since 2026-09-30. `item_responses` (RSVP, save) exists but only the persona seed writes to it. Home is paused and redirects to Explore.

## 1. Freshness on the tool side (beta)

The tool side keeps place and time as the order. Freshness acts only inside a ring band and a recency band.

### Precedents
- **Front Porch Forum**: "no algorithm; everyone using the service sees the same content in their geographic area"; human moderators review every post; a slow pace, no endless scroll [V] ([Wikipedia](https://en.wikipedia.org/wiki/Front_Porch_Forum)). Fresh because of a daily cadence and place, not because of ranking. One issue a day: [S].
- **Nextdoor**: machine learning ranks posts "most likely to matter to you" and re-engages lapsed members [V] ([Nextdoor blog](https://blog.nextdoor.com/whats-new-on-nextdoor-product-updates-1)). Engagement-ranked; not the tool side's model.
- **Are.na**: "No ads, no personalized recommendations"; what you see comes from what you chose to follow [V] ([are.na](https://www.are.na/home)).
- **Instagram Following and Meta under the DSA**: chronological feeds of what you follow; in the EU, Search "based only on the words they enter" [V] ([Instagram](https://about.instagram.com/blog/announcements/favorites-and-following), [Meta](https://about.fb.com/news/2023/08/new-features-and-additional-transparency-measures-as-the-digital-services-act-comes-into-effect/)).
- **Bluesky custom feeds**: the member picks the feed, the platform supplies sensible defaults [V] ([Bluesky](https://bsky.social/about/blog/7-27-2023-custom-feeds)). The nearest thing to our lenses.
- **Mastodon trends**: moderator-reviewed, but counted from popularity [V] ([Mastodon 3.5](https://blog.joinmastodon.org/2022/03/mastodon-3.5/)). Popularity is attention: not on the tool side.
- **Spotify Discover Weekly**: new every Monday [V] ([Spotify](https://newsroom.spotify.com/tag/discover-weekly-mondays/)). The cadence transfers; the personalisation does not.
- **Airbnb**: making neighbouring results less alike helped in A/B tests [V] ([arXiv 2210.07774](https://arxiv.org/abs/2210.07774)).

### Research
- **Fair exposure over many rankings** (Biega, Gummadi and Weikum, SIGIR 2018): no one list can be fair, so make each item's visibility, summed over many lists, proportional to its relevance [V] ([arXiv 1805.01788](https://arxiv.org/abs/1805.01788)); Singh and Joachims, KDD 2018, the same idea per list [V] ([arXiv 1802.07281](https://arxiv.org/abs/1802.07281)). **This is the one that fits a local platform: every business gets its turn.**
- **Novelty and diversity** (Kaminskas and Bridge, ACM TiiS 2016): diversity goes with novelty, and novelty raises coverage [V] ([UCC](https://research.ucc.ie/en/publications/diversity-serendipity-novelty-and-coverage-a-survey-and-empirical/)). MMR re-ranking cuts redundancy [V] ([Carbonell and Goldstein 1998](https://people.eng.unimelb.edu.au/ammoffat/sigir98/abstracts/carbonell.html)); topic diversification raised satisfaction while lowering accuracy [S] (Ziegler et al., WWW 2005).
- **Impression discounting** (Lee et al., LinkedIn, KDD 2014): showing an item again and again lowers its response [V, slides] ([slides](https://slideshare.net/mitultiwari/impression-kdd)). The basis for "not seen yet first", and it needs a per-member record of what was shown.
- **Bandits and Thompson sampling** (Li et al. 2010 [V], [arXiv 1003.0146](https://arxiv.org/abs/1003.0146)): learn from clicks. Not on the tool side; on the fun side, only as the exploration share in § 2, tuned to the member-first objective, not to clicks.
- **DSA Article 27** (explain the main ranking parameters) and **Article 38** (very large platforms offer one option not based on profiling) [V, mirror] ([27](https://www.eu-digital-services-act.com/Digital_Services_Act_Article_27.html), [38](https://www.eu-digital-services-act.com/Digital_Services_Act_Article_38.html)). We are not bound; the tool side's place-and-time order is Article 38's option by construction, and is the fun side's off switch.


### Options
- **A) Not seen yet, then fair turns (recommended, decided).** Inside each ring band and recency band: Pages the member has not been shown in the last 14 days first; then Pages with the fewest showings in the market over the last 7 days; the session seed breaks ties. "Seen" is one row per member per Page with the last time shown (not one row per card shown), expiring after 30 days, signed in only; it is listed in "What SocialUs knows about you" and stops with the learning switch (§ 3). The market-wide count is per Page per day with no member id (like `map_mix_log`). No two cards in a row from one Page (TikTok's same-creator rule [V], [TikTok](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you)); a Page leads at most one lens row on the first screen; the leading lens row rotates by the day; a "New since you were here" divider. **Path: well-worn**: Lee et al. 2014, Biega et al. 2018, Front Porch Forum's cadence. Conflicts: the 2026-09-12 ruling, noted above.
- **B) A without the server record.** "Seen" kept in the reader's browser. No member data, works signed out, but it does not follow the member across devices and a cookie holds only a few hundred ids.
- **C) Fair turns only.** No "seen" at all; every business still gets its turn, but a member who visits daily can see the same cards on two days.

**Decision taken here: A** (F112), because the PM asked for not-seen-yet in beta and the per-Page row is small and expires on its own. B is the fallback if the server record is ruled out.

## 2. The fun side's feed (after beta, design only)

### How Instagram and TikTok do it
- **TikTok For You**: interactions (likes, shares, follows, comments, finishing a video), video information and device settings; a finished long video counts far more than a weak signal. Cold start: newcomers pick interest categories; those who skip get a general popular feed that learns from their first engagement. Generally no two videos in a row from one creator or sound [V] ([TikTok](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you)). Mixes in content outside a member's interests and breaks repetitive runs (December 2021) [S]. "Refresh your For You feed" starts over as if new, follows kept (2023) [S]. Topic sliders, more or less, not off (June 2025) [S].
- **Instagram**: a separate ranking per surface. Feed predicts likes, comments, shares, saves and profile taps from your history with the account; Explore leans on popularity and how fast a post is gaining engagement; Reels predicts reshares and completion [V] ([Instagram Ranking Explained](https://about.instagram.com/blog/announcements/instagram-ranking-explained)). Controls: Not interested, Sensitive Content Control, "Why you're seeing this", Reset suggested content (November 2024) [S]. Teen accounts: a 60-minute prompt and a sleep mode (September 2024) [S].

### What we would avoid, and why
1. **Ranking on raw engagement.** A preregistered audit found Twitter's engagement ranking amplified angry, hostile content that users said they did not want (Milli et al., PNAS Nexus 2025) [V, preprint] ([arXiv 2305.16941](https://arxiv.org/abs/2305.16941)).
2. **Treating behaviour as preference.** Impulse and considered preference differ; engagement learns the impulse (Kleinberg, Mullainathan and Raghavan, 2022) [S] ([arXiv 2202.11776](https://arxiv.org/abs/2202.11776v3)).
3. **Counting comments and reactions as "meaningful".** Facebook's 2018 change rewarded outrage, per the 2021 Facebook Files [S] ([summary](https://electionlawblog.org/2021/facebook-tried-to-make-its-platform-a-healthier-place-it-got-angrier-instead/)).
4. **Infinite scroll, autoplay, push nudges.** The European Commission's preliminary finding against TikTok (2026-02-06) names all three plus its personalised recommender, and asks for breaks and a redesigned recommender [V] ([Commission](https://digital-strategy.ec.europa.eu/en/news/commission-preliminarily-finds-tiktoks-addictive-design-breach-digital-services-act)).
5. **Paying people to watch.** TikTok Lite Rewards was withdrawn from the EU for good (2024) [S].
6. **Rabbit holes.** DSA proceedings against Meta (May 2024) over narrowing loops in minors [S].
7. **Weighting how fast a post spreads.** Instagram Explore's velocity signal favours accounts built for attention over a new local maker [V, as above].
8. **Dwell and completion as the target.** YouTube moved away from raw watch time because "not all watch time is equal" [S] ([YouTube](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/)).

### Member-first design (proposal)
- **Cold start from what the member says**: interests picked at signup or first visit (TikTok's picker), plus the tool side's place and time, plus newly opened Pages. No popular-feed fallback.
- **Interests shown and editable**: every interest, declared or inferred, listed with its reason ("from 4 RSVPs"), removable, with a slider for more or less (TikTok Manage Topics); one-tap reset (TikTok Refresh, Instagram Reset); "Why this?" on every card. Facebook's 2019 "Why am I seeing this?" without real controls did not build trust [S], so the reason always comes with the control.
- **Rank on what members value, not on time**: weights tuned to "I'm coming", saves, follows and "more like this", checked against a short monthly question, "Did SocialUs help you find something good or meet people?" (YouTube's survey-based valued watch time [S]; Facebook's "worth your time" survey [S]).
- **A finite batch and a stop card**: about 20 cards, then "You've seen what's new" (Instagram's "You're all caught up", 2018 [S]; already ruled for Home 2026-10-04). No autoplay, no infinite scroll, no push to return.
- **Exploration by rule**: a fixed share of slots, about 15% [A], from outside the member's interests, spread across topics; at most one card per Page in any five (TikTok's rule).
- **Fair exposure**: a floor of showings for new and small Pages (Singh and Joachims 2018 [V]); nothing paid enters the ranking (assumed, open).
- **Member's choice of feed**: the fun feed, or Following newest first, or a lens (Bluesky's chosen feeds [V]); off means the tool side, nothing blank (YouTube's blank Home criticised [S]).
- **Draft objective, ours, not from a source**: score = 5 · P(said "I'm coming" and went) + 2 · P(save) + 2 · P("more like this") + 1.5 · P(follow) + 1 · P("I'm coming") + 1 · interest match + 0.5 · soon and in the member's rings − 4 · P("not interested") − 3 · P(hide or report). **Not inputs**: dwell, scroll depth, session length, completion, comment counts, spread velocity, payment. Time spent is a warning light: up is a question, not a win.

## 3. Learning about a member (both sides)

### Precedents
- **Pinterest, "Refine your recommendations"**: tabs for activity, boards, interests and following; any can be turned off; ads are separate [V] ([Pinterest](https://help.pinterest.com/en/article/tune-your-home-feed)).
- **Spotify, "Exclude from your taste profile"**: listens still recorded but count less, within about 48 hours [V] ([Spotify](https://support.spotify.com/article/exclude-playlists-or-tracks-from-your-taste-profile/)).
- **YouTube**: delete one history item, pause watch and search history, "Don't recommend channel" [V] ([YouTube Help](https://support.google.com/youtube/answer/6342839?hl=en)); with history off, Home goes blank, criticised as a dark pattern [S].
- **TikTok, "Refresh your For You feed"**: starts recommendations over as if new, Following untouched [V] ([TikTok](https://newsroom.tiktok.com/more-ways-to-discover-new-content-and-creators-you-love)). **Instagram, "Reset suggested content"** (2024–25) [S].
- **Google My Ad Center**: inferred topics shown, editable, one switch off [S]. **Auto-delete** of search history at 3, 18 or 36 months, 18 the default for new accounts since 2020 [S] ([9to5Google](https://9to5google.com/2020/06/24/google-auto-delete-history/)).
- **Goodreads, Threads**: interests the member declares, suggestions pre-filled [S].
- **Research**: implicit signals (opens, views) measure confidence, not preference (Hu, Koren and Volinsky, ICDM 2008) [S]; scrutable user models, a member can see and change what the system believes (Kay, CHIIR 2021) [S]; "Why am I seeing this?" without controls did not build trust, and its explanations were often incomplete (Andreou et al., NDSS 2018) [S].
- **Law (not advice; for `socialus-legal`)**: California's final ADMT rules (approved 2025-07-24) cover only "significant decisions" (money, housing, school, work, health); a Home feed of events is outside them on our reading [V] ([Morgan Lewis](https://www.morganlewis.com/pubs/2025/08/cppa-board-finalizes-new-rules-on-admt-cybersecurity-audits-and-risk-assessments)). CCPA rights to know, delete and correct apply only above its thresholds [A], and are cheap to meet anyway.


### What we would learn, and which side uses it

| Signal | Strength | Kept | Tool side (beta) | Fun side (after beta) |
|---|---|---|---|---|
| A declared interest | strong | until removed | Home rows | cold start, ranking |
| A follow | strong | until unfollowed | Home's following row (built) | ranking |
| "I'm coming" / RSVP | strong | 90 days after the date [A] | suggestions | ranking, the objective |
| A save, "more like this", "not interested" | strong | 90 days [A] | — | ranking |
| A search | weak | 90 days [A] | recent searches; suggestions; staff "found nothing" counts | inferred interests |
| A Page open from Explore (F109) | weak | 90 days [A] | suggestions; N per category (staff, aggregate) | inferred interests |
| Seen (§ 1) | — | 30 days | not seen yet first | not seen yet first |

On both sides: nothing changes what another member sees or what a Page owner sees about a member. On the tool side, search relevance and place-and-time order do not change.

### Options
- **A) One store the member can see, from beta (recommended).** Every signal above goes into one place the member sees: "What SocialUs knows about you" in You, each item deletable, and one switch, **Learn from what I do**, on by default as the data ruling and F109 have it, which stops learning and the F109 log and deletes raw signals. In beta the store drives only not-seen-yet and **suggestions the member accepts** ("Add trivia to your interests?"). After beta the fun side reads the same store and shows inferred interests with their reasons. Raw signals expire on their own, so nothing needs an operator. Conflict: the 2026-09-12 ruling (suggestions read behaviour back).
- **B) Collect from beta, show it when the fun side ships.** Cheapest beta (the F109 log and seen only, plus a stored search log); members cannot see what is kept until the fun side lands. Against Kay's scrutability and the trust the Charter asks for; the opt-out still has to exist (F109).
- **C) Collect only what beta uses.** Seen and the F109 log; no search history kept until the fun side is scoped. Least data; the fun side starts cold and the test profile has little to show.

**For the PM: A, B or C** (member trust, new territory). F113 is written to A.

## 4. The PM's test profile

**What exists [C].** Builder accounts (`builders` table, `scripts/builders.ts` through a GitHub workflow): a builder's follows, joins and RSVPs to real Pages do not count, and `delete_builder_content()` removes everything a builder made. The persona seed (`scripts/seed-personas.ts`) refuses any host that is not local. The operator account is a break-glass holding every permission (`OPERATOR_MEMBER_ID`). There is one remote Supabase project; previews use it.

### Options
- **A) A builder account in production, seeded by a script (recommended).** A second account, signed in with a PM test address, home zip in the Sacramento market, flagged builder so none of its activity counts and it can be wiped in one call. A script (`scripts/test-profile.ts`, dry run unless `--apply`) writes six weeks of history against real seeded Pages. The PM uses it on a phone, on the real data, without touching the operator account. Builder signals must be left out of staff counts and the F109 report.
- **B) The PM's own production account.** Least setup; mixes test history into the operator break-glass and into staff metrics, and wiping it wipes real history.
- **C) A local persona only.** Safest; the PM cannot use it on a phone or against the regional seed.

**For the PM: A, B or C.** The spec is F114.

## 5. Regional seed (build plan; no data loaded)

### Data
- **Overture Maps Places**, release `2026-09-23.1` [V] ([getting data](https://docs.overturemaps.org/getting-data/)). Licence: CDLA Permissive 2.0 per source, the Foursquare part Apache 2.0 with its NOTICE file; **Places has no OpenStreetMap data, so no share-alike** [V] ([attribution](https://docs.overturemaps.org/attribution/)). Fields include name, category, websites, socials, phones, address, confidence and `operating_status`; **no photos** [V] ([schema](https://docs.overturemaps.org/schema/reference/places/place/)). A pull of the whole area, Napa to Tahoe and Lodi to Colusa, gave **188,281 places, 142,290 with confidence 0.7 or more and not closed** [V, this session]. Known issues: duplicates and junk; confidence says only that a place exists [V] ([guide](https://docs.overturemaps.org/guides/places/)).
- **Not usable**: Google Places ("must not pre-fetch, cache, or store", only the place ID) [V] ([policy](https://developers.google.com/maps/documentation/places/web-service/policies)); Yelp ("create your own database" barred) [V] ([terms](https://terms.yelp.com/developers/api_terms/)); OpenStreetMap inside our Pages table makes it a derivative database under ODbL [V] ([OSMF guideline](https://osmfoundation.org/wiki/Licence/Community_Guidelines/Produced_Work_-_Guideline)), so check against it only.
- **Sizing**: Census ZIP Business Patterns 2023 (employers only, so a floor) [V, downloaded].

### How many, per town and category

Consumer categories only: food and drink, shops and makers, wine, beer and farms, arts, recreation and outdoors, lodging, and personal services. Left out: finance, real estate, legal, health care, auto, home trades, places of worship (a congregation may make its own Page), government. Independent first: a row with an Overture `brand` comes after every row without one. Caps are guesses [A].

| Town | Market | Census employers | Overture food and drink | Cap |
|---|---|---|---|---|
| Napa | Napa County (waiting) | 3,079 | 868 | 250 |
| St. Helena | Napa County | 556 | 329 | 80 |
| Calistoga | Napa County | 253 | 127 | 60 |
| Yountville | Napa County | 91 | 65 | 40 |
| American Canyon | Napa County | 363 | 56 | 40 |
| Truckee | Nevada County (waiting), see below | 1,104 | 136 | 150 |
| South Lake Tahoe | Tahoe (waiting) | 1,065 | 231 | 150 |
| Lodi | San Joaquin County (waiting) | 1,796 | 424 | 200 |
| Yuba City | Sutter County (waiting) | 1,959 | 198 | 150 |
| Marysville | Yuba County (waiting) | 492 | 94 | 60 |
| Colusa | Colusa County (waiting) | 191 | 34 | 30 |
| Williams | Colusa County | 113 | 18 | 20 |

About 1,230 Pages. **Split per town**: food and drink 35%, shops and makers 25%, wine, beer and farms 15% (30% in the Napa Valley towns and Lodi, taken from shops), arts, recreation and outdoors 15%, lodging and personal services 10%.

**The Sacramento market comes first.** It is the only open market, so it is the only place the PM can search as a member; about 111 unclaimed Pages are planned there today [C]. Wave 1 fills it to about 1,500 with the same rules, across Sacramento, Davis, Woodland, Roseville, Folsom, Auburn, Placerville and the towns between. Wave 2 is the table above.

### Photos, sample posts, links
- **Photos follow the 2026-10-05 ruling unchanged**: the business's own photo from its own site or socials, credited and linked, removable on its own; the loader already falls back to free-licence category stock [C] (`src/lib/unclaimed/photos.ts`). Unsplash [V] ([licence](https://unsplash.com/license)) and Pexels [V] ([licence](https://www.pexels.com/license/)) allow this, with no implied endorsement; Wikimedia Commons town photos need author and licence shown [S]; Street View is barred [S].
- **Risk for `socialus-legal`, not a new question**: copying a business's own site photo has no licence behind it; credit, link and instant removal reduce it; about 2,700 Pages instead of 111 scales it. Sample posts with invented offers attributed to real businesses were already sent to counsel (`copy-voice-pass-2026-10-10.md` 5.6); the same scaling applies.
- **Links**: the loader checks every link and drops dead ones [C]; only the business's own site, phone and socials.
- **Credit line**: Overture and Foursquare attribution on a credits page. New copy, so to the PM with the build.

### Waiting markets, and how the PM browses them
- Every town in wave 2 is in a waiting market: `market_key` gives `county-<fips>` for a county with no row, and Tahoe is seeded waiting [C]. **By F104 criterion 4, the Pages appear on no surface until the market opens, and appear with no act on the day it does.** So loading early is safe, and opening a market is the moment they show.
- **Truckee** is in Nevada County, outside the seeded Tahoe market (Placer's and El Dorado's Tahoe subdivisions) [C]. Recommend adding the Truckee county subdivision to Tahoe: one row (F103 criterion 1), CCD name verified against TIGER first [A].
- **Gaps [C]**: nothing reads `markets` yet (the feed still uses `metro_polygons`), and Census Places for Napa, Truckee, Lodi, Yuba City, Marysville, Colusa and Williams are not in `places`. Both are needed before wave 2 can be checked by town.
- **Browsing them**: a staff-only **market preview**. A staff member with a new permission sets a vantage in a waiting market and sees it as if open, under a banner, "Preview: this market is waiting." Members see F105 criterion 4 unchanged. A Page URL in a waiting market is `noindex` until the market opens. Precedent: Shopify's theme preview, Webflow's staging, WordPress's private preview [A, not re-read]. Staff-only and inside the 2026-10-09 two-level ruling, so it is decided here (F115).

### Load mechanics
`scripts/unclaimed/overture.ts` pulls a bbox from the Overture release with DuckDB, filters (confidence 0.7 or more, open, consumer categories, deduplicated by name and 50 m [A]), caps by the table, and writes the listings JSON the existing loader reads. `scripts/unclaimed/load.ts --apply` does the rest. The Overture `id` and release go into `page_sources`. Monthly refresh: an Overture `permanently_closed` hides an unclaimed Page; a claimed Page is the owner's and is not touched.


## Order to bring to the PM
1. **What we learn about a member (A/B/C, § 3).** It decides what F113, the F109 log and the test profile's history hold, and the store the fun side will read.
2. **Where the test profile lives (A/B/C, § 4).**
3. Copy for the credit line, the suggestion prompt and the preview banner, with the builds.

Tool-side freshness (A) and the seed plan are decided here, path well-worn; Truckee joining Tahoe is a one-row default the PM can reverse. The fun side waits for the PM to scope it after beta.
