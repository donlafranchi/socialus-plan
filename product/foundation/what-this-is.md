---
id: why-what-this-is
purpose: The canonical description of what this product is and who it's for — the sentence every other description is checked against.
layer: why
status: active
---

> **SETTLED — do not re-raise:** Wealth circulates here; it is never extracted. The many benefit, not a few — the only test any money decision must pass. Any mechanism that passes it is open; who is paid what, ownership and incorporation stay open. Detail: `product/foundation/monetization.md`.

# What this is

Written by the PM for a sign at a farmers market: what every description, pitch or metadata string is checked against (not the specs, which describe mechanics). Internal until the PM says otherwise.

## The sign

> **Better Together**
> **Not a~~nother~~ dating app.**
> **Help us shape the future.**

The strikethrough reads both ways: "Not another dating app" and "Not a dating app."

## What it is

Locals supporting locals. A local discovery and community-building platform — the organizing backbone for decent, caring people to find each other, meet up, trade, teach, volunteer, and buy from and sell to their neighbors. What members share leads: happenings, insights, recommendations, local tips, and the time-sensitive things a place offers. Businesses are one kind of local among many; this is not another business listing site. Someone with a new idea can put it to the community, and others signal real interest before it exists. Away from home it works the same: a visitor supports lodging, food and services owned by the people who live there.

## Direction

*Internal, early, not a promise (Don, 2026-10-10).* SocialUs is the people's platform. We're not taking money from traditional investors. We'd rather be owned by our members, and how that works is still open. We don't want a few people getting rich off our members. SocialUs collects data. We collect data to benefit our members, never to enrich shareholders or investors, and we make it easy to opt out (Don, 2026-10-11). When a feature uses member data, ask who it comes from and who gains. If it's someone else, check with Don.

## The elevator speech

> Better Together helps you find and support the people near you. Meet your neighbors. Trade what you make. Volunteer where it's needed. Got an idea — a workshop, something homemade? Share it. Your neighbors can show they want it before you even start. This is for people who care about each other and the place they live. Join us, and help shape the future — together.

## What this settles, by being said out loud

It's not a marketplace: meeting, volunteering and floating an idea sit alongside buying and selling. The audience is named by disposition, "people who care about each other and the place they live," never a segment. "Decent, caring people" is the trust model, enforced by community and peer pressure, not platform arbitration (`policy.md` § How good faith is enforced).

## Settled — the name and tagline

**SocialUs is the name. *Better Together* is the tagline.** The name stands in the code, metadata, repo and domain; the tagline goes on signs and headlines. Closed: don't reopen it on the strength of a good line.

## The call to action is participatory: a copy constraint

"Help shape a better future": everything user-facing reads as an invitation to build the thing together, not an announcement of a finished product. An empty state that apologizes for being empty contradicts this; one that invites you to be first serves it. Nearly every surface is empty at launch, so the empty states are the product on day one, and a promise made at a market and then broken by the interface is worse than none.

## Won't

- Streaks, guilt prompts and anything that works by making a member feel stuck: the extraction other apps use their tools for (the 2026-10-25 ruling below).
- Payroll, HR, or employee management — the platform records who's associated with a Page, it doesn't manage employment.

