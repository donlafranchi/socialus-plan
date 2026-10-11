---
id: brief-2026-10-11-wish-it-existed
title: Wish it existed (requests for things that may not exist locally)
status: awaiting-approval
size: null
path: new territory
area: market-commerce (proposed; it also touches create-posts and discovery)
horizon: after beta, outside the Beta milestone
date: 2026-10-11
criteria:
  - W1.1 A member can post a wish: a title, a description, an optional picture, an optional budget in their own words, and tags
  - W1.2 Anyone signed in can reply to a wish with a public offer: what they would build, a price or fee in words, and a way to be reached that the replier chooses
  - W1.3 The member who posted sees every reply on their wish, in order, with the replier's name
  - W1.4 A reply shows no button to pay, hire or message; the two people arrange the rest outside the app
  - W1.5 Starter examples sit in their own bounded block with a heading and a "Sample" mark, are not returned by search, and have no reply, follow or link control
  - W1.6 A real wish and a Sample are not shown in the same list
  - W1.7 A wish can be closed by the member who posted it; a closed wish says so and takes no new replies
  - W1.8 A wish can be reported with the existing report control
  - W1.9 Tags let a replier find wishes in their kind of work
  - W1.10 Empty states: no wishes yet, no replies yet, and a closed wish each say so in plain words
  - W1.11 Money moves only between the people; SocialUs holds none and the screen does not suggest otherwise
---

# Feature Brief: Wish it existed

**Goal:** A member can ask the neighbourhood for something they want that may not exist locally, and neighbours can answer "I can build that" with a price, or team up, when they have a want like a small frog habitat.
**Date / run by / PM context:** 2026-10-11 · plan-feature, one pass on a light model, chair merge · Don, voice-dictated: "I want a cute little frog habitat for my backyard ... a tiny thing that has a pond, running water, a little bit of plants ... it may exist somewhere but probably not locally ... can we post things like that as starter examples and see how the community responds, maybe someone says hey I can build that and offers to do so for some kind of a price or fee, or they work together to create something, and then we can see ideas like that as we think of them." A possibility, not a commitment.
**Scope line:** After beta. Not in the Beta milestone.

*Don, 2026-10-11.* A third concept, separate from the two market concepts. It connects to them (see [Market listings](2026-10-11-market-listings.md) for the map) but needs nothing from them.

## Why it fits (members first)

- **Flip 1, toward in-person.** The thing gets made by a neighbour and handed over in person; the want starts a conversation between two people who live near each other.
- **Flip 2, spreading wealth among the many.** The money goes to the member who builds, not to a catalogue company that does not make it. SocialUs earns only on a sale (DECISIONS 2026-10-07).
- **Who it serves first:** the person with a specific want the shops do not stock; the neighbour who can make things and has no way to be found for it.

## 1. What this is, and what it is not, in the plan today

| In the plan | State | What this concept adds |
|---|---|---|
| **Idea** (schema `wonder`): someone puts a new thing to the neighbourhood and others signal interest before it exists | Substrate only; signalling, threshold and conversion undesigned; ruled 2026-09-15: no conversion into another entry type, the author makes the new Page themselves | It is the same thing, with one new move: a reply that is an **offer to build** |
| **Offer / Ask** (schema `offer`, `ask`): entry types exist | No composer; blocked on the missing reply channel | An "I can build that" is an Offer. **A wish is an Ask or an Idea** |
| **Discussion message**: a reply on a Page's board, one level deep | Not built | The reply channel this needs, in its smallest form: one level of public replies on a wish |
| **F089 search demand** (draft) and **F064** (a tap on something not built) | Search demand is aggregated: a floor of ten members, one metro, raw rows deleted after 30 days; "resolved by somebody starting it" | A wish is the **member-written** form of that demand |
| **Sample rule** (DECISIONS 2026-09-17): examples live in their own marked block, not in search, not interactive | Ruled | Limits how starter wishes can appear (section 7) |

So the honest answer to "is this new?" is: **mostly no.** It is the undesigned half of Idea, plus one reply that carries a price. The brief is that design.

## 2. Facts (Stage 0)

