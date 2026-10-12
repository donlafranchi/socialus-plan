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
  - W1.1 [launch] A member can post a wish: a title, a description, an optional picture, an optional budget in their own words, and tags
  - W1.2 [if popular] Anyone signed in can reply to a wish with a public offer: what they would build, a price or fee in words, and a way to be reached that the replier chooses
  - W1.3 [if popular] The member who posted sees every reply on their wish, in order, with the replier's name
  - W1.4 [if popular] A reply shows no button to pay, hire or message; the two people arrange the rest outside the app
  - W1.5 [launch] Starter examples sit in their own bounded block with a heading and a "Sample" mark, are not returned by search, and have no reply, follow or link control
  - W1.6 [launch] A real wish and a Sample are not shown in the same list
  - W1.7 [launch] A wish can be closed by the member who posted it; a closed wish says so and takes no new replies
  - W1.8 [launch] A wish can be reported with the existing report control
  - W1.9 [if popular] Tags let a replier find wishes in their kind of work
  - W1.10 [launch] Empty states: no wishes yet, no replies yet, and a closed wish each say so in plain words
  - W1.11 [if popular] Until payments exist, money moves only between the people; SocialUs holds none and the screen does not suggest otherwise
  - W1.12 [launch] A wish quiet for 90 days sorts after the rest and stays readable; nothing is hidden or deleted for being old
  - W1.13 [launch] Any reply, edit or "still wanted" tap from the requester, or a member showing interest, brings a wish back up; a view does not
  - W1.14 [launch] A member can show interest in a wish, and the count is said in words, with "Nobody's shown interest yet" at zero
  - W1.15 [launch] The requester can link the finished thing to the wish once it exists
  - W2.1 [if popular] A wish can carry a terms card made from SocialUs's one standard template, and the card is shown before anyone backs
  - W2.2 [if popular] The terms card has these fields: what is funded, who is party, the amount, what the backer gets back, milestones, delivery, what happens if it falls through, who owns the result, and SocialUs's part
  - W2.3 [if popular] A backer picks one of three variants in plain words: gift, reward, or pre-purchase
  - W2.4 [if popular] Each party accepts the card before any pledge counts, and each can see the accepted card later
  - W2.5 [if popular] No screen, field or word offers a backer money back, a share, a return, a payout or a profit; the highest backing level is not offered until socialus-legal has cleared it
  - W2.6 [if popular] Until payments exist, a pledge is words between people and the screen says money moves outside the app
  - W2.7 [if popular] Once payments exist, pledged funds are held by the chartered partner, not by SocialUs, and released or returned as the card says
  - W2.8 [if popular] The card states SocialUs's part (its transaction income on the sale) before anyone backs
  - W2.9 [if popular] A wish with no backers, or whose goal was not met, says so in plain words and tells each person what happens next
---

# Feature Brief: Wish it existed

**Goal:** A member can ask the neighbourhood for something they want that may not exist locally, and neighbours can answer "I can build that" with a price, team up, or back the idea together, when they have a want like a small frog habitat.
**Date / run by / PM context:** 2026-10-11 · plan-feature, one pass on a light model, chair merge · Don, voice-dictated: "I want a cute little frog habitat for my backyard ... a tiny thing that has a pond, running water, a little bit of plants ... it may exist somewhere but probably not locally ... can we post things like that as starter examples and see how the community responds, maybe someone says hey I can build that and offers to do so for some kind of a price or fee, or they work together to create something, and then we can see ideas like that as we think of them." A possibility, not a commitment.
**Scope line:** After beta. Not in the Beta milestone.

**Phase rule (Don, 2026-10-11):** "For launch we are only offering it as an idea and early people will need to figure it out on their own. If it becomes popular then we will expand it. We aren't involved in the early phase."

