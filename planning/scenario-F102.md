---
id: F102
title: The poster answers first, report misuse is tracked, and the platform holds steady Tuesday to Thursday
status: approved
gates: launch
date: 2026-10-05
depends: [F078, F100, F101]
approved: 2026-10-05 — the PM's ruling: "we want to track for Reporting abuse and have a plan for that. and we want to put as much back on the creator poster before we have to do anything … I want to do minimal work on my end." The auto-restore question below is open.
---
## Story

**The constraint behind this design: one person runs the platform alongside a day job, and is mostly unavailable Tuesday to Thursday. Moderation has to run itself, and the PM's work is minimal and batched Friday to Monday.**

On Tuesday a bakery's Post is reported as spam three times in an hour, twice from accounts made that morning. It hides. The owner is told why and gets one answer: fix and repost, or say the report is wrong. They pick "Misusing reports" and write a line. The AI reads it; the row is marked as possible coordinated reporting, and the reporters' records sit beside it. Nobody acts until Saturday, when the PM approves it in one swipe. That dismissal counts against each reporter's record, and one of them now waits two weeks before a report of theirs hides anything again.

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

## Not this

A score, rank or label on a person. Telling a reported member who reported them (2026-09-30 ruling). Auto-banning accounts. Acting automatically on a coordinated-reporting flag. Email.

## Why

**The PM, 2026-10-05:** *"we want to track for Reporting abuse and have a plan for that. and we want to put as much back on the creator poster before we have to do anything. We give the creator a second chance to provide feedback that the report was malicious or ridiculous and being misused etc. I want to do minimal work on my end."* **The operating constraint** is the whole reason: every step here either moves work to the poster, moves it to a rule, or moves it to the Friday-to-Monday batch.

**Path: new territory.** It touches member trust, F078's strike rule and the beta shadow ruling.

### Counters on the act, not a score on the person

**ROADMAP § Won't: the platform currently doesn't rate, rank or label a person.** So nothing here is a reputation: no score, no badge, no tier on a member. What exists is counts of reports filed and how each ended, and caps and cool-downs on *the act of reporting*, exactly like today's per-reporter caps in `report.create` (5 open hiding reports, 20 open in total, 2 per subject). The counts are visible to the operator only and feed nothing outside the report path.

### What changes against today (read in `socialus-web` main, 2026-10-05)

- **The poster is told nothing today** (`report.create`: "no notification to the reported party"); F078 adds the notice and one rebuttal, and F102 gives the rebuttal its choices and the fix-and-repost path.
- **Caps exist but do not learn:** `MAX_OPEN_REPORTS_PER_REPORTER = 5`, `MAX_OPEN_REPORTS_TOTAL = 20`, `MAX_REPORTS_PER_SUBJECT = 2` are constants that ignore outcomes. Criteria 6–7 make the first one depend on dismissed reports.
- **No account-age or burst check exists.** Criterion 8 is new, and is a flag only.

### Precedent

- **Reddit** lets moderators report abuse of the report button itself, and acts on the reporter, up to suspension ([a new way to report abuse of the report button](https://www.reddit.com/r/modnews/comments/cgxuep/were_rolling_out_a_new_way_to_report_abuse_of_the/)). Tracking outcomes per reporter comes from that.
- **YouTube** gives the creator an appeal on each strike and lifts a strike when the appeal succeeds ([appeal a Community Guidelines strike](https://support.google.com/youtube/answer/185111?hl=en)). The poster's one answer comes from that.
- **Discord AutoMod** applies time-outs to the act, not a rating of the member ([AutoMod FAQ](https://support.discord.com/hc/articles/4421269296535)). Cool-downs come from that.

### Unattended time

Hiding is the safe default, so midweek nothing needs a person: content that might be bad is already down, and the cost of waiting falls on content that is fine, which the poster's answer and the batch handle.

[open-question owner=don raised=2026-10-05] **Apparent child sexual abuse material carries a US provider duty to report to NCMEC "as soon as reasonably possible" (18 U.S.C. 2258A).** That sits badly with a weekend batch and with the purge path (`socialus-web` `docs/purge-proposal.md`). New territory for the PM and counsel before production; not designed here. Beta's rule (F080: no images of children at all) narrows but does not remove it.

### Shadow mode against an empty Tuesday

[open-question owner=don raised=2026-10-05] **Should the AI auto-restore spam and other (severity 4) in beta?** Shadow mode means a mistaken spam report keeps a fine Post down until the weekend.

- **A — Pure shadow (as ruled).** Nothing restores before the batch. Cost: a fine Post can sit hidden up to four days.
- **B — Narrow auto-restore, recommended.** Severity 4 only, the poster answered, Haiku and Sonnet both suggest approve at ≥ 0.95, no coordinated-reporting flag, and only once the harness clears F100's targets on the severity-4 slice. Logged, reversible, and shown in the batch as "Restored by AI" for a one-tap confirm or undo. Cost: the AI acts before production on the lowest-harm tier.
- **C — Rule, not AI.** Severity 4 restores whenever the poster answers. Cost: a spammer restores their own spam by answering.

**Recommend B:** restoring is the reversible, low-harm direction, the gate keeps it off until the harness has measured it, and it removes the most common midweek wait.

### Size

**About 2 build days, in the beta (2026-10-30)**, after F078's notice: the answer choices and fix-and-repost (1 day); counters, cap and cool-down (half a day); the coordinated flag and the Friday summary (half a day). B adds about half a day. What to push is in F101 § Size.
