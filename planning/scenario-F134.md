---
id: F134
title: Visitors without an account can read everything; anything that writes asks them to sign in first
status: approved
horizon: next
rank: 5
date: 2026-11-12
approved: 2026-11-12, the PM picked A: "visitors can read everything; hearting, following, posting and reporting still need an account"
depends: [F059, F072]
concept: new
---
## Story

*The PM, earlier:* "remove the signed-out blockers". *Then, picking A on 2026-11-12, the option as put to him:* "visitors can read everything; hearting, following, posting and reporting still need an account."

A Sacramento visitor opens a friend's link to SacRiver Floaters and reads Thursday's post in full: what, when, and where, at the owner's chosen precision. They go back to Explore, open the map, and see the pins for what is on this week. They tap the heart on a post; before anything is saved, a sheet asks them to sign in, and after they do, the heart is there.

## Acceptance

1. **Signed out reads what a signed-in stranger reads.** For every Page and post, a signed-out visitor sees exactly what a signed-in member with no relation to that Page sees: the Page's location and tags, its public posts with body, time, place and photo, and the counts (hearts, how many are going). Checked by comparing the two responses for the same fixtures, field by field.
2. **Explore and the map are open.** Signed out, Explore lists Pages and posts the same way it does signed in (less the personal rows F059 keeps for members), and the Map pill opens the map with its pins, not sign-in.
3. **Places at their public precision.** A Page or post shows the exact place or the neighbourhood, whichever its owner chose; a signed-out map pin sits at that same precision and never closer.
4. **Every write asks first.** Heart, follow, get updates, RSVP, post, reply, message and report each open the sign-in sheet before anything is saved, and the tap completes after sign-in (deferred registration, 2026-09-18). A control that saves and then asks fails this.
5. **Enforced in SQL.** A request to the database's REST endpoint with the publishable key from the client bundle returns the public posts with body, `starts_at` and location, and is refused every insert, update and delete on every member table. Checked by calling the endpoint, not by reading the policy or the component.
6. **What stays private stays private, in SQL too.** The same anonymous request gets nothing that a signed-in stranger cannot read: no followers-only post, no contents of a community-only or private group Page beyond its front door and its public posts, no contact field the owner set to members, no member's legal name, zip, interests or follows, and no `members` row (`socialus-web` #178 stays a bug under any ruling).
7. **Member names stay between members.** Signed out, a member's display name and avatar do not show: a Page's founder, a Wonder's who-is-in list and a member's own post show without them ("a neighbour"), while the counts still show. Signed in, nothing changes.
8. **The withheld card is gone.** No "Sign in to see what's happening" card, no "the details are for members and followers of this Page", on Explore, Home, the today row or a Page; a link to `#announcement-<id>` lands on that post, readable.
9. **A signed-in member sees no change.** Same posts, same order, same places.
10. **Each check has been seen failing** against a fixture that should fail it ([guard-proves-itself]), including an anonymous write that must be refused and a followers-only body that must not come back.

## Not this

Hearting or saving without an account (option B, not picked). Reporting without an account (option C, not picked). Any change to who can see a member's name, contact details or a private group's contents. Rate limits on anonymous reads, which stay with `socialus-web` #195. A sitemap or structured data for search engines (a separate pick).

## Why

- **Lives somewhere better?** No: Yelp and Google show posts signed out; we hid ours (2026-10-15 pitch audit).
- **Only locals know?** Yes: what a local Page is doing this week.
- **Gets people together?** Yes: a stranger can see what is on and turn up, which a sign-in wall stopped.
- **Stays fresh on its own?** Yes: it reads the same posts members do.
- **Who keeps it current?** Page owners, as now.
- **Better as more people join?** Yes: every post now also reaches people who have not joined yet.

**What changes from 2026-09-23.** That ruling withheld what was happening and showed only that something was. It was gating, not privacy: a public post is one its owner made public. So it goes, with the rulings that built the withheld card, the no-pins map and the list-only signed-out Explore. **What protected members stays**, because it was never about signed-out reading: followers-only posts (2026-09-21), group Page levels (2026-09-15), the owner's choice of exact place or neighbourhood (2026-09-30), contact fields set to members (2026-10-07), and names shown between members only (2026-09-30). What a visitor may read and may not write is held in SQL, because the database answers anyone with the publishable key. F093 is retired with this scenario; its withheld card comes out of the code under criterion 8.

**Path: well-worn.** Airbnb, Luma and Google Business Profile keep browse and detail open signed out and ask for sign-in only when someone saves, follows or registers (`planning/research/design-references.md`). [platform key: what a visitor may read and may not write is enforced in SQL against anyone holding the publishable key, and a native client holds it too]

## Rulings

- **2026-11-12 — Visitors without an account can read everything a signed-in member with no relation to the Page can read, map pins included; hearting, following, posting, reporting and every other write still need an account and ask for sign-in first; both are enforced in SQL.** The PM, picking A, for F134. [replaces 2026-09-23: Who exists is public. What's happening is not] [replaces F093: The signed-out announcement card is one card per Page, and it shows the Page's photo.] [replaces F093: Signed-out visitors see no map pins.] [replaces F093: F093 criterion 8 amended: a signed-out visitor sees a Page's name, default photo, description and the withheld card, and no location, tags or founder.] [replaces F093: The signed-out main button reads "Sign in to see what's happening".] [replaces F091: Signed out, the "today" row shows one withheld card for each Page posting something today] [replaces F059: Signed-out Explore is list only, and the Map pill opens sign-in.] [replaces F072: a signed-out visitor still gets F093's withheld card] [replaces 2026-09-18: with announcements shown withheld (2026-09-23)] [replaces 2026-09-30: The levels apply to signed-in members.] [replaces 2026-09-30: A signed-out visitor gets a Page's front door] [binds tiers=planning,code surfaces=signed-out,explore,map,pages,announcements,rls]
- **2026-11-12 — Opening reading to visitors changes no member's privacy: followers-only posts, group Page levels, the owner's chosen location precision and contact fields set to members hold for a signed-out visitor as for a signed-in stranger, and a member's display name and avatar, shown between members, stay hidden from a signed-out visitor.** Decided by the agent under [member-data-disclosure], for F134; the PM's A was about reading, and these protect members, not content. [replaces none] [binds tiers=planning,code surfaces=signed-out,rls,names,contact,groups]
- **2026-11-12 — Later, visitors will have limited functionality: they can support Page owners as much as possible, while signing up brings a benefit visitors don't get. An intention, not a design; F134's build is unchanged.** The PM, verbatim: *"Visitors will have limited functionality somewhere down the road. The goal is to allow visitors to support the page owners in the app as much as possible while also providing an added benefit to patrons for having signed up that visitors don't receive. I don't know how this will work yet or what that means but that is the intention."* [for now] [replaces none] [binds tiers=planning surfaces=signed-out,signup build=none]

[open-question owner=don raised=2026-11-12] How do visitors support Page owners without an account, and what does signing up add that visitors don't get?
