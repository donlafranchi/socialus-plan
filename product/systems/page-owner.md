---
id: what-page-owner
purpose: When someone needs a Page, and how a Page owner is derived from Group membership, never a stored role or a business entity.
layer: what
status: active
---

# Page owner

A Page is for organizing things that recur: a business, a volunteer group, someone who teaches a class every week. A one-time act, such as a garage sale, needs no Page: the person posts an announcement without one. *(2026-11-16, Don: the word "creator" is retired for **Page owner**; see `foundation/nouns.md` § The two sides.)* There is no Page-owner record, no business entity and no stored role anywhere in this pattern: a Page owner is computed from Group memberships (`group_memberships.role`), which are dated, declared and auditable.

## Selling tools have no toggle

There is no "maker mode". Selling and hosting start from a Page (ruling 2026-10-05, below): the Page's Add offers a dated Post and the other Post kinds, and product and service listings come when they are due. A Member without a Page is fully functional: they can browse, RSVP, follow, save and post an announcement. To stop selling, end the owner membership; there is no separate off switch.

## Standing presence is a data state, not a mode

A Member has standing presence, the gate for the fuller assistant surfaces (`assistant.md`), when they hold an active business-Group membership of any role, or a steward role in any non-business Group. It is computed from membership rows, never stored.

## No promote-to-recurring flow

A one-off act never auto-upgrades into a persistent presence. A garage sale, a single class or one gathering stays an Item or announcement with a date. The platform does not detect a second occurrence and offer to turn it into a Page, and does not create one on someone's behalf. A Member who wants a long-lived presence creates it themselves, deliberately.

## What this rules out

A stored role or account-type column of any kind. A Business entity anywhere in the ownership chain: a Member who runs a business is captured by their Group memberships and Items. A promotion path from a one-off act to a persistent Page or Group.

## Rulings
- **2026-10-05 — Listing products and services, and hosting a gathering, start from a Page, not from You. `/you/sell` and its walkthrough retire to Create; their components and logic are kept, unrouted, for when product and service listings are due.** The PM, walking the preview: *"this is useful stuff but it should be product/service based and from a page not from you and is not a bad workflow just not in the right place."* And: *"let's not throw it away and add this information in the appropriate place for when it's time is due."* For beta the Page's Add offers a dated Post (a gathering) and the other Post kinds; product and service listings stay postponed until after beta (`ROADMAP.md` § Later). `socialus-web` #336, #369. [binds tiers=planning,code surfaces=you,pages,owner-tools,create]
- **2026-09-19 — Creator and organizer are distinguished by authority, not by attachment.** Don's ruling, and it lands in the code as a declared link. **Authority is `group_memberships.role`** — `owner` or `steward` — and it is what every managing check actually consults. **Attachment is `groups.founder_member_id`**, which records who *started* a Page and which **no permission reads**. **They coincide today only because one handler writes both**, and nothing makes them stay that way: **a steward who did not found a Page holds authority under the first and appears under neither of the others.** That relation ran the app while being undeclared; it is now the link *a Member runs a Page*. **The consequence for anything written before today: "the Page owner" and "the founder" are not synonyms**, and a scenario that assumes they are is wrong rather than loose.
- **2026-09-07 — The "Active in the community" badge is removed, no replacement.** A badge derived from a held role is the platform ranking people; same shape as the ownership tier already refused.
