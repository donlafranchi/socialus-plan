---
id: what-business-jurisdiction
purpose: Three-tier locally-owned verification without exposing addresses.
layer: what
status: active
---

# Business jurisdiction

A "locally owned and operated" claim needs to anchor to something more than self-report, without forcing an owner to expose a home address. The answer is a verification ladder — self-attested → community-attested → document-verified — whose tier is itself a public signal: a Group can be "Says locally owned" (Tier 0, the owner's own claim, 2026-09-30), "Community-confirmed" (Tier 1), or "Documented" (Tier 2). Members aren't punished for sitting at Tier 0; the badge is honest about the evidence level instead of pretending every claim is equally strong. A Group with no jurisdiction record from any owner simply doesn't surface the badge — the platform doesn't punish absence, it just doesn't claim what hasn't been claimed.

**Locality is separated from address by design.** The platform stores a ZIP (or ZIP-equivalent), never a street address, as locality evidence — the test is whether that ZIP's market is the Page's market (the market replaced the MSA, 2026-10-11, F103) — but a safety-conscious owner can declare an accountant's ZIP or a PO box instead of their kitchen. This is the same reasoning already ratified twice elsewhere in the project (the locality-vs-address separation on Pages, the findability-follows-publication rule) — one commitment, applied a third time.

**What Locally owned means (the PM, 2026-10-12).** It asks one question: *does the income generated here come back here?* It is a circulation question, not a legal-form question and not a distance. *The local badge is the receipt for a Page's declared give-back town (F106, ruled 2026-10-11); this ladder evidences the owner side of the same circulation, where the owner lives and operates.* **First version: the owner makes the claim**, in plain words, along the lines of "I live near here and I run this business here" (wording to be settled with copy; the Tier 0 label stays "Says locally owned"). No radius, no document and no check ship in the first version; the ladder above still holds for the later tiers.

[open-question owner=don raised=2026-10-12] How do we test "lives near and operates here" elegantly, with no arbitrary radius? Any fixed number leaves some people out: a 25-mile line shuts out the farmer 26 miles away and lets in the franchisee 24 miles away, and a rural owner and a downtown owner live at very different distances from "here". A) **Words, not a number** (recommended for the first version): the owner's claim names the town or market where they live and operate, and members see that name; nothing is computed. B) **Same market**: the owner's zip is in the Page's market, which is the test above and uses F103's rows, with no radius. C) **Same or touching town**: the owner's town is the Page's town or touches it, using the adjacency order the rings already use (`places.md`); a count of towns crossed, never a mile. D) **A radius**: only if the others fail, and then set per market by the operator, not one national number. Examples in the wild, none with a mileage: [Local First Arizona](https://localfirstaz.com/join) (Arizona-headquartered, owner lives in Arizona, privately held, independent of out-of-state chains, majority of the business in Arizona); [AMIBA](https://en.wikipedia.org/wiki/American_Independent_Business_Alliance) (at least half owned by area residents, final authority with the local owner, a limited number of locations and a limited geographic range, the limits left to each local affiliate to set). Both name a region and leave the line to people. **Come back to this before the badge design; it bites when badges return, not before.**

**OR-aggregation across all active owners, no founder privilege.** A business Group qualifies as locally owned if *any* active owner's jurisdiction record passes the market test — not all owners, not a designated "owner of record." A partnership with one local and two non-local owners is still locally-owned in the way that matters for a "should I support this" decision, and privileging the founder specifically would break the moment ownership transfers. The rule survives owner additions and removals automatically, because it's computed, not stored as a flag.

**Why Tier 1 is community-attestation, not a government-records lookup.** SOS-of-convenience filings (a Delaware LLC operating in Sacramento) are a known evasion path for record-based verification, and buyers who've actually transacted with a seller have ground-truth a public filing doesn't carry. This is peer pressure for the greater good, the same enforcement model the rest of the platform runs on — not an external integration. The tradeoff, accepted: Tier 1 needs the interaction graph to reach real density first, so it's a b2+ concern; Tier 0 self-attestation is the honest floor at launch.

**Document upload (Tier 2)** is the widest tier for sole props with no LLC — an EIN letter or business license, ZIP extracted, document never shown publicly, only the extracted ZIP and the tier label render.

**Entity type, legal entity name and state are asked at business registration only, and only of members who have a legal entity** (Don, 2026-09-30). Page creation and member-to-member surfaces carry no legal words.

## What this rules out

A parallel locality-derivation path that bypasses both signals — any future third signal (a federation peer's own verification, say) extends the ladder, it doesn't create a side channel around it. Auto-derivation from a Member's home location or affinities — the Member must explicitly declare a jurisdiction; the platform never infers one. Showing the underlying document publicly, ever — only the tier label and the ZIP.

## Companion badge

"Locally Made" is the sibling claim, on `items.made_at_place_id` — jurisdiction answers "does the money go to a local owner," provenance answers "was this made here." Same evidence-ladder shape, different signal, designed together so neither has to be retrofitted against the other.
