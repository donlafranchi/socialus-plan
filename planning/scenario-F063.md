---
id: F063
title: Someone says they're coming
status: approved
horizon: later
rank: 70
date: 2026-09-10
depends: []
approved: 2026-09-07
---
## Story

Rae finds a repair café three streets away on Saturday morning, but the page gives her nothing to press. She taps "I'm coming"; the count goes from 6 to 7. She changes her mind Thursday and taps again — it empties, no confirmation dialog. A friend who isn't signed in taps it, signs in, and lands back already marked as coming.

## Acceptance

1. Tapping the response control writes a response row and its event row in the same transaction; the count updates.
2. Tapping again withdraws the response with no confirmation dialog; a double-tap is a no-op enforced by a database constraint.
3. A signed-out tap survives the sign-in round trip and is recorded on return.
4. The count reflects distinct people, never rows.

## Not this

Notifications to the host. Capacity or waitlists. A list of who's coming shown to anyone outside the group — `product/foundation/policy.md` § Who sees who is involved.

## Rulings
- **2026-09-30 — Whoever is party to an RSVP currently sees it. For a gathering of many, they all do; for a one-on-one, only the two parties.** Don: *"Whoever is party to the rsvp sees it. If it's for a group of folks they all do. If it's for one on one then only the parties."* A Page's members who didn't RSVP are not party to it. Builds on `socialus-web` #246. [replaces 2026-09-30: Group members see who RSVP'd.] [replaces 2026-09-30: Who RSVP'd to a business Page's gathering is currently visible to its owners and to the others who RSVP'd.] [replaces 2026-09-13: Who sees who is involved: scoped by involvement, never forbidden outright.] [binds tiers=planning,code surfaces=rls,rsvp]
- **2026-09-12 — The response is a thumbs up or nothing; no declined state, no seen-and-undecided.** Replaces the same-day entry recording four states — those were Don painting the bigger picture, not a spec. The organizer sees two lists, who thumbed up and who didn't, which is presence or absence of a row rather than a state column. Names are in the list; the public sees the count. The avatar consequence is unchanged: `members.avatar_url` has no write path, and the list shows faces.
- **2026-09-12 — The response count is public.** Don: people want to know whether an event they are considering will be well attended, and more generally *"let them decide what they like and what's popular for them."* Withholding information from the public by instinct is the thing to resist.
- **2026-09-12 — Responses show names and small profile photos**, especially for meetups and group things. Supersedes the 2026-09-10 recommendation of count-only-no-names, and closes the open count-vs-names question from earlier the same day.
- **2026-09-12 — This answers, for responses only, the parked question of whether a Page owner sees who noticed.** Yes for an event response, which is a deliberate declaration a member makes. It does **not** automatically generalise: a page view (F068) is passive and a reaction on an announcement (F066, "a count and no identities, ever") is a lighter act. Both stay as they are until ruled on separately.
