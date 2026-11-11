**As of 2026-11-11** · Source: Patton (book via TOC and quotes, Patton Associates PDF, Agile Alliance timeline, InfoQ), Cockburn (his slides, secondary guides), Jeffries (Agile Alliance, ronjeffries.com via search), Torres (Product Talk), Cagan (SVPG), Basecamp Shape Up, Team Topologies (Fowler), Amazon (secondary), Nextdoor, Craigslist, Meetup, CMX, ActiveFence, TSPA · Maintained by: hand (research note; deleted at 30 days or once ruled and placed)

# Story mapping, and who to hire

**How this was read:** web search worked, but every page fetch was blocked in this session (jpattonassociates.com, nngroup.com, oreilly.com, ronjeffries.com, radar.zurb.com). So claims below rest on search-result excerpts of the pages linked, plus memory where marked **(memory)**. Section 4 lists what was not read.

## 1. Jeff Patton's user story mapping, the framework

**Where it comes from**
- Patton first set out the idea, unnamed, in "It's All in How You Slice It" (2005); "The new user story backlog is a map" (2008) named it; the book *User Story Mapping* (O'Reilly, 2014) is the full version. [Agile Alliance timeline](https://www.agilealliance.org/?p=5003329), [InfoQ 2009](https://www.infoq.com/news/2009/02/backlog-lacks-backbone)
- His complaint: a flat, ranked backlog loses the story; you can't see the whole journey, so you build pieces that don't add up. [InfoQ, "backlog lacks backbone"](https://www.infoq.com/news/2009/02/backlog-lacks-backbone)

**The structure, precisely**
- **Backbone, top row: user activities.** Big things a person does, left to right in the order they would tell the story ("first they..., then they..."). [barkingiguana summary](https://barkingiguana.com/writing/user-story-mapping-seeing-the-whole/), [Patton Associates PDF](https://jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf) (PDF found by search, not opened)
- **Backbone, second row: user tasks (book later calls them "steps").** Under each activity, the tasks that make it up, still left to right in narrative order. The user task is Patton's basic building block. [Patton slides, Northwestern](https://courses.cs.northwestern.edu/394/slides/spr12/Patton%20Building%20Better%20Products%20Using.pdf)
- **Body: details.** Under each task, top to bottom: sub-tasks, alternative ways to do it, exceptions, nice-to-haves. Higher on the page means more important. [rework.com explainer](https://resources.rework.com/libraries/project-management/user-story-mapping)
- **Reading it:** left to right is the story (time); top to bottom is priority. The backbone is not prioritised; you can't drop a step of the story, only make it thinner. **(memory, book ch. 1)**
- **Walking skeleton** (term borrowed from Alistair Cockburn): the thinnest slice that crosses every backbone step end to end. "Thin, ugly, but alive." [barkingiguana](https://barkingiguana.com/writing/the-workshop-user-story-mapping/), [Agile Alliance](https://www.agilealliance.org/?p=5003329)
- **Release slices:** horizontal lines drawn across the whole map. Everything above line 1 ships first; below is later. Each slice is named for the **outcome** it is meant to cause, not the features in it. [Patton Associates PDF](https://jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf), outcome-naming **(memory, book ch. 3)**
- **"Minimize output, maximize outcome":** "At the end of the day, your job is to minimize output, and maximize outcome and impact." [Goodreads quotes from the book](https://www.goodreads.com/work/quotes/41559956). Output = what you build; outcome = what changes for people; impact = what that does for the business. [Patton talk summary, designative](https://designative.info/2022/02/22/watch-jeff-pattons-output-versus-outcome-and-impact-talk)

**Card, conversation, confirmation (Ron Jeffries, 2001), which Patton builds on**
- **Card:** a short phrase, a reminder to talk, not a spec. **Conversation:** the real requirement, mostly spoken, best backed by examples. **Confirmation:** the acceptance tests that say it's done. [Agile Alliance glossary](https://agilealliance.org/glossary/three-cs), [Jeffries, Three C's Revisited](https://ronjeffries.com/articles/019-01ff/3cs-revisited/)
- Jeffries: if it doesn't fit on the card, split the story. [Three C's Revisited](https://ronjeffries.com/articles/019-01ff/3cs-revisited/)
- Patton's line: stories are for telling, not writing; the map is a tool for shared understanding. **(memory, book ch. 1 and 2)**

**How a map becomes a backlog**
- Start with **opportunities** (his preferred word over "epics", credited to Marty Cagan); for each one: dig deeper, trash it, or think about it. Killing a weak opportunity early is a win. [book TOC ch. 13](https://valsec.barnesandnoble.com/w/user-story-mapping/jeff-patton/1126354813), [reader notes](https://www.goodreads.com/notes/23317497-user-story-mapping/12470140-ma-ra?page=4)
- Then **discovery**: map today's behaviour, map the solution, break into options, slice what to release. A product backlog is worked out of an opportunity; it doesn't appear on its own. [Mind the Product podcast](https://mindtheproduct.com/getting-started-with-user-story-mapping-jeff-patton), [O'Reilly ch. 14 preview](https://www.oreilly.com/library/view/user-story-mapping/9781491904893/ch14.html)
- Then **delivery**: the cards in the top slice are the build backlog, each split small enough to build and confirm. [barkingiguana](https://barkingiguana.com/writing/the-workshop-user-story-mapping/)

**Cockburn's goal levels, as Patton uses them**
- Cockburn (*Writing Effective Use Cases*, 2001) uses altitude: **cloud** (very high summary), **kite** (summary goal, spans many sittings), **sea level** (user goal: one person, one sitting, "do they go home happy?"), **fish** (sub-function, a step with no meaning alone), **clam** (finest detail). [Cockburn slides PDF](https://alistaircockburn.com/Unifying%20us%20uc%20sm.pdf), [Visual Paradigm guide](https://guides.visual-paradigm.com/navigating-scope-the-impact-of-cloud-kite-sea-fish-clam-in-use-case-analysis/)
- Cockburn: the levels are a gradient, not boxes; use cases stop at fish; stories may go to clam. [Cockburn slides PDF](https://alistaircockburn.com/Unifying%20us%20uc%20sm.pdf)
- Patton: activities sit at kite, user tasks at sea level, details at fish and below; a task can be too high or too low, so altitude matters. [Patton slides](https://courses.cs.northwestern.edu/394/slides/spr12/Patton%20Building%20Better%20Products%20Using.pdf)

**Don's three levels mapped onto Cockburn and Patton (applied)**

| Don's level | Cockburn | Patton |
|---|---|---|
| 1. Whole-app capability ("people can gather") | cloud | the scope of a whole map, or an opportunity |
| *in between: a stage of the journey* | kite | **activity** (backbone row 1) |
| 2. A journey of steps | kite made of sea-level goals | the backbone read left to right |
| *in between: one step a member finishes in one sitting* | **sea level** | **user task** (backbone row 2) |
| 3. Implementation detail | fish, clam | body details; below clam is code work, which is not on the map |

- The level Don has no name for is **sea level, the user task**: "one member, one sitting, goes away happy". Cockburn calls it the most useful level; it is where acceptance checks belong. **(applied)**
- The other missing name is the **activity**, which groups steps inside a journey. **(applied)**

**Dual track: discovery and delivery**
- Discovery (are we building the right thing) and delivery (building it right) run at the same time, continuously; discovery does not finish before building starts. [Product School summary](https://productschool.com/blog/product-fundamentals/dual-track-agile), [UXDX session](https://uxdx.com/session/dual-track-development-involving-the-whole-team-in-discovery-and-delivery/)
- Patton: two kinds of work, not two teams; the same people do both. Article "Dual Track Development is not Duel Track" (not read; title from search). Idea traced to Desiree Sy (Autodesk, 2007). [Product School](https://productschool.com/blog/skills/dual-track-agile)

**Worked example (ILLUSTRATIVE, not a ruling or a scenario)**
Journey: "a neighbour finds something happening this weekend and goes."

| Activity (kite) | Find out | Choose | Commit | Go | After |
|---|---|---|---|---|---|
| **Tasks (sea level)** | open app, see this weekend nearby | open one, read what/when/where/who | say "I'm going" | get there | say how it went |
| Details, top | list of events near me, soonest first | time, place, organizer, who else is going | one tap "going" | address opens in maps | thumbs up |
| Details, lower | map view; filter by kind | photos; price if any | add to calendar; reminder | day-of reminder | photo; follow organizer |
| Details, lowest | saved searches | ask organizer a question | bring a friend | check in on arrival | rate; see their next event |

- **Slice 1, walking skeleton.** Outcome: "a neighbour finds one thing this weekend and turns up." Takes the top detail under every task: list, read, tap going, open in maps, thumbs up.
- **Slice 2.** Outcome: "they come back next weekend, and bring someone." Adds reminders, calendar, bring a friend, follow organizer.
- Each card in slice 1 gets a confirmation, e.g. "an event this Saturday within the metro shows up on the list". **(applied)**

## 2. How it maps onto the knowledge store (applied recommendation)

- **Whole-app capability** → `concept` (its timeline shows how it grows version to version).
- **Journey** → `feature` (the map itself: backbone plus body), linked to its concept.
- **Activity** → a grouping inside the feature; if it needs its own record, a `feature` child, not a new kind.
- **User task (sea level)** → `verb` (what a member does) acting on a `noun`, joined by a `link`.
- **Detail / alternative** → a card under a task in the feature; promoted to its own record only when it lands in a slice.
- **Release slice** → `slice`, named by its outcome; a `version` is the set of slices shipped together.
- **Acceptance check** → `criterion` on the slice (Jeffries' confirmation); a precondition like "signed in" → `condition`.
- **Why a slice line sits where it does** → `decision`; a later fix to it → `correction`.
- **How mapping is done here** → `practice`; "minimize output, maximize outcome" → `philosophy`; walking skeleton → `pattern`.

## 3. Roles if Don hires help

**Sourced practice**
- **Product trio:** product manager, designer, engineer jointly own discovery, with weekly customer contact; a default, may be a quartet. [Product Talk](https://www.producttalk.org/no-single-right-way-3/), [Product Compass](https://productcompass.pm/p/product-trio)
- **Cagan, empowered teams:** PM owns value and viability, designer usability, tech lead feasibility; teams get problems to solve, not feature lists; design is a team member, not a service. [SVPG, product vs feature teams](https://svpg.com/product-vs-feature-teams)
- **Shape Up:** a team is one designer plus one or two programmers, six-week cycles, then two weeks cool-down. [Shape Up ch. 8](https://basecamp.com/shapeup/2.2-chapter-08), [Basecamp, team setup](https://signalvnoise.com/svn3/how-we-set-up-our-work)
- **Team Topologies:** stream-aligned teams own a flow of work end to end and are the default; platform and enabling teams exist to lower their load. [Fowler](https://martinfowler.com/bliki/TeamTopologies.html), [Lucid](https://lucid.co/blog/understanding-the-4-main-team-topologies). Team size about 5 to 9, and Dunbar groupings (5, 15, 50, 150) **(memory; not confirmed by a source read here)**.
- **Amazon:** two-pizza teams (about 5 to 7) under a single-threaded leader who owns one thing. [Inc.](https://www.inc.com/jeff-haden/when-jeff-bezoss-two-pizza-teams-fell-short-he-turned-to-brilliant-model-amazon-uses-today.html), [SHRM](https://www.shrm.org/executive/resources/people-strategy-journal/Spring2019/Pages/galetti-golden.aspx)
- **Craigslist:** founder Craig Newmark called himself "customer service rep and founder"; tiny staff; "customer service has a lot more control over policy than I do." [encyclopedia.com](https://www.encyclopedia.com/books/politics-and-business-magazines/craigslist-inc), [MIT Tech Review 2005](https://www.technologyreview.com/2005/08/01/101200/socialized-computing-2/amp/)
- **Nextdoor:** launched one neighbourhood (Lorelei, Menlo Park) via its HOA board; founding members become Leads who verify neighbours and moderate. [Next City](https://nextcity.org/urbanist-news/building-the-facebook-of-neighborhoods), [Xconomy](https://legacy.xconomy.com/2014/01/23/walled-gardens-make-good-neighbors-argues-nextdoor-ceo/2)
- **Meetup:** grew through volunteer organizers; repeat attendees were prompted to start their own groups. [Hackernoon interview](https://www.hackernoon.com/the-past-present-and-future-of-meeting-people-with-meetup-founder-scott-heiferman-ae7f08951be8)
- **Community roles (CMX):** in a community-first company the community person is a very early hire, even at the top table; roles later split into engagement and operations. [CMX career path](https://cmxhub.com/an-introduction-to-the-community-career-path/), [CMX lead role](https://cmxhub.com/blog/what-does-a-lead-community-role-look-like-in-a-community-centric-company)
- **Trust and safety:** at a small startup it falls to the community manager or support; the first dedicated hire writes policy. [ActiveFence](https://activefence.com/blog/building-a-trust-and-safety-team), [TSPA](https://www.tspa.org/?p=4385)

**Applied recommendation** (my reading, not a source). Premise: AI agents write most code, so the scarce work is judgement, design, people, safety and the local market. Don stays the PM: ideas, versions, words and look.

**+1 person**

| Hire | Owns | Don stops | Main risk |
|---|---|---|---|
| Community and launch lead (local) | recruiting organizers and sellers in the metro, member support, first-line moderation, weekly member conversations fed back as evidence | answering members, chasing organizers, judging reports | becomes marketing, not listening; burns out holding safety alone |

**+3 people** (completes Cagan's trio around Don, plus the community lead)

| Hire, in order | Owns | Don stops | Main risk |
|---|---|---|---|
| 1. Community and launch lead | as above | as above | as above |
| 2. Technical lead (supervises agents) | feasibility, architecture, security, migrations, second-session review, on-call | being the last check on anything technical | becomes a lone coder instead of reviewing agents |
| 3. Product designer | usability, story maps, prototypes tested with members | sketching screens; designer brings options, Don picks look and words | blurs Don's look-and-feel right; agree who decides |

**+10 people** (two stream-aligned teams, one platform role, specialists)

| Hire, in order | Owns | Don stops | Main risk |
|---|---|---|---|
| 1 to 3. As in the +3 table | team A: "find and gather" | as above | as above |
| 4. Trust and safety lead | written policy, appeals, law-enforcement requests, safety data | ruling on individual cases | policy drifts from product without a seat in discovery |
| 5. Second product manager | team B: "buy, sell, trade", its outcomes and slices | running both journeys himself | two PMs pull the soul apart; Don sets outcomes, not features |
| 6. Second designer | team B usability | as above | design inconsistency between teams |
| 7. Second technical lead | team B feasibility and agent review | as above | two codebases in spirit |
| 8. Platform and agent-ops engineer | CI, agent tooling, data, performance, cost | knowing why the build broke | becomes a gate other teams wait on |
| 9. Second-metro launch lead | opening metro 2, local partners | being the face of each new city | copying metro 1 instead of listening |
| 10. Member operations and support | support queue, organizer success, money flows with the counsel repo | any member-ops ticket | support swamps the community lead without it |

- At +10 the company is about 11 people: under Dunbar's 15, so everyone can still know everyone, but decisions must be written. **(memory on Dunbar)**
- **Order of hiring and why:** community lead first, because the beta succeeds or fails on local people and agents can't do that work; then technical lead, because agents need a human checking correctness and safety; then designer, because Don's look-and-feel calls deserve real options; specialists only once two journeys run at once. **(applied)**

## 4. What was not read

- Every page fetch failed (host not allowed in this session): jpattonassociates.com (including "The new user story backlog is a map" and the story-mapping PDF), nngroup.com, oreilly.com, ronjeffries.com, radar.zurb.com. To read them, those hosts must be allowed in the session's network settings.
- Books not read: Patton *User Story Mapping* (2014), Cockburn *Writing Effective Use Cases* (2001), Torres *Continuous Discovery Habits* (2021), Cagan *Empowered* (2020), Skelton and Pais *Team Topologies* (2019). Claims rest on search excerpts, tables of contents, quotes and summaries.
- From memory, unconfirmed here: backbone not prioritised; slices named by outcome; "stories are for telling"; Team Topologies' 5 to 9 team size; Dunbar layers.
- Not found: Patton's "opportunity, discovery, build" stages as a primary text (only the book TOC and a podcast summary); an official CMX first-hire playbook; Nextdoor's own early staffing.
