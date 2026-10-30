---
id: brief-2026-10-11-market-shopper
title: Market shopper
status: awaiting-approval
size: null
path: new territory
area: market-commerce (proposed; no Area label exists for it yet)
horizon: after beta, outside the Beta milestone
date: 2026-10-11
criteria:
  - S1.1 A market's Page can post what it has this week, with a date, and a signed-out visitor can read it
  - S1.2 A member can offer to shop a market for neighbours from a Page of their own, with no new member type
  - S2.1 A member can ask a shopper for specific items from a market's list, with a budget
  - S2.2 A shopper can see open asks for one market and claim one; a claimed ask leaves the list for other shoppers
  - S2.3 Both people can see the ask's state: asked, claimed, picked, handed over
  - S2.4 The handoff happens in person at a place named on the market's post
  - S3.1 A producer can list what they carry this week in under two minutes
  - S3.2 A producer can offer the same service for their own regulars (pre-orders held at their stall)
  - S4.1 A shopper's rate or fee is shown before an ask is claimed
  - S4.2 SocialUs holds no funds; money moves between the people (off-app until on-platform payments exist)
  - S0.1 Empty states: no list yet, no shopper yet, no asks yet each say so in plain words
---

# Feature Brief: Market shopper

**As of 2026-10-16** · Source: hand-written · Maintained by: hand (set by tend-docs from the last commit date; the owner confirms on next edit)

**As of 2026-10-12** · Source: hand-written · Maintained by: hand (set by tend-docs from the last commit date; the owner confirms on next edit)

**Goal:** A member who cannot get to the farmers market can have a neighbour shop it for them, and farmers and producers can do the same for their own regulars, when the market is on.
**Date / run by / PM context:** 2026-10-11 · plan-feature, one pass on a light model per concept, chair merge · Don, voice-dictated: "a shopper like at Walmart but at a farmers market, and then how could we replicate that for farmers and producers." A possibility, not a commitment.
**Scope line:** After beta. Not in the Beta milestone (beta 2026-11-06, freeze 2026-10-30). Nothing leaves scope because nothing enters it.

*Don's words, 2026-10-11.* Two separate concepts that could be combined or not. This is the first; the second is [Market meal plans](2026-10-11-market-meal-plans.md).

## Why it fits (members first)

- **Flip 1, toward in-person.** Walmart and Instacart shopping replaces the visit. Here the handoff happens at the market, between neighbours, so it brings a person to the market instead of keeping them home.
- **Flip 2, spreading wealth among the many.** The money goes to the member who shops and the producers who grow, not to one corporation or one gig platform. SocialUs takes transaction income on member commerce (ruling 2026-10-07) and keeps what it needs to run.
- **Who it serves first:** the person who cannot get to the market (no car, a new baby, a bad week), and the producer whose regulars cannot come every Saturday.

## 1. Facts (Stage 0)

| Fact | Verified / assumed | Source |
|---|---|---|
| A farmers market is a Page that convenes people (a gathering Page); a given Saturday is a dated post with a time and place | Verified | the 2026-09-15 ruling; `model.md` |
| A Page's managers post; a Post can carry a date, a place and tags | Verified | `member-journey.md`; capabilities F072 |
| There is no messaging between members and no substrate for it | Verified | `member-journey.md`; the After beta milestone |
| The platform handles no money; on-platform payments are Later (closed-loop ledger, ACH via a chartered partner) | Verified | the After beta milestone; Terms draft |
| Product and service listings on a Page are postponed past beta | Verified | the After beta milestone |
| SocialUs takes transaction income on member commerce | Verified | the 2026-10-07 ruling |
| Won't: cart, checkout, inventory management as full products; funds held for the platform's benefit; pull-back notifications | Verified | what-this-is § Won't |
| A role is a relation, not a member type | Verified | `nouns.md` |
| One metro (Sacramento) at beta | Verified | ROADMAP |
| Whether a Sacramento market would post a weekly list, or whether producers would | **Assumed** | none; the first thing a pilot answers |

## 2. Prerequisites (no noun, verb or surface yet)

