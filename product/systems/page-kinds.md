---
id: why-page-kinds
purpose: The three things a person can start, what each needs at minimum, and where "kind" actually lives.
layer: why
status: needs-correction
date: 2026-09-15
---

# What a person can start

> **Restored 2026-09-15 after deletion the same day. Status: pending, not superseded.** This document was deleted on the reading that `model.md` retired Items. **That reading is disputed by Don and is not settled** — see `planning/ITEMS-QUESTION.md`. Nothing about the Item kinds was ever changed in code: all seven kinds and all four sub-tables are intact on `origin/main`.
>
> **One criticism of this document stands on its own and is unrelated to the dispute:** its kind-vocabulary table duplicates `item.md` § The kind vocabulary, and its schema section recommends a pattern the schema already uses. Those parts should be cut whichever way the Items question goes.

**Draft, not approved.** Written for Don's ruling of 2026-09-15: two durable kinds — someone selling, and someone with a recurring gathering — plus a deliberately thinner one-time gathering. Cross-references `../../planning/scenario-F087.md`, the one-create-flow scenario.

## First, the vocabulary — it does not mean what the ask assumed

**Don said "item kind." The three choices he described are Page purposes, not Item kinds.** The distinction is already ratified and both nouns already exist:

- **`nouns.md`: "A Page is the person or people behind the listing. Page is *who*; Item is *what*."**
- `groups.kind` exists: `place · interest · practice · event_anchored · family · business`, with typed child tables `group_businesses` and `group_event_anchored`.
- `items.kind` exists: `product · service · gathering · wonder · offer · ask · initiative`, with typed children `item_products`, `item_services`, `item_gatherings`, `item_wonders`.

**So "opening a shop" and "a group for meetups" are Page purposes. "Offering a service" is not** — a service is an Item filed under a Page. Don's own grouping already resolves this: his first durable kind is *"a person selling an item or service"*, one purpose covering both. **Nothing new is needed; the existing split carries it.**

**One correction to the brief: `code_kind` is unrelated.** It is a column on `metro_polygons` recording which census code a metro uses (CSA or CBSA). It has nothing to do with Pages, Items, or purposes.

**What the current model cannot carry without a ruling:** a one-time gathering as a Page. See § The thin one and § What this contradicts.

---

## The three

### 1 · Someone selling — a shop

**In plain words.** A person who makes or does something and wants to be found for it: a baker, a repairer, a teacher, a landscaper.

**What they are doing.** Creating a durable place of their own, then listing things under it over time.

**Minimum it needs.** A name · a location, either a real address or a neighbourhood · at least one tag in their own words · a description · a photo or generated art · the product and service composers · the ability to edit any of it.

**What it does not need.** A schedule or recurrence. Response collection — *`nouns.md`: no date on a product.* A business claim: that is a separate, deliberate act and remains the friction gate, not part of creation.

**Why it differs.** It is the only purpose whose Items are things rather than occasions, and the only one where a business claim later becomes meaningful.

### 2 · Someone with a recurring gathering — a group

**In plain words.** People who meet regularly. **Deliberately unconstrained as to why** — a run club, a repair café, a reading group, a congregation, a ward meeting. The platform does not ask what kind of gathering it is.

**What they are doing.** Creating a durable place for a thing that happens again.

**Minimum it needs.** Everything the shop needs, minus the product and service composers, plus: a gathering composer that can repeat · a next-occurrence date · response collection, so a host knows who is coming · followers, so there is somewhere to tell about the next one.

**What it does not need.** Product or service listing — permitted, since *a Page may sell, host, or both*, but not required to exist. A business claim. Jurisdiction or locality evidence.

**Why it differs.** It is the only purpose whose whole value is repetition. Everything it needs beyond a shop — recurrence, responses, followers — exists to serve a second occurrence.

### 3 · A one-time gathering — the thin one

**In plain words.** One thing happening once. A yard sale, a protest, a potluck, a work party.

**What they are doing.** Announcing an occasion, not founding anything.

**Deliberately general.** It carries no assumption about purpose and asks nothing about why people are meeting.

**Minimum it needs.** A title · one place · one date and time · a description · response collection, so the host knows who is coming.

**What it does not need.** Everything in the list below.

---

## What the thin one lacks — written down, not discovered later

**Compared with a recurring gathering, a one-time gathering has none of these. This is the whole list.**

