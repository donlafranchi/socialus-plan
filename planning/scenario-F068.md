---
id: F068
title: A Page owner sees who noticed
status: draft
horizon: later
rank: 140
date: 2026-09-10
depends: []
---
## Story

A Page owner wants to know whether people are looking and whether it's working — views on their Page and its posts, set beside how many responded. Nothing counts views today; this captures one row per viewer per day, rolled up daily, visible only to the Page's own manager.

## Acceptance

1. A view is recorded at most once per person per day; anonymous views are recorded as anonymous, not dropped.
2. Only the Page's manager sees view/interaction counts — nobody else sees anything about their own view.
3. Attributed and unattributed views are shown as distinguishable, not blended into one number.

## Not this

Referrers, sessions, or exportable reports. Showing names at launch — counts only for now; first-name/nickname display is a later increment per the 2026-09-10 ruling, on the existing `display_name` field.

## Rulings
- **2026-09-10 — Page-view counts to the owner (F068) will eventually show first names/nicknames, not stay counts-only forever.** Ships counts-only at launch; naming is a later increment on the same capture, using the existing free-text `display_name` field — no new column.