- **Launch phase (SocialUs not involved):** a wish is an **Idea** (`wonder`): a member posts it, other members show interest, the requester links the finished thing when it exists. No offers channel, no terms card, no backing, no money, no mediation. People find each other and work out the rest on their own, outside the app.
- **If it becomes popular:** expand in this order, each only when the one before is used: public offers ("I can build that, for this"); then the standard terms card with backers (words only); then, only once payments exist and socialus-legal has cleared it, pledges that carry money. The highest backing level stays held for counsel throughout.
- **Criteria are tagged `[launch]` or `[if popular]`.** Only the `[launch]` ones belong to the first phase. The sections on offers, the terms card and backing below are the plan for expansion, not for launch.
- **No expiry; old wishes go stale.** This is already ruled (ruling 2026-09-15: a wonder has no expiry; everything carries a last-interaction date, and anything quiet for 90 days sorts last rather than being hidden; a view does not count as interaction). `verbs.md` still said "expires 90 days"; it is corrected in the same change. Open from that ruling: whether 90 days is one number everywhere.

*Don, 2026-10-11.* A third concept, separate from the two market concepts. It connects to them (see [Market listings](2026-10-11-market-listings.md) for the map) but needs nothing from them.

## Why it fits (members first)

- **Flip 1, toward in-person.** The thing gets made by a neighbour and handed over in person; the want starts a conversation between two people who live near each other.
- **Flip 2, spreading wealth among the many.** The money goes to the member who builds, not to a catalogue company that does not make it. SocialUs earns only on a sale (ruling 2026-10-07).
- **Who it serves first:** the person with a specific want the shops do not stock; the neighbour who can make things and has no way to be found for it.

## 1. What this is, and what it is not, in the plan today

| In the plan | State | What this concept adds |
|---|---|---|
| **Idea** (schema `wonder`): someone puts a new thing to the neighbourhood and others signal interest before it exists | Substrate only; signalling, threshold and conversion undesigned; ruled 2026-09-15: no conversion into another entry type, the author makes the new Page themselves | It is the same thing, with one new move: a reply that is an **offer to build** |
| **Offer / Ask** (schema `offer`, `ask`): entry types exist | No composer; blocked on the missing reply channel | An "I can build that" is an Offer. **A wish is an Ask or an Idea** |
| **Discussion message**: a reply on a Page's board, one level deep | Not built | The reply channel this needs, in its smallest form: one level of public replies on a wish |
| **F089 search demand** (draft) and **F064** (a tap on something not built) | Search demand is aggregated: a floor of ten members, one metro, raw rows deleted after 30 days; "resolved by somebody starting it" | A wish is the **member-written** form of that demand |
| **Sample rule** (ruling 2026-09-17): examples live in their own marked block, not in search, not interactive | Ruled | Limits how starter wishes can appear (section 7) |

So the honest answer to "is this new?" is: **mostly no.** It is the undesigned half of Idea, plus one reply that carries a price. The brief is that design.

## 2. Facts (Stage 0)

| Fact | Verified / assumed | Source |
|---|---|---|
| Idea has substrate only; the signalling mechanic is undesigned | Verified | `nouns.md`, `verbs.md` |
| An Idea has no expiry and sorts last after 90 quiet days (ruling 2026-09-15); `verbs.md` wrongly said it expires at 90 days, now corrected | Verified | the 2026-09-15 ruling; `verbs.md` |
| No messaging, no reply channel; Volunteering (offer/ask) is blocked on it | Verified | `nouns.md`, the After beta milestone |
| No public member profile; a member who wants to be found makes a Page | Verified | After beta, speculative |
| The platform handles no money; payments are Later; no auctions or dynamic pricing | Verified | the After beta milestone; what-this-is § Won't |
| IMAGINE's "Missing pets" worries about request-shaped posts that become rants or scams | Verified | `IMAGINE.md` |
| A `page_posts` kind `sample` exists | Verified | `socialus-web` migration `20261010010000` |
| Locals will answer a wish with a real offer | **Assumed** | the pilot (T0) |

## 3. Prerequisites

