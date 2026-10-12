---
id: F074
title: A series repeats
status: approved
horizon: now
rank: 130
date: 2026-09-13
depends: [F072]
approved: 2026-09-20 — Don ruled B, simple repeat; Bulletins leaves the launch list to pay for it.
---
## Story

The run club meets every Thursday from the Sloppy Moose. Sam sets it up once — Thursdays, starting now, no end — and every Thursday for the next three months exists as its own occurrence, each separately editable, because the route changes every week. Harlow's summer patio series is the same feature with both bounds filled in: Saturdays, June to September. In February, Thursdays keep appearing without anyone doing anything. Rae, browsing *this week*, sees the run club once.

## Acceptance

1. A series is created once as **weekly on one or more chosen weekdays, with an optional start date and an optional end date**. The creator never enters individual dates, and no other pattern is offered.
2. Every occurrence is a real `page_posts` row referencing its parent post — never a date computed at read time.
3. **Occurrences exist from today to three months ahead, at all times.** Checked on any day, the furthest is no less than three months out.
4. The job that maintains that window is idempotent: running it twice in succession creates nothing the first run did not.
5. **An occurrence's start is computed in the metro's timezone, not by adding a fixed number of hours.** A weekly series spanning a daylight-saving change keeps its local time on both sides of it.
6. **A time-windowed read returns one row per series** — its soonest occurrence inside that window — and one row per non-recurring post. A week window containing seven occurrences of one series returns one.
7. Editing one occurrence changes that occurrence and no other.
8. Each occurrence behaves as its own dated post under F072: its own address, its own time-window match, its own responses.

## Not this

**Exceptions as rules.** A skipped week is an **edit to an occurrence row**, never a rule expressed against the series — that is the line between this and full recurrence, and it is stated as a line rather than left as an omission, because everything expensive about A arrives the moment a rule can describe its own exception. Also: any pattern but weekly — no monthly, no nth-weekday, no interval. Editing a whole series at once. Cancellation, which is F075. Unbounded horizons. Replacing an occurrence's row instead of editing it — **edits are in place** *(ruled 2026-09-13)*, which is what keeps its responses attached.

## Why

**Don ruled B on 2026-09-20**, against A (full rules) and C (manual reposting). **A is out on a reason, not a size:** exceptions-as-rules means a rule engine and a rule editor, and `model.md` already ratifies that every occurrence is individually editable *because every week differs anyway* — so the expensive half buys something the design does not want. **C is out because it is not the cheap option it looks like:** it builds nothing and produces an empty time lens, which is worse than not naming the set.

**The stakes, restated because they are the reason this is in at all.** Every example Don has given for *What's happening…* is recurring — happy hour, trivia, the market, a brewery's regular music slot. **One-offs are the rarest kind of dated content in a local discovery app**, so a time lens fed only by them returns an empty row most afternoons. **Cutting recurrence would not shrink the theme; it would hollow it out** — F091 criterion 3 hides empty rows, so the named set would silently not appear.

**Criterion 5 is first, and it is the one thing here with no substrate.** There is **no timezone column anywhere in the schema** — verified across every migration. F072 already owes a zone for *reading* a window; expansion needs the same missing column for *writing* one, and adding 168 hours of UTC to *every Thursday at seven* drifts an hour across a daylight-saving boundary. **Daylight saving ends 2026-11-01, two days after launch**, so the first month of this feature crosses it. The zone is a property of the metro, not of a Page, a post or a reader — F059 criterion 7 has members switching metros, so the reader is routinely not in the metro they are reading.

**Criterion 6 ships with this or this does not ship** *(Don, 2026-09-20)*. `browse_feed` has **no `distinct` and no grouping by parent** — verified in the merged migration — so a daily series returns seven rows in a week window and floods the lens. **A flooded lens reads as broken, not as incomplete.** It is written here rather than only in F091 because the flood is created by this scenario: the read-side rule (F091 criterion 6) and the write-side expansion must land in the same release, or the release is a regression.

**What is already true, checked rather than assumed.** `page_posts.parent_post_id` **exists**, nullable and indexed, added in `20260916003100_page_post_write.sql` against exactly this future. `starts_at` is `timestamptz` and indexed. **Given criterion 6, `browse_feed` needs a de-duplication rule** — its window parameters are already `timestamptz` compared with `>=`/`<`, never truncated to a day. **It also needs a caller, which it has never had**: only its own test imports `getBrowseFeed`, and Explore still reads the old Item-grain view client-side. **The old Item path's RRULE columns are not a head start and are a live defect.** `item_gatherings.recurrence_rule` and `location_recurring_temporary.recurrence_rule` are **both in production**, RRULE text with **no zone beside either**, and nothing reads them. *(The second table is `location_recurring_temporary`, not `location_events` — that is the partitioned event log and carries no rule.)* **So the daylight-saving defect is already shipped rather than being designed around**, in two tables, which is why fixing them belongs in the timezone ticket's scope: someone is already looking at exactly this question, and the alternative is finding it on 2026-11-01.

**The stack is three deep and F072 is still `draft`.** F072 (a Page owner posts, with a date, a time and an address) → this.

## Rulings
- **2026-09-20 — A repeating thing repeats, simply: weekly on chosen weekdays with optional start and end dates, expanded into real rows.** Don's ruling (*"sure, let's get building"*), closing the open question raised 2026-09-19. **Resolves and removes** *"Does a repeating thing repeat, and how simply?"* from § Open. **A is rejected on a reason, not a size:** exceptions-as-rules needs a rule engine and a rule editor, and `model.md` already ratifies that every occurrence is individually editable *because every week differs anyway* — the expensive half buys what the design does not want. **C is rejected because it is not cheap:** it builds nothing and produces an empty time lens, which is worse than not naming the set. **Three things ride on the ruling and are conditions of it, not follow-ups:** (1) **the metro timezone column lands before anything expands occurrences** — there is no timezone column anywhere in the schema, and adding a fixed number of hours to a weekly series drifts an hour across a daylight-saving change, which **ends 2026-11-01, two days after launch**; (2) **de-duplication ships with the expansion or the expansion does not ship** — `browse_feed` has no `distinct`, so one daily series returns seven rows in a week window, and *a flooded lens reads as broken, not as incomplete*; (3) **exceptions stay edits to an occurrence row, never rules** — that is the line that keeps B from becoming A, and it is written into F074 § Not this as a line rather than left as an omission. F074 approved the same day.
- **2026-09-10 — A recurring series generates its occurrences as real rows, on a rolling three-month horizon topped up nightly; cancelling an occurrence is a state on the row, never a deletion.** Rows rather than read-time computation because each occurrence is individually editable — the run club runs a different route every week. The top-up job is idempotent: it inserts only what is missing, so a deleted occurrence would simply reappear the next night. Editing one occurrence ships for launch; editing a series does not.
- **2026-09-10 — The occurrence-generating job is a scheduled function in the app, in TypeScript, under review and covered by tests — not a database job.** The general rule it sets: put logic where it can be tested and reviewed, put constraints where they cannot be bypassed. Generating occurrences is logic; cancellation state is a constraint.
