> **SETTLED — do not re-raise:** Wealth circulates here; it is never extracted. The many benefit, not a few — the only test any money decision must pass. Any mechanism that passes it is open; who is paid what, ownership and incorporation stay open. Detail: `product/foundation/monetization.md`.

# IMAGINE

Nothing here is a commitment, and scenarios may not cite this file. **An intake, not a library:** it holds only ideas with no noun, verb or surface yet. **Ideas live in the knowledge store as concepts** (F130, 2026-11-11): each keeps one id from first idea to what gets built, with its date, who it came from, the PM's words and every later change. Ask the lookup tool for a concept's id to read it.

**To add an idea:** write it under *Added under the house rules* as a `### Heading` with the date and who it came from. The next Knowledge import loads it as a concept with status idea, and it then leaves this file; its id joins the list below.

## House rules, so this doesn't become a graveyard

Every entry since 2026-09-12 carries: **a date and who it came from** (an ownerless idea is one nobody retires); **one line on what would make it real**, an observable fact, not "when we have time"; and **claim separated from analysis**, agent additions marked as analysis. **`Priority: higher`** means Don said it matters more, nothing more; its absence says nothing (2026-09-19). **Retiring is normal**: an entry leaves when it ships, its trigger fires, or it's called dead.

## Added under the house rules

### Posts by people without an organization (2026-11-26, the PM)

*The PM, 2026-11-26:* a post is a mechanism for Pages and, newly, for people who don't have an organization or entity, as a way to ask or offer something to the community. This will need to get built at some point.

**What would make it real:** a member with no Page can ask or offer something to their community from chat.

*Analysis, agent:* an announcement without a Page already exists in the ontology; this adds the person-facing ask and offer. Related: D-0435 (store), D-0430 (chat and generated interface).

### Location by use case (2026-11-26, the PM)

*The PM, 2026-11-26:* how precisely a place is shown needs a theme and a journey per use case: a storefront wants a precise location; a farmers market attendee may want a temporary one; someone who holds classes at various places wants something different; someone who offers things from home may not want it published and only available to certain people on certain occasions.

**What would make it real:** one use case's journey is designed and built, for example the market attendee's temporary location.

*Analysis, agent:* today the owner decides precision, an address or a neighbourhood, and a Page's position is worked out at read time; that is the base to build the journeys on.

### Where a business's money goes: levels, and a private honesty signal
*2026-11-16, from Don (PM). The mechanism is not designed and Don has chosen no option.*

**Claim (Don):** patrons should know their money ends up back in their community. Before money is collected, they need to know when profits go elsewhere; the rebate actually paid is the end solution, so it comes in levels. A Page owner chooses where they are local to, and Pages that declare nothing show behind those that declare local. Something simple, like a tax return, but not yet. Members may call out dishonesty without piling on: no cold proof required and report counts never published; instead an unpublished honesty rating kept by the algorithm, smell-tested by surveying a few members, until something more deterministic exists.

**What would make it real:** the first money flowing to a community fund, or the first local badge shipping.

**Analysis (agent):**
- Builds on D-0165, D-0288, F106 and `business-jurisdiction.md`; overlaps `planning/briefs/who-is-local-here-2026-11-23.md` (CO-0071, CO-0072): reconcile first. Report handling is D-0073 and D-0327.
- Owner tools (Don, 2026-11-26): how an owning entity (private equity, foreign owner) and the person behind a Page are shown is up to the Page owner. SocialUs needs to give owners tools to show who they are and that they are local, preferably by introducing themselves on their Page. A concept without a mechanism; overlaps CO-0071 Know your Page owner.
- Levels sketch: says (owner declares), confirmed (locals or a public record), proven (rebate paid).
- Risk before it affects ranking: a hidden score the owner cannot see or contest touches member trust and legal exposure.

### Hyper-local, photo-aligned search
*2026-11-13, from Don (PM). A long-term direction, not a build: the small version we build should step toward it.*

