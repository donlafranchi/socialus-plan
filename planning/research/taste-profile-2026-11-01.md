# Taste profile: one adaptive algorithm, built on a sliding interest scale

**As of 2026-11-01** · Source: hand-written · Maintained by: hand

## Bottom line for Don

**One idea runs everything a member is shown: for each member, how strong their interest in each thing is right now. It rises when they tap "This is cool", search or visit, fades over time, and follows the seasons. Discover, Home, the shelves, the weekly push and the order of search rows all read that one scale, so the app changes as the member changes.**

- **Your words, now in the ethos:** "We need to be fluid and evolve with our members however they evolve." This is proposed as a soul line [always], in its own small PR (#262).
- **What it replaces:** the profile checkboxes become "What you're into", a list with a strength per interest, optional months, and a short weekly chat that fills it in. That costs about a cent per member per month.
- **What it keeps:** Follow, renamed "Get updates", for the few Pages a member wants every post from. "This is cool" is the light tap that never subscribes.
- **What the member controls:** they see every strength and why it's there, drag it up or down, delete it, or turn learning off.
- **Your call:** A, B or C (at the bottom). I recommend **A**: two taps, the scale beside Follow, nothing already ruled breaks.

*The PM, 2026-11-01:* "So I want to review what the research surfaced but more importantly I want to capture this is a concept and use it for an algorithm that can be dynamic and adaptive. We need to be fluid and evolve with our members however they evolve. It needs to be part of our ethos and inform our choices." Earlier: "I want it to be something less committal than following and more akin to this is something I'm interested in where the strength of the interest is on a sliding scale that changes over time or between seasons." And: "I don't like the interest check boxes on the profile page … it's definitely not check boxes."

Research only. Nothing here is ruled except the soul line in #262, and nothing gets built until you pick.

## The algorithm: one scale, every surface

**Not a feature but one engine: signals come in, the scale holds a strength per thing with its season, the member sees and steers it, and every surface reads the same scale. Discover leans on it most. Find (search) uses it only to order rows and never hides a result.** That matches the two-sides principle (2026-10-12): Discover may serve what interests a member, and Find stays the member's own tool.

<details><summary>Details</summary>

```
 taps ("this is cool"), searches, opens, "I'm coming", saves
                │
 short chat (once a week) ──►  THE SCALE: per topic, Page or place
 member drags a strength   ──►  strength now · season · specifics
                │                          │
        You: "What you're into"     every surface below reads it
        (see, drag, delete, off)
```

| Surface | How it uses the scale | Limit that keeps it honest |
|---|---|---|
| **Discover / Home** | Picks which interest shelves appear ("Because you like wildflowers") and their order, by strength now × season | Get-updates Pages still come first (2026-10-30); a "what's new" shelf keeps unfamiliar Pages in view so the member isn't sealed into old tastes |
| **Shelves (F121)** | Up to three interest shelves per member are chosen from the scale, not from checkboxes; seasonal shelves appear only when in season for that member | The rotation and shelf counts stay as ruled; counts have no member id |
| **Weekly Thursday push** | Fills its interest slot with the in-season, high-strength topic | No new kind of notification; nothing is sent because a strength rose (§ 5) |
| **Search (Find)** | Orders the grouped rows (Live music: "Next 7 days", then the venue kinds you like most) and breaks ties among equally near, equally soon results | Never hides or drops a result; "Show as one list" stays plain. Going further than row order touches F113 criterion 5 (Find's order unchanged in beta), so it would come back to you |
| **You** | Shows every strength, its reason and its months, and lets the member edit them | The off switch stops all of it (F113) |
| **Page owners** | At most a count of "This is cool" taps on their Page | Never who tapped (F067 covers only Get updates) |

**Why it adapts:** guessed strengths fade by about half each month, so last spring's gardening doesn't crowd out this summer's concerts. Seasons bring interests back on time, and the member's own settings always win. This is the soul line in practice: the app follows the member, not the other way round.

</details>

## 1. The model: how interested is this person in X, right now

**Each member gets a strength per topic, Page or place. Taps, searches and visits push it up, and it fades by about half each month with no new signal. What the member says outranks what we guess, and a topic can carry its months, so gardening rises in March and drops in July without anyone touching it.** This is the standard short-term plus long-term shape the big apps use; the new part for us is that the member can see and drag every number.

<details><summary>Details</summary>

**What other apps do**

| App | What it holds | Can the member see or steer it? | What we take |
|---|---|---|---|
| [TikTok Manage Topics](https://techcrunch.com/2024/08/30/tiktoks-new-manage-topics-tool-gives-you-more-control-over-your-for-you-feed-heres-how-to-use-it) | A "see more / see less" slider per broad topic (about a dozen), starting in the middle | Yes, sliders. They never remove a topic, and they [don't touch the Following feed](https://www.engadget.com/social-media/tiktok-is-making-it-easier-to-control-what-is-and-isnt-in-your-for-you-feed-175301931.html) | **The closest precedent.** A strength slider kept apart from follows |
| [Instagram Your Algorithm](https://techcrunch.com/2025/12/10/instagrams-new-your-algorithm-tool-gives-you-more-control-over-the-reels-you-see) (Dec 2025) | An AI-written summary of the topics it thinks you like | Yes. Remove topics, type in your own, watch the feed change | A written summary the member edits, which is what the chat produces |
| [Spotify taste profile](https://support.spotify.com/us/article/exclude-from-your-taste-profile/) | Listening history weighted toward recent plays | Partly: "Exclude from your taste profile" per playlist | Recent counts for more; let a member exclude things |
| Netflix (thumbs, then [two thumbs up](https://about.netflix.com/en/news/two-thumbs-up-a-new-way-to-rate-on-netflix) in 2022) | Ratings plus viewing, with a light "love this" tier | Ratings only | Three steps (no, yes, love) beat five stars; people actually tap them |
| Pinterest ([Refine your recommendations](https://help.pinterest.com/en/article/tune-your-home-feed); [PinnerSage](https://arxiv.org/abs/2007.03634)) | Several separate interest clusters per person, with recent ones weighted up | Yes: "See more / fewer like this" per Pin, and turn off recommendations from what you looked at | A person holds many interests at once, each with its own strength |
| Pinterest Predicts / seasonal planning | People search for a season 1–3 months ahead | No | Seasonal interest starts **before** the season, so the lead time matters |
| Google Discover | Followed topics plus "More / Less stories like this" on each card | Yes, per card and per topic | A light per-card nudge, separate from following |
| Apple Music | "Love" and "Suggest less" | Per item | Two gentle taps, no subscription |

**The shape for SocialUs**

- **Things that carry a strength:** our 12 interest labels (Farmers markets, Live music, Gardening and so on), the finer tags under them (wildflowers, outdoor concerts, cover bands), single Pages, and places (a park, a neighborhood).
- **Strength now** is the member's own setting if they set one. Otherwise it's the recent signals, each weighted and faded by about half every 30 days [guess, tune in beta]. Suggested weights: "this is cool" or "I'm coming" 3, save 2, search 1, open ½ [guess].
- **Season:** a topic can carry months, either from the member ("only spring") or learned from last year's pattern ("you tapped gardening every March"). Outside its months a topic drops to near zero. It rises about four weeks before, matching the Pinterest lead time.
- **What the member says vs. what we guess:** a declared strength never fades and is never overwritten. A guessed one fades on its own. A removed topic is never guessed back (F113 criterion 2).
- **What the member sees:** five steps, not a number: *Not now · A little · Some · A lot*, plus the months. That's the explicit half. The implicit half shows as the reason ("from 3 taps and 2 searches"), as F113 already describes.

</details>

## 2. "This is cool" instead of Follow

**Add a one-tap "This is cool" on cards and Pages that raises the strength of that Page and its topics and never subscribes. Keep Follow, renamed "Get updates", for the few Pages a member wants every post from.** That's the split you already ruled on 2026-09-17 (support vs. get-updates), so "This is cool" is the unbuilt support ribbon, now with a job. Removing Follow outright would break five live features that need a list of "everyone who asked for this Page's posts".

<details><summary>Details</summary>

**What already exists:** the 2026-09-17 ruling gives two links between a member and a Page: **Support** ("I like that this exists", soft, never in the inbox, unbuilt) and **Get updates** ("tell me what this Page posts", which is today's Follow). "This is cool" is Support with a clearer name and a purpose. One conflict to settle: that ruling says support produces no notifications **ever**. Option A keeps that, since "This is cool" never sends anything on its own and only changes what the existing weekly push picks (§ 5).

**Everything that depends on Follow today, and what each becomes**

| Depends on Follow | Under A (keep both, rename) | Under B (Follow removed) |
|---|---|---|
| Push: "new posts from Pages you follow" (2026-10-25) | Unchanged, now "Get updates" | Gone; only the weekly push remains |
| Weekly Thursday push, "from followed Pages plus interests and area" | Reads Get-updates Pages **and** the scale's strength, with seasons | Reads the scale only |
| Followed first in every view, and F121's followed shelf (2026-10-30) | Get-updates Pages stay first; a "Because you like…" shelf reads the scale | The followed shelf becomes "Your favourites", the Pages scoring highest on the scale. Less predictable for the member |
| Signed-in Explore shows followed Pages' announcements (F059 2b) | Unchanged | Shows high-scoring Pages instead |
| Followers-only announcements (F072, the public/followers switch) | Unchanged | **Breaks**: no defined audience. Needs a new ruling |
| Page owner sees who follows, by name (F067) | Owner sees Get-updates names only; "This is cool" stays anonymous, shown at most as a count to the owner | Owner sees no one, which reverses F067 |
| Follower vs. member; private Pages have members only (F067) | Unchanged | Unchanged (membership doesn't depend on Follow) |
| A follow never grants access; no public follower counts (F065) | Unchanged. No public counts for "This is cool" either | Unchanged |
| F113 learns from follows; the off switch keeps follows | "This is cool" and Get updates are both declared, so both survive the off switch | Same, minus follows |
| F121 shelf "saves" count a thumbs up, calendar add or follow | Add "This is cool" to the saves count | Same |
| Member journey step 10, "Follow what you love"; use case P6, an artist who wants to be followed | Becomes "tap This is cool, or Get updates for every post" | Rewritten around the scale |

Follower counts: none are public today (F065 rules them out), so nothing changes there.

</details>

## 3. Taste profile instead of checkboxes

**Replace the 12 checkboxes with "What you're into": a list of topics, each with a strength and optional months, that a 3-question chat with a small model (Claude Haiku 5.5) can fill in about once a week. It costs about a cent per member per month at today's prices, even if every member chats weekly. The member can always read, drag, add and delete by hand for free, and the off switch stops all of it.** Specific where the member is specific ("bluegrass at small bars, not arenas"), broad where they're not ("music, sure").

<details><summary>Details</summary>

**Today:** 12 fixed labels, on or off, with no strength, no season and no detail. Only the member sees them, and they power the "My interests" filter.

**The chat**

- **Three questions, then a summary:** "What do you like doing around town?", "Anything specific: kinds, places, times of year?", and "Anything you'd like less of, or only sometimes?" It asks one follow-up when an answer is vague, then shows the profile it wrote. Nothing saves until the member taps Save.
- **What it writes:** a list of items, each with a topic from our labels, finer tags when the member was specific, a strength step, months if any, and the member's own words as the note ("cover bands, not big names").
- **Mapping:** every item lands on one of our 12 labels and our existing tags, so categories stay ours (the 2026-10-12 ruling: members never type hashtags). Words we have no tag for go to the search dictionary as candidates, with no member attached, the way search demand works today.
- **How often:** one chat a week; editing by hand is unlimited. A first chat is offered at signup, in place of the checkboxes.
- **Guardrails:** it only talks about local interests and declines anything else. It never asks about or infers health, politics, religion, sexuality or money. A short, fixed prompt and a cap on reply length bound the cost. Builder and test accounts never count (F114). The privacy page says plainly that an AI helper reads the chat.

**Cost at current prices** (Claude Haiku 5.5, launched 2026-10-07: [$0.10 per million tokens in, $0.50 out](https://latenode.com/news/anthropic-launches-claude-haiku-5-5-with-tiered-pricing) for prompts under 100k tokens, which ours always are)

| | Tokens | Cost |
|---|---|---|
| One chat: about 4 turns, our label list and the member's current profile resent each turn | ~10,000 in, ~1,500 out | about **$0.002** |
| Allow 30% for the new tokenizer ([reported](https://letsdatascience.com/blog/claude-haiku-5-5-cut-prices-90-prompts-over-100k-pay-5x)) | | about $0.0025 |
| One member chatting every week | ~4.3 chats | about **$0.01 a month** |
| 1,000 members, every one weekly (the ceiling) | | about $11 a month |
| 10,000 members, every one weekly | | about $110 a month |

Even at 5× these token counts it stays under $0.06 per member per month. The weekly limit is about keeping the profile settled, not about cost.

**Member control (F113 option A):** in You, "What you're into" lists every item with its strength step, months, note, and why we think so ("from 3 taps, 2 searches"). Drag a strength up or down, set months, delete an item, add one by hand. "I don't mind doing this myself" turns off learning and the chat, deletes raw signals, and keeps only what the member declared, as already ruled.

</details>

## 4. Watching search and taps

**We already collect most of what the scale needs, but nearly all of it is stored with no member attached, because it was built for counts. The scale needs a private, per-member, expiring record of taps, searches and opens, which F113 already allows under the data ruling (option C, tightened 2026-10-25).**

<details><summary>Details</summary>

| Signal | Collected today? | Tied to a member? | Needed for the scale |
|---|---|---|---|
| Searches (search demand) | Yes | **No**, by design; off with the logging switch | A private per-member copy, expiring at 90 days |
| Shelf views, taps and saves (F121) | Yes, weekly counts | **No**; raw rows deleted at 30 days | The same tap, per member, private |
| Page opens (F109) | Not built | — | Yes |
| Photo and video opens | Not built | — | Yes (F113 lists them) |
| Follow / Get updates | Yes | Yes | Yes |
| Interest checkboxes | Yes | Yes, readable by the member only | Become declared strengths |
| "This is cool" | Not built | — | Yes, the main explicit signal |
| "I'm coming", saves, "Count me in" | Partly | Yes | Yes |

**The privacy rules already in force, applied here:**
- Raw signals expire after 90 days [guess, F113]; only the strengths remain.
- One switch stops learning and deletes raw signals.
- Members opt out; they never have to opt in.
- Nothing is sold, and no one else profits.
- No other member ever sees it.
- Staff have no tool that targets one member.
- The weekly counts stay member-free.

</details>

## 5. "Alert me when the time is right"

**No new kind of notification. The weekly Thursday "this weekend near you" push already mixes in interests, so the scale decides what goes in it: a topic in season and high on the scale gets the slot ("Wildflower walks start this weekend"). Nothing is sent because a strength rose, and nothing is sent to someone who has been away.** This keeps "This is cool" inside the "support never notifies" rule, because it shapes a message the member already gets and never triggers one.

<details><summary>Details</summary>

- **Timing:** a seasonal topic enters the weekly push from about four weeks before its months begin, so planting talk arrives before planting.
- **No nagging:**
  - At most one item per topic per week.
  - A topic the member skipped three weeks running drops a step and says so in You, so the member can put it back.
  - Quiet hours and pause-all stay as ruled.
- **Within the 2026-10-25 ruling:** both kinds are unchanged; every push still lands on a view with one tap to turn that kind off; only weekly counts are kept, never used as a target.
- **Later, needs its own ruling:** an "in season" push separate from Thursday, for something like "the farm stand you like opened today". It's new territory because it would be a third kind.

</details>

## 6. Options

**A keeps what's built, adds the scale beside it, and is the smallest path. B is the purest version of your idea but breaks followers-only posts and owner audiences. C is only a better checkbox.** I recommend **A**.

<details><summary>Details</summary>

| | **A. Two taps, scale beside Follow** (recommended) | **B. The scale replaces Follow** | **C. Better checkboxes only** |
|---|---|---|---|
| What the member sees | "This is cool" on everything, "Get updates" on Pages, "What you're into" in You | "This is cool" only; strong interests get more | Today's Follow plus strength steps on the 12 labels |
| Matches "less committal than following" | Yes | Yes, fully | Partly |
| Breaks rulings | None. It uses the 2026-09-17 support/get-updates split | F072's followers-only switch and F067's owner list; needs new rulings for both | None |
| Precedent | TikTok Manage Topics (sliders kept apart from Following) | None of the big apps dropped following | Old-style onboarding pickers |
| Path | Well-worn | New territory | Well-worn |

**Smallest first version under A:**
1. Turn the checkboxes into "What you're into": the 12 labels with *Not now · A little · Some · A lot* and optional months. Existing ticks become "Some".
2. Add "This is cool" on cards and Pages. It raises that Page and its topics and is shown only to the member.
3. Feed the scale into the existing "Because you like…" shelf (F121) and the Thursday push.

**Next:** the 3-question chat, finer tags under each label, and learned seasons once there's a year of data. Renaming Follow to "Get updates" is copy, so it comes to you with the words.

</details>
