---
id: F080
title: No sensitive content, while we grow into a platform with staff
status: approved
horizon: now
rank: 70
gates: launch
date: 2026-09-14
concept: new
depends: [F077]
approved: 2026-09-14 — Don's ruling
amended: 2026-09-30 — Don: widened from pictures of children to sensitive content (children, animals and pets, anyone who can't fend for themselves), while we grow into a platform with staff. Earlier the same day: no attestation and no detection; a message at posting states the rule; reports are the backstop. (2026-09-27: no unlock; a photo rule, not a topic rule.)
amended: 2026-10-06 — the PM: the uploader confirms a photo shows no children; still nothing pre-screened; a report hides the photo at once pending operator review.
---
## Story

Maya runs a Saturday kids' craft table at the farmers market. She writes a post about it — ages, times, what to bring — and it publishes like any other. As she posts, the app asks her, while SocialUs grows into a platform with staff, not to post sensitive content: children, animals and pets, or anyone who can't fend for themselves. Her photo from last week shows the children at the table, so she uses one of the finished crafts instead. If someone had posted the other one, a single report would take it down. Nothing unlocks it for now — no tier, no request.

## Acceptance

1. **No image containing a child, an animal or pet, or anyone who can't fend for themselves is permitted, from any member, while we grow into a platform with staff.** The rule is stated and affirmed: the uploader confirms a photo shows no children. Every photo is also checked against known child-abuse hashes, and every post's text and images are screened automatically before they publish (2026-11-12).
2. **Text is not in scope.** A Page, post or description about a children's activity publishes normally; only an image is not permitted.
3. **No toggle, setting, tier, request or workaround allows it**, for any member. Lifting it, when there is staff, needs a new ruling, not a configuration change.
4. A published image reported as containing a child is caught by F078: a children-category flag hides at any bar (F078 criterion 8, `socialus-web` #284) and texts the operator, pending review.
5. **Wherever a member posts, the app asks them not to post sensitive content, and why; and each photo upload asks them to confirm it shows no children.** Placeholder copy in the app's copy module ([public-is-draft]); #221 carries the draft. The tone is the reciprocity principle: *"We are careful and supportive of our members and we ask that they be the same towards us"* (Don, 2026-09-30).

6. **Where a member posts, one short line encourages good, decent content: a positive reminder, not a list of don'ts.** PLACEHOLDER, the PM's words pending ([public-is-draft]): *"[PLACEHOLDER: positive posting reminder, the PM's copy to come]"*. It ships only with his words.
[open-question owner=don raised=2026-11-12] What does the positive posting reminder say? It encourages good and decent posts and lists nothing not to post.

## Not this

Any rule about text, topics, or Pages that serve children. Building any verification tier. Human review before a photo is visible. Detecting a child in a photo by AI as a gate on its own; the screen flags, the report path decides (F102).

## Why

**Reports and automated screening enforce it together** (reporting since 2026-10-01; screening since 2026-11-12). The ask at posting covers anything sensitive — children, animals and pets, anyone who can't fend for themselves — in any form. The report category widens from children to **sensitive content**, and it still hides at any bar. A pet groomer or dog walker can still show their work; the animals part is asked, not enforced.

### Why screening now (2026-11-12)

The 2026-10-06 call skipped pre-screening for cost and review load. Phone sign-up made the stance explicit: nobody posts anonymously, and we act fast. Screening is automated, so it adds no human review: a likely violation is held and goes down F102's report path, unattended Tuesday to Thursday. Hash matching is free (Cloudflare) and checks every photo served from our address. Earlier reasoning: git history.

## Rulings
- **2026-11-12 — Every photo is checked against known child-abuse hashes, and every post's text and images are screened automatically before they publish; the uploader's confirmation that a photo shows no children and the instant hide on report stay.** The PM approved the safety package: *"no user of ours thinks that they can post anything anonymously … we will know who they are and will take swift action."* Hash first: a match never reaches an AI provider (F100, 2026-10-05). Hashes through the Cloudflare CSAM Scanning Tool (#641). Path: well-worn. [for now] [replaces 2026-10-06: Pictures of children are currently handled on the uploader's word plus member reports: uploaders confirm a photo shows no children, nothing is pre-screened, and a report hides the photo at once] [binds tiers=planning,code surfaces=uploads,posting,reports,moderation,copy] Issue: #1288.
- **2026-11-12 — Where a member posts, a positive reminder encourages good, decent content, never a list of don'ts; a marked placeholder until the PM's words.** The PM: *"do we also need a reminder about posting rules. Not about what not to post but to make sure they're posting content that is good and decent? … put something in there for the second part as placeholder while I work out the copy."* Path: new territory. [for now] [replaces none] [binds tiers=planning,code surfaces=posting,copy build=none]
- **2026-10-01 — We can't enforce the sensitive-content rule; we rely on reporting. The ask at posting covers anything sensitive, in any form, and the children report category widens to "sensitive content", still hiding at any bar.** Don: *"We can't enforce this. We rely on reporting. A if we can."* Answers F080's question; `socialus-web` #221. [replaces none] [binds tiers=planning,code surfaces=posting,reports,moderation,copy]
- **2026-09-30 — While we grow into a platform with staff, we ask members not to post sensitive content: anything that would need a moderation team. Sensitive currently means children, animals and pets, and anyone who can't fend for themselves.** Don: *"while we grow into a platform with staff we are asking our users to support our mission by not posting anything sensitive that would require a moderation team. Sensitive items are generally anything related to children, animals/pets, or any other group that "cannot fend for themselves"."* **Why:** there is no moderation team yet, and we don't want to subject anyone on our team to unpleasant content (the reciprocity principle below). **Temporary:** it holds until there is staff to moderate, and lifting it is a new ruling. Widens F080 from pictures of children; the message at posting states it, and reports (F078) stay the backstop. The copy is a placeholder in `socialus-web`'s copy module ([public-is-draft]); the build task, #221, has a draft. Whether the report category and the photo-only scope widen too is open in F080. [replaces 2026-09-27: No pictures of children, full stop.] [replaces 2026-09-30: the app asks them, for safety reasons, to post no content with children.] [replaces F080: No pictures of children, from anyone] [binds tiers=planning,code surfaces=page-photos,posting,moderation,copy]
- **2026-09-27 — It is a photo rule, not a topic rule.** Don, defining the term the ruling below left open. **An image containing a child is not published by anyone; text about a children's activity is not caught** — a post about a kids' craft table publishes, a photo of the children at it does not. F080 rewritten around it; F078 criterion 8 hides a children flag at any bar. **The rule now needs a detection point and the repo has none**: nothing can see what is in a picture, and every Page photo uploads from the browser to a public bucket. **F082's step was checked as a home**: right place to *state* the rule, wrong place to *enforce* it — it runs once, misses stewards who never publish a Page of their own, and affirms locality and provenance. A one-line wording is proposed in F082 § Why, not adopted. [for now] [binds tiers=planning,code surfaces=page-photos,moderation] [replaces 2026-09-14: F080's scope confirmed]
- **2026-09-27 — Nothing unlocks F080. There is no stronger verification and none is being built.** Don's ruling on `socialus-web` #221. The content is not permitted at all; **allowing it later needs a new ruling, not a configuration change.** [binds tiers=planning,code surfaces=page-photos,verification] [replaces 2026-09-14: Nobody may post anything about a child, at any trust tier]
