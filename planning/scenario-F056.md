---
id: F056
title: A producer edits a shop that already exists
status: approved
horizon: now
rank: 150
date: 2026-09-10
depends: [F061]
approved: 2026-09-07 — Gate A/B cleared; values statement cut per PM ruling
amended: 2026-10-01 — Don: Page creation lands on the draft Page, so address, neighbourhood and tags move here from F061 (criteria 6–8). 2026-10-04 — Don: criterion 7, a seeded neighbourhood or town list, shown as a pin at its centre. 2026-10-05 — Don: criterion 9, hours hidden; the phone stays.
---
## Story

Maya's shop has a name and one product, but nothing she can change once the walkthrough ends. From You, she taps Edit shop: one page, four fields — image, name, about, and a self-written "what we stand for" line the platform never sources or infers. She saves once; her public shop page updates immediately.

## Acceptance

1. An owner can edit shop image, name, about, and a free-text values line from one prefilled page.
2. Only an active owner can save; the write runs through a named handler with its event row.
3. The values-statement column has no source/provenance field — nothing but the owner's own edit can write it.
4. The shop has a ≤120-char tagline separate from the long description, rendering on card/profile/link-preview.
5. A shop with every optional field empty still renders correctly, with nothing nagging about the absence.
6. **On the draft or live Page,** an address search resolves to real coordinates with a confirming map pin before it saves; an unresolvable address refuses loudly rather than defaulting to a placeholder point. *(Moved from F061 criterion 1, 2026-10-01.)*
7. A "give a neighbourhood or town instead" option sits beside the address: a pick from a seeded list covering MSA 40900. A neighbourhood-mode Page exposes no street address anywhere and shows as a pin at the neighbourhood's centre (Don, 2026-10-04). *(Moved from F061 criterion 2.)*
8. The owner picks or creates **tags** in their own words, editable at any time; no category is offered and no free-text "Something else" field exists. A Page needs at least one tag to publish. *(Moved from F061 criterion 3.)*
9. **The owner can add an optional public business phone.** It is separate from the member's private phone and shows only if the owner gives it; it shows to signed-in visitors, not on the signed-out front door (Don, 2026-10-01).

## Not this

Weekly hours: currently hidden from the Page and from Edit, data kept, on the Later list (Don, 2026-10-05). A member profile: there is none (2026-10-01). A values vocabulary or picker — free text only. Any consumer reaction to the declaration.

## Rulings
- **2026-10-07 — A Page's contact details each carry an "everyone" or "members" setting: website, hours (when shown) and the area-level location default to everyone; phone and the new Contact email default to members only. The owner flips a single field with a small globe/lock icon beside it (the (i) explainer sits on the icon); each field exists once, with no big toggles and no second section. Signed-out visitors are "everyone", signed-in members are "members". Free text on a Page is not scanned for email addresses.** The PM, option B. Because phones and emails shown to signed-out visitors get scraped by spam bots, while a website helps everyone; one icon per field is the Airbnb/Google Business Profile pattern of private-by-default contact with no duplicate fields. Closes the open question on `socialus-web` #450. Rationale and A/B/C: `planning/research/contact-visibility-2026-10-07.md`. Path: well-worn. [replaces 2026-10-01: It shows to signed-in visitors, not on the signed-out front door.] [binds tiers=planning,code surfaces=pages,page-edit,contact]
- **2026-10-05 — Business hours are currently hidden from Pages and from Edit; the data is kept and the business phone stays. When hours are shown at all, they link out to the business's own site or Google Maps rather than being kept up here.** Don. They fail the value test on three counts: they live somewhere better, they go stale, and the owner has to keep them current. Hidden in `socialus-web` #344. [replaces 2026-10-05: Business hours are currently hidden from Pages and from Edit, because they cluttered the Page] [binds tiers=planning,code surfaces=pages,edit]
- **2026-10-04 — A Page owner can pick a neighbourhood or town from a seeded list covering MSA 40900 instead of giving a street address. Only the neighbourhood shows, as a pin at its centre.** Don. F056 criterion 7 restated; `product/systems/groups.md` follows. The pin is the centre of the place the owner chose, not a guessed point. [replaces planning/scenario-F062.md] [binds tiers=planning,code surfaces=pages,page-edit,map,places]
- **2026-10-01 — A Page may carry an optional public business phone, in launch scope. The business phone is separate from the member's private phone and shows only if the owner gives it.** Don. F056 criterion 9 added. **New launch scope.** Builds on F056 and F093. [binds tiers=planning,code surfaces=pages,page-edit,contact]
- **2026-09-13 — The composer's category step becomes the tag step.** Don's ruling, answering the open question from the same day. A creator picks from existing tags or creates a new one, and picks no category. **A Page with no tags is invisible to search**, which is the outcome the tags-only ruling exists to prevent.
  - **Creators create their own tags.** There is no vocabulary to seed and nothing to wait for: the first creator types *sourdough* and that tag exists. **The picker over existing tags is a progressive enhancement**, not a precondition — with no tags yet it is a text input, and it fills itself as creators use it. *(Corrected 2026-09-13: an earlier version of this entry named "no tags to pick from" as a blocker. It is not one.)*
  - **The one real gate is moderation.** Public tags are member-contributed content that other members see, so rule 1 bars them from production without report-and-takedown — which does not exist, and whose own blocker is a PM operating decision rather than engineering (`socialus-web` #13: *"Depends on: nothing in code"*).
  - **The farmers market dictionary is not a precondition either.** It is what a finder types, not what a creator must choose from. It makes search better; it does not gate the step.
- **2026-09-09 — A Page's address is public if given; a neighbourhood is the private-safe alternative.** The address field must say it's public before anyone types into it.
- **2026-09-07 — The producer values declaration is cut from launch.** The constraint survives: a values statement, whenever built, is self-declared only, never sourced or inferred. [always]
- **2026-09-07 — "Where they'll be next" ships as one free-text line (≤140 chars) on the shop editor, not structured recurring scheduling.** Structure is a priced v2 buy-back; every producer who fills the sentence re-enters it by hand later.
