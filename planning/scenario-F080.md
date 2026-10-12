---
id: F080
title: No sensitive content, while we grow into a platform with staff
status: approved
horizon: now
rank: 70
gates: launch
date: 2026-09-14
depends: [F077]
approved: 2026-09-14 — Don's ruling
amended: 2026-09-30 — Don: widened from pictures of children to sensitive content (children, animals and pets, anyone who can't fend for themselves), while we grow into a platform with staff. Earlier the same day: no attestation and no detection; a message at posting states the rule; reports are the backstop. (2026-09-27: no unlock; a photo rule, not a topic rule.)
amended: 2026-10-06 — the PM: the uploader confirms a photo shows no children; still nothing pre-screened; a report hides the photo at once pending operator review.
---
## Story

Maya runs a Saturday kids' craft table at the farmers market. She writes a post about it — ages, times, what to bring — and it publishes like any other. As she posts, the app asks her, while SocialUs grows into a platform with staff, not to post sensitive content: children, animals and pets, or anyone who can't fend for themselves. Her photo from last week shows the children at the table, so she uses one of the finished crafts instead. If someone had posted the other one, a single report would take it down. Nothing unlocks it for now — no tier, no request.

## Acceptance

1. **No image containing a child, an animal or pet, or anyone who can't fend for themselves is permitted, from any member, while we grow into a platform with staff.** The rule is stated and affirmed, not detected: the uploader confirms a photo shows no children, and nothing checks a photo before it is visible.
2. **Text is not in scope.** A Page, post or description about a children's activity publishes normally; only an image is not permitted.
3. **No toggle, setting, tier, request or workaround allows it**, for any member. Lifting it, when there is staff, needs a new ruling, not a configuration change.
4. A published image reported as containing a child is caught by F078: a children-category flag hides at any bar (F078 criterion 8, `socialus-web` #284) and texts the operator, pending review.
5. **Wherever a member posts, the app asks them not to post sensitive content, and why; and each photo upload asks them to confirm it shows no children.** Placeholder copy in the app's copy module ([public-is-draft]); #221 carries the draft. The tone is the reciprocity principle: *"We are careful and supportive of our members and we ask that they be the same towards us"* (Don, 2026-09-30).

## Not this

Any rule about text, topics, or Pages that serve children. Building any verification tier. An automated image check or human review before a photo is visible — ruled out 2026-09-30 and not for beta (2026-10-06). Known-image hash matching stays planned in `socialus-legal`'s NCMEC plan (step 2); this scenario covers only the broader no-pictures-of-children policy.

## Why

**We can't enforce this; we rely on reporting** (Don, 2026-10-01, option A). The ask at posting covers anything sensitive — children, animals and pets, anyone who can't fend for themselves — in any form. The report category widens from children to **sensitive content**, and it still hides at any bar. A pet groomer or dog walker can still show their work; the animals part is asked, not enforced.

### Why a message and reports, not a check (2026-09-30)

**Nothing in the repo can see what is in a picture**, and every Page photo uploads from the browser to a public bucket. A check therefore meant a person holding every photo, or the uploader's word. Don chose neither: the rule is said where people post, and a report takes a photo down at once, whatever the metro's bar (F078 criterion 8). **What this accepts:** a picture of a child is public until someone reports it.

### Why the uploader's word and reports (2026-10-06)

**The PM, 2026-10-06 (`socialus-web` #221):** pre-screening every upload costs money and adds review work he can't staff before beta, so the protection is the attestation plus an instant hide on report. This reverses 2026-09-30's "the uploader affirms nothing": the upload now asks. **Known-image hash matching stays planned** in `socialus-legal`'s NCMEC plan (step 2, the Cloudflare CSAM Scanning Tool; open item: put Cloudflare in front of image delivery). This ruling covers only the broader no-pictures-of-children policy. Once we are aware of apparent CSAM, through a report or a review, the reporting duty applies.

## Rulings
- **2026-10-06 — Pictures of children are currently handled on the uploader's word plus member reports: uploaders confirm a photo shows no children, nothing is pre-screened, and a report hides the photo at once (the existing sensitive-content report hides at any bar, `socialus-web` #284) pending operator review.** The PM, answering F080 (`socialus-web` #221). Because pre-screening every upload costs money and adds review work the PM can't staff before beta; the platform is protected by the attestation and instant hide-on-report. Known-image hash matching stays planned as in `socialus-legal`'s NCMEC plan (step 2, the Cloudflare CSAM Scanning Tool; open item: put Cloudflare in front of image delivery); this ruling covers only the broader no-pictures-of-children policy. The ask at posting not to post sensitive content stands. [replaces 2026-09-30: A picture of a child is caught by a message at posting and by reports. There is no attestation and no detection.] [binds tiers=planning,code surfaces=uploads,posting,reports,moderation,copy]
- **2026-10-01 — We can't enforce the sensitive-content rule; we rely on reporting. The ask at posting covers anything sensitive, in any form, and the children report category widens to "sensitive content", still hiding at any bar.** Don: *"We can't enforce this. We rely on reporting. A if we can."* Answers F080's question; `socialus-web` #221. [replaces none] [binds tiers=planning,code surfaces=posting,reports,moderation,copy]
- **2026-09-30 — While we grow into a platform with staff, we ask members not to post sensitive content: anything that would need a moderation team. Sensitive currently means children, animals and pets, and anyone who can't fend for themselves.** Don: *"while we grow into a platform with staff we are asking our users to support our mission by not posting anything sensitive that would require a moderation team. Sensitive items are generally anything related to children, animals/pets, or any other group that "cannot fend for themselves"."* **Why:** there is no moderation team yet, and we don't want to subject anyone on our team to unpleasant content (the reciprocity principle below). **Temporary:** it holds until there is staff to moderate, and lifting it is a new ruling. Widens F080 from pictures of children; the message at posting states it, and reports (F078) stay the backstop. The copy is a placeholder in `socialus-web`'s copy module ([public-is-draft]); the build task, #221, has a draft. Whether the report category and the photo-only scope widen too is open in F080. [replaces 2026-09-27: No pictures of children, full stop.] [replaces 2026-09-30: the app asks them, for safety reasons, to post no content with children.] [replaces F080: No pictures of children, from anyone] [binds tiers=planning,code surfaces=page-photos,posting,moderation,copy]
- **2026-09-27 — It is a photo rule, not a topic rule.** Don, defining the term the ruling below left open. **An image containing a child is not published by anyone; text about a children's activity is not caught** — a post about a kids' craft table publishes, a photo of the children at it does not. F080 rewritten around it; F078 criterion 8 hides a children flag at any bar. **The rule now needs a detection point and the repo has none**: nothing can see what is in a picture, and every Page photo uploads from the browser to a public bucket. **F082's step was checked as a home**: right place to *state* the rule, wrong place to *enforce* it — it runs once, misses stewards who never publish a Page of their own, and affirms locality and provenance. A one-line wording is proposed in F082 § Why, not adopted. [binds tiers=planning,code surfaces=page-photos,moderation] [replaces 2026-09-14: F080's scope confirmed]
- **2026-09-27 — Nothing unlocks F080. There is no stronger verification and none is being built.** Don's ruling on `socialus-web` #221. The content is not permitted at all; **allowing it later needs a new ruling, not a configuration change.** [binds tiers=planning,code surfaces=page-photos,verification] [replaces 2026-09-14: Nobody may post anything about a child, at any trust tier]
