# Explore: shelves and shelf life

**Explore should work like the App Store: categories run top to bottom as shelves, the items in each run left to right, and timely shelves (today, this weekend, deals, Wonders) sit above the lasting ones (Pages by collection).** Every post gets a shelf life by kind and leaves Explore when it ends, but stays on its Page and in search.

**Your one call:** how the shelves are arranged (A, B or C, at the bottom). I recommend **A**.

*The PM, 2026-10-27:* "the categories are top to bottom and then the options in each category are left to right … the posts are timely and they need to be displayed in a timely manner and right now what we're showing is everything for all time and that's a little bit too much."

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

## 2. Categories before data

**Seven shelves at most on a phone screen stack: four timely shelves (Today, This weekend, Deals this week, Count me in) above three or more collection shelves of Pages (Food & drink, Makers, Farms, and so on), plus "New here."** Time and post kind decide the timely shelves. The Page's main collection decides the lasting ones. An item shows once per screen, and a shelf with nothing on it doesn't appear.

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

**Proposed shelves, top to bottom:**

| # | Shelf | What goes in it | Order inside |
|---|---|---|---|
| 1 | **Today** | Events and openings on now or later today | Soonest first |
| 2 | **This weekend** | Events Friday to Sunday (this week, Monday to Thursday) | Soonest first |
| 3 | **Deals this week** | Deals and offers that haven't ended | Ending soonest first |
| 4 | **Count me in** | Open Wonders | Closest to its goal first |
| 5 | **From Pages you follow** (signed in) | News from followed Pages | Newest first |
| 6+ | **One shelf per collection** with four or more Pages, using about seven groups of the current eleven collections: **Food & drink** (with bakery), **Makers** (goods, crafts, art and print), **Repair & trades**, **Farms** (farm, ranch, farm stay), **Community & volunteer**, **Arts & culture**, **Outdoors** | Pages, by the main collection the owner picked | Nearby, then recently active |
| last | **New here** | Pages created in the last 30 days | Newest first |

**How an item is placed:**
- Shelves are filled from the top, and an item lands in the first shelf it qualifies for.
- A Page goes in its main collection only.
- Each shelf shows about 10 to 12 items plus a quiet "See all" text link, which opens the full list as today's grid.

**How many shelves:** the four timely shelves plus up to three collection shelves on first load. More collection shelves load as the member scrolls. Every empty shelf is absent, which F091 already does for the "What's happening" rows.

**Samples:** samples are the unclaimed Page's own advertisement, not something timely. One sample per unclaimed Page goes on Explore, rotating, never three at once, and at most one in four cards on any shelf. All three stay on the Page.

**Find, Discover and Home:**
- **These shelves are Find.** They're ordered by place and time, with your declared interests and community response. Nothing is ever paid or learned from your views.
- **Discover, later:** may add learned shelves such as "Because you follow…" and a marked promoted slot, under the 2026-10-25 rulings.
- **Home:** Home was ruled on 2026-10-04 (F098) as Tonight, This weekend, New this week and a wildcard row. That's already a shelf design, so Home and Explore should share one set of shelf components.

</details>

## 3. Shelf life

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
| Recurring series | Only the next date shows | Meetup |
| Sample | One per unclaimed Page, as above | none |

**Where an expired post goes:**
- It stays on its Page under a "Past" section, as Meetup and Google do.
- It stays in search when the words ask for the past ("last week", "past events").
- It stays in the member's own You list if they responded to it.
- Nothing is deleted, which keeps the staleness ethos: nothing vanishes without a trace.

**How it leaves:** it's computed when the page loads, from the dates, the way it is today. No scheduled job.

</details>

## 4. Why the samples look noisy

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

## 5. Fit with chat-first

**A shelf is a named, linkable query (kind, time, place), so the Ask bar (F119) can open Explore with the right shelves already narrowed, and chat as home (F120) can show the same shelves and cards inline.** Shelves are the stable building blocks that chat combines and narrows. Chat never invents new layouts.

<details><summary>Details</summary>

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
| 2026-10-04: Home rows (F098) | **Fits.** Home and Explore share the shelf components. |
| 2026-10-10: every sample opens with "Sample" | **Kept on the Page.** On the card, "Sample" appears once, in the lead line. |
| 2026-10-05: the map's mix | **Unaffected.** |

</details>

## Your call: how the shelves are arranged

- **A — Time shelves first, then collections (App Store and Facebook Events).** Timely things are always on top; reaching a category takes a scroll.
- **B — Collection shelves only, each sorted soonest first (Netflix by genre).** The simplest category scan, but timeliness is hidden inside each row.
- **C — "This week" shelves on Explore, with Pages by collection moved to a separate directory.** The cleanest split between lasting and timely, at the cost of a new surface and search split in two.

**Recommend A.** It's the well-worn shape, it puts the timely items first, which is your point, and it keeps one surface for the Ask bar to open.