| Missing | Owner | Needed by |
|---|---|---|
| A one-level reply on a wish (the Discussion message, in its smallest form) | Architect, then Don (it is the messaging question in its smallest form) | T1 |
| A composer for Idea / Ask | Architect | T1 |
| Don's ruling on expiry | none needed: no expiry, stale after 90 quiet days, already ruled | done |
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
| **W6 Others back it** | Members read the terms card, accept it, and pledge toward the wish | "No backers yet." |

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
| Backer (someone who funds an idea) | To know exactly what they get back and what happens if it falls through, before they chip in | Their amount, held until the terms say it is released | Vague terms; any sense they are buying a stake | A pledge to something that does not ship, with no clear way back |
| Scout | See precedents | none | none | Thumbtack charges the pro to quote; this takes nothing to reply |

**Flag for socialus-legal (no detail):** liability and safety of a built item, payments, what may not be requested, and everything under backing (section 6a).

## 6. Who earns

The member who builds, from the price they state. SocialUs, transaction income on a sale once payments exist (ruling 2026-10-07). Nothing is charged to post or to reply.

## 6a. Backers and the standard terms

*Don, 2026-10-11:* "Maybe we also offer others to become backers and we provide the structure so that the parties don't have to figure this out for themselves." And: "A backer is someone who would fund an idea and there's a standard template of what the parties agree to."

**What backing is.** Another member funds the idea: they chip in toward a wish so it gets made. The requester, the maker (or team) and the backers all accept **one standard terms card**, so nobody invents terms.

**Why the platform does this (Don, 2026-10-11):** "We want to generate revenue for our members and not let outside lawyers take advantage of our members." SocialUs gets the template vetted **once, at the platform level**, so members do not need to hire a lawyer of their own to back, fund or build something together. **The revenue stays with members, and the template is a member benefit.** (Counsel decides how, or whether, this can ever be said to members. It stays out of any member-facing copy until then.)

### The terms card (one template, fixed fields)

| Field | What it says |
|---|---|
| What is funded | One sentence: the wish, e.g. "a small backyard frog habitat with a pond, running water and a few plants" |
| Who is party | Requester, maker or team, and each backer, by name |
| Amount | The maker's price or goal, and each backer's amount |
| What the backer gets back | Exactly one of: the thing itself, a defined reward (credit, discount, a share of the build), or thanks. Not money back |
| Milestones | Each step, what is delivered, and when pledged money is released (once payments exist) |
| Delivery | Where, when, and who hands it over, in person |
| If it falls through | Goal not met: every pledge returned. Maker cannot deliver: what is returned and who decides |
| Who owns the result | The requester, or the backers together, said in one line |
| SocialUs's part | Its transaction income on the sale, stated up front; it holds no money itself |
| Not covered | No warranty on the built thing; this is not an investment |

### Three variants of the card

| Variant | Backer gets | Closest precedent | Notes |
|---|---|---|---|
| **Gift** | Thanks; their name if they want it | GoFundMe | No reward; goal not met means returned |
| **Reward** | A defined reward: the thing, a credit, a discount | Kickstarter all-or-nothing | The reward is stated, not a share of anything |
| **Pre-purchase** | The thing itself, paid for in advance | Etsy custom order | Refund if not delivered, per the card |

### Backing is not investing, with one level held back

A backer funds an idea and receives a thing, a reward or thanks. **Gift, reward and pre-purchase are not investments.** No screen or word may suggest money back, a share, a return or a payout in any of them.

**The highest backing level (Don, 2026-10-11):** "a backer at the highest level is an investor. We want to be an economic engine for our members." This is Don's direction and it is recorded as that, nothing more:

- **Not designed and not offered.** The brief carries no terms, amounts or conditions for it. Whatever it is, it sits **above** the three variants and is **held for socialus-legal**: crowdfunding rules, securities rules, and money handling may all apply, and counsel decides what is possible and how it could be said. No detail here.
- **The aim is a member benefit.** SocialUs as an economic engine for its members: the template, the structure and the revenue stay with members (see the purpose above).
- **Kept apart from the settled ruling.** That members are SocialUs's own investors (and the only people paid out) is a ruling about SocialUs itself. Backing a member's wish is member to member. Counsel should read the two together, because the words overlap.
- **Until counsel clears it,** criterion W2.5 stands: the three variants only, and no investment-style wording anywhere.