**Claim (Don):** search that matches what someone asks for to what places look and feel like: "a quiet patio, not on a busy street" surfaces venues through photos members posted, shown as proof. Locals say specifics ("cozy", "dog-friendly grassy area") instead of rating a whole place, and those specifics become what search matches. Later, results lean on members with similar taste, and a venue missing one thing people keep asking for learns what to offer. Every change touching search, photos or tags should say how it moves toward this, or at least not block it.

**What would make it real:** a search result that shows the member photo matching the words asked for.

**Analysis (agent):**
- Builds on D-0220, D-0127, D-0045, D-0166 and D-0294 (a tip steers toward or away; SocialUs is not primarily a review site).
- Small version first: one shared tag vocabulary across photos, tips, search and owner insight, with each search logging which tags it asked for and which results missed.
- Taste matching overlaps "Narrow it down: taste as specific as the member" (2026-11-24); settle which carries it. Moderation of tips is a tentative yes (Don, 2026-11-13); do not raise it until he asks.
- Image embeddings (pgvector on Supabase) are the later engine step. Owner insight stays free and informational until a ruling says otherwise.

### A category icon on an unclaimed Page, so a photo means an owner (2026-11-12, the PM)

**Claim (the PM):** *"I wouldn't mind giving many of these pages default icons instead of photos to allow users to know which pages have owners."* Then: *"I'm currently thinking that more is less. We have a picture search concept that should help us and we'll roll with that. … photos should indicate a person owns this page and posted photos. We don't need to change anything now but we will adjust at some point."*

**What would make it real:** the PM adjusts the unclaimed-Page photo rule (Pages, 2026-11-12 ruling), or the hyper-local photo search idea starts carrying the photos.

**Analysis (agent):** an unclaimed Page leads with its primary label's icon, its seeded photos sit in the gallery, and the owner's first photo replaces the icon on claim. Precedents: Yelp's "Unclaimed" mark, Google Maps' claim prompt. Icon table: socialus-design `research/icons-and-pins-2026-11-12.md`.

### Market rings: where a market ends, and who may sign up when it opens (2026-11-23, the PM)

*The PM, 2026-11-23:* "one concern is a market opening and which consumers can also sign up. That is the market three ring … let's approve E for the market opening that way for the next market opening we can use the same parameters"

*Analysis, agent:* approved as option E of the Sacramento market-edges brief; the method and its parameters (hub 50,000; one hour of free-flow drive time from the hub; a town nearer another hub goes there; small leftovers merge in; tie broken by commuting zone; the Tahoe subdivisions stay their own) are in `product/systems/rings.md`. Not the search rings. Belongs to the Sacramento launch campaign (CO-0070), F103, F076.

**What would make it real:** a second market opens on the same parameters, with no new rule.

### Search rings: how wide one person's search widens (2026-11-23, the PM)

*The PM, 2026-11-23:* "the other three ring is search for a user or a person and the three ring search is that's how wide we go when we're trying to find a certain number of results for whatever they're looking for"

*Analysis, agent:* per person, centred on their vantage (F105), widening hood, town, area, beyond, labelled, until enough results; 10 by default (Yelp, Google and Airbnb precedent). Not the market rings. Part of hyper-specific search (F136), F104. Rules: `product/systems/rings.md`; build: socialus-web #1425.

**What would make it real:** a search with few nearby results widens and names how far it went.

### Get specific: taste as specific as the member (2026-11-24, the PM)

*The PM, 2026-11-24:* "I like the "narrow it down" part especially. For my purposes I really like riding bicycles except I have very specific bike riding preferences. I enjoy steel frame single speed bikes and hard tail mountain bikes and cruising on the beach bikes … That is more specific than just bicycling. … This theme will inevitably be an ongoing thing so how should we capture this?"

