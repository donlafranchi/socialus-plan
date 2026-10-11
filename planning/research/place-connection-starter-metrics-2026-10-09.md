# Place-connection starter metrics for beta (2026-10-09)

Status: proposal, awaiting PM yes/no. Source idea: the full place-connection metric set (person / place / outcome layers), a Claude project doc not in any repo. Canonical metrics home stays `product/foundation/metrics.md`; if approved, the chosen set moves there and this note becomes the record of why.

## The finding that decides it
- Beta tests posting, not attendance (RSVP cut 2026-10-05). The app records no RSVP, check-in, or host-marked attendance anywhere. Verified in `socialus-web` migrations and `src/`.
- So **showing up** (attended vs RSVP) and **first-timers at events** cannot be measured at beta. Dropped.
- What exists and is written by live code: dated posts (`page_posts.starts_at`, `location_id`), venues (`locations` with geography), metros (`metro_polygons`), signup date (`members.created_at`), follows (`member_follows`), page joins/follows (`group_memberships`), and audit logs (`member_events`, `group_events`).
- Connection at beta therefore means **follow or join**, not meet. That is a proxy, and we say so wherever the number appears.

## Starter set A (recommended, ~12 h, SQL only, no UI)

| Metric | Data (verified) | Formula | Effort | Reading triggers |
|---|---|---|---|---|
| **Gathering density** | `page_posts` (`starts_at` not null, active) → `location_id`, else page `anchor_location_id` → `locations.geography` within `metro_polygons` | Dated gatherings starting in metro per week | 5 h (incl. metro resolver) | Flat or falling 3 weeks → seed more hosts in that area; rising → nothing |
| **Places to gather** | Same join, distinct `location_id` | Distinct venues hosting ≥1 dated gathering in last 30 days | 1 h (reuses resolver) | Few venues carrying most gatherings → recruit venues, not posts |
| **Newcomer connection rate** | `members.created_at`, `member_follows.created_at`, `group_memberships.joined_at` | Of members who joined in week W, % who follow or join ≥1 page or member within 14 days | 3 h | Low → review signup-to-first-follow path; never contacts the person |
| **Unconnected share** | Active `member_follows` (no `unfollowed_at`) + `group_memberships` (no `left_at`) | % of members ≥14 days old with zero active follows and zero memberships | 2 h | Rising → look at what Explore shows new people; aggregate only, no individual trigger at beta |
| Weekly readout | Script prints the four numbers for Sacramento | — | 1 h | PM reads it Mondays |

All four run as service role or a `security definer` function, return metro-level counts only, and never store person-level rows.

## Fallback B (~6 h)
Gathering density + newcomer connection rate. One place number, one people number.

## Dropped for beta, and what unlocks them
- Showing up, first-timers → need F063 "I'm coming" (`socialus-web` #34) plus an organiser-confirmed attendance record (the 2026-09-30 definition). After beta.
- Isolation by attendance → same.
- Attachment pulse and any survey → needs new UI. Later.
- Neighbourhood cuts → Sacramento-only beta will be too small; suppressed below 10.

## Comparison with existing metrics

| Existing | Where | Label | Note |
|---|---|---|---|
| North star: discretionary hours ≥40, adequacy ≥1.5× | `metrics.md` | complements | Outcome layer; not measurable at beta |
| Discovery → relationship (search → follow/save/message) | `metrics.md` | complements | Funnel; ours is place-level |
| Time to a new member's first action | `metrics.md` | **duplicates** | Newcomer connection rate is the concrete version; keep one, under that name |
| Repeat action within 30 days | `metrics.md` | complements | |
| Communities forming vs dormant | `metrics.md` | **duplicates** | Gathering density + places to gather are its place cut; reuse 90-day stale rule |
| Participation across communities | `metrics.md` | complements | Unconnected share is its floor |
| Net retention 30/60/90 | `metrics.md` | complements | |
| Home stop-card reach | `metrics.md` | complements | Home rows cut from beta |
| Session length as a ceiling; anti-metrics list | `metrics.md` | complements | Starter set measures no attention |
| No thresholds until 90 days of usage | `metrics.md` | complements | All triggers above are directional only |
| A view never counts as interaction | `DECISIONS.md` 2026-09-15 | complements | Starter set uses no views; `map_mix_log` excluded |
| Search aggregates: ≥10 distinct members, coarse bands | `DECISIONS.md` 2026-09-15 | complements | Adopt the same ≥10 floor for suppression |
| Completed attendance = organiser-confirmed | `DECISIONS.md` 2026-09-30 | complements | Future showing-up metric must use this definition |
| F063 counts distinct people, no attendee list outside group | `planning/scenario-F063.md` | complements | Enabler for the dropped metrics |
| F064 not-built-yet signal | `planning/scenario-F064.md` | complements | |
| Map mix review vs beta bucket counts | `ROADMAP.md` (#331) | complements | |
| Won't: pull-back notifications | `ROADMAP.md` | **conflicts** | With the full doc's isolation "gentle outward invitation". Not in starter set; needs a ruling before it ever ships |
| Later: producer dashboard, peer benchmarks | `ROADMAP.md` | complements | Watch: peer benchmarks must not become a place ranking |
| Planned PostHog events (`group_joined`, `page_followed`, `item_viewed`…) | `socialus-web` `INFRASTRUCTURE.md` §13 | **replaces** | Audit tables already hold joins/follows; no PostHog needed for this. `item_viewed` must never feed a connection metric |
| Build progress (STATUS, DASHBOARD) | root | n/a | Not product metrics |

Nothing in the starter set contradicts `goals.md`: aggregate only, nothing sold, no person scored, no attention measured.

## How it becomes a system

```
signal captured -> metric computed -> place sees drivers -> intervention -> re-measure
```

| Step | Beta (now) | After beta | Later |
|---|---|---|---|
| Signal | posts, venues, follows, joins (exists) | RSVP + confirmed attendance (F063) | attachment pulse |
| Compute | weekly SQL readout (starter set) | add showing up, first-timers | stored weekly snapshots, trends |
| Place sees drivers | PM only | members-only drivers per metro, ≥10 floor | per-neighbourhood, public or not (PM call) |
| Intervene | PM acts by hand (seed hosts, recruit venues) | playbook per driver | gentle invitation, if ruled compatible |
| Re-measure | next Monday's readout | 4-week trend | outcome layer vs north star |

## Guardrails carried into the tickets
- Metro-level only; any count under 10 is shown as "<10".
- No person-level output, no stored person rows, no individual flags.
- Follows and joins only; no views, no time in app.
- Every threshold is a guess until 90 days of beta data.

## Open questions for the PM
1. Who sets targets once the baseline exists?
2. Where does the attachment pulse live (after beta)?
3. Is the place grade public or members-only?
4. Minimum count before showing a number: proposed 10, matching search aggregates.
5. Do these become the named community metrics the governance model commits to trend? Naming them is a commitment.

## What leaves beta scope to make room
- Proposed: the performance trend dashboard (`socialus-web` #536) moves to after beta. Similar effort, and the readout matters more for judging beta.
