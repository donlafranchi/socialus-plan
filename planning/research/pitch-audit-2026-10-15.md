# Pitch audit: does SocialUs work for the member? (2026-10-15)

**Bottom line: the pitch's two headline promises, timely announcements and "the app works for you", are each about half built. Nothing a member does (follow, save, interests) brings anything to them yet; they still have to come and look. Start by fixing post expiry (half a day). Then let members choose interests as a filter, then send a weekly "your week" email.**

Method: socialus.org signed out at 390px; signed-in member and Page owner on a local copy with seeded data at 390px (production sign-in needs the PM's inbox); then code and schema on `main` at `56d9792`. **V** = seen in the app or code. **A** = assumed. Test Page and post were deleted afterwards.

## Ratings (HAVE / WANT at soft launch, 0–4)

| # | Capability | HAVE | WANT | Gap | |
|---|---|---|---|---|---|
| 1 | Timely Page announcements | 2 | 4 | **2** | V |
| 2 | Discovery without searching for a Page | 3 | 4 | 1 | V |
| 3 | Results driven by the member's own signals | 1 | 3 | **2** | V |
| 4 | Member control over what shows | 1 | 3 | **2** | V |
| 5 | Staying current without following many | 2 | 4 | **2** | V |
| 6 | Page owners served; the Page is the product | 2 | 3 | 1 | V |
| 7 | Yelp/Google/TikTok/FB/IG comparisons hold up | 2 | 3 | 1 | V (felt) |

**Ranking does not serve the platform. V:** no engagement, paid or attention signal anywhere in Explore's order. The gap is the other way round: almost nothing serves the member's own signals yet.

## How, today

**1. Timely announcements**
- Owner: Page → Announce → type → "Add a date and time" → date, start, end → Announce. About 7 taps, one screen. **V**
- Breaks: a post leaves Explore when it **starts**, not when it ends (a market from 8 to 2 is gone at 8:01). **V** (`browse_feed`: `starts_at >= now`, `ends_at` ignored)
- Breaks: no multi-day span (a "Sat and Sun" special had to be Saturday only); no "special/holiday" kind; a post with no date never expires. **V**
- Breaks: no schedule-to-publish-later. Weekly repeats are behind an off flag, and no job creates the occurrences. **V**
- Signed out, every post reads "The details are for members and followers of this Page". **V** (socialus.org)

**2. Discovery without searching**
- Member: open Explore (0 taps) → "What's new since you were here" (6 cards), then up to 100 Pages in the metro. **V**
- Breaks: posts moved behind Filters → Show → Updates (3 taps); on prod, `?view=updates` turns into the search box reading "updates". **V**
- Breaks: in Updates one post appears up to 4 times (happening rows plus the list). **V** (local)
- Breaks: search only covers the 100 rows already loaded. Filters offer only Any time / This week / This weekend and Updates; no kind, interest or town. **V**

**3. The member's own signals**
- Used: metro (from zip), recency, follows (Following row, Updates view only), and "seen" in a cookie per browser. **V**
- Not used: interests (`member_interests` and an add action exist, with no screen to set them); saves and RSVPs (`item_responses`, no screen, nothing reads it). **V**

**4. Member control**
- /you offers: name, metro, zip. Nothing else. **V**
- Missing: interests, mute or hide a Page, pin, notification level, a saved neighbourhood (`?area=` is per visit). **V**

**5. Staying current without following many**
- "What's new since you were here" is the only push-like help, and it lives in a cookie per browser. **V**
- Following a Page delivers nothing: no email, push or in-app notice to members. A saved-search digest was planned (`member_saved_searches`), but its worker was never built. **V**

**6. Page owners**
- Create: about 14 taps (kind → Start → name, where, description, tag → agree → Publish). Clear checklist. **V**
- Breaks: owners see no answer to "who will see this and when". The audience switch has only "Anyone", because follower delivery was cut. There is a follower count, and nothing on views. **V**
- Breaks: hours are hidden by a flag; nothing approves a claim, so an unclaimed Page cannot be handed to its owner. **V**
- Minor: choosing "It moves" still showed "East Sacramento" as the location. **V** (local)

**7. Comparisons**
- Yelp/Google: holds only partly. Pages exist, but there are no hours and no reviews, and signed-out visitors see no post details, where Yelp and Google show everything signed out. **V**
- TikTok/IG ("works for you"): doesn't hold yet. The app doesn't decide for the member, but nothing comes to them either. **V**

**Built but not wired:** `member_interests` and its add action; `item_responses` (save/RSVP); `post_series` repeats (flag off, no job); the followers-only audience; `member_saved_searches` digest; `member_notices` (in-app, used only for hidden content); hours (flag off); claim approval (no handler). **V**

## First small builds (smallest first)

**A. Posts last until they end, and can span days. Start here.**
- What: a post stays in Explore and "What's new" until its end time, and an end can fall on a later day (Sat–Sun special).
- Hours: 4–6, including a migration (the PM applies it).
- Touches: new migration replacing `browse_feed` (`coalesce(ends_at, starts_at)`); `src/lib/browse/lead.ts` (tonight/this weekend); `AnnouncementFields.tsx` (end date). Table: `page_posts` (no new columns).
- Moves: #1 2→3, #7 +½.
- Unlocks: a "special" label and expiry for undated posts; a digest can trust dates.
- Path: well-worn. Google Business Profile offers and events, Facebook events and Eventbrite listings all run from start to end (links not checked this session).

**B. "My interests": the member picks, Explore filters.**
- What: pick interests on /you (and one optional step after sign-up); a "My interests" choice in Filters narrows Explore to matching tags. It is a filter, not a ranking, so Find keeps its place-and-time order. Private to the member.
- Hours: 8–12. No migration (table and action exist).
- Touches: `src/app/you/page.tsx`, `src/actions/member/interests-add.ts` (plus remove), `src/lib/onboarding/interest-vocab.ts`, `src/lib/browse/filters.ts`, the filter sheet. Table: `member_interests`.
- Moves: #3 1→2, #4 1→2, #2 +½.
- Unlocks: the digest (C) can follow interests as well as Pages; Discover later has a cold start.
- Path: well-worn. Interest pickers at Pinterest, Meetup and Eventbrite (links not checked this session). Needs new copy, so it goes to the PM.

**C. "Your week": a weekly email of what's on (opt-in). Flag: 2–3 days.**
- What: Thursday email of this weekend and next week from followed Pages and the member's interests in their metro, with one-tap pause and unsubscribe. Owners can be told "your followers get this in Thursday's email".
- Hours: 16–24: email sending, a GitHub Actions cron, a preference column, an unsubscribe link, F114 exclusion.
- Touches: new `scripts/digest/`, `.github/workflows/digest.yml`, a migration adding `members.digest_frequency`; reads `page_posts`, `group_memberships`, `member_interests`.
- Moves: #5 2→3, #6 2→3, #4 +1, #7 +½.
- Unlocks: the honest answer to "who will see this and when"; follower delivery without a feed.
- Path: new territory (emails members, member trust, copy). Precedents: Front Porch Forum's daily issue, Meetup's weekly digest, Eventbrite's weekly email.

**Start with A:** smallest, no copy or ruling needed, and it fixes a bug that makes the pitch's headline feature fail on the day it matters. In production it hides 261 of 420 live posts right now (below). B and C both depend on dated posts being right. B also needs the seeder to tag Pages first (adjustment a2), or the filter matches nothing.

## Content reality check (production, read-only totals, 2026-10-15)

- Pages: 149 live; 137 unclaimed (seeded), 12 others (builder and test Pages; no outside owner yet). 33 places covered. **V**
- Posts: 420 live; 408 are seeder "Sample" posts (3 per Page: event, deal, last-minute), 12 written by a person. **V**
- Dated: 410 of 420 have a start and an end; 135 Pages have a post still to come; 62 posts start this weekend. **V**
- **Hidden while running: 261 of 420** (all 136 deals, which run 6–9 days, and 125 last-minute posts). They have started, they haven't ended, and Explore drops them at the start. **V**
- Interests and categories: 9 of 149 Pages carry any tag; 0 posts are tagged; 0 Pages have a category. **V**
- Hours: 1 Page of 149. **V**

| # | Capability | Enough content to judge? | Low rating is a… |
|---|---|---|---|
| 1 | Timely announcements | Yes: 408 dated samples, but only 12 real posts | **Feature gap** (expiry hides 62%); content gap for real owner posts |
| 2 | Discovery without searching | Yes: 149 Pages, 33 places | Small feature gap |
| 3 | Member's own signals | **No**: Pages carry no interest tags | **Both**: an interest feature would match nothing today |
| 4 | Member control | No, for interests (same reason) | **Both** |
| 5 | Current without many follows | Partly: dated samples exist, no real follows to deliver | **Feature gap** (nothing is delivered) |
| 6 | Owners served | No: no outside owner, and a claim can't complete | **Both** |
| 7 | Comparisons hold up | No: every post says "Sample… not a real offer"; 1 Page has hours | **Content gap** first, then the signed-out gate |

## Our rubrics against the pitch

| # | Capability | Seeder rules (THEMES.md, #353/#517/#542/#556, #788) | MVP grading (approved scenarios, 52 launch-blocking Issues) |
|---|---|---|---|
| 1 | Timely announcements | Partly: 3 dated samples, rolled forward; not real, none scheduled | Partly: F072.3, F072.6, F074; F072 rules out scheduling |
| 2 | Discovery | Partly: 10 a day, themes, at least 5 towns | Yes: F059.1–4, F091.1–7, F104.1–2 |
| 3 | Member's own signals | No | Partly: F059.3 bars payment and attention ranking; interest signals only in drafts F112/F113 |
| 4 | Member control | No | Partly: area only (F105, F059.6–7); no mute, pin, interests or notification level |
| 5 | Current without many follows | Partly: samples feed What's happening | Partly: F091, F065.1; follower delivery is "beta-partial" |
| 6 | Owners served | Partly: claim, instant remove, credited own-site photos | Partly: F072.1–2, F056, F099 |
| 7 | Comparisons hold up | Partly: Yelp and Google appear only as claim precedents | No: no criterion tests it |

- Bundle b1 is retired (2026-10-05). The beta grade is now the "Beta 11-06" milestone: 52 launch-blocking Issues, 3 open, none on capabilities 3, 4 or 7. **V**
- The daily seeder's rules all live in `scripts/unclaimed/THEMES.md`. No separate prompt file was found. **V**

## Proposed adjustments

**(a) What the builder seeds and posts.** All are well-worn tweaks to the seeder, except a4.
- a1. Spread sample dates over the coming 14 days, with at least one per Page landing Fri–Sun. A deal may span days. Moves the judging of 1 and 5.
- a2. Tag every new and existing unclaimed Page with 1–2 of the 12 interest tags, and its samples with the same. Moves the judging of 3 and 4; B needs it.
- a3. Coverage rule per daily batch: at least 5 towns and at least 4 interest tags, logged in `ADDED.md`. Moves the judging of 2–4.
- a4. **New territory:** where the business's own site lists a real dated event or seasonal special (Apple Hill harvest, holiday hours), post it as real, credited and linked, instead of a "Sample". This is the only way capability 7 can be judged before owners arrive, and it touches member trust and posting on a business's behalf.

**(b) MVP grade card: soft-launch pass bars.** New territory: the PM sets the bars. Today's state is in brackets.
1. An owner posts a dated special in at most 8 taps; it shows from posting until it ends, and can span days. [fail: hidden at start]
2. A new member with a zip sees at least 6 things happening this week on first open, with 0 taps. [pass when A lands]
3. Nothing the member didn't give orders their results; at least one signal they gave (follows or interests) visibly changes what they see. [fail]
4. From You, in at most 3 taps, a member sets or clears area and interests. [fail: area only]
5. A member following up to 5 Pages learns this week's posts from all of them without opening each Page. [fail]
6. Before posting, an owner sees who will see it and where; a claim can be completed. [fail]
7. On a phone, signed out, the PM can find a Page and see what's on and when, as on Yelp or Google. [fail: details gated]

## cap-8, Honest origin (added 2026-10-16)

The prompt was Etsy: a handmade marketplace where mass-made goods posed as handmade after its 2013 rule change and 2015 IPO. The PM's direction: no badge for everything; owners tell their own story and link their socials; small-batch producers are worth supporting; members vouch for makers and producers (for Pages, never for other members).

**Precedents: how a vouch is earned, guarded and shown**
- **Nextdoor Faves.** A Fave is "a verified neighbor… willing to vouch". It is earned by being nearby, guarded by address-verified accounts, and shown as a count on the business page. More Faves rank higher in search, which we would not copy on Find. ([Nextdoor](https://business.nextdoor.com/en-us/blog/how-to-make-the-most-of-nextdoor-neighborhood-favorites), [awards](https://about.nextdoor.com/press-releases/nextdoor-celebrates-businesses-loved-by-locals-with-7th-annual-neighborhood-faves-awards)) [V]
- **Etsy reviews.** Earned by a purchase: a review is tied to a completed order, needs an account, opens a limited window, and is blocked while a case is open. ([guide](https://crosslist.com/blog/how-to-leave-a-review-on-etsy)) [S]: secondary sources only.
- **Yelp check-ins.** These were shown on reviews as a visit count to add trust, and frequent visitors became "regulars". They are tied to a visit, but they were a 2010 feature, and whether they are still current is unconfirmed. ([TechCrunch](https://techcrunch.com/?p=136195)) [S]
- **Google Local Guides.** Points reward volume, and practitioners report unvisited and bought reviews as the result. This is the anti-pattern: never reward vouching itself. ([forum](https://localsearchforum.com/threads/local-guides-are-posting-bogus-photos-reviews.50987)) [S]
- **Faire's "handmade" value tag.** It means made or designed by the brand's own team, with no outside production partner. The brand self-attests and is responsible for complying. It is the closest precedent for an owner tag. ([guide](https://fitsmallbusiness.com/how-to-sell-on-faire)) [S]
- **Front Porch Forum.** It has no endorsement feature; neighbours recommend businesses in ordinary posts, under real names and addresses. ([Wikipedia](https://en.wikipedia.org/wiki/Front_Porch_Forum)) [V]
- **Pattern:** the well-worn shape is one verified local person, one vouch, shown as a count. Earning it by a purchase or visit needs commerce or check-ins, which we don't have. Ranking by vouches (Nextdoor, Google) is what we refuse.

**What exists today** (production totals; code on `main`)
- Linked socials: `groups.social_links` (Instagram, Facebook, TikTok, X, YouTube, Bluesky, website), https only. 111 of 157 Pages have at least one. **V**
- Story: `groups.description`, 80 characters or more on 153 of 157 Pages, but the seeder wrote it on unclaimed Pages ("Claim this Page to tell your own story"). **V**
- Page tags: `page_tags` exists, with 9 Pages tagged. There is no small-batch, handmade or origin field anywhere. **V**
- An origin badge already exists: the "Locally Owned" claim (F037), where the owner self-asserts a ZIP and a badge shows. It conflicts with "no badge for everything"; it should be kept, folded in or retired. **V**
- `item_responses` (interest, rsvp, follow, save, pledge, purchase, support) hangs off legacy `items`, not Pages or posts, and nothing in the app writes to it. The only signal a member can give a Page today is a follow (`group_memberships`). **V**
- Reports and self-correct-first: report answers already include `mistake` and `fix_and_repost`, and `member_notices` has a `courtesy` kind. **V**

**Smallest soft-launch version (recommended)**
- **Vouch**, on a Page: "I vouch for them". On a Page tagged small-batch, it reads "They really make it themselves". One per member per Page, withdrawable.
- **Who can vouch:** a signed-in member in the Page's metro who has followed the Page for at least 7 days. A Page's own managers can't vouch for it, and test accounts are excluded (F114). Following is the only signal that exists today, and the wait slows brigading the way Etsy's order link does.
- **Shown:** "Vouched for by 12 members" to everyone. A first name shows only if that member chose to show it when vouching ("Show my first name"; off by default). That keeps to member-to-member privacy and sharing being opt-in. There is no score on any person, and vouches never order Find.
- **Small-batch producer:** one optional owner tag, defined the Faire way (made or grown by the owner or their own team, no outside production). It is self-attested on the editor.
- **Call it out:** Report → "This claim isn't true". The owner gets a courtesy notice first (self-correct first). An upheld report removes the tag, and nothing more is done automatically.
- **Who's behind it:** the About block (story plus socials) moves to the first screen of a Page, so it is 1 tap from any card.
- **Hours:** 16–22 (2–3 days, flagged). It covers:
  - a migration: a `page_vouches` table with RLS where a member reads only their own rows and others get counts only
  - a `page.vouch` handler and its `links.ts` entry
  - the button and count
  - the small-batch tag and its editor toggle
  - the report reason
  - the F114 exclusion and tests
- **New territory for the PM:** showing first names at all; the 7-day follow wait as the bar for earning a vouch; the small-batch definition and its copy; whether "Locally Owned" stays as a badge.

## Proposed homes (draft text below; homes not edited until the PM reviews the grade card)

1. **Pitch** → socialus-plan `PRINCIPLES.md`, anchor `#pitch`, carrying `changed:`. It holds the 8 capabilities as `cap-1`…`cap-8` and is the only copy.
2. **Grade card** → a new approved scenario, "Pitch grade card" (F116 if free), horizon now. Its 7 criteria are the bars above, plus `[binds tiers=planning,code]` and `[for now]`, so they roll into tickets, the criterion roll-up and "lost since last look".
3. **Builder rubric** → socialus-web `scripts/unclaimed/THEMES.md`: a1–a3 as rules, mapped to `cap-1`…`cap-5`.
4. **Pipeline hook** → one line in socialus-ops. It goes after the Gate bullet in `PIPELINE-build.md` § 5 Scenario, because that is where approval actually happens, not `PIPELINE.md`.
5. **Cascade** (about 5–7 hours) → no new tool. A `[derives pitch@<date>]` marker kind is added to socialus-plan `scripts/markers.py`, the same script that already fails the lint on stale `[binds]` constraints and already reads socialus-web lines. It fails and names each file whose `@` date is older than `#pitch`'s `changed:`. The planning agent or the weekly tend-docs pass opens one PR updating them, and only a changed pass bar goes to the PM. The dashboard adds one row, "pitch changed → N files updating", until green.

<details><summary>Draft text per home</summary>

**PRINCIPLES.md**
> - <a id="pitch"></a>**2026-10-15 — SocialUs works for the member; the member doesn't work for it.** `changed: 2026-10-16`. Pages say what's coming and when it ends; members see what's happening around them without endless scrolling, hunting for Pages or following hundreds of accounts. What a member sees is driven by signals they gave: interests, area, saves, attends, follows. An engagement signal is welcome when it serves the member; ranking that serves the platform at the member's expense is not. Capabilities: `cap-1` timely Page announcements · `cap-2` discovery without searching · `cap-3` results from the member's own signals · `cap-4` member control over what shows · `cap-5` current without following many · `cap-6` the Page is the owner's product · `cap-7` holds up against Yelp, Google, TikTok, Facebook, Instagram · `cap-8` honest origin: owners tell who they are in their own words and links, members who know them vouch for them, and a false claim can be called out; no badge for everything. *Example:* Etsy, a handmade marketplace whose listings filled with mass-made goods once growth outranked origin. *Why:* a local platform is only worth trusting if what a Page says about itself holds up, and the people best placed to say so are the members who buy from it.

**Scenario F116, "Pitch grade card"** (frontmatter as F091; `horizon: now`; `derives-from: PRINCIPLES.md#pitch @ 2026-10-16`)
> Acceptance 1–7 = the pass bars in (b), each opening with its `cap-n`. 8. `cap-8` From any card, a member sees who's behind a Page (story and links) in 1 tap, and can vouch or report a false claim in 2. Measures (dashboard, Page-level totals only): share of Pages with an owner-written story or linked socials; vouches per Page; false-claim reports upheld. Rulings: `- **2026-10-15 — The pitch is the MVP grade.** [binds tiers=planning,code surfaces=explore,announcements,you] [for now]`

**THEMES.md** (`derives-from: PRINCIPLES.md#pitch @ 2026-10-15`)
> - Dates (`cap-1`, `cap-5`): samples spread over the next 14 days, at least one per Page Fri–Sun; a deal may span days.
> - Interests (`cap-3`, `cap-4`): every Page and its samples carry 1–2 of the 12 interest tags.
> - Coverage (`cap-2`): each batch spans at least 5 towns and at least 4 interest tags; `ADDED.md` records both.

**PIPELINE-build.md § 5 Scenario, after Gate** (`derives-from: PRINCIPLES.md#pitch @ 2026-10-15`)
> - **Pitch test:** before approval, the scenario names which of `cap-1`…`cap-8` it moves, or says none, and passes the pitch's member-first test; one that moves a capability against the member goes to the PM.
</details>

## Questions only the PM can answer

- Should a signed-in member see posts from Pages they follow on Explore's default view, not only under Updates? (This reverses part of the 10-14 Explore ruling.)
- Is a weekly email to members acceptable at soft launch, and opt-in or on by default?
- Should signed-out visitors see a Page's public specials and events, as on Yelp and Google, instead of "sign in to see"?
- Does claiming an unclaimed Page need to work before owner outreach starts?
- The grade card's seven pass bars: keep, loosen or tighten?
- cap-8: may a vouch show the member's first name (opt-in), and is following for 7 days the right bar for earning a vouch?
- cap-8: keep, fold in or retire the existing "Locally Owned" badge, given "no badge for everything"?
- May the seeder post a business's real, dated events from its own site, instead of "Sample" posts (a4)?

**Next action: build A (posts last until they end), opened as a change Issue in socialus-web. Owner: Code agent, with the PM applying its migration. Then the PM reviews the grade card, and the homes are written.**
