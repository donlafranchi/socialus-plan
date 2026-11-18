---
id: brief-2026-11-18-recommendations-agent-led
status: awaiting-approval
size: L
path: new territory
fits: grows from the taste profile (F113, draft) and the Ask bar (F119, approved); held by the 2026-11-06 build freeze until the PM lifts it; the agent-led part waits for chat as home (F120, later)
criteria:
  - A member sees, in one place, everything SocialUs uses to recommend to them (asks, saves, "I went", "not for me"), each with its reason, and can delete one item, delete all, or turn learning off in one step; no other member, Page or visitor can read it (a test proves it, seen failing first).
  - A recommendation shown in chat or on a card says why in plain words ("because you asked for pottery evenings"), and "not for me" on it is never guessed back.
  - Nothing is learned from time spent, scrolling, or what a member looked at without acting; a test proves no such field is stored.
  - Matching a member to similar members switches on only in a market where it beats ask-matching on the same week's saves and "I went", judged with at least 10 members' worth of each; until then recommendations match what was asked to what is on nearby.
  - When SocialUs runs inside someone else's chat app, it keeps only what the member did through SocialUs's own tools and screens, and the member's record says which app each item came from.
---

# Recommending in an agent-led app: what members ask, what they do, and what we keep

**As of 2026-11-18** · Source: the PM's question of 2026-11-18; `PRINCIPLES.md`, `product/foundation/model.md` § Personalized means interests, not engagement, `what-this-is.md` § Rulings, F113, F119, F120, F121, `planning/research/taste-profile-2026-11-01.md`, the hyper-specific-search brief; the MCP Apps spec and the precedents linked below · Maintained by: hand (brief; deleted at 30 days or once ruled and placed)

*The PM, 2026-11-18:* "We want to collect taps from our users to find and deliver to them what's important. We will likely end up using something like MCP UI or MCP Apps and our platform will be natural language requests handled by agents. Would we need analytics if our users are asking us directly what they want using language? Then can we create patterns from users across the platform and recommend things based on similar users and not need analytics at all? Our goal was to be as good as TikTok's recommendation algorithm but we have different interaction patterns and so can't copy much of what TikTok captures."

**Bottom line: yes, mostly. Asking replaces most of what TikTok learns by watching, but not all of it: what a member says and what they then do differ, so keep a small record of both, owned and edited by the member (A). Don't log every tap (C), and don't rely on words alone (B). At hundreds of members, "people like you" doesn't work yet; match what each member asked for to what is on nearby, and switch on similar-member matching per market once it measurably wins. This is F113's taste profile, carried into chat.**

## The five questions, answered short

