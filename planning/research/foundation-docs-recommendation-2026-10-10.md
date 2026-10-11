---
id: foundation-docs-recommendation
title: Charter, draft 2 (recommendation only, nothing built)
status: draft
date: 2026-10-11
---

# Charter: draft 2

**As of 2026-10-11. A work in progress. Recommendation only; nothing is built and nothing here is ruled until the PM says so.** Lines marked **[ruled date]** come from a ruling; lines marked **[proposed]** are new and need the PM's yes. Redrafted from the PM's reply on #64.

**Shape:** one page, three parts (Mission, Principles and pledges, Pledge), as Mozilla's manifesto does; guidelines until the organization is formed. It replaces `goals.md` once approved, as the Charter, generated from `DECISIONS.md`.

## Mission (work in progress)

**SocialUs: the people's platform. Members first, always.** [ruled 2026-10-10]

SocialUs exists to serve its members, not shareholders, and to give them a platform to build a better future. [the PM, 2026-10-11; "built to serve its members" ruled 2026-10-10]

## Three flips

We are trying to flip how technology gets used.

**1. Bring people together in person, not stand in for it.** Technology here points people at each other and at a place and a time. It does not replace meeting.
- We currently order what you see by where it is and how recent it is, never by what holds your attention or what someone paid for. [ruled 2026-09-12; F059]
- Ranking is a place, time and relationship engine, not a watch-time optimizer. Browse is complete, not ranked by your interests. [ruled 2026-09-12; `systems/discovery.md`]
- Every Page, post and event is built around something people do together: a gathering, a place, a neighbour. [proposed]
- We measure whether neighbours met, not how long they stayed. [proposed]

**2. Spread wealth among the many, not concentrate it among the few.** The platform exists so what people earn here stays with the people who earned it and the places they live.
- We are never extractive: we take no value from people without giving something back. [ruled 2026-09-12]
- We currently take a share of transaction income on member commerce at a rate the income plan sets, and our fees favour no member over another. [ruled 2026-10-07; 2026-09-30]
- No member can pay to rank above another: visibility is not sold by default. [ruled; guideline in `goals.md`]
- Everyone who makes or hosts something here starts on equal footing: a Page costs nothing to create. [ruled 2026-10-08]
- We collect data to benefit our members, never to enrich shareholders or investors, and we make it easy to opt out. [ruled 2026-10-11]

**3. Design for kindness; make cruelty hard.** We use social norms, not only rules, to keep people good to each other. Three ways to say it, for the PM to choose or mix:
- *"We design for kindness: it's easy to be good to each other here and hard to be cruel."*
- *"Here, kindness is the easy path. We build the app so being good to each other takes no effort."*
- *"We help each other be good to one another."* (the PM's own words on F078, 2026-09-14)

What that means in the product:
- A report hides the content at once and tells the poster why, kindly, in the app, never by email. [ruled; F078]
- Reporting is for real problems: misused reports carry a visible consequence for the reporter, and reports never become a score on a person. [ruled 2026-10-05; F078, F102]
- We currently default to what people would expect socially about who sees what. [ruled 2026-09-30]
- A gentle pause before posting something that is likely to hurt ("Are you sure?"), so people can change their mind. [proposed; reads drafts, so it needs its own ruling (`ai-moderation-scoring.md`)]

## Real examples, a few good ones

Sources: Wikipedia pages are third-party summaries; REI's and Stocksy's own pages blocked my fetch.

- **Front Porch Forum** ([Wikipedia](https://en.wikipedia.org/wiki/Front_Porch_Forum)): geographic forums, posts reviewed by human moderators, a Vermont public benefit corporation paid by local business ads and a fundraiser; a 2023 survey says 80% of respondents think people treat each other with respect there. *Teaches: staying local and keeping a person in the loop makes respect the norm.*
- **Nextdoor's Kindness Reminder** ([Nextdoor, 2019](https://blog.nextdoor.com/2019/09/18/announcing-our-new-feature-to-promote-kindness-in-neighborhoods)): a prompt before posting a likely-unkind reply; in the early test 1 in 5 reminded neighbours edited and negative comments fell by 20%. *Teaches: a nudge beats a ban.*
- **Instagram's "Are you sure you want to post this?"** ([NPR via MPR, 2019-07-10](https://www.mprnews.org/story/2019/07/10/npr-instagram-to-flag-hateful-comments-before-you-send-them)): the head of Instagram said some users post fewer harmful comments after a chance to reflect. *Teaches: a pause works without removing anyone.*
- **REI** ([Wikipedia](https://en.wikipedia.org/wiki/REI)): owned by its members, who pay a $30 lifetime fee and get a yearly dividend normally 10% of what they spent on regular-priced goods, and vote for the board. *Teaches: wealth can flow back in proportion to taking part.*
- **Stocksy United** ([Wikipedia](https://en.wikipedia.org/wiki/Stocksy_United)): a platform cooperative whose artists co-own it with one vote each, with 50% royalties and year-end profit sharing. *Teaches: the people who make the content can share the platform's profit.*

None of these is a promise for us. They show it can be done; how we do it is open until the organization is formed.

## Helping members not feel squeezed, and see a bright future

**The worry.** For children born in the 1980s only about half earn more than their parents, down from about 90% for those born in 1940, and spreading growth as evenly as in the 1940 cohort would reverse more than 70% of that fall ([Chetty and others, Science 2017](https://www.nber.org/papers/w22910)). The news says Gen Z may be the first generation worse off than its parents; that study stops at the 1980s cohort, so I have no source for Gen Z itself.

Five things the product can do, each tied to what is already ruled or built:
1. **Earning.** Put a member's own skill in front of neighbours for free: Pages for makers and services, with no pay-to-rank. [builds on Pages and the Browse ordering ruling]
2. **Lower costs.** Make what is free, cheap or shared nearby easy to find: swaps, borrowing, volunteering, group buys. [the "free things" lens is an open question, F059]
3. **Skills.** Classes, workshops and repeating series from neighbours, and Pages for "teach what you know". [F072 and F074; built in part]
4. **Connections.** Meet the people who lead to work, tools and mentors, in person; "I'm coming" makes a gathering real. [F063, not built]
5. **Prove it.** Track the North Star, Member Flourishing: more time to live and more money to live, both rising. Report it in aggregate, never per person. [`goals.md`, `metrics.md`; reporting is proposed]

## Left out on purpose

No entity or legal terms; no payout promises ("members are the investors" stays a standing ruling, not a Charter line, until the organization forms); no "outside capital" line; no promise on an unbuilt feature. "Never" appears only as "never extractive" and inside the PM's verbatim data line.

## Decision for the PM

**Decision for the PM:** read this draft and pick one.
- **A (recommended):** approve the wording. I then write it to `product/charter.md`, add `regen-charter` (rebuilds it from tagged rulings, runs with the Friday report), and retire `goals.md`; each [proposed] line waits for your yes before it goes in.
- **B:** change the wording; reply with edits and I redraft.
- **C:** a shorter Charter: Mission and the three flips only, with no examples or prospects section.
