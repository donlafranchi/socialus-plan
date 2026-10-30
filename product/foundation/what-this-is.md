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

Locals supporting locals. A local discovery and community-building platform — the organizing backbone for decent, caring people to find each other, meet up, trade, teach, volunteer, and buy from and sell to their neighbors. What members share leads: happenings, insights, recommendations, local tips, and the time-sensitive things a place offers. Businesses are one kind of local among many; this is not another business listing site. Someone with a new idea can put it to the community, and others signal real interest before it exists. Away from home it works the same: a visitor supports lodging, food and services owned by the people who live there.

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

- Streaks, guilt prompts and anything else that works by making a member feel stuck. The tools other apps use are ours, for members (see the 2026-10-25 ruling below); this is the extraction they are usually used for.
- Payroll, HR, or employee management — the platform records who's associated with a Page, it doesn't manage employment.

## Rulings
- **2026-10-26 — SocialUs is moving toward chat-first: a member's question opens the right page.** The PM, verbatim: *"I like C. Let's use that as our direction and the users question opens one of these pages e.g. /you or /explore or other pages for example. We don't need to work on that now but should come up with a near term and long term plan."* The pages stay; chat becomes the way in. Near term is F119 (an Ask bar that deep-links to existing pages, in the beta); long term is F120 (answers and actions in chat, chat as home, after the soft launch). AI helps and never replaces a person (`PRINCIPLES.md` § Soul). [for now] [replaces none] [binds tiers=planning,code surfaces=navigation,ask,ai,explore,you build=none]
- **2026-10-25 — The tools other apps use are ours too, used for everyone's benefit: personal and response-aware ranking on Discover and Home, notifications, AI, and marked promotion on Discover are in, each one something a member can turn off; Find stays the plain tool. Only extraction stays out: selling data, and tricks that work by making a member feel stuck.** The PM approved the ethos and this reversal 2026-10-25 (`PRINCIPLES.md` § Soul, `#benefit-all`). Trust and verification may use automation too; a person decides when it is contested. [always] [replaces none] [binds tiers=planning,code surfaces=explore,discovery,notifications,ranking,ai build=none]
- **2026-10-25 — Rulings tagged for-now because their record didn't say otherwise stay for-now; the release-planning pass keeps, hardens or retires each against the soul. Only the soul, the defaults and the principles marked so hold in every version.** By the defaults (trust first; well-worn). [for now] [binds tiers=planning surfaces=principles,roadmap build=none]
- **2026-10-23 — There is no beta deadline and no feature freeze until April 2027: the beta runs until then, one metro (Sacramento), open from the waitlist and signup; production launch stays April–May 2027.** The PM: *"Remove the deadline until next April 2027. This is going to be a beta test until next year."* F100–F102 (AI first-pass moderation in shadow, the Posts review page, the poster answering first) stay in the beta and the built map work merges; everything on the council's CUT list stays in "After beta"; anything else cut from the beta is logged in `ROADMAP.md` under the PM's asterisk. The photo and report-path tripwires of 2026-10-07 are void. [for now] [replaces 2026-10-07: the feature freeze moves from 2026-10-23 to a proposed 2026-10-30 and the beta from 2026-10-30 to 2026-11-06] [replaces 2026-10-05: Beta is 2026-10-30, a soft target for testing in one metro, not a hard deadline. Feature freeze is 2026-10-23, also soft. Production launch is currently April–May 2027.] [binds tiers=planning,code surfaces=beta,launch,roadmap,moderation build=none]
- **2026-10-30 — SocialUs is locals supporting locals, not a business listing site: what members share (happenings, insights, recommendations, local tips) and the time-sensitive things a place offers (deals, specials) lead; a business is one kind of local among many and a listing is never promoted for its own sake. The same when travelling: support the people who live where you are visiting.** Don, verbatim: *"I essentially don't want this to be another business listing site. … Maybe promote/support local, or time sensitive deals or specials. For example bars and restaurants that hosted the World Cup this past summer. And most importantly we need people to be able to share happenings and insights, recommendations and local tips."* A Page still carries contact details, pictures and hours; what changes is what leads. [always] [replaces 2026-10-01: The launch is a rich-context yellow pages: organizations, not people, filled in by their owners, with pictures, links and contact details. Individual product and service listings are postponed until after launch.] [binds tiers=planning,code surfaces=principles,explore,pages,launch,copy build=none]
- **2026-09-30 — SocialUs is currently not a fully built-out platform of any kind — booking, storefront, payments or other — except for helping with discovery and support of locals. It may offer basic versions of these, so people can transact in the platform and connect.** Don: *"as far as becoming a booking app. That's probably accurate but we may want to offer basic services and not be a fully built out booking service. We'd like people to transact in our platform and possibly connect to others. Let's make the differentiation where needed. It's also possible a global statement too. We are not a fully built out any platform except to help with discovery and support of locals."* **The ROADMAP Won't line is restated:** full-featured versions are out, basic in-platform versions are possible. Its old words were *"the platform coordinates, it isn't a storefront or a booking system"*, from a deleted producer roadmap (2026-05-27) that also said the platform *"may link to external booking … but won't build its own"*; neither was a dated ruling, and that second line survives nowhere live. [for now] [binds tiers=planning surfaces=scope,booking,payments,storefront]