**1. What we get that TikTok doesn't, and what TikTok gets that we don't**
- **Ours, and stronger than anything TikTok sees:** the ask itself ("pottery class, evenings, Midtown"); a save; Remind me; directions or "how do I get there"; "I'm coming"; "I went" afterwards; "not for me"; a follow; a message to a maker. Each is a deliberate act with a stated reason, worth more per event than a view.
- **TikTok's, with no honest equivalent here:** watch time, rewatches, finishing a video, the skip after a second, and millions of these per member per month. TikTok's own account of For You leads with exactly these ([TikTok, 2020](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you/)); its training system updates on every view ([Monolith, ByteDance 2022](https://arxiv.org/abs/2209.07663)). We have few items, a few acts per member per week, and `model.md` refuses dwell and scroll time anyway.
- **So "as good as TikTok" means a different thing here:** not "knows what holds your eye" but "the thing you'd have wanted to go to, found before you'd have found it".

**2. Can what members say replace what they do?** Partly. Words are the best start and the wrong finish.
- **Words beat behaviour near the start.** With little or no history, language preferences recommend about as well as history-based methods ([Sanner et al., Google, RecSys 2023](https://research.google/pubs/large-language-models-are-competitive-near-cold-start-recommenders-for-language-and-item-based-preferences/)); conversational recommenders are built on asking ([Jannach et al., survey, 2021](https://arxiv.org/abs/2004.00646)).
- **Behaviour corrects words.** Netflix dropped stars for thumbs in 2017, saying "the implicit signal of your behavior is more important" than what people rated ([Netflix, 2017](https://about.netflix.com/en/news/goodbye-stars-hello-thumbs)). People ask for the aspirational ("more classical concerts") and go to the familiar.
- **But raw behaviour misleads too.** Engagement is not value: what keeps someone tapping differs from what they'd say was worth it ([Kleinberg, Mullainathan, Raghavan, 2022](https://arxiv.org/abs/2202.11776); [Milli, Belli, Hardt, 2021](https://arxiv.org/abs/2008.12623)). YouTube counts "valued" watch time from survey answers and trains a model to predict them for everyone ([YouTube, 2021](https://blog.youtube/inside-youtube/on-youtubes-recommendation-system/)); Meta does the same with "worth your time?" ([Meta, 2021](https://about.fb.com/news/2021/04/incorporating-more-feedback-into-news-feed-ranking/)). Nobody at scale replaces behaviour with words; they use words to say what counts as value, then weigh behaviour toward it.
- **For us:** the acts that close the loop are the ones that mean value, not attention: saved, reminded, went, came back, "not for me". Those are what to keep. Views, opens and time are not.

**3. Holding each member's history so it serves them**
- **One record, the member's:** asks, saves, reminders, "I went", "not for me", follows. Shown in You as "What we think you like", each item with its reason, deletable one at a time or all at once (F113's design, already ruled 2026-10-12 and 2026-10-25).
- **One switch:** "I don't mind doing this myself" stops learning and deletes raw signals (F113's ruling).
- **Raw acts fade:** F113 says 90 days; the search brief recommends 18 months for searches. Interests fade at their own speed (the taste research's "always loved / on occasion / passing spike").
- **Never sold, never another company's model** (the AI principle, 2026-10-25).
- **Similar-member matching can use the record without exposing it:** a member is matched to anonymous groups ("people who saved pottery and farm stands"), never to named people; nothing is shown that rests on fewer than ten members (the floor already used for producer counts). No member or Page can work backwards to one person ([no stalking], PRINCIPLES 2026-11-15).
- Precedents for a visible, editable record: [Spotify "Exclude from your taste profile"](https://engineering.atspotify.com/2023/10/exclude-from-your-taste-profile), [ChatGPT Memory](https://help.openai.com/en/articles/8590148-memory-faq) (see, delete, turn off, temporary chat), [Google My Ad Center](https://support.google.com/My-Ad-Center-Help/answer/12155451) (your topics, more or fewer), [Pinterest's Refine your recommendations](https://help.pinterest.com/en/article/tune-your-home-feed), and [Bluesky custom feeds](https://bsky.social/about/blog/7-27-2023-custom-feeds) (members pick the algorithm).

**4. At one region with hundreds of members: similar members, or ask-to-nearby?** Ask-to-nearby wins, for now.
- **Collaborative filtering needs overlap.** Similar-member matching works when many members have acted on many of the same things. Events are short-lived and in the future, so each one is "cold" ([Macedo et al., RecSys 2015](https://dblp.dagstuhl.de/rec/conf/recsys/MacedoMS15.html), already in the taste research): the signals that carry them are the group, place, time and the event's own content. Meetup's own recommender today weighs distance, topic fit, timing and RSVP popularity ([Meetup help](https://help.meetup.com/hc/en-us/articles/39488979117837-Location-recommendations)); knowledge-based recommenders have no ramp-up problem, which is why Burke's hybrid used them first and similar-user matching only to break ties ([Burke, AAAI workshop 2000](https://cdn.aaai.org/Workshops/2000/WS-00-04/WS00-04-003.pdf)).
- **Hundreds of members acting a few times a week** gives too little overlap per item; "people like you also saved" would rest on two or three people, under the ten-member floor and close to identifying them.
- **What works now:** match the ask and the member's record to what is on, by tag, place and time (F092's item tags, F136's time and vibe words, F121's shelves). An agent does this well: it reads the ask, reads the record, and picks from what's live.
- **When to switch on similar members:** per market, once a test shows it adds saves and "I went" over ask-matching alone, with ten or more members behind every pattern shown. Across markets, patterns from similar communities can help a new one sooner (F089's rollup).

**5. If members reach us through ChatGPT or Claude**
- **Verified in the MCP Apps spec** ([ext-apps, stable 2026-01-26](https://github.com/modelcontextprotocol/ext-apps/blob/main/specification/2026-01-26/apps.mdx)): a tap inside our screen goes to the host, which forwards a tool call to our server, adds a message to the conversation, or opens a link. The host may block or ask the member to approve any of these. Our screen can't call our own server directly unless we declare the domain and the host allows it.
- **So inside someone else's app we see only:** the tool calls the model chose to make (with arguments it wrote, not the member's words) and the taps on our screen that call our tools. We don't see the conversation, what the member said before or after, or taps that only message the model. Hosts listed today: ChatGPT, Claude, VS Code, Goose and others ([ext-apps README](https://github.com/modelcontextprotocol/ext-apps); [MCP-UI](https://github.com/MCP-UI-Org/mcp-ui)).
- **ChatGPT's rules point the same way:** apps collect only the minimum data needed and must not request full conversations or transcripts ([Apps SDK guidelines](https://developers.openai.com/apps-sdk/app-guidelines); [security and privacy](https://developers.openai.com/apps-sdk/guides/security-privacy)).
- **In our own app we are the host** and see every ask and tap, which is why the line in Q3 matters: we choose not to keep views and time.
- **What follows:** design our tools so the acts that matter are tool calls ("save", "remind me", "I'm coming", "I went", "not for me"); those reach us from any host. Use app-only tools (hidden from the model, callable only from our screen, which the spec allows) for saves and "not for me". The member's record notes which app each item came from. A member who is signed in through someone else's app sees the same record in You.
- **Risk:** in another app, the model decides what to send us. A member may ask ChatGPT for "pottery" and the model may search us for "craft classes". Asks seen there are weaker than asks typed into our own bar.

## Options

**A. A taste record each member owns, from what they ask and what they do (recommended)**
- Kept: asks (own app), saves, Remind me, "I'm coming", "I went", "not for me", follows, directions taps. Not kept: views, opens, time, scrolling.
- Visible and editable in You; one switch off; raw acts fade (F113).
- Recommends by matching the record and the current ask to what's on nearby; similar-member matching added per market when it wins.
- Precedents: Spotify's taste profile exclusions; ChatGPT Memory; Google Maps saved lists and "Want to go"; Eventbrite's like-and-follow recommendations (taste research § 2).
- Trade-off: some build (the record and its You screen); the member's control means some signal is lost when they delete or switch off. That loss is the point.

**B. Language only: recommend from what members ask, keep nothing else**
- Each ask is answered from what's on; no record of saves or visits.
- Precedents: plain search (Craigslist); a general assistant without memory; Google's language-preference study shows this works near the start.
- Trade-off: least to hold and disclose, but it never learns that a member asks for classical concerts and goes to jazz, can't tell "always loved" from "once", and forgets each season. Members must repeat themselves, against `#works-for-you`.

**C. Log every tap per person, TikTok-style**
- Every view, open, dwell and scroll per member, trained on continuously.
- Precedents: [TikTok For You](https://newsroom.tiktok.com/en-us/how-tiktok-recommends-videos-for-you/); [Monolith](https://arxiv.org/abs/2209.07663); Instagram Reels.
- Trade-off: refused already (`model.md`: never dwell, scroll or engagement; 2026-10-25 ruling: no tricks that work by keeping a member stuck). It also wouldn't work: hundreds of members and few items give it too little to learn from, and inside other chat apps we wouldn't see the taps at all.

## Recommendation: A

- **Why:** it uses the strongest signal we have (the ask) and corrects it with the acts that mean value (save, went, not for me), keeps nothing the member can't see, and works the same in our app and inside others.
- **Your question, "do we need analytics at all?":** for recommending, no tap logging beyond the record above. The anonymous product counts you already have (F133) stay for you, for a different job.
- **"Similar users" is the second step, not the first:** it waits per market until it beats ask-matching.

## How A would be measured

- **North star, per market, weekly:** of the things recommended to members, how many were saved, reminded, or marked "I went". Time and money together (`PRINCIPLES` § Measure) are the outcome.
- **"Did it find what you asked?":** share of asks where the member saved or acted on one of the first three answers.
- **"Not for me" rate,** falling over a member's first month.
- **Control:** the share of members who open their record, edit it or switch learning off; a rising off-rate is a warning, not a cost to push down.
- **Similar-member test:** ask-matching alone versus ask-matching plus similar members, split by week, judged only with ten members' worth of saves and "I went" in each arm.
- **What we never count:** time in app, scroll depth, sessions per day.

## What conflicts, and what this brief changes

- **F120 criterion 8** (draft) says chats are not used to profile. F119 criterion 7 (approved, amended 2026-11-15) and `model.md` (2026-11-15) already let a member's own asks feed their own record. The newer wins; F120's line should read "not used to profile for anyone but the member, or sold" at its approval. Not changed here.
- **F113** (draft taste profile) lists photo opens and Page opens as signals. A drops views and opens; if you pick A, F113 criterion 4 loses them.
- **F113 vs the search brief:** 90 days versus 18 months for raw acts. Your call on retention in the search brief settles both.
- **Build freeze** (2026-11-06) holds the build; nothing here is filed.

## Your calls, one at a time

1. **A, B or C** (recommend A).
2. **"I went"**: a new tap after an event, worth adding when the freeze lifts? It is the strongest value signal and doesn't exist today. Recommend yes.
3. **Opens and views out of the record** (changes F113): recommend yes.

## Verified vs assumed

- **Verified:** the MCP Apps spec and the ext-apps and MCP-UI READMEs, read in full (host forwards taps as tool calls or messages, may block or ask for approval, blocks undeclared network domains, app-only tools); the plan files cited.
- **Assumed:** every other external link rests on search summaries; this session's network refused arxiv.org, blog.youtube, newsroom.tiktok.com and developers.openai.com, so none was read in full. Netflix's reason is its own quote, not a measured finding. Whether ChatGPT or Claude pass any of the member's words beyond tool arguments: the spec doesn't say, OpenAI's guidelines imply not, neither host was tested. The ten-member floor for similar-member patterns borrows the search brief's number, untested here.
