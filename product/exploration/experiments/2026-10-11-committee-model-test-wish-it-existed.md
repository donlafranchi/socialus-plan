---
id: exp-2026-10-11-committee-model-test-wish-it-existed
title: "Wish it existed — requests with backers (committee model-test, PLAN ONLY)"
status: awaiting-approval
experiment: feature-intake council run with lower-level agents on Sonnet (chair on Opus 4.8)
size: null          # PM sets S, M or L
path: new territory
date: 2026-10-11
run_by: committee skill (plan-feature), chair Opus 4.8, nine roles on Sonnet
criteria_ref: see §6
---

# Feature Brief: "Wish it existed" — requests for things that don't exist yet, with people who can make them (and, later, back them)

> **Experiment note.** This brief was produced by the `plan-feature` committee with the nine council
> roles run on **Claude Sonnet** (the chair/merge on **Opus 4.8**), to test the committee at a lower
> model tier. It is written PLAN ONLY — no scenario, Issue, branch or code. Structure is
> **Area → Feature → Journey → Criterion** per the repo's one-structure convention. Models-per-role and
> timings are in §10.

**Goal:** A member can *get something made that doesn't exist yet* when they want it and can't find it
locally — the platform connects the one who wants it, someone who can make it, and (later) others who
help fund it, and supplies enough structure that the parties aren't left to figure it out alone.

**Date / run by / PM context:** 2026-10-11 · committee (roles on Sonnet, chair Opus 4.8) · Sacramento
open beta 2026-11-06, feature freeze ~2026-10-30, payments **cut** from beta, one operator away Tue–Thu.

**Scope line:** If the beta slice enters, nothing is removed — it rides approved F064 + existing nouns.
Everything involving money, backing, or a platform-authored agreement is **After beta** and **blocked on
socialus-legal**.

---

## 1. Facts (Stage 0)

| Fact | Verified / assumed | Source |
|---|---|---|
| Payments are cut from beta; no checkout exists | verified | ROADMAP § Cut; DECISIONS 2026-10-07 |
| "Money back, or a share" backing is a **securities** question → socialus-legal, never a PM decision, no detail designed here | verified | DECISIONS 2026-10-07 + header; repeated in IMAGINE/DECISIONS |
| **F064 "someone asks for something that isn't built" is approved** — one signal table, a tap acknowledged once, **no count, no date/plan/queue, no reply**; second tap a no-op via constraint; operator groups the raw table by subject (no screen). "Not this": a leaderboard / "most requested" surface, any admin UI, replying | verified | planning/scenario-F064.md |
| **Idea** noun (schema `wonder`): "someone puts a new thing to the neighbourhood and others signal interest before it exists"; never converts to another entry type; author makes the Page themselves and links it | verified | nouns.md |
| **Volunteering** noun (schema `offer`/`ask`): offering / asking for help; composer "tractable inside a group the moment the board ships; **blocked across the neighbourhood**" | verified | surfaces.md, nouns.md |
| Verbs a person already does include **make, sell, host, offer, ask, wonder, show up, back, follow, save** ("back" exists as a word) | verified | nouns.md |
| Item kinds: Product, Service, Gathering, **Idea, Offer, Ask**, Initiative (`items.kind`); /explore indexes Items | verified | nouns.md, surfaces.md |
| No person-noun shown to a member (member is "you"); no ratings / reputation / tiers for people | verified | nouns.md, ROADMAP § Won't |
| Won't: legal/tax language **between members** or in Page creation; legal-entity info from anyone without a legal entity; platform-custodied funds held for the platform's benefit, lending, credit; business-entity modeling; full e-commerce — **but** "basic in-platform versions, so people can transact and connect, are possible" | verified | ROADMAP § Won't; PM 2026-09-30 |
| IMAGINE, not built: "Community funds a seller designates"; the cooperative engine (pooled-commitment purchasing, co-op templates); "Reciprocity & goodwill" on Offer/Ask. Standing decision against speculative cooperative tooling until documented member demand | verified | IMAGINE.md |
| Seed starter requests are labelled **Sample**; sample/builder content never counts in real numbers and is one-tap hideable | verified | PM test setup; DECISIONS 2026-10-05 builder content |
| No contract/agreement noun, no backer noun/edge, no escrow, no fulfilment/commitment state, no cross-member reply surface across the neighbourhood | assumed | Architect + Developer (no repo write-path found this run) |

