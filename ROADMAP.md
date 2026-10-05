# ROADMAP

Now / Next / Later / Won't, one line each. Detail and days: `socialus-web` Issues (was `planning/now/initiative-launch.md`).

**Beta 2026-10-30, one metro** — for testing; a soft target, not a hard deadline *(2026-10-05)*. **Feature freeze 2026-10-23**, also soft: the last week is fixes and the copy pass. **Production launch April–May 2027.** "Launch" below means production; "beta" means 2026-10-30.

**Beta keeps** *(2026-10-05)*: sign-in; one-question Create; Page types; the Page; Posts (the rename); latest posts; owner tools; edit by section; badges; the location picker; navy/gold anodised colours; Page logo and Post images (F099); What's happening dates, repeating series and time rows (F091); end time, add-to-calendar and default alt text; tags on posts; the report path; the metro waitlist; patron signup; the footer with About/Terms/Privacy drafts; the builder seed-content job; the three accepted-risk fixes due 2026-10-16. What left is in § Cut.

## Now — Fortnight 1, in build

- Page composer: address or neighbourhood/town location step (seeded list covering MSA 40900, shown as a pin at its centre, 2026-10-04), category step, photo step + takedown, default art, resume fix. *(The gate on the PM making their own Page is met — they have made several, Sac Floaters among them, 2026-10-01.)*
- Dead producer page fix — approved, ticketed, buildable today.
- Producer entry point (`/you/create`, no shop required to host) — reviewed, ticketed.
- Report path + image takedown — approved; no photo goes to production until this ships.
- Display name in public; flagged content auto-hides with an immediate reason and appeal, anything a member posts is reportable, and the reporter picks a reason the poster can rebut (F078, scope added 2026-09-30); no pictures of children from anyone, stated at posting with reports as the backstop (F080, 2026-09-30) — approved, gates beta alongside the report path.
- Metro waitlist at signup — pick a metro, say creator or patron, see a count in a popup. **Added 2026-09-14 at the PM's direction; nothing was removed to make room.** F076.
- Patron signup (legal name, verified email, verified as a person — method open, zip; the zip determines the metro, every US zip known before beta; a line on what the app is for, 2026-09-30; an 18+ checkbox with the Terms link beside it, 2026-10-05) and agreeing to the versioned rules before each new Page, selling and hosting alike — F081, F082. **Added 2026-09-14 at the PM's direction; nothing was removed to make room. Both approved 2026-09-14.**

## Next — Fortnights 2–3

