---
id: what-location
purpose: Permanent / recurring-temporary / area places — why Location carries no purpose of its own, and the accountable-participation commitment it encodes.
layer: what
status: active
---

# Location

A Location is the platform's record of one physical place where things happen — a name, a geography, an optional description, a creator-of-record. It carries no purpose of its own; purpose comes from the Items attached and the Pages anchored to it. Three kinds, fixed at creation and never transitioning: **permanent** (a fixed point — a shop, a park, a bar), **recurring-temporary** (a point that hosts activity on a cadence — a market booth, a bar where a run club meets), **area** (a Member-drawn polygon — a service radius, a custom delivery zone).

## What a Location deliberately is not

**Not a Page.** A neighbourhood park is a Location; the Group that gathers there is a different record that may anchor to it. People affiliate with Pages; they relate to Locations only through Items they create, Pages they join, and searches they save.

**Not recognized civic geography.** A city or county is a Place (`places.md`), platform-curated and infrastructural. An "area" Location is Member-declared and personal — a service radius is not the same kind of thing as the city of Sacramento, and conflating them would let a Member's polygon carry authority it shouldn't have.

**Not a complaint surface.** This is where the accountable-participation commitment takes its structural form: when messaging ships, it's scoped to Items or Pages only — never to a Location. No Location wall, no Location feed, no Location DM. The platform's answer to "I have a problem with this place" is to create an Item that leads a fix (a Wonder, an Initiative), not to open a channel for complaint.

**Not a Person.** A Member's home-location pointer is a soft default, never a stored address. A Member's actual geographic life lives across three purpose-owned, mostly-private substrates (seller locality, community-awareness scope, saved searches) — none of them a column on the Member row.

**Not auto-discovered.** No Location is pre-populated from Google Places, OpenStreetMap, or any third-party source at launch — every row exists because a Member added it. Pre-populating would make the map look filled-in on day one at the cost of every row being a third party's fact, inheriting their errors and their update cadence. The deliberate-presence guarantee (no auto-assignment, no scraped identity) is the same one every other primitive on this platform carries.

## Locations are not transferred, only claimed

The original creator of a Location record can't hand off maintainership at launch — a future claim flow lets another Member become the maintainer of an inactive record. This is deliberately conservative: a transfer flow is exactly the surface an adversarial actor uses to take over an established, trusted record with a plausible cover story. The cost of "creator can't hand off yet" is small; the cost of "anyone can claim Drake's by submitting a form" is large enough to corrupt the trust the whole locality index depends on.

## Address handling stays deliberately unambitious

Street addresses are free Member-authored text — never run through a geocoder, validated, or auto-corrected at launch. This keeps the platform out of the address-canonicalization business and avoids standing up a new sensitive, normalized-address dataset with its own privacy footprint. Revisit only if duplicate Location rows measurably degrade discovery, not preemptively.

## What this rules in and out

**Rules in:** a Location existing because a Member declared it exists; a personal address route through an "unlisted" location a stranger never browses into, reached only via the Item that references it.

**Rules out:** a Location as an addressability surface of any kind. Coordinate drift without review — a small movement auto-applies, a large jump flags for re-confirmation, because a moved pin is either a legitimate fix or vandalism and the platform can't tell which from the delta alone. A `mobile` or `route` kind before a real case can't be modeled by the existing three — the enum stays narrow on purpose.

## Rulings
- **2026-10-06 — Location ("venue") pages are currently retired, and their address `/p/<place>/l/<slug>` is deleted. A post at an address with no Page shows the address and a map pin.** The PM, URL decision 3, option A. Because a place should have one home, its Page; separate place pages produced duplicates and unclaimed copies at Facebook before it merged them into Pages; Google Maps and Yelp treat the business as the place. Kept option: an auto-generated "everything at this address" list (Eventbrite and Instagram style) as a view, not an owned page. Consistent with "Venue is not a noun" (2026-09-12). Built before production, not beta: `socialus-web` #420. Rationale: `planning/research/url-plan-2026-10-06.md` §1, §7.3. [binds tiers=planning,code surfaces=location-url,pages]
- **2026-09-30 — "Local" means where a thing is, not who may see it. A Page's own settings decide whether it is open to the public.** Don, on F094: an open run club shows where it meets. F094 criterion 3 restated in his terms; it had been Cowork's reading. [binds tiers=planning,code surfaces=pages,venue,locality]
- **2026-09-30 — A residence's address is public if given, at launch. The protection is the existing option to give a neighbourhood instead of a street.** Don took recommendation A on `nouns.md`'s residence question. **Revisit** withholding a residence address from anyone not invited or responding once RSVPs (F063) and a residence flag exist. [binds tiers=planning,code surfaces=pages,location]
- **2026-09-21 — Where a Page is, is resolved at read time from its Location's geography, never stored on it. Deepest containing Place wins, and "deepest" means the kind rank that already exists.** Ruling for `socialus-web` #175, the root cause of Don's dead links: `locations.place_id` was added by T075 and its population deferred to a ticket that never landed, so **every member-created Page has no place path and therefore no reachable URL** — `browseHref` returns null when the path is missing, which is every card on the new Browse surface. **(a) populating on insert is refused** for the reason T143 already gave: it is a second source of truth that goes stale the day a boundary moves, and boundaries move. **(b) is the ruling** — one GiST lookup against `l.geography` on the browse path. [binds tiers=code surfaces=page-location]
  **The order, and it is not a new one.** `src/lib/feed/feed-place.ts` `bySlug()` already ranks **neighborhood > city > county** for exactly this kind of collision. **Deepest means that rank, extended through state and region — not a computed tree depth.** `places.kind` is an explicit ordered enum, so counting ancestors would be a second definition of the same idea, and the two would disagree the first time the tree gained a tier.
  **The tiebreak, which is the actual decision.** Two containing polygons of the **same kind**: **the smaller area wins** — most specific geometrically is the honest reading of deepest, and it needs no new column. **Same kind and same area: lowest id, and that is a data fault rather than a valid state.** It must be made visible rather than merely deterministic. **That condition is written as a refusal on purpose**, because the existing accepted risk on the two `places` rows sharing the slug *sacramento* names this exact failure: *"the heuristic makes it deterministic and therefore silent."* A silent tiebreak is how the wrong geography looks plausible for a month.
  **What happens when the deepest match is a county or coarser:** the URL degrades to the state path, because ADR-0022 makes the county tier transparent and `place_url_path` already filters it out. **Coarse but reachable — not a dead link**, which is the bar here.
- **2026-09-12 — Confirmed, no longer provisional: the creator sets pin precision and the platform never snaps, rounds or coarsens it.** The consequence is unchanged and now load-bearing — with no guard in the data, the copy is the only thing between a creator and pinning their home. The warning at the moment of placement and the confirm-back of the derived place are **required**.
- **2026-09-12 — A creator dropping a pin sets its precision; the platform never snaps, rounds or coarsens it.** *(Provisional — read from a transcription artifact, being confirmed.)* The consequence is not provisional: with no guard in the data, the copy is the only guard. A warning at the moment of placement and a confirm-back of the derived place are both **required**, not advisory.
- **2026-09-07 — One Page is one place; no map grouping across locations.** A two-location business is two Pages. Introduces "appearances" (a Page appearing at a Venue) as the one new vocabulary word needed.
