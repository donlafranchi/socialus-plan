---
id: brief-2026-10-11-market-meal-plans
title: Market meal plans
status: awaiting-approval
size: null
path: new territory
area: market-commerce (proposed; no Area label exists for it yet)
horizon: after beta, outside the Beta milestone
date: 2026-10-11
criteria:
  - M1.1 A market's Page can post what it carries this week, dated, readable signed out
  - M2.1 A member can write a plan of one meal, a couple of days, or a week, tied to one named market; each length is complete on its own
  - M2.2 The plan shows which ingredients are on that market's list for the week and which are not
  - M2.3 A plan is saved with the date of the list it was written against
  - M2.4 The author's name on a plan leads to the author's own Page, not a public member profile
  - M3.1 A plan appears on its market's Page, newest first, and a family can read the whole plan and its shopping list before choosing it
  - M3.2 A family keeps a plan after getting it; it is not removed when the market's list changes
  - M3.3 The shopping list can be printed or saved as plain text, not only seen in the app
  - M3.4 A family can choose one meal without taking a whole week
  - M4.1 When the market's list changes, a plan written against an older list says so in plain words
  - M4.2 A plan older than 14 days is marked as written for an earlier week
  - M5.1 An author can see how many families chose their plan, and says "Nobody's chosen it yet" at zero
  - M0.1 Empty states: no list yet, no plans yet, no market named each say so in plain words
---

# Feature Brief: Market meal plans

**As of 2026-10-16** · Source: hand-written · Maintained by: hand (set by tend-docs from the last commit date; the owner confirms on next edit)

**As of 2026-10-12** · Source: hand-written · Maintained by: hand (set by tend-docs from the last commit date; the owner confirms on next edit)

**Goal:** A family can have a week of meals planned around what their farmers market has this week, written by a neighbour, when they want to cook from the market.
**Date / run by / PM context:** 2026-10-11 · plan-feature, one pass on a light model per concept, chair merge · Don, voice-dictated: "recipes for families that used the ingredients that were at a farmers market ... a week full of meals ... created by members of the community, and then they can sell their meal plan ... in reference to a farmers market and what that farmers market carries." A possibility, not a commitment.
**Scope line:** After beta. Not in the Beta milestone (beta 2026-11-06, freeze 2026-10-30). Nothing leaves scope because nothing enters it.

*Don's words, 2026-10-11.* A second concept, separate from [Market shopper](2026-10-11-market-shopper.md), which it can combine with or stand without.

## Why it fits (members first)

- **Flip 1, toward in-person.** A plan sends a family to the market with a list. Unlike a plan tied to a chain's sale items, the shopping happens in person, with the people who grew the food.
- **Flip 2, spreading wealth among the many.** The author is a neighbour who earns on their own work; the producers sell their own goods at their own prices; no corporation sits between. SocialUs takes transaction income on member commerce (ruling 2026-10-07) and keeps what it needs to run.
- **Who it serves first:** the family who does not know what to cook with a bag of kale; the neighbour who loves to cook and wants to be paid for it; the producer whose unusual crop finally has a recipe.

## 1. Facts (Stage 0)

| Fact | Verified / assumed | Source |
|---|---|---|
| A farmers market is a Page that convenes people; a given Saturday is a dated post | Verified | the 2026-09-15 ruling |
| A Page's managers post; a Post carries a date, place and tags; the search dictionary is seeded with farmers-market items | Verified | `member-journey.md`; the 2026-09-12 ruling |
| No messaging between members; the platform handles no money; payments are Later | Verified | `member-journey.md`; the After beta milestone |
| Listings on a Page are postponed past beta | Verified | the After beta milestone |
| No public member profile; someone who wants to be found makes a Page | Verified | After beta, speculative |
| Won't: full e-commerce, checkout, inventory management as products | Verified | what-this-is § Won't |
| A plan is information (recipes and a list), not food | Chair's reading of Don's words | this brief |
| A market, or its producers, would keep a weekly list current | **Assumed** | none; the first thing a pilot answers |

## 2. Prerequisites (no noun, verb or surface yet)

