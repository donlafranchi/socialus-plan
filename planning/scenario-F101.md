---
id: F101
title: One scannable page of flagged and reviewed Posts, decided in one tap
status: approved
gates: launch
date: 2026-10-05
depends: [F078, F080, F099, F100, F102]
approved: 2026-10-05 — the PM's ruling: "a clean page of 'Posts' for all flagged and reviewed content … quickly and easily scannable and possible sortable by how serious the allegation is", and the same day, "easy to review and pass or fail with either a swipe or a big button for approve … minimal steps for approve or deny".
---
## Story

**The constraint behind this design: one person runs the platform alongside a day job, and is mostly unavailable Tuesday to Thursday. Moderation has to run itself, and the PM's work is minimal and batched Friday to Monday.**

Saturday morning, on a phone, the PM opens Posts. The header says 31 waiting: 1 severity 1, 4 severity 2, 26 below. The worst is on top. Each row shows enough to decide: a thumbnail, a line of text, the badge, "Harassment ×3", "AI: remove · 0.91", the poster's rebuttal, the reporters' record, and how long it has been hidden. The PM swipes right on a spam report the poster rebutted; it is approved, a toast offers Undo for five seconds, and the next row slides up. A big Remove button handles the next. The severity-1 row asks once more before anything restores it. The batch is done in minutes.

## Acceptance