| Missing | Owner | Needed by |
|---|---|---|
| **Market listings** (a producer lists an item, optional price, availability, tied to their Page and the market). This is the shared foundation: see [Market listings](2026-10-11-market-listings.md). Its combined weekly view is the market's "carry list", so no separate carry-list noun is needed | Architect | T1 (it is T1) |
| An ask (a member's request for items from a listing) and its states | Architect | T2 |
| Messaging between members, or an in-ask status line that replaces it | Don (messaging is Later) | T2 |
| On-platform payments | Don (Later) | T3 |

## 3. Area → Feature → Journey → Criterion

**Area:** market-commerce (proposed; Areas today are create-posts, explore-map, moderation, page-editing, sign-in-you).
**Feature:** Market shopper (unnumbered; an F number is assigned when it becomes a scenario).

| Journey | Who and what | Zero state |
|---|---|---|
| **S0 Anyone** | Sees what the market has this week | "No list posted for this week yet." |
| **S1 The market posts its week** | A market's manager posts what is here, dated | "Nothing posted for this week. Post what's here." |
| **S2 A neighbour is shopped for** | A member asks, a shopper claims, they meet at the market | "No shoppers for this market yet. Be the first to offer." |
| **S3 A producer shops for their regulars** | A producer lists what they carry and offers pre-orders held at their stall | "Nothing listed for this week." |
| **S4 The shopper is fairly paid** | Rate shown up front, money moves between the two | no zero state; the rate is required |

Criteria are in the frontmatter, each tagged to its journey (S1.1 and so on). All binary.

## 4. Roles (chair-merged; each ran at 200 words or less)

| Role | Needs | Cost | Veto | One risk |
|---|---|---|---|---|
| Person (asking) | A neighbour they can trust to shop for them; to see items and a budget before the day; no substitution without being asked | A fair fee to the shopper; no markup on the goods | A subscription or standing order; their purchases shared with anyone | The shopper drops out the day before |
| Maker (the shopper; the producer) | The shopper sets and sees their own rate; the producer lists in two minutes and can still sell directly | Time at the market; list upkeep | Platform lock-in; producers forced to hold stock for asks | A producer sells out to walk-ins before the shopper arrives |
| Money | Rate shown first; SocialUs earns transaction income per the ruling; no float | Processor fees once payments exist | A cut that grows with dependence (goals promise 3); tips as the real pay | Cash-flow strain if both sides expect to be paid first |
| Architect | Three new nouns (carry list, ask, a shopper's claim) on top of Page and Post | A second state machine | A second source of truth for what a market carries | A carry list that drifts from the real stall |
| Developer | A first slice that works alone | See sizes | Building checkout or delivery routing | Dependence on messaging and payments that are Later |
| Tester | Binary criteria; every empty state | Multi-person test data | A non-binary criterion | Two shoppers claim one ask (a race) |
| Operator | Self-service; no queue to moderate midweek | Near zero | Anything needing a person Tuesday to Thursday | A shopper forgets to mark an ask picked |
| Guardian | In-person, wealth-spreading, member-benefit | none | Engagement ranking of shoppers; push notifications | Opt-out and privacy of purchase history |
| Scout | See precedents | none | none | None of the precedents combine in-person handoff with neighbour earnings |

**Flag for socialus-legal (no detail):** food handling and safety, payments, liability and insurance, how a shopper's work is classified.

## 5. Who earns

- The member who shops (a fee they set, shown before claiming).
- The producers whose goods are bought (their full price, no markup).
- SocialUs, transaction income on the sale per the 2026-10-07 ruling. Nothing is promised to any member beyond what each earns on their own sale.

## 6. T0 / T1 / T2 / T3 (pilot, then the three sizes)

Don, 2026-10-11: the listing foundation is likely T1 for both market concepts, so T1 is shared and the no-build pilot becomes T0.

| | **T0 Pilot** | **T1 Listings foundation (shared)** | **T2 Right-sized (recommended)** | **T3 Full** |
|---|---|---|---|---|
| Ships | Nothing built. The market's Page posts "what's here this week"; one member's Page offers to shop it; asks arranged outside the app | Producers list items (optional price, availability, which market) from their Page; the market's Page shows the week's listings | An ask on a listing, a shopper's claim, four states; handoff place from the market's post; money outside the app | Payments through the chartered partner; a shopper working several markets; order history |
| Hours (estimate) | 0 to 8 | about 24 to 30, see the listings brief | about 40 on top of T1 | about 120 or more |
| Existing data only? | Yes | Mostly: reuses the kept composer and item.create; availability and the market link are new | No: two new nouns (ask, claim) | No: payments, messaging |
| Proves | Whether anyone posts a weekly list and asks | Producers will list; neighbours read the week | The ask, claim, handoff loop works for strangers | The economics hold with money in the app |
| Leaves out | Anything in-app | Asks, shoppers | Messaging, payments | Delivery routing, inventory sync, checkout (Won't) |
| Trigger to move up | Four market weeks with a posted list and two real asks | Ten producers listing in one market for four weeks | Ten completed handoffs in one market | Payments exist (Later) and a second market asks |

## 7. Gates

- [x] Prerequisites listed, each with an owner
- [x] Criteria binary
- [x] Zero states defined (section 3)
- [ ] Copy written to voice rules: not yet (post-beta)
- [x] Guardian: no promise broken; legal flagged for counsel without detail
- [x] **Kill criterion:** in the pilot (T0), fewer than two real asks across four market weeks: stop, and ask the market's manager and three producers why
- [x] **Metric:** completed handoffs per market per week (an ask picked and handed over in person). Real-world meetings, not attention.
- [ ] Tickets: none until Don approves a size
- [ ] Assumed facts verified as ticket 1: whether a Sacramento market will post a weekly list

## 8. Precedents

Looked up this run:
- [Instacart shoppers](https://dollarsprout.com/become-an-instacart-shopper): an independent contractor takes an order in an app, shops, delivers; paid per batch plus tips. Copy the clear job; skip tip-dependence and the delivery that replaces the visit.
- [Market Wagon](https://farmprogress.com/marketing/online-delivery-business-links-local-farmers-and-customers): an online farmers market where producers keep control of their stock and the company is courier and marketplace. Copy producer control; skip the central hub.
- [CSA](https://csacoalition.org/about-csa): members commit to a farm, with a pick-up point. Copy the pick-up point and the producer relationship; skip the up-front commitment.

Recalled, not looked up: Walmart Pickup (store staff pick, the customer collects).

## 9. Combining with the meal plans

A plan's shopping list could go to a shopper, as eMeals sends lists to Instacart. Neither needs the other.

## 10. For Don (only what he alone can answer)

**A. Park both concepts in IMAGINE until after beta.** B. **Run a no-build pilot at one Sacramento market once beta is open** (recommended: T1 of both, zero code, learns whether anyone wants it). C. Pick one to build first after beta (meal plans: it is information, with less legal weight).
