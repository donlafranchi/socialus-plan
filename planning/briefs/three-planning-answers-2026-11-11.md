---
id: brief-2026-11-11-three-planning-answers
status: awaiting-approval
size: M
path: new territory
criteria:
  - Each of the three answers (what we built, where we are, what's next) fits in 10 lines or fewer on a phone, in plain words, with no ticket numbers.
  - Each answer is one call to the lookup tool and the same text on one generated page; no answer is a maintained document.
  - Every line names its source (store, GitHub, or both); a line no source can back is not shown.
  - What's next lists at most five things, in order, each with who does it, and a broken site always comes first.
  - The dashboard page, DASHBOARD.md, handoff/state.md, handoff/capabilities.md and the launch reports are retired once the three answers are live.
---

# Three planning answers: what we built, where we are, what's next

**As of 2026-11-11** · Source: STATUS.md (generated 16:16 UTC), DASHBOARD.md and the dashboard page (2026-11-10), handoff/, the knowledge lookup tool, HumanLayer's public GitHub repos · Maintained by: hand (brief; deleted at 30 days or once ruled and placed)

*The PM, 2026-11-11:* "I need to know what the next few things we need to do are." And: the goal is "to allow me to ask many different kinds of questions with an agent not having to have a search party through documents."

**Bottom line: make the three answers three tools on the lookup the agents already use, and one generated phone page showing the same three; retire the dashboard, the handoff files and the top of STATUS.**

## What HumanLayer hit, and what they built

- **Context fills and quality drops** ("the agent starts apologizing"): they compact the work into a short written artifact and start fresh. Rule of thumb: keep the context 40 to 60% full; wrong information is worse than missing, missing worse than noise.
- **Search floods the context:** read-only sub-agents find and summarise, so the main agent only sees conclusions.
- **State lost between sessions:** a handoff file and a resume command; progress is ticked back into the plan file itself.
- **Humans cannot review 2,000-line changes:** they review the plan instead ("I can read 200 lines of a well-written implementation plan"). A plan may hold no open questions.
- **Bad research makes bad code:** one wrong line of research becomes thousands of wrong lines of code, so the human steers research and plans, not code.
- **Their 12-factor rule 5:** derive "where are we" from the event record (one source of truth), never from a second copy.
- **What it means here:** answers are generated from records, short enough to read, and written for a human to steer. The handoff and state files are the part to drop: the store and GitHub already hold that state, and the PM does not want history.

## Why the dashboard is too long

- The page is 234 KB with 8 sections and about 40 feature cards; DASHBOARD.md is 30 lines; STATUS.md is 304 lines.
- It mixes agent health (undated docs, guard coverage, agent safety, criteria roll-ups) with the PM's three questions.
- It carries history ("built since last look", "100 criteria newly met, 29 lost") the PM does not need; git holds it.
- "Waiting on you: 21" and "Your to-do (1)" are two counts of the same thing.

## Answer 1: What did we build, and the point of each

Shape: one line per area, the plain name, then the point. Only what is live. Source: the store (concepts marked built, and the shipped capabilities F129 is loading); the point is the concept's own "why" field.

Worked example, today:
- **Sign in with an email code; your zip picks your town.** One way in, and you land where you live.
- **Waiting list for towns not open yet.** Prove a town wants it before we open there.
- **Pages for anything you do, one question, no forms.** Anyone can start something, not only shops.
- **Posts with a time and a picture.** What is happening near you today and this week.
- **Explore, as a list or a map.** Finding things is local first.
- **Follow a Page or a person.** Keep up without a feed choosing for you.
- **Wonders: "I'm in" and offers to help.** Neighbours make things happen together.
- **Reports: a second report hides it, AI reads first, a person decides.** Safe without a staff.
- **The knowledge store, for agents.** Agents ask one tool instead of reading documents.

## Answer 2: Where are we

Shape: live, broken, in flight, waiting on you. Five to seven lines. Source: GitHub for broken and in flight (deploys, check runs, open bugs, open PRs, the nightly smoke and speed runs); the store for what is building and what waits on the PM.

Worked example, today:
- **Live:** beta, one area, runs until April 2027.
- **Broken:** the latest build of main fails on Vercel, and the overnight smoke found a problem.
- **Slow:** 4 member screens are red; Explore takes 1.6 seconds to settle.
- **In flight:** four Page features (start something without a shop, a Page worth showing, several Pages, every Page has a face) and the store work (versions, how we work, what SocialUs can do).
- **Before beta closes:** 11 launch blockers, mostly reports and the one step before publishing.
- **Waiting on you:** set up Twilio for the phone check (first of 21).

## Answer 3: What's next

Shape: at most five things, in order, each with who. Broken comes first, then what unblocks others, then the top of Now. Source: the store for order (F127's horizon and rank, F126's conditions for what is blocked) and GitHub for anything broken or waiting on the PM, which jumps the queue.

Worked example, today:
1. Fix the Vercel build on main. *Code.*
2. Fix what the overnight smoke found. *Code.*
3. Set up Twilio; it unblocks posting without a Page. *You.*
4. Run the three-account report test, then close the report blockers. *You, then Code.*
5. Finish the four Page features in build. *Code.*

## What replaces the dashboard

- **One phone page, three sections, the three answers above, about 25 lines in all.** Generated on push and nightly, from the same three tools, so the page and a chat answer never disagree.
- **Agent health leaves the PM's view.** Guard coverage, undated docs, ontology counts and agent safety become checks that open an Issue when they fail, read by agents, never by the PM.
- **The to-do list folds into Answer 3:** the PM's items are the lines marked *You*.

| Today | Retired by |
|---|---|
| dashboard/status-dashboard.html, DASHBOARD.md, scripts/dashboard.py | the phone page (all three answers) |
| handoff/capabilities.md, the eight launch reports | Answer 1 |
| handoff/state.md, STATUS.md down to "In the code repo", the dashboard's numbers | Answer 2 |
| the dashboard's Upcoming and Needs your attention, don-todos.json | Answer 3 |
| the rest of STATUS.md (guard coverage, ontology, docs by age) | checks that open Issues |
| README.md | stays as a 5-line pointer to the page; GitHub shows it |

## What an agent's orientation shrinks to

- **CLAUDE.md, about 40 lines:** which repo holds what, the absolutes by slug, how decisions flow, and the lookup tool's verbs.
- **First calls, not first reads:** `where`, then `next`, then `live(concern)` for the area it will touch. No STATUS.md, no dashboard, no handoff.
- **HumanLayer's discipline, kept:** research and plan are short artifacts a human can steer; anything the next session needs goes in the store or the PR, not in a handoff file.

## Options

- **A. Three tools and one generated page (recommended):** add `built`, `where` and `next` to the lookup tool; a nightly job writes GitHub's live state (deploys, checks, open bugs, smoke, speed) into the store so `where` is one call; the page renders the three. Retire the files in the table. Builds on F127 and F129, which are already in flight.
- **B. Trim the dashboard to three sections:** fastest; keeps the 833-line script and the habit of documents as the record, and chat answers still need a search party.
- **C. No page, ask in chat:** an agent composes each answer live from the store and GitHub. Least to build; answers vary between agents, and there is nothing to glance at on a phone.

**How A would be measured:** each answer 10 lines or fewer; "what's next" answered in one call; an agent oriented in 3 calls instead of reading about 330 lines (CLAUDE.md, STATUS.md, DASHBOARD.md); generated status files go from about 1,000 lines to one page.

## What I did not read

- socialus-web Issues, PRs, check runs and deployments directly: this session reaches that repo by git only, so live state comes from STATUS.md (16:16 UTC today) and the dashboard (2026-11-10), which disagree on the build (the dashboard says green; STATUS lists the Vercel failure).
- The dashboard page's cards: its content is drawn by script; I read the section titles and the script.
- basecamp.com (Shape Up hill charts), linear.app (project updates) and humanlayer.dev (their blog) are blocked by this environment's network. I named them as precedents and did not use their content. HumanLayer is read from GitHub: the humanlayer repo (its commands and agents as of the commit before their removal on 2026-10-22), 12-factor-agents (factors 3, 5, 12) and advanced-context-engineering-for-coding-agents.
- The F127, F128 and F129 work in flight in other sessions.