---

## 2. Prerequisites (no noun, verb or surface yet — listed first, never a task inside the feature)

| Missing | Why it's a prerequisite | Owner | Needed by |
|---|---|---|---|
| **A cross-member reply path across the neighbourhood** | Today a wanter and a would-be maker can only connect inside a group; "I can build that" from a lone neighbour has nowhere to land | Developer (design) | Feature B (beta slice) |
| **Maker-raises-hand edge** (maker → wish) | `offer` models *help*, not *I'll make this deliverable*; closest reuse, but a new edge | Architect | Feature B |
| **Backer noun + many-to-one "I'll support this" edge** | `back` is a verb-word only; no noun, no edge, no state | Architect | Feature C (post-beta) |
| **Agreement noun + state + versioned template store** | No contract noun, no proposed/accepted/fulfilled/lapsed state | Architect | Feature D (post-beta) — **and blocked on legal, see §5** |
| **Securities clearance** for any money-back / share backing | Settled: goes to socialus-legal, no PM detail | socialus-legal | Feature C/E |
| **UPL / legal clearance** for a platform-authored agreement | A "standard agreement between members" is adjacent to "no legal/tax language between members" and to unauthorized practice of law | socialus-legal + Don | Feature D |

---

## 3. Roles (committee, roles on Sonnet)