- Retired vendor routes redirected or removed.
- Footer linking About, Terms and Privacy pages (design decision 8, 2026-10-01, the PM) — **beta scope**; none of the three pages exists in the app today. Privacy is due before the first signup. The page text is supplied from outside this repo.
- **Tags on posts, and tag editing any time** (2026-10-01) — **in beta, confirmed 2026-10-01**; **nothing was removed to make room.** Post replaces announcement as the user-facing word; the copy review rides with the copy pass.
- **What's happening…** — a date, a time and a post-level address on an announcement (F072); **a series that repeats, weekly with optional bounds (F074, ruled 2026-09-20)**; the time lens rows (F091). The browse query shipped 2026-09-19 **and nothing calls it** — Explore still reads the old Item-grain view client-side. So it needs **two** things, a caller and a de-duplication rule, not the one change this line claimed until 2026-09-20. **The new cost is F073, recurrence, and the parser.** Recurrence is what makes the lens non-empty; Bulletins was cut to pay for it — see § Cut.
- Optional end time, add-to-calendar, and default alt text from title, date and place on dated announcements and gatherings (F072 criterion 6, 2026-09-30) — **beta scope**.
- Optional public business phone on a Page (F056 criterion 9, 2026-10-01) — built (#293). Hours are hidden for beta (below).
- **Page kinds and badges** — the kind line (icon · Business or Social group · main collection), Locally owned for businesses only; the latest 2–3 posts on a Page with "See all posts"; "Post" everywhere in copy (2026-10-05, dispatch-decided) — **beta scope; nothing was removed to make room.** The Page values list follows after beta.
- **Page logo and Post images** (F099) — **beta scope**; slice approved 2026-10-05: one Page picture per Page, one photo per post, gallery after beta.
- **AI first-pass review, the Posts review page, and the poster answering first** (F100, F101, F102, approved 2026-10-05) — **beta scope, nothing removed to make room**; about 8 build days with the freeze on 2026-10-23. The AI runs in shadow in beta. F101's scope signal recommends what to push past beta if the freeze is at risk. Auto-restore of severity-4 content stays open in F102.
- Anodised palette tokens: navy actions, gold highlight (2026-10-04, `socialus-web` #325).
- The three accepted risks due 2026-10-16: error tracking in production, real deletion of removed photos, browser tests running in CI — **beta scope**.
- Builder seed-content job — synthetic, display-only content — Fortnight 4.
- Onboarding, empty states, copy pass — Fortnight 4, after the 2026-10-23 freeze. The copy pass covers person-nouns by hand.

## Later — deferred past beta, priced

- Weekly business hours on a Page — built (#293, #344) and currently hidden from the Page and Edit because they cluttered it; the data is kept (the PM, 2026-10-05).
- Real names between people who dealt with each other (F077, `socialus-web` #219) — **out of scope 2026-09-30; revisit with legal counsel.**
- Bulk actions on the review queue (F079) — written, unscheduled; waits on real volume. *(The ID + selfie tier left this line 2026-09-27: the PM ruled none is being built, so F080 names no unlock.)*

- Individual product and service listings on a Page — **postponed until after beta** *(the PM, 2026-10-01)*. **Starting point when it's due (the PM, 2026-10-05):** the old `/you/sell` flow, moved onto the Page's Add. Its pieces are kept in `socialus-web`, unrouted since #336: the composers `src/components/sell/ProductComposer.tsx`, `ServiceComposer.tsx`, `GatheringComposer.tsx` and the `Add*Button.tsx` triggers; their server actions under `src/app/you/sell/product/`, `service/` and `gathering/` (`actions.ts`, with `action-result.ts`); and the walkthrough's helpers `src/lib/sell/` (`purpose.ts`, `unwrap.ts`). `SellWalkthrough.tsx`, `SellCta.tsx` and `getDraftGroup.ts` belong to the retired walkthrough that Create replaced.
- Item-level photos — substrate built, ~half a day when resumed.
- Volunteering (offer/ask composer) — blocked on messaging, not on the composer.
- The idea mechanic (wonder composer) — specced and substrate shipped, composer/page missing.
- Metro scoping — ticket written, returns with a second metro.
- Page-level appearances at venues — ~1.5 days, scoped.
- Follow-substrate merge and the map's area rendering — both scoped.
- Member-to-member messaging — no substrate at all; blocks a volunteering reply channel.
- Structured recurring-location scheduling — priced v2 buy-back for the free-text "where they'll be next" line.
- Paid visibility / advertising mechanic — gated on passing the member-benefit test; not designed.
- Cooperative coordination tooling (voting, distributions) — waits on documented demand.
- LLM-enhanced natural-language search ("sourdough near me Saturday") and SEO-structured public pages. **In-app answering is the next version after beta, not backlog for 2026-10-30** *(the PM, 2026-09-21: "something I'd like to prepare for for the next version after")*. **What is wanted before beta is not building it but not foreclosing it** — five constraints in `planning/AGENT-ANSWERING.md`, each cheap now and expensive to retrofit. Paired with the crawler-blocking and thin-public-tier work in `socialus-web`.
- **Values-shaped recommendations** (F097, draft) — private values, a ranked buying list, blended recommendations, opt-in badges, endorsements shown as a meter not a number. **Nobody can search values.**
- Saved-search subscriptions ("notify me: new products in Oak Park").
- Richer service-listing fields (appointment availability, scope of work), item lifecycle states (draft/paused/archived), stock indicators, bundled items.
- Community-attested (Tier 1) and document-verified (Tier 2) locality/provenance badges — Tier 0 self-attestation is all that ships in beta.
- Follow-stream notifications, item-level customer inquiry, follower-list management for a producer.
- Producer growth dashboard, weekly digest email, peer benchmarks.
- Multi-location/ambulatory-route management, sub-venue support (e.g. "Drake's barn" under Drake's).
- On-platform payments — closed-loop ledger + ACH via a chartered partner, zero platform transaction fees on member commerce (the wealth-circulation rubric), a stablecoin path long-horizon.
- Treatment-review surface (reviews the treatment, not the person) and member references.
- Multi-owner/partnership business Pages, staff-confirmation flows, community-stewardship-to-business transition.

**Speculative, not ruled**
- Price on cards: Free / Donation / Paid *(the PM, 2026-09-30)*. F072 criterion 2 stands: an announcement carries no price today.
- A public member profile, like a TikTok profile *(the PM, 2026-10-01)*. You currently isn't visible to anyone else; someone who wants to be followed creates a Page.
- An event without an organization: a one-time Page for it *(the PM, 2026-10-01: "even though that doesn't really make sense")*. Today an event is a post a Page makes.
- Vouching: a neighbour chooses to vouch for a service provider *(the PM, 2026-09-30; F095)*.
- Page components not offered in beta *(the PM, 2026-09-30: a Page is composed of components any owner can add)*: RSVP on a single post; transactions and one-on-one meetings; visibility levels on a Page that isn't a group Page; switching following or joining off.
- When in-app purchasing exists, producer and purchaser see each other as far as the transaction needs *(the PM, 2026-09-30)*.

## Cut — taken off the beta list, dated and reasoned

*Not the same as Won't. A cut thing is still wanted; it lost a trade against the deadline and may come back. A Won't thing is refused on principle and doesn't come back. Recorded here rather than quietly deleted, because a line that vanishes from Next leaves no trace of who decided or why.*

**Cut 2026-10-05 — beta trimmed to what testing needs.** *Asterisk: the PM may pull any of these back into beta by judgement.*

- **Badges & values section in Page settings** *(cut 2026-10-05)*. **What left:** the settings section with the kind facts (Locally owned, Family-owned, Since, Co-op, Nonprofit, Free to join, Everyone welcome) shown as badges. **What stayed:** the kind line and Locally owned for businesses. **Why:** room for F100–F102 before the 2026-10-23 freeze; F101's scope signal named it first to push. **Comes back when:** after beta, with the values list (F097), or the PM pulls it back.
- **Search and Browse rebuild, and popularity ordering** *(cut 2026-10-05)*. **What left:** search over Pages, Browse rebuilt around Pages and gatherings, and popularity ordering with a reserved share for new Pages. **Why:** beta tests making and reading Pages and posts; a beta-sized set of Pages needs no ranking, and latest posts covers reading. **Comes back when:** beta Pages outgrow one scroll, or production scope is set.
- **RSVP / response path** *(cut 2026-10-05)*. **What left:** one response per person on a gathering. **Why:** beta tests posting, not attendance; a dated post already carries date, time and place. **Comes back when:** beta testers ask to say they're going, or production scope is set.
- **Follows simplification** *(cut 2026-10-05)*. **What left:** one follows table for three subjects. **Why:** plumbing with no member-visible change in beta. **Comes back when:** follower delivery (Bulletins, below) returns, since that is what reads it.
- **Person-noun lint** *(cut 2026-10-05)*. **What left:** the `socialus-web` build check that fails on a person-noun in a user-facing string (spec in `product/foundation/nouns.md`). **Why:** the copy pass in the last week covers it by hand. **Comes back when:** before production, so new strings stay clean without a hand pass.
- **Map bottom control and metro memory** *(cut 2026-10-05; `socialus-web` #328–330)*. **What left:** the map's bottom control and remembering a member's metro. **Why:** beta is one metro, so metro memory has nothing to remember; the map control is polish. **Comes back when:** a second metro opens, or testers find the map hard to use.
- **Places open data plan** *(cut 2026-10-05)*. **What left:** loading places from open data. **Why:** the seeded neighbourhood/town list already covers the one beta metro. **Comes back when:** a second metro opens, or production scope is set.
- **Home rows** *(cut 2026-10-05; F098)*. **What left:** Home as rows that keep going — Tonight, This weekend, New this week, a wildcard, ending at a stop card. **Why:** still a draft with open questions, and latest posts covers beta. **Comes back when:** its open questions are answered and there are enough dated posts to fill the rows.
- **Dateless posts expiring to "Earlier" after 14 days** *(cut 2026-10-05)*. **What left:** moving a post with no date under "Earlier" once it is 14 days old. **Why:** beta volume is too low for old posts to crowd new ones. **Comes back when:** posts start to crowd latest posts.
- **Narrowing in a modal that writes text** *(cut 2026-10-05; F092)*. **What left:** a modal that narrows What's happening and writes the narrowing back as text. **Why:** the time rows (F091) already do the narrowing beta needs; the modal and its parser are extra build. **Comes back when:** testers want to narrow past the time rows, or production scope is set.
- **Metadata rewrite** *(cut 2026-10-05)*. **What left:** rewriting page titles, descriptions and share previews. **Why:** beta is for testing, not search or sharing reach. **Comes back when:** before production, when public pages need to be found and shared.

- **Bulletins — the member-audience half of a post** *(cut 2026-09-20, the PM)*. **What left:** a post being delivered to the feed of everyone who follows a Page or belongs to its group. **What stayed:** the composer, and posts appearing in browse — both are what *What's happening…* runs on. **Why:** recurrence (F074) was ruled in the same day and is what makes the time lens non-empty; the beta list was already over, so something had to pay. **Cost of the cut:** a Page owner has no way to reach people who already follow them, which is the thing followers are for. **It comes back when** the time lens is shipped and the follower graph has enough density that delivery reaches more than a handful of people. **Re-examine this trade if F059 criterion 2b slips.** The cost above is survivable *only* because announcements from followed Pages are meant to surface on Explore for a signed-in reader — that is F059 criterion 2b, item 2 on the PM's list, and **it is not built**. If it moves, a Page owner has no route to their own followers at all, and this stops being a deferral and becomes a hole. **Nothing built is discarded** — the subscription link exists in `group_memberships` and nothing reads it yet, so the cut removes unbuilt work. Reflected in F072 criterion 2.

## Won't

- Platform-generated QR codes — a producer's own business QR stays open as an unbuilt idea; the platform doesn't generate any.
- Activity badges, reputation scores, star ratings, ownership tiers — the platform currently doesn't rate, rank, or label a person.
- Business-entity modeling — ownership transfer, succession, corporate shells. Membership is the only access-granting verb.
- Geofenced or auto-assigned group membership.
- Engagement-optimized ranking, streaks, pull-back notifications.
- Venture capital funding.
- Legal or tax language between members or in Page creation; legal-entity information from anyone without a legal entity (2026-09-30).
- Full e-commerce catalog (variants, SKUs, cart), automated/dynamic pricing, inventory or warehouse management, POS/checkout, appointment-booking or calendar sync, as full-featured products. SocialUs isn't a fully built-out platform of any kind except for discovery and support of locals; basic in-platform versions, so people can transact and connect, are possible (the PM, 2026-09-30).
- Automated government-API verification of producer claims — the trust ladder is human-driven (self-attest → community-attest → document-upload) only.
- Mass-email marketing tooling, push notifications to non-followers, individual visitor-tracking analytics for a producer.
- Platform-custodied funds held for the platform's own benefit, lending, or credit.
- Payroll, HR, or employee management — the platform records who's associated with a Page, it doesn't manage employment.
