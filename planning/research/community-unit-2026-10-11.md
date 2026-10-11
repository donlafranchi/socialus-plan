# What replaces the metro, and how markets open (2026-10-11)

Research note behind F103. **Path: new territory.** Every item carries a status so no agent reads a plan as a fact: **Built** (in `socialus-web` main today), **Beta** (by 2026-11-06), **Next** (after beta, before production), **Later** (thinking only, no date, nothing built). [A] marks an assumption.

## 1. Local, in one paragraph
Local is a walk up a tree from the member's home, not a polygon drawn around a labour market. The finest unit is the **hood** (neighbourhood, where one exists), then the **town** (a Census Place: incorporated city or town, or a Census Designated Place; county remainders fill the gaps), then the **area** (a named set of counties, which is also the market that opens and closes). Discovery scopes to the area and orders hood → town → area → online, never by miles. The MSA/CSA becomes a code on the area row, for reports only. Sacramento's area is the same four counties as MSA 40900, so the switch costs members nothing. **Status: Next (F103)**; the tree, the gate and the waitlist are **Built**.

**The three rings are the member's own.** They are built from the place tree and centred on the member's home: hood, town, area. They are not consumer-based, metro-based or city-based. Who may sign up is decided by the area ring (is the member's county in an open market); what a member sees is the area ring ordered hood-first; where a Page is stays as fine as its owner gave it.

## 2. Markets
**Sacramento: staff-led.** The PM opens it. **Built:** `metro_polygons.is_open`, the waitlist counting makers and finders separately against per-market thresholds (50/250, tunable), "eligible is not open", opening is a person's act, the builders job seeding content. **Beta:** this is how Sacramento opens.

**Every market after: community-led.** The same gate. Makers and finders sign up before a market opens; finders are people who come to find things, not Page followers. A market opens when both counts clear their thresholds, the operator can afford it (members fund the platform first; seller fees are the step after beta, DECISIONS 2026-10-07), and a person flips it. **Next:** re-key the gate from MSA to the area's county set (F103); thresholds stay tunable and get re-set from what Sacramento shows.

**Pages ready on day one.** Two routes. (1) A maker in a closed market builds their Page now; it stays out of Explore until the market opens, then appears at once. **Next (F103 criterion 5).** (2) An agent drafts a Page from the maker's own website or public social profile, and the maker claims and approves it before anything shows. **Later; new territory** (consent, copyright, impersonation). The nearest built thing is the unclaimed-Page ruling of 2026-10-05 with its credited photo, Claim and Ask-us-to-remove.

Precedents: Nextdoor's founding-member gate (10 households, progress visible only to that neighbourhood); Craigslist opening sites in batches, never ranked; Kickstarter's all-or-nothing threshold; Shopify stores in password mode before launch.

## 3. What data decides, what a person decides
Every number here starts at today's value and is re-set from Sacramento's data, never ruled: ring sizes, the liveness floor (10, the existing aggregate floor), the open gate (50/250), badge reach. Humans decide three things: whether an area exists and which counties it holds, whether a fund's payee is real (Later), and copy.

**Rings sized by density and mobility — Later.** Cheapest input when due: 2020 Census Urban Area membership plus ACS density and car-free share per town, three bands (walkable core, car suburb, rural), a start ring and a ceiling per listing type, widen one ring at a time to the floor, every widened ring labelled. Free data only. **Boundary signals — Later:** state lines as labelled walls; curated areas; LEHD commute flows to *propose* areas; aggregate follow/RSVP pairs above the floor of 10 to propose splits and merges; member-reported "my area" via `member_location_affinities` (Built, unused for this). Humans ratify; the system proposes.

## 4. Money — Later, kept in the plan
Nothing about funds, designation or payouts exists; payments are cut from beta; the platform is never the bank (DECISIONS). The thinking to keep: a community may hold several funds; a seller would designate one; changes once a year like open enrollment; money leaves the chartered partner only to a verified legal payee the community already has (nonprofit, community foundation, fiscal sponsor); surplus with no payee accrues visibly as pending, which is the motivation to organise; communities form their own entities, SocialUs creates none; no top-down pools, choice replaces pooling. Legal treatment unknown; to `socialus-legal` when due. Precedents: Open Collective fiscal hosts and pending balances, payroll-giving designations, co-op patronage declarations. IMAGINE § Community funds.

## 5. Evidence of deceit — Later, designed ahead
Members need a way to submit evidence, not only a flag: a report reason "not what it claims" with a statement and an attachment, private to review, the accused answering first (F102's shape). Staff are alerted when evidence arrives or when a Page's declared home disagrees with its locations or licence jurisdiction (`member_business_jurisdictions`, Built). Never an automatic penalty. Precedents: eBay and Etsy report-a-shop with evidence, BBB complaints where the business answers first, Google Business "suggest an edit". IMAGINE § Evidence of deceit.

## 6. Beta: not foreclosing
Three data items, no behaviour change, inside the batched-migrations rule: the Sacramento area row with its four counties and El Dorado's polygon; a zip → county table; Pages record a home town defaulted from the anchor location, and the waitlist records a county `place_id` beside the metro. F103 options A/B/C say when the gate and feed switch; B (first week after beta) is recommended.

## 7. What goes, what stays, when the metro leaves (Next)
Goes: the CSA bounding box, `browse_feed(p_metro_id)`, `resolve_home_metro` as the home resolver, the MSA→slug bridge in `zip-metro.ts`, `MarketSelector`'s haversine, the MSA-keyed badge test. Stays: the `places` tree and its geographies, `locations.place_id`, the member's primary-home Place, `member_location_affinities`, the waitlist and its thresholds, the floor of 10, the hood → metro → wider → online order (now hood → town → area → online).
