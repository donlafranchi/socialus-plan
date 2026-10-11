> **Generated** by `scripts/criteria.py --capabilities` from the feature reports in socialus-web, 2026-10-10. Never hand-edited.

# What the app can and cannot do

Generated from the per-criterion feature reports (`scripts/criteria.py --capabilities`). Never hand-edited. Built means the code is on main; it says nothing about review or smoke.

## F060 someone starts something without opening a shop (create-posts): 4 of 5

- Can: A Member with no Page can create a hosted gathering: no business record, no document/ID/ZIP check; F082 agreement is the only thing before publish
- Can: First question is what they're starting; no self-classification anywhere
- Can: No legal/tax language or legal-entity questions at Page creation
- Can: Second Page is one tap from the end of the first; first unchanged
- Cannot yet: /you/sell redirects to /you/create preserving the query string

## F061 creating a Page asks one question, its kind (create-posts): 3 of 3

- Can: Create asks one question, the kind, each a question with a one-line purpose; the screen says this just starts the process
- Can: Creation lands the owner on the draft Page; name, address, neighbourhood, tags are set there
- Can: Map/card placement from a single read-time resolver; nothing precomputed or cached

## F064 someone asks for something that isn't built (create-posts): 0 of 5

- Cannot yet: One signal table, two sources (unmapped label, Other description), each row says which
- Cannot yet: Tap on a not-built option is acknowledged; second tap by the same person is a no-op via a constraint
- Cannot yet: No copy in this flow implies a date, plan or queue position
- Cannot yet: The person who signaled sees no count
- Cannot yet: Operator can group the raw table by subject, ranked list, no screen

## F072 a Page owner announces something, with a time on it (create-posts): 4 of 6

- Can: Only the managing role announces or edits; edit in place; deleting refused
- Can: Optional date/time and own address; windowed read to the hour; undated never windowed; metro time
- Can: One audience switch, default anyone; words name people; no "announcement"/"bulletin" in a label; count in words at zero
- Can: A failed save leaves nothing behind
- Cannot yet: Appears on Page and in browse as the Page's voice (no price, buy, listing chrome); past start drops out; undated leaves after 14 days to "Earlier", optional sho
- Cannot yet: Optional end time after start; add-to-calendar; default alt text from title, date, place; label "Event"

## F074 a series repeats (create-posts): 0 of 8

- Cannot yet: Series made once: weekly, chosen weekdays, optional start and end; no other pattern
- Cannot yet: Every occurrence is a real page_posts row with parent_post_id; never computed at read
- Cannot yet: Occurrences from today to three months ahead, at all times
- Cannot yet: The window job is idempotent
- Cannot yet: Start computed in the metro's timezone; keeps local time across daylight saving
- Cannot yet: Windowed read: one row per series, one per non-recurring post
- Cannot yet: Editing one occurrence changes only that one
- Cannot yet: Each occurrence is its own dated post under F072 (address, window match, responses)

## F082 the rules a member agrees to before publishing a Page (create-posts): 7 of 9

- Can: Becoming a creator = agreeing before each new Page; no role column
- Can: Fixed statements, agreeing is the attestation; no upload, ID or check
- Can: Gates publishing, not drafting; selling and hosting alike
- Can: No "are you a business", legal or tax wording
- Can: Versioned; each agreement recorded; only the PM and operators see it
- Can: Publishing needs name, location, description, agreement, one tag; photo optional
- Can: One rule is "no pictures of children", verbatim
- Cannot yet: Nothing attested shows as a badge or label
- Cannot yet: Rules one click away, even if not publishing (launch-blocking)

## F099 every post shows a picture, and every Page can have a Page picture (create-posts): 12 of 13