## Rulings
- **2026-11-23 — The January 6, 2027 opening is a beta of the Sacramento-area market: the company forms January 1, the beta tests that one market until about April or May 2027, and production follows then. There is still no build freeze: approved work builds in its lane order, and everything the 2026-11-06 freeze held is unheld.** The PM, verbatim: *"let me clarify that this would be a beta launch so that I can set up my LLC on January 1 and we would test until April or May in this market."* The no-freeze half is carried forward unchanged from 2026-11-21 (*"What's the build freeze? There is no build freeze."*); what changes is the market (Sacramento, F103), the opening date and an end to the beta in place of "no deadline". F118's "Sacramento is … already open" describes the data; people sign up from the opening (F076.17). The edge is the PM's open call: `planning/briefs/sacramento-market-edges-2026-11-23.md`. [for now] [replaces 2026-11-21: There is no build freeze: approved work builds in its lane order, and everything the 2026-11-06 freeze held is unheld. The beta runs to the 2027 launch with no deadline, open from the waitlist and signup, in one market, Northern California (F103); production stays April–May 2027.] [binds tiers=planning,code surfaces=beta,launch,roadmap,moderation build=none]
- **2026-11-06 — The message is one line: "Locals, finding and supporting locals." The landing page, /join and every pitch say that and nothing competing; the message stays open to anything that revolves around locals supporting locals.** Don, verbatim: *"we simplify our message and landing page to Locals, finding and supporting locals. And leaving out open to anything that revolves around locals supporting locals."* No copy changes yet (Don, 2026-11-06: *"don't change any copy yet"*); the rewrite is a to-do on his dashboard, and he approves it before it ships. [for now] [replaces none] [binds tiers=planning,code surfaces=copy,landing,join,ethos build=none]
- **2026-11-26 — SocialUs is chat and search with a generated interface: a member asks, and the answer is built for that request; Explore, the map and other views are things a request returns, not places to navigate to, and a new member lands in chat.** The PM, verbatim: *"/explore is now a request from chat. so a new member should land in the chat interface and then the interface is based on user request like from generative ui"*, then *"I want to approve the chat/search and generative ui path. one example of how to build is to use googles sdk A2UI."* A2UI is an example, not a ruling on the tool. [for now] [replaces 2026-10-26: SocialUs is moving toward chat-first: a member's question opens the right page] [binds tiers=planning,code surfaces=navigation,ask,front-door,explore,map,onboarding build=none]
- **2026-10-25 — The tools other apps use are ours too, used for everyone's benefit: personal and response-aware ranking on Discover and Home, notifications, AI, and marked promotion on Discover are in, each one something a member can turn off; Find stays the plain tool. Only extraction stays out: selling data, and tricks that work by making a member feel stuck.** The PM approved the ethos and this reversal 2026-10-25 (`PRINCIPLES.md` § Soul, `#benefit-all`). Trust and verification may use automation too; a person decides when it is contested. [for now] [replaces none] [binds tiers=planning,code surfaces=explore,discovery,notifications,ranking,ai build=none]
- **2026-10-25 — Rulings tagged for-now because their record didn't say otherwise stay for-now; the release-planning pass keeps, hardens or retires each against the soul. Only the soul, the defaults and the principles marked so hold in every version.** By the defaults (trust first; well-worn). [for now] [binds tiers=planning surfaces=principles,roadmap build=none]
- **2026-10-30 — SocialUs is locals supporting locals, not a business listing site: what members share (happenings, insights, recommendations, local tips) and the time-sensitive things a place offers (deals, specials) lead; a business is one kind of local among many and a listing is never promoted for its own sake. The same when travelling: support the people who live where you are visiting.** Don, verbatim: *"I essentially don't want this to be another business listing site. … Maybe promote/support local, or time sensitive deals or specials. For example bars and restaurants that hosted the World Cup this past summer. And most importantly we need people to be able to share happenings and insights, recommendations and local tips."* A Page still carries contact details, pictures and hours; what changes is what leads. [for now] [replaces 2026-10-01: The launch is a rich-context yellow pages: organizations, not people, filled in by their owners, with pictures, links and contact details. Individual product and service listings are postponed until after launch.] [binds tiers=planning,code surfaces=principles,explore,pages,launch,copy build=none]
- **2026-09-30 — SocialUs is currently not a fully built-out platform of any kind — booking, storefront, payments or other — except for helping with discovery and support of locals. It may offer basic versions of these, so people can transact in the platform and connect.** Don: *"as far as becoming a booking app. That's probably accurate but we may want to offer basic services and not be a fully built out booking service. We'd like people to transact in our platform and possibly connect to others. Let's make the differentiation where needed. It's also possible a global statement too. We are not a fully built out any platform except to help with discovery and support of locals."* **The ROADMAP Won't line is restated:** full-featured versions are out, basic in-platform versions are possible. Its old words were *"the platform coordinates, it isn't a storefront or a booking system"*, from a deleted producer roadmap (2026-05-27) that also said the platform *"may link to external booking … but won't build its own"*; neither was a dated ruling, and that second line survives nowhere live. [for now] [binds tiers=planning surfaces=scope,booking,payments,storefront]
