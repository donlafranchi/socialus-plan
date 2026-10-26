---
id: F120
title: Chat is the way to use SocialUs, answering with real cards and acting only on a confirm tap
status: draft
horizon: later
rank: 1
date: 2026-10-26
depends: [F119]
---
## Story

*2026-10-26, the PM, verbatim:* "I like C. Let's use that as our direction … We don't need to work on that now but should come up with a near term and long term plan." This is the long-term half, after the soft launch and toward the hard launch; F119 is the near-term half.

A member opens SocialUs to a conversation. "What's on this weekend for kids?" gets three event cards inline, each one tappable. "RSVP me to the second one" shows "Say you're going to Saturday Story Time?" and acts only on Yes. An organizer types "post that the market moves indoors Sunday" and confirms the draft. A Wonder's poster asks "who's still undecided on size?" and gets the list.

## Acceptance

Draft criteria, to sharpen before approval:
1. **Answers inline with real cards**: answers are built from the same Pages, posts and events the pages show, as tappable cards. Nothing is invented: a card that doesn't exist in the data is never shown.
2. **Actions need a confirm tap**: the existing action registry in the code is the only set of tools. Each action is shown in plain words and runs only when the member taps to confirm.
3. **Chat as home**: the conversation becomes the first screen; every page stays reachable directly.
4. **Organizers by chat**: managers run their Pages (posts, edits) and coordinate Wonders (who's in, helpers, sizes) through the same confirm-tap actions.
5. **Visible memory**: anything the assistant remembers is listed where the member can see it, delete it, or switch memory off.
6. **Voice, later**: speaking a question is a later step on the same path.
7. **Daily limits**: per-member limits keep the cost down; past the limit, the member still has the pages.
8. **Privacy and moderation**: chats are not used to profile or sell; what the assistant posts for a member goes through the same moderation as anything else they post.
9. **The soul**: AI helps and never replaces a person; the benefit goes to members.

## Not this

An AI that posts, messages or RSVPs without a confirm tap. A companion or chatbot personality. Selling, or training on, members' chats.

## Why

- **Lives somewhere better?** Not for local: general assistants don't know local Pages.
- **Only locals know?** The cards are what locals posted.
- **Gets people together?** Yes: from a wish to an RSVP in one sentence.
- **Stays fresh on its own?** Yes: answers are read live.
- **Who keeps it current?** The action and page registries.
- **Better as more people join?** Yes: more to find, more organizers on it.

Precedents: ChatGPT apps and Claude tools (cards and tool calls with confirmation), Google Assistant's App Actions, Shopify Sidekick for merchants. Path: new territory for us (memory, cost, moderation), so it comes back to the PM before approval. Soul: `#works-for-you`, `#you-choose`, `#never-extractive`.
