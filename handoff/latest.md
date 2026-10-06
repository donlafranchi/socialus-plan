# Handoff — redesign lane, end of 2026-10-05

The session that ran the redesign lane on 2026-10-05 stops here; a fresh one picks up on 2026-10-06. Overwrite this file at each handoff.

## Blocked first
- **GitHub Actions is stopped by the account's spending limit** ("The job was not started because … your spending limit needs to be increased"). Nothing merges until the PM raises it. #403 (CI diet, another lane) cuts minutes per push.
- **Docker Desktop is off on this machine**, so no local stack, screenshots or persona first passes. UI PRs carry `review-skipped` with that reason; run their first passes when it's back.

## Migration order (the PM applies; one at a time, strictly in order)
1. **363** (`20261004130000_page_purpose.sql`, PR #364): purpose first. Safe to apply before its code ships (old kinds are translated on insert). **Hold until #364's Browser job passes**; it failed on a seed bug fixed in `3c503be` and hasn't rerun (Actions blocked).
2. **353** (`20261005130000_unclaimed_pages.sql`, PR #378, seed lane).
3. **331** (`20261005150000_map_mix.sql`, PR #383; the `331-map-mix` branch already carries 353's migration).

**Batching (the PM, 2026-10-05):** merge `origin/363` into `331-map-mix`, and the three apply in one run from that branch: GitHub app → socialus-web → Actions → apply → branch `331-map-mix` → type `apply`. Until that merge, any later branch must contain 363's file once 363 is applied, or `db push` refuses.

## Open PRs this lane owns (socialus-web)
- **Merge on green (Don doesn't need to look):** #395 (no previews until the freeze), #397 (a UI PR needs the first pass), #399 (review page accessibility), #385 (voice-and-tone references). Watchers ran in the old session; re-arm them, or merge by hand once CI runs.
- **human-review, merge on green plus first pass (no previews until 10-23):** #360 (edit the Page by section), #379 (Sign-in and You; no public member profile), #382 (Create: Be creative), #383 (map mix, migration), #392 (retire /you/sell, stacked on #379).
- **The 363 stack:** #364 (purpose, migration) → #366 → #368 → #370 (owner tools; Add offers an event or a post), all stacked on #360. Merge #360, then retarget #364 to main and work down. Stacks deeper than two are now against the build rules: collapse as they merge.
- **#372 (badges):** builds the Badges & values section the PM cut from beta. Left untouched; the PM to say close or park.

## Next
- Re-arm the merges once Actions runs; confirm #364's Browser, then hand the PM the batched apply.
- First passes (UX checklist) for the human-review PRs when Docker is back.
- #398 findings 6–7 (swipe hint copy; category on the blur once F078 exists) wait on the PM and F078.
- Spawned task: remove the unused member-profile code after #379 merges.