- Can: Every Page, any kind, may set one optional Page picture; same flow and copy
- Can: No Page picture shows the kind's placeholder, same for everyone
- Can: A post may carry one photo; a second is refused
- Can: A post's photo belongs to that post, never becomes the Page's photo
- Can: Existing upload path: WebP, stripped, own folder, 5 MB, bytes verified
- Can: Every post card shows exactly one image: post photo, else Page picture, else placeholder
- Can: Visible = not hidden, not removed, resolved in SQL; URL never reaches the browser
- Can: Each image reportable on its own; hides that one image; notice names which
- Can: Adding either image shows the sensitive-content ask at upload
- Can: Every image has alt text: Page name, or the owner's words, else default
- Can: Removing either image records an event; gone on next load
- Can: Current Page photo stays; Page picture starts empty
- Cannot yet: Signed out: no post photo in any response; Page picture/placeholder where the name shows

## F044 newcomer switches between list and map with an inline toggle (explore-map): 2 of 5

- Can: Tap Map: same result set as pins, toggle shows map active
- Can: Tap List: back to the card list, toggle updates
- Cannot yet: No fixed full-width List/Map bar; a compact inline [List] · [Map] in the results
- Cannot yet: Toggle scrolls with content, never fixed or floating, never occludes a card
- Cannot yet: Toggle sits after the first 3-5 cards, centred, 24px above and below

## F045 a newcomer filters Explore with a filter icon, kind pills and a bottom sheet (explore-map): 2 of 9

- Can: No separate market/category/day buttons; filter icon at the right of the sticky search bar
- Can: A dot on the filter icon when secondary filters are active
- Cannot yet: Kind pills (All, Events, ... Asks) fixed above the bottom nav, All default
- Cannot yet: Tapping the icon opens a sheet: distance 1/5/10/25, schedule any/week/weekend/recurring, category multi-select, sort; Show results; Clear all when set
- Cannot yet: Tapping the Events pill filters instantly to gatherings; pill selected state
- Cannot yet: Active secondary filters show as removable chips below the search bar; no chip for kind
- Cannot yet: Chip row disappears when no chips remain
- Cannot yet: URL carries all active filters (kind + secondary); the URL restores them
- Cannot yet: Back from an Item page restores filters and scroll

## F046 scrolling hides the bottom nav (explore-map): 6 of 7

- Can: Scroll down more than 20px: nav slides out, ~200ms ease-out
- Can: Scroll up more than 20px: nav returns
- Can: At scrollTop <= 0 the nav is visible
- Can: Nav visible on first render of any tab
- Can: No layout shift or scroll jump when it shows or hides
- Can: Same behavior on Home, Explore, You
- Cannot yet: Visual spec: 44px, 9px/500 labels 3px below icon, 20px/1.5 icons filled when active, charcoal active, #717171 inactive, 1px #EBEBEB border, opaque white

## F059 Browse, where a newcomer finds the neighbourhood (explore-map): 9 of 12

- Can: Browse is its own surface at /explore, own tab; not merged with Home
- Can: Signed in, also own announcements and things coming up; signed out, absent
- Can: Signed-in half withheld server-side, never rendered and hidden
- Can: Order is locality and recency; never payment, size, follower count or what keeps you scrolling
- Can: List and map by width; Map pill under 1024; side by side from 1024; owner-panel switch at 1280-1439; signed out is list only
- Can: Metro switcher moves a signed-in member's results too
- Can: Past-dated posts drop out on their own
- Can: Each result carries the name its people are known by; a concealing brand label fails
- Can: Shared link reopens same metro and search; back restores scroll
- Cannot yet: Pages and posts together, complete, nothing withheld that the reader may see
- Cannot yet: Curated lenses (today, local food, household, art, free); no kind picker; search separate
- Cannot yet: Scoped to the active metro; a member outside every seeded metro chooses, none is picked for them

## F063 someone says they're coming (explore-map): 0 of 4

- Cannot yet: Tap writes a response row and its event row in one transaction; count updates
- Cannot yet: Tap again withdraws, no dialog; double-tap is a no-op enforced by a database constraint
- Cannot yet: A signed-out tap survives sign-in and is recorded on return
- Cannot yet: Count is distinct people, never rows

## F070 every Page has a face, even without a photo (explore-map): 3 of 5

