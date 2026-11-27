---
id: brief-2026-11-21-shop-by-your-values
status: awaiting-approval
size: L
path: new territory
concept: CO-0068
fits: after the waitlist and the chat-first first slice (the town brief); goes to counsel before anything is built
criteria:
  - A member who never takes the survey gets exactly the same screens, search results and order as before; a test compares both responses for the same fixtures, field by field, seen failing first.
  - A blue dot shows on a Page only to a viewer who took the survey, when the Page's owner took it too and their answers align past the PM's threshold; every other viewer, signed in or out, gets no dot and no field that hints at one, enforced in SQL.
  - No screen, response or staff tool shows one person's answers to anyone else, or a per-question match; the only output of matching is dot or no dot for one viewer and one Page.
  - A member's answers can change at most once in 30 days and are deleted in one step; deleting removes every dot they saw or gave.
  - The neutral question uses no politically coded word, works on its own (its answers lean only the member's own front door and Discover, never Find), and offers the survey once, only to a member who picked a values answer; a test with a price-and-close-by answer proves no offer appears, seen failing first.
  - Nothing about the survey itself appears on the main path: not in onboarding, not in a notification, not as a banner; the only ways in are that one offer, the line in You, the help, and asking the chat.
  - A Page never learns which members see its dot; any count is per market, of ten or more different people, never per Page.
---

# Shop by your values: an invitation, never an interruption

**As of 2026-11-21** · Source: hand-written · Maintained by: hand (set by tend-docs from the last commit date; the owner confirms on next edit)

**As of 2026-11-21** · Source: the PM's words below; the values-survey brief of 2026-11-18 (folded in here and deleted); plan PR #348 (the 2026-11-13 blue dot sketch, replaced); `product/systems/signals.md`; Badges vs values (CO-0029), Locally Made badge (CO-0008), Reciprocity & goodwill (CO-0013), Discovery that knows what a person is optimizing for (CO-0025), The town before it opens (CO-0065), F136, JY-BRING, PRINCIPLES · Maintained by: hand (brief; deleted at 30 days or once ruled and placed)

*The PM, 2026-11-21:* "So I want to have a theme for this topic about values and how this app is supposed to be different than other apps and allows our members to search and discover and support based on their values and that we need to be able to figure out how to allow certain people to stop [shop] by their values and support page owners, who also believe that supporting people with good values is important. What I'm looking for is a way to approach members about this without diverting what it's for or how it's used and so that those who think it's important can opt in and those who don't think it's important don't ever have to think about it."

*Then, on the blue dot:* "The blue dot Easter egg is this values concept where if I take the survey about values that they matter to me and others also take the survey about values and it matters to them that if both people have taken that survey then they see a blue dot Santa [on a] page so for example if I take a survey and I care and I like the blue dot concept then I can see every page that has a blue dot because I took that survey and same as the page owner. They took a survey a blue dot will be displayed on their page, but only for those who took the survey and matched essentially and it doesn't have to be 100% match, but it should be some type of alignment and that way it can be a small little thing that certain users see that nobody else does because they both care. There still isn't fully defined, but I do like the part where this little blue dot is only visible if both parties are in alignment on the survey."

*Then, on how to ask:* "I wonder if an intro question like what's important to you when you shop or when you're looking for a producer, for example, could be innocuous enough to not be leading and not raise any suspicions or have anyone read into this very much"

*And, earlier, 2026-11-13:* "theres something we're missing here and it goes along with the easter egg blue dot concept. we want to be able to allow people to tell others about who they are. and we want consumers to sort based on who they want to support. I need a research session to figure out some options for us to build this in the app. perhaps its a survey about what kinds of people you want to do business with. this is a political survey as that is very important to people right now so it needs to be handled with care and will likely be a behind the scenes feature. We may want a badge for people to say "we took the survey" or something along those lines as a wink gesture for others to know it's available."

**Bottom line: one private survey that members and Page owners can each choose to take. Where two people who took it align, the Page shows that member a small blue dot; nobody else sees anything, and the app of someone who never takes it doesn't change at all. The way in is one neutral question everyone can answer, useful on its own; only people who pick a values answer are quietly offered the survey. Start with the question, the survey and the dot (A).**

**Your call:** which first slice: A, B or C?

*In the store:* this brief names its concept, so each version reaches the store as a dated change on it. Your pick goes in as a dated ruling under a new `## Rulings` in `product/systems/signals.md`, so the import carries it too.

**Names to pick from (working name first):** *Shop by your values* · *Who you support* · *Kindred*.

## The picture

After her first few searches, the chat asks Ana once: "What matters to you when you choose where to shop or who to buy from?" She taps close by, locally owned and how they treat their people. Her front door leans that way from then on. Because she picked a values answer, one quiet line follows: "Want to find owners who care about the same things? A short, private survey." She takes it in five minutes and skips the political part. Over the next weeks a small blue dot appears on three Pages she visits: their owners took the same survey and they line up. Ben answers the same question with price and close by. His front door leans that way, he is never offered the survey, and he never sees a dot, a prompt or a hint.

## How members come across it (invitation, not interruption)

**The door is one neutral question,** your idea of 2026-11-21: "What matters to you when you choose where to shop or who to buy from?" Pick any: price · quality · close by · open when I need it · locally owned · made nearby · how they treat their people · care for the environment · giving back to the community · shares my values.

- **Useful on its own:** every answer leans that member's front door and Discover (the town brief's widgets, F136's engine); Find is never reordered (2026-10-12). Like Pinterest's and Etsy's interest pickers, it reads as personalization, because it is.
- **No coded words:** nothing about politics, faith or causes; nothing anyone would read into.
- **The quiet offer:** only a member who picks one of the last four answers sees one line offering the survey, once. "Not now" ends it; the line in You stays.
- **Other ways in:** a line in You; "Want a blue dot?" in Page help for owners and a plain answer to "what's the blue dot?" (`signals.md`'s help engine); asking the chat "who shares my values".
- **Never:** the survey as an onboarding step, a notification, a banner, a reminder, or a nag after a "not now".
- **The answers are the member's:** kept like search history, seen only by them, changed or deleted any time.

## What's asked

- **Chosen, never inferred:** only what a person answers; nothing from what they search, follow or buy.
- **Two layers:** broad values first (how a business treats people, community and giving back, the environment, local ownership and where the money goes); a separate, optional political layer, worded so a member of any party reads it as fair. You write the questions.
- **Same survey both sides:** a Page owner answers for their Page; a member for themselves.
- **Change or delete any time:** changes at most once in 30 days (against guessing, below); delete is one step and removes every dot.

## Matching and the blue dot

**Settled by you (2026-11-21):** a viewer sees the dot on a Page only when both took the survey and align enough, not a 100% match. Everyone else, including anyone who didn't take it, sees nothing.

- **One output:** matching returns dot or no dot for one viewer and one Page. Never a score, a percentage or which answers matched.
- **Never ranks anyone down:** a Page without a dot, or an owner who never took it, keeps its place for everyone.
- **One-way:** members choose businesses; a business never sees, sorts or refuses members by their answers.

**Still open (your options):**

| Question | Options | Recommend |
|---|---|---|
| What "aligned enough" means | T1: most of the questions both answered agree (say 6 in 10). T2: their top three priorities overlap by two. T3: a weighted score. | T1: simple, explainable, tunable |
| Which questions count | Broad only; or broad plus political when both answered it | Broad plus political when both answered |
| Dot only, or a hint why | Dot only; or "you both care about local ownership" on tap | Dot only (a hint reveals answers) |
| Member to member too | Page only; or members' profiles as well | Page only for now |
| Takers filter to blue-dot Pages | No; or yes, in the chat and Browse widgets | Yes, in the second step (B) |
| Where the neutral question appears | Q1: a step after sign-up (Pinterest, Etsy). Q2: only in You. Q3: the chat asks once after a few searches, one tap to skip, editable in You | Q3: sign-up stays short and it arrives when it is useful |
| What non-takers see | Nothing (your words) | Nothing |
| The "we took the survey" wink (2026-11-13) | None; or visible only to takers; or a public mark | None in A: a public mark tells everyone who took it, which is what made public lists targets |

## Options: the first slice

- **A. The question, the survey and the dot (recommended).** The neutral question for everyone; the survey offered to those who pick a values answer; aligned pairs see the dot; nothing else. Your settled core, the least to build and to protect.
- **B. A, plus "show me blue-dot Pages".** Takers can ask the chat or filter Browse to Pages they align with. What "shop by your values" means in practice; one more surface to keep private.
- **C. B, plus member to member and a wink.** Dots on members' profiles, and a "we took the survey" mark. The richest; the most to leak, and the wink reveals who took it.

## Risks, plainly

- **Guessing an owner's answers.** Someone retakes the survey many ways and watches the dot. Mitigations: one survey per member, changes at most once in 30 days, a coarse threshold, no per-question reveal, and a minimum number of questions both answered before any dot.
- **Sensitive data.** Political and religious views are special-category data under the GDPR and sensitive personal information under California's CPRA and several other state laws; picking "shares my values" says a little too, so it is kept like search history; the dot itself says something about both people. Kept owner-only, excluded from staff screens, deletable in one step.
- **Discrimination law.** If a business could sort or refuse customers by their answers, California's Unruh Act and places that protect political affiliation (the District of Columbia, for one) come into play. The design is one-way so it can't; counsel confirms.
- **Brigading.** Public values lists became boycott and harassment lists (PublicSq, Buycott, Yelp's 2020 attributes). No public list, no counts per Page, and a dot no outsider can see.
- **App stores.** Apple and Google treat political and religious data as sensitive: explicit consent at collection, a stated purpose, easy deletion.
- **Counsel:** the questions are in socialus-legal (`terms-privacy/values-survey-counsel-2026-11-21.md`); nothing is built before counsel answers.

## Checked against the principles

- **You choose; works for you:** opt-in on both sides, a quiet invitation, one-step off.
- **No stalking:** no one can follow a member's values or which dots they see; a Page never learns who sees its dot.
- **Data serves the members it comes from; never extractive:** answers are never sold, never used for ads, never ranked for anyone else's benefit.
- **Two halves:** discovery with a lens for those who want it, and owners and members who share values finding each other.

## Precedents

| Precedent | What it does | What we take or leave |
|---|---|---|
| [OkCupid](https://en.wikipedia.org/wiki/OkCupid) | Private answers to questions, shown back only as a match percentage | Take private answers and matching; leave the percentage |
| Bumble and Hinge ([Axios](https://www.axios.com/2020/02/14/dating-political-trump-apps-okcupid)) | An optional politics field, hideable, usable as a private filter | Take the private filter; leave the visible label |
| Mutual friends ([Facebook](https://www.facebook.com/help/1124310004297166)) | A signal shown only between two people, about what they share | Take: shown only to the two |
| [Goods Unite Us](https://www.goodsuniteus.com/where-do-we-get-our-data) | Party lean of big brands from public donations | Leave: public, a proxy |
| [PublicSq](https://www.catholicnewsagency.com/news/255114/public-square-marketplace-based-on-biblical-values-set-to-become-profitable-in-2024) | A public directory of businesses affirming one side's values | Leave: the list [became a boycott target](https://www.rawstory.com/maga-2671858890) |
| [Buycott](https://www.ecowatch.com/new-buycott-app-makes-voting-with-your-dollar-easier-than-ever-1881736507.html) | Public campaigns, scan to check a product | Leave: campaigns turned into mass boycotts |
| [2ndVote](https://www.influencewatch.org/non-profit/2nd-vote/) | Its own scores of companies on issues | Leave: one-sided by design |
| [Google Business Profile](https://support.google.com/business/answer/9049526?hl=en) and [Yelp](https://www.restaurantdive.com/news/yelp-adds-alerts-for-businesses-accused-of-racism/586725/) | Owner-chosen identity attributes, public, searchable | Take opt-in and opt-out any time; leave public marks |
| [B Corp](https://www.bcorporation.net/en-us/certification/) and [1% for the Planet](https://onepercentfortheplanet.org/) | Values proven by audit or giving, shown publicly | A later, public layer ties to where the money goes (plan PR #364), kept separate |
| [Etsy](https://www.etsy.com/) | Filters by what a shop is (handmade, local), and a style picker when you join | Take: values as a filter only for those who ask; a picker that reads as personalization |
| [Pinterest](https://help.pinterest.com/en/article/edit-your-home-feed) | Pick topics when you join; they tune your home feed, editable later | Take: the neutral question tunes the front door and stays editable |

<details><summary>How it maps to what exists</summary>

- **The neutral question** carries out a live ruling (D-0142, 2026-10-01): members can rank how they choose what to buy, and add values only if values matter to them.
- **Hidden signals** (`signals.md`): the dot is the first one; only holders see it.
- **The town brief's widgets:** the values widget and the "who shares my values" answer.
- **Hyper-specific search (F136):** the filter in B is one more lens on the same engine.
- **Where the money goes (plan PR #364):** a separate, later thread about proven giving.
- **Replaced:** the 2026-11-13 sketch (a survey SocialUs reviews earns the dot, plan PR #348) and the 2026-11-18 values-survey brief, both folded in here.

</details>

**Verified vs assumed:** the PM's words, the store's concept and journey, and the counsel file were read 2026-11-21. Precedent facts rest on their linked pages and press coverage; Etsy's join-time picker and Pinterest's current topic picker were not checked first-hand.
