# Taste profile, "this is cool", and the right time

**Your three ideas fit together. A short chat writes a taste profile the member can read and edit. A light "this is cool" tap tells us what they like without subscribing them to anything. Season and timing live on the profile, so the weekly Thursday note brings it up when it's in season. Most of this is already ruled in principle. The new parts are the chat and the seasons.**

**Your calls (three, one per idea, each A/B/C below):** **taste profile A** (a 3-question chat, once a week, editable list), **cool A** (build the ruled soft "support" tap as "This is cool" and rename Follow to "Get updates"), **timing A** (in-season interests ride in the existing Thursday note, no new notification).

Research only: no rulings and no code. Path: new territory. It touches member data, notifications and Follow, which everything else leans on.

## The picture

Three things the member does, one profile, two outputs:

- **Tell us:** a short chat ("what are you into lately?") → the taste profile.
- **Show us:** searches, opens and "this is cool" taps → the profile, as suggestions the member can keep or remove.
- **Profile:** a short list in plain words. Broad where they're broad ("live music"), specific where they're specific ("bluegrass, outdoors"), each with an optional season ("spring") or time ("weekend mornings").
- **Out to Home and shelves:** what's shown first, now.
- **Out to the Thursday note:** "it's that time again: wildflower walks this weekend", only when the season matches.