- Can: The photo step is optional; composer completes without one
- Can: Stored bytes carry no metadata, GPS included, verified against the file
- Can: A raw upload that bypasses the client is rejected by the storage API
- Cannot yet: No photo shows the kind's default art, identical for every viewer; missing Page picture falls back to it
- Cannot yet: Operator removes a Page's photo in one action; object deleted, event recorded

## F076 a person outside an open metro joins its waitlist (explore-map): 12 of 16

- Can: Every US metro is in the list at signup
- Can: Zip may suggest a metro; never IP, default or nearest-match selection
- Can: Role is on the waitlist entry, none pre-selected, no role on the member
- Can: Changing metro moves the count, no double count or strand
- Can: Creator and patron counts stored separately, readable apart
- Can: Message says what is needed, never a date or a promise
- Can: Eligible only at 50 creators and 250 patrons
- Can: Thresholds per metro, no migration or deploy
- Can: Opening a metro is deliberate; crossing the threshold never opens it
- Can: Leave an email, no account, no password, no name
- Can: Identical response for a new and a known address, same number
- Can: Metros are ordered by the cached waiting count
- Cannot yet: One person counts once in one metro, signed up or email only (launch-blocking)
- Cannot yet: A popup shows a count for everyone, from the cache (launch-blocking)
- Cannot yet: One combined number against 300; same figure as the picker's ordering (launch-blocking)
- Cannot yet: An address is used only to say the metro opened, then discarded

## F091 What's happening, today and this week (explore-map): 5 of 7

- Can: A row returns only posts starting in its window, soonest first
- Can: Windows in the metro's timezone, bound to the hour
- Can: A row with no results is absent
- Can: The stem is absent when every row is
- Can: Signed out, the today row is one "Sign in to see what's happening" card per Page posting today
- Cannot yet: The same link reopens the same rows
- Cannot yet: A series appears at most once in a row

## F092 narrowing happens in a modal that writes what it did (explore-map): 1 of 6

- Can: Only the panel-opening control on the results surface; no chips or pills
- Cannot yet: Apply closes the panel and writes the selection into the box as readable, retypable text
- Cannot yet: Results match the box text, panel-written or typed
- Cannot yet: Every string the panel can write is understood by the box reader
- Cannot yet: Text not understood opens the panel; never errors, never silently empties
- Cannot yet: Clearing the box clears the narrowing

## F093 a signed-out visitor sees that something is happening, and is asked in to read it (explore-map): 9 of 12

- Can: Anonymous PostgREST call returns no body
- Can: Same for starts_at, location_id and later columns
- Can: Withholding is enforced in SQL, a projection not a filter
- Can: One card per Page, count named as a period, no nought
- Can: Signed-out Explore still has post-kind rows, withheld
- Can: Signed-out front door: name, default photo, description, card; no location, tags or founder; indexable
- Can: Any #announcement-<id> link lands on the Page's one card, marked, with CTA
- Can: No link to a body signed out; the ask comes first
- Can: Same card for every anonymous reader
- Cannot yet: Card has exactly five things; no-photo shows the kind's default art (launch-blocking)
- Cannot yet: A signed-in member sees no change (launch-blocking)
- Cannot yet: Every criterion has a check seen failing

## F058 a member reports something, and the operator can take a photo down (moderation): 4 of 6

- Can: A signed-in member sends a free-text report from an item or shop page
- Can: Only the operator sees or can invoke Remove; others rejected by the handler
- Can: The report reaches a place a person reads
- Can: Every decision reversible from the item by a new decision; reviewer sees history
- Cannot yet: A report changes nothing visible to anyone, including the reported party (launch-blocking)
- Cannot yet: Removal stops every surface serving the photo, writes who/when/why, listing survives (launch-blocking)

## F078 flagged content hides itself, and the poster is told why (moderation): 8 of 11

