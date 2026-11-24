> **SETTLED — do not re-raise:** Wealth circulates here; it is never extracted. The many benefit, not a few — the only test any money decision must pass. Any mechanism that passes it is open; who is paid what, ownership and incorporation stay open. Detail: `product/foundation/monetization.md`.

# IMAGINE

Nothing here is a commitment, and scenarios may not cite this file. **An intake, not a library:** it holds only ideas with no noun, verb or surface yet. **Ideas live in the knowledge store as concepts** (F130, 2026-11-11): each keeps one id from first idea to what gets built, with its date, who it came from, the PM's words and every later change. Ask the lookup tool for a concept's id to read it.

**To add an idea:** write it under *Added under the house rules* as a `### Heading` with the date and who it came from. The next Knowledge import loads it as a concept with status idea, and it then leaves this file; its id joins the list below.

## House rules, so this doesn't become a graveyard

Every entry since 2026-09-12 carries: **a date and who it came from** (an ownerless idea is one nobody retires); **one line on what would make it real**, an observable fact, not "when we have time"; and **claim separated from analysis**, agent additions marked as analysis. **`Priority: higher`** means Don said it matters more, nothing more; its absence says nothing (2026-09-19). **Retiring is normal**: an entry leaves when it ships, its trigger fires, or it's called dead.

## Added under the house rules

### Where a business's money goes: levels, and a private honesty signal
*2026-11-16, from Don (PM). A concept with the mechanism not yet designed; Don has not chosen an option and is not ready to.*

**Claim (Don, 2026-11-13 to 16):** the point is that patrons know their money ends up back in their community. Before any money is collected, users need some way to know when a business's profits go elsewhere, and the rebate (the give-back actually paid to the community) is the end solution, so this comes in levels. A Page owner chooses where they are local to, with some way for that to matter, and Pages that declare nothing show behind Pages that declare local. He wants something simple, like a tax return, but is not ready to ask for that yet and it may not matter until we collect money. Community members should feel empowered to call out dishonesty without piling on: no cold hard proof required, and the number of reports is never published. Instead keep an unpublished honesty rating handled by the algorithm on the back end, surveying a few members to smell-test a claim, until something more deterministic exists.

**What would make it real:** the first money flowing to a community fund, or the first local badge shipping.

**Analysis (agent):**
- Builds on D-0165 (local means money returns; the owner chooses where it goes), D-0288 (10-16: the badge comes from the owner's claim alone, which this re-thinks), F106 (the give-back badge, approved for later), and `business-jurisdiction.md` (mostly old; its ownership ladder is likely retired once this is designed). Report handling is D-0073 and D-0327.
- Levels as a sketch, not a decision: says (owner declares), confirmed (locals or a public record back it), proven (the rebate was actually paid).
- Risk to settle before it affects ranking: a hidden score about a business, which the owner can't see or contest, touches member trust and possible legal exposure, so owner visibility, appeal and counsel come first.
- Not decided: what "matters" for a declaring Page beyond ranking, how the survey works, and what the signal is allowed to change.

### Hyper-local, photo-aligned search
*2026-11-13, from Don (PM). Long-term direction, not a build: the small version we build should be a step toward it.*

**Claim (Don, 2026-11-13):** search that matches what a person asks for to what places actually look and feel like. Someone asks for "a nice place for a drink on a patio, not on a busy street, not noisy", and photos of that kind of setting, from anyone who posted one, surface that venue as the proof. Locals say specifics ("welcoming for an afternoon picnic", "cozy and relaxing", "dog-friendly grassy area") instead of rating a whole place, and those specifics become what search matches. Because members value different things, later a member's results lean on people with similar taste, and a venue that matches everything but one thing people keep asking for (dog-friendly) learns what to offer. Photos belong inside this hyper-local, hyper-specific search, so every change touching search, photos or tags should say how it moves toward this or at least does not block it.

**What would make it real:** a first search where a result shows the member photo that matches the words asked for.

**Analysis (agent):**
- Builds on D-0220 (what locals search for, aggregated and anonymous, shown back to owners), D-0127 (plain-words search built to grow into natural-language), D-0045 (LLM tag proposals; dictionary grows from creator tags and zero-result searches), D-0166 (area-type search) and D-0294 (locals tips, steering toward and away; reworded 2026-11-13 to say a tip is in effect a review but SocialUs is not primarily a review site).
- Small version first: one shared tag vocabulary across photos, locals tips, search and the owner view, with each search recording which tags it asked for and which results missed.
- The taste-matched layer overlaps the entry "Narrow it down: taste as specific as the member" (2026-11-24); settle which one carries it when either is built.
- Taste matching needs enough members and uses member data: infer from what people loved and where they go rather than asking for a profile, and settle visibility and reset before building.
- Moderation of tips that steer toward or away: a tentative yes (Don, 2026-11-13). Do not raise it again until Don asks how to handle moderation.
- Image embeddings (pgvector on Supabase) are the later engine step; tags, text and distance come first.
- Owner insight stays free and informational until a ruling says otherwise, because paying to close a gap touches transaction income and member trust.

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

### Narrow it down: taste as specific as the member (2026-11-24, the PM)

*The PM, 2026-11-24:* "I like the "narrow it down" part especially. For my purposes I really like riding bicycles except I have very specific bike riding preferences. I enjoy steel frame single speed bikes and hard tail mountain bikes and cruising on the beach bikes … That is more specific than just bicycling. … This theme will inevitably be an ongoing thing so how should we capture this?"

*Analysis, agent:* a theme over the taste record (CO-0066, F113), narrowing (CO-0059, F092), item tags (#1318) and hyper-specific search (F136): facets on everything, narrowing in conversation, "More like this" that isn't kept unless confirmed, interests as a tree. Options: `planning/briefs/narrow-it-down-2026-11-24.md`; proposed story map JY-NARROW.

**What would make it real:** the PM picks the button option and the first slice is scoped as a scenario.

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
