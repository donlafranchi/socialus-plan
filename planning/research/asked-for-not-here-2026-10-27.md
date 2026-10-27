# Asked for, not here yet, and teaching the ask

**When many people nearby ask for something SocialUs doesn't have, the app can say so to the community ("lots of people near you are looking for X"), so someone can start a Wonder or a Page for it.** No individual is ever exposed. Separately, people need to be shown what they can ask, and the well-worn way is a few example asks on an empty Ask bar that rotate and fade once they've asked.

An idea to explore, not a plan. The entry is in IMAGINE; this file holds the detail.

*The PM, 2026-10-27:* "show people … that they can search for anything even things that don't exist and that if many people ask for something that doesn't exist that this app should surface that for them and put that out to the community … and let others try to bring that thing into existence."

## Asked for, not here yet

**Most of the pieces exist or are planned:**
- F119 logs questions under the F089 rules: anonymous, a floor of ten members, one metro, raw rows deleted after 30 days, with an opt-out.
- Plan #228 analyses searches nightly.
- Wonders (F117) let a maker ask who's in.

**The missing link is the demand side:** unanswered asks, counted and shown to the community, with a path to start something.

<details><summary>Details</summary>

**The flow:**
1. **Ask.** A question with no good match is counted as unmet.
2. **Count.** Unmet asks are grouped by meaning (the nightly pass, #228). A group shows only once at least ten members in one metro have asked, using F089's floor.
3. **Show.** A shelf or line on the wide-open view, "Asked for near you, not here yet". The wording is yours.
4. **Answer.** Two ways:
   - "I could make this" starts a Wonder, pre-filled with the ask and the count.
   - "I know a place" suggests a Page.
5. **Close.** When a Page or Wonder answers it, the people who asked are told, if their notifications are on.

**Precedents:**
- **[Google Trends](https://trends.google.com/):** shows aggregated, anonymous search interest by place.
- **Kickstarter and Product Hunt:** a maker tests demand before building. Product Hunt once ran "Ship" upcoming pages.
- **Nextdoor and Reddit "does anyone know…" posts:** demand asked in public, answered by neighbours.
- **Amazon and Etsy:** use "no results" searches internally to decide what to stock. They don't show them to shoppers.
- **Uber and DoorDash "request your city" or "request a restaurant":** often cited, but I couldn't confirm it in this pass. Treat it as unverified.

**Open questions:**
- **A ruling it touches, 2026-10-11:** "Wish it existed launches as an Idea only … SocialUs is not involved." In this idea the app itself raises the demand, so that ruling would need a newer one if this goes ahead.
- Does an ask count as unmet when there are no results, or when the asker leaves without tapping anything?
- Could it be gamed, for example a business seeding demand for itself?
- Does a member see that their own ask was counted? It's private, so only the member would.
- What's the floor in a small town, where ten members may be most of the people asking?

</details>

## Teaching the ask (onboarding)

**Chat-first apps show example asks on the empty box.** ChatGPT rotates starters, and Claude groups its suggestions by kind of task. Guides warn against a bare "Ask me anything", against the same starters for everyone, and against starters that promise things the app can't do. For SocialUs, show three local, real examples that each open a different view, rotate them, and stop once the person has asked a few times.

<details><summary>Details</summary>

**Proposed:**
- **On the empty Ask bar:** three example asks, each one a different view and each built from real data in the member's metro:
  - "What's happening this weekend?"
  - "Who has happy hour today?"
  - "Who's hiring near me?"
- **Rotate** them each visit, from what has results today. An example that would return nothing is never shown.
- **First run:** the first example is tapped automatically, as a short demo, so the person sees a view open from a question.
- **Fade:** after about three asks the examples go, and the box keeps a one-line hint.
- **Later:** one example comes from "Asked for, not here yet", to show that you can ask for things that aren't here yet.

**Sources:**
- [Prompt starters pattern (AI UX Playground)](https://aiuxplayground.com/pattern/prompt-starters)
- [AI onboarding patterns](https://www.aiuxplayground.com/guides/ai-onboarding)
- [Claude onboarding teardown (Supademo)](https://supademo.com/user-flow-examples/claude)

These are third-party write-ups; check the live apps before copying detail.

</details>
