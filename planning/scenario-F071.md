---
id: F071
title: A stranger searches, and finds someone
status: draft
horizon: later
rank: 150
date: 2026-09-12
depends: [F059]
---
## Story

Mara has just moved and wants good bread. She opens the app and the search box offers a few things people actually look for — *sourdough*, *yoga*, *guitar lessons*. She types "sourdough". Nothing in her neighbourhood has that word on it, but the curated dictionary maps it to the tags *bread* and *bakery*, so she gets the bakers and the jam maker anyway. On a quieter day the same search finds nothing at all, and rather than an empty screen she is shown what *is* near her, so she learns the neighbourhood is thin rather than that the app is broken. She has not signed in and is never asked to. Meanwhile Priya, setting up her bike-repair Page, sees a line telling her which words will find her — including the tags she picked.

## Acceptance

1. Search matches a Page on three sources: the curated term dictionary, the Page's own tags, and the Page's own text — its description, what it offers, and its posts. A Page matching on any one of them is returned.
2. A term in the dictionary returns Pages carrying the tags it maps to, even when no Page contains that word.
3. A search matching a Page's tag returns that Page. Tags are authored by the creator, not picked from a fixed list, and are visible to anyone viewing the Page.
4. There is no category anywhere — not as a control, not as a field a creator fills in. **Tags are the only vocabulary**, and search is the only filter.
5. The pre-search state shows a small set of example searches in plain words, not a category list or a taxonomy.
6. A search with no matches shows what is near the searcher instead of an empty result set, and says in one line that nothing matched the words used.
7. The no-match state never renders as an error, a dead end, or an empty page.
8. Every search behaviour above works for an anonymous visitor: no sign-in wall, no truncated result set, no prompt to register before results.
9. A Page creator sees, at the point of writing their description and on their own Page, one line telling them what makes them findable.
10. No copy in the creator tips carries legal, tax, or entity language, and none promises placement or ranking.

## Not this

Free-text search over posts' bodies ranked by relevance — matching is enough at this size. Autocomplete, spell-correction, or synonym expansion beyond the curated dictionary. A surface for editing the dictionary. Saved searches. Any use of the embedding tables.

**The creator-facing half of tags is NOT in this scenario and needs its own.** Authoring a tag, the store behind it, and **moderating tags that are now public** — member-contributed content other members see, which [member-content-takedown] bars from production without a report-and-takedown path. This scenario covers only that search matches tags that exist.

**The dictionary's automation is not here either.** An LLM agent proposing entries from submitted tags and zero-result searches, and the human approval gate before anything reaches the live dictionary, are their own work.

## Why

### Open

**Tags are moderated after they appear** — visible at once, removed on report, against a list marking each safe, unsafe or needs review (Don, 2026-10-01).