1. **No durable identity.** No public URL of its own that survives the event, no profile, nothing to link to afterwards.
2. **No followers.** Nobody can subscribe, so there is no way to tell anyone about a next time.
3. **No recurrence.** There is no second occurrence, and no path from one to a series without starting something new.
4. **No photo.** Photos belong to Pages under the 2026-09-07 model change. A one-time gathering that is not a Page carries no face.
5. **No tags.** Tags are a Page's own vocabulary, so a one-off is not findable by the words its host would choose for it.
6. **Not indexed as an organization.** It never appears in Browse's Pages list. **This is the point, not a defect** — it is why the no-Page-for-a-single-occasion rule exists.
7. **It disappears once past.** *Anything in the past doesn't appear* — time-based and automatic.
8. **No business claim, jurisdiction, or locality badge.**
9. **No editing lifecycle** beyond an Item's own `state` — no archive, no dormancy, no retirement.

**Whether this is acceptable is Don's call.** Items 1, 2 and 4 are the ones a host is most likely to notice and mind.

---

## Schema — the recommendation

**Use the pattern the codebase already uses twice: one table, a `kind` column, and a typed child table where a kind genuinely needs extra fields.** `groups` does this with six kinds; `items` does it with seven.

| Option | Cost | What it forecloses |
|---|---|---|
| **A · `groups.kind` + typed children** *(recommended)* | **Near zero — it already exists.** `event_anchored` and its child `group_event_anchored` are already there for the recurring case; `business` and `group_businesses` for the shop. | Nothing. It is the pattern every read path already understands. |
| **B · A table per kind** | High. Every read, every RLS policy and every resolver forks three ways. | **A Page that both sells and hosts** — already ratified as permitted. This alone rules B out. |
| **C · A new `page_purposes` join or lookup** | Moderate, and buys nothing: `kind` already exists and already constrains. | Nothing, but it adds a layer with no question behind it. |

**Recommend A, with one constraint carried from `nouns.md`: the kind selects copy and tools at creation and must gate nothing afterwards.** A Page's entry says *"No permanent kind that gates anything."* The purpose is what the person was told they were doing, not a permission.

**The one-time gathering is an Item, not a row in this table** — `items.kind = 'gathering'` with `item_gatherings` carrying the date. **No migration is proposed here.**

---

## What this contradicts, for Don to rule on

1. **The one-time gathering versus F087 criterion 1.** F087 says *every path through the create flow produces a Page*. This document says the thin one is an Item. **`nouns.md`: "No Page for a single occasion"**, and the 2026-09-07 ruling gives the reason — browse and the map would index listings as if they were people, and a follower graph on something ephemeral is worthless. **Either F087 criterion 1 narrows, or the rule reverses.**
2. **If a container Page is created silently** to hold a one-off, it collides with **F069 criterion 3**: *"A Member holding several Pages sees every one on any producer surface — none silently chosen for them."* A silent container is a Page the person never knew they made. Either it is hidden from producer surfaces too, narrowing an approved criterion, or the person is told, which breaks the point of it being silent.
3. **`items.category` is still a live column** while categories are retired and *tags are the only vocabulary* (2026-09-13). Nothing in this document uses it; it is named so nobody revives it.
4. **`groups.kind = 'business'` already gates** — it carries a 1:1 child and the business claim attaches to it. That sits in tension with *"no permanent kind that gates anything"*, and predates this document.

