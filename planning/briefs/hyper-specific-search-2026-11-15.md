---
id: brief-2026-11-15-hyper-specific-search
status: awaiting-approval
size: L
path: mixed (history, insights and slots well-worn and filed as Issues; how long history is kept and the launch slot set are the PM's)
fits: after the waitlist (#1299); the 2026-11-06 build freeze holds the build until the PM lifts it for this theme
criteria:
  - A member sees their own searches on You, deletes one or all, and turns keeping them off; no other member, Page or visitor can read them (a test proves it, seen failing first).
  - A Page's managers see a searched term only when ten or more different members searched it in that market in 30 days, and an area only when it alone clears ten.
  - The front door shows the search box and at most three slots; a member with no history gets the market's story and the next seven days.
  - A search with time words orders what is happening soonest first; item, place and vibe words work alone or mixed.
  - The Privacy page says what is kept, for how long, and how to delete it, before history ships.
---

# Hyper-specific search: connecting members, a minimal front door, and what producers learn

**As of 2026-11-15** · Source: the PM's words in one thread, 2026-11-14 to 11-15; socialus-web at `4a45ea5`; a sweep of socialus-plan, socialus-ops and socialus-web; the precedents linked below · Maintained by: hand (brief; deleted at 30 days or once ruled and placed)

*The PM, 2026-11-15:* "the most important thing is that we connect our members and help them connect with each other and that's kind of what this searches meant to empower"

**Bottom line: search is how members find each other. Keep each member's searches for them alone, tell producers only what many people want, and keep the front door to a search box and a few things that matter today. Most of the parts exist; your one call now is how long a member's searches are kept.**

## Why

A search is a member asking. The answer is another member: the maker, the group, the shop down the street. Three things follow, and all three are the PM's rulings of 2026-11-15 (`scenario-F136.md` § Rulings):

- **Hyper-specific, not just local.** Specific by place, by item, by vibe, or any mix: "cozy coffee with a patio, Midtown", "pottery class, evenings", "skateboards". Timely: what's on now and soon.
- **Your searches serve you.** Kept on your profile so the front door learns what to show you. You see them and delete them.
- **Producers learn what many want, never who.** "Twelve people searched for pottery classes in Midtown this month." That is how consumers and producers help each other.
- **The front door stays minimal.** Less is more, with history or without. What fills it is a pool of ideas that come and go, not fixed sections.

## What exists today (socialus-web `4a45ea5`, read 2026-11-15)

- **Search:** one box on Explore; full-text with stemming, a synonym list, typo matching when few results come back; a Page's products are searchable. Time words ("today", "this weekend") narrow by date; there is no "now" or "open now", and no vibe words.
- **Item tags:** ruled 2026-11-13 to lead search (F092); build Issue #1318 is open, after the waitlist. Only the seed files carry a "carries" list so far.
- **Search counts:** every search is counted by words, market and result count, with no member id; "Count my searches" on You turns it off. Staff see top searches and "found nothing" per week and area.
- **Producer card, already live:** a Page's managers see terms searched **3 or more times** in 30 days, "never who made them". It counts searches, not people, so one person searching three times clears it.
- **Reminders:** "Remind me" on a post or series sends a push or email the evening before and an hour before.
- **Saved searches:** a table exists; nothing sends alerts from it (#725).
- **Shelves:** rows as data with rules (F121): followed first, Next 7 days, seasonal, interest shelves from declared interests; rotation per member per day. This is the pool the front door draws from.
- **Ask bar:** approved, not built (F119): a cheap model call turns a question into a page and filters.
- **Waitlist answers:** what a person plans to do and offers (#1299); staff-only, deleted when the invite goes.
- **Not there:** a member's own search history, a front door (signed-in members land on Explore), account deletion or data export.

## The launch slice (robust to build on)

**1. Your searches** (web #1326, well-worn)
- A table owned by the member: the words searched and when. Not where they stood; not searches that reach a hidden signal's help.
- On You: the list, newest first; delete one; delete all; a switch to stop keeping them. Separate from "Count my searches".
- A scheduled job deletes rows past the retention you choose (call 1).
- Account deletion, when built, deletes them; export includes them.
- Precedent: [Google My Activity](https://support.google.com/accounts/answer/465): delete one, a range or everything, and auto-delete; Etsy's "Recently viewed".

**2. What producers learn** (web #1327, well-worn; replaces the live 3-searches rule)
- Counted as distinct members, possible now because each member's searches are theirs; the anonymous market count stays as is for people who keep no history.
- Floor: **ten different members per term, per market, per 30 days**, applied at every level shown; an area appears only if it alone clears ten. Smaller counts are stored and withheld.
- Shown as "About 12 people searched for this near Midtown". Never who, never one person's searches.
- Precedents: [Google Trends](https://support.google.com/trends/answer/4365533) shows small volumes as zero; [Popular times](https://support.google.com/business/answer/6263531) appears only with enough data; [CDC WONDER](https://www.cdc.gov/pcd/issues/2019/18_0441.htm) suppresses counts under 10; Etsy shows sellers the search terms that found them ([help](https://help.etsy.com/hc/articles/115015774268)); Shopify reports top searches and searches with no results ([help](https://help.shopify.com/en/manual/online-store/search-and-discovery/analytics)).
- **Why ten:** F089's arithmetic (two searchers in a new market is nearly one person), and public-statistics practice.

**3. The front door** (web #1328; mechanism well-worn; the slot set is yours, call 2)
- The search box on top (the Ask bar when F119 lands), then **at most three slots**.
- Each slot is filled from the shelf pool by simple rules: new member or has history; day of week; time of day; what's timely (a reminder tonight, a seasonal shelf).
- New member or visitor: the market's story or a did-you-know, and the next seven days.
- With history: one slot may come from what they searched ("New since you looked for pottery").
- An empty slot is absent. Nothing scrolls past the third.
- Precedents: Yelp's Spring 2026 home feed is personalized by an AI model ([release](https://www.businesswire.com/news/home/20260421195188/en/)); [Nextdoor's 2025 redesign](https://blog.nextdoor.com/meet-the-new-nextdoor) leads with a few pinned modules (alerts, local news, Faves); Google Discover fills from activity. We take the bounded set and leave the endless feed.

**4. Hyper-specific search** (web #1329, well-worn)
- Item tags lead (#1318).
- Time words: "now", "tonight", "open now", "this week"; with them, soonest first.
- Vibe words ("cozy", "quiet", "kid-friendly", "outdoor") join the one dictionary, mapped to tags.
- Place words already work (F105, F107).
- No distance in ranking: `places.md` holds that for this version.

**What ranks the slots:** recency, time (happening soon), the member's declared interests and follows, their own searches. Never time spent, scrolling, payment or follower count (`model.md` § Personalized means interests, not engagement, updated 2026-11-15).

## Chat-first, folded in (CO-0041)

*The PM, 2026-10-26:* "I like being able to chat with an agent." Its near step is the Ask bar (F119); this concept puts that bar at the top of the front door, so search and the assistant are one box. Chat as the whole home (F120) stays later: the front door stays minimal. What a conversation is as a thing is still CO-0041's.

## Bring it to life

*The PM, 2026-11-15:* "I like that name and theme bring it to life. And it's crucial that the search [will] bring this about." Search is the main way members bring things to life together: an unmet search becomes an ask, a welcome, a maker partnership. The theme is a story map in the store; the soul line is `PRINCIPLES.md` § two-halves.

## Later

- **Assistant chat** that answers in conversation (Yelp Assistant, relaunched April 2026 as its own tab: [Yelp](https://www.yelp-ir.com/news/press-releases/news-release-details/2026/Yelp-Launches-the-New-Yelp-Assistant-Transforming-Local-Discovery-from-Search-to-Answers-and-Actions/default.aspx), [TechCrunch](https://techcrunch.com/2026/04/21/yelps-updated-ai-assistant-can-answer-questions-and-book-a-restaurant-or-service-in-one-conversation/)). Each turn costs a model call; the 2026-11-10 ruling allows no new paid tool before go-live unless it saves PM time. F119's router (one small call, a daily cap, falls back to search) is the step that fits now.
- **Saved-search alerts** (#725) and "Remind me when one joins" (the unmet-search brief).
- **A taste profile** a member can see and edit (F113), of which search history is the first piece.
- **Insights across markets** (F089's similar-community rollup).

## Privacy and legal

- **Search history is personal information** under CCPA/CPRA (Cal. Civ. Code §1798.140(v)(1)(F), "browsing history, search history"). The CCPA's thresholds are not met yet (`socialus-legal`), but CalOPPA requires the Privacy page to name what is collected, so it must say: searches are kept on your profile to tailor what you see, for how long, how to see and delete them, and that no one else sees them.
- **Producer counts** are aggregate consumer information (§1798.140(b)) once the floor holds. Whether the floor and area rule meet that definition is a question for counsel, sent to `socialus-legal` (not for the PM).
- **No stalking** is the test (PRINCIPLES, reworded 2026-11-15): no member or Page can piece together one person's searches. History is owner-only at the row level, like saved searches.
- California's SB 976 addictive-feed rules cover minors; members are 18+, and the front door is not a feed. Already with counsel (F098).

## What conflicts, and what this PR did

**Changed in this PR** (the PM's new words, or newer wins):
- The 2026-11-12 privacy principle: "can never be tracked" became no stalking, in the PM's words (full words in `member.md` § Rulings).
- `model.md`: a member's own searches count as telling us what they want; engagement stays refused.
- F098's 2026-10-04 "rows that keep going" ruling: replaced by the minimal front door (F136).
- F121 criterion 7: interest shelves may also come from a member's searches.
- F119 criterion 7: a member's own questions join their own history; counts stay anonymous.
- The unmet-search brief: "no one, staff included, can see who searched" became: the member sees their own; no Page or member ever learns who.
- F116: "per-member tracking" became "a per-member breakdown".

**Left for the build or a later pass** (each listed with its fix):
- **Live producer card** counts 3 searches, not 10 people: the insights Issue replaces it.
- **F089** (draft): criteria 4, 5 and 7 (metro only, bands, no Page-scoped view) are overtaken by F136; fold F089 into F136 at approval.
- **F098** (draft Home): the rest folds into F136 at approval.
- **F113** (draft taste profile): keep; history is its first piece.
- **Find/Discover principle** (2026-10-12): kept. The front door is Home, which `model.md` already lets personalize; Find may use a member's own signals (F059, 2026-10-31).
- **Build freeze** (2026-11-06, `what-this-is.md`): holds the build. Issues are filed and queued after the waitlist.
- **F064's 2026-09-15 ruling**, which says zero-result searches don't feed the dictionary, conflicts with F071 (2026-10-25) and F092 (2026-11-13). The newer rulings win; F064's line should go at the next sync.
- **policy.md**: "default off for non-essential sharing" is about sharing between members. History isn't shared, so this is kept.
- **Naming:** "front page" already means the signed-out landing page, so this is the **front door**.
- **F134's open question** (what signing up adds): a front door that knows you is one answer.
- **IMAGINE ideas this grows from:** Asked for, not here yet; Chat-first; Two sides; Holiday specials up front; Discovery that knows what a person is optimizing for. Linked as lineage when F136 is approved.

## Your calls, one at a time (most-unblocking first)

1. **How long your searches are kept** (blocks the history table).
   - **A (recommended): 18 months, then deleted on their own;** delete any or all any time. Google's default for new accounts. Long enough to learn seasons ("last spring you looked for seedlings").
   - **B: 90 days.** The 2026-11-01 taste-profile research's number. Less to hold, but the front door forgets each season.
   - **C: until you delete them.** Simplest. The most to hold, and the most to disclose.
2. **What the front door shows at launch** (look and feel): the slot set and its rules, as a live link behind the builders-only flag.
3. **The words:** "Your searches", the switch line, the producer card line, and the Privacy page paragraph.

## Verified vs assumed

- **Verified:** the code facts above, read from socialus-web main at `4a45ea5`; the plan sweep (rulings, criteria, briefs, IMAGINE); Yelp's privacy policy (searches personalize results; no separate delete-history control); Google My Activity, Popular times, Trends, Nextdoor's redesign post, and Craigslist saved searches, read in full.
- **Assumed:** Yelp's current home screen comes from its April 2026 release, not a live look; yelp.com blocked the browser. The Etsy and Shopify seller reports, Amazon Brand Analytics, and Google's 3, 18 or 36 month options rest on search summaries. CCPA section numbers come from a secondary copy of the statute.
- **The knowledge store** wasn't queried live; its lookup tool isn't connected to this session. The sweep read the files it imports from.
