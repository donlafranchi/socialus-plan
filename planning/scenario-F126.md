---
id: F126
title: Decisions and features wait on exactly the conditions they need
status: approved
horizon: now
rank: 2
date: 2026-11-10
approved: 2026-11-10, the PM: "yes to conditions", and they must be fine-grained, not all or nothing
depends: [F125]
---
## Story

*The PM, 2026-11-10, verbatim:* "we aren't adding certain functionality until certain other things are in place. Right now we have nothing for payments because the infrastructure isn't set up yet." Then: "I can imagine a scenario where we begin to add payments and add a small version of the full implementation that could unlock some features/functionality but not others. we need a way to be adaptable and not be all or nothing."

Payments is a condition made of parts: take a one-off card payment, pay out to a seller, refunds, holding funds, tax forms. The first part is built and its check passes. That day the PM gets one Issue: card pre-orders and the two decisions parked on card payments are ready; payouts and refunds stay parked, each naming the part it waits on.

## Acceptance

1. **A condition is a record** in the F125 store, with a why, an owner, a status (not started, partial, met, withdrawn) and, where one exists, the check that decides it is met.
2. **Conditions have parts:** a condition can be made of other conditions; the parent's status is computed from its parts (partial while any is unmet, met when all are) and is never set by hand.
3. **A condition can be a number crossing a line** (members in a metro at or above N), decided by a scheduled query.
4. **Two ways to wait:** a decision, feature or slice of a feature links to any condition or part with `starts when` (parked until it is met) or `ends when` (holds until it is met). Waiting on one part does not wait on the whole.
5. **Both questions in one call each:** "what does this condition unlock", and "what is this waiting on", following parts all the way down.
6. **One batch when something is met:** when a condition or part becomes met, one GitHub Issue lists everything it starts or ends, and nothing is sent item by item.
7. **Parked means parked:** an agent asked about something parked answers with the condition it waits on, and the lookup tool refuses to mark parked work as building.
8. **Runs without a computer:** checks and thresholds run on a GitHub Actions schedule; the PM marks a condition met or withdrawn through the lookup tool or an Actions run from his phone.
9. **Today's waiting lines come in as proposals:** the `until` text of `[for now]` rulings and scenarios' `gates:` and `depends:` become proposed conditions, grouped by meaning, listed for the PM in one Issue to confirm.

## Not this

Versions and what is in or out of each (a proposal in the F125 brief, stage 2). Building payments. Time-based conditions with no check or owner.

## Why

- **Lives somewhere better?** No: feature-flag tools gate code, not decisions and their whys; nothing we use links a ruling to the capability it waits on.
- **Only locals know?** No: this is how the platform remembers what it is waiting for.
- **Gets people together?** Indirectly: parked features come back the day they can work, instead of being forgotten or built too early.
- **Stays fresh on its own?** Yes: checks and thresholds run on a schedule, and a met part announces what it unlocks.
- **Who keeps it current?** Agents record what waits on what as they decide; the PM confirms conditions and marks the ones no check can decide.
- **Better as more people join?** Yes: thresholds on members and metros unlock features as the platform grows.

**Path: well-worn.** Stripe gives each connected account separate capabilities (card payments, transfers), each inactive, pending or active, and a product unlocks by the capability it needs ([Stripe](https://docs.stripe.com/connect/account-capabilities)). LaunchDarkly makes one flag wait on another's state ([LaunchDarkly](https://docs.launchdarkly.com/home/flags/prerequisites)). [platform none]

## Rulings

- **2026-11-10 — Decisions and features wait on conditions, and conditions are fine-grained: a condition has parts, and something unlocks when the parts it needs are met, not the whole.** The PM, for F126. [binds tiers=planning,code surfaces=knowledge] [always]
