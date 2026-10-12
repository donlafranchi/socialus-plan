---
id: F061
title: Someone creates a Page worth showing people
status: building
horizon: now
rank: 10
date: 2026-09-10
depends: []
amended: 2026-10-01 — Don: creation is one question, the kind; it lands on the draft Page. Criteria 1–3 moved to F056 (editing); criterion 5 (resume returns to review) retired. 2026-10-04 — Don: each kind is a question with a one-line purpose.
---
## Story

Don taps create to make his own business's Page. He's asked one thing: what kind of Page it is. Each kind says what it's for and which parts it comes with by default, and the screen tells him this just starts the process. He picks one and lands on his draft Page, where he fills in everything else — the name, where it is, its tags, a photo, two sentences — and publishes when he's ready.

## Acceptance

1. **Creating a Page asks one question: its kind.** Each kind is offered as one question with a one-line purpose, for example "Have a business where you sell products or services?" (Don, 2026-10-04), and the screen says this just starts the process (Don, 2026-10-01).
2. **Creation lands the owner on their draft Page**, where they fill in everything else, the name included. Address, neighbourhood and tags are set there (F056 criteria 6–8).
3. A Page's map/card placement comes from a single resolver evaluated at read time — nothing precomputed or cached.

## Not this

Editing a Page, draft or live (F056). Browse, search, or the map's rendering of any of this (F059). Verification of any kind.

## Rulings
- **2026-10-05 — Create has a fourth answer, "Be creative", with the line "Start anything that helps you find your people.", after the three questions, which stay. It lands on the same draft Page as a group.** Don: *"A be creative option. this is a local discovery app. we exist to help you find your people."* The one Create answer that is not a question; the other three keep the 2026-10-04 rule. Copy stays a draft ([public-is-draft]). No role label. `socialus-web` #381. [binds tiers=planning,code surfaces=create,copy]
- **2026-10-04 — Each Create kind is one question with a one-line purpose, for example "Have a business where you sell products or services?".** Don. F061 criterion 1 restated. [replaces 2026-10-01: Each kind is explained — what it's for and which components it has by default —] [binds tiers=planning,code surfaces=create,copy]
- **2026-10-01 — Creating a Page is one question: its kind, and the screen says this just starts the process. Creation lands the owner on their draft Page, where they fill in everything else, the name included.** Don: *"Creating the page only needs the kind of page. We can explain the different types of pages and what they are for or how they come as default and that this just starts the process and the next part is where they fill out their info. It could be just one question."* F061 restated: criteria 1–3 (address, neighbourhood, tags) move to editing (F056 criteria 6–8); criterion 5 (resume returns to review) is retired. Tags are set on the draft Page and still required to publish. "Stays six steps" was an agent's line, not Don's; the seventh-step question in `surfaces.md` goes with it. F060 criteria 1–2 now match F082: the rules agreement comes before each publish. Builds on F061, F056 and F060. [replaces 2026-09-13: Same position in the walkthrough, which stays six steps;] [replaces 2026-09-13: Not deferred to the Page editor] [replaces F061: Resume returns to the first incomplete step, including review] [replaces F060: F082's one-time self-attestation is the only thing that precedes it] [replaces F060: made once before this flow] [binds tiers=planning,code surfaces=page-create,page-edit,page-publish,tags,copy]
- **A point asserts presence; nothing absent may make that assertion.** Position for a Page is resolved at read time from its Items, never stored or cached.
