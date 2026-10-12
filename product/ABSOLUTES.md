> **SETTLED — do not re-raise:** members are the investors and the only people paid out. "Ownership, not profit-share" is rejected. Legal/securities questions about this go to `socialus-legal` for counsel and never come back to the PM as a decision. SocialUs takes transaction income; any 'no fee' language is retired.

# Product absolutes

What the platform will not do to a member. The process absolutes — production,
public acts, authority — are in `ops-pattern/process/ABSOLUTES.md`, which also carries
**the four-harms test** every absolute must pass and the rule for adding another. Both are stated once, there, and govern this page too.

Cite these by slug in brackets — `[member-content-takedown]`, never "rule 1".

## People

### member-content-takedown

Nothing a member contributes — image, text, page, listing — goes live in
production until there is a report-and-takedown path for that kind of content.

### member-data-disclosure

Member data is never exposed beyond what the member chose to show. Addresses,
contact details, and private records stay private by default.

## The value absolute lives elsewhere

The product's one value absolute — wealth circulates in the community, the
platform never extracts it — is in `charter.md`, not here.

## Rulings
- **2026-09-16 — `RULES.md` is split into `ops-pattern/process/ABSOLUTES.md` and `product/ABSOLUTES.md`, and absolutes are cited by slug, never by number.** The six absolutes are unchanged in substance; only where they live and how they are cited changed. Rules 1-2 (member-facing) went to `product/ABSOLUTES.md`; rules 3-6 went to `ops-pattern/process/ABSOLUTES.md`, which also carries the four-harms test and the rule admitting a seventh, stated once for both files. **Why:** three of the five numbered rule sets across these repos were already dead pointers and nothing flagged them — numbers renumber and citations to them rot silently. `scripts/lint.sh` now fails on any bracketed slug with no matching `###` heading, which is the point of the change; the split is what makes the check possible. **This file is exempt from that check and its own citations are deliberately not rewritten** — append-never-edit outranks tidiness. The map, so they stay resolvable: rule 1 → `[member-content-takedown]`, rule 2 → `[member-data-disclosure]`, rule 3 → `[production-asks-don]`, rule 4 → `[public-is-draft]`, rule 5 → `[don-decides]`, rule 6 → `[ruling-is-dated-line]`. Earlier lines here naming `RULES.md` as a file mean those two pages. [for now]
