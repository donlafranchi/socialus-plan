# How SocialUs works

Briefing for idea chats, written 2026-11-05 from the plan, ops and web repos; 2026-11-06 direction applied. It stands alone. **[unverified]** marks anything not checked against the code or a dated ruling.

## What it is

**SocialUs is a map-based app where the people of one town find and support each other. The message (11-06): "Locals, finding and supporting locals." Businesses are one kind of local among many, never the point.**

- It is never another business listing site. At launch it is "a yellow pages of organizations, not a white pages of people."
- Members are the investors and the only people paid out. SocialUs takes transaction income. Legal structure lives in the private legal repo, not here.
- One market for now: Northern California (11-06; was Sacramento, the counties not yet redrawn). There is no "near you".
- Build freeze (11-06): no new features until the 2027 launch; refine, clean up, prepare.

## Ethos: the soul lines

**A short list of [always] lines that every design call is checked against.**

- We assume the best of each other.
- Everything we do benefits all of us, not a few.
- You choose. It works for you. Never extractive.
- We build the system, then get out of the way.
- Locals supporting locals.
- We evolve with our members however they evolve. Don: "I only plan one day ahead whereas someone else may plan a year ahead."
- Defaults: trust first, offer a choice, share the benefit, make it self-serve, pick the well-worn path.
- Data serves the members it comes from. Never sold; opting out is one step.
- AI helps people and doesn't replace them. What an assistant knows belongs to the member, can be exported and deleted, and never trains anyone else's model.

**Find vs Discover.** Find is the tool: you look for something specific, and results are never reordered by payment. Discover is the fun: you browse with nothing in mind, and an algorithm may serve what interests you. Paid promotion, if it ever exists, is allowed on Discover only, and marked.

**Words we don't use.** People are never a category: no creators, vendors, sellers, makers, supporters or consumers. A person is "you." No chip or pill UI anywhere.

## The nouns

**Members make Pages; Pages post; members heart, save and get updates. Everything is listed under one shared label list.**

- **Member.** A person with a private account. There is no public profile. Between members you see only a display name and avatar.
- **Page.** Anything local with a purpose: gather, sell, offer or create. A business or a group. A Page needs a location to show up anywhere.
- **Unclaimed Page.** A real business added from public info. The owner claims it by entering a code sent to an email at the business's own website domain, and owns it at once. Claim by phone is built but off. Anyone can ask to remove an unclaimed Page; it hides at once.
- **Posts and their kinds.** A Page posts one of seven kinds, each with a shelf life. When it ends it leaves Explore and search and sits under "Earlier" on the Page.
  - Event and Reminder: until the date passes.
  - Offer (sale): its end date, else 7 days, never past 30.
  - Update (news): 7 days. Limited: 14 days. Hiring: 30 days.
  - **Proposal:** "would people want this?" Members tap "I'm in" (with a size) or "I can help" in one of eight roles. A count and a goal bar show; the poster sees who. No money moves. Lasts 14 days.
- **Person posts** (posts without a Page, live today). Lost & found, Free / for sale, Ask a neighbor. Up to 3 at once, 7 or 14 days. One answer instead of comments: "I saw it" or "I'm interested", seen only by the poster. Signed-in readers only. They need a confirmed phone, which isn't open yet, so today only test accounts can post them.
- **Listed under.** Pages and posts pick up to 3 labels from one shared list (12 top labels, about 65 finer ones). Free-typed tags are refused. If you pick none, labels are suggested from your own words.
- **Heart.** "I like this." The Page's managers see who. Counts are not public. It also feeds the taste scale later.
- **Save.** "Keep this for later." Private, listed on You.
- **Get updates** (was Follow). The Page's news comes to you by push; the owner never gets your contact details. Its job is to replace promotional email.
- **Remind me / Add to calendar** on dated posts.
- **Shelves.** Explore is rows of things. Things you get updates from come first, then Next 7 days, then themed shelves that rotate. Ruled 11-06: this week, then later, then Pages after the timely posts; today the main list below the shelves mixes Pages and posts by last update. A shelf is a row of data, not code; seasonal shelves run by date, and the order rotates per member per day.
- **Search groups.** Results come in groups: time first (Today, Next 7 days, This weekend, Coming up), then Pages by kind, then posts by kind, then "From neighbors."
- **The taste scale** (research only, not built). One sliding interest scale per member, by topic, Page and place, that the member can see and steer. Discover leans on it; Find only uses it to order and never hides a result. Ruling: no checkboxes or manual strength pickers as the main way in.

## Journeys