- Can: Poster told in-app, never email, with category, reporter's reason and a plain explanation
- Can: Poster submits one explanation; unanswered takedown stays hidden and closes itself
- Can: Threat of harm / children texts Don at once; rest queues in a mobile review view
- Can: Below the bar nothing automatic; lands in the same queue; at launch nothing is below
- Can: Bar is per-metro data, no migration or deploy; starts at 0; unresolvable metro uses 0
- Can: Children / threat-of-harm hide at any bar
- Can: No report without a reporter-chosen reason
- Can: Reporter told before sending: misuse is a strike, three stops hiding
- Cannot yet: Everything a member posts is reportable; a report triggers agent classification (launch-blocking)
- Cannot yet: Hides when score is at or above the metro's bar, by the agent
- Cannot yet: Every string kind and gracious; wording is Don's

## F080 no sensitive content in photos; the uploader confirms, a report hides (moderation): 3 of 5

- Can: Uploader confirms each photo shows no children; nothing pre-screens
- Can: A reported sensitive photo hides at once at any bar and texts the operator
- Can: The app asks not to post sensitive content wherever a member posts, and why; each photo asks for confirmation
- Cannot yet: Text is not in scope; only images are restricted
- Cannot yet: No toggle, setting, tier, request or workaround allows it

## F100 an AI reads every reported item first, and a person makes the call (moderation): 8 of 12

