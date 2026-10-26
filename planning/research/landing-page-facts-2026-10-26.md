# Landing page facts — what the app does today (2026-10-26)

**Bottom line: a landing page can truthfully show "find what's near you this week, follow it, get reminded, go" and "post a weekly thing once and your followers hear about it." It can't promise RSVPs, co-hosts, messaging, a market application or a contact address, because none of those exist yet. Sacramento is the only open market.**

Source: socialus-web `origin/main` @ 6470159 (2026-10-26). Paths are relative to socialus-web. "Reachable" means a member can get there by tapping from Explore or You, with no flag or direct URL needed.

---

## 1. Discovery → attendance

**Shipped and reachable**
- One concrete path, screen by screen:
  1. **Explore** (`/`, which redirects to `/explore`, `src/app/page.tsx:17`). Opens on the nearest ring with about 24 things on this week (Q5).
  2. Tap a card to open the **Page** at `/g/<id>` (`src/app/g/[handle]/page.tsx`).
  3. **Follow** (`FollowPageButton`, `ShopPublicPage.tsx:23`). Its posts then come to the member in the app, plus opt-in push from `/you/notifications`.
  4. On a dated post: **Remind me** ("Just this one" / "Every time" for a weekly post), **Add to calendar** (.ics), and **Tickets** when the post has a link (`PagePosts.tsx:658-680`). "How to find us" is a one-line meeting spot (`PagePosts.tsx:650`).
  5. **Directions** from the Page's Where block opens Apple Maps on iPhone and Google Maps elsewhere (`PageStops.tsx:1-21`, `PageMap.tsx:23`).
- Signed out, Explore shows Pages plus "withheld" post cards that ask the visitor to sign in to read them (F093, `explore/load.ts` signed-out branch).