**Sign in with an emailed code, one onboarding screen, then Explore. Owners answer one question and land on a draft Page.**

**A member:**
1. The front page is for signed-out visitors. Enter an email, then the emailed 6-digit code. Sign-up and sign-in are the same step.
2. One onboarding screen: legal name (private), display name, zip, 18+ and Terms. The zip picks the market, or a waitlist if the town isn't open.
3. An optional "What are you into?" step.
4. Explore: one top row with search (What, Where, When), ➕ to create, and You. No bottom bar.
5. Heart, save, get updates, remind me, say "I'm in" on a Proposal, post to the neighborhood, report something.

**An owner:**
1. ➕ then "What are you starting?" Four answers set the purpose and make a draft Page.
2. A short checklist before publishing: name, where, description, Listed under, optional photo. One line: "By posting you agree to the Terms."
3. Post: pick a kind first, then write.
4. Or claim an existing unclaimed Page.

**Reports, courtesy first.** A first report sends the poster a courtesy notice and the post stays up. A second report from someone else hides it for a person to review. Threats and sensitive content hide at once, and a sensitive-content poster is never told who or why.

## Stack and architecture

**A Next.js web app on Vercel, a Supabase Postgres database, and GitHub Actions for everything scheduled. No servers of our own, no GPU.**

- **App:** Next.js 16 and React 19, deployed on Vercel. A merge to main deploys to production. Vercel plan is Hobby (free) per the ops docs **[unverified against the dashboard]**.
- **Database:** Supabase Postgres on the Free plan, with PostGIS for maps, pgvector (installed, unused) and text search. Row-level security on every table. Pro ($25/month) is planned two weeks before launch.
- **Writes** go through one action layer: every change is a named handler with a checked input.
- **Migrations:** about 154 SQL files, applied by a manual GitHub workflow, with a daily drift check.
- **Scheduled jobs** (all GitHub Actions): push for followed Pages every 15 minutes, a Thursday "this weekend" push, bug-report filing every 30 minutes, nightly tests, a daily read-only check of production, tap-speed checks, daily venue-events import, daily test-account activity, and data purges (deleted Pages after 14 days, IP records after 1 year).
- **Seeders and importers:** test personas for local tests only; hand-researched lists of real businesses loaded as unclaimed Pages; a daily reader of venues' own event pages (obeys robots.txt). None of them call a model.
- **Other services:** Resend for email (free tier), Web Push with our own keys, Mapbox maps (free tier), Sentry wired but off until a key is set, Twilio parked until Don adds keys.
- **AI in use today:** two places, both Anthropic, both only when a key is set. A first read of reported posts (shadow mode: it records, a person decides) and labelling members' bug reports. See the AI briefing for detail.

## Privacy and data rules

**You is private. Members see each other's display name only. Operators alone see legal name, email and phone. Nothing is sold.**

- No public member profile, ever (ruled 2026-10-01).
- Your zip is never shown. A Page's exact address shows only if the owner makes it public.
- A heart shows your name to the Page's managers; saves are private.
- The address and time of every post and upload are kept for operators and deleted after one year.
- Any AI provider gets content only, never names, emails or member details. Suspected child-safety content is never sent to an AI.
- The privacy page is still a draft. Retention periods, a processor agreement with Anthropic and the full list of processors are on the to-do list for counsel.

## How decisions flow

**Don gives direction; agents research options with a recommendation; Don decides. Well-worn calls the agents make themselves.**

- **Decision rule:** look at 2–3 precedents first. If there's a clear, established pattern, the agent decides and builds it ("Path: well-worn"). Anything that touches a ruling, legal, privacy, money or member trust goes to Don as A/B/C with a recommendation ("Path: new territory").
- **Don decides** ideas, what goes in each version, and the words and look. Agents decide the rest. New user-facing copy and anything reaching production go to Don.
- **Roles:** Don is the PM. Cowork plans in the plan repo. Code agents build. Dispatch is Don's phone-side agent: each ask becomes a web Issue, and one build loop runs per Issue.
- **The pipeline:** Issue → tests written first and seen failing → PR → a separate reviewer agent's first pass → self-merge when green → production. A PR either says "Don doesn't need to look" or gives three steps to check it on a phone.
- **The record:** each ruling is dated and lives in the doc it governs. STATUS is generated, never hand-written.

## Known gaps between rulings and the app

**[verified in code 2026-11-05]**
- "Near you" wording is still live in the app title, share image and weekend push.
- The /join page still says "vendor."
- "Neighbor" wording is live (Ask a neighbor, /neighbors) though Don asked for "locals" on 10-31.