| Fact | Verified / assumed | Source |
|---|---|---|
| Idea has substrate only; the signalling mechanic is undesigned | Verified | `nouns.md`, `verbs.md` |
| `nouns.md` says an Idea has no expiry; `verbs.md` says it expires at 90 days | Verified (an open inconsistency) | the two files |
| No messaging, no reply channel; Volunteering (offer/ask) is blocked on it | Verified | `nouns.md`, ROADMAP Later |
| No public member profile; a member who wants to be found makes a Page | Verified | ROADMAP Speculative (2026-10-01) |
| The platform handles no money; payments are Later; no auctions or dynamic pricing | Verified | ROADMAP Later, Won't |
| IMAGINE's "Missing pets" worries about request-shaped posts that become rants or scams | Verified | `IMAGINE.md` |
| A `page_posts` kind `sample` exists | Verified | `socialus-web` migration `20261010010000` |
| Locals will answer a wish with a real offer | **Assumed** | the pilot (T0) |

## 3. Prerequisites

| Missing | Owner | Needed by |
|---|---|---|
| A one-level reply on a wish (the Discussion message, in its smallest form) | Architect, then Don (it is the messaging question in its smallest form) | T1 |
| A composer for Idea / Ask | Architect | T1 |
| Don's ruling on expiry (none, per `nouns.md`, or 90 days, per `verbs.md`) | Don | T1 |
| Terms wording for what may be requested | socialus-legal | T1 |

## 4. Area → Feature → Journey → Criterion

**Area:** market-commerce (proposed); touches create-posts and discovery. **Feature:** Wish it existed (unnumbered).

| Journey | Who and what | Zero state |
|---|---|---|
| **W1 Someone makes a wish** | Writes what they want, tags it, posts | "No wishes yet. Be the first to say what you'd love to see made." |
| **W2 A neighbour answers** | Finds a wish in their kind of work, replies with what they would build and for how much | "No replies yet." |
| **W3 The two people meet** | Arrange the rest outside the app; the wisher closes it | "Closed." |
| **W4 The team-up** | Two neighbours each reply with a part; the wisher sees both | n/a |
| **W5 Starter examples** | A few examples show what a wish looks like | n/a |

Criteria are in the frontmatter, each tagged to its journey. All binary.

## 5. Roles (chair-merged)

