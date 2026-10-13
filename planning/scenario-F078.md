---
id: F078
title: Flagged content hides itself immediately, and the poster is told why
status: approved
horizon: now
rank: 60
gates: launch
date: 2026-09-14
depends: [F058, F077]
approved: 2026-09-14 — Don's ruling
amended: 2026-10-13 — courtesy notice first (PM ruling 2026-10-11, web #626): criteria 2, 3, 6, 7 and 8 restated, 12 added; the story and Why follow. Code is built to it. Earlier, 2026-09-30 — Don: everything a member posts is reportable; "threat of harm" is a seventh category that hides at any bar; the bar rises when his daily review passes 30 minutes; the reporter picks a reason the poster sees and can rebut, and is told misuse costs a strike (after three, their reports stop auto-hiding). Criteria 1, 3, 5 and 8 restated, 9–11 added. (2026-09-27: the hide bar is per-metro data starting at zero.)
---
## Story

A photo gets reported. The reporter picks a reason, and is told kindly that reports are for keeping everyone safe and that misusing them has consequences. An agent reads the report and the content and tags a category and a confidence score. The first report does not hide the post: its owner gets a courtesy notice, in plain words, with the reason the reporter gave, and a chance to fix it themselves. A second report, from a different member, hides it and sends it to a person on our team. A Threat of harm or Sensitive content report hides at once. A hidden post's owner is told why within seconds, and if they think it's wrong they write back explaining themselves.

## Acceptance

1. **Anything a member can post is reportable: photos, Pages, announcements and posts.** A submitted report triggers agent classification: category (harassment, nudity, spam, violence, children, threat of harm, other) and a confidence/severity score.
2. **A first report leaves the post up and sends its owner a courtesy notice; a second report from a different member hides it and sends it to a person on our team.** Hiding is the mechanism F058's Remove-photo control uses. Threat of harm and Sensitive content are the exceptions (criterion 8). *(Amended 2026-10-13: this read "hides when its score is at or above its metro's hide bar"; no score drives hiding at launch.)*
3. The poster is notified immediately, in-app (never email), with the specific category, **the reason the reporter chose**, and a plain-language explanation: a courtesy notice after the first report (the post is still up), a takedown notice when it hides.
4. The poster can submit one explanation, rebutting the reason; submitting is the only thing that creates work for a person — an unanswered takedown stays hidden and closes itself.
5. Threat-of-harm or children-category flags text Don's phone (SMS) immediately regardless of confidence; everything else queues in a mobile review view for whenever he's free.
6. Every report lands in the same queue for an unhurried look, whether or not it hid anything. A first report is a notice, not a takedown.
7. **The hide bar stays per-metro data without a migration or a deploy**, the way F076 criterion 11 makes the waitlist thresholds, for when the agent's score is allowed to drive hiding. **That is not built at launch (web #626, PM option A): the bar sits at zero and the AI stays in shadow, and agent-scored hiding is built before any metro's bar is raised.** Content whose metro cannot be resolved uses zero.
8. **A Threat of harm or Sensitive content report (children, animals, anyone who cannot speak up) hides at once, on the first report and regardless of the bar.** Pictures of children are not permitted (F080), and a threat of harm cannot wait on a second report. Child content does not go back to the poster (2026-10-07; CyberTipline duty, web #648).
9. **A report cannot be sent without a reason the reporter chose.**
10. **Before sending, the reporter is told that misusing reports has consequences: each report Don rejects is a strike, and after three, that person's reports stop hiding anything and go to his queue.**
11. **Every string in the report path, to reporter and poster alike, is kind and gracious** — Don: *"help us all be good to one another."* Wording is Don's ([public-is-draft]).
12. **The second report that hides an item must come from a different member than the first.** One member filing twice cannot hide a post.

## Not this

A public-facing appeals board or an SLA promise. Building the classification logic itself (Code's implementation detail). Bulk actions on the queue (F079). Per-category bars — one number per metro until volume shows one is not enough. Raising the bar automatically from volume or time: it moves when Don moves it.

## Why

### Courtesy notice first (2026-10-11)

**With one operator, the first step is the poster correcting it, before staff work is needed.** So a first report only notifies; a second report from a different member hides. The metro bar stays as data for the day an agent's score is allowed to hide things, and it is built before any bar is raised.

### When the bar rises (2026-09-30)

**When Don's daily review runs past 30 minutes**, he raises that metro's bar. His time is the signal, not a queue size or a count, because his time is what a buried queue costs.

### Threat of harm (2026-09-30)

Don delegated what a credible threat is to Cowork. **A seventh category, not a score threshold inside one**, so the text to Don doesn't wait on a confidence number, and the reporter can name it directly.

### Misuse (2026-09-30)

**We don't currently share a misusing reporter's identity with the person they reported** (Don, 2026-09-30): it would make the platform a party to a dispute between members. Three strikes is the consequence. Revisit later.

**Unresolvable metro uses zero** so the fallback leans toward hiding, never toward leaving something up.

## Rulings
- **2026-10-11 — The second report that hides an item must come from a different member than the first.** Dispatch, shipped in `socialus-web` #706, on top of the courtesy-notice-first ruling above. Because one member filing twice cannot hide a post. [replaces none] [binds tiers=planning,code surfaces=reports,moderation] Issue: #706.
- **2026-10-11 — The report-path copy takes these edits: no numbers in the misuse warning (it says graciously that misusing reports has its own consequences), and "a person from our team", not "a real person". Final approval comes after Don reviews a screenshot storyboard of every report-path screen in context, before going public.** The PM, 2026-10-11, via Dispatch, on `socialus-web` #627 (F078 criterion 11). [replaces none] [binds tiers=planning,code surfaces=reports,copy] Issue: #627.
- **2026-10-11 — A first report gives the owner a courtesy notice and a chance to fix the post themselves, and the post stays up; a second report on the same item hides it and sends it to a person on our team. Threat of harm and Sensitive content (children, animals, anyone who cannot speak up) hide at once, and child content does not go back to the poster (2026-10-07; CyberTipline duty, #648).** The PM, 2026-10-11, on `socialus-web` #626. Because with one operator the first step is the poster correcting it, before staff work is needed (see the standing rule below). [replaces 2026-09-27: starts at zero — every report hides —] [binds tiers=planning,code surfaces=reports,moderation,copy] Issue: #626.
- **2026-09-30 — Misusing reports: three strikes.** Don took the recommendation on F078. Each report Don rejects is a strike; after three, that person's reports stop auto-hiding and go to his queue. The reporter warning (F078 criterion 10) says so. **We don't currently share a misusing reporter's identity with the person they reported,** because that would make the platform a party to a dispute between members. Revisit later. [binds tiers=planning,code surfaces=reports,moderation]
- **2026-09-30 — Anything a member can post that could cause offence is reportable at launch: photos, Pages, announcements and posts.** Don, on #220. F078 widens the report path beyond Page photos. F078 criterion 1 restated. [binds tiers=planning,code surfaces=reports,moderation]
- **2026-09-30 — "Threat of harm" is a seventh report category. It hides the content at once, whatever the metro's bar, and texts Don.** Don delegated what a credible threat is to Cowork (#220); this is Cowork's choice under that delegation. **A category, not a score threshold inside another one,** so the route doesn't wait on a confidence number. It joins children as the second category that hides at any bar. F078 criteria 1, 5 and 8 restated. [binds tiers=planning,code surfaces=reports,moderation]
- **2026-09-30 — Don raises a metro's hide bar when his daily review runs past 30 minutes.** Don, on #220. The trigger is his time, not a count, and nothing raises the bar automatically. **The same ruling adds scope to #220** (flagged, not cut; cuts are decided 2026-10-15): the reporter must choose a reason; the reason is sent to the person whose content was reported, and they can rebut it; the reporter is told that misusing reports has consequences; the tone throughout is kind and gracious, *"help us all be good to one another."* The consequence is the strike rule below. F078 criteria 9–11 added. [binds tiers=planning,code surfaces=reports,moderation,copy]
- **2026-09-27 — The F078 hide bar is not a fixed number. It is per-metro configuration that tightens as volume grows, without a code change.** Don's ruling on `socialus-web` #220, rejecting a fixed confidence threshold *on the grounds that the right one depends on volume: very few users at launch, more later.* One constant cannot be right at both ends, so the bar is a value on the metro, **changed as data, the way F076 criterion 11 already makes the waitlist thresholds** (`metro_polygons.creator_threshold` / `patron_threshold`) — checked, not assumed. Per metro because metros open at different times with different volume. **Two floors on it:** content whose metro cannot be resolved uses zero, and a children-category flag hides at any bar, because F080 makes that content unpublishable. One number per metro, not per category, until volume shows one is not enough. F078 criteria 2 and 6 restated, 7 and 8 added. [binds tiers=planning,code surfaces=reports,moderation]
- **2026-09-14 — Correction: reaching Don by email being deprioritized is a guideline, not an absolute, and belongs in `CLAUDE.md` § How to talk to Don, not a scenario or a hard "never."** Supersedes the same-day line's "Don is never emailed by the platform... no email destination will ever be named" — that overstated it against RULES.md's own six-absolutes test (no dated harm behind an email ban). Correct framing: email is not the best route to reach him; in-app is better; faster channels are TBD. F078 still builds SMS + a mobile queue because that's the better design, not because email is forbidden. [for now]
- **2026-09-14 — Content gets hidden the moment the agent flags it, before any human looks — not held for a person's decision first.** The poster is told immediately and specifically why; getting it restored is their burden, not the platform's — they explain themselves, and only a filed explanation reaches a person. Silence costs nobody staff time. Reverses the same-day F078 line's original shape ("the agent drafts a recommendation; it never removes or hides anything itself") — the agent's flag is the action now; a person is the exception path, not the default one. [for now]
