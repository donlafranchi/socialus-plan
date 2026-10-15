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

**Start with A:** smallest, no copy or ruling needed, and it fixes a bug that makes the pitch's headline feature fail on the day it matters. B and C both depend on dated posts being right.

## Questions only the PM can answer

- Should a signed-in member see posts from Pages they follow on Explore's default view, not only under Updates? (This reverses part of the 10-14 Explore ruling.)
- Is a weekly email to members acceptable at soft launch, and opt-in or on by default?
- Should signed-out visitors see a Page's public specials and events, as on Yelp and Google, instead of "sign in to see"?
- Does claiming an unclaimed Page need to work before owner outreach starts?

**Next action: build A (posts last until they end), opened as a change Issue in socialus-web. Owner: Code agent, with the PM applying its migration.**