*Analysis, agent:* a theme over the taste record (CO-0066, F113), narrowing (CO-0059, F092), item tags (#1318) and hyper-specific search (F136): facets on everything, narrowing in conversation, "More like this" that isn't kept unless confirmed, interests as a tree. Options: `planning/briefs/narrow-it-down-2026-11-24.md`; proposed story map JY-NARROW.

*The PM, 2026-11-25:* "the name is get specific." The button: taps the member never manages, kept and fading, summarized once there is enough (F113 § Rulings).

**What would make it real:** the PM picks the first slice and it is scoped as a scenario.

### Prove the promises that would hurt most if broken (2026-11-26, the PM)

*The PM, 2026-11-26:* "I've even recently heard how agents can use math proofs to check code to make it more bullet proof."

*Analysis, agent:* the costliest promises (one account per number, a banned number stays banned, never charged twice) checked against every sequence of events, not only the ones a test thought of: random-sequence tests first, a formal proof (TLA+, via pstack) where a model is worth the upkeep. Builds on the absolute that a check must be seen failing first. Review: planning/research/proving-promises-2026-11-26.md.

**What would make it real:** the PM picks a pilot after January 6.

## In the knowledge store

*Loaded 2026-11-11 by the Knowledge import; listed by concept id so the dashboard's lanes still show them. The words, dates and analysis are in the store. When an idea gets a noun, verb or surface, its scenario names the concept in `concept:` and the line here goes.*

- **CO-0003 Affinity-derived Group suggestions.** [lane: later]
- **CO-0004 Apple platform integration.** [lane: later]
- **CO-0005 Brand strategy & naming.** [lane: later]
- **CO-0006 Bulletin intelligence.** [lane: later]
- **CO-0007 Local stays.** [lane: later]
- **CO-0008 Locally Made badge.** [lane: later]
- **CO-0009 MEHKO home kitchens.** [lane: later]
- **CO-0010 The mighty oak.** [lane: later]
- **CO-0011 Missing pets.** [lane: later]
- **CO-0012 Project arc overview.** [lane: later]
- **CO-0013 Reciprocity & goodwill.** [lane: later]
- **CO-0014 Recruitment plan.** [lane: later]
- **CO-0015 Rising tide — civic pride.** [lane: later]
- **CO-0016 Social capital.** [lane: later]
- **CO-0017 A scored community-health rubric.** [lane: later]
- **CO-0018 The cooperative engine (5 sketches).** [lane: later]
- **CO-0019 Short video and photos on Pages.** [lane: considering]
- **CO-0020 Artist collaborations on Pages.** [lane: considering]
- **CO-0021 Follow an artist across venues.** [lane: considering]
- **CO-0022 Local scouts.** [lane: considering]
- **CO-0023 Ticketing, and what RSVPs have to do with Ticketmaster.** [lane: later]
- **CO-0024 Blog posts and emails that explain what's what.** [lane: later]
- **CO-0025 Discovery that knows what a person is optimizing for.** [lane: considering]
- **CO-0026 The occasion — a thing people organize around, with no row of its own.** [lane: later]
- **CO-0027 Places compete to keep spending local.** [lane: later]
- **CO-0028 Civic voice — a pulse of how a community feels about local issues.** [lane: later]
- **CO-0029 Badges vs values.** [lane: later]
- **CO-0030 Tone adapted by region, or per person.** [lane: later]
- **CO-0031 Community funds a seller designates.** [lane: later]
- **CO-0032 Evidence of deceit, submitted by members.** [lane: later]
- **CO-0033 Market shopper: a neighbour shops the market for you.** [lane: considering]
- **CO-0034 Market meal plans: a week of meals from what one market carries.** [lane: considering]
- **CO-0035 Two sides: Find and Discover.** [lane: later]
- **CO-0036 Two-way ratings between members and Pages.** [lane: later]
- **CO-0037 Member-facing names for Find and Discover.** [lane: later]
- **CO-0038 Holiday specials up front.** [lane: later]
- **CO-0039 Local is where the money returns.** [lane: later]
- **CO-0040 Inventory: import, then our own tool.** [lane: later]
- **CO-0041 Chat-first SocialUs.**
- **CO-0042 Vouching: a member posts about a place they love.** [lane: considering]
- **CO-0043 Asked for, not here yet.** [lane: considering]
- **CO-0064 One-off creations: a member with an idea partners with a local maker.**
- **CO-0065 The town before it opens.** [lane: considering]
- **CO-0068 Shop by your values.** [lane: considering]
- **CO-0069 The blue dot.** [lane: considering]
- **CO-0071 Know your Page owner.** [lane: considering]
- **CO-0072 Your patronage supports a neighbor.** [lane: considering]
