# Explore freshness, learning about a member, a test profile and a regional seed (2026-10-12)

Asked for by the PM: show new and interesting things on every revisit, learn about a member from what they search for, build a test profile for the PM, and add businesses from Napa Valley to Truckee, South Lake Tahoe, Lodi, Yuba and Colusa. Draft scenarios: F112 (freshness), F113 (what we learn), F114 (test profile), F115 (regional seed).

**How sources are marked.** **[V]**: the page was read this session. **[S]**: only a search snippet or a secondary write-up was seen. **[A]**: assumed, verify before building. **[C]**: read in `socialus-web` main at `0e5ee14`.

## The rules this has to fit

The repo has no literal `[always]` / `[for now]` tags. The convention (Charter ruling 2026-10-11, `product/foundation/model.md`) is that **"currently" marks a ruling that is not permanent**, and a line without it stands until a ruling replaces it.

| Rule | Where | Tense |
|---|---|---|
| Order by where it is and how recent it is, not by what holds attention or what was paid for | Charter, flip 1 | **currently**: a ruling can change it |
| Ranking is a place, time and relationship engine; Browse is complete, not ranked by your interests | Charter, flip 1; F059 2026-09-12 | standing |
| "Personalized" (Home) means declared interests and where they are; behaviour is not read back at the member | F059 ruling 2026-09-12 | standing |
| Home ranking uses time, place, declared interests and curation, not time spent; one wildcard row outside declared interests | ruling 2026-10-04 | **currently** |
| Lenses vary what is shown: "variety without compulsion", not addicting and not boring | F059 criterion 3, 2026-09-17 | standing |
| Collect data to benefit members, not shareholders; easy opt-out | Charter, flip 2; 2026-10-11 | standing |
| Log which Page a member opens from Explore, with member id, staff-side, opt-out | F109 ruling 2026-10-12 | standing |
| Member to member strict; staff have access; no tools that target one member | ruling 2026-10-09 | standing |
| Sharing is opt-in; a member is private by default | PRINCIPLES 2026-10-12 | standing |
| No distance, radius or "near you" anywhere | 2026-09-30, F104 | standing |
| A Page in a waiting market appears on no Explore, Home or search surface until it opens | F104 criterion 4 | standing |
| Members self-correct before staff work | 2026-10-11 | **until the operator has help** |
| Unclaimed Pages: the business's own photo, credited, from its own site or socials; "Unclaimed" tag; claim and remove | ruling 2026-10-05 | standing |

**Already built [C].** PR #558 shuffles Explore once per session: four recency bands (2, 7 and 30 days, then older), and inside a band an order from a hash of a session cookie (`su_seed`) and the row id (`src/lib/browse/session-shuffle.ts`). Lenses are `recent | soonest | newest` plus tags and time rows. No "seen" tracking, no search log, no opt-out flag and no F109 open log exist yet. `member_interests` and `member_follows` read self-only since 2026-09-30. `item_responses` (RSVP, save) exists but only the persona seed writes to it. Home is paused and redirects to Explore.

## 1. Freshness without engagement ranking

