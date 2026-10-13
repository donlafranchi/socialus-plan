# Explore freshness, learning about a member, a test profile and a regional seed (2026-10-12)

Asked for by the PM: show new and interesting things on every revisit, learn about a member from what they search for, build a test profile for the PM, and add businesses from Napa Valley to Truckee, South Lake Tahoe, Lodi, Yuba and Colusa. Sections 6–9: how Find and Discover look and feel, the switch, a categorization engine, and why TikTok's feed works. Draft scenarios: F112 (Find freshness, beta), F113 (what we learn), F114 (test profile), F115 (regional seed). The Discover feed is designed here only, after beta, and is not a scenario.

**How sources are marked.** **[V]**: the page was read this session. **[S]**: only a search snippet or a secondary write-up was seen. **[A]**: assumed, verify before building. **[C]**: read in `socialus-web` main at `0e5ee14`.

## Two sides, and what conflicts

**The newer direction (the PM, 2026-10-12; `IMAGINE.md` § Two sides: the tool and the fun, `PRINCIPLES.md`):** the app has two sides, internally named Find and Discover. **Find** (the tool) is finding something specific, like Yelp: place and time order, and search. **Discover** (the fun) is exploring with nothing in mind, more like Instagram or TikTok, and the algorithm is for that side. Discover is after beta and not ready for council. Earlier stances that go against it are tagged `[for now]` and listed for review in `planning/research/two-sides-conflicts-2026-10-12.md`; none is treated as a blocker here.

**Conflicts this note touches** (noted, not resolved):
- Charter flip 1, "never by what holds your attention" and "Browse is complete, not ranked by your interests": Discover ranks by interests and is engagement-aware (§ 2). Find keeps place and time.
- F059's 2026-09-12 ruling, "behaviour read back at the member may not": Find's "not seen yet" (§ 1) and suggestions from behaviour (§ 3) read behaviour back at the member.
- F098 criterion 4, no input measures opens or dwell: Discover's objective uses opens and saves; dwell stays out (§ 2).
- **Paid promotion on Discover is open for design after beta** (the PM removed no-pay-to-rank from Discover, 2026-10-12). Find keeps Charter flip 2's "no member can pay to rank above another". The test for any design is PRINCIPLES' member-benefit gate for paid visibility; "it funds the platform" fails alone.

**Rules still standing that this fits:** collect data to benefit members with an easy opt-out (2026-10-11); the F109 open log, staff-side with opt-out (2026-10-12); member to member strict, staff have access, no tools that target one member (2026-10-09); sharing opt-in and private by default (PRINCIPLES); no distance anywhere (2026-09-30); a Page in a waiting market on no surface until it opens (F104); members self-correct before staff work (2026-10-11); unclaimed Pages carry the business's own credited photo, the Unclaimed tag, claim and remove (2026-10-05).

**Already built [C].** PR #558 shuffles Explore once per session: four recency bands (2, 7 and 30 days, then older), and inside a band an order from a hash of a session cookie (`su_seed`) and the row id (`src/lib/browse/session-shuffle.ts`). Lenses are `recent | soonest | newest` plus tags and time rows. No "seen" tracking, no search log, no learning opt-out and no F109 open log exist yet. `member_interests` and `member_follows` read self-only since 2026-09-30. `item_responses` (RSVP, save) exists but only the persona seed writes to it. Home is paused and redirects to Explore.

## 1. Freshness on Find (beta)

Find keeps place and time as the order. Freshness acts only inside a ring band and a recency band.

