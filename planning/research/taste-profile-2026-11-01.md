# Taste profile: one adaptive algorithm, built on a sliding interest scale

**As of 2026-11-01** · Source: hand-written · Maintained by: hand

## Bottom line for Don

**One idea runs everything a member is shown: for each member, how strong their interest in each thing is right now. It's learned mostly from what they already do (opens, saves, shares, searches, return visits, "I'm coming"), plus one light, private tap that's weaker than Follow. Each interest fades at its own pace, so "always loved" lasts months, "on occasion" comes back when it recurs, and a passing spike fades in weeks. Discover, Home, the shelves, the weekly push and the order of search rows all read it.**

- **Your ruling (2026-11-01):** no checkboxes and no manual strength pickers as the main way in; Follow is too strong. The new section right below answers it, with how TikTok does it.
- **Your words, in the ethos:** "We need to be fluid and evolve with our members however they evolve." Soul line [always] (#262), with your one-day vs. one-year example.
- **How, not just what:** the same engine learns how far ahead each member plans, when they look and how far they'll go (§ 2).
- **What Follow becomes:** a quiet "Get updates" in a Page's menu, for the few Pages a member wants every post from. Nothing built breaks.
- **What the member controls:** they see what was learned and why, remove it, say "less of this", or turn learning off.
- **Your calls:** A, B or C, then the tap's word. I recommend **A** (learn from use + one light private tap; Follow kept quiet), and lean "Save" or "This is cool".

*The PM, 2026-11-01:* "We should be able to adapt to each members preferences in a way that serves them. For example I only plan one day ahead whereas someone else may plan a year ahead." Before that: "So I want to review what the research surfaced but more importantly I want to capture this is a concept and use it for an algorithm that can be dynamic and adaptive. We need to be fluid and evolve with our members however they evolve. It needs to be part of our ethos and inform our choices." Earlier: "I want it to be something less committal than following and more akin to this is something I'm interested in where the strength of the interest is on a sliding scale that changes over time or between seasons." And: "I don't like the interest check boxes on the profile page … it's definitely not check boxes."

Research only. Nothing here is ruled except the soul line (#262) and the 2026-11-01 ruling below, and nothing gets built until you pick. Sections 1–7 are the earlier research; where they conflict with the new section, the new section holds.

## Gauging interest without asking

**Bottom line: learn interest mostly from what members already do, plus one light, private tap that's weaker than Follow and never subscribes. Keep Follow only as a quiet "Get updates" on a Page's menu, so nothing that's built breaks. The thing TikTok does that we should copy isn't watch time. It's that every interest learns its own fade rate from how often it comes back, so "I've always loved this" fades over months and "a passing spike" fades in two weeks.** We have hundreds of signals per member where TikTok has billions, so we use simple, explainable counts, borrow from the Page's own topic and season and from what's popular nearby, and treat "I'm coming" as the strongest signal of all. I recommend **A** (below).

**Ruling (Don, 2026-11-01): no checkboxes, and no manual strength pickers as the main way in. Follow is too strong; find something lighter. [for now]** Don: "No checkboxes. We need to figure out the TikTok methods for gauging interest that means something between I've always loved this and I love this on occasion. Follow is too strong so we need to find something lighter." This replaces the parts of § 4 and § 7 that made a picker the main way in. A member can still see and correct what was learned in You; that just isn't how it starts.

<details><summary>1. How TikTok actually gauges interest</summary>

**What it watches** (TikTok's own [How TikTok recommends videos](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you), 2020):
- **Interactions:** likes, shares, comments, follows, and whether you watch to the end. "Not interested" (long press) is the explicit negative.
- **Video information:** captions, sounds, hashtags.
- **Device and account settings:** language and country. These weigh least, because users don't choose them as preferences.
- **Strength counts more than presence:** finishing a longer video outweighs living in the creator's country.
- **No two in a row:** two videos in a row never share a sound or creator, and nothing you've already seen is shown again.

**What it optimizes:**
- The 2021 leaked internal doc ([NYT reporting](https://www.nzherald.co.nz/business/how-tiktok-reads-your-mind/KARWQK6ZOGITZACXNAWRGH2ETU/), syndicated) gives a simplified score: predicted like × its value, plus predicted comment × its value, plus expected watch time × its value, plus predicted play × its value. The goals are **retention and time spent**.
- The same doc says repetition breeds boredom, so it penalizes the same creator or tag twice in a day and forces in other content.
- **This is the part we don't copy (never-extractive).**

**What actually moves the feed:**
- The WSJ's 2021 bot investigation ([summary](https://www.tubefilter.com/2021/07/21/tiktok-recommendation-algorithm-wall-street-journal-guillaume-chaslot/amp/)) found **lingering and rewatching** drove what came next more than likes or shares. Feeds narrowed within an hour or two.
- An academic audit ([Boeker & Urman, WWW '22](https://arxiv.org/abs/2201.12271)) found **follow** the strongest factor, then like, then share of the video watched.
- So the deliberate signals still weigh most per action. Watch time wins because there's so much of it.

**Lasting vs passing:**
- ByteDance's [Monolith paper](https://arxiv.org/abs/2209.07663) (2022) shows the plumbing.
  - The model updates from new feedback within minutes.
  - An interest no one engages with for a set period **expires**.
  - A one-off is admitted only after it shows up a set number of times.
- Industry models keep two memories:
  - a **lifelong** history, searched for whatever relates to the item in front of you ([Alibaba SIM](https://arxiv.org/abs/2006.05639); [Kuaishou TWIN](https://arxiv.org/abs/2302.02352), up to 100,000 past actions);
  - a **recent-session** model ([SLi-Rec](https://www.ijcai.org/proceedings/2019/585) blends the two by how long it's been since your last action).
- An interest "lasts" because it keeps coming back, not because it once spiked.

**Controls:**
- **Manage topics** ([TikTok, 2025](https://newsroom.tiktok.com/personalize-for-you-feed-with-new-features?lang=en-MY)): more or less of about 10 topics, never all-or-nothing.
- **Refresh your For You feed** ([2023](https://www.searchenginejournal.com/tiktok-refresh-for-you-feed/482667/)): starts the feed over as if you'd just joined, without touching who you follow.
- **Favorites:** a private bookmark (not confirmed on an official TikTok page).

**The others, briefly:**

| App | What it weighs | Lasting vs passing | Source |
|---|---|---|---|
| Instagram Reels | Predicted reshare, watch to the end, like, open the audio page; Explore adds saves. Since 2024 the head of Instagram has said **sends** (shares to a friend) matter most for reach (press, not an official page). "Not interested" | Not published | [Instagram Ranking Explained](https://about.instagram.com/blog/announcements/instagram-ranking-explained) (2023); [press](https://www.socialmediatoday.com/news/instagram-shares-algorithm-2025/738034/) |
| YouTube | Clicks, watch time, likes, dislikes, shares, and **"valued watch time"**: 1–5 star surveys where only 4–5 stars count, predicted for people who don't answer | Ranks by expected watch time, with an age correction so new things aren't buried | [On YouTube's recommendation system](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/) (2021); [Covington et al.](https://research.google/pubs/deep-neural-networks-for-youtube-recommendations/) (2016) |
| Pinterest | Saves, clicks and close-ups, grouped into **several interests per person** | **The clearest precedent.** Each interest is weighted by how often and how recently it was used, recomputed daily from 60–90 days of actions. Weighting recency too heavily "compromises long-term interests." A separate real-time model handles today | [PinnerSage](https://arxiv.org/abs/2007.03634) (2020); [TransAct](https://arxiv.org/abs/2306.00248) (2023) |

**Not verified:** the WSJ and NYT originals (read through syndicated copies); any audit measuring how fast an interest fades on TikTok; the exact weight Instagram gives shares vs likes.

</details>

<details><summary>2. Telling "always loved" from "love on occasion"</summary>

**The idea:** each member-topic pair (and each member-Page pair) gets a pattern from **how often it comes back**, and the pattern sets how fast it fades. That replaces § 1's flat "half every month". It's PinnerSage's frequency-times-recency idea, sized for us.

**What we'd count, per member, per topic and per Page:**

| Signal | What counts | Weight [guess, tune in beta] |
|---|---|---|
| **"I'm coming"** / Count me in | Tapped | 4: real-world intent, our strongest |
| **The light tap** (part 3 below) | Tapped | 3 |
| **Share** | Sent to someone | 3 |
| **Save / add to calendar** | Tapped | 2 |
| **Search** | A search matching the topic or Page | 1 |
| **Return visit to a Page** | Opened on a different day from the last open | 1 |
| **Open** | Card opened | ½ |
| **Card dwell** | Card stopped on screen 2+ seconds without opening | ¼, a hint only |
| **Fast scroll-past** | Seen under half a second, three times or more | Only nudges down; never on its own |
| **"Not for me"** | In the card's menu | Drops the Page or topic a step, and it isn't guessed back |

**The measures** (computed nightly from the 90 days of raw signals F113 keeps, plus the monthly summaries that outlive them):
- **Active weeks:** weeks out of the last 26 with a signal worth 1 or more.
- **Spread:** months between the first and last active week.
- **Burst share:** the share of the signal that landed in the busiest single week.
- **Same months last year:** whether it was active in the same months a year ago.

**The patterns:**

| Pattern | Rule [guess] | Fades by half in | Example |
|---|---|---|---|
| **Always loved** | 6+ active weeks out of 26, spread over 3+ months, no week over 40% | ~6 months | Live music every few weeks all year |
| **On occasion** | 2–5 active weeks, spread over 2+ months | ~2 months, back to full strength when it recurs | Antique fairs a few times a year |
| **Seasonal** | Active in the same months last year, quiet between | Near zero out of season; rises ~4 weeks before | Gardening each March |
| **Passing spike** | 60%+ in one week, no return within 8 weeks | ~2 weeks | Wedding venues for a month |
| **Too early to tell** | Under 8 weeks of history | ~1 month (§ 1's default) | Any new member |

**What it changes:**
- "Always loved" earns a Home shelf.
- "On occasion" shows up when something fits and otherwise stays out of the way.
- A spike doesn't take over Home after it's over.
- The member sees the pattern in plain words in You ("you come back to this every few weeks"), and can remove it or say "less of this".

</details>

<details><summary>3. The lightest tap that's weaker than Follow, and what to call it</summary>

| App | Light gesture | Who learns of it | Stronger tier |
|---|---|---|---|
| Instagram | Like (public to the poster); **Save** to a collection ([private](https://help.instagram.com/1744643532522513)) | Save: only you | Follow |
| TikTok | Like; **Favorites**, a private bookmark | Favorites: only you, by default | Follow |
| YouTube | Like | Not you, but counted | Subscribe, then the [bell: All, Personalized, None](https://support.google.com/youtube/answer/3382248) |
| Pinterest | **Save** to a board | Counted in the creator's stats | Follow |
| Letterboxd | Heart; **Watchlist** ("want to see") | Your own profile | Follow a member |
| Goodreads | **[Want to Read](https://help.goodreads.com/s/article/000001101)** shelf | Can show in friends' feeds | Follow an author |
| Google Discover | **Heart** on a card; "Not interested in…" | [Shared anonymously](https://support.google.com/websearch/answer/2819496) with publishers | Follow a topic |
| Apple Music | **[Favorite](https://support.apple.com/guide/iphone/tell-apple-music-what-you-enjoy-iph744ea4009/ios)** (was "Love"); Suggest Less | Only you | Add to library |
| Facebook Events | **[Interested](https://www.ubergizmo.com/2015/11/facebook-kills-maybe-button-for-interested/)** (replaced "Maybe" in 2015) | **The host, and it subscribes you to updates** | Going |

**The lightest one that still gives a clear signal is a save-type tap: private and forward-looking ("I want this in my orbit").**
- A like is mostly a social gesture to the poster, so it says little about what you want later.
- A save says what you want, and it's what Instagram weighs for Explore. Letterboxd's watchlist and Goodreads' Want to Read are the same "want to" idea.
- Ours must notify no one and subscribe to nothing. That keeps it inside the 2026-09-17 "support never notifies" ruling.
- Facebook's "Interested" is a warning: the word sounds light, but it subscribes you and tells the host.
- F121's "saves" count (thumbs up, calendar, follow) would count this tap too.

**Word options for you** (it's new copy, so it's your call):

| Word | Feel | Risk |
|---|---|---|
| **Save** (bookmark icon) | The most familiar; reads as "for later", private by habit | Sounds like a list feature more than a taste signal |
| **This is cool** | Your words; warm and local | New to members; a little long on a card |
| **Into it** | Casual; says taste, not a plan | Untested |
| **Interested** | Pairs with "I'm coming" | On Facebook it subscribes you and tells the host |
| Heart alone | Light, universal | Reads as a public like on Instagram; we'd have to say it's private |

I lean **Save** for clarity, or **This is cool** if you want the warmer voice.

</details>

<details><summary>4. What happens to Follow</summary>

**Keep it, quiet:** "Get updates" moves into the Page's menu, like YouTube's bell sitting behind Subscribe.
- It's for the few Pages a member wants every post from: their kid's school, their own farm stand.
- Everyone who follows today keeps it under the new name, so no one loses anything.
- **Nothing breaks.** The "new posts" push, Get-updates Pages first in every view, followers-only announcements (F072) and the owner's named list (F067) all keep working (§ 3's table, column A).

**Drop it:** everything in § 3's column B breaks.
- Followers-only announcements lose their audience.
- Owners no longer see who follows.
- The "new posts from Pages you follow" push has nothing to read.
- The followed shelf becomes a guess.
- Each would need a new ruling.
- No big app has dropped following. They added lighter taps beside it.

</details>

<details><summary>5. Options, and how we start with little data</summary>

**Where we differ from TikTok, and what it means:**

| TikTok | SocialUs | So we… |
|---|---|---|
| Billions of signals a day; hundreds of videos per session | A few dozen signals per member per month | Use weighted counts, per-pattern fades and a few hand-set rules, not a trained model. Every strength can show its reason (F113) |
| Optimizes time spent and retention | Never-extractive: the goal is finding something and going | Dwell is a hint and never a goal; "I'm coming" weighs most; success is saves and "I'm coming", never minutes in the app |
| Every video is the same kind of thing, available any time | Things happen on a date, nearby | Season, date and distance matter as much as taste; a great thing that's over is worth nothing |
| Learns from strangers' behaviour at huge scale | Small towns, small numbers | Borrow from the Page's own topic and season and from member-free area counts, not from other members' profiles |

**Starting with little data:**
1. **A new member** starts with what's popular near them this week (the member-free weekly counts) and the season, so Home isn't empty.
2. **Fast early learning:** the first few signals count double for two weeks, so a member who taps three garden things sees gardening by the weekend.
3. **Lean toward the town until there's enough:** a topic's strength blends with the area average until the member has about five signals for it [guess].
4. **The Page tells us the rest:** one tap on a farm stand also lifts its topic (Farmers markets), its places and its season.
5. **Patterns wait for evidence:** "Too early to tell" until 8 weeks; seasons from each topic's known calendar until a year of data exists.
6. **Keep a window open:** the "what's new" shelf keeps unfamiliar Pages in view, TikTok's anti-repetition lesson.

| | **A. Learn from use + one light private tap; Follow kept quiet** (recommended) | **B. Learn from use only; Follow unchanged** | **C. One light tap replaces Follow** |
|---|---|---|---|
| Way in | Nothing to fill in; the tap speeds it up | Nothing to fill in | Nothing to fill in; the tap speeds it up |
| "Lighter than Follow" | Yes | No; Follow stays the only gesture | Yes |
| Learns fast with little data | Yes: the tap is a strong, clear signal | Slowly; few signals per member | Yes |
| Breaks rulings | None | None | F072 and F067, and the new-posts push (part 4) |
| Precedent | Instagram, TikTok, Pinterest: save beside follow | Pure TikTok For You | None of the big apps |
| Path | Well-worn | Well-worn | New territory |

**Smallest first version under A:**
1. Record the signals per member (F113 already allows this).
2. Add the tap on cards and Pages, plus "Not for me" in the card menu.
3. Run the nightly patterns into the "Because you like…" shelf and the Thursday push.
4. Move Follow to "Get updates" in the Page menu.
5. In You, "What you're into" shows the learned list with reasons, for removing or correcting, not for picking.
6. The weekly chat (§ 4) becomes an optional "tell us more" later, not the way in.

**Your calls:** A, B or C; then the tap's word.

</details>

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
| **Weekly Thursday push** | Fills its interest slot with the in-season, high-strength topic | No new kind of notification; nothing is sent because a strength rose (§ 6) |
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
- **What the member sees** (no longer the way in, per the 2026-11-01 ruling; the fade rate now depends on the pattern): five steps, not a number: *Not now · A little · Some · A lot*, plus the months. That's the explicit half. The implicit half shows as the reason ("from 3 taps and 2 searches"), as F113 already describes.

</details>

## 2. How each member plans and uses the app, not just what they like

**The scale also holds a handful of habits per member, starting with how far ahead they plan. A one-day planner's Home opens on tonight and tomorrow; a year-ahead planner's opens on "Plan ahead" shelves months out. Each habit is learned from what the member taps and searches, can be asked once in the taste chat, and shows in You as one plain line they can change.** The evidence is strong that people differ here. Eventbrite found [57% of US music tickets were bought a week or less before the show](https://www.nivassoc.org/news/2024/last-minute-ticket-buying-eventbrite-releases-study-at-niva-24) (2024), while galas and dinners sell months out.

<details><summary>Details</summary>

**What other apps do**

| App | What it adapts to | What we take |
|---|---|---|
| Spotify [daylist](https://www.engadget.com/spotifys-latest-playlist-auto-adapts-to-your-day-122541712.html) (2023) | Time of day: it refreshes several times a day from what you played at that hour | Time of day is a habit worth learning |
| Netflix ([Learning a Personalized Homepage](https://gwern.net/doc/www/netflixtechblog.com/2f5717e8bbdc98d2caf5c7a972359fbb7e7c0b28.html)) | Which rows a member gets and their order, from viewing pattern | Shelf order per member, not one fixed order |
| Google Maps commute | Learns your usual trips and times, then times its alerts to them | Alerts arrive when a member usually plans, not on our schedule |
| Google Calendar | Working hours and "find a time" around your habits | A stated preference overrides the guess |

**The habits, how we'd learn each, and what it changes**

| Habit | Learned from | Or asked once in the chat | What it changes | What the member sees in You |
|---|---|---|---|---|
| **How far ahead they plan** (the first one) | How far out the dates are on things they open, save or say "I'm coming" to | "Do you plan the day of, a week out, or months ahead?" | Home's time window; puts "Tonight" first or "Plan ahead: next 3 months" first; how early the weekly push mentions something | "You usually plan **a day or two** ahead" · change |
| **Time of day** | When they open the app and when they tap | — (learned only) | When the weekly push arrives, within quiet hours; morning vs. evening shelves | "You usually look **in the evening**" · change |
| **Weekday vs. weekend** | Which days the things they save fall on | "Mostly weekends, or weeknights too?" | Shelf order (weeknight trivia vs. Saturday markets); Thursday push content | "Mostly **weekends**" · change |
| **How far they'll go** | Distances of what they open and say "I'm coming" to | "How far will you go for something good?" | The ring Home and shelves open on (the place rings already exist) | "Usually within **20 minutes**" · change |
| **Alone, with friends, or with kids** | Taps on family vs. 21+ posts | "Who do you usually go with?" | Kids & family shelves rise or fall; bars and late shows fall for a family planner | "Often **with kids**" · change |
| **How often they want a nudge** | Which pushes they open or turn off | "How often should we tell you about things?" | Weekly only, or weekly plus in-season (if you later rule that kind) | "**Weekly**" · change |
| **Price comfort** (weaker evidence) | Free vs. paid on what they save | — | Free things rise for members who mostly pick free | "Mostly **free things**" · change |

**Rules for habits, the same as for interests:**
- A stated habit always beats a learned one, and never fades.
- A learned one fades if behaviour changes, so a member who starts planning further ahead in summer sees Home follow within weeks.
- Each one is a single line in You with a reason ("from 12 things you saved") and a change link.
- The off switch stops learning habits too.
- Habits never hide anything. They change order and timing only, and Find stays complete.
- No habit is shown to anyone else or to Page owners.

**Smallest first step:** planning horizon only. Learn it from saves and "I'm coming", ask it as one question in the chat, and use it for Home's time window and the order of "Next 7 days" and "Plan ahead" shelves.

</details>

## 3. "This is cool" instead of Follow

**Add a one-tap "This is cool" on cards and Pages that raises the strength of that Page and its topics and never subscribes. Keep Follow, renamed "Get updates", for the few Pages a member wants every post from.** That's the split you already ruled on 2026-09-17 (support vs. get-updates), so "This is cool" is the unbuilt support ribbon, now with a job. Removing Follow outright would break five live features that need a list of "everyone who asked for this Page's posts".

<details><summary>Details</summary>

**What already exists:** the 2026-09-17 ruling gives two links between a member and a Page: **Support** ("I like that this exists", soft, never in the inbox, unbuilt) and **Get updates** ("tell me what this Page posts", which is today's Follow). "This is cool" is Support with a clearer name and a purpose. One conflict to settle: that ruling says support produces no notifications **ever**. Option A keeps that, since "This is cool" never sends anything on its own and only changes what the existing weekly push picks (§ 6).

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

## 4. Taste profile instead of checkboxes

*Superseded in part by the 2026-11-01 ruling: the list and chat stay as optional ways to correct or add, not the way in (see Gauging interest without asking).*

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

## 5. Watching search and taps

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

## 6. "Alert me when the time is right"

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

## 7. Options (earlier; replaced by the options under Gauging interest without asking)

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
