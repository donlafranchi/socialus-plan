---
id: what-design-language
purpose: Design principles the code can't self-document — the reasons; the tokens themselves live in the app code.
layer: what
status: active
---

# Design language

White canvas + photography + navy for actions, with a little gold. The chrome disappears so the content speaks.

## Principles — the why, not derivable from the code

1. **Navy for actions, gold as a highlight under 5% of the screen** *(Don, 2026-10-04, palette option A "Anodised")*. Navy marks what you can press; gold sits only on navy, as small accents, the way gold parts sit on a dark bike frame. Present enough to register, restrained enough that photos lead. The plan and contrast numbers: `socialus-design/palette/PALETTE-PLAN.md`.
2. **Dark neutral text, never brand-colored.** The accent never appears on paragraphs or headings — only on interactive surfaces and accents.
3. **White-dominant canvas.** No tinted backgrounds, no graduated color across components. The feed breathes.
4. **Photography is sacred.** No color pills, frosted badges, or overlays on photo cards. Metadata lives in the text zone below the image, never on top of it.
5. **No color-block cards.** A card without a photo is text-forward and neutral — never a solid-color rectangle.
6. **Hairlines over shadows.** Separation is a 1px border; shadow is reserved for hover lift and overlays.
7. **One typeface, restrained scale.** Inter, four weights, tops out at 32px in product surfaces.
8. **Controls sit where the hand already is** *(restated by Don, 2026-09-13 — this replaces "bottom-anchored, thumb-reachable," which stated the tactic and lost the reason)*.
   - **On a small phone, that means near the bottom**, because it is one-handed operation and the top of the screen is where the thumb cannot reach. **That is the whole point of the rule** — not the bottom edge for its own sake.
   - **On a larger screen it matters less**, because those are usually two-handed. There the aim is the **left and right edges**, where either hand already is, rather than the bottom.
   - **This is an aim, not a prohibition.** Don: *"sites like AllTrails and Airbnb also have very nice layouts even though they don't follow the guideline I just described."* Good products break it and remain good, so a layout that puts a control elsewhere **needs a reason, not an exemption** — and the reason can be as ordinary as "this is where it reads best."
   - The browse search row, which also carries the list/map toggle (2026-09-13), sits at the top. Recorded as a judgment rather than as a violation being tolerated.
9. **No overlay ever carries color or decoration for its own sake** — an overlay exists to hold a state (loading, selected), never to add visual interest a photo or a hairline can't supply.
10. **Filtering controls live in a filter surface, never on the results surface.** *(Ratified 2026-09-12, Don.)* **Zero filter pills** — no pill row, chip row or control strip sits alongside results. A results surface shows results. Sibling of principle 8: both say a control belongs where the thumb and the attention already are, not stapled to the content. **What replaces the pill row is settled the same day: search** — categories stop being a visible control entirely (`../foundation/model.md` § Search is the filter). A Page still declares a category; no surface renders one as a control.

11. **Never show someone a zero counter on their own work.** *(Moved here 2026-09-14 from the retired `../foundation/role-language.md`, where it sat among naming rules; it is a UX rule and always was.)* A gathering nobody has joined reads *"No one's in yet. Be first."* to a visitor and *"Nobody's in yet"* to the host — never "0 RSVPs." A zero on your own thing is a small daily failure notice, and the surfaces are nearly all empty at launch. **Confirmed independently by Don in `../foundation/voice-and-tone.md` 2026-09-15**, in the same words.

12. **Design up to about 1440px** *(Don, 2026-10-04)*. 13–16" laptops are the large screens that matter. Above that, the content cap and centring are enough: someone on a 27" screen is assumed to have two windows side by side, each about 1280px, so there is no separate 27" layout.

## Tokens — the reasons only

**Design tokens live in the app code, the single source of truth** *(Don, 2026-10-01, design decision 7)*: `globals.css` and the components hold every value — colour, type, radius, shadow, motion. This section keeps only why, per `ops-pattern/process/LIVING-DOCS.md`; a value written here would be a second description that drifts.

- **Navy for actions, gold under 5%, and gold only on navy.** Gold on white fails contrast and reads washed out. The chrome steps back so photographs and what people wrote carry the page.
- **Body text isn't brand-coloured,** because reading comes first.
- **Semantic colours mean system feedback only** — toasts, validation, alerts. Colour used as decoration stops meaning anything when it has to.
- **Ownership colour is one axis, on badges and map pins only,** so a reader learns it once.

## Rules the components must hold, that the components alone won't tell you why

