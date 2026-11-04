# Organizing what people post: simple, flexible, then sorted by AI

**As of 2026-11-04** · Source: hand-written · Maintained by: hand

## Bottom line for Don

**Ask one question when someone posts: what kind is it? Everything else (the category and a few labels) is suggested for them, and they change it with one tap. Today the suggestion comes from a simple word match on one shared list. Later a small model (Claude Haiku) reads the words and the photo instead, at about $0.0002 a post.** It's how Facebook Marketplace, eBay, Shopify and Nextdoor's For Sale & Free work. Facebook built it because 7–9% of people gave up listing when they had to pick a category themselves.

- **Why the kind is the one choice:** it changes the form itself (a date for an Event, a price for an Offer, when it comes down). Google asks only this, from 3 kinds, and so does Nextdoor, from about 4.
- **What breaks today:**
  - Tags are a free-typed box that "behaves like a hashtag box". It splits the same thing into many words, so Explore's interest filters miss most posts.
  - Person posts have no Page to borrow tags from.
- **Your call:**
  - **A:** pick everything from short lists.
  - **B (recommended):** pick the kind; we suggest the rest; you confirm.
  - **C:** just write it; AI picks everything, the kind included.
- **Smallest first version of B, no AI:**
  - Replace the tag box with "Listed under: Gardening · Change", filled from the words and the Page.
  - Give person posts their 3 kinds.
  - Haiku slots in later behind the same line.