1. **An operator-only page, Posts, lists every reported subject one row each**: a Post (its photo's reports roll into its row), a Page or a Page picture. Non-operators get 404, as `/admin/reports` does today.
2. **Each row shows:** thumbnail; text excerpt (120 characters at most); severity badge; report reason(s) and count; AI suggestion and confidence (F100); the poster's rebuttal (F102); the reporters' counters and any coordinated-reporting flag (F102); status (hidden, restored, removed, under appeal); age since hidden.
3. **Severity is 1–4** (§ Why): the highest tier among the row's open reports. In shadow mode the reporter's category sets it and the AI's tier shows beside it; in live mode the higher of the two sets it.
4. **Default order: severity, then oldest hidden first.** Sortable by severity, age and report count; filterable by status. The header counts waiting rows by severity.
5. **Two actions, Approve and Remove, as full-width buttons on every waiting row**, at least 48 px tall, in the bottom half of the row. Approve restores the content and closes its reports; Remove keeps it down and closes its reports.
6. **Swipe right approves; swipe left removes.** Each with the action's colour and word revealed under the row as it moves.
7. **One decision is at most one tap or one swipe from the list.** Severity-1 Approve is the one exception: one extra confirm, so two taps.
8. **No confirm dialog otherwise; an Undo toast for five seconds.** An undone decision writes no decision row and sends the member nothing.
9. **The next waiting row moves into place automatically** after each decision.
10. **A one-tap decision records a default reason**: Approve → "Nothing wrong with it"; Remove → the reason that matches the row's top category. The reason can be changed afterwards from the row's detail.
11. **A decision on a row writes one `report_decisions` row per open report it closes** (F079 criterion 3's rule), attributed and reversible as today.
12. **Tapping a row opens the subject with its full history**: every report, assessment, rebuttal and decision, newest first, with Undo on any decision (today's reversal, unchanged).
13. **Thumbnails for severities 1–3 are blurred until pressed and held.** Severity 4 shows plain.
14. **On desktop: A approves, R removes, J/K move, U undoes.**
15. **A batch of 50 waiting rows is clearable in under 10 minutes on a phone**, measured in a browser test at 375 px with seeded rows.

## Not this

Multi-select bulk actions (F079, still unscheduled; swipe triage covers the batch). Member-facing appeal boards. Assigning rows to more than one operator. Per-category hide bars.

## Why

**The PM, 2026-10-05:** *"I want a clean page of 'Posts' for all flagged and reviewed content. I need something quickly and easily scannable and possible sortable by how serious the allegation is."* And: *"easy to review and pass or fail with either a swipe or a big button for approve. I want minimal steps for approve or deny, e.g. minimal clicking."* **The operating constraint** sets the bar: a week's reports land on a Friday-to-Monday batch, so the page is built to be cleared, not browsed (criterion 15).

**Path: well-worn** for the list, swipe and undo; **new territory** only where it amends a ruling (below).

### The severity scale (Cowork's call under the decision rule; the PM may change it as data)

| Tier | Name | F078 / F080 categories |
|---|---|---|
| 1 | Child safety or illegal | children (any image of a child, F080), anything illegal |
| 2 | Threats and harassment | threat of harm, violence, harassment |
| 3 | Sensitive or adult | nudity; sensitive content other than children (animals and pets, anyone who can't fend for themselves) |
| 4 | Spam and other | spam, other |

An ordinary picture of a child is tier 1 because F078 already treats it at the top: it hides at any bar and texts the PM. The mapping is a constant in code, so a change is an edit, not a migration.

### Action words: Approve and Remove

**Reddit's mod queue uses exactly these two verbs** for "this stays up" and "this comes down" ([updates to mod queue](https://www.reddit.com/r/modnews/comments/yxztfa/updates_to_mod_queue/)). They match the PM's own word ("a big button for approve"), and both name what happens to the Post, not to the report. Today's buttons read Approve and Reject; Reject leaves unclear whether the Post or the report is rejected.

### Precedent

- **Reddit mod queue:** Approve / Remove on each queued item, with a removal reason ([updates to mod queue](https://www.reddit.com/r/modnews/comments/yxztfa/updates_to_mod_queue/)).
- **Gmail:** swipe actions on list rows ([how to change swipe actions](https://9to5google.com/2022/04/06/how-to-change-gmail-swipe-actions-on-android/)) and a five-second Undo by default ([undo send](https://blog.google/products/gmail/how-to-unsend-email-gmail/)). Swipe-plus-undo, not confirm, comes from here; right-for-keep follows the swipe-right-is-yes convention of card triage apps.
- **Meta:** review queues ordered by severity ([how Meta prioritizes content for review](https://transparency.meta.com/policies/improving/prioritizing-content-review/)). **Blurring an image until the reviewer chooses to look** cut exposure without slowing reviewers or hurting accuracy ([HCOMP 2020 study](https://ojs.aaai.org/index.php/HCOMP/article/view/7461)). Criterion 13 comes from that.

### What changes against today (read in `socialus-web` main, 2026-10-05)

- **Today's queue** (`src/app/admin/reports/page.tsx`, `src/lib/admin/reports-queue.ts`) lists **one card per report**, Page photos only, undecided first then oldest hidden, 50 at most. The new page lists **one row per subject**, ordered by severity.
- **Today a decision takes two taps:** Approve or Reject opens a list of preset reasons, then a reason is picked (`ReportEntry.tsx`). Criterion 10's default reason makes it one. **This amends the 2026-09-17 ruling** ("two buttons, both always present", each opening preset reasons); the two buttons stay, the reason picker moves to the detail. Newer ruling wins.
- **Today there is deliberately no undo window** (`ReportEntry.tsx` header: permanent reversibility instead). Both now exist: the toast for the slip, reversal from the detail for later.
- **Today's photo is blurred until a tap.** Criterion 13 keeps that for tiers 1–3 and drops it for spam.
- **Reason codes** (`src/lib/admin/reason-codes.ts`) need remove codes that match the F078 categories (harassment, threat, sensitive content, spam); a schema CHECK change on `report_decisions.reason_code`.

### Size

[platform none]

**About 2.5 build days, in the beta (2026-10-30)**, after F078: the per-subject query, severity and sort (half a day); rows, buttons, swipe, toast and auto-advance (1.5 days); detail, reason codes and the 50-row timing test (half a day).

**Scope signal:** F100, F101 and F102 together are about 8 build days, the sixth launch addition since 2026-10-01 with nothing removed, with feature freeze on 2026-10-23. **Recommend pushing to after beta, in this order:** the Badges & values section; add-to-calendar and end time on dated Posts (F072 criterion 6); repeating series (F074). Or hold F100's harness runner and live-mode gate to after beta (saves about 1 day), since they gate production, not beta.
