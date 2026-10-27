# Views built from the ask: shelves, followed first, shelf life

**Every view is built from what the person asks for. In every view, timely posts from the Pages and people they follow come first. When those run out, a quiet line marks the end, and the view widens to everything else that matches.** A wide-open ask ("show me everything going on around me") gets the shelf view, which works like the App Store: categories run top to bottom and the items in each shelf run left to right. Every post gets a shelf life by kind, leaves these views when it ends, and stays on its Page and in search.

**Your one call:** how the shelf view is arranged (A, B or C, at the bottom). I recommend **A**.

*The PM, 2026-10-27:* "the categories are top to bottom and then the options in each category are left to right … the posts are timely and they need to be displayed in a timely manner and right now what we're showing is everything for all time and that's a little bit too much."

*The PM, later the same day:* "this is essentially one view … behind an agent search and if a person just says hey … I want to see all kinds of things going on around me then this is that view … every time a user comes in … we show them … the people they follow the announcements that they follow first and for any particular category or search request and when they run out, then we opened it up to more things … every view is based on the users search or what they're asking for."

Research only. Nothing here is ruled yet, and nothing gets built until you pick.

## 1. What other apps do

**Every large catalog app uses the same shape: a vertical stack of named shelves, each a horizontal row, with the timely shelves on top and the lasting ones below.** Apps that show timely things (Google, Facebook Events, Marketplace, Craigslist) all give posts a shelf life and keep the expired ones findable somewhere else.

<details><summary>Details</summary>

| App | Shape | Lasting items | Timely items |
|---|---|---|---|
| **App Store / Apple HIG** | Rows of collections ("shelves"), each scrolls sideways; a quiet "See All" opens the full list | Apps sit in category shelves | The Today tab and dated stories go on top; shelves are edited daily |
| **Google Play** | Bold section headers over sideways carousels; storefronts switched in the nav | Category carousels | Editorial cards for events and sales, swapped out when they end |
| **Netflix** | Rows ranked by the system, then titles ranked left to right inside each row; one image per title | Genre rows | "New this week" and "Top 10 today" rows on top |
| **Airbnb (2022)** | A sideways tab bar of 50+ categories above one grid | Listings by category | Nothing timely. **The tab bar is a row of controls, which our rulings forbid.** |
| **Yelp** | Search, then a row of category icons, then a vertical feed of local highlights | Businesses by category | Feed highlights come and go |
| **Eventbrite** | "Popular in [city]" first, a grid of top categories below | None | Every event leaves when it's over |
| **Facebook Events** | Time shelves (Today, Tomorrow, This weekend) and category shelves (Music, Food, Nightlife) | None | Time decides first, category second |
| **Meetup** | The group page splits Upcoming and Past events, with counts | The group | Past events move to Past; they're never deleted |
| **Apple News** | Top Stories (edited twice a day), then Trending, then sections by topic | Channels and topics | Stories age out of Today but stay in their channel |
| **Google Business Profile** | Posts on the business listing | The listing | Plain updates are current for about 7 days; offers and events until their end date; the rest are archived under "view more" |
| **Facebook Marketplace / Craigslist** | Listings by category | None | Marketplace about 7 days with a renew; Craigslist 7–45 days by category and city |
| **Nextdoor** | One feed | Business pages | No public documentation found on how posts expire. Gap. |

**What we take:**
- The shelf shape from the App Store and Play.
- The order, time first and category second, from Facebook Events and Netflix.
- Shelf life with an archive from Google Business Profile and Meetup.

**What we leave:**
- Airbnb's tab bar, because it's a row of controls.
- Netflix's engagement ranking, because Find never optimizes for time spent.

