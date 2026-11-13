---
id: what-assistant
purpose: What the in-app assistant is for a member, what it may and may not do, and when it must get a tap.
layer: what
status: active
---

# Assistant

*Index of every product doc and its settled rules: [`../README.md`](../README.md).*

The in-app assistant is meant to become a first-class way to use SocialUs, next to browsing and search (Don, 2026-11-13: *"we're moving toward an agent assistant as a first class interaction system"*). This file is what it is for a member. How its permissions are enforced is in `socialus-web` `docs/action-layer.md`, not here.

## What a member can count on

- **Reads can be automated; writes need a tap.** The assistant may look things up for a member, but anything it would publish or change waits for the member's own confirmation tap, never one the assistant mints.
- **A member grants it, scoped and expiring.** A Delegation is a permission a member gives a non-human actor, narrow and short-lived. Only a member can grant or withdraw one; Groups hold none, and Group-coordination agents are platform-curated (`groups.md`).
- **It acts as the member, on the record.** Every write it makes is attributed to the member and to the Delegation that allowed it.
- **It never holds a member's credentials,** and nothing it reads can make it act as someone else.
- **Refusals are by absence:** an action that is not in the catalog cannot be asked for. Whether an action should exist runs through the three-filter test in `foundation/policy.md`.

## Status

Delegation and member-context tables exist since launch with no surface (`member.md` § Substrate reserved at launch for agent assistance). Nothing the member can see yet.

[open-question owner=don raised=2026-11-13] What is the assistant's first job for a member: search ("find me a quiet patio"), doing things (post, RSVP), or something else? It decides which actions enter the catalog first.

Related: if agent search replaces keyword search, SocialUs should be the agent for its own domain (`foundation/policy.md`, 2026-09-21), which is where the hyper-local search concept points.