### Precedents
- **Front Porch Forum**: "no algorithm; everyone using the service sees the same content in their geographic area"; human moderators review every post; a slow pace, no endless scroll [V] ([Wikipedia](https://en.wikipedia.org/wiki/Front_Porch_Forum)). Fresh because of a daily cadence and place, not because of ranking. One issue a day: [S].
- **Nextdoor**: machine learning ranks posts "most likely to matter to you" and re-engages lapsed members [V] ([Nextdoor blog](https://blog.nextdoor.com/whats-new-on-nextdoor-product-updates-1)). Engagement-ranked; not Find's model.
- **Are.na**: "No ads, no personalized recommendations"; what you see comes from what you chose to follow [V] ([are.na](https://www.are.na/home)).
- **Instagram Following and Meta under the DSA**: chronological feeds of what you follow; in the EU, Search "based only on the words they enter" [V] ([Instagram](https://about.instagram.com/blog/announcements/favorites-and-following), [Meta](https://about.fb.com/news/2023/08/new-features-and-additional-transparency-measures-as-the-digital-services-act-comes-into-effect/)).
- **Bluesky custom feeds**: the member picks the feed, the platform supplies sensible defaults [V] ([Bluesky](https://bsky.social/about/blog/7-27-2023-custom-feeds)). The nearest thing to our lenses.
- **Mastodon trends**: moderator-reviewed, but counted from popularity [V] ([Mastodon 3.5](https://blog.joinmastodon.org/2022/03/mastodon-3.5/)). Popularity is attention: not on Find.
- **Spotify Discover Weekly**: new every Monday [V] ([Spotify](https://newsroom.spotify.com/tag/discover-weekly-mondays/)). The cadence transfers; the personalisation does not.
- **Airbnb**: making neighbouring results less alike helped in A/B tests [V] ([arXiv 2210.07774](https://arxiv.org/abs/2210.07774)).

### Research
- **Fair exposure over many rankings** (Biega, Gummadi and Weikum, SIGIR 2018): no one list can be fair, so make each item's visibility, summed over many lists, proportional to its relevance [V] ([arXiv 1805.01788](https://arxiv.org/abs/1805.01788)); Singh and Joachims, KDD 2018, the same idea per list [V] ([arXiv 1802.07281](https://arxiv.org/abs/1802.07281)). **This is the one that fits a local platform: every business gets its turn.**
- **Novelty and diversity** (Kaminskas and Bridge, ACM TiiS 2016): diversity goes with novelty, and novelty raises coverage [V] ([UCC](https://research.ucc.ie/en/publications/diversity-serendipity-novelty-and-coverage-a-survey-and-empirical/)). MMR re-ranking cuts redundancy [V] ([Carbonell and Goldstein 1998](https://people.eng.unimelb.edu.au/ammoffat/sigir98/abstracts/carbonell.html)); topic diversification raised satisfaction while lowering accuracy [S] (Ziegler et al., WWW 2005).
- **Impression discounting** (Lee et al., LinkedIn, KDD 2014): showing an item again and again lowers its response [V, slides] ([slides](https://slideshare.net/mitultiwari/impression-kdd)). The basis for "not seen yet first", and it needs a per-member record of what was shown.
- **Bandits and Thompson sampling** (Li et al. 2010 [V], [arXiv 1003.0146](https://arxiv.org/abs/1003.0146)): learn from clicks. Not on Find; on Discover, only as the exploration share in § 2, tuned to the member-first objective, not to clicks.
- **DSA Article 27** (explain the main ranking parameters) and **Article 38** (very large platforms offer one option not based on profiling) [V, mirror] ([27](https://www.eu-digital-services-act.com/Digital_Services_Act_Article_27.html), [38](https://www.eu-digital-services-act.com/Digital_Services_Act_Article_38.html)). We are not bound; Find's place-and-time order is Article 38's option by construction, and is Discover's off switch.


### Options
- **A) Not seen yet, then fair turns (recommended, decided).** Inside each ring band and recency band: Pages the member has not been shown in the last 14 days first; then Pages with the fewest showings in the market over the last 7 days; the session seed breaks ties. "Seen" is one row per member per Page with the last time shown (not one row per card shown), expiring after 30 days, signed in only; it is listed in "What SocialUs knows about you" and stops with the learning switch (§ 3). The market-wide count is per Page per day with no member id (like `map_mix_log`). No two cards in a row from one Page (TikTok's same-creator rule [V], [TikTok](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you)); a Page leads at most one lens row on the first screen; the leading lens row rotates by the day; a "New since you were here" divider. **Path: well-worn**: Lee et al. 2014, Biega et al. 2018, Front Porch Forum's cadence. Conflicts: the 2026-09-12 ruling, noted above.
- **B) A without the server record.** "Seen" kept in the reader's browser. No member data, works signed out, but it does not follow the member across devices and a cookie holds only a few hundred ids.
- **C) Fair turns only.** No "seen" at all; every business still gets its turn, but a member who visits daily can see the same cards on two days.

**Decision taken here: A** (F112), because the PM asked for not-seen-yet in beta and the per-Page row is small and expires on its own. B is the fallback if the server record is ruled out.

## 2. Discover's feed (after beta, design only)

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
- **Cold start from what the member says**: interests picked at signup or first visit (TikTok's picker), plus Find's place and time, plus newly opened Pages. No popular-feed fallback.
- **Interests shown and editable**: every interest, declared or inferred, listed with its reason ("from 4 RSVPs"), removable, with a slider for more or less (TikTok Manage Topics); one-tap reset (TikTok Refresh, Instagram Reset); "Why this?" on every card. Facebook's 2019 "Why am I seeing this?" without real controls did not build trust [S], so the reason always comes with the control.
- **Rank on what members value**: weights tuned to "I'm coming", saves, follows and "more like this", checked against a short monthly question, "Did SocialUs help you find something good or meet people?" (YouTube's survey-based valued watch time [S]; Facebook's "worth your time" survey [S]).
- **A finite batch and a stop card**: about 20 cards, then "You've seen what's new" (Instagram's "You're all caught up", 2018 [S]; already ruled for Home 2026-10-04). No autoplay, no infinite scroll, no push to return.
- **Exploration by rule**: a fixed share of slots, about 15% [A], from outside the member's interests, spread across topics; at most one card per Page in any five (TikTok's rule).
- **Fair exposure**: a floor of showings for new and small Pages (Singh and Joachims 2018 [V]). **Paid promotion is open for design** (above); whatever it becomes, the floor for unpaid new and small Pages stays, and a promoted card says so.
- **Member's choice of feed**: the Discover feed, or Following newest first, or a lens (Bluesky's chosen feeds [V]); off means Find, nothing blank (YouTube's blank Home criticised [S]).
- **Draft objective, ours, not from a source**: score = 5 · P(said "I'm coming" and went) + 2 · P(save) + 2 · P("more like this") + 1.5 · P(follow) + 1 · P(opens a photo or video) + 1 · P("I'm coming") + 1 · interest match + 0.5 · soon and in the member's rings − 4 · P("not interested") − 3 · P(hide or report). **Not inputs**: scroll depth, comment counts, spread velocity; dwell and session length are the open time-spent choice (§ 9). Payment: open, with paid promotion (below). Under § 9 option B, a capped per-card time term joins it.

### Paid promotion (open, after beta)
The PM removed no-pay-to-rank from Discover (2026-10-12); how it works is a design after beta, not decided here. What a design would have to answer, from the rules that stand:
- **The member-benefit gate** (PRINCIPLES 2026-10-12): paid visibility must show what the member gains; "it funds the platform" fails alone.
- **Find is unchanged**: Charter flip 2 holds there, so a paid card does not reach Find's place-and-time order or search.
- **Disclosed**: a promoted card says it is promoted, the way Instagram's and TikTok's sponsored posts are labelled [A, not re-read]; US endorsement rules expect clear disclosure [A].
- **Bounded**: a fixed share of a batch, kept inside the member's interests and markets; the unpaid floor for new and small Pages stays; "not interested" and the learning switch apply to promoted cards too.
- **Fees favour no member over another** (2026-09-30): one price list, open to every Page.

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

| Signal | Strength | Kept | Find (beta) | Discover (after beta) |
|---|---|---|---|---|
| A declared interest | strong | until removed | Home rows | cold start, ranking |
| A follow | strong | until unfollowed | Home's following row (built) | ranking |
| "I'm coming" / RSVP | strong | 90 days after the date [A] | suggestions | ranking, the objective |
| A save, "more like this", "not interested" | strong | 90 days [A] | — | ranking |
| A search | weak | 90 days [A] | recent searches; suggestions; staff "found nothing" counts | inferred interests |
| A photo or video tapped or opened, counted per Page and per category (the PM, 2026-10-12) | medium: deliberate, one tap per item | counts by day, 90 days [A] | suggestions; which Pages lead with media | inferred interests; a key ranking term; more photo and short-video cards where members open them |
| A Page open from Explore (F109) | weak | 90 days [A] | suggestions; N per category (staff, aggregate) | inferred interests |
| Seen (§ 1) | — | 30 days | not seen yet first | not seen yet first |

On both sides: nothing changes what another member sees or what a Page owner sees about a member. On Find, search relevance and place-and-time order do not change.

### Options
- **A) One store the member can see, from beta (recommended).** Every signal above goes into one place the member sees: "What SocialUs knows about you" in You, each item deletable, and one switch, **Learn from what I do**, on by default as the data ruling and F109 have it, which stops learning and the F109 log and deletes raw signals. In beta the store drives only not-seen-yet and **suggestions the member accepts** ("Add trivia to your interests?"). After beta Discover reads the same store and shows inferred interests with their reasons. Raw signals expire on their own, so nothing needs an operator. Conflict: the 2026-09-12 ruling (suggestions read behaviour back).
- **B) Collect from beta, show it when Discover ships.** Cheapest beta (the F109 log and seen only, plus a stored search log); members cannot see what is kept until Discover lands. Against Kay's scrutability and the trust the Charter asks for; the opt-out still has to exist (F109).
- **C) Collect only what beta uses.** Seen and the F109 log; no search history kept until Discover is scoped. Least data; Discover starts cold and the test profile has little to show.

**Ruled A** (the PM, 2026-10-12, on #137): a member-visible profile of what we think they like, each item editable or deletable, from beta; the switch reads "Help me discover things I might like" or "I don't mind doing this myself"; built from app usage, searches, clicks and our categorizing. F113 carries the criteria. **Open**: collecting data the member is not shown (device, location); nothing is built until ruled.

## 4. The PM's test profile

**What exists [C].** Builder accounts (`builders` table, `scripts/builders.ts` through a GitHub workflow): a builder's follows, joins and RSVPs to real Pages do not count, and `delete_builder_content()` removes everything a builder made. The persona seed (`scripts/seed-personas.ts`) refuses any host that is not local. The operator account is a break-glass holding every permission (`OPERATOR_MEMBER_ID`). There is one remote Supabase project; previews use it.

### Options
- **A) A separate production test account whose activity counts nowhere, seeded by a script (recommended).** A second account, signed in with a PM test address, home zip in the Sacramento market, flagged builder so none of its activity counts and it can be wiped in one call. A script (`scripts/test-profile.ts`, dry run unless `--apply`) writes six weeks of history against real seeded Pages. The PM uses it on a phone, on the real data, without touching the operator account. Builder signals must be left out of staff counts and the F109 report.
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


## 6. How Find and Discover look and feel (after beta)

The PM, 2026-10-12: "One needs to be party and the other needs to be business like a mullet, business up front party in the back." **Find is business up front; Discover is the party in the back.**

### Find: business up front
**Feels like** checking a well-kept noticeboard: type, see what is on today and in which town, done in seconds.
- **Precedents.** Yelp: map and list together, one strip of filter and sort under the map [S] ([TechCrunch 2022](https://techcrunch.com/2022/08/02/yelp-updates-its-android-app-with-a-redesigned-home-feed-and-map-based-search/)). Airbnb: list and map split on desktop, a floating Map pill on a phone, the pattern F059 criterion 5 already follows [S]. Apple's HIG: search where people expect it, results as you type, scopes rather than complex filters, no blank empty state [S] ([HIG, Searching](https://developer.apple.com/design/human-interface-guidelines/searching); the page did not render here). Google Maps keeps its feed of business posts apart from search and the map [V] ([Google, 2020](https://blog.google/products/maps/discover-more-with-google-maps-community-feed)).
- **Look.** Light. An off-white ground, white cards, near-black text, grey second lines, one accent for pins, links and the selected chip. System fonts; body about 15px, meta 13px, card titles 17px semibold.
- **Cards.** Dense: about 90px tall, a 64–72px square photo on the left; three lines: name, "Town · category", "Today 7pm" or "Open till 9". No distance (2026-09-30). Thin dividers, small corners, no heavy shadows.
- **Behaviour.** Sticky search, results as you type, skeleton rows the exact shape of the cards so nothing jumps, a row of text chips (today, this weekend, events, makers, free), fades of 150ms at most. List and map by width as ruled.

### Discover: the party in the back
**Feels like** walking into the party: a dark room, one thing at a time filling the screen, one thumb to say "I'm coming."
- **Precedents.** TikTok, Reels and Shorts: one item full screen, vertical swipe, a rail of actions on the right, caption bottom-left over a dark gradient [S]. Spotify's 2023 Home feed: short vertical previews that lead to the real thing, with save, share and go to the artist [V] ([MusicTech](https://musictech.com/news/music/spotify-launches-tiktok-style-scrolling-feed-discovery-music)), the nearest model: a preview card that leads to a Page or a gathering. Airbnb Icons (2024): playful, in-house 3D illustration [S].
- **Look.** Dark, whatever the device setting: black ground, a bottom gradient, white type, one bright accent kept for "I'm coming". A bold display face for titles over the media.
- **Card.** One item per screen, full height; photo or video edge to edge; caption: Page, town, when, then two lines of the post, expandable. Rail: I'm coming, Save, Follow, Share; Not interested under "⋯". Touch targets 44px or more.
- **Motion.** Spring transitions, a small burst on "I'm coming". Video muted, `playsinline`, paused off screen, one sound control for the feed [V] ([WebKit](https://webkit.org/blog/6784/new-video-policies-for-ios/), [Chrome](https://developer.chrome.com/blog/autoplay)). Snap one card per flick: `scroll-snap-type: y mandatory` [V] ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/scroll-snap-type)) with `scroll-snap-stop: always` [A].
- **Access.** A pause control on anything that moves for over 5 seconds (WCAG 2.2.2) [V] ([W3C](https://www.w3.org/WAI/WCAG22/Understanding/pause-stop-hide.html)); with reduced motion, cross-fades, no autoplay, a still and a play button [V] ([MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)); captions on; named buttons; arrow keys on desktop, where the feed is a centred 9:16 column on dark.

### How the two meet
- **Two tabs, not one surface.** Instagram, Pinterest and Apple Music each give the immersive mode its own tab and turn it dark [S]. Snap merged its tabs in 2024, lost about a million North American users, and went back to five, saying its most engaged users preferred them [V] ([Engadget](https://engadget.com/apps/snap-is-seemingly-rethinking-that-simplified-app-154628101.html)).
- **The bottom nav stays visible on both**, so the way back to Find is always one tap. Tab labels and icons are copy, to the PM.

## 7. Switching today's Explore to Find, and opening Discover (after beta)

**Trigger, not a date: the first Discover slice passes the PM's phone check.** Until then nothing members see changes.

### Preconditions
1. **The in-flight branches land first**: F103's markets as rows and zip-picks-the-market (`socialus-web` branches `693-markets-are-rows`, `694-zip-picks-the-market`) and the home town (#695), so the feed reads `markets` before anything is split; and the copy drafts #681–#692 merge or close, so no string is drafted twice (the Explore wording draft is #683) [C].
2. **Beta has shipped.** F112 and F113 are on Find by then.

### Steps
1. **Discover slice 1, behind a flag.** A `/discover` route visible to staff and builder accounts only (the builder switch is the precedent [C]). Full-screen cards from existing Pages and posts, ordered by § 9's small-scale ranking, with categories from § 8; the rail's actions write to the § 3 store. No change to `/explore`.
2. **The phone check.** The PM tries it on a phone as the F114 test member; the UAT checklist gains a Discover journey.
3. **The switch, one PR.**
   - **Routes.** Find keeps `/explore` until its tab label is decided; if the label is "Find", `/find` becomes canonical and `/explore` 308-redirects with its query kept, so shared links still work (F059 criterion 10). `/map` follows Find. `/discover` opens to everyone signed in; signed out, a short preview and sign-in [A, the PM's call]. Which tab `/` lands on stays Find until data says otherwise, a later PM call.
   - **Server.** Find keeps `browse_feed` and `browseFeedAction` as they are. Discover gets its own `discover_feed` and `discoverFeedAction`; nothing on Find calls them, so Find's place-and-time order stays testable on its own. One card model is shared.
   - **Nav.** `BottomNav` goes from Explore and You (plus Create) to Find, Discover and You (plus Create) [C]. Labels and icons to the PM.
   - **Tests** [C]: `BottomNav.test.tsx`'s label arrays; the about 33 unit files and 17 source files that name `/explore`, through one route constant; the Playwright evals (F059's spec, `smoke/live.spec.ts`, `screens/routes.ts`, `speed/steps.ts` with a Discover step and budget); `_guard/must-fail`; `tests/changed-routes.test.ts`; the UAT checklist regenerated. New: a guard that Find never calls `discover_feed`, a reduced-motion test, and one for the stop card.
   - **Redirects.** `next.config.ts` entries for `/explore`, `/map` and `/business/:slug` follow Find [C].
   - **Events.** None exist for Explore today [C]. Add, under the learning switch and with builder accounts excluded: `find.search` (query, result count, market), `find.open` (F109), `discover.shown`, `discover.action` (I'm coming, save, follow, share, not interested, open), `media.open` (photo or video, Page, category; on Find and Discover), `discover.stop_card`, `nav.switch` (from, to; counts only), and `discover.dwell` only if the PM picks B in § 9.
4. **After the switch.** Watch the `nav.switch` counts and the § 9 measures for four weeks; Find's personal rows (following, coming up) stay on Find until then.

## 8. A categorization engine (beta: the profile in F113 needs it)

**What it does.** Gives every Page and post up to three categories from one shared list, from its own text, photo and any hashtags in its words, with a cheap model pass, so members' interests (§ 3) and Discover (§ 9) read the same keys.

**What exists** [C]: creator-typed tags (`tags`, `page_tags`, `post_tags`, with a safety review column); a fixed interest list (`INTEREST_VOCAB`); a `#` typed into a tag is ignored and post bodies are not parsed; unclaimed Pages' categories are used only to pick a stock photo and not stored; pgvector is enabled with unused `vector(1536)` tables; AI calls are raw `fetch` to the Messages API, run after a report with `after()` (F100's moderation, Haiku first with a Sonnet second opinion).

**Design.**
- **One list**: about ten top categories and sixty under them [A], the same keys as `INTEREST_VOCAB`, extended by a person, not by the model.
- **Internal categories, not hashtags**: the engine reads a post's words, a `#word` included, as plain text; categories are ours, assigned by the engine and editable by the owner and, on their own profile, by the member. Nothing asks a poster to type hashtags and no hashtag shows on a card, in line with 2026-10-11 (#619, #621: plain words, no hashtags). Ruled by the PM, 2026-10-12 (F113).
- **When**: on create or edit, after the save, like F100 (`after()`); the seed and any backfill through the Batch API at half price.
- **Input and output**: name, description or body, tags, hashtags, Overture's category for seeded Pages, and the first photo at 512px; out comes up to three categories with a confidence each, structured JSON.
- **Correction, members first**: the owner sees "Listed under: bakery, coffee" with Change; an owner's choice is pinned and a re-run does not overwrite it; on an unclaimed Page, staff fix it from a count of "wrong category" taps. Nothing needs ongoing operator work.
- **Similarity later**: embeddings into the existing pgvector tables when Discover needs "more like this" (§ 9); the embedding provider is a later choice [A].

**Cost per 1,000 items**, list prices (cached 2026-09-25): Haiku 4.5 $1 in / $5 out per million tokens, Sonnet 5.5 $2 / $10, Opus 5.5 $4 / $20; Batch API half. Assumed per item [A]: 1,500 tokens of instructions and list, cached; 300 tokens of text; about 350 for a 512px photo; 100 out.

| Model | Text only | With photo | Batch, with photo |
|---|---|---|---|
| Haiku 4.5 | $0.95 | $1.30 | $0.65 |
| Sonnet 5.5 | $1.90 | $2.60 | $1.30 |
| Opus 5.5 | $3.80 | $5.20 | $2.60 |

So the whole seed (about 2,700 Pages) costs about $2 to $14, and a year of posts at beta scale stays in the tens of dollars on any model [A]. Sonnet and Opus think by default and add tokens beyond this at higher effort. **Which model is the PM's call after a bake-off** on 100 hand-labelled items, the way bug triage was decided (2026-10-06).

## 9. Why TikTok's feed works, and what we can copy

### Why it works
1. **Interest graph, not social graph.** Nobody has to follow anyone first; the app learns from what you watch, so the feed is never empty [V] ([Wei, "TikTok and the Sorting Hat"](https://www.eugenewei.com/blog/2020/8/3/tiktok-and-the-sorting-hat)).
2. **Many clear signals per item.** Short items, so every minute yields dozens of judgments; finishing a video outweighs weak signals, and follower count is not a direct factor [V] ([TikTok](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you)). The WSJ's 100 bots were read in under 40 minutes, from watch time and rewatches [S].
3. **An objective built for daily use.** The leaked "TikTok Algo 101" scores predicted likes, comments, playtime and plays, toward time spent and retention, and docks categories already watched that day [S] (NYT, December 2021, via [The Batch](https://www.deeplearning.ai/the-batch/what-makes-tiktok-tick)).
4. **New items tried small, then widened.** A new video goes to a few hundred viewers and widens if they finish, like and share it [S] (Brennan, *Attention Factory*); staff can also "heat" videos by hand [S] (Forbes 2023, via [Tubefilter](https://tubefilter.com/2023/01/23/tiktok-for-you-page-heating-recommend-videos-algorithm/)).
5. **It learns in near real time.** ByteDance's Monolith trains and serves in one loop, keeps one embedding per id without collisions, expires stale ids and filters rare ones; fresher syncs kept improving accuracy [V] ([arXiv 2209.07663](https://arxiv.org/abs/2209.07663), RecSys 2022 workshop, in BytePlus Recommend).
6. **It understands content before anyone reacts.** Vision, text and speech models describe each upload, so a new video can be placed with no history [V] (ByteDance's LEMUR, [arXiv 2511.10962](https://arxiv.org/html/2511.10962v1)).
7. **The format is the sensor.** One full-screen item, autoplay, swipe on: every swipe is a clean yes or no about one thing, with no grid to choose from [V] ([Wei, "Seeing Like an Algorithm"](https://www.eugenewei.com/blog/2020/9/18/seeing-like-an-algorithm)). Plus rules: no two in a row from one creator, and items from outside your interests mixed in [V] (TikTok, above).

### What we can copy, at our size (best value for effort first)
1. **The format** (§ 6): one card, clear actions; a photo or video open is a tap per item, the signal the PM named (§ 3), and Discover leans to photo and short video where members open them. No data needed; this is most of TikTok's advantage.
2. **Content-based cold start**: categories (§ 8) now, embeddings of text and photo later; a member's taste is a recency-weighted mix of what they acted on. Works from the first day; Zalando's CLIP version lifted half-completed views 39% [V] ([arXiv 2507.19346](https://arxiv.org/html/2507.19346v1)).
3. **A market prior**: recent saves and "I'm coming" in the member's market, decaying over days. Needs tens of actions a week.
4. **Variety rules**: one Page per five cards, a cap per category per session, less of what was seen today. No data.
5. **Thompson sampling over categories**, with cautious priors from the market down to the member [V] ([Eugene Yan, "Bandits for Recommender Systems"](https://eugeneyan.com/writing/bandits/)). Needs hundreds of actions per category.
6. **Small-batch tests for new Pages**: show a new Page to 20–50 matched members, widen if saves or "I'm coming" beat its category [A, our design]. Needs a few hundred weekly members. It is also how a new maker gets seen.
7. **Session re-ranking**: nudge the next card toward what was just saved, from precomputed vectors [V] ([Huyen 2022](https://huyenchip.com/2022/01/02/real-time-machine-learning-challenges-and-solutions.html)).
8. **Later**: a learned two-tower model once there are tens of thousands of logged actions [S] ([Eugene Yan](https://eugeneyan.com/writing/system-design-for-discovery/)). **Skip**: Monolith-style real-time training; a nightly job plus session re-ranking is enough at a few thousand items.

### Time spent: an open choice for the PM
The PM lifted the attention rule for Discover, so whether time counts is a choice, not a rule. Evidence against: the European Commission's preliminary finding (2026-02-06) names infinite scroll, autoplay, push and the personalised recommender as addictive design [V] ([Commission](https://digital-strategy.ec.europa.eu/en/news/commission-preliminarily-finds-tiktoks-addictive-design-breach-digital-services-act)); engagement ranking amplified content users said they did not want [V] ([arXiv 2305.16941](https://arxiv.org/abs/2305.16941)).
- **A) Time as the goal** (session length, return visits): TikTok's way; the strongest signal; works against meeting in person and invites the Commission's findings.
- **B) Time per card only**: how long a card held someone counts as one signal about that card, capped, weighted below saves and "I'm coming"; session length is not a goal; a finite batch and a stop card stay. Keeps the densest signal for cold start.
- **C) No time at all**: rank on saves, follows and "I'm coming" only. Simplest to explain; thin signals at low volume, so new Pages are learned slowly.

Recommend B. § 2's draft objective is written without time; under B it gains one capped per-card term.

## Order to bring to the PM
1. ~~What we learn about a member~~: ruled A.
2. **Where the test profile lives (A/B/C, § 4)**, with the PM now.
3. Then, one at a time: time spent on Discover (A/B/C, § 9); the categorization model after its bake-off (§ 8); Discover's tab labels, icons and signed-out preview (§ 6, § 7); copy for the credit line, the suggestion prompt, the preview banner and the stop card.

Find freshness (A) and the seed plan are decided here, path well-worn; Truckee joining Tahoe is a one-row default the PM can reverse. Discover and the switch are after beta; the categorization engine is needed in beta for F113's profile, and the seed can run it on the Batch API.
