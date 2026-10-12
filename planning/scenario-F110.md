---
id: F110
title: A Support page shows the rough roadmap and how to help fund it
status: draft
horizon: later
rank: 290
date: 2026-10-12
---
## Story

A neighbour who likes what SocialUs is doing opens Support. She sees what the platform is working on now, what is next and what comes later, in plain words, and the next milestone it is funding. She sees how to be told when giving opens. Nothing on the page takes her money today.

## Acceptance

Backlog; not approved. Criteria follow the PM's call on timing and `socialus-legal`'s clearance. The shape so far:

1. **The roadmap on the page is generated from scenario `horizon` and `rank` and the socialus-web milestones (the dashboard's Where we're going), never hand-kept.** A build step reads Now, Next and Later and renders them as plain-word lines (no ticket ids, no dates beyond the section names). A line changes only when `ROADMAP.md` does. Cut and Won't are not shown.
2. **The page headlines the next funding milestone, not a finished goal** (ruling 2026-10-07, `product/systems/contributions.md`). The numbers stay private in `socialus-legal` until counsel clears publishing them.
3. **Held for `socialus-legal`, not designed here:** whether and how donations are accepted, the form and terms of any gift, tax treatment, who receives the money, any thank-you or reward for giving, and any promise about what a gift buys. No payment flow, amount, button or terms card is specified until counsel clears it and an entity exists.
4. **Until then the page offers one action: be told when giving opens** (an email, like F076's tell-me-when-it-opens). No money moves.
5. **Plain, honest words.** The page says what is built and what is only planned, uses the Charter's wording rules, and promises no return, share or payout (ruling 2026-10-11, backing).

## Not this

A payment form, a donation amount, a tier, a perk, a tax statement or a receipt. A public thermometer or totals. A hand-written roadmap copy.

## Why

- **Lives somewhere better?** No: GitHub Sponsors, Open Collective and Wikipedia's banner all show what the money is for; ours reads from the live roadmap.
- **Only locals know?** No: the roadmap is the platform's own.
- **Gets people together?** Indirectly: people who want it to exist can follow it.
- **Stays fresh on its own?** Yes: it is generated from scenario frontmatter and the milestones.
- **Who keeps it current?** Nobody; scenario frontmatter and the milestones are the only input.
- **Better as more people join?** Yes: more members make the roadmap's asks more real.

**Path: new territory.** It touches money, legal exposure and member trust; nothing is decided about taking money. Precedents: [Open Collective](https://opencollective.com), [GitHub Sponsors](https://github.com/sponsors), [Wikimedia fundraising](https://donate.wikimedia.org).

[open-question owner=don raised=2026-10-12] When does the Support page ship? A) Beta, as roadmap and the "tell me when giving opens" action only. B) After beta, once `socialus-legal` has cleared how giving works. Recommend A: it carries no money and no legal exposure.

[platform none]
