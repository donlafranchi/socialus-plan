---
id: F065
title: Someone follows something
status: approved
horizon: next
rank: 140
date: 2026-09-10
depends: []
approved: 2026-09-07 — guard rails settled, unscheduled build
---
## Story

Rae wants to hear from a bakery, a repair collective, and the Saturday market — three different kinds of thing, one Follow button, one list. Following changes nothing else about her relationship to any of them: no membership, no role, no access she didn't already have, and nobody's roster shows her as staff.

## Acceptance

1. Following a person, Page, or venue writes one row with its event row in the same transaction.
2. A follow never grants membership, a role, or read access to anything unlisted — checked directly against every authorization/roster path.
3. A Member who follows a business and owns no shop still sees the Sell control offer to help them start something.
4. Unfollowing then re-following revives the original row rather than duplicating it.
5. The following list has one reader (the table layout is unchanged; see the 2026-10-11 ruling, #605).

## Not this

Public follower counts. Follow suggestions or mutual-follow surfaces. Notifying the subject that they were followed.

## Rulings
- **2026-10-11 — The following list keeps its three tables and has one reader (what `get-member-follows.ts` does today); no schema change. F065 criterion 5 now says so.** The PM, 2026-10-11, option B on `socialus-web` #605. [replaces none] [binds tiers=planning,code surfaces=follows] Issue: #605.
- **2026-09-17 — Support and get-updates are two different links between the same two things, and the difference is the inbox.** Don: *"Support is a like or a follow. I don't know if there's a difference yet. I just don't want to copy Airbnb exactly which is why the ribbon."* / *"There could be a get updates button. This should be in place of emails from vendors with offers etc."* / *"Where a support is perhaps a softer signal."* **Support (the ribbon)** is one tap, a soft public-ish backing of a Page — *I like that this exists*. **It produces nothing in anyone's inbox: no notification, no alert, no digest, no subscription.** **Get updates** is the actual subscription, and its stated purpose is to **replace promotional email from businesses** — updates arrive in the app, never in a mailbox. Named in words rather than by number because they are two link types, not two buttons: *a Member supporting a Page* and *a Member subscribed to a Page's updates*. Written up in `product/foundation/verbs.md` § Support and get-updates. [for now]
- **2026-09-17 — The design consequence that keeps support honest: support generates no notifications, and if it ever does, it has silently become a subscription.** This is what makes the ribbon compatible with the not-addicting constraint rather than a second pull-back loop wearing a softer word. It sits under the standing *no engagement optimization, anywhere* line and under `product/foundation/metrics.md`'s refusal of notification open-rate as a metric. **The test is one sentence: if tapping the ribbon can cause a member's phone to light up later, the ruling has been broken.** [for now]
- **2026-09-17 — Get-updates is a privacy posture, not only a feature: a Page owner reaches the people who subscribed without ever holding their contact details.** It answers the escape hatch `product/foundation/messaging-problem.md` names — an organizer publishing a contact address in a public announcement, *"scrapeable, not revocable"* — by giving a route that needs no address at all. **Checked against what is already ruled: it contradicts nothing and reinforces two things** — signup collecting *"nothing more without a stated reason"* (2026-09-14), and the refusal of pull-back notification loops. **One real tension found and NOT resolved here:** the 2026-09-08 line says a business *"may see its own audience"*, while F067's implementation writes followers with `source = 'soft_via_follow'` specifically so the list is unreadable **by anyone, the owner included**. *Reaching people without holding their email* and *reaching people without knowing who they are* are different promises. **Don has to say which one get-updates makes.**
