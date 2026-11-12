---
id: F102
title: The poster answers first, report misuse is tracked, and the platform holds steady Tuesday to Thursday
status: approved
horizon: now
rank: 190
gates: launch
date: 2026-10-05
depends: [F078, F100, F101]
approved: 2026-10-05 — the PM's ruling: "we want to track for Reporting abuse and have a plan for that. and we want to put as much back on the creator poster before we have to do anything … I want to do minimal work on my end." The auto-restore question below is open.
concept: new
amended: 2026-11-12 — the PM: new accounts start small; a banned number stays banned (15, 16); the safety package (17–21).
---
## Story

**One person runs the platform beside a day job and is mostly away Tuesday to Thursday, so moderation runs itself.** A bakery's Post is reported three times in an hour, twice by day-old accounts; it hides, the owner answers "Misusing reports", the row is flagged as possible coordinated reporting, and on Saturday the PM dismisses it in one swipe, which counts against each reporter.

## Acceptance

1. **When content hides, the poster is told the category and the reporter's reason (F078 criterion 3) and gets one answer**: fix and repost, or say the report is wrong.
2. **Fix and repost:** the poster edits the hidden content; the edit shows again at once and its reports stay on the row for review. A second hide on the same content offers no second repost. Not offered for severity 1.
3. **Say the report is wrong:** one of "Mistaken", "Malicious", "Misusing reports", plus a note of 280 characters at most. It is one answer per hide, it goes to the AI pass (F100) and onto the row (F101), and the content stays hidden until a person decides.
4. **No answer is no work:** an unanswered hide stays hidden and closes itself after 14 days, as F078 criterion 4 intends. The PM's batch shows it only if its severity is 1.
5. **Counters on the act of reporting, per reporter:** filed, upheld, dismissed, open. Operator-only, shown on the row, used by no feature outside the report path.
6. **The cap tightens with dismissals:** a reporter's hiding reports open at once start at 5 (today's constant) and drop to 1 after any dismissed report in the last 30 days.
7. **Cool-down:** two dismissed reports in 30 days start a 14-day cool-down in which that reporter's reports are stored and queued but hide nothing. F078's three strikes (reports stop hiding until the PM lifts it) stands above this.
8. **Coordinated reporting is flagged, not acted on:** three or more reports on one poster's content within 24 hours, at least two from accounts under 7 days old, mark the row "Possible coordinated reporting" and add one tier of priority within its severity.
9. **Tuesday to Thursday, with no person:** severities 2–4 stay hidden with any answer recorded and wait for the batch. Severity 1 stays hidden and the PM is texted (F078 criterion 5), with no expectation of same-day action.
10. **Report copy for threat of harm tells the reporter to call 911 if someone is in danger now**, kindly, before sending ([public-is-draft]).
11. **The PM gets one in-app summary on Friday morning**: waiting rows by severity, answers received, cool-downs started. Nothing else asks for attention midweek except severity 1.
12. **Severity 4 restores itself in beta, narrowly (ruled B):** only when the poster answered, Haiku and Sonnet both suggest approve at ≥ 0.95 (Sonnet runs on every such candidate, not only below F100's escalation threshold), there is no coordinated-reporting flag, and the harness has cleared F100 criterion 11's targets on the severity-4 slice. The restore is a logged, reversible decision attributed to the AI, and the batch shows it as "Restored by AI" for a one-tap confirm or undo. Severities 1–3 never restore without a person.
13. **Every upload and every post records the IP address and time it came from**, operator-only, kept one year and then deleted, so abuse and legal requests can be traced. It is shown to no member and used by no feature outside the report path.
14. **Child-safety content (severity 1, apparent CSAM) is a legal tier, not a moderation judgement** (18 U.S.C. 2258A; `socialus-legal` `safety/ncmec-plan.md`): it never auto-restores, never goes back to the poster for an answer, gets no AI processing (F100 criterion 12), and is preserved and reported to NCMEC per the plan. The poster-answers-first rule (criteria 1–4) and narrow auto-restore (12) apply to every other tier.
15. **New accounts start small for 7 days:** 3 posts a day and first messages to 10 people a day; replies, follows, Going and hearts are not limited. It lifts on day 8 by itself. At the limit, one line says when they can post again ([public-is-draft]). Configurable without a deploy.
16. **A banned number stays banned:** a ban keeps a one-way hash of the number, never the number, and it cannot sign up again (F081), even after deletion. Banning stays a person's act.

17. **Removal for a violation bans the number for good** (16).
18. **Apparent CSAM goes to NCMEC** (14): a duty on actual knowledge, with no duty to scan (2258A(a), (f)).
19. **A credible threat goes to the police with the poster's number,** by a person, per the staff runbook.
20. **Evidence (content, number, IP, time) is kept one year from the report** (13), matching 2258A's one-year preservation (REPORT Act, 2024).
21. **A fresh prepaid line gets extra caution:** its first reports rank one tier higher.
[open-question owner=code raised=2026-11-12] Which signal marks a fresh prepaid line: Telesign's subscriber status (enterprise accounts only), Twilio SIM Swap (US gives only yes/no, private beta), or none until a vendor gives one at our size?
[open-question owner=don raised=2026-11-12] Should a reported or repeat account be asked for a photo ID check? Not decided; nothing is built.

## Not this

Telling a reported member who reported them (2026-09-30 ruling). Auto-banning accounts. Acting automatically on a coordinated-reporting flag. Email.

## Why

**The PM, 2026-10-05:** put as much back on the poster as possible and keep his own work minimal and batched. Every step moves work to the poster, a rule, or the Friday-to-Monday batch.

**Path: new territory.** It touches member trust, F078's strike rule and the beta shadow ruling.

### Precedent

Reddit acts on abuse of the report button ([r/modnews](https://www.reddit.com/r/modnews/comments/cgxuep/were_rolling_out_a_new_way_to_report_abuse_of_the/)); YouTube gives an appeal per strike ([help](https://support.google.com/youtube/answer/185111?hl=en)); Discord AutoMod times out the act ([FAQ](https://support.discord.com/hc/articles/4421269296535)): counters, the poster's answer and cool-downs come from these.

### Unattended time

Hiding is the safe default, so midweek nothing needs a person; waiting costs only content that is fine, which the poster's answer, narrow auto-restore (12) and the batch handle.

### Size

[platform store=ugc: the report path, the poster's answer and report-misuse limits are part of the moderation app stores require of an app with user-generated content]

About 3 build days; 15–21 ride on #1280, #1288.

## Rulings
- **2026-11-12 — The safety package: removal bans the number for good; apparent CSAM goes to NCMEC; credible threats go to the police with the number; evidence is kept one year per the 2026-10-05 retention ruling; a fresh prepaid line gets extra caution; every photo is hash-checked and every post screened before publish (F080). Photo ID for reported or repeat accounts is not decided.** The PM: *"no user of ours thinks that they can post anything anonymously and that if they do post anything heinous or dangerous or gross that we will know who they are and will take swift action."* Path: new territory. [always] [replaces none] [binds tiers=planning,code surfaces=moderation,reports,abuse,uploads,signup] Issue: #1280.
- **2026-11-12 — New accounts start small for 7 days, and a banned number stays banned (as a one-way hash).** The PM: "yes for new accounts starting small", bending the trust-first default for a week. Evidence: `planning/research/phone-sign-up-2026-11-12.md`. Path: well-worn. [for now] [replaces none] [binds tiers=planning,code surfaces=posting,messages,abuse,signup] Issue: #1280.
- **2026-10-16 — The "no score on a person" rule is removed.** Person ratings are open to design (e.g. Uber-style two-way ratings between members and Pages). [replaces 2026-10-12: The platform never rates, ranks or labels a person] [replaces F102: never as a score, rank or label on a person] [for now] [binds tiers=planning,code surfaces=members,reports build=none]
- **2026-10-11 — Apparent CSAM is reported through NCMEC's manual CyberTipline web form for beta, and through registration with the CyberTipline when the entity structure is set up and we go public (entity questions go to `socialus-legal`). Preservation is built now either way. A staff runbook (apparent CSAM, threats of harm, other severities: step by step, phone-readable, linked from the admin reports page) and a reminder tied to entity setup ("register with the CyberTipline and switch from the manual form") are in scope. We collect enough member information (verified phone, legal name, F077/F081) to act on abusive or harmful content and say plainly that we do not tolerate it; per policy it is collected for the platform's protection and not shown member to member.** The PM, 2026-10-11, option B for beta and A at public launch, on `socialus-web` #648 (F102 criterion 14). [replaces none] [binds tiers=planning,code surfaces=moderation,reports,uploads,privacy] Issue: #648.
- **2026-10-06 — Apparent child sexual abuse material (the child-safety tier, severity 1) is a legal requirement, not a moderation judgement: it never auto-restores, never goes back to the poster for an answer, gets no AI processing, and is preserved and reported to NCMEC per the plan.** Because a US provider must report apparent CSAM to NCMEC's CyberTipline "as soon as reasonably possible" once aware (18 U.S.C. 2258A) and preserve it (`socialus-legal` `safety/ncmec-plan.md`, ruled 2026-10-05). F102's poster-answers-first rule and narrow auto-restore apply to every other tier. Scenario: F102 (criterion 14). The weekend batch does not govern this tier; counsel is asked whether the plan's 72-hour target meets the duty. [always] [binds tiers=planning,code surfaces=moderation,reports,ai,uploads]
- **2026-10-05 — In beta the AI restores severity-4 reported content on its own, narrowly: only when the poster answered, Claude Haiku and Claude Sonnet both suggest approve at 0.95 or higher, nothing flags coordinated reporting, and the evaluation harness has passed on that slice. Severities 1–3 currently never restore without a person.** The restore is logged, reversible and shown in the weekend batch for a one-tap confirm or undo. Option B of F102's A/B/C. Scenario: F102. [for now] [binds tiers=planning,code surfaces=moderation,reports,ai]
- **2026-10-05 — Every upload and post records the IP address and time it came from, operator-only, kept one year and then deleted.** For tracing abuse and answering legal requests; no member sees it and no feature outside the report path reads it. The privacy policy must disclose it. Scenario: F102. [binds tiers=planning,code surfaces=uploads,posts,privacy,moderation]
- **2026-10-05 — Moderation is designed to run unattended: one person operates the platform alongside a day job and is currently away Tuesday to Thursday, so review work is batched Friday to Monday and nothing midweek asks for attention except severity 1.** The constraint behind F100, F101 and F102; a design that needs a person midweek fails it. Scenarios: F100, F101, F102. [binds tiers=planning,code surfaces=moderation,reports,process build=none]
- **2026-10-05 — When content hides, the poster answers first: fix and repost, or say the report is wrong. Report misuse is tracked as counters on the act of reporting (filed, upheld, dismissed, open).** Dismissed reports tighten a reporter's hiding cap and can start a cool-down; coordinated reporting is flagged for the operator, not acted on automatically. Whether the AI may auto-restore severity-4 content in beta is open in F102. Scenario: F102. [always] [binds tiers=planning,code surfaces=moderation,reports,members]