**In code but not reachable**
- Gathering "Items" with a host, at `/m/<handle>/e/<slug>` (`src/app/m/[handle]/e/[slug]/page.tsx`). The composer that makes them is unrouted since #336 (`src/app/you/sell/page.tsx:1-10`, `GatheringComposer.tsx`).
- Reminders fall back to email when the member has no push device (`lib/notify/push/reminder-sender.ts:1-4`). That email can't send yet because `FOLLOW_EMAIL_FROM` isn't set in production (PR #1056 body).

**Planned only**
- **RSVP / "I'm coming" with a public count** (F063, approved, horizon *later*, rank 70). There is no going/RSVP control anywhere in `src/`.

## 2. Organizer tools

**Shipped and reachable** (on the organizer's own Page, `/g/<id>`, the post composer in `PagePosts.tsx`)
- **Dated posts** with a start/end time, a place, and "How to find us" (`actions/group/post.ts:1-60`).
- **Repeat weekly** on chosen days, with optional start and end dates (F074.1). The button is at `AnnouncementFields.tsx:188` and validation at `post.ts:237-241`. Followers can tap "Remind me every time".
- **Audience**: "Anyone", or "Only people who get updates from you" (followers) (`AudienceSwitch`, `PagePosts.tsx:834`).
- **Reaching followers**: the push sender batches followed Pages' new posts every 15 minutes, plus a Thursday "this weekend near you" (`.github/workflows/notify.yml`, `lib/notify/push/sender.ts`). Members opt in per device. Push needs VAPID keys (`send.ts:18`); whether they are set in production is unverified.
- **Wonders** (F117, merged today as #1081, migration applied). A post with a goal: members tap "I'm in" with a size or offer to help in one of eight roles, the poster accepts helpers, and a progress bar shows (`components/wonders/WonderPanel.tsx`). The words were held for the PM.
- **Search demand**: an owner-only card showing what locals near the Page searched this month (`ShopPublicPage.tsx:450`, #909).
- Edit Page (the pencil): hours, contact, social links, where (fixed, roaming with stops, or service area), featured items, photo and tags (`OwnerPanel.tsx:18`, `components/group/edit/`).
- **Roles**: one managing role per Page, `owner` for a business and `steward` for a group (`actions/group/constants.ts:22`). Only the founder holds it.

**In code but not reachable**
- Nothing found for co-hosts, admins, invites or adding another manager. `member-join.ts:10-11` names "owners adding OTHER members" as a future verb.

**Planned only**
- RSVP lists that organizers see (F063). Cancelling one occurrence (F075, draft, later). "Owner sees who noticed" (F068, draft, later). Direct messaging (only discussed in `product/foundation/messaging-problem.md`).
- Note: the app refuses an email address typed into post or Page text (`lib/text/contact-info`), so organizers can't fall back to "email me".

**Strongest workflow to show:** post a weekly gathering once with **Repeat weekly**. Every follower can tap "Remind me every time" or add it to their calendar, the post reaches followers by push, and it shows on Explore for people nearby that week. Wonders is the runner-up: it's newer, and its words are still with the PM.

## 3. Local businesses

Two different claims. The brief treats them as one, but they aren't.

**(a) Claiming an unclaimed Page, i.e. ownership (#990, merged 2026-10-21)**
- **Shipped and reachable.** Unclaimed Pages are made from public info and tagged "Unclaimed: added from public info". At the bottom of the Page, **Claim this Page** sends a 6-digit code to an address at the business's own website domain. The code is good for 15 minutes and allows 5 tries. A right code makes the claimant the owner and removes the Sample posts (`UnclaimedBox.tsx:31,77`, `ClaimForm.tsx`).
- A Page with no website gets a proof-link path instead, decided by an operator in Admin → Unclaimed Pages. Claiming by text code is behind `CLAIM_BY_PHONE`, which is off (Twilio is parked).
- **Self-serve: confirmed.** No one on our side is involved except in the proof-link case.

**(b) The "Locally Owned" claim, i.e. the badge (F037, #806, #874)**
- **Shipped and reachable.** The owner of a *business* Page sees a "Locally Owned claim" card on their own Page and enters a ZIP (`LocallyOwnedClaim.tsx:30-80`, `ShopPublicPage.tsx:445`). The Page header then shows **"Claimed local owner"** (`resolve-shop.ts:108, 367-374`, rendered at `ShopPublicPage.tsx:258`).
- It is the owner's own declaration, with no verification. A registered ZIP is collected but never displayed (#246).
- Open question in code (`ShopPublicPage.tsx:444`): "Badges are cut from beta, Locally owned included (DECISIONS 2026-10-06)" versus F037 still requiring the card.

**Planned only**
- F106 (approved, *later*): a give-back town, with the badge as the receipt.

**What owners manage today:** posts (dated, weekly, followers-only), Wonders, the Edit Page fields, featured items, the Locally Owned claim, the search-demand card, and removing a false market-stall link (handler only, see Q4).

## 4. Third spaces

**Shipped and reachable**
- **Venue Pages with imported shows** (#997). Every morning a job reads each venue's own events page or feed (JSON-LD, iCal, Tribe or HTML) and posts the next 60 days of shows as dated posts. Each carries a Tickets link and credits the source. Aggregators like Songkick and Eventbrite are refused (`lib/unclaimed/venue-events.ts:1-30`, `.github/workflows/unclaimed-events.yml`, daily at 06:15 PT). Parsers are tested against real venues such as Nevada Theatre, Fox & Goose, Powerhouse Pub, B Street Theatre, Old Ironsides and Channel 24 (`lib/unclaimed/fixtures/`).
- **Market Pages with real "Market day" posts**. When a market's own site states its day and hours, it gets a weekly series and its next three dates, so "Remind me every time" works (`lib/unclaimed/market-days.ts:1-3`).
- **Recurring posts**: any Page can repeat weekly (Q2).
- **Roaming Pages** (food trucks, market sellers): "It moves" lists stops, each with Directions (`WhereFields.tsx:40`, `PageStops.tsx`).
- Unclaimed Pages carry **Sample** posts until they're claimed (`lib/unclaimed/samples.ts`).

**In code but not reachable**
- **Market vendors / stalls** (#955): set, skip, remove and confirm handlers (`actions/group/market-stalls.ts`, `actions/index.ts:110-113`), plus the stall line in reminders (`lib/markets/stalls.ts`). No screen calls these handlers.

**Planned only**
- F096 (draft): event import with consent that sends traffic back to the source. F115 (draft): unclaimed Pages from Napa Valley to Tahoe.

## 5. Feed and discovery (Explore)

**Shipped and reachable** (default Explore order, `src/app/explore/load.ts`)
1. **Place**: `browse_nearby` starts from the member's home town (signed out, from the market's main city) and widens in 15-minute rings (15, 30, 45, 60) until about 24 things are on this week. "Show more nearby" goes to the next ring or the whole area (`migrations/20261019010000_explore_reach.sql:1-13`, `20261026120000_browse_nearby_one_pass.sql`, `lib/browse/reach.ts`).
2. **Time**: within the ring, the server orders by `sort_at` (recency, or soonest under a date filter), then `updated_at` (`20261019070000_explore_feed_speed.sql:433-446`). A search puts the best text match first.
3. **First look**: up to 6 things that are new or happening soon (tonight, this weekend, last-minute, Pages new since the last visit), never ones this browser has already seen (`lib/browse/lead.ts`, `load.ts:257`).
4. **Rotation**: a seeded shuffle within recency bands (2, 7 and 30 days), so each session leads with different Pages (`lib/browse/session-shuffle.ts`, `load.ts:246`).
5. **Variety interleave**: never more than 2 in a row sharing a category (`lib/browse/mix-runs.ts`, `load.ts:252`).
- **Filters** (`lib/browse/filters.ts:66-80`): Type, post kind, Following, Category (12 interest tags or a creator's own), **My interests** (applied in the browser from the member's own interest tags, `load.ts:104,137`), Date, a search box, and a neighbourhood narrow (`?area=`).
- **No engagement ranking: confirmed.** Nothing named likes, views, clicks, impressions, popular, trending or follower counts appears in any ordering. A search of `supabase/migrations` and `src/` (excluding test fixtures) found no such tables or columns. `filters.ts:5-7` says ordering is "locality and recency, never payment and never what holds attention". The PRINCIPLES.md 2026-10-25 ruling also says Find is never reordered by payment.

**In code but not reachable**
- The old Home feed with interest ordering (`LocalityFeed`, `locality_feed_items`) is kept but paused (`src/app/page.tsx:1-13`).

**Planned only**
- F109, F112 and F113 (drafts): top results per category, giving every Page its turn, and "what SocialUs thinks you like".
- PRINCIPLES 2026-10-25 allows marked, opt-out promotion on Discover only. None is built.

## 6. New markets

**Shipped and reachable**
- **The zip decides the market** (`lib/signup/zip-market.ts`): zip → county (or county subdivision) → market. An open market lets the person in; any other zip goes to that market's waitlist. Every county not named in a market is its own waiting market (`migrations/20261012020000_markets.sql:3-6`).
- Signed in: onboarding's zip either places the member in Sacramento or shows the waitlist step with "make or find" (`onboarding/actions.ts:57-85`, `MetroWaitlistStep`).
- Explore's area picker shows a "not covered yet" panel for a waiting area (`MetroNotCoveredPanel.tsx`).
- **Conditions to open** (F076): at least 50 creators *and* at least 250 patrons, shown publicly as one combined number out of 300. The thresholds can be changed per market (`markets.creator_threshold` / `patron_threshold`). **Crossing them never opens a market by itself.** A person opens it by running `scripts/market/open-market.ts <key>` (#1056, merged 2026-10-26). That script sets `is_open`, sends "SocialUs is open in {name}. See what's going on." to each landing-list address, then deletes the address (`lib/market/open-market.ts:20-45`). The send is blocked until `FOLLOW_EMAIL_FROM` is set.

**In code but not reachable**
- **`/landing` waitlist form** (email, zip, "I run a business or group", "I'd help build this"), wired to `metroWaitlistJoinAnonymous` through `marketForZip` (`src/app/landing/actions.ts`). The page is a preview: not linked from anywhere and noindex (`landing/page.tsx:9-15`). "I'd help build this" is **not stored** (`actions.ts:37-40` TODO). "I run a business" is stored as role `creator`. When the zip is in an open market, the form returns "open" with a button to `/auth/login`.

**Planned only**
- No application or "open SocialUs in your area" flow exists beyond the waitlist. F111 (draft, later) is a join-the-team page and F110 (draft, later) a support/roadmap page.

**Launch market in the data:** **Sacramento**, the only open market. It was opened in `20260914204920_metro_waitlist.sql:67` (`sacramento-roseville-ca`), carried into `markets` slug `sacramento` (MSA 40900): Sacramento, Yolo, Placer and El Dorado counties, minus the Tahoe subdivisions. Its search area stretches south to Stockton (`20261016180000`). "Lake Tahoe" is a named waiting market. `supabase/seed-markets.sql` holds farmers markets (Folsom, Sacramento Central, Roseville) for the same area.

## 7. Signup, consent, contact

- **One way in: email, then a 6-digit code** (the PM, 2026-10-18), at `/auth/login` (`components/auth/SignInForm.tsx:1-2,71`; `CODE_LENGTH = 6` at `CodeEntry.tsx:10`). The same email also carries a one-tap link. `/auth/signup` redirects to `/auth/login` (`auth/signup/page.tsx`). `/auth/password` exists for automated tests only and is unlinked.
- **Onboarding** (`/onboarding`): one screen with legal name, display name, zip and an 18+ checkbox, then an optional interests step. The zip decides the market (open, or the waitlist). Phone verification is off until `PHONE_VERIFICATION_REQUIRED` is set (`onboarding/page.tsx:20-24`).
- **Waitlist vs signup wiring:** the landing waitlist is anonymous (email only, no account), keyed per market by normalised email, and its address is used once. Signup is separate. A signed-in member in a waiting market joins the same waitlist with their member id. Both feed the same counts.
- **Existing consent copy:** the onboarding checkbox reads "I’m 18 or older and agree to the [Terms]" (`OnboardingFlow.tsx:236`). It has no Privacy link and there is no "By continuing…" line. The sign-in screen shows no Terms or Privacy line. The Terms page body says "By signing up you confirm that you are 18 or older and agree to these Terms." (`lib/text-pages.ts:41`). Terms and Privacy are marked **draft**, pending counsel.
- **Contact destination: none.** There is no `/contact` route, no mailto in About or the footer, and no support email in config. The footer has About, Rules, Terms, Privacy and "Report a problem with the app" → `/report`, which needs sign-in (`SiteFooter.tsx:12-18`, `src/app/report/page.tsx`). Onboarding's error message says "Please contact support" but points nowhere (`onboarding/actions.ts:77`).