| Role | Needs | Cost | Veto | One risk |
|---|---|---|---|---|
| Person (the wisher) | Say what they want in their own words; see who offers and at what price | Free to post; they pay only whoever builds | Strangers they cannot vet or compare | Many replies and no way to message, so offers must be public and clear |
| Maker (the builder, or a team) | See wishes in their line of work; reply with an offer and a price; keep what they earn | Time to read and answer | An auction, dynamic pricing, or a fee to reply | Thin or vague replies; a wish that is really a job posting |
| Money | A price in words; SocialUs earns on a sale only, once payments exist; nothing for posting or replying | none now | Charging to post or reply; deposits or escrow in this concept | A wish that is really repeat labour (Thumbtack's territory) |
| Architect | Idea or Ask plus a one-level reply; reuse tags and the report control | One reply surface | A conversion into another entry type (ruled out); a hidden second place for replies | Duplicate wishes: ten people want the same frog habitat; no dedupe is designed |
| Developer | A composer, a reply, a bounded Sample block | See sizes | A messaging system, a booking or a checkout | The reply is "just messaging" and grows |
| Tester | Binary criteria; the Sample rules; closed and empty states | Real wish, Sample and closed data | Samples that behave like real ones | A Sample taken for a real offer |
| Operator | Remove a hostile or off-topic wish fast, with the report path | Low | A person needed midweek; approving every wish first | The Missing-pets pattern: emotional wishes, scams, requests that should not be made |
| Guardian | A plain list of what may not be requested; no safety warranty on a built thing; replies are public | One paragraph in Terms | Any promise that SocialUs vouches for a builder or the result | A built thing fails or hurts someone |
| Scout | See precedents | none | none | Thumbtack charges the pro to quote; this takes nothing to reply |

**Flag for socialus-legal (no detail):** liability and safety of a built item, payments, and what may not be requested.

## 6. Who earns

The member who builds, from the price they state. SocialUs, transaction income on a sale once payments exist (DECISIONS 2026-10-07). Nothing is charged to post or to reply.

## 7. Starter requests and the sample rule

The sample rule makes a Sample non-interactive and keeps it out of search, so **a Sample cannot be used to test how people respond**; it can only show what a wish looks like. Don's frog habitat is also a **real** want. So:

| Seed | What | How it appears |
|---|---|---|
| 1 | A small backyard frog habitat: a tiny pond, running water, a few plants | **Real**, posted by Don as himself; real replies |
| 2 | A raised garden bed for a shady corner, weatherproof | Sample, bounded block, marked |
| 3 | A sturdy outdoor bench for a small budget | Sample, bounded block, marked |
| 4 | A small outdoor sculpture, abstract | Sample, bounded block, marked |
| 5 | A balcony compost bin | Sample, bounded block, marked |

New ideas Don thinks of are added to this table, dated.

**Open for Don:** how many real wishes to seed. Option A: Don's frog wish real, four Samples to show the shape (recommended). B: five real wishes from Don and people he knows (more honest response, more asking of friends). C: Samples only (shows the shape; learns nothing about response).

## 8. T0 / T1 / T2 / T3

| | **T0 Pilot** | **T1** | **T2 (recommended)** | **T3** |
|---|---|---|---|---|
| Ships | Nothing built. A Page for wishes posts each as an ordinary Post; replies happen outside the app, the Page's contact links say where | A wish composer (Idea or Ask), a one-level public reply, a close action, the report control | T1 plus the bounded Sample block, tags to find wishes by kind of work, and a small operator view of new wishes and replies | A replier's own Page linked on the reply; team-up display; wishes linked to listings |
| Hours (estimate) | 0 to 6 | about 30 (the committee said 12; there is no reply surface to reuse, so the chair's estimate is higher) | about 50 | about 80 |
| Existing data only? | Yes | Mostly: Idea and Ask substrate exists | Yes | No |
| Proves | Whether anyone posts a wish and anyone answers | Wishes get public offers from strangers | Starter examples teach the shape without confusing people | Builders can be found and trusted by their work |
| Leaves out | Replies in the app | Samples, tags, an operator view | Payments, messaging, dedupe | Escrow, ratings (Won't) |
| Trigger to move up | Five real wishes and two with an offer in four weeks | Two wishes with three or more offers each | Wishes keep arriving without Samples | Payments exist (Later) |

## 9. Gates

- [x] Prerequisites listed, each with an owner
- [x] Criteria binary
- [x] Zero states defined (section 4)
- [ ] Copy written to voice rules: not yet (post-beta)
- [x] Guardian: no promise broken; legal flagged without detail
- [x] **Kill criterion:** in the pilot (T0), no wish draws a real offer in four weeks, or a third of wishes are rants, scams or job postings: stop, and ask the first wishers and two builders why
- [x] **Metric:** wishes that reach a closed state with someone building (the wisher says so). Real-world meetings, not attention.
- [ ] Tickets: none until Don approves a size
- [ ] Assumed facts verified as ticket 1: whether locals answer a wish with a real offer

## 10. Precedents

Looked up this run:
- [Etsy custom orders](https://help.etsy.com/hc/en-in/articles/115015440167-How-to-Request-a-Personalised-or-Custom-Item): a buyer asks a seller for something made to order; they agree details in messages. Copy the made-to-order idea; skip the private messaging that does not exist here.
- [Thumbtack](https://d3.harvard.edu/platform-digit/submission/meet-thumbtack-your-local-handyperson-reimagined/index.html): a customer posts a request, professionals send quotes with a price, the customer picks. Closest model; skip the fee to quote.
- [Nextdoor For Sale and Free](https://about.nextdoor.com/press-releases/nextdoor-expands-its-buy-sell-and-give-feature-with-the-launch-of-free-finds): neighbours list things, with Neighbor Made and Neighbor Services categories. The "wanted / ISO" post is recalled, not looked up.
- [Kickstarter](https://updates.kickstarter.com/how-crowdfunding-works-a-guide-for-creators/): a goal, a deadline, and nothing charged unless the goal is met. A fit for "teaming up", but it needs money in the app, so it is T3 at the earliest.

## 11. For Don (only what he alone can answer)

**A. Run the pilot (T0): a Page for wishes, your frog habitat first, replies outside the app, with no code** (recommended; it tests the one thing nobody knows, whether neighbours answer). B. Wait and build T1 after beta, once the reply surface is decided with messaging. C. Fold it into the Idea design now. Also: expiry (none, or 90 days) and how many real wishes to seed (section 7).