## Rulings
- **2026-09-15 — Don confirmed two mappings: a class is a gathering, tutoring is a service.** Both fall out of the model as written; recorded because they were the test cases.
- **2026-09-15 — The one-pager is `planning/PAGE-KINDS.md`** (renamed from `THREE-KINDS.md`, which replaced the same-day two-kind draft). **Gap restated: `item_services.rate_model` is `hourly · flat · quote · membership` and nothing there means free**, which is half of what Don said a service is.
- **2026-09-15 — Proposed, not ruled: three Page kinds — `selling`, `service`, `gathering`.** Don: *"People are either selling something"* · *"Offering a service for money or for free"* · *"gathering one or many times."* **Once-or-many is a property of a gathering Page, not a fourth kind.** Replaces the six `groups.kind` values and supersedes the same-day two-kind draft. Mapping: `business` → selling; `place`, `interest`, `practice`, `event_anchored` → gathering; `family` → gathering set to private. **Written short in `planning/THREE-KINDS.md`.** Overturns: *"A Page may sell, host, or both"* · the six-kind list · the affiliate-versus-operate split · *"a Group never changes kind"*, now the main path rather than an edge. **And `item_services.rate_model` has no value meaning free.** [for now]
- **2026-09-15 — The collapse deletes four open questions and shrinks two.** Gone: the community merge, `event` as a kind, the farmers-market gap (a market convenes, so it is a gathering Page), and the `event_anchored` misleading-name flag. Much smaller: the label layer, where every label now points at one of two kinds instead of seven, and F088's explainer, which may reduce from a page to a sentence.
- **2026-09-15 — Flagged: two exclusive kinds contradicts a ratified rule, and Don's two messages do not settle it.** `nouns.md`: *"A Page may sell, host, or both, and needs no business record to do either."* **Either a Page that does both is two Pages, or selling and gathering are capabilities held together rather than exclusive kinds, or the rule is amended and "or both" goes.** Also noted: with two kinds, *"a Group never changes kind"* now governs the gathering-that-starts-selling case, which stops being an edge and becomes the main path from patron to creator — **it should be re-examined rather than assumed to survive.** [for now]
- **2026-09-15 — "We don't need categories for kinds."** Don's words. **No subject-matter taxonomy sits on top of them, beside them, or inside them** — the list floated in conversation (House and home · Yard and garden · Art and artists · Clothing · Outdoor goods · Services) is not a categorisation of Page kinds and must not be written as one. **If subject matter has a home it is tags**, which already exist as free vocabulary requiring no approval; nothing is to be built for it and no new mechanism written. **One correction forced:** the label layer in `page-kind-tools.md` now states that a label names what someone is *starting*, never what it is *about* — otherwise a subject list enters the mapping and becomes a category layer over Page kinds through the back door. [for now]
- **2026-09-15 — Proposed, not ruled: merge `place`, `interest`, `practice` and `event_anchored` into one Page kind, `community`.** They produce an identical tool set. `groups.md` already calls them "community kinds" in prose. **Result would be four Page kinds: `community`, `family`, `business`, `event`.** `group_event_anchored` survives as nullable provenance, recommended rename `group_seeded_by`. **Recommendation is not to merge before launch** — it buys a person nothing they would notice and touches `member_has_standing_presence`. **The real cost is the one thing genuinely lost: four values' worth of historical intent that is written down nowhere.**
- **2026-09-15 — Flagged, not applied: `event_anchored` is now a misleading value name.** It means a social group seeded by a gathering, usually a recurring one — and *event* now means one-time. **Recommend renaming the value to `seeded` and the table to `group_seeded_by`**, unless the community merge retires it first.
- **2026-09-15 — Proposed, not ruled: a one-time gathering becomes its own Page kind, `occasion`, not a catch-all.** Don: *"Add one time gathering as a page kind type. Perhaps it goes in an other category."* **Recommendation is against the catch-all, on this project's own evidence:** the *"Something else"* free-text field was retired 2026-09-13 because its rows *"sat unread by anything."* **`event_anchored` is not a home for it** — its child table's `seeded_by_item_id` means a social group that formed out of an existing gathering, the opposite shape. **One value does not also fix the farmers-market gap**, which fails the six for the opposite reason (a recurring organization, not a single occasion); that gap stays open. Written up in `planning/PAGE-KIND-OCCASION.md`, with a first cut of the tools mapping — the first Page kind that would look broken without one.
- **2026-09-15 — `product/systems/page-kinds.md` is deleted.** It was written on the retired Item model, duplicated `item.md`, and proposed a schema the codebase already used. Its two surviving contributions — the missing-features list for a one-off, and the Page-versus-Item conflict — are respectively obsolete under the ruling above and now settled. Git history holds it.
- **2026-09-15 — Three things a person can start, written up as `product/systems/page-kinds.md` (draft).** Don's ruling: two durable kinds — someone selling an item or service, and someone with a **recurring gathering of any sort, social, political, spiritual or otherwise, deliberately unconstrained** — plus a one-time gathering that is knowingly thinner. **The thin one's missing features are a written list of nine, not a surprise for later.**
- **2026-09-15 — Clarification: "kind" for the create flow lives on the Page, not the Item.** Don's phrasing said "item kind," but the three choices describe what a Page is *for*. `Page is who; Item is what` already settles it, and his own grouping — "selling an item or service" as one choice — matches. **`items.kind` is unchanged. `code_kind` is unrelated to any of this** — it is a census-code column on `metro_polygons`.
- **2026-09-15 — Schema recommendation, not applied: one table with a `kind` column plus typed child tables, which is what `groups` and `items` already do.** A table per kind is ruled out because it forecloses a Page that both sells and hosts, which is already permitted.
