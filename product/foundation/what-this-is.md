---
id: why-what-this-is
purpose: The canonical description of what this product is and who it's for — the sentence every other description is checked against.
layer: why
status: active
---

> **SETTLED — do not re-raise:** members are the investors and the only people paid out. "Ownership, not profit-share" is rejected. Legal/securities questions about this go to `socialus-legal` for counsel and never come back to the PM as a decision. SocialUs takes transaction income; any 'no fee' language is retired.

# What this is

Written by the PM for a physical sign at a farmers market — the clearest statement of the product produced so far, and what every description, pitch, or metadata string is checked against (not the specs, which describe mechanics). Internal until the PM says otherwise — not published anywhere.

## The sign

> **Better Together**
> **Not a~~nother~~ dating app.**
> **Help us shape the future.**

The strikethrough on "nother" is deliberate — the line reads both ways: "Not another dating app" and "Not a dating app."

## What it is

A local discovery and community-building platform — the organizing backbone for decent, caring people to find each other, meet up, trade, volunteer, and buy from and sell to their neighbors. Someone with a new idea — a workshop, something homemade, any idea at all — can put it to the community, and others signal real interest before it exists, turning ideas into local economic activity.

## Direction

*Internal, early, not a promise (Don, 2026-10-10).* SocialUs is the people's platform. We're not taking money from traditional investors. We'd rather be owned by our members, and how that works is still open. We don't want a few people getting rich off our members. SocialUs collects data. We collect data to benefit our members, never to enrich shareholders or investors, and we make it easy to opt out (Don, 2026-10-11). When a feature uses member data, ask who it comes from and who gains. If it's someone else, check with Don.

## The elevator speech

> Better Together helps you find and support the people near you. Meet your neighbors. Trade what you make. Volunteer where it's needed. Got an idea — a workshop, something homemade? Share it. Your neighbors can show they want it before you even start. This is for people who care about each other and the place they live. Join us, and help shape the future — together.

## What this settles, by being said out loud

It's not a marketplace — meeting, volunteering, and floating an idea sit alongside buying and selling, in that order. The audience is named by disposition, not demographic — "people who care about each other and the place they live," not a segment or an age or an income. The invitation is participatory — "help shape the future" asks people to build the thing, not use it. "Decent, caring people" is the trust model in three words, and matches how good faith is actually enforced: community and peer pressure, not platform arbitration (`policy.md` § How good faith is enforced).

## Settled — the name and tagline

**SocialUs is the name. *Better Together* is the tagline.** Nothing is renamed — the name stands in the code, metadata, repo, and domain; the tagline goes on signs and headlines. The question is closed — don't reopen it on the strength of a good line.

## The call to action is participatory — a copy constraint, not decoration

"Help shape a better future" — the PM wants people to feel that they can, and that it's done together. Everything user-facing should read as an invitation to build the thing, not an announcement of a finished product. The test: an empty state that apologizes for being empty contradicts this; one that invites you to be first serves it. Nearly every surface is empty at launch, so the empty states *are* the product on day one — the same argument as the default Page art. A participatory promise made at a market and then broken by the interface is worse than not making it at all; someone told "help shape the future" who then meets copy that treats them as a consumer has been told two different things, and will believe the interface.

## Won't

- Engagement-optimized ranking, streaks, pull-back notifications. [for now — Find only; newer direction 2026-10-12, see PRINCIPLES.md "two sides"; under review]
- Automated government-API verification of producer claims — the trust ladder is human-driven (self-attest → community-attest → document-upload) only.
- Mass-email marketing tooling, push notifications to non-followers, individual visitor-tracking analytics for a producer.
- Payroll, HR, or employee management — the platform records who's associated with a Page, it doesn't manage employment.

## Rulings
- **2026-10-07 — The beta is an open beta from the waitlist and signup, Sacramento only (council option B): F100–F102 (AI first-pass moderation in shadow, the Posts review page, the poster answering first) stay IN beta; the feature freeze moves from 2026-10-23 to a proposed 2026-10-30 and the beta from 2026-10-30 to 2026-11-06; the built map work (`socialus-web` #479, #482) merges. Everything on the council's CUT list moves to "After beta".** The PM, option B. Because more feedback from an open beta is wanted, and AI moderation has to be running before strangers arrive at volume with the operator away Tue–Thu. Council transcript, MVP IN and CUT lists, tripwires (proposed, pending PM) and dissents: `planning/council/2026-10-07-beta-mvp.md`. [binds tiers=planning,code surfaces=beta,roadmap,moderation build=none]
- **2026-10-05 — Beta is 2026-10-30, a soft target for testing in one metro, not a hard deadline. Feature freeze is 2026-10-23, also soft. Production launch is currently April–May 2027. Anything cut from beta is logged in `ROADMAP.md` under the PM's asterisk.** [binds tiers=planning,code surfaces=launch,roadmap build=none]
- **2026-10-01 — The launch is a rich-context yellow pages: organizations, not people, filled in by their owners, with pictures, links and contact details. Individual product and service listings are postponed until after launch.** Don: *"The launch is mostly a modern yellow pages with links and contact info like address of business and phone."* And: *"think of this similar to a yellow pages, but we're doing a little bit more like a more rich context information Yellow Pages because we can because it's modern because the people will be filling it out themselves and yellow pages as opposed to white pages and also that we already have pictures and will include that."* Listings wait in `ROADMAP.md` § Later. A business phone and weekly hours are on a Page (below). [binds tiers=planning surfaces=launch,pages,items]
- **2026-09-30 — SocialUs is currently not a fully built-out platform of any kind — booking, storefront, payments or other — except for helping with discovery and support of locals. It may offer basic versions of these, so people can transact in the platform and connect.** Don: *"as far as becoming a booking app. That's probably accurate but we may want to offer basic services and not be a fully built out booking service. We'd like people to transact in our platform and possibly connect to others. Let's make the differentiation where needed. It's also possible a global statement too. We are not a fully built out any platform except to help with discovery and support of locals."* **The ROADMAP Won't line is restated:** full-featured versions are out, basic in-platform versions are possible. Its old words were *"the platform coordinates, it isn't a storefront or a booking system"*, from a deleted producer roadmap (2026-05-27) that also said the platform *"may link to external booking … but won't build its own"*; neither was a dated ruling, and that second line survives nowhere live. [binds tiers=planning surfaces=scope,booking,payments,storefront]