## Rulings
- **2026-10-25 — The LLM pass runs as a scheduled job and its proposals land in a queue any operator with the moderation role reviews, not the PM; the dictionary grows from both the tags creators create and logged zero-result searches.** Decided by the agent under the 2026-10-25 decision rights (soul and defaults; well-worn): AI helps people and doesn't stand in for them, so a person approves; batching is how Google Search Console and Algolia surface no-result queries. [for now] [replaces none] [binds tiers=planning,code surfaces=tags,search,ai build=none]
- **2026-10-01 — Tags are moderated after they appear, against a list that marks each tag safe, unsafe or needs review.** Don: *"tags will be moderated after and we'll have a list that is safe and unsafe and unknown/needs review."* Answers F071's question (A). [replaces none] [binds tiers=planning surfaces=tags,moderation,reports]
- **2026-09-13 — One vocabulary: tags only. Categories are retired, not reduced.** Don's ruling. **Creators pick or create tags and do not pick a category.** The twelve are gone; **the draft of five is void** and is not a live proposal. [for now]
  - **The reasoning, recorded because it is the part that has to survive:** Amazon and Yelp both look like they have categories and do not. Yelp carries ~1,500 labels a business picks three of; Amazon has ~37,000 browse nodes essentially nobody browses. **Fine-grained labels chosen by the creator, with search as the front door.** A coarse category adds nothing for the person filling in the form — it is one more decision that buys the finder nothing search does not already do.
  - **If a coarse grouping is ever needed** — a map legend, an empty state — **it is derived from tags, never chosen.** Recorded as the shape, not as work to do now.
  - **"Something else" goes**, superseded by tag creation. A creator writing a suggestion and a creator creating a tag were always the same act; keeping both meant two writes for one intent. Its rows seed the initial tag list.
  - **The farmers market dictionary is the seed tag vocabulary**, not a separate artefact. **One list, not two:** what Don writes is the tags that exist on day one, and the search dictionary is that same list plus the terms people type for it.
  - **The composer's category step now has nothing to do.** Whether it becomes a tag step or disappears is open, below.
  - **Tags are creator-authored and public.** Not picked from a fixed list — created. Search matches them.
  - **Categories survive, and the count is open.** A creator still picks one. **Twelve is not the answer** — Don has said twelve is too many and has not said what replaces it. **Nothing may assume twelve**, including `research/search-dictionary-draft.md`, which is organised by the twelve and is now provisional.
  - **The free-text field becomes backend-only.** Not a user-facing category, never displayed. Monitored input. **This answers whether tags replace it: neither — they have different jobs now.** Tags are public and creator-facing; the field is private and operational.
  - **Three inputs, one authoritative dictionary.** Creator tags, the backend field, and zero-result searches all feed the dictionary; **only the dictionary is authoritative.** Nothing reads the three directly at search time and nothing builds a second vocabulary from any of them — three inputs to one list, not three parallel lists.
  - **Automation is intent, with the shape stated and not designed.** Submitted tags and zero-result searches go in; proposed dictionary entries come out.
  - **A human approves before anything reaches the live dictionary. This is a recommendation, not Don's words** — he asked for automation and did not mention a gate. The reason to write it in: **an unattended loop that writes its own search vocabulary drifts, and the failure is invisible** — bad entries do not error, they quietly make search worse, and the surface that reports the problem is a member who searched and found nothing. Cheap to keep, expensive to retrofit.
  - **Moderation changes shape.** A tag other members can see is not the same as a suggestion only an operator reads: it is creator-published visible text, which is an abuse surface. `product/foundation/messaging-problem.md` carries the note.
- **2026-09-12 — Don authors the search dictionary, seeded with farmers market items. Creators pick or submit tags, and submissions grow the reference list.** His words: *"we are going to write the dictionary and start it with farmers market items. and then we need to allow page creators to pick or submit tags so we can grow that reference list."* **Answers the open question of who authors it.** A ~410-term draft across the twelve categories is in `research/search-dictionary-draft.md` so the edit starts from something rather than from blank; **that file is deleted once edited** and the list moves into the app beside `PAGE_CATEGORIES`, because a vocabulary read by code must not also live in a document that can drift from it. [for now]
  - **Tags are new scope, and it is not small.** A tag store, a picker on the composer, a submission path, and **moderation of submitted tags** — an open text field on a public surface is a place people write things that must not appear on the site. Rule 1 already bars member-contributed content from production without a report-and-takedown path, and a submitted tag is member-contributed content. **Named rather than absorbed:** the creator-facing half needs its own scenario; F071 covers only that search matches tags.
  - **It overlaps "Something else" and one of them should go.** `group_category_suggestions` already captures free text from creators in their own words, at publish, with a `normalized_text` index — the same act with a worse name, and still unread by anything. **Two capture mechanisms for one need is the thing to avoid.** Whether tags replace that field or absorb its rows is open, below.
  - **A curated dictionary of search terms maps to categories, built up front.** *"Sourdough"* leads to Food & Drink, *"homemade soap"* to Home & Body. So a search finds Pages that never contain the searched word, which is the point: at launch volumes the words a member types and the words a creator wrote will rarely be the same.
  - **Page creators get tips on how to be found.** The other half of the same mechanism — the dictionary closes the gap from the finder's side, the tips close it from the creator's.
  - **Not embeddings, and this says what would change that.** `item_embeddings` and `member_embeddings` exist, hold **zero rows, and no code reads them** — verified, not assumed. A curated dictionary is cheaper, controllable, inspectable, and has no model to train or drift. **Revisited when the dictionary stops scaling** — concretely: when maintaining it is a recurring cost somebody notices, or when searches that should match are missing because nobody thought of the term. **Not before**, and not on the grounds that the tables are already there. Unused substrate is not a reason to build on it.
  - Scenario: `planning/scenario-F071.md` (`status: draft` — Cowork approves, not Code).