### The commerce-income tie

Backing is member commerce. SocialUs's part is its transaction income on the sale (ruling 2026-10-07), stated on the card before anyone backs; nothing is charged to post a wish, reply or back. Holding pledged money until a goal is met is custody of funds, so it can only be done for the members' benefit through the chartered partner's closed-loop ledger (the After beta milestone); the Won't against funds held for the platform's own benefit still stands. **Until payments exist, a pledge is words between people** and the card says money moves outside the app.

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

## 8. Launch phase, then T1 / T2 / T3 if it becomes popular

The launch phase is Don's "only offering it as an idea": what the old T0 pilot described, using the Idea entry type, with SocialUs not involved. T1 to T3 are the expansion, in order.

| | **Launch phase (was T0)** | **T1 if popular** | **T2 (recommended)** | **T3** |
|---|---|---|---|---|
| Ships | Nothing built. A Page for wishes posts each as an ordinary Post; replies happen outside the app, the Page's contact links say where | A wish composer (Idea or Ask), a one-level public reply, a close action, the report control | T1 plus the bounded Sample block, tags to find wishes by kind of work, and a small operator view of new wishes and replies | A replier's own Page linked on the reply; team-up display; wishes linked to listings |
| Hours (estimate) | 0 to 6 | about 30 (the committee said 12; there is no reply surface to reuse, so the chair's estimate is higher) | about 50 | about 80 |
| Existing data only? | Yes | Mostly: Idea and Ask substrate exists | Yes | No |
| Proves | Whether anyone posts a wish and anyone answers | Wishes get public offers from strangers | Starter examples teach the shape without confusing people | Builders can be found and trusted by their work |
| Leaves out | Replies in the app | Samples, tags, an operator view | Payments, messaging, dedupe | Escrow, ratings (Won't) |
| Trigger to move up | Five real wishes and two with an offer in four weeks | Two wishes with three or more offers each | Wishes keep arriving without Samples | Payments exist (Later) |

**Backing in the sizes.** T1 and T2 do not move money: T2 adds the standard terms card, so members can agree the terms in words and arrange payment outside the app. T3 adds pledges that carry money, which needs payments (Later) and counsel's decision first.

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
- [Kickstarter](https://updates.kickstarter.com/how-crowdfunding-works-a-guide-for-creators/): a goal, a deadline, reward tiers, and nothing charged unless the goal is met. The model for the reward variant; it needs money in the app, so it is T3 at the earliest.
- [GoFundMe](https://www.gofundme.com/c/how-it-works): an organizer sets a title, a story and a goal; donors give; the organizer receives what is raised minus processing fees; no reward. The model for the gift variant. It takes no platform fee and asks for optional tips; SocialUs takes transaction income instead.
- [Patreon](https://smallbiztrends.com/2024/02/what-is-patreon.html) (a secondary source): recurring monthly pledges in tiers with perks. Copy the clear tier of what you get; skip the monthly subscription, which does not fit a one-time wish.
- Etsy custom orders (above): the model for the pre-purchase variant, where the buyer funds a made-to-order thing.

## 11. For Don (only what he alone can answer)

**A. Run the pilot (T0): a Page for wishes, your frog habitat first, replies outside the app, with no code** (recommended; it tests the one thing nobody knows, whether neighbours answer). B. Wait and build T1 after beta, once the reply surface is decided with messaging. C. Fold it into the Idea design now. Also: expiry (none, or 90 days) and how many real wishes to seed (section 7).

**Decided (Don, 2026-10-11):** option A on backing (words-only terms, no money until payments exist and counsel has cleared it); the highest backing level is held for socialus-legal; at launch it is offered only as an Idea and SocialUs is not involved; no expiry, old wishes go stale. **Still open:** how many real wishes to seed (section 7), and whether 90 quiet days is the right number for wishes.
