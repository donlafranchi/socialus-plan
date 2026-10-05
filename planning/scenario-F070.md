---
id: F070
title: Every Page has a face, even without a photo
status: building
date: 2026-09-10
depends: [F061]
amended: 2026-10-05 — Don (F099): a Page with no image shows its kind's placeholder, which is how kinds are told apart at a glance; letter art is gone. A Page may also carry one Page picture (F099), so "Multiple images per Page" leaves Not this.
---
## Story

Don adds a photo of the counter to his new Page; it's downscaled, re-encoded, and stripped of GPS metadata before it ever leaves his phone. The seeded Pages with no photo don't look broken — each shows its kind's placeholder image, the same every time, so a group reads as a group and a shop as a shop at a glance, and nothing looks unstable or borrowed from a stock library.

## Acceptance

1. A photo step is optional; the composer completes without one.
2. An uploaded photo's stored bytes carry no metadata block (GPS included) — verified against the file, not the code's intent.
3. A raw upload bypassing the client (wrong format, oversized, wrong path) is rejected by the storage API itself.
4. A Page with no photo shows its kind's default image or icon (Don, 2026-10-01) — identical on every load, to every viewer. Where a Page picture is missing, the same kind placeholder stands in (F099).
5. The operator can remove a Page's photo in one action; the object is deleted and an event recorded.

## Not this

Cropping UI beyond a fixed centre-crop. More than the one Page photo and one Page picture (F099); a gallery is after beta. Initials or letter art. Anything sourced from a stock library.
