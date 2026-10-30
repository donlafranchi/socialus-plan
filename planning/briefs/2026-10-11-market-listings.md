---
id: brief-2026-10-11-market-listings
title: Market listings (the shared foundation)
status: awaiting-approval
size: null
path: new territory
area: market-commerce (proposed; no Area label exists for it yet)
horizon: after beta, outside the Beta milestone
date: 2026-10-11
criteria:
  - L1.1 A producer can list an item from their own Page with a name, an optional price, and availability (in season, available this week, not this week)
  - L1.2 A listing says which market the producer sells at, and a producer can name more than one
  - L1.3 A producer can change a listing's availability or price, or remove it, in under a minute
  - L1.4 A listing with no price says nothing about price, and does not show "0"
  - L2.1 A market's Page shows this week's listings from the Pages that appear there, grouped by producer
  - L2.2 Each listing shows its availability in words
  - L2.3 A tap on a producer's name opens that producer's Page
  - L2.4 The market's week loads in under three seconds with 50 or more listings
  - L3.1 A listing carries no cart, checkout, stock count or payment control
  - L0.1 Empty states: no listing yet, none this week, no market named each say so in plain words
---

# Feature Brief: Market listings (the shared foundation)

**As of 2026-10-16** · Source: hand-written · Maintained by: hand (set by tend-docs from the last commit date; the owner confirms on next edit)

**As of 2026-10-12** · Source: hand-written · Maintained by: hand (set by tend-docs from the last commit date; the owner confirms on next edit)

**Goal:** A producer at a farmers market can say what they bring this week, in a minute, and a neighbour can see what the market has, when the market is on.
**Date / run by / PM context:** 2026-10-11 · plan-feature, one pass on a light model, chair merge · Don, voice-dictated: "we would need a way for the farmers market attendee to list products ... a simple way for them to list their products and possibly prices." A possibility, not a commitment. Likely T1 for both the Market shopper and Market meal plans.
**Scope line:** After beta. Not in the Beta milestone. This is the ROADMAP "Individual product and service listings on a Page (postponed until after beta, 2026-10-01)" item, now also the foundation for the market concepts.

## How the four pieces connect

```
                      Market listings  (T1, shared foundation)
                      a producer lists what they bring; a market's week
                         |                              |
              Market shopper                    Market meal plans
              asks are made against             plans are written against
              the week's listings               the week's listings
                         \                              /
                          Wish it existed (concept 3)
          a request is answered by an "I can build that" offer;
          a repeated wish becomes a listing; wishes show what to grow
```

- **Listings feed both market concepts.** The "carry list" the first brief asked for is simply the market's week of listings.
- **A wish can ask for either** ("someone to shop for me", "a week of meals for two toddlers from the market"), and an answer to a wish can become a listing once it is for sale.
- **Wishes tell producers what to bring.** This is the same idea as F089, search demand: what people want that does not exist locally.

## 1. Facts (Stage 0)

| Fact | Verified / assumed | Source |
|---|---|---|
| `/you/sell` is retired and redirects to Create; the list-a-product flow is kept, unrouted | Verified | `socialus-web` `src/app/you/sell/page.tsx` |
| The kept composer takes title, description, price or Free, unit and pickup location; `item.create` and a public product page exist; `items` link to a Page | Verified | `ProductComposer.tsx`, `you/sell/product/actions.ts` |
| Listings on a Page are postponed past beta; the starting point is the old sell flow moved onto the Page's Add | Verified | the After beta milestone (2026-10-01, 2026-10-05) |
| There is no availability or in-season field; stock indicators are Later | Verified | the composer; the After beta milestone |
| An Appearance (a Page at a Venue for a bounded time) is a noun, scoped at about 1.5 days and Later | Verified | `nouns.md`; the After beta milestone |
| A farmers market is a Page that convenes people | Verified | the 2026-09-15 ruling |
| Won't: cart, checkout, SKUs, inventory management as full products | Verified | what-this-is § Won't |
| Price on cards (Free, Donation, Paid) is speculative, not ruled | Verified | After beta, speculative |
| The kept composer still builds and runs after the retirement | **Assumed** | ticket 1 settles it |
| Producers will list weekly if it takes about a minute | **Assumed** | the pilot (T0) of the other briefs |

## 2. Prerequisites

| Missing | Owner | Needed by |
|---|---|---|
| An availability field on a listing (in season, this week, not this week) | Architect | T1 |
| "Sells at this market" for a producer's Page: the Appearance noun, or a plain tag on the listing as a stopgap | Architect, then Don's ruling | T1 |
| A market's weekly view (listings of the Pages that appear there) | Architect | T1 |
| Don's ruling that listings return to the Page's Add after beta | Don | T1 |

## 3. Area → Feature → Journey → Criterion

**Area:** market-commerce (proposed). **Feature:** Market listings (unnumbered).

