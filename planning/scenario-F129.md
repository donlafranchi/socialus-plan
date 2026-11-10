---
id: F129
title: Anyone can ask what SocialUs can and can't do, and get a short true answer
status: approved
horizon: next
rank: 3
date: 2026-11-10
approved: 2026-11-10, the PM: "I'd like a similar pattern for 'What SocialUs Can Do' ... somewhat brief and describe what users can and can't do in the app"
depends: [F125, F126, F127]
---
## Story

*The PM, 2026-11-10, verbatim:* "in addition to the question 'How We Work' I'd like a similar pattern for 'What SocialUs Can Do' or something else along the lines of What's built in the app. This should be somewhat brief and describe what users can and can't do in the app."

The PM opens the "code good" project on his phone and asks what a Page owner can do today. The answer is a dozen plain lines: post an event, edit the Page, see who's in. Then "not yet: take card pre-orders (waiting on card payments)". It matches what is live on socialus.org that morning.

## Acceptance

1. **One answer, by who is asking:** a visitor without an account, a member, and someone who runs a Page or an event; each a short list of what they can do and what they can't yet.
2. **Plain and brief:** one line per thing, in words a member would use, no ticket or scenario numbers; the whole answer under 1,500 words.
3. **Can means proven:** a line goes under "can" only when its feature slice (F127) is shipped and its checks and the live smoke test pass; anything else is not listed as possible.
4. **Can't yet says why:** each "can't yet" names the condition (F126) it waits on, or "not planned", in plain words.
5. **Asked through the store:** "what can SocialUs do", optionally for one kind of person, is one call to the lookup tool and returns this answer with each line linked to its feature.
6. **A pack for a chat project:** the same answer is written as one Markdown file in `socialus-plan` whenever a slice ships, is withdrawn or changes condition, and once a month regardless.
7. **It stays true:** if a "can" line's live smoke test fails, the line moves to "can't right now" until it passes.
8. **It takes over** the capabilities page written today by hand-run `regen` (capabilities), after a week side by side.

## Not this

Telling members what is coming and when (later, with the public side). How the app works inside. Marketing copy.

## Why

- **Lives somewhere better?** No: only the store knows which features are shipped and proven today.
- **Only locals know?** No: it describes the app, not the place.
- **Gets people together?** Yes, later: a member's agent that knows what the app can do points people to events and Pages instead of guessing.
- **Stays fresh on its own?** Yes: it is rewritten when a slice ships or its smoke test fails.
- **Who keeps it current?** The store and the checks; nobody edits it by hand.
- **Better as more people join?** Yes: more features shipped means more true lines, and the same answer serves every person and agent who asks.

**Path: well-worn.** Apple and Google publish what each app can do and on which devices from their own release data ([Apple feature availability](https://www.apple.com/ios/feature-availability/)); Stripe's docs list what each account capability enables ([Stripe](https://docs.stripe.com/connect/account-capabilities)). Stage 2 of the F125 store. [platform none]

## Rulings

- **2026-11-10 — "What SocialUs can do" is one short answer by kind of person, listing only what is shipped and proven live, with what can't be done yet and why.** The PM, for F129. [binds tiers=planning,code surfaces=knowledge,capabilities]
