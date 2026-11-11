---
id: brief-2026-11-11-product-analytics
status: awaiting-approval
size: M
path: new territory
criteria:
  - The PM can read, once a week on the dashboard, how many members came back each week by the week they joined, which parts of the app they used, and where sign-up and first post drop off.
  - Every number is a count; no member id, email, IP address or precise location is stored with a usage count or sent to any outside service.
  - A member who turns sharing off on You is never counted, using the switch that already covers search and map taps.
  - No new paid tool, and nothing added to a member's page load beyond what the app already sends.
  - Counts start before the first invited cohort arrives, so that cohort is not lost.
---

# Product analytics

**As of 2026-11-11** · Source: socialus-web INFRASTRUCTURE.md (Product analytics, Error tracking), docs/error-tracking.md, src/lib/observability, the map-tap and search-demand migrations; socialus-ops process/PERFORMANCE.md; vendor docs linked below · Maintained by: hand (brief; deleted at 30 days or once ruled and placed)

*The PM, 2026-11-11:* asked for "load testing and ... other app telemetry type things", and picked A: agents build load tests, uptime and backups now; analytics comes back as options because it touches member data.

**Bottom line: count usage in our own database, the way map taps and search demand are already counted; nothing leaves the platform, it costs nothing, and it answers the three questions. Add an outside tool only if a question comes up our counts cannot answer.**

## What the PM wants to know

- Are people coming back? Members active each week, by the week they joined.
- What do they use? Posts, Explore, Pages, groups, the map, search, Ask.
- Where do they drop off? Sign-up steps, first post, first follow.

## What already exists

- **Errors** go to Sentry, scrubbed: no user, cookies, bodies or query strings; emails and phone numbers cut out. Off until a key is set. This is the bar for anything that leaves the platform.
- **Two counts are already ours:** map taps per day (no member id, dedupe keys deleted after 8 days) and search demand (no member id with a query). Both skip a member who turns sharing off on You.
- **Sign-in times** are already held by the login system, so "came back" needs no new tracking of where a member goes.
- **The infrastructure plan names PostHog** for this, with replay off and profiles only for signed-in members. That was written before the 2026-10-25 data principle and the opt-out switch; it is a plan, not a ruling.

## Precedents

- **Plausible** ([data policy](https://plausible.io/data-policy)): no cookies; a visitor is a hash of IP and browser with a salt deleted every 24 hours, so no one is followed across days. Paid hosting (a few dollars a month) or free to run yourself. Answers page counts and simple goal funnels; cannot answer "did the same person come back".
- **Vercel Web Analytics** ([limits and pricing](https://vercel.com/docs/analytics/limits-and-pricing)): built into our host; free plan includes 50,000 events a month, collection pauses at the cap. Page views, referrers, device and country. Funnels and retention need custom events and a paid plan (assumed from the docs, to verify before choosing).
- **PostHog** ([pricing](https://posthog.com/pricing), [anonymous vs identified](https://posthog.com/event-comparison)): first 1M events a month free; funnels, retention and paths out of the box; a cookieless mode exists. It answers all three questions best, and it does so by keeping a per-person history of every event on its servers.

## Options

- **A. Count it ourselves (recommended):** daily and weekly counts in our own database, with no member id beside them, read on the dashboard. Answers all three questions at the cohort level. $0. Nothing leaves. Costs a few days of agent build, and fewer charts than a product built for this.
- **B. Vercel Web Analytics:** turn it on, no code. $0 to 50,000 events. Page paths, referrer, device and country go to Vercel, without cookies. Answers "what do they use" by page; not who came back or where a sign-up stalled.
- **C. PostHog Cloud, as the infrastructure plan says:** $0 to 1M events. Answers everything, including paths and individual drop-off. A per-person event stream leaves the platform for a third party; that is the thing our error tracking was built to avoid, and the data principle asks who gains.

## Why A

- Data serves the members it comes from, is never sold, and opting out is one step: A uses the switch members already have; B and C would need their own.
- The PM's questions are about members in aggregate, not about any one member; counts answer them without a history of anyone.
- Same pattern as map taps and search demand, which agents already run; no new paid tool (the 2026-11-10 ruling).
- B can be added on top later, if page-level referrers are wanted, without changing A.

## One call that comes with A

- The build freeze (2026-11-06) holds anything that adds a stored field. New count tables are stored fields, so A needs the PM's yes as launch preparation, or it waits and the first cohort goes uncounted.

**How A would be measured:** the dashboard shows weekly returning members by join week, use by part of the app, and the sign-up and first-post funnel, within a week of the build; a review of what is stored finds no member id, IP or email beside any count; and one test member with sharing off is absent from every count.
