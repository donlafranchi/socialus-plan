# Taste profile: one adaptive algorithm, built on a sliding interest scale

**As of 2026-11-01** · Source: hand-written · Maintained by: hand

## Bottom line for Don

**Can members like or save posts today? No.**
- **There's no like, save or thumbs up anywhere.** No post or Page has one.
- **Add to calendar** downloads a calendar file, and we don't record who tapped it.
- **What we do record per member:** Follow (Join on a private Page), Remind me on a dated post, and Count me in.
- **Recommendation: add one private tap to every post and Page.** It means "I like this, keep it for me". It saves the post to the member's list and teaches the app what they're into. It notifies no one and subscribes them to nothing.
- **Follow** becomes a quiet "Get updates" in a Page's menu.

- **Your direction (2026-11-02):** "Since we're not like TikTok we'll need another method though."
  - The model is now the local apps: Eventbrite, Yelp, Google Maps, Airbnb, Pinterest, Meetup and Facebook Events. They learn from a small number of deliberate taps, not from watch time.
  - Only TikTok's fading and recurrence ideas carry over.
- **Your ruling (2026-11-01):** no checkboxes, no manual strength pickers as the main way in, and Follow is too strong.
- **Telling "always loved" from "on occasion":** we judge it by how often a member comes back to a topic or Page over months, and each kind fades at its own speed.
- **Your words, in the ethos:** "We need to be fluid and evolve with our members however they evolve." This is the soul line [always] (#262).
- **Your calls:**
  - Pick A, B or C. I recommend **A**: one tap that both likes and saves.
  - Pick the tap's word. I lean **Save**, or **Like** with a heart as Eventbrite does.

*The PM, 2026-11-02:* "Since we're not like TikTok we'll need another method though. Can we like or save posts" *2026-11-01:* "We should be able to adapt to each members preferences in a way that serves them. For example I only plan one day ahead whereas someone else may plan a year ahead." Before that: "So I want to review what the research surfaced but more importantly I want to capture this is a concept and use it for an algorithm that can be dynamic and adaptive. We need to be fluid and evolve with our members however they evolve. It needs to be part of our ethos and inform our choices." Earlier: "I want it to be something less committal than following and more akin to this is something I'm interested in where the strength of the interest is on a sliding scale that changes over time or between seasons." And: "I don't like the interest check boxes on the profile page … it's definitely not check boxes."

Research only. Nothing here is ruled except the soul line (#262) and the 2026-11-01 ruling below, and nothing gets built until you pick. Sections 1–7 are the earlier research; where they conflict with the new section, the new section holds.

## Gauging interest without asking

**Bottom line: one private tap that means "I like this, keep it for me" does both jobs, the way Eventbrite's heart and Airbnb's wishlist do. Add it to posts and Pages, learn the rest from what members already do, and keep Follow as a quiet "Get updates".** Lasting interest shows up as coming back to a topic or Page over months, the way Pinterest boards, Google Maps lists and repeat RSVPs show it. With little data, the Page's own topic, its distance and its date carry most of the weight, which is what the Meetup research found too. I recommend **A** (part 6).

**Ruling (Don, 2026-11-01): no checkboxes, and no manual strength pickers as the main way in. Follow is too strong; find something lighter. [for now]** Don: "No checkboxes. We need to figure out the TikTok methods for gauging interest that means something between I've always loved this and I love this on occasion. Follow is too strong so we need to find something lighter." Then, 2026-11-02: "Since we're not like TikTok we'll need another method though. Can we like or save posts". This replaces the parts of § 4 and § 7 that made a picker the main way in. A member can still see and correct what was learned in You; that just isn't how it starts.

<details><summary>1. What members can do today (from the code, 2026-11-02)</summary>

| Gesture | Where | Stored per member? | Notifies anyone? |
|---|---|---|---|
| **Like / heart / thumbs up** | Nowhere. An unused heart Follow button sits in the code, shown on no screen | — | — |
| **Save / bookmark** | Nowhere. An older items table reserves "save" and "interest" kinds, but nothing writes them | — | — |
| **Add to calendar** | Dated posts and gathering pages | **No.** It downloads a calendar file. From a shelf it adds one to that shelf's member-free weekly save count | No |
| **Remind me** | Dated posts ("Just this one" or "Every time" for repeats) | **Yes**, private to the member | Only the member, before it starts |
| **Follow / Join** | Pages (Join when private) | **Yes** | The member gets new-post pushes; the owner sees followers by name (F067) |
| **Count me in** | "Count me in" posts | **Yes** | The post shows a count |
| **"I'm coming" / RSVP** | **Not built.** A reserved kind in the older items table only | — | — |

**So:** the only light, private, per-member signal today is Remind me, and it exists only on dated posts. Nothing light exists for a Page or an undated post. Earlier sections that treat "I'm coming" or saves as existing were wrong.

</details>

<details><summary>2. How local listings and events apps gauge interest</summary>

| App | Light gestures | Who learns of it | Stronger tier | How it tells lasting from occasional |
|---|---|---|---|---|
| **[Eventbrite](https://www.eventbrite.com/help/en-us/articles/783059/)** | **Like** (heart): "saves it for later, but doesn't reserve a ticket" | The organizer sees a count, never who | Follow an organizer (emails on new events); buy a ticket | Recommendations use followed organizers plus events attended or saved ([release notes, press](https://techcrunch.com/2012/08/03/eventbrite-recommendations/)) |
| **Yelp** | **Bookmark** into Collections; check-ins; Useful / Funny / Cool on reviews | New collections are private by default ([press](https://smartphones.gadgethacks.com/how-to/use-yelp-collections-find-new-places-keep-your-bookmarked-locations-more-organized-0194859); not on an official page) | Review | **[Your Preferences](https://www.yelp-ir.com/news/press-releases/news-release-details/2019/Yelp-Introduces-an-Easier-Way-to-Find-Places-Youll-Love-Based-on-Personal-Preferences/default.aspx)** (2019), a page you fill in on purpose; repeat check-ins at a place |
| **[Google Maps](https://support.google.com/maps/answer/7546473)** | Save to **Want to go**, **Favorites**, Starred or your own list | Private unless shared | [Follow a place](https://techcrunch.com/2018/10/25/google-maps-takes-on-facebook-pages-with-new-follow-feature-for-tracking-businesses): its posts appear in "For you" | Lists are the lasting record. "Want to go" is intent; Favorites is love |
| **[Airbnb](https://www.airbnb.com/help/article/338)** | **Heart** into a named **wishlist** | Private, or shared with people you pick. Whether hosts are told isn't published | Book | Named wishlists hold lasting interest; one search's hearts group together on their own |
| **[Pinterest](https://help.pinterest.com/article/create-a-board)** | **Save** to a board (secret boards too) | Board visibility is yours to set | Follow | Boards are lasting interests. [PinnerFormer](https://arxiv.org/abs/2205.04507) learns from what you'll do over the **next 28 days**, not the next tap, and [a separate model](https://arxiv.org/abs/2209.08435) handles today |
| **[Meetup](https://help.meetup.com/hc/en-us/articles/39235072484109)** | **Save** an event | Private | **RSVP** (reminder 24 hours before), join a group | Joining a group plus repeat RSVPs to its events |
| **Facebook Events** | **[Interested](https://thenextweb.com/news/facebook-has-officially-killed-the-maybe-button-on-events-in-favor-of-interested)** (replaced "Maybe", 2015) | **The host and often friends; it also subscribes you to updates** | Going | Not published |
| **Instagram** | Like (the poster sees it); **[Save](https://about.instagram.com/blog/announcements/introducing-new-ways-to-organize-your-saved-posts)** (only you) | Save is private | Follow | [Explore weighs likes, saves and shares](https://about.instagram.com/blog/announcements/instagram-ranking-explained); saves signal stronger interest than likes |
| **[Letterboxd](https://letterboxd.com/about/faq/)** / Goodreads | **Watchlist** / **Want to Read** | Public by default | Log / Read | "Want to" moves to "done" once you act; repeat logs in a genre show lasting taste |

**What they share:**
- **Saving is private and doesn't subscribe.** Instagram, Eventbrite, Google Maps, Meetup and Airbnb all work this way. Only Follow, and Facebook's Interested, sign you up for updates.
- **"Interested" is the trap:** it sounds light, but on Facebook it tells the host and subscribes you.
- **Reminders hang on a commitment (Meetup's RSVP), not on a save.** Ours already do: Remind me is the member's own choice.
- **Lasting interest comes from repetition and lists, never from one tap:**
  - repeat saves on a topic;
  - a named list or board;
  - repeat RSVPs to one group.
- **Little data:** event research on Meetup data ([Macedo et al., RecSys 2015](https://dblp.dagstuhl.de/rec/conf/recsys/MacedoMS15.html); [Qiao et al., AAAI 2014](https://ojs.aaai.org/index.php/AAAI/article/view/9095)) calls events "intrinsically cold-start", because each one is short-lived and in the future. The signals that carry it are group membership, location, time and the event's own content, more than any one member's history.

**Not verified:**
- Facebook's official help on what Interested shares.
- Whether Airbnb tells hosts about hearts.
- Yelp's current privacy default for bookmarks.
- Meetup's exact save label.
- Which single signal won in Macedo 2015.

</details>

<details><summary>3. What we borrow from TikTok, and only this</summary>

TikTok learns from watch time on endless short video ([TikTok, 2020](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you); [WSJ reporting](https://www.tubefilter.com/2021/07/21/tiktok-recommendation-algorithm-wall-street-journal-guillaume-chaslot/amp/)), aiming at time spent ([NYT leak](https://www.nzherald.co.nz/business/how-tiktok-reads-your-mind/KARWQK6ZOGITZACXNAWRGH2ETU/)). We have neither, and we don't want the second (never-extractive). We borrow three things:
- **Recurrence:** an interest is lasting because it keeps coming back. Pinterest's [PinnerSage](https://arxiv.org/abs/2007.03634) weighs frequency against recency.
- **Decay:** unused interests expire ([Monolith](https://arxiv.org/abs/2209.07663)).
- **A weak negative:** a fast scroll-past, repeated, nudges down a little and is never used on its own.

</details>

<details><summary>4. Telling "always loved" from "love on occasion"</summary>

**The idea:** each member-topic pair (and each member-Page pair) gets a pattern from **how often it comes back**, and the pattern sets how fast it fades. That replaces § 1's flat "half every month".

**What we'd count, per member, per topic and per Page** (✓ = recorded today):

| Signal | What counts | Weight [guess, tune in beta] |
|---|---|---|
| **Remind me** ✓ | Set on a dated post | 4: the member plans to go |
| **Count me in** ✓ | Tapped | 4 |
| **The tap** (part 5) | Tapped on a post or Page | 3 |
| **Get updates** ✓ (today's Follow) | On | 3, and it doesn't fade while on |
| **Share** | Sent to someone | 3 |
| **Add to calendar** | Tapped (would need recording per member) | 2 |
| **Search** | A search matching the topic or Page | 1 |
| **Return visit to a Page** | Opened on a different day from the last open | 1 |
| **Open** | Card opened | ½ |
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
| **Always loved** | 6+ active weeks out of 26, spread over 3+ months, no week over 40% | ~6 months | Saves live music every few weeks all year |
| **On occasion** | 2–5 active weeks, spread over 2+ months | ~2 months, back to full strength when it recurs | Antique fairs a few times a year |
| **Seasonal** | Active in the same months last year, quiet between | Near zero out of season; rises ~4 weeks before | Gardening each March |
| **Passing spike** | 60%+ in one week, no return within 8 weeks | ~2 weeks | Wedding venues for a month |
| **Too early to tell** | Under 8 weeks of history | ~1 month (§ 1's default) | Any new member |

**What it changes:**
- "Always loved" earns a Home shelf.
- "On occasion" shows up when something fits and otherwise stays out of the way.
- A spike doesn't take over Home after it's over.
- A saved dated post leaves the member's list after its date, but still counts toward the pattern.
- The member sees the pattern in plain words in You ("you come back to this every few weeks"), and can remove it or say "less of this".

</details>

<details><summary>5. Like, save, or both: the lightest tap</summary>

**Recommendation: one tap, not two. It saves the post or Page to the member's list and counts as "I like this".**
- **Precedent:** Eventbrite does exactly this; its heart is called Like and saves the event for later. Airbnb's heart is a save too.
- **Why not two taps:**
  - With few signals per member, splitting them between Like and Save halves what we learn from each.
  - Members would have to guess the difference. Instagram has both, but its like is a public nod to the poster, which we don't want: no public counts (F065).
- **What it means:**
  - On a **dated post**: "I might go." It lands in a Saved list in You, and Remind me stays one tap away for going further.
  - On an **undated post**, a sale or a listing: "I want this in my orbit."
  - On a **Page**: "I like this place." It's the Google Maps Favorites idea, and no posts are pushed.
- **What it never does:**
  - It notifies no one and subscribes to nothing; the 2026-09-17 "support never notifies" ruling still holds.
  - It shows no public count.
  - The owner sees at most a private count, like Eventbrite.
- **If you'd rather have both:** Like means taste (it trains the scale, saves nothing). Save means a plan (it keeps the post in a list and trains the scale more). That's two words to explain and half the signal each, so I wouldn't start there.

**Word options** (new copy, your call):

| Word and icon | Feel | Precedent | Risk |
|---|---|---|---|
| **Save** (bookmark) | Clear: it's kept for later | Instagram, Meetup, Google Maps, Pinterest | Reads as a list, less as "I like it" |
| **Like** (heart) | Warm: says taste | Eventbrite (where it also saves), Airbnb heart | People expect a public like; we'd show it's private |
| **This is cool** | Your earlier words; local voice | None | Long for a card; new to members |
| **Into it** | Casual taste | None | Untested |
| **Interested** | Pairs with going | Facebook | On Facebook it tells the host and subscribes you |

I lean **Save** for clarity, with **Like** (heart) as the warmer alternative.

**Storage note for builders:** the older items table's reserved "save" kind isn't wired to posts or Pages, so the tap needs its own small private table. Under F113 the off switch keeps it, because it's declared, not guessed.

</details>

<details><summary>6. What happens to Follow</summary>

**Keep it, quiet:** "Get updates" moves into the Page's menu, like YouTube's bell sitting behind Subscribe, or Eventbrite's follow sitting beside its like.
- It's for the few Pages a member wants every post from: their kid's school, their own farm stand.
- Everyone who follows today keeps it under the new name, so no one loses anything.
- **Nothing breaks.** The "new posts" push, Get-updates Pages first in every view, followers-only announcements (F072) and the owner's named list (F067) all keep working (§ 3's table, column A).

**Drop it:** everything in § 3's column B breaks.
- Followers-only announcements lose their audience.
- Owners no longer see who follows.
- The "new posts from Pages you follow" push has nothing to read.
- The followed shelf becomes a guess.
- Each would need a new ruling.
- None of the local apps (Eventbrite, Google Maps, Meetup, Yelp) dropped following. Each keeps a lighter save beside it.

</details>

<details><summary>7. Options, and how we start with little data</summary>

**Starting with little data** (what the event research and the local apps rely on):
1. **The Page tells us most:** one tap on a farm stand also lifts its topic (Farmers markets), its places and its season.
2. **Distance and date carry the rest:** a new member starts with what's near them this week (the member-free weekly counts) and the season, so Home isn't empty.
3. **Fast early learning:** the first few signals count double for two weeks, so a member who saves three garden things sees gardening by the weekend.
4. **Lean toward the town until there's enough:** a topic's strength blends with the area average until the member has about five signals for it [guess].
5. **Patterns wait for evidence:** "Too early to tell" until 8 weeks; seasons from each topic's known calendar until a year of data exists.
6. **Keep a window open:** the "what's new" shelf keeps unfamiliar Pages in view.
7. **Simple and explainable:** weighted counts and a few rules, computed nightly, not a trained model. Every strength can show its reason (F113), and success is saves and Remind me, never minutes in the app.

| | **A. One private tap (like + save) on posts and Pages; Follow kept quiet** (recommended) | **B. Two taps, Like and Save; Follow kept quiet** | **C. One tap replaces Follow** |
|---|---|---|---|
| Lighter than Follow | Yes | Yes | Yes |
| Learns with little data | Best: every tap counts once, clearly | Splits few signals two ways | Same as A |
| Member understands it | One meaning | Two meanings to learn | One meaning, but Page updates are gone |
| Breaks rulings | None | None | F072 and F067, and the new-posts push (part 6) |
| Precedent | Eventbrite, Airbnb, Google Maps | Instagram | None |
| Path | Well-worn | Well-worn | New territory |

**Smallest first version under A:**
1. Add the tap on posts and Pages, with a Saved list in You. Dated posts leave the list after their date.
2. Record Remind me, the tap, Get updates and opens per member (F113 already allows this).
3. Add "Not for me" in the card menu.
4. Run the nightly patterns into the "Because you like…" shelf and the Thursday push.
5. Move Follow to "Get updates" in the Page menu.
6. In You, "What you're into" shows the learned list with reasons, for removing or correcting, not for picking.

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
| The light tap (like + save) | Not built | — | Yes, the main explicit signal |
| Remind me, Count me in | Yes | Yes | Yes |
| Add to calendar | Downloads a file only | No | Yes, if recorded |
| "I'm coming" / RSVP | Not built | — | Yes, later |

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