| Role | Needs | Cost | Veto | Risk |
|---|---|---|---|---|
| **Person** | Say the wish in a sentence + photo, like wondering; see it's out there; know a real neighbour noticed; one clear place to read "I can build that" and say yes/no | One short composer; a reply understood in seconds | Any step where they wait with no sign anything happened; a feed to scroll for their own wish; any guess about who owes what or whether money is safe; any legal-sounding terms; any "most requested" board | **Silence.** Post a wish, nobody answers, F064 forbids a count/reply → feels like shouting into a void; a first dead wish kills the second |
| **Maker** | Two fields max: "I can build that" line + price-or-collaborate choice; everything else rides `wonder`/`offer` + their own Page; a plain "what we agreed" summary so they don't draft terms | ~2 min to respond; delivery/follow-up stays off-platform in beta (payments cut) | More than two fields; **paid reach** (boosted/promoted replies, pay-for-placement) | Builders quote real effort, nothing funds it (no count, no checkout) → they learn replying is wasted and stop; supply dies |
| **Money** | SocialUs earns **only** standard transaction income on a real sale, later; beta = signal + connect only, nothing held; a voluntary non-return "support" is commerce (fee later); any return/share → legal | Beta: zero build, zero revenue; later: payments, disputes, refunds, legal | Visibility sold; a cut that grows with dependence; platform-held funds for platform benefit | "Backers who fund an idea" drifts into investment-style backing — pooled/held/promised-return = securities + custody problem; the template wording could create it |
| **Architect** | Reuse F064 signal + `wonder` for the wish; **new**: maker→wish edge (prefer an edge over a new kind), backer edge+table, agreement noun+state+template store; surfaces: wish detail (maker + backer sections), agreement view/accept, operator raw-table view; events: maker-claimed, backer-joined, agreement-accepted, done; notifications per party | ~4 new tables + state logic + ~3 surfaces + notifications = **not beta-sized** by 11-06. Cheapest cut: wonder + maker edge only, no money/agreement/backers | Anything needing a **second source of truth**; agreement state living outside the wish; a backing ledger parallel to payments | The agreement/commitment state quietly makes SocialUs the record-keeper and dispute party, with enforcement duties it has no model for |
| **Developer** | Ordered slices (estimates): (1) schema+RLS migration 6h [not shippable alone]; (2) wanter wish page + "I can build that", reuses `items.kind=Idea`, indexed in /explore, 14h [**first shippable slice**]; (3) non-monetary backing pledge 6h [shippable only if legal clears wording, else post-beta]; (4) static versioned agreement template + click-to-accept 8h [needs slice 2; content waits on legal]; (5) in-thread messaging 12h (post-beta); (6) fulfilment + money-back/share 20h+ [post-beta, legal first] | Slices 1–3 ≈ 26h; feasible before freeze **if started this week** | Slice 1 alone (schema, no UI); any first slice needing messaging or payments | **Ship-order stall**: slice 2 needs a cross-member reply path, which today works only inside a group; if it falls back to group-only the feature is dead for a lone wanter |
| **Tester** | Binary criteria written before build, every zero state (see §5 Zero states and §6) | ~1 new wish noun, maker edge, (later) backer edge + agreement record; ~12 tests across 3 zero states | Any criterion with "feels/clear/reasonable/enough"; any threshold with an undefined number; any payment behaviour in beta | The agreement template reads as a legal/financial promise → breaks "never extractive" unless legal signs off first |
| **Operator** | Signal-only extension of F064: a "want" row grouped Fri–Mon; every maker reply/backer/agreement **async and inert**; no action-needing notifications, no live queue, no stranger messaging, no fulfilment tracking midweek; shadow AI pass for moderation | ~zero infra; real cost is Fri–Mon time (~15 min / 10 offers); one-time template legal review | Any live matching/messaging; any dispute/scam/"where's my item" flow with a days-SLA; any backer money/pledge state; any offer-for-money open to strangers without Fri–Mon pre-approval | **Scams / off-platform solicitation**: a scammer posts Tue, hits a member Wed, nobody acts until Fri. Rare at 10 users, weekly at 100 → extractive harm, breaks the one "never". Mitigation: maker offers hidden until Fri–Mon approval; strip contact details |
| **Guardian** (blocks) | Securities clearance before any backer surface/copy; **no platform-authored legal instrument** between members (legal approves a plain-language non-advisory record, or members use their own terms); no legal/tax language in Page creation; no entity info from the entity-less; no platform-custodied funds; wanter/backer identity private, no profile/ratings/tiers; all new copy draft until Don | The safe subset waits on legal; cannot ship in open beta without it; Don away Tue–Thu | **1.** agreement template as framed breaks "no legal/tax language between members" + UPL → blocked pending legal. **2.** any return/share/"money back" = securities + broken promise → blocked. **3.** platform-held pooled funds → blocked. **4.** maker reputation/rating for trust → blocked. **5.** "generate revenue for members" is an outward promise → blocked until legal clears the mechanism + Don approves copy | Don's aim — protect members from outside lawyers — could lead us to hand members **our** template, putting the platform in the lawyer's seat and exposing the members we meant to protect |
| **Scout** (advisory) | All-or-nothing funding with money held until a first milestone; a scoped request with budget range + deadline (open-ended wants stall); a public "I can build that" with a visible track record; a plain-language checklist (scope, price, date, revisions, what-if-it-fails), not legal advice; a fixed local boundary | Request+offer board with no money = low; pooled payments = escrow/refunds/disputes = medium-high | None | If SocialUs holds backer funds it becomes escrow + dispute party → money-transmitter + consumer-protection exposure + refund burden; authoring the "agreement" edges toward UPL |

