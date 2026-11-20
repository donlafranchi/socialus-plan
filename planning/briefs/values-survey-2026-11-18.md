---
id: brief-2026-11-18-values-survey
status: awaiting-approval
size: M
path: new territory
fits: grows from the blue dot (plan PR #348) and sits beside where a business's money goes (plan PR #364); after the waitlist and the 2026-11-06 build freeze
criteria:
  - A member's and a Page owner's survey answers are readable by that person alone; no other member, Page, visitor or staff screen shows one person's answers (a test proves it, seen failing first).
  - A member who turns on "favor who I want to support" sees Discover reordered for them only; Find is never reordered by it, and turning it off is one step.
  - No Page learns which members favored it; any count shown is per market, of ten or more different members, never per member.
  - The "we took the survey" mark says only that a survey was taken, never an answer, and its owner can hide it.
  - Every question reads as fair to a member of any party; the PM approves the wording before it ships.
---

# A values survey: telling people who you are, and choosing who you support

**As of 2026-11-18** · Source: hand-written · Maintained by: hand (set by tend-docs from the last commit date; the owner confirms on next edit)

**As of 2026-11-18** · Source: the PM's words of 2026-11-13; plan PRs #348 (the blue dot) and #364 (where a business's money goes); `product/systems/signals.md`, `member.md`, PRINCIPLES.md; the precedents linked below · Maintained by: hand (brief; deleted at 30 days or once ruled and placed)

*The PM, 2026-11-13:* "we want to be able to allow people to tell others about who they are. and we want consumers to sort based on who they want to support… perhaps its a survey about what kinds of people you want to do business with. this is a political survey… handled with care… likely a behind the scenes feature. We may want a badge… 'we took the survey'… as a wink gesture."

**Bottom line: make it one private survey both sides can take. Answers stay with the person who gave them. A member can let their answers quietly reorder Discover toward the people they want to support, and a Page can wear a "we took the survey" wink that never says what it answered. Every app that made values public turned into a boycott list; the ones that kept them private and personal did not.**

**Your call:** how far the first version goes.
- **A: Owners only, the blue dot path.** Page owners take the survey; we review it; the dot is the result. Smallest, ties straight to #348, but members can't sort by it yet.
- **B (recommended): Both sides, private matching.** Owners and members take the same survey; answers stay private; a member can turn on "favor who I want to support" for their own Discover; the wink mark is optional. Does what you asked; needs the most care and goes to legal first.
- **C: Public labels to filter by.** Owners pick public tags (veteran-owned, faith-based, and so on) and anyone filters by them, like Google and Yelp. Well-worn, but public political labels are how PublicSq's list got used for boycotts; it fights the hidden-signal design.

## The picture

Four parts, one engine that already exists on paper (hidden signals, `signals.md`):