- **The card's media block always renders**, present or absent photo, because a grid whose card height depends on per-row data reads as broken rather than varied. The no-photo state is a neutral field with the kind's glyph — never a color, never an emoji, never a per-kind palette (the one-accent budget doesn't stretch to a seven-color kind ramp, and emoji render inconsistently across platforms).
- **A Page's default art (no photo) is its kind's default image or icon** *(Don, 2026-10-01)* — the same on every load, to every viewer. Placeholder art handsome enough to pass for a real photo misrepresents the place; a photograph-quality placeholder removes the reason to ever add a real one. No stock photography, ever — it depicts somewhere that isn't there.
- **One primary (accent-filled) button per screen.** Two competing primaries is a smell that means the page hasn't decided what it wants the visitor to do.
- **Multi-step composers write progress on advance**, not on final submit — the Member is editing a half-built thing from step one, not filling a buffer. This is what makes "your work is saved" an honest claim rather than a hope.
- **Trust microcopy next to a primary CTA states what's true right now, in the present tense — never a promise about the future.** ("Listing costs nothing" states a present fact; it does not promise a future price. A recipe that generates promise language generates it on every surface that copies the recipe.)
- **An owner-only management affordance renders inline on the real public page**, never as a separate "manage" view — the owner should see what everyone else sees, with controls layered on top.
- **Layout by width** *(Don, 2026-10-01)*. Below 1280px an owner gets the phone owner bar and sheets; the owner panel appears from 1280px. On a phone, a detail page's action bar sits above the nav. The nav moves to the top at 744px. The nav is hidden in wizards and full-height sheets, so the task has the whole screen. Explore's list and map: F059 criterion 5.

## Anti-patterns

Two filled-accent buttons side by side. A primary-styled button in a destructive context. Routing to a full auth page from a card action instead of a modal at peak intent. Producer recruitment as the loudest thing on the homepage — it's the smaller audience; consumer signup wins the hierarchy.

## Rulings
- **2026-10-07 — On Explore's map, an exact public address is a classic teardrop pin (a round head tapering to a point); a place known only to a metro, city or neighbourhood is an area marker: a soft translucent disc with a count, no point, no tail. The two differ in shape and fill and are distinct from clusters and from any boundary outline. Items sharing a centroid group into one area marker that opens to a list; pins at one address spread apart.** The PM, option A. Because the map answers "is anything going on around me", not "where exactly": a disc cannot imply a front door, and a pin must never be used for a place that is only an area. Built in `socialus-web` #475. Rationale and rejected options: `planning/research/map-markers-2026-10-07.md`. [for now] [binds tiers=planning,code surfaces=explore,map]
- **2026-10-04 — We design up to about 1440px. Above that, the content cap and centring are enough, and a 27" screen is treated as two side-by-side windows of about 1280px each. There is currently no separate 27" layout.** Don: *"13-16 are most important for large screens. If users need more screen like 27" we can assume two windows open with different purposes side by side."* `product/ui/design-language.md` and `socialus-design/screens/design-language.md` restated; the 1680px cap in the page shell (#296) stands. [binds tiers=planning,code surfaces=layout,shell]
- **2026-10-04 — The palette is option A, "Anodised": a white base, navy `#24405A` for actions, and gold only as accents on navy. Design-language principle 1 is now "navy for actions, gold as a highlight under 5% of the screen".** Don chose it from `socialus-design/palette/PALETTE-PLAN.md`; it fixes the accent's contrast failure. Token values live in the app code; Code adopts them in #325. [binds tiers=planning,code surfaces=design-language,tokens]
- **2026-10-01 — Design tokens live in the app code as the single source of truth; the design-language doc keeps only the reasons.** Don's design decision 7, per `ops-pattern/process/LIVING-DOCS.md`. `product/ui/design-language.md` § Tokens rewritten to reasons only; its names and values are gone. Colours are still undecided. [binds tiers=planning,code surfaces=design-tokens,design-language build=none]
- **2026-09-13 — Principle 8 restated: controls sit where the hand already is, and it is an aim rather than a prohibition.** Don's words: *"we aim to have as many button controls near the bottom of the screen for easy one hand operation on smaller mobile screens — that's the point. Larger screens is less necessary since they are usually two hand operation and then we'd want the controls at the edges of either side of the screen. Also sites like AllTrails and Airbnb also have very nice layouts even though they don't follow the guideline I just described."*
  - **The rule had stated its tactic and lost its reason.** "Bottom-anchored, thumb-reachable" reads as a rule about an edge; **the reason is one-handed reach on a small phone**, and the bottom is only where that lands. Anything derived from the old wording — including that a top-anchored control is automatically wrong — was derived from the tactic.
  - **Large screens get a different answer, not a weaker one:** two-handed operation, so the aim is the **left and right edges**, not the bottom.
  - **It is explicitly not a prohibition.** Don names AllTrails and Airbnb as good layouts that break it. **A control placed elsewhere needs a reason, not an exemption.**
  - **Consequence, stated because it undoes earlier bookkeeping:** the sticky browse search row has been carried since 2026-09-04 as an *accepted violation for one release*, with the expectation that a chrome rework would repay it. **Under the restated principle it is a judgment, not a debt** — the machinery built around it (a standing exception, a dated carve-out, a follow-on scenario to "fix" it) is heavier than the principle now warrants. **Whether that follow-on work is still wanted is Don's call and is not decided here.**