**Scout precedents (all recalled unless noted; Scout web-searched this run):** Kickstarter all-or-nothing — *copy* (backers not charged unless goal met); *failed* (delivery never guaranteed, late/never shipments). Patreon commissions / Fiverr / Upwork escrow — *copy* milestone release; *extracts* via 5–20% fees + platform-controlled disputes. Thumbtack — *extracts* (pay-per-lead charges pros with no job). TaskRabbit — *copy* the scoped priced task; *extracts* via service fees. Etsy custom requests — *copy* the "request → quote" flow. Facebook Groups "ISO" — *copy* the low friction; *failed* on trust/scams, no funding. **Local commission precedent: none found** — closest are CSA shares and neighbourhood group-buys, which run on trust with no template. *PR/FAQ lens:* write the member FAQ first, starting with "What if the maker disappears?". *Shape Up appetite:* a 2-week appetite fits a request+offer board; pooled funding is a separate, larger bet.

---

## 4. AREA → FEATURE → JOURNEY → CRITERION

**AREA — Wished-for things** (the request-and-make loop; part of the Items / discovery area). A member names
something that doesn't exist locally; neighbours who can make it step forward; later, neighbours help fund it.

### Feature A — Post a wish *(beta; rides approved F064 + `wonder`)*
- **Journey A1 — "I wish this existed."** A member in the moment ("a frog habitat for my backyard") says it in a sentence + optional photo, like wondering.
  - *Criteria:* §6 #1, #3, #4, #6, #11, #13.
- **Journey A2 — The metro has none yet.** A member opens the wished-for surface in a sample-only or empty metro.
  - *Criteria:* §6 #2, #10 (zero/sample states).

### Feature B — "I can build that" *(beta slice, first shippable; rides `offer` + new maker→wish edge; needs the cross-member reply prerequisite)*
- **Journey B1 — A neighbour offers to make it.** A member sees a wish and raises a hand with a one-line "I can build that" + price-or-collaborate; the offer is **hidden until the operator approves it Fri–Mon**, contact details stripped.
  - *Criteria:* §6 #3, #7, #12, #14, #15, #16.
- **Journey B2 — The wanter decides.** The wanter reads approved offers (arrival/relevance order, never paid order) and says yes/no; a yes just connects the two — no platform money, no platform contract.
  - *Criteria:* §6 #14, #15, #17.

### Feature C — Back a wish *(AFTER BETA; blocked on socialus-legal)*
- **Journey C1 — "I'd support this."** A neighbour adds a **non-monetary pledge of intent** (no money, no return, no share) to a wish.
  - *Criteria:* §6 #4, #8, #9 — **and** Guardian veto 2 cleared (securities wording) before any backer surface exists.

### Feature D — A fair-terms checklist *(AFTER BETA; blocked on Don + socialus-legal — UPL)*
- **Journey D1 — "What did we agree?"** The two parties see a plain-language, non-advisory checklist (scope, price, date, revisions, what-if-it-fails) — **only if** legal approves it as a record, or the parties use their own terms. The platform does **not** draft, recommend, or imply enforceability.
  - *Criteria:* §6 #8, #9, #18.

### Feature E — Funding, escrow & fulfilment *(AFTER BETA; blocked on payments + securities + custody clearance)*
- **Journey E1 — Pooled, all-or-nothing funding held to a milestone; dispute + refund handling.** Not designed here; requires money-transmitter / consumer-protection review. Scout's "right-sized/full" vision lives here.

---

## 5. Zero states (every list defines its zero state — never pad)

| State | What shows | Copy (draft — Don approves) |
|---|---|---|
| Nobody has wished | An invitation to ask; no rows, no counts, no sample filler passed as real | *[draft]* "Nothing's been wished for around here yet. What do you wish existed?" |
| Sample-only metro | Sample wishes render labelled **Sample**; every real count/threshold/"enough interest" check = 0 | *[draft]* badge "Sample" |
| Wish with no maker | No date, plan, queue, progress, or count; an invitation/refine instead (per F064) | *[draft]* "No one's offered yet. Share it with a neighbour who might." |
| Maker offer with no backers | Defined zero state; no backer count, no funding bar, no "0 of N" | *(Feature C, post-beta)* |

