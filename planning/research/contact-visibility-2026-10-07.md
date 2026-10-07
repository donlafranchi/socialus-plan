# Contact fields: who sees them (2026-10-07)

PM ruled option B. Decision line: `DECISIONS.md` 2026-10-07. Matrix: `product/foundation/nouns.md`. Issue: `socialus-web` (change · Page contact email…). Path: well-worn.

## Rule
- Every contact field (website, hours, phone, Contact email) has one visibility: **everyone** (signed-out visitors included) or **members** (signed in).
- Defaults: website, hours, area-level location = everyone. Phone, Contact email = members.
- Owner flips one field with a small globe (everyone) / lock (members) icon beside it. The (i) explainer sits on that icon. Each field exists once.
- Signed-out = public; signed-in = members. Free text is not scanned for emails (closes #450's remaining question).

## Why members-only for phone and email
Public phone numbers and emails are harvested by spam bots; a website and hours are what a passer-by needs. Signed-in members are verified people (2026-09-30), so the field reaches real customers without reaching scrapers.

## Precedents (patterns, not deep links; unverified detail to confirm at build)
- [Google Business Profile](https://business.google.com): the owner chooses which contact details show on the listing.
- [Airbnb](https://www.airbnb.com): contact details stay private until a relationship exists.
- [Yelp](https://biz.yelp.com): a business's website and phone are listed; personal emails are not.

## Options
- **A. Fixed split.** Website, hours public; phone, email members-only; no owner control. Simplest, but a business that wants its phone public can't.
- **B. Same default + per-field globe/lock (chosen).** One field, one icon, one flip. Small UI, no duplicated fields, owner stays in charge.
- **C. Two sections.** Fields moved between "public" and "members" cards. Clear but heavier, and moving a field is more work than flipping an icon.
