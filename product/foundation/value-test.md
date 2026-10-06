---
id: why-value-test
purpose: Six questions every feature and field answers before it is built here — whether it belongs on SocialUs at all.
layer: why
status: active
reviewed: 2026-10-05
---

# The value test

**Don, 2026-10-05: "go."** Every new scenario answers these in its `## Why`, one line each, before anyone writes acceptance criteria (from F103 on; `scripts/lint.sh` checks it). They ask whether a thing belongs on SocialUs at all, not how to build it.

## The six questions

1. **Lives somewhere better?** Does it already live on their website, their social, or Google? Then link out, per *"we send traffic to a venue's own site and channels rather than capturing it"* (2026-09-30).
2. **Only locals know?** Home bakers, pop-ups, a run club with no website: what nobody else lists is our edge.
3. **Gets people together?** In person. That is the mission, so it counts double.
4. **Stays fresh on its own?** Dated things renew themselves; static facts go stale and lie quietly.
5. **Who keeps it current?** Anything that needs the solo operator, or constant upkeep from an owner, is a cost — one person runs this with a day job.
6. **Better as more people join?** Follows, vouching and exchange grow with the network; a field on one Page doesn't.

No score and no threshold. A feature that fails several should say why it's still worth it; one that passes 2, 3 and 6 is the shape we want.

## Worked example: business hours

- **Lives somewhere better?** Yes — the business's own site and Google Maps. **Fails.**
- **Only locals know?** No; the business publishes them.
- **Gets people together?** Indirectly at best.
- **Stays fresh on its own?** No — holidays and seasons make them wrong. **Fails.**
- **Who keeps it current?** The owner, every time they change. **Fails.**
- **Better as more people join?** No.

So hours are currently hidden (2026-10-05), and when shown at all they link out to the business's site or Google Maps rather than being kept here.

## Strong passes

- **Dated Posts** — only locals know, they bring people together, and the date keeps them fresh.
- **"How do people find you?"** — a pop-up's or a roaming maker's whereabouts live nowhere else.
- **Unclaimed Pages for businesses without a web presence** — the find-it-nowhere-else case, with credit and a link wherever a site exists.
- **Moneyless exchange** — giving, swapping, lending and skill trades: only locals, in person, better with every neighbour who joins (`product/needs/member-journey.md`, Exchange).
