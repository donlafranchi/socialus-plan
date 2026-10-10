---
id: research-reclaim-standing-rule-2026-10-10
purpose: Where "use what's available, for the people it comes from" becomes a standing rule, everything it touches today, and what to call it. Proposal only; nothing here is ruled.
layer: research
status: draft
authored: Claude agent, 2026-10-10, at Don's request (voice-dictated)
---

# The standing rule: use what's available, for the people it comes from (2026-10-10)

**Proposal only.** Nothing here is a ruling until Don gives it as a dated `DECISIONS.md` line. It corrects the first voice pass (`copy-voice-pass-2026-10-10.md`), which framed the position as rejecting data collection. What Don means: we collect data and use the same tools others use to extract, but only for the benefit of the people they come from, never to enrich shareholders, executives or anyone else.

## The rule and its test

> We use the tools others use to extract. We point them at the people they come from.

The tool is never the problem. The aim is. Every use of data, or of any technique built to extract (targeting, personalization, analytics, AI, ranking, notifications), answers two questions:

1. **Whose is it?** The members it comes from.
2. **Who gains?** Only those members, in a way they can see and turn off. Nobody else is enriched, including partners, sponsors, vendors and us.

A use that passes is allowed, even if a platform elsewhere would do the same thing to its users. A use that fails stays out. This is why streaks and pull-back notifications stay refused: they fail question 2, so they need no separate ban.

It reverses nothing already settled. No shareholders, no selling member data, members are the investors, "never extractive": all stand. It changes one thing: several rules today refuse a *tool* outright (see *Reopened*), where this rule refuses the *aim*.

## What to call it

| | Name | Why | Against |
|---|---|---|---|
| **A (recommended)** | **Reclaim** | A verb, so it reads as a practice. Admits the tools are the same ones. Pairs with the one allowed "never": we refuse extraction, we reclaim the tools. Short enough to say in a meeting. | Slightly political. |
| B | Common Use | Data and tools held in common, used for the common good. Fits "owned by the people". | Abstract; reads like policy. |
| C | Same Tools, Our Side | Plain and a little wry, close to the voice. | Long; hard to use as a verb or a slug. |

Recommend A. In a sentence: "We reclaim the tools." In copy: "We use the same tools as everyone else, for the people they come from." The test above is the **source test**: whose is it, who gains.

## Where it becomes standing

Make it live in layers, because a rule agents must remember is a guard nobody runs. Each layer already exists; this adds to it rather than inventing a new place.

1. **The constitution: `product/foundation/goals.md`.** `product/ABSOLUTES.md` points there for "the product's one value absolute", so this is the home. Add a named section beside "The one thing refused: extraction", and reword promise 3 from only refusing ("No selling member data") to refusing the aim and naming the practice.
2. **A dated ruling in `DECISIONS.md`**, with a `[binds tiers=planning,code …]` tag, so `constraints/` regenerates and every build agent reads it. This is what makes it reach the work.
3. **A product absolute** in `product/ABSOLUTES.md`, next to `member-data-disclosure`. It passes the four-harms test (harm to a member). Don decides whether it is an absolute or a guideline; suggested slug `data-serves-its-source`.
4. **Two checks that already run.** `product/foundation/value-test.md` (six questions every scenario answers in its `## Why`, lint-checked from F103) gets a seventh: the source test. `product/foundation/policy.md` (three filters plus the opt-out default) gets the same line, so every data-touching spec states who gains.
5. **Legal.** `socialus-legal/entity/principles.md` item 6 ("No extraction") gets the affirmative half. Terms and Privacy say what each thing collected is for.
6. **Voice.** `voice-and-tone.md` § What we say carries the one-line version.
7. **Culture.** Suggestions only, each needs Don: a yearly public page listing what we collected and who it served; members can export or delete their data (already named in `impact-diagnostic.md` as portable identity); a community vote before any new data use, extending the "one member, one vote" already ruled for give-back.

## What it touches

### Already in line

- `goals.md` promises 2, 3 and 6; `impact-diagnostic.md` (restore information symmetry, reduce switching costs).
- F089 search demand: Don's 2026-09-15 ruling that it serves "creators" and "members" both, aggregated, a floor of ten members, raw rows deleted after 30 days. The first live example of this rule.
- Venues: we send traffic to their own channels and credit them (2026-09-30).
- `socialus-legal/entity/principles.md` items 5 and 6; give-back in `product/systems/contributions.md`, which is the money half of the same rule.

### Reopened: refused today, needs Don's call per item

| Where | Refused today | Under the rule |
|---|---|---|
| `monetization.md` § Refused outright | Behaviorally targeted advertising; data sales or licensing | Sales and licensing stay out (they enrich others). Targeting is allowed only when it serves the member it is about. Sponsorship and ads stay an open question. |
| `model.md` § Personalized means interests; `discovery.md` | Personalization only on declared interests; "anything reading behaviour back at them is refused" | Behavior-based suggestions become possible if they help the member and they can see why and turn them off. |
| `metrics.md` anti-metrics; `ROADMAP.md` Won't | Engagement metrics, streaks, pull-back notifications, visitor-tracking analytics for a producer, mass email | Streaks and pull-back notifications stay out (they fail the test). Measuring what helps members, and producer analytics that serve the people tracked, are judged case by case. |
| `goals.md` promise 3 | "No selling member data" | Widen to "no using member data to enrich anyone else", and add the affirmative half. |
| `policy.md` opt-out default | Non-essential sharing off by default | Stays. Add: opt-in states who gains. |
| `IMAGINE.md`, F089 follow-ons | Market intelligence, sponsorship forms | Evaluate with the source test rather than a blanket no. |

### Live in the product today

What the app collects now, and who gains, from the code and the legal starter. Each needs an honest answer to "who gains":

- Email, phone (Twilio check), legal name, zip, 18+ box. Gains: the member (safety, metro, accountability).
- IP and time on posts and uploads, kept one year, operators only. Gains: safety for members.
- Error tracking (Sentry). Gains: working software. Confirm it sends no member content.
- Saved searches, follows, RSVPs. Gains: the member.
- Reports and the AI first pass (Anthropic, as a processor). Gains: members, if the vendor cannot train on or keep the content. Counsel should confirm the contract says so.
- Unclaimed business Pages built from public information (#353). The hardest current case: data taken from businesses who did not ask. Today it is credited, removable, labeled. Check it against the rule before it grows.
- Third parties that see queries (geocoding, map tiles). Confirm what they receive.
- The legal starter lists Vercel Analytics; I found no analytics package in the app. One of the two is out of date.
- Ranking: weights change only through code review (`discovery.md`), nothing is boosted by payment.

### Copy

- Signup line, About, Privacy, phone step, waitlist note, landing: "never shown" and similar become "currently don't", and one line says what collection is for. Suggested: "What we collect is used for the members it comes from, not to enrich anyone else." Folded into the voice pass.

### How the work is done

- Feature intake (`planning/council/feature-intake.md`) and the brief template: add the source test.
- Build agents: no new third-party script, tracker, SDK or data recipient without stating who gains. Add to the review checklist.
- Vendors and partners: who receives member data, and can they resell or train on it.

## For socialus-legal

- A public "we use data only for the members it comes from" is a wider commitment than "we don't sell". Counsel should define "enrich others" (processors, AI vendors, sponsors, partners) before it is published.
- CCPA wording in `terms-privacy/starter.md` ("we currently do not sell or share") should stay consistent with it.

## Not read

I read the foundation, systems, legal and decision files named above and searched the rest by keyword. I did not read every scenario (F048 to F102) end to end, so some scenario criteria may carry a touchpoint not listed here.