---

## 6. Acceptance (binary, written before tickets)

*Beta slice (Features A–B):*
1. A member can post a wish (sentence + optional photo); it is stored as a `wonder`/F064-sourced row carrying its source.
2. In a sample-only or empty metro, every real count, total and threshold reads 0, and Sample rows are labelled "Sample".
3. No copy anywhere in the wish flow implies a date, plan, queue position, or progress.
4. The person who posted a wish sees **no count** of how many others wished or backed.
5. A second identical wish/signal from the same person is a no-op enforced by a DB constraint; no error shown.
6. The wish is acknowledged exactly once; no count is visible to any member on any screen.
7. No leaderboard, "most requested" sort, or admin UI exists (route/query search returns none).
8. **No payment field, amount, escrow, refund, or share-of-proceeds text appears anywhere** in beta; any agreement text contains no money terms.
9. Any agreement/record shown is read-only, identical for all parties, and non-advisory; a party cannot proceed without having viewed it. *(Feature D, post-beta.)*
10. Sample/builder rows are excluded from every real number (verified with mixed data).
11. The wanter can withdraw their wish; after withdrawal nothing of theirs is shown to makers.
12. A maker's "I can build that" offer is **hidden until the operator approves it** (Fri–Mon); unapproved offers are invisible to the wanter.
13. Makers see no wanter identity beyond what the wanter explicitly consented to.
14. The wanter reads approved offers in arrival or relevance order; **no offer is ordered or surfaced by payment** (no boost/promoted reply).
15. A maker needs at most two inputs to offer: an "I can build that" line and a price-or-collaborate choice.
16. A maker offer's text has contact details (phone/email/URL) stripped before it is shown.
17. A wanter's "yes" connects the two parties and creates no platform-held money and no platform-authored contract.

*Post-beta, legal-gated (Features C–E) — criteria recorded, not built:*
18. The fair-terms checklist, if shown, is legal-approved as a plain-language non-advisory record (or absent); the platform neither drafts nor implies enforceability.
19. No backer return, share, or "money back" is offered or implied on any surface until socialus-legal has cleared it.

**Open binary criterion for Don (not yet decidable):** whether an honest, non-extractive "a neighbour noticed" signal can exist **without** a count (reconciling the Person's anti-silence need with F064's no-count rule). See §9-B.

---

## 7. Gates (Stage 3 — not ready until all yes)

- [x] Prerequisites listed, each owned (§2)
- [x] Criteria binary (§6)
- [x] Zero states defined (§5)
- [ ] Copy written to voice rules — **drafts only; Don approves** ([public-is-draft])
- [ ] **Guardian clear or conflict named — CONFLICT NAMED** (five blocks, §3 Guardian; §9)
- [ ] Kill criterion — **proposed, Don confirms the number** (§8)
- [ ] Metric — proposed (§8)
- [x] Work sequenced, each beta slice shippable alone (§3 Developer) — *not Issues; PLAN ONLY*
- [ ] Assumed Stage-0 facts verified as first work item (the cross-member reply path, §2)

---

## 8. Three sizes

| | **Smallest** (beta) | **Right-sized** (post-beta) | **Full** (post-beta) |
|---|---|---|---|
| Ships | Wish board (A) + "I can build that" (B): post a wish, makers raise a hand (operator-approved Fri–Mon, contact stripped), wanter says yes/no → the two connect | + non-monetary backing pledge (C) + a legal-approved plain-language fair-terms checklist (D) + in-thread messaging between accepted parties | + scoped budget/deadline, all-or-nothing pooled funding held to a milestone, disputes/refunds (E) |
| Hours (estimate) | ~26h (slices 1–3 minus money), or ~20h for A+B only | +~20h | +40h+ |
| Existing data only? | Yes (F064 + `wonder` + `offer`) | No (new backer + agreement tables) | No (payments stack) |
| Proves | Does anyone wish for things, and does anyone offer to make them? | Do neighbours commit (non-monetarily) and agree on terms without a lawyer? | Will people fund local making, safely? |
| Leaves out | All money, backers, platform contract | Money/escrow | — |
| Trigger to move up | Real wishes get real maker offers at a steady rate in Sacramento | Legal clears the checklist + securities wording; demand is documented | Payments exist; money-transmitter/consumer-protection review done |