- Can: Every report and every poster rebuttal triggers one read, after the report is stored; the report never waits
- Can: Haiku with text and vision, structured: category, severity 1–4, confidence, outcome, reason ≤ 140
- Can: Under 0.70 Sonnet gives a second opinion; both stored, second shown
- Can: Send only content, reporter's reason, rebuttal; no name, handle or email; rules versioned
- Can: Each assessment stores model, prompt version, category, severity, confidence, outcome, reason, latency, time; RLS on, no policies
- Can: Shadow mode: an assessment changes nothing (but F102's severity-4 auto-restore)
- Can: A person's decision is logged against the AI suggestion
- Can: Live mode is a data switch; live raises severity and order; remove, restore, strikes stay a person's
- Cannot yet: Harness prints recall, false alarms, severity accuracy, latency, cost; runs on every prompt change (launch-blocking)
- Cannot yet: Builder-built labelled set; licensed photos, licence per photo; children and adult cases handled safely (launch-blocking)
- Cannot yet: Live needs ≥ 95% recall, 100% severity-1, < 10% false alarms, plus two weeks of shadow the PM read
- Cannot yet: Suspected severity-1 never sent to a provider; images hash-checked; row goes to a person with the result (launch-blocking)

## F101 one scannable page of flagged and reviewed Posts, decided in one tap (moderation): 12 of 15

- Can: Operator-only Posts page, one row per subject (Post with its photos, Page photo, Page picture); non-operators 404
- Can: Severity 1–4, highest open tier; shadow = reporter's, live = higher of the two
- Can: Order severity then oldest; sort severity/age/count; filter by status; header counts by severity
- Can: Approve/Remove full-width, 48 px+, bottom half of row; Approve restores, Remove keeps down
- Can: Swipe right approves, left removes, colour and word revealed
- Can: One tap or swipe per decision; severity-1 Approve asks once more
- Can: No confirm dialog; 5-second Undo; undone writes no decision and tells nobody
- Can: Next waiting row moves into place after each decision
- Can: One-tap default reason: Approve "Nothing wrong with it"; Remove matches top category; changeable in detail
- Can: A decision writes one report_decisions row per open report, attributed, reversible
- Can: Desktop keys: A approves, R removes, J/K move, U undoes
- Can: 50 rows clearable in under 10 minutes on a phone, browser test at 375 px
- Cannot yet: Row shows thumbnail, 120-char excerpt, badge, reasons+count, AI read, rebuttal, reporter counters + coordinated flag, status, age
- Cannot yet: Tap row: full history, every report, assessment, rebuttal, decision, newest first, Undo on any decision (launch-blocking)
- Cannot yet: Severity 1–3 thumbnails blurred until pressed and held; severity 4 plain (launch-blocking)

## F102 the poster answers first, report misuse is tracked, and the platform holds steady Tuesday  (moderation): 9 of 14

- Can: Poster told category and reporter's reason; gets one answer
- Can: Fix and repost shows again at once; reports stay; no second repost; not for severity 1
- Can: Say it's wrong: Mistaken/Malicious/Misusing + 280-char note; one per hide; to AI and row; stays hidden
- Can: Per-reporter counters (filed, upheld, dismissed, open), operator-only, used by nothing else
- Can: Cap 5, drops to 1 after any dismissal in 30 days
- Can: 3+ reports on a poster in 24h, 2 from accounts under 7 days: flag, +1 tier in severity
- Can: Tue-Thu with no person: sev 2-4 wait; sev 1 stays hidden and texts the PM
- Can: Threat-of-harm report sheet says call 911 if in danger now
- Can: Severity 4 auto-restore, narrow gate, logged, reversible, "Restored by AI"
- Cannot yet: Unanswered hide stays hidden, closes at 14 days; batch shows it only if severity 1 (launch-blocking)
- Cannot yet: Two dismissals in 30 days start a 14-day cool-down; stored and queued, hide nothing; three strikes above
- Cannot yet: One Friday summary: waiting by severity, answers, cool-downs (launch-blocking)
- Cannot yet: IP and time recorded on every upload and post; operator-only; 1 year then deleted (launch-blocking)
- Cannot yet: Child-safety is a legal tier: never restores, never to poster, no AI, preserved and reported to NCMEC (launch-blocking)

## F056 a producer edits a shop that already exists (page-editing): 5 of 9

- Can: invariant
- Can: behavior
- Can: invariant
- Can: behavior
- Can: invariant
- Cannot yet: behavior
- Cannot yet: invariant
- Cannot yet: behavior
- Cannot yet: behavior

## F069 a non-business Page resolves everywhere, and holding several is ordinary (page-editing): 2 of 4

- Can: A non-business Page's URL renders instead of 404ing
- Can: A Member with several Pages sees every one on a producer surface
- Cannot yet: Products, services, gatherings under a non-business Page resolve
- Cannot yet: Draft-resume keeps every in-flight draft

## F057 someone who isn't selling yet finds the way in (sign-in-you): 2 of 5

- Can: /you has no "vendor", "market" or "business owner" and queries none of the dead tables
- Can: /following redirects to /you/following; sign-out and follow list as shipped
- Cannot yet: A Member with no Page sees no shop controls, only their own stuff and one invitation
- Cannot yet: The invitation names specific maker categories, with one worked example
- Cannot yet: A Member with Pages sees a row per Page (Edit shop + create controls) and their listings, reusing the existing query

## F065 someone follows a person, Page or venue, and nothing else changes (sign-in-you): 3 of 5

- Can: Following a person, Page or venue writes one row plus its event row in one transaction
- Can: A follow never grants membership, a role or unlisted read access, checked against every authorization/roster path
- Can: Unfollow then re-follow revives the original row
- Cannot yet: A Member who follows a business and owns no shop still sees Sell offer to start something
- Cannot yet: The following list reads from one table, not three

## F077 members see a display name; the legal name stays with the platform (sign-in-you): 1 of 8

- Can: Legal name never on a public/discovery surface or to anonymous
- Cannot yet: Signup requires a legal name; no account without it
- Cannot yet: Display name shown wherever a peer would see the legal name
- Cannot yet: Operator report view shows legal name beside display name
- Cannot yet: Seeded/test members backfilled or flagged
- Cannot yet: Counterparties each see the other's legal name, per interaction
- Cannot yet: Name legible 12 months from the interaction, then display name
- Cannot yet: Interaction is the only path to a name: no search, lookup, roster, export

## F081 everyone signs up the same way, and the zip sets the metro (sign-in-you): 5 of 9

- Can: Four fields, 18+/Terms box, email verified
- Can: The zip sets the metro and the screen says which
- Can: A "what this app is for" line; no "never sell" line
- Can: No maker/finder question
- Can: No home place assigned for the person
- Cannot yet: Zip never shown to others (invariant: absence of code proves nothing)
- Cannot yet: Nobody picks a metro; changing the zip on /you moves it (launch-blocking)
- Cannot yet: Every US zip resolves; unknown refused (launch-blocking)
- Cannot yet: Phone verification refuses VoIP

