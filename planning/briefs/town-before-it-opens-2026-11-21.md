---
id: brief-2026-11-21-town-before-it-opens
concept: CO-0065
status: awaiting-approval
size: L
path: new territory
fits: builds on F119 (Ask bar, approved), F120 (chat with real cards, draft), F136 (hyper-specific search and the minimal front door), F118 and F123 (town pages, makers by kind), F124 (cost covered) and F134 (visitors read everything); held by the build freeze (D-0275) until the PM lifts it for this
criteria:
  - The front door is one box; a question there opens one widget from a fixed, tested library and fills it from the database; no widget shows a Page, post, person or number the database does not hold (a test with an invented place proves it, seen failing first).
  - With no model at all, every question still lands on a widget by rules (where/near → map, time words → what's on, a town plus "open" or "how" → town dashboard, a kind alone → results, nothing typed → Browse); a test suite of at least 50 real questions from the search log routes as labelled.
  - A map appears only when the answer is spatial or the member asks for one; there is no standing map button, and a "Browse" chip gives the old Explore without typing.
  - The town pulse shows activity by neighbourhood only: no dot for a person, no cell shown below the PM's floor of different people, delayed at least an hour; a test with one active member in a sparse neighbourhood proves that cell stays dark.
  - Nothing floats or is listed as a wish unless it maps to a known item tag or category, passed post screening, was searched by at least ten different people in that market, and is a few minutes old; commentary floats only after it passed screening and has a report path (D-0383, member-content-takedown).
  - "Me too" counts once per person into the same aggregate producers see (F136, never who), and everyone who said it is told when a Page that carries it opens or is claimed.
---

# The town before it opens, through a chat-first front door

**As of 2026-11-21** · Source: hand-written · Maintained by: hand (set by tend-docs from the last commit date; the owner confirms on next edit)

**As of 2026-11-21** · Source: the PM's words below; Chat-first SocialUs (CO-0041), Two sides (CO-0035), Asked for (CO-0043), F118, F119, F120, F123, F124, F128, F133, F134, F136, the unmet-search and welcome brief, the producer count rule (D-0402), the build freeze (D-0275), PRINCIPLES · Maintained by: hand (brief; deleted at 30 days or once ruled and placed)

*The PM, 2026-11-21:* "I have a couple concepts. I want to talk to you about four socialist and one is how to make the app a little bit more interesting to get a little bit of more interaction when I'm thinking is for The people who have joined but can't sign up because they're not in their market that we still allow them to do search and tell them why with the searches for essentially, and that as people do searches, they the searches kind of scroll by similar to how Facebook and TikTok do hearts and emojis when a person taps a heart and that they scroll by on the screen and float from maybe bottom to top or something like that as a way too, have people kind of check in and see what what are people talking about? What are people asking for? What are people saying?"

*Then:* "I think that encompass both concepts and they were a way to make that interesting to use similar to how Instagram and TikTok or interesting to users and not just a discovery tool. I see this app as a discovery tool and while that's necessary and useful, I don't think it's very engaging so I'm trying to think of ways to make it engaging and then the second topic was about the waitlist people and signing up in basically creating their community through their searches or conversations"

*Then, on the map:* "I wonder if this is a good use case for the Matt [map] as well if a person can brings up a map and see what's active in their town this is the idea I mentioned earlier about some kind of dashboard for a market or an area. The dashboard could be how many people are commenting and communicating and how many sign ups and how many people there are that have businesses and maybe what kinds of businesses and I love the different ways that you described with interacting and it doesn't necessarily have to be something I want or something before, but it could be anything related to the town any kind of commentary otherwise I'm not seeing a huge use case for the map outside of this. It's not quite as hopeful as I thought it would be."

*Then, on the front door:* "What there's also means is that we should convert this to a chat first app and start trying to incorporate some generative UI for example a person says where are the local cattle ranchers to me or people who sell beef perhaps then that pulls up a map otherwise I don't know that we need a map button buttons are good for searching for things like hotels or Airbnb's or restaurants are running errands but maybe ours is show me where all the options are with live music tonight and that can pop up on a map."

*And:* "Is there a use case where we have a predefined UI for questions like this and so instead of explore going away it may be goes away as a dedicated screen, but maybe it stays as a predefined UI widget same with the map for these kinds of tasks"

**Bottom line: make the front door one box that answers with a fixed library of tested widgets (results, map, what's on, Browse, town pulse, town dashboard, floating wishes, town board). Start with no AI model, rules only, for towns that aren't open yet; add a cheap model to pick widgets at go-live. Explore and the map stop being screens and become widgets.**

**Your call:** which first slice: A, B or C?

*In the store:* this brief names its concept (CO-0065), so each version reaches the store as a dated change on it. The PM's pick is recorded as a dated ruling under `## Rulings` in `product/foundation/what-this-is.md`, where chat-first was ruled, so the import carries it too.

## The picture

Maya in Vacaville (waitlisted) types "who sells beef near me". A map opens with three ranches in Dixon and Winters, pins at their public precision. She types "live music tonight": a short list of tonight's shows, with "see on map". She types "pottery class": nothing here yet. *"Every search tells local makers what Vacaville wants."* She taps **Me too** and watches Vacaville's wishes and neighbours' tips drift up: *sourdough · pottery class · "the farm stand has peaches this week" · kids' climbing*. "How's Vacaville doing?" brings the town card: 41 locals, 6 makers (food 3, shops 2, groups 1; still missing: coffee), people talking this week, 38% of its cost covered, and how close it is to opening. "What's going on in town?" brings the pulse map: Downtown glowing, Alamo quiet, no dots for anyone.

## Scope, said once

This changes the core UI. **Leaves as a screen:** Explore (becomes the Browse widget and a "Browse" chip), the Map pill and its toggle, the filter sheet (the box takes "this weekend, kid-friendly" instead). **Shrinks:** the bottom bar. **Stays:** every Page, post and You screen, reachable by link (F119's deep links). The build freeze holds new features until the 2027 launch; the smallest slice touches only people in towns that aren't open, so beta members' screens don't change until the PM says so.

## Options: the first slice

- **A. Rules only, towns not yet open (recommended).** The box routes by words to the widgets below; waitlisted people get search, nothing-found with "me too", floating wishes and the town dashboard. No model, about $0, no new paid service before go-live (F128). Misses some phrasing; the log shows which.
- **B. A model picks the widget, everywhere.** The smallest Claude model, through Vercel's AI Gateway, turns each question into a widget and its filters. Handles any phrasing; a new paid service, so after go-live under F128; about $7 a month at 1,000 questions a day.
- **C. Hybrid.** Rules first; the model only when rules can't place a question. Most of B's reach at a fraction of the calls. The natural second step after A.

**Recommend A now, C at go-live.** It proves the widget library and the waitlist loop at no cost, and every question it can't place becomes the training list for C.

## Options: the map

**Honest read:** counting is in place (map taps since 2026-11-02, F133 usage counts since 2026-11-12), but no invited cohort has arrived, so there is no real map use to judge yet; I couldn't read the live counts from here. "Explore → Show the map" is one of the five slowest taps on the speed check.

- **M1. The map becomes a widget (recommended):** it opens for "where" questions and as the town pulse; no standing button. Its two real jobs, nothing else.
- **M2. It stays a secondary tool:** today's Map pill on Explore, unchanged.
- **M3. Both:** the widget, plus a map button kept on Browse.

## The widget library

Every widget is built and tested once, filled from the database, never from model text (F120 criterion 1: nothing invented).

| Widget | Questions that open it | Rules (no model) | With a model |
|---|---|---|---|
| Results (cards) | "sourdough", "who fixes bikes" | a kind or item alone | picks kind, item, vibe |
| Map | "where are the cattle ranchers", "beef near me", "live music tonight on a map" | where, near, around, map | spots spatial intent in any phrasing |
| What's on | "tonight", "this weekend", "kid-friendly Saturday" | time words | time plus vibe |
| Browse (old Explore) | nothing typed, the Browse chip, "what's around" | empty or browse words | same |
| Page card | a Page's name | exact name match | fuzzy names |
| Nothing found | a search with no results | zero results | same |
| Floating wishes and talk | waitlisted front door, "what does Vacaville want" | town not open, or "want/wish" | same |
| Town dashboard | "how's Vacaville doing", "when does it open" | town plus open, how, doing | any phrasing |
| Town pulse map | "what's going on in town", "what's busy" | town plus going on, active, busy | any phrasing |
| Town board | "ask the neighbours", "has anyone…" | ask, anyone, recommend | drafts the question; posting needs a tap |
| Welcome | on opening, for "me too" people | an event, not a question | same |

The box is still F136's front door: one box, then at most three slots. A member's questions join their own search history, which only they see and can delete (F119.7, F136).

## The town pulse and dashboard

- **Pulse map:** activity by neighbourhood (posts, comments, board posts, RSVPs, new Pages), never a person's dot, delayed at least an hour, a neighbourhood dark until enough different people are active in it (default ten, like D-0402). In public, locality is coarse; no stalking.
- **Dashboard:** people talking this week (counts), sign-ups (F076's one combined number), Pages by kind with what's still missing (F123), top wishes, how close it is to opening (F118), and how much of its cost is covered (F124; PRINCIPLES 2026-11-01).
- **What floats:** wishes (a known category, ten or more different people, delayed) and town commentary: board posts, questions and tips that passed screening, with a report path. A set plays and stops; reduced-motion gets a still list. A check-in, not a feed.

## Cost

Vercel's AI Gateway charges the provider's list price with no markup ([pricing](https://vercel.com/docs/ai-gateway/pricing)). Claude Haiku 5.5 is $0.10 in and $0.50 out per million tokens; Claude Sonnet 5.5 is $2 and $10.

| Questions a day | Rules only (A) | Haiku picks the widget (B) | Hybrid, a third to the model (C) | Sonnet writes a reply too (not recommended) |
|---|---|---|---|---|
| 100 | $0 | about $0.70 a month | about $0.25 | about $36 |
| 1,000 | $0 | about $7 | about $2.50 | about $360 |
| 10,000 | $0 | about $68 | about $23 | about $3,600 |

Assumes about 1,500 tokens in and 150 out to pick a widget ($0.0002 a question) and 4,000 in and 400 out to write a reply. Widgets speak for themselves, so no written replies.

## Checked against the rulings

- **AI helps people and doesn't stand in for them:** the answer is always real local Pages and people; the model only picks which widget to show.
- **What an assistant knows belongs to the member:** questions go to the member's own history, deletable, one switch off.
- **No new paid tool before go-live (F128):** A uses none; B and C start at go-live.
- **Works for you; the north star is time and money:** bounded widgets and a float that stops, no feed, no streaks.
- **In public, locality is coarse; no stalking:** pulse by neighbourhood with a floor, wishes and counts never tied to anyone.

## Precedents

- **Fixed widgets filled by a model:** [Vercel AI SDK generative UI](https://ai-sdk.dev/docs/ai-sdk-ui/generative-user-interfaces) (a tool call renders a React component); [apps in ChatGPT](https://openai.com/index/introducing-apps-in-chatgpt/) (conversations open an app's own cards); [Slack Block Kit](https://api.slack.com/block-kit) (fixed blocks, filled per message); [Siri](https://developer.apple.com/design/human-interface-guidelines/siri) and [Google Assistant App Actions](https://developer.android.com/develop/devices/assistant/overview) (answers as an app's cards).
- **Local answers:** [Google's local pack](https://support.google.com/business/answer/7091) (a fixed map-plus-three-results block on local searches); [Google AI Mode](https://blog.google/products/search/ai-mode-agentic-personalized/) (a curated list with booking links); [Yelp Assistant](https://www.yelp-ir.com/news/press-releases/news-release-details/2026/Yelp-Launches-the-New-Yelp-Assistant-Transforming-Local-Discovery-from-Search-to-Answers-and-Actions/default.aspx) (local search to answers, as its own tab).
- **Why buttons still suit some tasks:** [Airbnb](https://www.airbnb.com/) and Yelp lead with where, when and who, because a booking has fixed fields; SocialUs keeps that only as the Browse chip.
- **Live maps of a place:** [Snap Map](https://en.wikipedia.org/wiki/Snap_Map) heat map; [Google Maps busy areas](https://blog.google/products-and-platforms/products/maps/keep-it-chill-holiday-new-tools-google-maps/) (differential privacy, never a head count); [Waze](https://en.wikipedia.org/wiki/Waze) (reports from people, shown live); [Citizen](https://en.wikipedia.org/wiki/Citizen_(app)) (a live incident map criticized for fuelling fear, a tone to avoid); [Strava's global heatmap](https://en.wikipedia.org/wiki/Strava) exposed military bases in 2018 because sparse areas showed single people: the reason for the floor.
- **Floating reactions:** [Periscope hearts](https://en.wikipedia.org/wiki/Periscope_(service)); [Facebook Live Reactions](https://fortune.com/2016/04/06/facebook-beefs-up-live-video/), [adjusted in July 2016](https://thenextweb.com/news/facebook-updates-live) when emoji floated over hard-hitting videos.
- **Live search tickers, 1990s:** [MetaSpy](https://en.wikipedia.org/wiki/MetaCrawler) kept a filtered view beside an unfiltered one; [Excite's Search Voyeur](https://anildash.com/1999/10/12/search-engine-q/) streamed raw searches; Ask Jeeves had "Peek Through the Keyhole". Raw queries were offensive and revealing, and [AOL's 2006 search log release](https://en.wikipedia.org/wiki/AOL_search_log_release) showed searches can identify a person. [Google Trends](https://support.google.com/trends/answer/4365533) shows only terms with enough volume.
- **Before a town opens:** [Nextdoor](https://en.wikipedia.org/wiki/Nextdoor) opened a neighbourhood at ten households, with a founding member; [Clubhouse](https://en.wikipedia.org/wiki/Clubhouse_(app)) waitlists let people reserve a name; [Midjourney](https://en.wikipedia.org/wiki/Midjourney) ran its whole early community in Discord.

<details><summary>How each piece maps to what exists</summary>

- **The box:** F119's Ask bar and page registry become a widget registry; F120's "real cards, confirm tap" is the widget rule.
- **The engine:** F136 hyper-specific search and item tags leading search (web #1318); the chat is the voice in front of it.
- **Me too:** the unmet-search brief's reminder, plus one count into F136's producer aggregate (web #1327).
- **Add a place you love:** F118's add-a-maker form makes an unclaimed Page ready to claim.
- **Town pages:** F118 (built behind a flag, web #1093), F123 (makers by kind, still missing), F124 (cost covered); the next-moves per-market dashboard notes (sign-ups, money raised, share of cost met).
- **Founders and welcome:** F118 recognition only (2026-10-31); the unmet-search brief's welcome, widened to the town.
- **Town board:** courtesy-first report path (D-0076), screened before publish (D-0383).
- **Usage:** F133 counts which widgets get used, so the library is pruned by evidence.

</details>
