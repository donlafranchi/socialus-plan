---
id: explore-search-direction
purpose: Where Explore search is heading (Google-style words in one box, no hashtags, natural language later) and how today's grammar and reader should be built to grow into it.
layer: exploration
status: direction
date: 2026-10-11
---

# Search direction

**A direction, not a ruling.** Nothing here is built or approved as scope. It tells today's work which way to lean.

## What the PM said (2026-10-11)

> "I like the way Google does it. I'm not sold on hash tags. Eventually I'd like natural language search."

## What is true today

- Explore's state is `q` (free text), `tags`, `schedule`, `area` and `metro`, carried in the URL (`src/lib/browse/query.ts`). [V]
- F092 (approved 2026-09-19): a filter panel writes its selection into the search box as words a person can read and retype; the results match the box whether the panel or a hand wrote it; text the reader does not understand opens the panel, never errors; clearing the box clears the narrowing. Natural-language understanding is listed under its *Not this*. [V `planning/scenario-F092.md`]
- The grammar and the reader are **not built yet**. Issues #619 (the panel writes the box) and #621 (the reader understands every string the panel writes) wait on the PM approving the words, so this is the moment the shape can still be chosen. [V `gh issue view`]

## What the direction means

1. **Plain words, no symbols.** Tags are words in the box, not `#tags`. The only operator worth keeping is quotation marks for an exact phrase, as Google does. Reserve no other punctuation.
2. **One box is the whole state.** What you see is what is searched; no hidden filter state (this is already F092 criterion 3).
3. **Natural language later** ("live music near midtown this weekend") must arrive as a better *reader*, not a new surface.

## How to build today's grammar so it grows

- **One reader, one result type.** `readQuery(text, context)` returns a structured intent: `{ terms, tags[], when, area, metro, spans[] }`, where each recognised word carries its span, its kind (when, area, tag) and its canonical value. Whatever is left over is free text.
- **The panel's writer is the reader's inverse.** `write(intent)` produces the words; a test asserts `read(write(x)) = x` for every panel output. That is F092 criterion 4 stated as a property, and it is also what lets a later model-assisted reader emit the same intent and have it written back into the box as canonical words.
- **Vocabulary is data, not code.** Time words (today, tonight, this weekend, this week), area names (from `places`) and tag aliases live in tables the reader consults. Synonyms, other languages and neighbourhood names then grow by adding rows, and a natural-language layer reuses the same tables.
- **Failure is free text.** Anything not understood searches as words and offers the panel (F092 criterion 5). A future model reader gets the identical contract: it may only *suggest* an intent, which is rewritten into the box for the person to see and edit; if it is slow, down or unsure, the rule reader answers.
- **A model reader may only output the intent schema.** It never writes ranking, SQL or filters directly. Ranking stays the discovery core's (no payment, no attention). [for now — the tool side only; newer direction 2026-10-12, see PRINCIPLES.md "two sides"; under review]
- **Links carry the text.** Once the grammar lands, `?q=` plus `metro` is the whole link; the older `category=` and `schedule=` params are still read. A natural-language reader then cannot break a shared link.
- **Learn from what is not understood.** Count unparsed strings in aggregate (no member ids) to grow the vocabulary. This is also F071's open question, how the search dictionary grows.

## Not now, and open

Which model, where it runs and what a query costs; whether the text of a member's search may leave our servers (member privacy comes first); languages; neighbourhood names per metro. Each is a decision for the day a natural-language reader is scoped, with its own scenario.

## Precedents already cited on #619

Gmail's filter panel writes operators into the box (support.google.com/mail/answer/7190); GitHub issue search qualifiers (docs.github.com, searching issues and pull requests); Linear's visible filter state (linear.app/docs/filters). Google's own search is the model for one box and plain words.