- *Don, 2026-11-04 (plan #270, option B):* "B is good for now although we need a way to help people organize what they're posting that is simple and flexible. Let's figure that out before implementing. Also in the end this would hopefully be auto categorized by something like Jev" (read as a small model, Claude Haiku).

Research only, no rulings. Person posts aren't built until you pick.

## 1. How others help people organize what they post

**The fewest choices that still sort well is one: the kind of post, from a handful. The category is suggested from the words and photo, and the person can change it. Everyone with a big category list suggests first; only Craigslist still makes you pick from 130+.**

<details><summary>Details</summary>

| App | What the poster picks | Suggested? | Can change? | Required? |
|---|---|---|---|---|
| **[Google Business posts](https://support.google.com/business/answer/7662907)** | Update, Offer or Event (3) | No | — | Yes |
| **Nextdoor** | A post type (message, event, poll, alert; about 4), then a category such as For Sale & Free or Lost & Found ([press](https://www.businessinsider.in/tech/how-to/how-to-post-to-nextdoor-and-communicate-with-your-neighborhood/articleshow/79534764.cms)); current composer not verified | [For Sale & Free](https://about.nextdoor.com/press-releases/nextdoors-genai-assistant-expands-to-for-sale-free-listings) (2024): AI suggests category, title, price and description from photos | Yes | Type yes |
| **[Facebook Marketplace](https://engineering.fb.com/2018/10/02/ml-applications/under-the-hood-facebook-marketplace-powered-by-artificial-intelligence/)** | Item, vehicle or home | A model suggests one of 29 top categories from the photo and words | Yes, "keep or change" | Yes |
| **[eBay](https://www.ebay.com/help/selling/listings/creating-managing-listings/adding-category-listing?id=4149)** | Nothing at first | Category "pre-populated" from the title; since 2023 [from a photo](https://innovation.ebayinc.com/stories/magical-listing-tool-harnesses-the-power-of-ai-to-make-selling-on-ebay-faster-easier-and-more-accurate/) | Yes | Yes |
| **[Shopify](https://help.shopify.com/en/manual/products/details/product-category)** | Nothing at first | Suggested from product details; saving confirms it | Yes | — |
| **[Etsy](https://www.etsy.com/seller-handbook/article/604203126614)** | One category by searching 6,000+ | Title help, not confirmed for category | — | Yes |
| **[Craigslist](https://www.craigslist.org/area/sfbay)** | A posting type (about 12), then one of about 130 categories | No | — | Yes |
| **Threads** | One topic tag, no # ([press](https://www.engadget.com/metas-threads-is-getting-searchable-topics-just-dont-call-them-hashtags-191915209.html)) | No | — | No |
| **Instagram Reels** | Up to 3 topics from a fixed list ([press](https://www.socialmediatoday.com/news/instagram-tests-new-add-topics-option-in-the-reels-upload-process/631189/)) | No | — | No |
| **Reddit** | Flair from a list each community sets; can be required ([mods](https://lr.in.psf.lt/r/modnews/comments/fah9mc/post_requirements_post_flair_support_on_old)) | No | — | Per community |

**What it adds up to:**
- **One required choice, kept tiny:** Google 3, Nextdoor about 4, Threads 1 tag.
- **Big lists are suggested, never picked from scratch:** Facebook, eBay, Shopify, Nextdoor. Facebook is the only one that says why: people abandoned the listing.
- **Tags without the #:** Threads chose one tag per post, so tags describe "communities" rather than "engagement hacking" (Mosseri). That matches our 2026-10-12 ruling.
- **Hick's law** (more choices take longer) is the usual argument for short menus, but HCI researchers say it rarely predicts interface results well ([paper](https://hal.inrae.fr/DIVA/hal-02867301v1)). The stronger evidence is Facebook's abandonment figure.

</details>

## 2. Our case: where "simple and flexible" breaks today

**The kinds are fine. The labels underneath them aren't: tags are typed freely, so "bakery", "baked goods" and "pastries" never meet, and Explore's interest filters match only posts tagged with the exact interest name. Person posts make it worse, because they have no Page to inherit from.**

<details><summary>Details</summary>

**What exists** (verified in code):
- **Page post kinds:** Event, Update, Offer, Limited, Reminder, Hiring, Proposal. The kind sets the form and the shelf life.
- **Person post kinds** (plan #270, option B): Lost & found, Free / for sale, Ask a neighbour. Not built.
- **12 interest labels:** Farmers markets, Live music, Food & drink, Crafts & makers, Gardening, Kids & family, Fitness & outdoors, Arts & culture, Volunteering, Local business, Sustainability, Neighborhood life. Explore's category filter reads these labels as tags.
- **Tags:** a free text box ("Tags (optional)") on the post and the Page. The code describes it as a box where "creators create their own tags — the vocabulary starts empty and fills itself", and "it behaves like a hashtag box". A post with no tags carries its Page's.
- **A Page category:** free text, up to 80 characters.
- **Shelves and search groups** (for example Live music: "Next 7 days", then venue kinds) need clean keys to fill.

**Where it breaks:**

| Problem | Effect |
|---|---|
| Free-typed tags | The same thing ends up under many words. Shelves and filters miss posts, and search leans on synonyms to cope |
| Explore's interest filter matches only tags equal to the 12 labels (as read from the code) | A post tagged "sourdough" never shows under Food & drink |
| A tag box that acts like a hashtag box | Runs against 2026-10-12 (members never type hashtags), even though the # is dropped |
| Person posts have no Page | Nothing to inherit tags from; an untagged lost dog sorts nowhere |
| Kinds overlap | Free / for sale vs Offer; Ask a neighbour vs Update. Fine as long as person posts and Page posts each show only their own kinds |
| Page category is free text | Search groups by venue kind can't trust it |

**What "simple and flexible" should mean for us:**
- **Simple:** one tap that must happen (the kind); nothing else is required.
- **Flexible:** anything written in plain words still lands somewhere sensible, and the poster can always change where.

</details>

## 3. Auto-categorizing with a small model

**After someone posts, Haiku reads the words and the photo and returns a category and up to 3 labels from our own list, with how sure it is. The poster sees "Listed under: Gardening · Change". It costs about $0.0002 a post, never slows posting down, and falls back to the word match if it fails. The same pass can flag likely problems for the existing review, without deciding anything.**

<details><summary>Details</summary>

**How it would work:**
- **What it reads:** the kind, the headline and text, the Page's category if it's a Page post, and the first photo at 512 px. Nothing about the person.
- **What it returns:** one of the 12 labels, up to 3 finer labels from a list of about 60 under them that a person keeps (never the model), each with a confidence. It may also flag "this reads like a different kind" (an Offer that's really an Event).
- **When:** after the post is saved, like the AI first-read on reports does today (the code already calls Haiku and Sonnet this way). Posting is never held up.
- **What the poster sees:**
  - Before the AI result arrives: the word match ("Listed under: Gardening · Change").
  - When the model is sure: it replaces the word match quietly.
  - When it's unsure: the word match stays.
  - Whatever the poster picks is pinned and never overwritten.

**Accuracy to expect:**
- Large product catalogues get the first guess right about 81–85% of the time from titles alone:
  - Rakuten's 2018 challenge: best score 0.85 ([results](https://sigir-ecom.github.io/ecom2018/data-task.html));
  - one study with 28,000 categories: 81% ([COLING 2016](https://aclanthology.org/C16-1051.pdf)).
- Models used without examples trail trained ones, most of all on unusual label sets ([Bucher & Martini 2024](https://arxiv.org/abs/2406.08660)).
- **Our list is tiny by comparison: 12 labels, about 60 finer ones.** So expect higher at the top level and lower on the finer labels. That's an inference, not a measured result.
- **Measure it first:** a bake-off on 100 hand-labelled posts, the way bug triage was chosen (2026-10-06). Ship only if the top-level label is right on at least 90 of them [guess].

**Cost**, from [Anthropic's pricing page](https://platform.claude.com/docs/en/about-claude/pricing) (checked 2026-11-04). Haiku 5.5, prompts under 100,000 tokens: $0.10 per million tokens in, $0.50 out, cache hits $0.01, Batch half price.

| Per post | Tokens | Cost |
|---|---|---|
| Instructions and our label list, cached | ~1,500 | $0.000015 |
| Headline and text | ~300 | $0.00003 |
| Photo at 512 px | ~350 | $0.000035 |
| Answer | ~120 | $0.00006 |
| **Total** | | **about $0.00014** (about $0.0002 with an occasional cache write) |
| 1,000 posts | | about $0.15–0.40 |
| Back-filling every existing Page and post, by Batch | | a dollar or two |

(The October categorization research priced Haiku 4.5 at $1 / $5. Haiku 5.5 is a tenth of that.)

**Speed:** it runs after saving, so nobody waits. Expect a second or two for the result [estimate; measure in the bake-off].

**When it fails:**
- **Timeout or error:** the word match stands, and a background retry runs later.
- **Unsure:** the word match stands.
- **Wrong:** one tap to change it. A "wrong category" count on unclaimed Pages goes to staff, as the October design said.
- **Never:** it never blocks a post and never hides one.

**Help for moderation:**
- The same pass can say "looks like a phone number in a lost-and-found post", "not local", or "might break the kids-and-pets rule".
- A flag only sends the post to the existing first-read and review (F100–F102). It never removes anything itself, because a person decides.

**Privacy:**
- **What's sent:** the post's text and first photo, plus the Page's category for a Page post.
- **What's not sent:**
  - no name, member id, email or location finer than the market;
  - phone numbers stripped before sending (emails are already refused in posts).
- **What we keep:** the label and confidence, never the prompt.
- **The privacy page says plainly** that an AI helper reads posts to sort them.
- Anthropic's commercial terms say API inputs aren't used for training by default. Confirm retention before launch [from memory, not checked today].
- It's the same data the post already shows publicly, and the same kind of call moderation already makes.

</details>

## 4. Options

**I recommend B: pick the kind, we suggest the rest, one tap to change. It's the Marketplace, eBay and Shopify pattern, it works before any AI exists, and Haiku drops in later without changing the screen.**

<details><summary>Details</summary>

| | **A. Pick from short lists** | **B. Pick the kind; we suggest the rest** (recommended) | **C. Just write it; AI sorts everything** |
|---|---|---|---|
| What the poster does | Kind, then one of the 12 labels, then optional labels | Kind (one tap), then writes; sees "Listed under: …" and can change it | Writes; sees the kind, category and labels and confirms |
| Required choices | 2 | 1 | 0 (one confirm) |
| Works without AI | Yes | Yes (word match) | No |
| Sorting quality | Depends on people picking well | Good with the word match, better with Haiku | Best when right; a wrong **kind** breaks dates, shelf life and reminders |
| Fits "simple and flexible" | Simple, not flexible | Both | Flexible; simple only when the AI is right |
| Precedent | Craigslist, Google (kind only) | Facebook Marketplace, eBay, Shopify, Nextdoor For Sale & Free | eBay's photo listing, Nextdoor's AI draft |
| Path | Well-worn | Well-worn | New territory (AI decides what the form is) |

**Smallest first version of B, before the AI step:**
1. **Kinds:** person posts show their 3 kinds and Page posts their 7. Never mixed.
2. **One shared list:** the 12 labels plus about 60 finer ones, each with a few plain words that point to it ("sourdough", "bread", "pastries" → Food & drink · Bakery). A person keeps it.
3. **The tag box goes.** In its place, "Listed under: Food & drink · Bakery · Change", filled by matching the headline and text against that list, then the Page's own labels. Change opens the 12 labels with their finer ones beneath; pick up to 3.
4. **Nothing matches:** it says "Listed under: Neighborhood life · Change" for a person post, or the Page's labels for a Page post.
5. **Explore, shelves and search** read these labels instead of free tags. Existing tags are mapped once.

**Then:** Haiku replaces the word match behind the same line, after the 100-post bake-off passes. Its moderation flags feed the existing review.

**What it costs to build** [estimates]:
- First version: about 16 h (the list and word match 6, composer line 4, Explore and shelves read the labels 4, mapping existing tags 2).
- The Haiku step: about 10 h more, plus the bake-off.

**Copy note:** "Listed under" and "Change" are new words on screen, so they come to you with the build.

</details>