**Sources:**
- [Apple HIG: collections](https://developer.apple.com/design/human-interface-guidelines/collections)
- [Apple TVML: shelf](https://developer.apple.com/documentation/tvml/shelf)
- [Netflix Tech Blog: Learning a Personalized Homepage (2015)](https://gwern.net/doc/www/netflixtechblog.com/2f5717e8bbdc98d2caf5c7a972359fbb7e7c0b28.html)
- [Airbnb 2022 release](https://news.airbnb.com/en-au/a-new-airbnb-for-a-new-world-of-travel-launching-the-biggest-change-to-the-platform-in-a-decade)
- [Play Store 2019 redesign](https://mobilesyrup.com/2019/06/07/google-play-store-material-design-update-rolling-out/)
- [Yelp home feed, 2022](https://techcrunch.com/2022/08/02/yelp-updates-its-android-app-with-a-redesigned-home-feed-and-map-based-search/amp/)
- [Eventbrite design critique](https://ixd.prattsi.org/2020/02/design-critique-eventbrite-com/)
- [Facebook Events categories and time frames (TechCrunch, 2016)](https://techcrunch.com/2016/06/27/facebook-launches-human-curated-featured-events-list/)
- [Meetup group page, upcoming vs past](https://www.meetup.com/brisbane-social-singles/)
- [Meetup help: finding an event](https://help.meetup.com/hc/en-us/articles/39235072484109)
- [Apple News guide](https://support.apple.com/en-us/guide/news/welcome/6.1/mac)
- [Google Business posts (Zoho guide)](https://www.zoho.com/publish/google-business-profile-guide/google-posts/)
- [Craigslist: posting lifespan](https://www.craigslist.org/about/help/faqs/lifespan)
- [Marketplace renewals (Vendoo)](https://blog.vendoo.co/facebook-marketplace-delete-and-relist)

Most of the detail on Yelp, Eventbrite, Facebook and Marketplace comes from third-party write-ups between 2016 and 2026. Check the live apps before copying any specific detail.

</details>

## 2. Followed first, then wider: the rule for every view

**Instagram has shown "You're all caught up" and then suggested posts since 2018 and 2020. Threads and X keep a separate Following tab.** We adapt Instagram's version: an ask returns its matches from the Pages and people you follow first, newest and soonest first. Then one quiet line marks the end, and the rest of what matches follows, ordered by place and time. We don't copy its suggested posts, its ads, or its "can't turn it off".

<details><summary>Details</summary>

| App | What it does | What we take, what we leave |
|---|---|---|
| **Instagram** | A "You're all caught up" marker (2018) ends what's new from accounts you follow. From 2020, suggested posts from accounts you don't follow appear below it, with ads, and can't be hidden | **Take:** the marker and the order, followed first and then the rest. **Leave:** the ads, recommendations learned from your behaviour, and "can't hide" |
| **Threads / X** | A Following tab with posts in time order, next to an algorithmic For You tab | **Leave:** two tabs. One view that does both is simpler, and an ask already narrows it |
| **Nextdoor** | A business page collects neighbours' posts that mention it alongside its own posts | See the vouching entry in IMAGINE |

**How a view is built**, the same for every ask:
1. **Read the ask** (F119's router turns it into filters for kind, time, place and words).
2. **Followed block:** posts that match the ask, from Pages and people the member follows, that haven't passed their shelf life. Soonest first for dated posts, newest first for the rest.
3. **End marker:** one quiet line. Its words are yours to choose. It's absent when the member follows nothing, or when nothing they follow matches.
4. **Wider block:** everything else that matches, in Find's order (place, time, declared interests, community response). The followed items aren't repeated.

**What decides the view's shape:**
- A **wide-open ask** (no kind, no category) gets the **shelf view**: the followed block becomes the top shelf.
- A **narrow ask** ("food trucks this weekend") gets a **list**: the followed block, the marker, then the wider block.

**Following means getting their announcements.** This matches the existing rulings:
- 2026-09-17: a follow is "get updates", in place of vendor emails.
- 2026-10-25: push for new posts from Pages you follow.

**What's already in code:** Explore already reads the member's followed Pages and has a following row (`src/app/explore/load.ts`). The change makes that row the first block of every view, not one row among many.

**Sources:**
- [Instagram: "You're all caught up" (2018)](https://m.gsmarena.com/instagram_introduces_youre_all_caught_up_feature-news-32018.php)
- [Instagram: suggested posts after it (TechCrunch, 2020)](https://techcrunch.com/2020/08/19/instagram-finds-new-ad-space-at-the-end-of-your-feed-with-launch-of-suggested-posts-feature)
- [Instagram: suggested posts can't be hidden (Bustle)](https://www.bustle.com/life/instagram-suggested-posts-feature)
- [Threads' Following feed (CNBC, 2023)](https://www.cnbc.com/2023/07/25/meta-threads-gets-chronological-feed-for-people-you-follow.html)
- [Following vs For You on Threads and X (TechCrunch, 2024)](https://techcrunch.com/2024/11/06/for-you-feeds-fail-on-election-night-offering-outdated-information-angering-users)

</details>

## 3. Categories before data: the shelf view

**The shelf view answers a wide-open ask. Top to bottom:**
- **From Pages you follow**
- **Four timely shelves:** Today, This weekend, Deals this week, Count me in
- **Collection shelves of Pages:** Food & drink, Makers, Farms, and so on
- **New here** Time and post kind decide the timely shelves. The Page's main collection decides the lasting ones. An item shows once per screen, and a shelf with nothing on it doesn't appear.

<details><summary>Details</summary>

**The item types the code has today:**
- **Pages:** Business or Social group, each with owner-chosen collections.
- **Posts** come in three shapes:
  - Announcements, which are undated.
  - Dated posts, which count as events.
  - Wonders, which carry a threshold count.
- **Samples on unclaimed Pages:** three per Page (event, deal, last-minute opening).
- **Seeded posts:**
  - Market days, from a weekly series.
  - Venue shows, scraped up to 60 days ahead.

**A gap:** only samples say whether they're a deal or a last-minute opening. A real post can't, so a real deal can only show as news or as an event.

**A new item type: job postings** ("who's hiring"). This is a post kind: a role, pay if the owner gives it, how to apply. Its shelf life is 30 days or until it's filled. Until a kind field exists, it can't be told apart from news.

**Named views, composed from shelves.** Each one is an ask the router maps to filters, with followed items first:
- **"Who's hiring near me?"** A list of job postings, nearest first.
- **"What's happening this weekend?"** The This weekend shelf, opened as a list, split by day.
- **"Who has happy hour today?"** Recurring deals (a series, like market days) on today, soonest first. This needs the deal kind on real posts.

**Proposed shelves, top to bottom:**

| # | Shelf | What goes in it | Order inside |
|---|---|---|---|
| 0 | **From Pages you follow** (signed in) | Timely posts from followed Pages and people | Soonest, then newest |
| 1 | **Today** | Events and openings on now or later today | Soonest first |
| 2 | **This weekend** | Events Friday to Sunday (this week, Monday to Thursday) | Soonest first |
| 3 | **Deals this week** | Deals and offers that haven't ended | Ending soonest first |
| 4 | **Count me in** | Open Wonders | Closest to its goal first |
| 6+ | **One shelf per collection** with four or more Pages, using about seven groups of the current eleven collections: **Food & drink** (with bakery), **Makers** (goods, crafts, art and print), **Repair & trades**, **Farms** (farm, ranch, farm stay), **Community & volunteer**, **Arts & culture**, **Outdoors** | Pages, by the main collection the owner picked | Nearby, then recently active |
| last | **New here** | Pages created in the last 30 days | Newest first |

**How an item is placed:**
- Shelves are filled from the top, and an item lands in the first shelf it qualifies for.
- A Page goes in its main collection only.
- Each shelf shows about 10 to 12 items plus a quiet "See all" text link, which opens the full list as today's grid.

**How many shelves:** the followed shelf, the four timely shelves, and up to three collection shelves on first load. More collection shelves load as the member scrolls. Every empty shelf is absent, which F091 already does for the "What's happening" rows.

**Samples:** samples are the unclaimed Page's own advertisement, not something timely. One sample per unclaimed Page goes on Explore, rotating, never three at once, and at most one in four cards on any shelf. All three stay on the Page.

**Find, Discover and Home:**
- **These shelves are Find.** They're ordered by place and time, with your declared interests and community response. Nothing is ever paid or learned from your views.
- **Discover, later:** may add learned shelves such as "Because you follow…" and a marked promoted slot, under the 2026-10-25 rulings.
- **Home:** Home was ruled on 2026-10-04 (F098) as Tonight, This weekend, New this week and a wildcard row. That's already a shelf design, so Home and Explore should share one set of shelf components.

</details>

## 4. Shelf life

**Posts already leave Explore in code:**
- An event leaves when it ends.
- Any other post leaves 14 days after it was posted.

**What keeps Explore looking "everything for all time" is three other things:**
- Sample posts roll forward forever, three to every unclaimed Page.
- The main list is one flat mix with nothing to say what's timely.
- Pages, which last, fill it.

The proposal: a shelf life by kind, and every expired post still findable on its Page.

<details><summary>Details</summary>

**What the code does today:**
- `post_current_until`, from 2026-10-18 (#314), keeps a dated post until its end and an undated one for 14 days or until its `show_until`.
- `rollSample` moves a finished sample three weeks ahead, so samples never expire.
- Venue shows load up to 60 days ahead, so far-off shows sit next to tonight's.

**Proposed shelf life by kind:**

| Kind | On Explore until | Precedent |
|---|---|---|
| Event, market day, venue show | It ends. Only events in the next 14 days go on the timely shelves; later ones appear under "See all" and in search | Eventbrite, Facebook Events |
| Last-minute opening | It ends, within 48 hours | none needed |
| Deal or offer | Its end date: 7 days by default, 30 at most | Google offers |
| News (announcement) | 7 days by default; the owner can set up to 30. **Change:** down from 14 today | Google updates (7 days), Marketplace (7 days) |
| Wonder | Its sign-up closes: 30 days by default. Once it reaches its goal, it shows "It's happening" for 7 days, then leaves | none; new |
| Recurring series (market day, happy hour) | Only the next date shows | Meetup |
| Job posting | 30 days, or until filled | Craigslist jobs (30 days) |
| Sample | One per unclaimed Page, as above | none |

**Where an expired post goes:**
- It stays on its Page under a "Past" section, as Meetup and Google do.
- It stays in search when the words ask for the past ("last week", "past events").
- It stays in the member's own You list if they responded to it.
- Nothing is deleted, which keeps the staleness ethos: nothing vanishes without a trace.

**How it leaves:** it's computed when the page loads, from the dates, the way it is today. No scheduled job.

</details>

## 5. Why the samples look noisy

**A sample card says "Sample" four times and never says, in its first words, what it is, when, or who it's for.** The two lines under the headline are always the same disclaimer. The fix is a card whose first line is built from fields (kind · when · where) instead of the first sentence of the post.

<details><summary>Details</summary>

**What one sample card shows today, from `samples.ts` and `BrowseResultCard.tsx`:**
1. **Date line:** "SAT 5 PM". Fine.
2. **Title:** "Sample · Tasting at Folsom Coffee: free samples, the new seasonal lineup, and a chance to meet…"
   - It's a sentence, cut off after two lines.
   - It repeats the Page name, which the card shows anyway.
   - The kind word is buried.
3. **The two lines under the title:** "This is a sample post showing what Folsom Coffee's Page could look like. It is not a real offer…" It's identical on every sample card, so a shelf of them reads as a wall of disclaimers.
4. **Small marks:** a type mark, a Sample label and the kind line.
5. **A Sample watermark** over the card.

**The pattern:** no lead line. Each card opens with prose, so a reader has to read a sentence to learn whether it's a deal, an event or news.

Venue shows have the opposite problem: the title is just the act's name ("X with Y"), with no "live music" and no venue.

**Proposed card anatomy for a post** (it keeps the 60/40 text-led shape):
1. **Lead line**, small caps and bold, built from fields and never from the body: **KIND · WHEN · WHERE**. For example:
   - "TASTING · SAT 5–8 PM · MIDTOWN"
   - "DEAL · THROUGH SUN · EAST SAC"
   - "COUNT ME IN · 12 OF 30 · CLOSES NOV 8"
   - "NEWS · TUE"
2. **Headline** in one line, under about 60 characters, without the Page name: "Free tasting of the fall lineup."
3. **Who**: the Page's avatar and name. Add "For families" or "All ages" only when the owner said so.
4. **The smaller photo.**
5. **For samples:** the word Sample goes once, in the lead line ("SAMPLE DEAL · …"), and the watermark and the repeated disclaimer go. The disclaimer stays in the body on the Page itself, where the 2026-10-10 "every sample opens with Sample" rule applies.

**Seeder changes**, for the code lane, after you pick:
- **Samples:** write a separate short headline (no Page name) and the details; drop the disclaimer from what the card previews; show one sample per unclaimed Page on Explore.
- **Venue shows:** set the kind from the venue ("Live music", "Comedy", "Theatre") and use the venue name as the where.
- **Market days:** kind "Market" and the hours. Already close.

**Builder (compose) changes:**
- Pick the kind first: news, event, deal, opening, or Wonder.
- Write the headline separately from the details.
- A date is required for events and deals.
- The shelf life follows the kind, and the owner can change it.
- **Schema:** a real post needs a kind field, since only samples have one today. Code writes the architecture note.

</details>

## 6. Fit with chat-first

**The Ask bar (F119) turns a question into filters, and one rule builds the view from them:**
1. What you follow first.
2. A marker.
3. Everything else.

A wide-open question gets shelves; a narrow one gets a list. Shelves and cards are the stable building blocks that chat as home (F120) later shows inline. Chat never invents new layouts.

<details><summary>Details</summary>

- **The view rule goes in the page registry** (F119 criterion 5), so a routed question and a typed URL get the same view.

- **One registry entry per shelf**, with an id, its filters and a URL. This is F119 criteria 4 and 5: Explore can be reached by date, category and place.
- "Anything fun Saturday near Midtown?" opens Explore narrowed to Saturday and Midtown. The time shelves narrow to that day, the collection shelves to that place, and empty ones drop out.
- **"See all" on a shelf is a deep link**, so the router can open "Deals this week in Midtown" directly.
- **F120 later:** chat answers render the same shelf and card components, which fits F120's "nothing invented" criterion.

</details>

## Conflicts with recorded rulings

**Two rulings would change:**
- **The 2026-10-18 card rule (#922):** the post card's first line becomes kind · when · where, built from fields, instead of the first line of the body.
- **The 2026-09-15 "one staleness number" ruling:** it needs a clarifying line saying that shelf life (when a post ends) is not staleness (when something goes quiet).

The rest fit as they stand.

<details><summary>Details</summary>

| Ruling | Effect |
|---|---|
| No chips or pills; principle 10, no controls on the results surface [always] | **Fits.** Shelf names are headings, not controls, and "See all" is a quiet text link. Airbnb's tab bar is rejected for this reason. |
| 2026-09-19: collections are never a row of controls beside results | **Fits.** Collections become shelf headings, which are not controls. |
| 2026-10-18 card rule (#922): Page cards 80/20 image-led, post cards 60/40 text-led | **Page cards fit**, at the shelf width that already exists (78% of the screen, at most 20rem). **Post cards change:** the first line becomes the field-built lead line instead of "date line + first line of the body". |
| 2026-10-18 "adaptive area" | **Changes on the default view only:** the stack of shelves replaces the single adaptive grid there. Search results and "See all" keep today's grid. |
| 2026-09-12: "Browse is everything", inclusion by default | **Already narrowed for posts** by F059 criterion 8 and #314, under which past posts drop out. Shelf life narrows it further for timely posts only. Pages are always included. |
| 2026-09-15: staleness is one number, 90 days, sort last and never hide | **Needs a clarifying line.** The staleness rule is about things that go quiet (Pages); shelf life is about posts that have ended. Quiet Pages still sort last and are never hidden. |
| 2026-10-12: Find and Discover | **Fits.** These shelves are Find; learned or promoted shelves wait for Discover. |
| Find ordering: place, time, declared interests, community response; never favour an item for its follower count | **Fits, with a clarifying line.** Putting the member's own follows first uses their deliberate choice, like a declared interest. It never favours a Page for how many followers it has. |
| 2026-09-17 follow = "get updates"; 2026-10-25 push for followed Pages | **Fits.** Followed-first is the same promise, kept on screen. |
| 2026-10-04: Home rows (F098) | **Fits.** Home and Explore share the shelf components. |
| 2026-10-10: every sample opens with "Sample" | **Kept on the Page.** On the card, "Sample" appears once, in the lead line. |
| 2026-10-05: the map's mix | **Unaffected.** |

</details>

## Also added to IMAGINE

**"Asked for, not here yet"** (unmet asks shown to the community) and **teaching the ask** (example asks on the Ask bar). Detail: `planning/research/asked-for-not-here-2026-10-27.md`.

### Vouching

A member without a Page posts about a place they love (a sale, a great meal, the best date-night spot). It's in IMAGINE as an idea to explore, with precedents and open questions. It's not part of this call.

## Your call: how the shelf view is arranged

All three keep the same top two pieces: the followed shelf first, then its end marker.

- **A — Then time shelves, then collections (App Store and Facebook Events).** Timely things stay on top, and categories are still in view; reaching a category takes a scroll.
- **B — Then collection shelves only, each sorted soonest first (Netflix by genre).** The simplest category scan, but timeliness is hidden inside each row.
- **C — Then one mixed timeline sorted by time, with categories reached only by asking.** The closest thing to a feed, but categories disappear from the wide-open view.

**Recommend A.** It's the well-worn shape, it shows the timely items and the categories you asked for, and it gives the Ask bar one view to open.
