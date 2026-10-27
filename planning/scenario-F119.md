---
id: F119
title: A member asks or taps ➕, and the app opens the right widgets filled in, and organizers see what neighbours look for
status: approved
horizon: next
rank: 2
date: 2026-10-26
approved: 2026-10-26 — the PM chose chat-first (option C) as the direction and asked for a near-term plan; build after the current Now work
depends: []
---
## Story

*2026-10-26, the PM, verbatim:* "I'm thinking of a very different way of organizing this app too. I like being able to chat with an agent. What would it take for my app to have a similar experience to a chat app?" Then: "I like C. Let's use that as our direction and the users question opens one of these pages e.g. /you or /explore or other pages for example."

A member types "anything fun this Saturday near Midtown?" into the Ask bar. Explore opens filtered to Saturday and Midtown. Another types "did anyone reply to me?" and lands on You → Notifications. A third types "I want to sell my sourdough" and gets a post draft with the words filled in, ready to edit. Nothing is answered in chat yet: every question ends on a page that already exists.

## Acceptance

1. **Ask bar and ➕**: one text box, on every signed-in page, that takes a question in plain words; and one ➕ as the single place to start anything (a post, an event, a Wonder, a Page).
2. **Routing**: one cheap model call (the smallest current Claude model) turns the prompt into a workflow: which widget opens, with which settings filled in. "Weekly run club Saturday mornings" opens the composer set to weekly, Saturday, 7am, near the member; "anything fun this Saturday near Midtown?" opens Explore filtered.
3. **Fallback**: if the call fails, times out, or finds no page, the question runs as an ordinary search. The member always lands somewhere.
4. **Deep links**: every widget and every setting it takes can be reached by URL (Explore by date, category and place; a Page; You's settings and Notifications; the composer with text, kind and schedule; a Wonder).
5. **One widget registry**: a single list in the code describes each widget, its URL and its settings. The router reads only that list and can't open a widget that isn't on it, or invent one.
6. **Nothing is done for the member**: the router only opens pages. A prefilled draft is not posted until the member posts it.
7. **Questions logged by the search-demand rules** (F089): anonymous, aggregated (a floor of ten members, one metro), raw rows deleted after 30 days, never tied to a member in anything shown.
8. **Opt-out**: one setting stops a member's questions being logged; routing still works for them.
9. **Cost cap**: a per-member daily limit on model calls, after which the bar falls back to search.
10. **Search analysis**: nightly, Claude Haiku through the Batch API tags each logged search (intent, category, place, time window, matched or not, a normalised query); weekly, unmet demand is clustered per area and shown to creators and organizers (the owner card, a "what neighbours are looking for" list, suggested Wonders), under criterion 7's rules. Not DeepSeek's hosted API (member trust). Plan: `planning/research/chat-first-plan-2026-10-26.md`.

## Not this

Answers written in chat, cards in a conversation, actions taken for the member, memory, voice, chat as the home screen (F120).

## Why

- **Lives somewhere better?** No: a general chat app doesn't know local Pages, posts and events.
- **Only locals know?** The answers do; the bar just gets a member to them faster.
- **Gets people together?** Yes: fewer taps between a wish and the event or Page.
- **Stays fresh on its own?** Yes: it opens live pages and stores no answers.
- **Who keeps it current?** The widget registry, updated with each new widget or setting.
- **Better as more people join?** Yes: more questions show what people look for (F089).

Precedents: Google's search box opening an app's deep link (App Actions), Airbnb's and Expedia's natural-language search filling filters, Linear's command bar. Path: well-worn. Soul: `#works-for-you`, `#out-of-the-way`. Sins: none.

[platform none]
