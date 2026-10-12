---
id: F064
title: Someone asks for something that isn't built
status: approved
horizon: next
rank: 130
date: 2026-09-10
depends: []
approved: 2026-09-07
---
## Story

Priya is making a Page for bike repair and none of the labels are hers, so she taps Other and says what she is actually running. Sam taps an option marked "not built yet"; it's acknowledged once, with no count shown and no date implied. Neither of them is told a date, a plan, or where they sit in a queue, and neither hears back.

## Acceptance

1. **One signal table serves two sources** — an unmapped label, and an Other description (F088) — each row carrying which source it came from. *(Reduced from three on 2026-09-15: a zero-result search is an honest answer, not a signal.)* *(Amended 2026-09-15. This read: "Free-typed category text renders on the Page as the Member's own words and is search-matchable, without becoming a filter." **That described the twelve categories and the "Something else" field, both retired 2026-09-13** — building it as written would ship a deleted field.)*
2. A tap on a not-yet-built option is acknowledged; a second tap from the same person is a no-op enforced by a constraint.
3. No copy anywhere in this flow implies a date, plan, or queue position.
4. The person who signaled sees no count of how many others did.
5. The operator can group the raw signal table by subject and see a ranked list, with no screen built for it.

## Not this

A public leaderboard or "most requested" surface. Any admin UI for the signal table. Restoring the free-text category field — it was removed deliberately, not lost. Replying to anyone.

## Rulings
- **2026-09-15 — A search that returns nothing is an honest answer, not a gap to fix.** Don: there may genuinely be nothing, and we can say that. **This removes zero-result searches as a source for the signal queue** — F064 now serves two sources, an unmapped label and an Other description, not three. **It does not retire the search dictionary**, which still grows from the tags creators create; it retires the second of its two inputs. **Resolves the open question "How does the search dictionary grow?" to A alone** — the creator's vocabulary — where the standing recommendation had been A and B together.
- **2026-09-15 — Triage outcome that matters most: "already covered" is a labelling failure, not a dismissal.** Three people describing a thing the product already does means a label is missing, and the label layer makes the fix one row.