**Kill criterion (proposed — Don confirms):** if, four weeks into the Sacramento beta, fewer than **10 real
(non-Sample) wishes** are posted **and** fewer than **3 maker offers** land, stop and fold the wish into F064.

**Metric (proposed, tied to place-connection-metrics):** count of wishes that receive at least one
operator-approved maker offer per week (a connection made). An offer that leads to an in-person meeting
counts double.

---

## 9. For Don (A/B/C — only what he alone can answer)

**Path: new territory** — this touches money, member trust, securities and UPL exposure. Recommendation first.

**A — Scope for beta (recommended: A1).**
- **A1 (recommended):** Ship the **wish board only** (Features A + B) in beta — no money, no backers, no
  platform contract. Everything else is After beta behind legal. Smallest honest test, rides approved F064.
- **A2:** Also ship the **non-monetary backing pledge** (Feature C) in beta, *only if* legal green-lights the
  wording before the 10-30 freeze. (Money + Guardian warn even non-monetary backing drifts toward securities;
  Developer says it's ~6h if cleared.)
- **A3:** Defer the whole thing until legal clears the agreement + securities questions; ship nothing in beta.

**B — The silence problem (design ruling only you can make).** The Person role's biggest risk is a wish that
goes nowhere, because F064 forbids a count or reply. Do we (B1) keep F064's strict no-count silence, or
(B2) design one honest, non-extractive "a neighbour noticed" acknowledgement that is **not** a count and
**not** a leaderboard? This needs your call before Feature A's copy is final.

**C — The agreement template (to Don + socialus-legal).** Don's aim is to *"generate revenue for our members
and not let outside lawyers take advantage of our members"* via *"a standard template of what the parties
agree to."* Guardian + Scout flag that a **platform-authored** agreement between members is adjacent to the
"no legal/tax language between members" line and to unauthorized practice of law — it could expose the very
members it means to protect. Decision: does SocialUs (C1) commission a legal-approved, plain-language,
non-advisory checklist; (C2) point members to their own terms and stay out of it; or (C3) route the whole
template question to socialus-legal before any design? (Securities questions on money-back/share are already
settled → socialus-legal, no PM detail.)

---

## 10. Experiment self-report (committee model-test)

- **Chair / merge:** Opus 4.8 (this session).
- **Council roles (all on Sonnet):** Person, Maker, Money, Architect, Developer, Tester, Operator, Guardian, Scout — nine agents, dispatched in parallel.
- **Turns:** one parallel dispatch (9 agents), one chair merge. No second round (V0 = Round 1 only).
- **Council wall time:** ~1m45s (first dispatch 19:46:13Z → last role in ~19:48:00Z).
- **Per-agent compute:** 5.8–8.8s each; ~47k tokens each (≈0.42M tokens across the nine); Scout the longest (web search).
- **Where the committee struggled:** (1) convergence was *very* high — all nine independently landed on the
  same legal/securities/UPL gate and the same F064-rides-it beta slice, so the nine roles added confirmation
  more than breadth; a cheaper panel or fewer roles might have reached the same brief. (2) Roles leaned on the
  chair-supplied Stage-0 facts rather than verifying in-repo (by instruction, to stay blind to the other
  session) — so the "assumed" facts in §1 are genuinely unverified and must be checked as the first work item.
  (3) The Person↔F064 "silence vs no-count" tension (§9-B) is the one genuinely unresolved design question the
  panel surfaced but could not settle — it needs Don.
