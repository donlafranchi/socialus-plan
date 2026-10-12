---
id: F065
title: Someone follows something
status: approved
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
5. The following list has one reader (the table layout is unchanged; see DECISIONS 2026-10-11, #605).

## Not this

Public follower counts. Follow suggestions or mutual-follow surfaces. Notifying the subject that they were followed.