| Journey | Who and what | Zero state |
|---|---|---|
| **L1 A producer lists their week** | Opens their Page, taps Add, enters an item, an optional price, availability, the market | "Nothing listed yet. List what you're bringing." |
| **L2 A neighbour sees the market's week** | Opens the market's Page and reads the week's listings | "Nothing listed for this week yet." |
| **L3 A producer says it's gone** | Changes availability or removes an item | n/a |

Criteria are in the frontmatter, each tagged to its journey. All binary.

## 4. Roles (chair-merged)

| Role | Needs | Cost | Veto | One risk |
|---|---|---|---|---|
| Person (browsing) | Sees what the market has, the price if there is one, and whether it is there this week | Twenty seconds | A listing that shows stock that is gone | A visit on Monday finds no list yet |
| Maker (the producer) | Lists in about a minute, optional price, can say it is gone | Weekly upkeep | Required photos, stock counts, or more than four fields | Listing at the wrong market, or forgetting to update |
| Money | Listings are free; SocialUs earns only when a sale happens (ruling 2026-10-07) | none now | Charging to list; a cut before a sale | A listing leads to a sale off the app |
| Architect | An availability field; a "sells at" link; the market's week view | Two new fields and one view, on the kept items | A second source of truth for what a market carries | Old items orphaned from a market |
| Developer | Re-route the kept composer onto the Page's Add; add the new fields | See sizes | Building stock sync, a cart or an order system | The composer depends on the retired walkthrough |
| Tester | List, edit, remove, view as a stranger; every empty state | Two producers, one market | A non-binary criterion | A weeks-old listing taken for current |
| Operator | Hide a bad listing fast; no review before publishing | A report path that already exists | A person needed midweek | A deleted market leaves listings behind |
| Guardian | Prices as the producer's own words; no promise of freshness or quality | none | Implying SocialUs vouches for a product or a licence | Prepared food listed with no guidance |
| Scout | See precedents | none | none | Precedents bundle logistics and payments that do not exist here |

**Flag for socialus-legal (no detail):** food rules and licences, price accuracy, liability.

## 5. T1 / T2 / T3

| | **T1 (the foundation)** | **T2** | **T3** |
|---|---|---|---|
| Ships | Producers list items from their Page: name, optional price, availability, which market; a market's Page shows the week | "Every Saturday" repeat; a photo; grouping by kind; edits keep a note of when | Search inside a market; a quantity as a plain note; follow a producer or market |
| Hours (estimate) | **about 24 to 30.** The committee said 6 to 7 if the kept composer is clean; the chair's estimate is higher because it was built for the retired walkthrough and the market link and availability are new. Ticket 1 is a spike that settles it | about 20 | about 40 |
| Existing data only? | Mostly: the kept items and composer | Mostly | No (quantities, repeat) |
| Proves | Producers list and neighbours read the week | Weekly upkeep is light enough to keep up | Listings are useful enough to search |
| Leaves out | Photos, repeats, search, any sale or order | Search, quantity | Inventory counts, checkout (Won't) |
| Trigger to move up | Ten producers listing in one market for four weeks | Lists stay current for six weeks | Neighbours ask to search |

## 6. How each concept uses a listing

- **Market shopper:** an ask is made against listings; the shopper reads the same week. Nothing else about shopping needs a new list.
- **Market meal plans:** a plan is written against the week's listings and carries the list date; a plan says so when the listings change.
- **Wish it existed:** an "I can build that" offer, once it is for sale, is a listing.

## 7. Gates

- [x] Prerequisites listed, each with an owner
- [x] Criteria binary
- [x] Zero states defined (section 3)
- [ ] Copy written to voice rules: not yet (post-beta)
- [x] Guardian: no promise broken; legal flagged without detail
- [x] **Kill criterion:** fewer than ten producers across two markets list anything in four weeks of T1: stop, and ask five producers why
- [x] **Metric:** producers who list at least once a week, per market. Real people, not attention.
- [ ] Tickets: none until Don approves a size
- [ ] Assumed facts verified as ticket 1: whether the kept composer still runs

## 8. Precedents

Looked up this run: [Market Wagon](https://farmprogress.com/marketing/online-delivery-business-links-local-farmers-and-customers) (producers control their own listings, stock and prices; copy that, skip the hub and delivery); [CSA](https://csacoalition.org/about-csa) (a fixed weekly offering and a pick-up point; skip the pre-season commitment); [Nextdoor For Sale and Free](https://about.nextdoor.com/press-releases/nextdoor-expands-its-buy-sell-and-give-feature-with-the-launch-of-free-finds) (a neighbour lists in a few fields, with a Neighbor Made category).

## 9. For Don (only what he alone can answer)

**A.** Return listings to the Page's Add after beta, as T1 for both market concepts. B. Return them to the Page's Add **now-ish** (before the freeze, kept hidden) so the market pilot can run on real listings. C. Keep listings out entirely and run the pilots (T0) on posts alone. Recommend A: B touches the beta freeze, C learns less.
