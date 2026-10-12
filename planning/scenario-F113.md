---
id: F113
title: A member sees what SocialUs has learned about them, and changes it
status: draft
horizon: next
rank: 130
date: 2026-10-12
depends: [F109, F112]
---
## Story

A member has searched "trivia" twice and said "I'm coming" to three trivia nights. Home asks once: "Add trivia to your interests?" They tap Add, and Home's rows start carrying trivia nights. In You, "What SocialUs knows about you" lists their interests, follows, RSVPs, recent searches and what they have been shown; they delete one search. Later they turn off "Learn from what I do": suggestions stop, the Explore open log and the seen record stop, and the raw signals are gone.

## Acceptance

Not written. Brought to the PM first (options below); criteria follow the call. Fixed under every option:

- **One store, both sides.** What beta learns is what the fun side reads later; nothing is kept that the member cannot see once the store's page exists.
- **Every signal is listed to the member and deletable one at a time.** One switch stops all learning, including the F109 log and F112's seen record, and deletes raw signals.
- **Raw signals expire on their own** (searches, opens, RSVPs past their date: 90 days [guess]). No operator step.
- **Nothing changes what another member sees or what a Page owner sees about a member.** On the tool side, search relevance and place-and-time order do not change.
- **Builder accounts' signals count nowhere** (F114).

## Not this

The fun side's feed (after beta). Ads or anything sold. A score or label on a person. Telling another member what someone searched. Sharing signals outside SocialUs.

## Why

- **Lives somewhere better?** Partly: platforms show what they learned; few let the member decide what it may change.
- **Only locals know?** Yes: what a member looks for nearby is local.
- **Gets people together?** Yes: Home leads with gatherings the member actually goes to.
- **Stays fresh on its own?** Yes: signals expire on their own.
- **Who keeps it current?** The member.
- **Better as more people join?** Yes: more to suggest from.

**Path: new territory** (member trust, privacy). Research: `planning/research/explore-freshness-and-learning-2026-10-12.md` § 3. **Conflict, noted for the two-sides review:** suggestions from behaviour read it back at the member (F059, 2026-09-12).

**For the PM (A/B/C):**
- A) **One store the member can see, from beta** (recommended): every signal listed and deletable, one switch; beta uses it for not-seen-yet and suggestions the member accepts; the fun side reads it later with inferred interests and their reasons. Pinterest, Spotify, TikTok Refresh, Kay's scrutable models.
- B) **Collect from beta, show it when the fun side ships**: cheapest beta; members cannot see what is kept for months.
- C) **Collect only what beta uses**: seen and the F109 log, no search history; the fun side starts cold.

[open-question owner=don raised=2026-10-12] What does beta learn about a member: one store they can see and edit from day one (A), collect now and show later (B), or only what beta uses (C)? Recommend A.

[platform none]
