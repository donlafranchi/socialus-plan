---
id: F113
title: A member sees what SocialUs thinks they like, and edits it
status: draft
horizon: considering
rank: 130
date: 2026-10-12
depends: [F109, F112]
---
## Story

A member has searched "trivia" twice, opened photos on three trivia-night posts and said "I'm coming" to one. In You, "What we think you like" shows Trivia, from 2 searches, 3 photo opens and 1 "I'm coming". They remove Bowling, which they only opened once for a friend, and it does not come back. Later they switch to "I don't mind doing this myself": learning stops and what was kept is deleted. Find looks the same throughout.

## Acceptance

1. **A profile the member sees, from beta**: in You, every interest SocialUs holds for the member, each with its reason in plain counts ("from 2 searches, 3 photo opens"), and beside it their follows, "I'm coming", saves, recent searches and what they have been shown (F112).
2. **Every item can be edited or deleted one at a time.** A removed interest is not inferred again unless the member adds it back. An interest the member adds is kept as theirs.
3. **The choice in the member's terms**: "Help me discover things I might like" (on, as the data ruling has it) or "I don't mind doing this myself" (off). Off stops all learning, the F109 open log and F112's seen record, and deletes raw signals; what the member declared and follows stays. Words to the PM.
4. **What it learns from**: searches; Page opens (F109); photo and video taps or opens, counted per Page and per category; follows; "I'm coming"; saves. Each is turned into interests through SocialUs's own categories (research note § 8), not member-typed hashtags.
5. **What it may change in beta**: which interests the profile shows, and F112's not-seen-yet. Find's place-and-time order and search relevance do not change. After beta, Discover and Home read the same profile.
6. **Raw signals expire after 90 days** [guess]; interests stay until removed or until no signal supports them for 90 days. No operator step.
7. **Nobody else sees it.** Member to member strict; staff under the 2026-10-09 ruling, with no tool that targets one member. Builder accounts' signals count nowhere (F114).

## Not this

Collecting data the member is not shown (device details, location; open below). Ads or anything sold. A score or label on a person. Telling another member what someone searched. Hashtags on cards.

## Why

- **Lives somewhere better?** Partly: platforms show what they learned; few let the member decide what it may change.
- **Only locals know?** Yes: what a member looks for nearby is local.
- **Gets people together?** Yes: what they like leads them to gatherings.
- **Stays fresh on its own?** Yes: signals expire on their own.
- **Who keeps it current?** The member.
- **Better as more people join?** Yes: more to learn from.

**Path: new territory, ruled.** Precedents: Pinterest's Refine your recommendations, Spotify's Exclude from your taste profile, TikTok's Refresh (research note § 3). **Conflict, noted for the two-sides review:** reads behaviour back at the member (F059, 2026-09-12).

[open-question owner=don raised=2026-10-12] Should SocialUs collect data it does not show the member, such as device details and location? The PM is considering it; nothing is built until ruled.

[platform none]

## Rulings
- **2026-10-12 — Learning about a member is option A: from beta, a member-visible profile of what we think they like, where they can edit or delete each item. The choice is framed in the member's terms, "Help me discover things I might like" or "I don't mind doing this myself" (the off switch). It is based on app usage, what they search for and click on, and our categorizing of it.** The PM, 2026-10-12, on #137. Because a member should see and control what is learned about them. [for now] [replaces none] [binds tiers=planning,code surfaces=you,privacy,explore,discovery build=none]
