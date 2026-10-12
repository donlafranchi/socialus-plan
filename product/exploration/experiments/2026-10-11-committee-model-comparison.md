---
id: exp-2026-10-11-committee-model-comparison
title: Committee model comparison, "Wish it existed" (plan #101 vs #102)
status: done
date: 2026-10-11
experiment: nine council roles on Sonnet (chair Opus 4.8, blind) vs the default-model committee run with Don's follow-up guidance
---

# Committee model comparison: "Wish it existed"

**As of 2026-10-11** · Source: socialus-plan #101 (brief on main) and #102 (experiment file on its branch), the `plan-feature` skill, `planning/council/feature-intake.md`, `socialus-web` main · Maintained by: hand (ops session)

**Question.** Is Sonnet good enough for the nine lower-level committee roles? Two briefs on the same concept were scored on one rubric, 1 to 5 each, with an example per score.

| | **#101** (normal run) | **#102** (model test) |
|---|---|---|
| Roles / chair | default light model / default chair | Sonnet / Opus 4.8 |
| Context | the concept plus three rounds of Don's guidance (#98 to #101) | fresh context, blind, a chair-written facts brief |
| Output | `planning/briefs/2026-10-11-wish-it-existed.md`, merged | `product/exploration/experiments/2026-10-11-committee-model-test-wish-it-existed.md`, PR open, lint red |

**The confound, stated first.** #101 is not one run. Its brief was built across four PRs in 17 minutes (#98 council run, then #99, #100, #101 chair-only edits after Don dictated backers, option A, the launch phase and no expiry). #102 ran once, blind, with none of that. Where #101 scores higher on fit or clarity, part of the margin is Don's words, not the model. Where #102 matches #101 on gates and risks with no guidance, that is the strongest evidence in this comparison.

## Scores

| Rubric | #101 | #102 | What decided it |
|---|---|---|---|
| (a) Follows the skill's steps and outputs | 3 | 4 | #102: Stage 0 table with verified or assumed per line, prerequisites first, nine roles with Needs, Cost, Veto, Risk, three sizes with all six rows, honest gates (five boxes left unticked), A/B/C with a recommendation, a self-report. Deviations: criteria in §6 instead of the frontmatter the skill asks for; an `exp-` id. #101: criteria in the frontmatter as the skill says, precedents labelled looked-up; but four sizes (T0 to T3) instead of three, a tenth role (Backer) added, Don's rulings written into the brief as a "Decided" paragraph with no dated ruling, which the handoff rule requires the same day. |
| (b) Concrete testable criteria | 4 | 4 | #101: 24 criteria tagged launch or if-popular; "the count is said in words, with 'Nobody's shown interest yet' at zero" is binary. Weak: W1.9 "tags let a replier find wishes in their kind of work". #102: 19 criteria; "no leaderboard or admin UI exists (route and query search returns none)" and "a second identical signal is a no-op enforced by a DB constraint" are mechanically checkable. Weak: #13 "beyond what the wanter explicitly consented to" with no consent step, #14 "relevance order" undefined. |
| (c) Fit with rulings | 4 | 4 | #101: a "Why it fits (members first)" section with both flips; the Sample rule applied exactly as ruled 2026-09-17 (bounded block, heading, mark, not in search, no controls); backing is not investing with the highest level held for counsel. Miss: W1.2 lets a replier publish "a way to be reached" on a public reply, which is the contact-exposure the 2026-09-30 names rulings guard against, and it is not reconciled. #102, blind: reached the same securities and UPL gates, no paid reach, no boost, Sample rows labelled and excluded from every real number, no legal words between members. Miss: no members-first framing at all; treats Don's template aim as a risk without recording his purpose. |
| (d) Feasibility against today's code | 3 | 3 | Both ran in the planning repo and neither read `socialus-web`. What is there: `items` has the seven-kind enum with `wonder` live and `offer`, `ask` reserved; `item_wonders` carries `interest_count` and `item_responses` is the interest join, so the "show interest" substrate #101 calls undesigned exists; the create action is kind-agnostic but gates `wonder` out; there is no reply surface; `page_posts.sample_kind` covers only event, deal and last-minute on Pages, not items. #101's launch phase (a Page, ordinary posts, 0 to 6 h) is buildable today, but its own launch criteria are not: W1.12 "no expiry" contradicts migration 015, where a wonder's `expires_at` defaults to 90 days (the PR corrected `verbs.md` and missed the schema). #102's first slice (wish page plus "I can build that", 14 h) needs a cross-member reply path and an operator approval queue, neither of which exists; its Developer said "no repo write-path found this run" and labelled the whole row assumed, which is honest but not feasibility. |
| (e) Risks caught | 4 | 5 | #102: off-platform solicitation ("a scammer posts Tue, hits a member Wed, nobody acts until Fri") with a mitigation (offers hidden until Fri to Mon approval, contact stripped); the platform becoming record-keeper and dispute party if agreement state lives in it; "generate revenue for members" as an outward promise; maker ratings as trust drift; the silence-vs-no-count tension handed to Don as the one open design call. #101: the Missing-pets pattern (rants, scams), wishes that are job postings, duplicate wishes with no dedupe, "the reply is just messaging and grows", a built thing that fails or hurts. Miss: it allows public contact details and names no scam mitigation. |
| (f) Precedents with real links | 5 | 2 | #101: six precedents with URLs, labelled looked up this run, one marked as a secondary source, one (Nextdoor ISO) marked recalled; five of six URLs answer 200 today, Etsy's help centre answers 403 to a script but is a real page. #102: eight precedents, zero URLs, and a contradiction in one line: "all recalled unless noted; Scout web-searched this run". |
| (g) Clarity for Don on a phone | 4 | 3 | #101: Don's phase rule in his own words near the top, narrow tables, the A/B/C at the end with the recommendation first and a "Decided / Still open" split. #102: the roles table has ten rows of 60 to 90 words per cell across five columns, unreadable on a phone; the A/B/C itself is clear and recommends A1 in one line. |
| (h) Cost and time | 3 | 4 | #102 self-report: nine agents in parallel, council wall time about 1m45s, about 47k tokens each (0.42M across nine, the chair merge not reported), dispatch to PR about 5 minutes (19:46 to 19:51 UTC). #101, estimated: the #98 council covered three concepts in one light-model pass (about 0.3 to 0.4M tokens per concept) plus three chair-only follow-ups at roughly 0.1M each, about 0.7 to 0.8M tokens and 17 minutes of PR time, plus three dictation turns of Don's. #102 loses a point because all nine roles converged on the same slice, so most of the nine agents bought confirmation, not breadth. |
| **Total** | **30** | **29** | |

## Is Sonnet good enough for the lower-level roles?

**Yes for the judgement roles, with two named exceptions.** Blind, the Sonnet panel reached every gate the guided run reached (securities to counsel, no platform-authored legal text, no platform-held money, Sample rows excluded), added the solicitation risk and its mitigation, and found the one design tension (silence vs no-count) that #101 never names. Guardian, Money, Operator, Tester, Person and Maker are good enough on this evidence.

**Where it fell short:**
- **Scout.** No URLs, and a sentence claiming both "recalled" and "web-searched". The skill's red flag ("precedents from memory are fine") is exactly this. Fixable by instruction: a Scout output with no URL is rejected by the chair.
- **Developer and Architect.** Hours were low (14 h for a slice that needs a reply surface nobody has built; #101's chair had already raised the committee's 12 h to 30 h for the same reason) and nothing was verified in the repo. Both roles labelled their rows assumed, which is correct behaviour, but it means the brief's feasibility came from the chair's facts brief, not the roles.
- **Breadth.** Nine roles produced one answer. Convergence this high means the facts brief did the thinking; a Sonnet panel reads its brief faithfully and does not argue with it. The chair, not the roles, is where the default model earned its keep in #101 (correcting hours, folding Don's rulings, writing the member-first framing).

## What to change in the next test

1. **Same inputs, one variable.** Give the Sonnet panel the same facts brief and the same three rounds of Don's guidance that #101 had, chair unchanged (Opus 4.8), and score again. Then a second run that swaps only the chair. Today's comparison changed context and model at once.
2. **Make Scout and Developer prove it.** Scout must return a URL per precedent and the chair runs `curl` on each; Developer runs in the code repo with `grep` and cites a file or migration per estimate. Score (d) and (f) are then about the model, not about access.
3. **Round 2 where roles disagree** (feature-intake V2). With Round 1 only, a panel that converges looks the same whether it is right or merely obedient. A forced objection round shows whether Sonnet can dissent.
4. **Blind scoring.** Hand both briefs, stripped of their experiment notes and model lines, to a scorer that does not know which is which, on this rubric.
5. **Fix the lint red on #102 before it merges or is closed:** the phrase post-beta written inside square brackets reads to the lint as a citation of an absolute that does not exist.
