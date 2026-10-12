---
id: F087
title: One create flow, and what you call it depends on what you are starting
status: draft
horizon: later
rank: 210
date: 2026-09-15
depends: [F060, F069]
---
## Story

Priya wants to convene a Tuesday run. Marcus wants to sell hot sauce. Dana is starting a monthly repair meetup. All three tap the same control and are asked one question first: what are you starting? Priya picks hosting a gathering, Marcus picks opening a shop, Dana picks starting a group. From there each sees a flow written in their own words, offering the tools their thing needs and not the ones it doesn't. Underneath, all three just created a Page. **None of them was ever told to open a shop in order to do something that isn't a shop.**

## Acceptance

1. **Every path through the create flow produces a Page.** An event is a post a Page makes, with no Page of its own (2026-10-01). There is no second entity, no alternative record, and no path that creates something else. *(Confirmed by Don 2026-09-15; `nouns.md`'s "no Page for a single occasion" was overruled the same day.)*
2. **Purpose is chosen first, from a named set**, before any other field. Nothing is pre-selected and nothing is inferred.
3. **The words shown to the person differ by purpose** — headings, labels, buttons, and the confirmation. Opening a shop, posting a gathering and starting a group read as three different things.
4. **The tools offered differ by purpose.** A purpose's flow omits steps its thing does not need, rather than showing them disabled or skippable.
5. **"Shop" never names the general act.** No string outside the shop purpose calls creating a Page opening a shop, and no person reaches a shop-worded step from a non-shop purpose.
6. **Every Page is an organization; the chosen type — Business (enterprise) or Social group — is stored and changeable any time in Page settings** (Don, 2026-10-05). Use cases are presets under the two types, and the type sets only the defaults a new Page starts with; any component can still be added to any Page (dispatch-decided 2026-10-05; Don can override). Locally owned is offered to businesses only. It confers no permission.

## Not this

Converting one Page into another — rejected outright since 2026-09-07 and still rejected. Creating two Pages at once; they are made sequentially. The business claim, which remains the friction gate and is separate from the purpose dropdown. Naming the members of the purpose set — that is Don's, and criterion 2 only requires it be named and closed.

## Why

### What this dissolves

**"Hosting requires opening a shop first" was never a missing substrate. It was a label on a door.** A 2026-09-15 read of the project named it the one awkward thing a person meets today; F060 already ticketed the entry point. This scenario makes the fix general instead of a special case for hosts.

### Checked against what is already approved — no conflict on self-classification

**The dropdown classifies the thing, not the person, and that is exactly what the existing rules ask for.** F060 criterion 2: *"`/you/create`'s first question is what they're starting, not what they are — no self-classification anywhere in the flow."* Don's dropdown asks what they are starting. **The rules it might have collided with are all about the person:** no stored role on a member, no account type, no umbrella noun for a person. None is touched.

**And a prior ruling already asked for this.** The 2026-09-07 ruling: *"Different creation flows per type is correct; nothing ever mutates."* F087 is that ruling built.

### The purposes themselves

**Named, defined, and sized in `product/systems/page-kinds.md`** (draft, 2026-09-15): someone selling, someone with a recurring gathering, and a deliberately thinner one-time gathering. That document carries what each needs at minimum, what it does not need, the schema recommendation, and the full list of what the thin one lacks.

### Settled — the one-time gathering

**Don ruled 2026-09-15:** *"We can create a page for every kind. It just doesn't require all of the same tools. It would still require an announcement and perhaps a following list and later messaging etc."*

**What differs between Pages is the tools.** *(The one-off Page went 2026-10-01: an event is a post.)* Every Page gets a baseline — announcing, and a following list — with messaging later. `nouns.md` was amended the same day; criterion 1 stands as written and is no longer in conflict.

**What this costs is in `planning/ONE-MODEL.md`** — the baseline is not free, and neither half of it has a writer today.

## Rulings
- **2026-10-05 — Purpose first, type for listing. Every Page has ONE primary purpose, what it mainly accomplishes. Beta's purposes are Create's four answers: Gather (find your people, meet regularly), Sell (make and be found), Offer a service or teach (a local pro, or someone who leads a class), Be creative (start or float something). The type, Business or Social group, follows from the purpose by default and can be changed in settings; it is what member browsing, filters and the Locally owned badge (business only) read.** The PM chose A. Later loops (Share/Ask, Pooling, Federation) get purposes when built; each purpose names the loops it serves in `product/needs/member-journey.md`. Carried forward from the line this replaces: the type sets defaults only, any component can be added to any Page, and Locally owned stays business-only. Existing Pages map business → Sell; place, interest, event_anchored → Gather; practice → Offer; family → Gather, private. `socialus-web` #363. [replaces 2026-10-05: Every Page is an organization. Its two primary types are Business (enterprise) and Social group; the use cases are presets and defaults under those two.] [binds tiers=planning,code surfaces=pages,create,page-settings,badges,explore]
- **2026-10-05 — A kind line sits under the Page's name on cards and in the Page header: kind icon · kind · main collection, for example "Business · Bakery".** Dispatch-decided 2026-10-05 under Don's delegation (*"knock items off without my help"*), from `socialus-design/research/BADGES-VALUES-KINDS-PLAN.md`; **Don can override.** Scenario: F087. [binds tiers=planning,code surfaces=cards,pages,explore]
- **2026-09-15 — At creation the list of labels stays short, and the list itself is left open pending research.** Don does not think this needs much worry. **A separate research task on comparable platforms and how people come together to work together will feed the label list**, so it is not guessed at now.
- **2026-09-15 — Proposed, not ruled: a label layer in front of the Page kind.** Don: *"let people choose based on their terms, but then it just directs them to whatever we're calling it behind the scenes so they don't need to guess based on an incomplete list of options."* **Many labels to one Page kind, held in a table** — not configuration and not seeded data, because both cost a deploy per label and labels will be added constantly. **Reuses the 2026-09-13 search-dictionary mechanism** (an agent proposes, a human approves) rather than inventing a second queue. **An unmapped label still works**: the Page is created, the label is kept as typed, it maps to a default kind and enters the queue. **That is what separates it from the retired "Something else" field, whose rows mapped to nothing and were read by nothing.** **It dissolves the four-community-kinds argument** — a label layer gives more recognition than four values ever could — **and it closes the farmers-market gap**, because a market is a label, not a kind.
- **2026-09-15 — There is one create flow and it always creates a Page. What the person is told they are doing is chosen up front from a named set.** Don: nothing is ever called "opening a shop" in general — a business is opening a shop, someone hosting is posting a gathering, someone starting a recurring meetup is starting a group, and all three are creating a Page. Copy and tools differ by purpose; the purpose gates nothing afterwards. **This dissolves "hosting requires opening a shop first" as a labelling problem, not a missing substrate.** Written as F087 (`draft`). **No conflict with the no-self-classification rule** — F060 already says the first question is *"what they're starting, not what they are"*, and every rule it might have hit (no stored role, no account type, no umbrella noun) is about the person. **It is the 2026-09-07 ruling "different creation flows per type is correct" finally built.** [for now]
- **2026-09-15 — Open, flagged by F087: does the host purpose create a Page or an Item?** Don's framing makes hosting a Page. `nouns.md` says "No Page for a single occasion" and `DECISIONS.md` 2026-09-07 says one-time events are Items with a date filed under a Page, because browse and the map would otherwise index listings as people and a follower graph on something ephemeral is worthless. **F087 criterion 1 assumes the Page reading.** Don rules.
- **2026-09-07 — Page creation drops the "both sell and host" option; Pages are created sequentially.** A one-line "start another Page" offer at the end of creation is the load-bearing mitigation.
