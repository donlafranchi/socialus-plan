---
id: F092
title: Narrowing happens in a modal that writes what it did
status: approved
horizon: later
rank: 90
date: 2026-09-19
depends: [F091]
approved: 2026-09-19 — Don ruled filtering lives in a modal that writes its selection into the search box as text, Gmail-style.
---
## Story

Rae wants coffee this weekend. She taps the filter control beside the search box; a panel comes up over the results. She picks *this weekend* and *coffee* and taps apply. The panel closes and the search box now reads what she chose, in words. The results narrow to match. Next time she skips the panel and types it herself, because she has seen what it looks like.

## Acceptance

1. No filtering control sits beside the results. The only thing on the results surface is the control that opens the panel.
2. Applying dismisses the panel and writes the selection into the search box as text a person can read and retype.
3. The results match the text in the box, whether that text was written by the panel or typed by hand.
4. Every string the panel can write is understood by the reader of that box.
5. Text that is not understood opens the panel. It never errors and never empties the results without saying so.
6. Clearing the box clears the narrowing.

## Why

**This threads design-language principle 10 rather than amending it** *(Don, 2026-09-19)*. That principle already says filtering controls live in *a filter surface, never on the results surface* — a modal is the shape it names. Criterion 1 is what keeps it honest: `ActiveFilterChips` and `KindFilterPills` ship on Explore today and are exactly the chip and pill rows the principle removed. They go with the rewrite; surviving beside the panel would make the panel a dodge.

**Criterion 4 is the whole risk, and it is also what makes this affordable.** The panel defines the grammar, so the parser's required input is the set of strings the panel emits, plus graceful failure. It does not have to understand prose. **A panel that writes a string its own reader cannot parse is worse than no panel** — the product would contradict itself in public.

**Criterion 2's stated purpose is teaching** — Don: the box demonstrates the syntax by writing it, and typing it directly is the same path once someone has seen it. That is why the text has to be readable words rather than an opaque encoding.

**Criterion 5 replaces Issue #57's "unparseable input falls back to chips."** Chips are the thing principle 10 removed.

## Not this

Natural-language understanding. Saved searches. A second entry point to the panel. Narrowing that survives a link without being in the text — the text is the state.

## Rulings
- **2026-10-11 — Search box text is plain words, as Google writes it, with no hashtags: tags are written as plain words in lowercase matching the panel's labels (`coffee live music this weekend`, not `#livemusic`). The box grammar and reader are built so they can grow into natural-language search.** The PM, 2026-10-11, on `socialus-web` #619 and #621 (F092 criteria 2 and 4). A separate product note captures the natural-language search idea. [replaces none] [binds tiers=planning,code surfaces=search,explore] Issue: #619.
- **2026-09-19 — Filtering lives in a modal that writes its result into the search box as text.** Don's ruling, and it **threads principle 10 rather than amending it**: that principle says filtering controls live in *a filter surface, never on the results surface*, so a modal is the shape it already permits. **It appears on request and dismisses on apply** — nothing persistent sits beside the results but the control that opens it, which is one button and not a pill row. **Applying writes the selection into the search box as text, Gmail-style**, so the person sees the query they just built. **The stated intent is teaching**: the box demonstrates the syntax by writing it for them, and typing it directly is the same path once they have seen it. **This makes the query parser load-bearing, which it was not before** — but it also bounds it: the modal defines the grammar, so the parser's required input is exactly the set of strings the modal can emit, plus graceful failure on anything else. **Free-typed prose that does not parse opens the modal rather than erroring**, which replaces Issue #57's *"unparseable input falls back to chips"* — chips being the thing principle 10 removed. **What this supersedes:** the 2026-09-12 line *"search is the filter"* stands, and this says how a person gets to the syntax without knowing it cold. **What has to be true or the design contradicts itself in public: the modal's output grammar and the parser's input grammar are one grammar.** A modal that writes a string its own parser cannot read is worse than no modal. [for now]
- **2026-09-12 — Zero filter pills outside the filter view.** Don's ruling. Filtering controls live in a dedicated filter surface, not on the results surface itself — no pill row, chip row or control strip alongside results. **The ruling is the constraint, not the solution:** what replaces the pill row is deliberately unchosen, and a research pass is running to find options with real examples. Nothing may specify a replacement shape before that lands. Stated in `product/ui/design-language.md` principle 10, which is its one home; `product/ui/surfaces.md` points at it rather than restating it. **Why it came up:** the Page rewrite replaces seven Item-kind pills with twelve Page categories, and twelve longer words do not fit a phone-width row. Applied to `socialus-web` #53, which specified pills on the results row.
