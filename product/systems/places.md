---
id: what-places
purpose: Places primitive — recognized geographic scope for locality URLs. Why platform-curated, not user-declared.
layer: what
status: active
---

# Places

A place is a recognized geographic scope — region, state, county, city, neighborhood — that everything else anchors to: a Location sits inside a place, a Page carries a place anchor, an Item inherits one, URLs nest under the place tree. Places answer two structural questions: where does a URL belong, and what counts as "near me."

**Places are platform-curated, not user-created — deliberately.** A "city" is a unit of recognized civic geography; if Members could declare one, someone could declare their block a city and own the URL namespace forever. User-declared geographic scope has its own primitive (`locations.kind='area'`) for service areas and custom polygons that aren't infrastructural. Curation by the platform is what keeps the URL hierarchy and the locality index trustworthy rather than a land-grab or a popularity contest.

**Deliberately separate from Locations.** A Location is a specific point a Member declared (Drake's Bar, at its actual coordinates); a place is an infrastructural scope nobody declares (the neighborhood it's in). Conflating them either gives every Location curation authority it shouldn't have, or makes places user-declarable and destroys the URL namespace's stability.

**Parent-scoped slug uniqueness.** A place's slug is unique under its parent, not globally — two distinct Oak Parks (a Sacramento neighborhood, an Illinois city) are two rows with different parents and neither needs a name-mangling suffix. The hierarchy carries the disambiguation so the slug stays legible.

**Granularities can be skipped.** A small town's city row can parent directly to state; some neighborhoods have no universally-recognized boundary and never get their own row — their Locations anchor to the parent city. The hierarchy is variable-depth by design, not every place uses every level.

**Distinct from the business-jurisdiction ladder.** Places are a discovery/URL surface; jurisdiction (`business-jurisdiction.md`) is an evidence surface using ZIPs, not place rows. A business Group carries both a place anchor (for its URL) and a jurisdiction tier (for its badge) — never one standing in for the other.

## Proposed: three rings replace the metro

*Proposed 2026-10-11, from the PM's direction. Not accepted. Its status is F103's frontmatter (`planning/scenario-F103.md`, draft); this section says how it would work, not whether it ships. Until F103 is approved, the metro (MSA 40900 via the zip crosswalk, the CSA polygon for Explore) is what the code reads, and "local" means the whole metro (DECISIONS 2026-09-27).*

**The rings are the member's own, built from the place tree and centred on their home.** Three of them, coarse to fine:

| Ring | Unit | Rows | Who defines it | Used for |
|---|---|---|---|---|
| hood | neighbourhood, where one is recognised | `kind=neighborhood` | platform-curated, as today; turns on in a town once owners there pick neighbourhoods | the finest ordering band; never a scope on its own |
| town | a Census Place (incorporated city or town, or a Census Designated Place); the county remainder where there is none; a tribal area only if the member chose it | `kind=city` (a CDP is a city row) and county rows | Census TIGER, imported; nobody draws one | the **home community**: where a seller's give-back goes and the unit a fund belongs to |
| area | a named set of counties | `kind=region` with county children | the operator adds a county with one row | the **market**: who may sign up, what Explore scopes to, what opens and closes |

The MSA/CSA becomes a code on the area row, read by reports and nothing member-facing. The metro overlay (`metro_polygons`) retires once every reader has moved to the area row; what it did survives in the tree.

**Order, not distance.** Every surface that scopes by locality scopes to the member's area and orders hood → town → area → online. No miles are shown or filtered; the ring is the only nearness the product has. Widening past the area (a neighbouring area, the state) happens only in its own labelled section, never silently. Rings sized by density, drive time or behaviour are later and data-led; the model needs none of that to start.

**A market opens on sign-ups, by a person.** Makers and finders (people who come to find things; the waitlist calls them patrons) sign up before the market opens. It opens when both counts clear their per-market thresholds (F076: 50/250 to start, tunable), the operator can afford it, and a person flips it. Sacramento is staff-opened; every market after is community-led this way. A maker in a closed market can build a Page that is absent from Explore until the day the market opens.

**What "local" means to a seller.** The PM's definition, 2026-10-11: *local means money stays in the community.* So a seller's local is the **home community** their give-back goes to, which is their **town** by default (the Place their anchor Location sits in), and they may choose an adjacent town or an overlapping tribal area instead. Discovery is wider than money: a seller is *found* across their area and *local* to their town. When the Locally owned badge returns, its test becomes "the seller's home community is inside the viewer's area", replacing the MSA test in `business-jurisdiction.md`; the evidence ladder there is unchanged.

**Community, defined for money.** `contributions.md` says give-back is decided "per community" and defines the word nowhere. Proposed: **a community is a town ring.** A fund belongs to one community; a community may hold several funds; a seller designates one fund, changeable once a year (IMAGINE § Community funds, later). A community too small to hold a fund pools nothing top-down: its surplus accrues as pending until it organises, or its sellers designate a fund elsewhere (open question below). The money unit is chosen and auditable; discovery is fuzzy and viewer-relative. They must stay separate columns.

**Colloquial places.** Apple Hill is a growers' association of about fifty farms around Camino and Placerville, not a Census Place. Such a place is a `region` row *below* a county, platform-added like any place, so a Page can say it is at Apple Hill and a finder can browse it; it is never a home community, because money needs a unit the Census and a bank both recognise. The same shape serves "Tahoe-Truckee" or "Gold Country" above the county, with the open question on state lines in F103.

**Worked example: Apple Hill, from Sacramento.** A member living in Sacramento city has hood = their neighbourhood, town = Sacramento, area = Sacramento (Sacramento, Placer, El Dorado and Yolo counties). Camino is a CDP in El Dorado County, so an Apple Hill farm is inside their area ring: it appears in their Explore after hood and town content, labelled by its town ("Camino") or its colloquial place ("Apple Hill"), never "45 minutes" or "40 miles". The farm's own rings: town = Camino, area = Sacramento. Its give-back goes to Camino's fund, or, if Camino has none, accrues as pending or goes to a fund its owner designated under the rule below. A Bay Area member, outside the area, does not see the farm as local; they see it only in a labelled wider section once their own area is open, or by its link.

**Precedents.** Craigslist's hand-drawn regions give every address a home and use colloquial names; Nextdoor's neighbourhood is the finest ring and "Nearby Neighborhoods" the next, with a founding-member gate before a neighbourhood opens; the USDA local food directories key on city and county, not metro. Conflict: Craigslist's unit is the region, Nextdoor's the neighbourhood; here the area is the market and the hood the finest ring, so both fit.

[open-question owner=don raised=2026-10-11] What is a community, for money? A) **The town ring: a Census Place or county remainder, the seller's by default, adjacent allowed** (recommended: discrete, auditable, free data, matches how people name where they are from). B) The county: fewer, larger funds, but Davis and Woodland share one and neither feels it is theirs. C) Free text the seller types, matched to a fund later: flexible, unauditable, invites gaming.

[open-question owner=don raised=2026-10-11] May a seller designate a fund outside their home community? A) **Any fund inside their area, with the home community's funds first** (recommended: an Apple Hill grower in Camino can back a Placerville fund, and no money leaves the market). B) Home community only: simplest, but a town with no fund strands its sellers' give-back. C) Anywhere: breaks "local means money stays in the community".

[open-question owner=don raised=2026-10-11] "Community" is also the proposed merged Page kind (DECISIONS 2026-09-15, not ruled). Two meanings of one word in one product. A) **Keep "community" for the money unit and call the Page kind "group", which is what members already see** (recommended). B) Keep the Page kind and call the money unit "hometown". C) Live with both; copy disambiguates.