| Missing | Owner | Needed by |
|---|---|---|
| **Market listings** (what a market's producers carry this week): the shared foundation, see [Market listings](2026-10-11-market-listings.md). Its weekly view is the list a plan is written against | Architect | T1 (it is T1) |
| A plan and a recipe (nouns), tied to a market and a list date, in three lengths | Architect | T2 |
| A way for a family to get and keep a plan | Architect | T2 |
| Payments, if plans are sold in-app | Don (Later) | T3 |

## 3. Area → Feature → Journey → Criterion

**Area:** market-commerce (proposed). **Feature:** Market meal plans (unnumbered).

| Journey | Who and what | Zero state |
|---|---|---|
| **M1 The market posts its week** | A market's manager (or a producer) posts what is here, dated | "Nothing posted for this week. Post what's here." |
| **M2 An author writes a plan** | A member writes one meal, a couple of days, or a week against the week's list; the plan flags what is off the list | "No market named yet. Pick the market this plan is for." |
| **M3 A family finds and keeps a plan** | Reads the whole plan first, then keeps it | "No plans for this market yet. Want to write one?" |
| **M4 The week moves on** | The list changes; the plan says it was written for an earlier week | n/a |
| **M5 The author sees it was used** | A count of families, in words | "Nobody's chosen it yet." |

Criteria are in the frontmatter, each tagged to its journey. All binary.

## 4. Roles (chair-merged)

| Role | Needs | Cost | Veto | One risk |
|---|---|---|---|---|
| Person (the family) | Meals that fit the week's list, a list to print, a plan that still works if one item is gone | Time to read; the plan's price once payments exist | Recipes calling for things the market does not have | The list changes after the family has chosen |
| Maker (author; producers) | Their name on the plan (via their own Page); a way to be paid; producers see their goods used | Time to write and to keep it in step with the list | No relationship to the market; no way to earn | A stale list makes the author's plan look careless |
| Money | Families pay the author; SocialUs earns transaction income per the ruling; authors earn enough to keep writing | Processor fees once payments exist | A cut that grows with volume or dependence (goals promise 3) | So little earned that few write plans |
| Architect | Plan, recipe, carry list; verbs: write, tie to a market, update the list, keep | Three new nouns | A plan edited after a family kept it, with no record of the change | The carry list is never updated, orphaning plans |
| Developer | A first slice that works alone | See sizes | Payments in the first slice | Markets post their lists in different shapes |
| Tester | Binary criteria; the "item no longer carried" state | Test data for two markets | A criterion that is not binary | A tester takes a weeks-old list for current |
| Operator | Self-service; no midweek work | Watching for stale lists | A list left unattended for more than a week | At 10 users a market stops posting |
| Guardian | Recipe attribution; plain words, no health claims | One legal read before launch | A plagiarised recipe; missing allergen notes | A plan titled with a health claim |
| Scout | See precedents | none | none | The plan-matched-to-a-store pattern (eMeals) serves the store; this one serves the market's people |

**Flag for socialus-legal (no detail):** recipe rights, health and dietary claims, allergens, payments, liability.

## 5. Who earns

- The author, for each plan a family chooses (price set by the author, once payments exist).
- The producers, through the sales the plan sends them at their own prices.
- SocialUs, transaction income on a sale per the 2026-10-07 ruling. Nothing else is promised to any member.

## 6. T0 / T1 / T2 / T3 (pilot, then the three sizes)

Don, 2026-10-11: the listing foundation is likely T1 for both market concepts, so T1 is shared and the no-build pilot becomes T0. **Plans come in three lengths: one meal, a couple of days, a week**, so authors and families can start small. One meal is the starting point everywhere below.

| | **T0 Pilot** | **T1 Listings foundation (shared)** | **T2 Right-sized (recommended)** | **T3 Full** |
|---|---|---|---|---|
| Ships | Nothing built. The market's Page posts its week; one member's Page posts **one meal** as a Post tagged with the market, then a few days, then a week | Producers list items (optional price, availability, which market); the market's Page shows the week's listings | A plan and recipe form in three lengths, tied to a market and a list date; plans on the market's Page; a printable list; money outside the app | Plans sold in-app; versions; search across markets; recommendations |
| Hours (estimate) | 0 to 8 | about 24 to 30, see the listings brief | about 40 on top of T1 | about 100 or more |
| Existing data only? | Yes | Mostly (reuses the kept composer) | No: plan and recipe nouns | No: payments, recommendation |
| Proves | A family cooks from a neighbour's one-meal plan; a market posts a list | Producers list and a plan can be written against real listings | The plan-to-market link works at all three lengths | The economics hold with payments |
| Leaves out | Tying, flags, a printable list | Plans | Payments, search, versions, dietary variants | Delivery, inventory sync (Won't) |
| Trigger to move up | Four weeks with a posted list and three plans used | Ten producers listing in one market for four weeks | Five plans for one market and a list kept current for six weeks | Payments exist (Later) and authors in a second market |

## 7. Gates

- [x] Prerequisites listed, each with an owner
- [x] Criteria binary
- [x] Zero states defined (section 3)
- [ ] Copy written to voice rules: not yet (post-beta)
- [x] Guardian: no promise broken; legal flagged for counsel without detail
- [x] **Kill criterion:** in the pilot (T0), fewer than three families use a plan across four market weeks: stop, and ask the author and two families why
- [x] **Metric:** families who shop the market with a plan in a week (the plan author asks "did you use it?"). Real-world meetings, not attention.
- [ ] Tickets: none until Don approves a size
- [ ] Assumed facts verified as ticket 1: whether a Sacramento market will post a weekly list

## 8. Precedents

Looked up this run:
- [eMeals](https://emeals.com/how-it-works/): weekly meal plans matched to a grocery store's sales, with a list sent to a grocer for pickup. Copy the week-at-a-time plan and the list; skip tying it to one chain's sale items.
- [CSA](https://csacoalition.org/about-csa): a weekly box of one farm's produce, so a family gets what is in season; no plan comes with it, which is the gap a plan fills.
- [Market Wagon](https://farmprogress.com/marketing/online-delivery-business-links-local-farmers-and-customers): a market's goods ordered online, with producers controlling their listings. Copy producer control of what is listed.
- [Instacart shoppers](https://dollarsprout.com/become-an-instacart-shopper): the shopping a plan's list could hand to a neighbour (see the Market shopper brief).

## 9. For Don (only what he alone can answer)

**A. Park both concepts in IMAGINE until after beta.** B. **Run a no-build pilot at one Sacramento market once beta is open** (recommended: T1 of both, zero code, learns whether anyone wants it). C. Pick one to build first after beta (meal plans: it is information, with less legal weight).
