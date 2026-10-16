---
id: community-review
title: Community review — neighbours who help decide reports (2026-10-13)
status: reference
date: 2026-10-13
---
# Community review

**A report goes to a small random panel of opted-in local neighbours, who decide keep or hide; the owner sees the outcome and the reason, and Don only handles threats, child safety and legal. It is a well-worn path at Nextdoor's scale, but at beta size the panels would mostly be empty, so it fits best as the next step after beta, switched on per metro once enough neighbours have opted in.**

**Your call:** A, B or C at the end. Recommend **A**: ship the Page-words fix (web #625) on today's courtesy-first flow now, collect "neighbours who help" opt-ins during beta, and turn panels on per metro when the pool is big enough.

## The picture

**Five parts: the report, the AI hint, the panel, the outcome to the owner, and a narrow lane to Don.**

<details><summary>Details</summary>

```
report ──► courtesy notice (first report, unchanged)
   │
second report from a different member
   │
   ├─ threat of harm / sensitive / legal ──► hides at once ──► Don (unchanged)
   │
   └─ everything else ──► AI reads it (hint only)
                             │
                      random panel of 3 neighbours who help
                             │
                  2 of 3 agree ──► keep or hide, with a one-line reason
                             │
                  owner sees outcome + reason; one answer goes to a fresh panel
```

- **The report** works as it does today: a first report is a courtesy notice, a second from a different member starts review.
- **The AI hint** is the shadow read F100 already runs. Panelists see its suggestion after they vote, or not at all; it never decides.
- **The panel** is 3 neighbours drawn at random from members in the same metro who opted in, have been members long enough, and have nothing to do with the case.
- **The outcome** goes to the owner in-app with the panel's chosen reason. The owner's one answer (F102) goes to a fresh panel, not to Don.
- **Don's lane** is what a member must never judge: threats of harm, child safety (a legal duty), and legal requests.

</details>

## Why it answers Don's problem

**It takes the judgement call off Don and gives it to neighbours, which is what "the community keeps each other decent" means in practice, and it ends the "not hiding teaches people to ignore it" loop because every report gets a real answer within a day or two.**

<details><summary>Details</summary>

Don, 2026-10-13: *"not hiding does nothing. this teaches people to ignore it. on the other hiding it and resending to the owner may or may not change behavior and just causes more work… its all judgement calls. I need an approach that doesn't put the burden on me and allows the community to keep each other decent."*

- **"Judgement calls"**: a panel of three neighbours is a better judge of local norms than one operator, and two of three agreeing is a decision without Don.
- **"Not hiding does nothing"**: the reporter learns the outcome. A report that leads to a verdict is not ignored, even when the verdict is keep.
- **"More work"**: the owner's answer goes to a fresh panel, so a dispute never lands on Don.
- **"Misused the report button"**: a panel that votes keep is the dismissal F102 already counts against the reporter, without Don.

</details>

## Precedents

**Nextdoor runs this at scale and it works there; X's Community Notes shows how to resist brigading but needs far more raters than we will have. Both route the hardest cases to staff.**

<details><summary>Details</summary>

**Nextdoor: volunteer reviewers vote on reported content.** Checked against the source:
- 2023 transparency report: *"nearly 200,000"* volunteer community moderators reviewed **90% of reported content**, with a **median removal time of 5.3 hours** ([Nextdoor, Feb 2024](https://blog.nextdoor.com/2024/02/13/nextdoor-2023-transparency-report)). Our earlier exploration quoted these correctly.
- 2021: volunteers reviewed 86.9% of reported content and voted to remove 52.5% of it, median 4.6 hours ([Nextdoor 2021 report via Business Wire](https://www.businesswire.com/news/home/20220223005561/en/Nextdoor-Publishes-First-Annual-2021-Transparency-Report)).
- Reviewers **apply** and must be active neighbours; reports of misinformation or racism go **straight to trained staff**; reports about a person (an account) are always staff ([How moderation works, Nextdoor, 2021](https://blog.nextdoor.com/2021/02/10/how-moderation-works-on-nextdoor)).
- Not found in Nextdoor's own pages: how many votes decide, or how appeals are routed. A third-party summary says appeals go to a different set of reviewers; unverified, so not relied on here.
- What we keep: neighbours judge content, staff keep accounts and the dangerous categories. What we change: random panels instead of whoever shows up, because a small metro can't absorb self-selection.

**X Community Notes: bridging, so one faction can't win.** Checked against the source:
- A note needs **at least 5 ratings**, and shows when its helpfulness score passes **0.40**; the score comes from a model that only rewards notes rated helpful by people who **usually disagree** ([Community Notes ranking, open source](https://github.com/twitter/communitynotes/blob/main/documentation/under-the-hood/ranking-notes.md)).
- The cost: only **about 11.5%** of notes ever reach agreement, and published notes appear **65.7 hours** after the post on average ([Timeliness, Consensus, and Composition of the Crowd, 2025](https://arxiv.org/abs/2510.12559)). Another study finds about 10% rated helpful, Nov 2022 to Jul 2024 ([Request a Note, 2025](https://arxiv.org/abs/2509.09956)).
- What we keep: the idea that agreement across people who don't know each other beats a majority of friends. What we change: bridging needs a rating history per rater, which a beta metro won't have. We get a cheap version from random draws and conflict exclusions; real bridging is later, if ever.

**League of Legends Tribunal (2011–2014): a jury of players.** Riot's own figures: 92.7% of cases ended in punishment, and 74% of players warned once never returned ([Riot's Lyte, 2013, via Surrender at 20](https://www.surrenderat20.net/2013/01/lyte-talks-tribunal.html)). It was retired for being slow. Lesson: juries tend to agree with the report, so the reason given to the owner and a fresh-panel answer matter.

</details>

## Rulings it touches

**Three rulings shape it and one would change: the second report would send content to a panel instead of "a person on our team".**

<details><summary>Details</summary>

- **Eligibility is tenure** (days since joining); F102 already uses account age the same way for its coordinated-reporting flag. Opting in is the member's own choice, like any sharing setting.
- **Roles are derived, never stored (principle).** "Neighbour who helps" is an opt-in setting, not a role; eligibility is worked out at draw time.
- **Self-correct first (2026-10-11).** Kept: the courtesy notice still comes first. The panel only sees what a second report hides.
- **Don runs it alone, away Tuesday to Thursday (2026-10-05).** Improved: panels decide midweek, so a fine post isn't down until Saturday.
- **Nothing that outgrows one person.** Improved: work grows with the panel pool, not with Don.
- **Changes: "a second report hides it and sends it to a person on our team" (F078, 2026-10-11).** The panel replaces the person on our team for everything outside Don's lane. That's a ruling change, so this is **new territory**.
- **Unchanged:** threat of harm and sensitive content hide at once and go to Don; child content never goes back to the poster and gets no AI processing (F102, legal); reporters stay anonymous to the owner (2026-09-30). Panelists are anonymous too.
- **"We don't subject our team to unpleasant content" (2026-09-30).** Panelists are members, so the same care applies: they never see the sensitive categories, every case opens with the reason first, and they can skip any case.

</details>

## Risks and fallbacks

**Two risks: friends voting together (brigading) and too few neighbours in a small metro. Both have a simple fallback: the case falls back to today's flow.**

<details><summary>Details</summary>

**Brigading: a group gets onto panels to keep a friend's post up or take a rival's down.**
- Panelists are **drawn at random**, never volunteered per case, so nobody can choose a case.
- **Excluded from a draw:** the reporter(s), the owner, anyone on that Page, anyone who reported or was reported in that case, and members under the tenure floor (start at 30 days).
- **A cap** of a few panels per neighbour per week, so a small group can't sit on everything.
- **The owner's answer goes to a fresh panel** with none of the first three.
- **F102's coordinated-reporting flag** (3 reports in 24 hours, 2 from new accounts) skips the panel and goes to Don's batch, as today.
- **Later, if needed:** a light bridging check (a split panel goes to a larger one) once there is enough history.

**Empty panels: a beta metro with a few dozen members won't have 3 eligible, unconnected neighbours on call.**
- **Panels turn on per metro when the pool reaches a set number** (start at 15 eligible opt-ins), stored as a value on the metro the way the hide bar is: no code change to turn on.
- **A case with no quorum in 48 hours falls back to today's flow:** it stays hidden and joins Don's Friday batch.
- **Below the threshold, the metro runs today's flow**, and the opt-in quietly builds the pool.

**Smaller risks**
- *Panels agree with the reporter too often* (Tribunal): track keep/hide rates per metro; the owner's fresh-panel answer is the check.
- *Panelists burn out*: cap per week, skip any case, thank them; no badges (no labels on people).
- *A wrong hide stays up for days*: 48-hour quorum window, then today's flow.

</details>

## What beta needs vs later

**Beta needs none of the panel machinery. The only beta piece worth building is the opt-in, so the pool exists when a metro is ready.**

<details><summary>Details</summary>

**Beta (with option A):**
- The #625 fix as built on today's flow: first report is a courtesy notice, second hides only the Page's words, the Page stays up.
- A "neighbours who help" opt-in in settings (copy is Don's). About half a day.

**After beta, per metro, when the pool is ready (about 3–4 build days):**
- The draw (random, exclusions, cap), a phone-sized vote screen showing the content, the reason and three choices, the 2-of-3 rule, the reason to the owner, the fresh panel for the owner's answer, the 48-hour fallback, and the per-metro switch.
- "Stricter panel for a repeat": a Page with upheld hides in the last 90 days gets a panel of 5 needing 4 to keep. That counts outcomes on the content, operator-only, like F102's counters on the act of reporting, never a mark on the person.

**Later still:** bridging, a reviewer guide, an AI-drafted reason the panel can accept or edit.

</details>

## Against the earlier #625 options

**Community review answers who decides after something hides; A/B/C answer what hides. They stack: community review works best on top of A.**

<details><summary>Details</summary>

| | What hides | With community review |
|---|---|---|
| **A** First report: notice only. Second report: only the words hide, the Page stays up | Smallest harm if wrong | Panel decides the words; the rest of the Page never goes down. **Best fit.** |
| **B** Second report hides the whole Page | A rival with a friend can take a business offline | Panel shortens the outage but doesn't remove it |
| **C** Hide on the first report | Breaks courtesy-first (2026-10-11) | Panel load doubles: every report is a case |

The courtesy notice (#220's live check) is the same under all three; it doesn't wait on this.

</details>

## Your call

**Recommend A.**

- **A. Ship #625 on today's flow now; add the opt-in in beta; panels turn on per metro once the pool is big enough (recommended).** Trade-off: Don still clears the Friday batch until a metro's pool is ready.
- **B. Build community review into beta now.** Trade-off: 3–4 more build days before beta for panels that would mostly fall back to Don anyway.
- **C. Don't adopt community review; stay with courtesy-first plus raising the hide bar as volume grows.** Trade-off: Don stays the judge, so his load grows with every metro.

[open-question owner=don raised=2026-10-13] Community review: A, B or C (above). Recommend A.