Follow stays only where someone truly wants every post (the bakery's sourdough day), under a clearer name.

## 1. Watching search and taps

**Today we log searches anonymously by area (no member attached), count shelf views and taps in aggregate, and store the member's checkbox interests. We can't yet learn from one member's own searches and taps: the member-level log, the "what we think you like" view and the single off switch are ruled but not built.**

<details><summary>What we capture today</summary>

| Signal | Stored | Tied to the member? |
|---|---|---|
| Explore searches | Query text, area, result count | **No.** Anonymous on purpose (search demand, for Page owners and staff). A member can turn it off on You |
| Shelf views, taps, saves | Per shelf per day (the shelves scenario) | No. Hashed, aggregate |
| Map mix | Which bucket each pin came from, per day | No |
| Checkbox interests | 12 broad labels (Farmers markets, Live music, Gardening…) | Yes, owner-only |
| Follows, "I'm coming", saved searches | Rows per member | Yes |
| Page opens from Explore | Ruled (member id, staff-side, opt-out), **not found in the code** | Would be |
| "Seen" record per Page | Ruled draft (F112), not built | Would be |

</details>

<details><summary>What's missing to learn from searches and taps</summary>

- **A member-level signal log:** searches, Page and photo opens, cool taps, each with the member and a date, expiring after 90 days. Today's search log has no member on purpose, and that stays; this would be a second, private record.
- **Turning signals into interests** through our own labels and tags (ruled: SocialUs categorises, members never type hashtags).
- **The profile view on You** (F113 option A), each interest with its reason in plain counts ("from 2 searches, 1 cool").
- **Season memory.** Raw signals expire at 90 days, so we can't learn "every spring" from raw history. The season has to sit on the interest itself ("wildflowers · spring"), either said in the chat or added after two springs of taps. That keeps the 90-day rule intact.

</details>

<details><summary>Privacy rules it must keep</summary>

- **One switch, in the member's words:** "Help me discover things I might like" (on) or "I don't mind doing this myself" (off). Off stops all learning and deletes raw signals; what the member said themselves stays. Today the only switch is search sharing, so the single switch has to be built.
- **Raw signals expire after 90 days;** interests fade after 90 days with no support unless the member added them.
- **Nobody else sees it.** Not other members, not Page owners; staff only under the existing ruling, with no tool aimed at one member.
- **Never sold, never used for anyone's profit but members'.** The chat's words count as member data under the same rules (AI principle: exportable, deletable).

</details>

## 2. Taste profile instead of checkboxes

**The best apps mix three inputs: a few picks or words up front, quiet learning from what you do, and a page where you can see and correct it all. A 3-question Haiku chat, about once a week, can write a structured profile for about a cent per active member per month. It needs guardrails: our labels only, nothing sensitive, editable afterwards.**

<details><summary>How others build taste</summary>

| App | Up front | Learned | Member can see and edit |
|---|---|---|---|
| [Spotify](https://www.spotify.com) | Pick a few artists | Listening | "Exclude from taste profile"; [Prompted Playlists](https://techcrunch.com/2026/01/22/spotify-brings-ai-powered-prompted-playlists-to-the-u-s-and-canada/) take plain-language requests over your history |
| [Netflix](https://www.netflix.com) | Pick 3 titles | Viewing, thumbs | Rate, remove from history |
| [Pinterest](https://www.pinterest.com) | Pick topics | Saves, clicks | "Refine your recommendations" lists topics to switch off |
| [TikTok](https://www.tiktok.com) | Optional topics | Almost all implicit | [Manage topics](https://techcrunch.com/2024/08/30/tiktoks-new-manage-topics-tool-gives-you-more-control-over-your-for-you-feed-heres-how-to-use-it) sliders, more/less per topic; "Refresh" to start over |
| [Instagram](https://www.instagram.com) | None | Likes, watches | ["Your algorithm"](https://hypebeast.com/2025/12/instagram-launches-your-algorithm-controls-for-reels) (Dec 2025): an AI-written summary of your topics you can edit and add to |
| [Letterboxd](https://letterboxd.com) | None | Logs, likes, ratings | Watchlist and lists are fully yours |
| [Yelp](https://www.yelp.com) | Preferences (diet, cuisines) | Searches, visits | Edit preferences |
| [Google Discover](https://support.google.com/websearch/answer/2819496) | None | Search, activity | "More/less like this", follow a topic, "Don't show from" |
| [Apple Music](https://www.apple.com/apple-music/) | Tap genre bubbles | Plays, Love | "Suggest less like this" |

**Pattern:** checkboxes are the weakest version, used only at sign-up. The direction since 2025 is Instagram's: an AI-written, plain-language summary the member edits. That's your idea, with a chat in front.

</details>

<details><summary>The chat, about 3 questions</summary>

**Shape:** Haiku asks, the member answers in their own words, and Haiku writes a profile (structured, not free text) at the end. Three turns by default; it stops early if the answers are clear.

1. "What do you like doing around here, or wish you did more?" (open)
2. A follow-up on the most specific thing said: "Bluegrass: just shows, or jams you can join too?" Or on timing: "Is that a summer thing for you?"
3. "Anything you're done with, or don't want to see?" (exclusions are as useful as likes)

Then it shows the result as a short list and the member keeps, edits or removes each line before anything saves.

**What it writes, one line per interest:**
- **What:** one of our labels (broad) and optionally a narrower tag ("Live music → bluegrass"). Only words from our list; a new word becomes a suggestion for staff, not a new tag.
- **How specific:** broad or narrow, as the member put it.
- **When:** optional season (spring, summer…), months, or time of week ("weekend mornings").
- **Where:** optional ("near home", "when I'm in Tahoe").
- **Not for me:** exclusions.
- **Source:** "you said", kept apart from "we noticed".

**How often:** once a week by default (your idea), plus a free edit any time on the plain list, which costs nothing. "Add one thing" can be a one-question chat.

</details>

<details><summary>Cost at Haiku prices</summary>

Claude Haiku 5.5: **$0.10 per million tokens in, $0.50 per million out** (Anthropic's price list, as cached 2026-10-06).

One session, three questions plus the final write-up, resending the conversation each turn: about 16,000 tokens in (instructions, our label list, the current profile, the chat) and about 3,000 out (replies, thinking, the profile). **About $0.003 per session.**

| Use | Per member per month | 1,000 members | 10,000 members |
|---|---|---|---|
| Weekly, every member (worst case) | ~$0.013 | ~$13 | ~$130 |
| 1 in 5 members, weekly | ~$0.003 | ~$3 | ~$26 |

Caching the fixed instructions cuts the input part further. The weekly limit matters less for cost than for keeping it a ritual instead of a chatbot; even unlimited use would be cents.

</details>

<details><summary>Guardrails</summary>

- **Our words only:** output is checked against our labels and tags; anything else is dropped or offered to staff as a suggestion.
- **Nothing sensitive is stored:** health, religion, politics, sexuality, kids' names, addresses. If a member says it, the profile keeps only the activity ("faith community events" only if they ask for that label).
- **The member confirms** the list before it saves; nothing is written silently.
- **No selling, no persuasion:** the chat never suggests a Page or business; it only asks about the member.
- **Limits:** a set number of turns, a short reply length, the weekly cap, and a staff-side spend cap.
- **Off switch honoured:** with "I don't mind doing this myself" on, the chat is still offered (it's the member telling us), but no learning is added on top.
- **Words to you:** every question and label the member reads is draft copy for you.

</details>

<details><summary>How it maps to what we have</summary>

- The 12 broad labels stay as the top level; the chat adds narrower tags under them from our tag list (Pages and posts already carry tags).
- Seasons and times are new fields on an interest; nothing else in the data changes shape.
- The checkboxes on You become the plain, editable list the chat writes to. The same list is F113's "what we think you like", with "you said" and "we noticed" kept apart.
- Explore's "My interests" filter reads the same list, now with narrower tags.

</details>

## 3. "This is cool" instead of Follow

**You already ruled this distinction on 2026-09-17: "support" is a soft like with no inbox, "get updates" is the subscription. Support was never built. "This is cool" is that tap, under a better name. Recommended: keep both, build Cool, rename Follow to "Get updates", and Cool never notifies by itself.**

<details><summary>Precedents</summary>

| App | Light tap | Heavy tap |
|---|---|---|
| [Pinterest](https://www.pinterest.com) | Save a Pin: shapes your feed, no notifications | Follow a board or person |
| [Instagram](https://www.instagram.com) | Like: shapes recommendations | Follow: their posts in your feed |
| [Spotify](https://www.spotify.com) | Like a song | Follow an artist (release alerts) |
| [Google Discover](https://support.google.com/websearch/answer/2819496) | More/less like this | Follow a topic |
| [Letterboxd](https://letterboxd.com) / [Goodreads](https://www.goodreads.com) | Watchlist / Want to read: "I'd like this some day" | Follow a member |
| [YouTube](https://www.youtube.com) | Like; Subscribe without the bell | Subscribe with the bell (all notifications) |

**Pattern:** every big app has both, and the light tap is used far more than the heavy one. YouTube's "subscribe without the bell" is the closest to your "I want to know some things, not everything".

</details>

<details><summary>What Cool does and doesn't do</summary>

- **One tap** on a card or Page, undone with another tap. No count shown to anyone (no vanity numbers, already ruled).
- **It teaches the profile:** a cool on a wildflower walk in April adds or strengthens "wildflowers · spring" as "we noticed".
- **It never sends anything by itself** (the 2026-09-17 test: if support ever notifies, it has become a subscription). Timing comes from the profile, section 4.
- **The owner sees** at most a weekly count ("12 people thought this was cool"), never names. Same question as the open "may an owner see their audience" ruling.

</details>

<details><summary>What happens to Follow: replace, keep both, or rename</summary>

- **Replace:** simplest to explain, but loses "tell me every time my bakery posts", which is the one thing Follow does well and which you ruled replaces promotional email.
- **Keep both, rename Follow "Get updates" (recommended):** matches the precedents and your 2026-09-17 ruling word for word. Cool is the default tap; Get updates sits one step further in (on the Page).
- **Merge into one tap with a bell inside:** YouTube's model. Neat, but two decisions in one control, and people end up subscribed without meaning to.

</details>

<details><summary>Everything that leans on Follow, and what it becomes</summary>

| Today | Under "keep both, rename" |
|---|---|
| Push: "new posts from Pages you follow" (2026-10-25) | "New posts from Pages you get updates from". Unchanged otherwise |
| Weekly Thursday "this weekend near you", from followed Pages plus interests and area (2026-10-25) | Same, plus in-season interests from the profile (section 4) |
| "From who you follow" shelf, fixed first (shelves scenario) and "followed first" in every view (2026-10-27) | Stays for Get updates; a cool on a Page raises it within shelves but doesn't put it in the fixed first shelf |
| Shelf "saves" counted as thumbs up, add to calendar or follow (shelves scenario) | Add Cool to what counts as a save |
| Followed Pages' posts reach a signed-in reader on Explore (F059) | Unchanged, for Get updates |
| You → Following, the management list | "Get updates from" plus "Things you thought were cool", each removable |
| F113 profile lists follows; the off switch keeps follows | Lists both; the off switch keeps both (the member chose them) |
| No public follower counts; ranking never uses follower count | Same for Cool counts |
| Owner's audience is unreadable today (open question) | Same open question, now for both |
| Private Pages have members, not followers | Unchanged; Cool works only on what the member can already see |
| Messaging between creators and followers (future, 2026-09-12) | "Get updates" people, not Cool people |
| Use cases and member journey ("follow what you love") | Reworded: cool what you love, get updates from your regulars |

</details>

## 4. "Alert me when the time is right"

**Timing should come from the profile ("wildflowers · spring"), not from each tap, and it should ride inside the Thursday note members already get. One more line in a note they've allowed, not a new ping. Nothing is ever sent because a member has been away.**

<details><summary>How it works without nagging</summary>

- **Season comes from the member:** said in the chat ("I garden in spring") or added from two seasons of cools, and always shown on the profile so they can change it.
- **It fires on a real thing, not the calendar:** the Thursday note mentions wildflowers only when there's a matching post this weekend nearby. "It's spring" with nothing to go to is noise.
- **One line, at most once a week:** inside the existing weekly note, under its own on/off, quiet hours and pause.
- **Out of season, it rests:** gardening drops out of Home and shelves in winter unless the member searches for it. Find never hides anything.
- **Tracking:** aggregate counts only (how many notes mentioned an in-season interest, how many were opened), never a target to raise, as already ruled.

</details>

<details><summary>Fit with the notification rulings</summary>

- **2026-10-25 notifications:** two kinds today: new posts from followed Pages, and the weekly Thursday note from followed Pages plus interests and area. In-season interests are "interests" already, so this fits the second kind without a new ruling on kinds. It does need a ruling that a season on an interest may decide what the Thursday note includes.
- **"Support never notifies":** kept. Cool shapes the profile; the profile, not the tap, informs the weekly note. If you'd rather be strict, timing can stay off push entirely (option C).
- **Nothing sent because a member has been away:** kept; timing is about the season, not the member's absence.

</details>

## 5. Options

**One recommendation per idea, and a smallest first version that tests all three together.**

<details open><summary>Taste profile</summary>

- **A. Short chat plus an editable list (recommended).** Three questions about once a week, our labels only, the member confirms; the list on You replaces the checkboxes. About a cent per member per month.
- **B. A better picker, no AI.** Type-to-search our labels and tags, with a season choice on each. Cheapest and predictable, but still forms to fill in, and the no-chips rule limits how rich it can look.
- **C. Learn only from behaviour.** No chat, no picker: searches and cools build it, the member edits. Least effort for members, but slow to start and blind to seasons until a year has passed.

</details>

<details open><summary>Cool and Follow</summary>

- **A. Keep both, build Cool, rename Follow "Get updates" (recommended).** Matches your 2026-09-17 ruling and every precedent; nothing that leans on Follow breaks.
- **B. Replace Follow with Cool.** One tap, simplest story, but the bakery's regulars lose "tell me every time", and the posts-from-Pages push and the first shelf need rebuilding around interests.
- **C. One tap with a bell inside.** Cool by default, "tell me everything" one step in. Tidy, but two decisions in one control.

</details>

<details open><summary>Right-time alerts</summary>

- **A. In-season interests ride in the Thursday note (recommended).** No new notification kind; one line, only when there's a real match nearby.
- **B. A new "in season" notification kind,** at most weekly, with its own switch. Clearer for members, but one more ping and one more thing to tune.
- **C. No push: timing only reorders Home and shelves.** Zero nagging risk, but "alert me when the time is right" becomes "show me first when I open the app".

</details>

<details><summary>Smallest first version</summary>

1. **Cool tap** on cards and Pages; it writes "we noticed" interests; no notifications; counted as a shelf save.
2. **The interests list on You** in plain words, with "you said" and "we noticed" apart, each removable, plus an optional season per line. This replaces the checkboxes.
3. **The 3-question chat** writing to that list, once a week, with confirmation.
4. **One in-season line** in the Thursday note, behind its own switch.
5. **Rename Follow to "Get updates"** (copy only).

Then watch, in aggregate: cool taps vs Get updates taps, how many members finish the chat, and whether in-season lines get opened. Words throughout are drafts for you.

</details>