1. **The survey.** Short, about what kinds of people you want to do business with. The same questions for a member and a Page owner, worded so a member of any party reads them as fair: SocialUs is for all Americans. You are writing the questions (#348); this brief does not draft them.
2. **Private answers.** Kept like saved searches and search history: owner-only at the row level. No one else reads one person's answers, staff screens included. Change or delete any time.
3. **Favor who I want to support.** A member's own switch. When on, Discover leans toward Pages whose answers match theirs. Find stays as it is: you asked for it and it comes back as asked. The match is coarse ("fits"), mixed with the other ranking, and never shown as a score.
4. **The wink.** "We took the survey" on a Page or profile, the owner's choice to show or hide. It says a survey was taken, never what was answered. In A it is the blue dot; in B the blue dot can stay the reviewed, stronger mark, and the wink is the light one.

**How it meets no stalking:** no one can follow one member's values or what they favored. A Page never learns which members leaned toward it. Counts, if shown at all, follow the search rule: ten or more different members per market, never per person.

**How it ties to the other two threads:**
- **The blue dot (#348):** the survey is its early path ("we ask them to take a survey and then we review it"). Option A is exactly that; B adds the member side.
- **Where the money goes (#364):** same shape, kept separate. That one is about where profits go, in levels; this one is about who a person is and who they want to support. Both keep anything judging a Page behind the scenes, so both share #364's risk: an owner should know what a hidden mark says about them and be able to contest it.

<details><summary>Precedents: what each collects, who sees it, how it sorts, what went wrong</summary>

| Precedent | Collects | Who sees it | Sorts by | What went wrong |
|---|---|---|---|---|
| [Goods Unite Us](https://www.goodsuniteus.com/where-do-we-get-our-data) | Nothing from owners: public federal donation records of companies' PACs and executives | Everyone | Party lean per brand, plus "alternatives" | Big brands only; a donation is a proxy, not what the owner believes |
| [PublicSq](https://www.catholicnewsagency.com/news/255114/public-square-marketplace-based-on-biblical-values-set-to-become-profitable-in-2024) | Owners affirm five stated values; a team vets public statements | Everyone (a public directory) | One side's values only | Critics used the public list to [boycott the listed businesses](https://www.rawstory.com/maga-2671858890) ([also](https://tagteam.harvard.edu/hub_feeds/2087/feed_items/13703336)); a [payment vendor cut it off](https://www.fintechfutures.com/press-releases/psq-payments-partners-with-atrius-development-group-to-provide-payment-services-after-sudden-cancellation-from-former-vendor) |
| [Buycott](https://www.ecowatch.com/new-buycott-app-makes-voting-with-your-dollar-easier-than-ever-1881736507.html) | Members join or create campaigns; nothing from owners | Campaigns are public | A scan says if a product conflicts with your campaigns | Campaigns become mass boycotts ([2014](https://english.alarabiya.net/media/digital/2014/08/23/Boycott-app-gets-popular-of-Israel-Gaza-war)); owners have no voice |
| [2ndVote](https://www.influencewatch.org/non-profit/2nd-vote/) | Its own 1 to 5 scores on seven issues, from public stances and giving | Everyone | Conservative lean | One-sided by design; [method questioned](https://mediabiasfactcheck.com/2ndvote/) |
| [Google Business Profile](https://support.google.com/business/answer/9049526?hl=en) | Owner opts in to identity attributes (Black-, women-, veteran-, LGBTQ+-owned and more) | Everyone | Search can match them | Owners got harassing reviews; Google [promises fast abuse action](https://support.google.com/merchants/answer/10342414) and lets owners opt out any time |
| [Yelp](https://www.restaurantdive.com/news/yelp-adds-alerts-for-businesses-accused-of-racism/586725/) | Owner attributes (Black-owned, 2020) | Everyone | Search and filters | Pile-on reviews from people who never visited; Yelp added alerts and froze reviews |
| Bumble, Hinge | Member's own politics field, optional, can be hidden ([Digital Trends](https://digitaltrends.com/social-media/swipe-left-dating-apps-politics-social-justice-activism)) | Profile viewers, if shown | Each member's private filter or dealbreaker ([Axios](https://www.axios.com/2020/02/14/dating-political-trump-apps-okcupid)) | Labels get gamed ("moderate" read as hiding); the private filter itself works |

**What we take:** from dating apps, the private, per-person filter; from Google, owner opt-in and opt-out any time, with abuse handled fast. **What we leave:** any public directory or score of who believes what (PublicSq, 2ndVote, Buycott), and anything one-sided.

</details>

<details><summary>Why B, and what it costs</summary>

- **It is what you asked:** people say who they are, and consumers sort by who they want to support. A covers the first half only.
- **Private and personal is the pattern that held up.** Every public version became a target list; the dating apps' private filter did not.
- **Fits the rulings:** you choose (the member turns it on); Find untouched (2026-10-12); a member's own data serves them (2026-10-25); no stalking (2026-11-15); hidden signals already say politics belongs behind the scenes.
- **Costs:** two surveys' worth of screens instead of one; a matching rule; and a stronger privacy promise to keep. Build it in two steps: the survey and the wink first (A's work, reused), the member switch second.
- **Watch:** a member could flip the switch on and off to guess a Page's answers. Coarse matching mixed into other ranking makes that a guess, not a readout; tell owners plainly that matching uses their answers.

</details>

<details><summary>Goes to socialus-legal before anything is built</summary>

Noted only; no analysis here.
- Political opinions as sensitive data under state privacy laws (consent, storage, deletion).
- Discrimination law, if favoring or a Page's answers ever lead to refusing service.
- A hidden mark about a Page that its owner can't see or contest (shared with #364).

</details>

<details><summary>What this does not decide</summary>

- The questions and their wording: yours (#348 already says you are writing them).
- How a reviewed survey earns the blue dot, and who reviews it: #348's open question.
- The names on screen ("favor who I want to support", "we took the survey"): yours, after the call.

</details>

## Verified vs assumed

- **Verified:** #348 and #364 read in full; `signals.md`, `member.md` and PRINCIPLES.md read on origin/main 2026-11-18.
- **Assumed:** precedent facts rest on search summaries and press coverage, mostly 2013 to 2024; Bumble's and Hinge's current menus and PublicSq's vendor dispute were not checked first-hand.
