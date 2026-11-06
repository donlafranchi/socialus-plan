# Near-term plans

**As of 2026-11-06** · Source: hand-written · Maintained by: hand (set by tend-docs from the last commit date; the owner confirms on next edit)

Briefing for idea chats, written 2026-11-05 from the plan and web repos; direction change of 2026-11-06 applied. It stands alone. Numbers in brackets are web PRs or Issues unless marked "plan." **[unverified]** marks anything not checked.

## Direction, 2026-11-06

**Build freeze: no new features. Refine what is built, clean up, and prepare for a 2027 launch.** Don: *"I don't want to build anything else only refine what we've built."*

- **Held, not cancelled:** video A [plan #271]; the /join gaps (a link on each post, search-engine visibility, owner names and a note, "where I'll be", private stats); the Jev or Haiku sorting step [plan #273]; the taste scale and Haiku chat [plan #263, #269]; public counts; the Staff link; every approved scenario not yet built (the whole Next lane below).
- **Continues:** bug fixes, copy, cleanup, performance, the overnight live check, seeding.
- **Explore order:** what's happening this week, then later, then Pages after the timely posts.
- **Market:** the beta market is Northern California, not Sacramento. The counties it covers are proposed, not yet changed.
- **Message:** "Locals, finding and supporting locals." No copy changes yet; the rewrite is a to-do for Don.

## Live now

**The core app is live: Pages, seven post kinds, Proposals, person posts, Listed under, heart and save, push, and a self-serve claim.**

Shipped this week:
- Posts without a Page: Lost & found, Free / for sale, Ask a neighbor [#1184]. Phone check gates them, so members can't post them yet.
- Listed under: one shared label list for Pages and posts [#1181].
- Heart, save and "Get updates" in place of Follow [#1172].
- Bigger cards, clearer report wording, map tap counts [#1168, #1170, #1169, #1163].
- One top row with a single ➕ [#1161]; Explore shelves as data [#1159]; grouped search [#1155].

Shipped earlier:
- Explore mix, search and My interests [#881, #932, #924, #934, #911]. No chips anywhere [#956].
- Seven post kinds with shelf lives [#1126, #1143, #1153]; new Page layout [#1140, #1131]; readable addresses [#1146, #1149].
- Proposal, renamed from Wonder [#1081, #1150, #1142]. Featured items [#920, #929].
- Self-serve claims by website email [#990].
- Venue event imports [#999, #1039, #1043, #1046]; farmers-market vendors [#963, #964]; daily seeding of real local businesses [#1111 and others].
- Remind me [#952], push [#930], Following list [#966], sign-in by emailed code [#946, #928, #933].
- Landing page and welcome [#1091, #1129, #1130, #1134, #1156, #1133]. Rules page replaced by one Terms line [#1135, #1087, #1096]. Install to home screen [#925].
- Speed work [#1025, #1074, #1076, #983, #989, #992]; new-version prompt [#967]; build-failure alert [#954].
- "Open your town" is built but switched off [#1093, #1100].

## Being built

**Mostly seeding, a few fixes, and the launch blockers that wait on Don's keys and tests.**

- Open PRs: an Edit link [#1071] and rotating the seeding themes [#1128]. The daily seed PRs through 11-06 merged; they load into production on the next write run.
- Launch blockers:
  - Report flow and the AI first read in shadow: needs Don's three-account test and the Anthropic key [#220, #486].
  - Waitlist message [#616, #1118]; [#1112]; a failing production check [#1166].
  - A Vercel build Issue that is likely closable [#1121].
- Speed is red: tapping from the header to Explore took about 4 seconds [#978].
- The rest of the Explore shelves work [#1158], plus smaller Issues [#1080, #1173, #1101, #1102, #1103, #1078].
- Plan's "Now" lane lists F060, F061, F069 and F070 as building **[unverified]**.

## Decided, queued (held by the freeze)

**Ruled and waiting their turn, held until the freeze lifts. Nothing here needs Don again unless it changes.**

- Video: option A ruled 11-05 [plan #271]; no web Issue yet.
- AI sorting of posts into labels: a 100-post test of Jev against Haiku first, 90 of 100 right to pass, and Jev's data retention confirmed in writing [#1182, plan #273].
- Phone check: built, waits on Twilio keys [#707].
- Next lane: F118 (open your town), F119 (Ask bar), F121 (shelves), F104/F105, F057, F059, F064, F065, F093.
- "Open your town" turns on after the soft launch reaches 100 makers and 1,000 supporters.
- AI moderation goes live only after two weeks of shadow data (F100). The kindness pause waits on that data too (F108).
- Place pages before production. Native apps later.
- A plan PR is blocked on a doc size limit [plan #257].

## Researched, awaiting Don

**Calls only Don can make: copy, money, and the open questions in STATUS.**

- The /join page copy [plan #274].
- Sellers research: paid promotion, the fee rate and when it starts, public counts [plan #269].
- Draft words in the person-posts and Listed-under work [#1184, #1181].
- Open plan PRs: chat-first [plan #228] and lifecycle email [plan #227].
- 13 open questions in STATUS, including F122/F123/F124, the payment rail, F110/F111, scouts and surplus.
- Don's to-dos: the rules list, the three-account report test, founding-circle interviews (11-06), and accounts for Sentry, Speed Insights, the Resend domain, HUD and Cloudflare [#981, #787].

## Parked

**Not now, by ruling.**

- Proposals without a Page. Purchase tracking. A multi-Page activity view.
- Claim by phone (built, off).
- The 26 ideas in IMAGINE. The deferred tickets [#715–#745].

## Soft launch timing

**No date is set. Ruling (11-06): build freeze, prepare for a 2027 launch; one market, Northern California; production April–May 2027.**

- Whether the soft launch has already started is **[unverified]**.
- Blockers: the seven launch Issues above, Don's keys, test coverage of the launch criteria at 66%, speed red. Latest launch report: 10-30.
- The launch checklist's one open item: child-safety hash checking through Cloudflare at entity setup.

## Out of scope before launch

**Payments, messages and anything that makes SocialUs a marketplace or a social feed wait.**

- Recommended, not ruled (sellers research): payments, direct messages, full product listings, video upload, cross-posting.
- Ruled: badges cut; galleries after beta; place pages before production; "verified local" V1 is the owner's own statement; no kindness pause at launch; AI moderation in shadow during beta; counsel after launch; the council's CUT list.