### Precedents
- **Front Porch Forum**: "no algorithm; everyone using the service sees the same content in their geographic area"; human moderators review every post; a slow pace, no endless scroll [V] ([Wikipedia](https://en.wikipedia.org/wiki/Front_Porch_Forum)). Fresh because of a daily cadence and place, not because of ranking. One issue a day: [S].
- **Nextdoor**: machine learning ranks posts "most likely to matter to you" and re-engages lapsed members [V] ([Nextdoor blog](https://blog.nextdoor.com/whats-new-on-nextdoor-product-updates-1)). The model the Charter refuses.
- **Are.na**: "No ads, no personalized recommendations"; what you see comes from what you chose to follow [V] ([are.na](https://www.are.na/home)).
- **Instagram Following and Meta under the DSA**: chronological feeds of what you follow; in the EU, Search "based only on the words they enter" [V] ([Instagram](https://about.instagram.com/blog/announcements/favorites-and-following), [Meta](https://about.fb.com/news/2023/08/new-features-and-additional-transparency-measures-as-the-digital-services-act-comes-into-effect/)).
- **Bluesky custom feeds**: the member picks the feed, the platform supplies sensible defaults [V] ([Bluesky](https://bsky.social/about/blog/7-27-2023-custom-feeds)). The nearest thing to our lenses.
- **Mastodon trends**: moderator-reviewed, but counted from popularity [V] ([Mastodon 3.5](https://blog.joinmastodon.org/2022/03/mastodon-3.5/)). Popularity is attention, so it is out.
- **Spotify Discover Weekly**: new every Monday [V] ([Spotify](https://newsroom.spotify.com/tag/discover-weekly-mondays/)). The cadence transfers; the personalisation does not.
- **Airbnb**: making neighbouring results less alike helped in A/B tests [V] ([arXiv 2210.07774](https://arxiv.org/abs/2210.07774)).

### Research
- **Fair exposure over many rankings** (Biega, Gummadi and Weikum, SIGIR 2018): no one list can be fair, so make each item's visibility, summed over many lists, proportional to its relevance [V] ([arXiv 1805.01788](https://arxiv.org/abs/1805.01788)); Singh and Joachims, KDD 2018, the same idea per list [V] ([arXiv 1802.07281](https://arxiv.org/abs/1802.07281)). **This is the one that fits a local platform: every business gets its turn.**
- **Novelty and diversity** (Kaminskas and Bridge, ACM TiiS 2016): diversity goes with novelty, and novelty raises coverage [V] ([UCC](https://research.ucc.ie/en/publications/diversity-serendipity-novelty-and-coverage-a-survey-and-empirical/)). MMR re-ranking cuts redundancy [V] ([Carbonell and Goldstein 1998](https://people.eng.unimelb.edu.au/ammoffat/sigir98/abstracts/carbonell.html)); topic diversification raised satisfaction while lowering accuracy [S] (Ziegler et al., WWW 2005).
- **Impression discounting** (Lee et al., LinkedIn, KDD 2014): showing an item again and again lowers its response [V, slides] ([slides](https://slideshare.net/mitultiwari/impression-kdd)). The basis for "not seen yet first", and it needs a per-member record of what was shown.
- **Bandits and Thompson sampling** (Li et al. 2010 [V], [arXiv 1003.0146](https://arxiv.org/abs/1003.0146)): learn from clicks, which is attention optimisation by definition. Out.
- **DSA Article 27** (explain the main ranking parameters) and **Article 38** (very large platforms offer one option not based on profiling) [V, mirror] ([27](https://www.eu-digital-services-act.com/Digital_Services_Act_Article_27.html), [38](https://www.eu-digital-services-act.com/Digital_Services_Act_Article_38.html)). We are not bound; a place-and-time Browse is Article 38's option by construction.

### Options

- **A) Fair turns, no repeats, and "new since you were here" (recommended).** Inside each ring band and recency band, the Pages shown least in the market over the past 7 days come first, the session seed breaking ties, so the same business cannot lead every visit and every business gets a turn. The count is per Page per day with no member id (like `map_mix_log`). No two cards in a row from one Page, and a Page leads at most one lens row on the first screen. The lens row that leads rotates by the day. A divider, "New since you were here", uses a last-visit time kept in the member's own browser, so the server stores nothing about the visit. **No Charter change**: it replaces the random tie-break #558 already uses inside a place-and-time band; place and time still decide the order, and nothing reads attention. **Path: well-worn** (Biega 2018, Front Porch Forum's cadence, Airbnb's diversity).
- **B) A, plus "not seen yet" first, per member.** The server records which cards each member was shown and puts unseen ones first. Fresher, but it reads behaviour back at the member, against the 2026-09-12 ruling, and it adds an ordering input the "currently" Charter line does not list. **Needs a ruling and a Charter line change**: "We currently order what you see by where it is, how recent it is and whether you have seen it." Staff could read every card a member was shown.
- **C) Learn what each member opens and show more of it** (bandits). **Needs a Charter change** to flip 1 ("not by what holds your attention") and the 2026-09-12 Browse ruling. Not recommended: it is the Nextdoor model.

**Decision taken here: A**, path well-worn, as F112. B is held as F112's *Not this* until the PM asks for it.

## 2. Learning about a member

### Precedents
- **Pinterest, "Refine your recommendations"**: tabs for activity, boards, interests and following; any can be turned off; ads are separate [V] ([Pinterest](https://help.pinterest.com/en/article/tune-your-home-feed)).
- **Spotify, "Exclude from your taste profile"**: listens still recorded but count less, within about 48 hours [V] ([Spotify](https://support.spotify.com/article/exclude-playlists-or-tracks-from-your-taste-profile/)).
- **YouTube**: delete one history item, pause watch and search history, "Don't recommend channel" [V] ([YouTube Help](https://support.google.com/youtube/answer/6342839?hl=en)); with history off, Home goes blank, criticised as a dark pattern [S].
- **TikTok, "Refresh your For You feed"**: starts recommendations over as if new, Following untouched [V] ([TikTok](https://newsroom.tiktok.com/more-ways-to-discover-new-content-and-creators-you-love)). **Instagram, "Reset suggested content"** (2024–25) [S].
- **Google My Ad Center**: inferred topics shown, editable, one switch off [S]. **Auto-delete** of search history at 3, 18 or 36 months, 18 the default for new accounts since 2020 [S] ([9to5Google](https://9to5google.com/2020/06/24/google-auto-delete-history/)).
- **Goodreads, Threads**: interests the member declares, suggestions pre-filled [S].
- **Research**: implicit signals (opens, views) measure confidence, not preference (Hu, Koren and Volinsky, ICDM 2008) [S]; scrutable user models, a member can see and change what the system believes (Kay, CHIIR 2021) [S]; "Why am I seeing this?" without controls did not build trust, and its explanations were often incomplete (Andreou et al., NDSS 2018) [S].
- **Law (not advice; for `socialus-legal`)**: California's final ADMT rules (approved 2025-07-24) cover only "significant decisions" (money, housing, school, work, health); a Home feed of events is outside them on our reading [V] ([Morgan Lewis](https://www.morganlewis.com/pubs/2025/08/cppa-board-finalizes-new-rules-on-admt-cybersecurity-audits-and-risk-assessments)). CCPA rights to know, delete and correct apply only above its thresholds [A], and are cheap to meet anyway.

### What we would learn, and what it may change

| Signal | Strength | Kept | May change |
|---|---|---|---|
| A declared interest | strong, the member said so | until removed | Home rows and their order |
| A follow | strong | until unfollowed | Home's following row (built) |
| "I'm coming" / RSVP | strong | 90 days after the date [A] | suggestions only |
| A search | weak | 90 days [A] | the member's own recent searches; suggestions; staff "searched, found nothing" counts |
| A Page open from Explore (F109) | weak | 90 days [A] | suggestions; the N per category (staff, aggregate) |

**Nothing in any option changes Browse's order, search relevance, what another member sees, or anything a Page owner sees about a member.**

### Options

- **A) Declared, with suggestions the member accepts (recommended).** Signals only *suggest*: "You've been to three trivia nights. Add trivia to your interests?" with Add or No thanks. Home ranks on what the member declared and follows, as the 2026-10-04 ruling already says. **"What SocialUs knows about you"** in You lists every interest, follow, RSVP and recent search, each deletable, and one switch, **Learn from what I do**, on by default as the data ruling and F109 have it, which stops suggestions and the F109 log and deletes the raw signals. Raw signals expire on their own after 90 days, so nothing needs an operator. **Fits every rule as written.** Backed by Goodreads, Threads, Kay, Hu et al.
- **B) Inferred interests, visible and editable.** Home ranks on interests the platform infers, each listed with its reason ("from 4 RSVPs"), removable, with a reset and the same switch. Best relevance and well-worn (Pinterest, Spotify, Google), but it **needs a ruling change**: the 2026-09-12 and 2026-10-04 rulings say *declared* interests. No Charter change. Risk: the Facebook critique, and staff can read inferences.
- **C) Follows only.** No learning; recent searches stay in the browser. No change to any rule, nothing to explain; Home and Explore feel alike and the test profile has little to test.

**For the PM: A, B or C** (member trust, so new territory). F113 is written to A and its criteria wait for the call.

## 3. The PM's test profile

**What exists [C].** Builder accounts (`builders` table, `scripts/builders.ts` through a GitHub workflow): a builder's follows, joins and RSVPs to real Pages do not count, and `delete_builder_content()` removes everything a builder made. The persona seed (`scripts/seed-personas.ts`) refuses any host that is not local. The operator account is a break-glass holding every permission (`OPERATOR_MEMBER_ID`). There is one remote Supabase project; previews use it.

### Options
- **A) A builder account in production, seeded by a script (recommended).** A second account, signed in with a PM test address, home zip in the Sacramento market, flagged builder so none of its activity counts and it can be wiped in one call. A script (`scripts/test-profile.ts`, dry run unless `--apply`) writes six weeks of history against real seeded Pages. The PM uses it on a phone, on the real data, without touching the operator account. Builder signals must be left out of staff counts and the F109 report.
- **B) The PM's own production account.** Least setup; mixes test history into the operator break-glass and into staff metrics, and wiping it wipes real history.
- **C) A local persona only.** Safest; the PM cannot use it on a phone or against the regional seed.

**For the PM: A, B or C.** The spec is F114.

## 4. Regional seed (build plan; no data loaded)

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
1. **What we learn about a member (A/B/C, section 2).** It decides what F113, the F109 log and the test profile's history hold.
2. **Where the test profile lives (A/B/C, section 3).**
3. Copy for the credit line, the suggestion prompt and the preview banner, with the builds.

Freshness (A) and the seed plan are decided here, path well-worn; Truckee joining Tahoe is a one-row default the PM can reverse.
