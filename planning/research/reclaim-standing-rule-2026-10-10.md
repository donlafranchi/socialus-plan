---
id: research-reclaim-standing-rule-2026-10-10
purpose: Internal direction for agents building SocialUs: what kind of platform this is, and where it stands on data and extractive tools. Not a commitment, not public copy, not an absolute.
layer: research
status: draft
authored: Claude agent, 2026-10-10, at Don's request (voice-dictated)
---

# Direction for builders: don't let a few get rich off our members (2026-10-10)

**Internal orientation only.** No public commitment, no copy, no new absolute, no legal wording. Its job is to let an agent building a feature know what kind of platform this is. Exactly what it looks like is open (Don, 2026-10-10: "I don't know what that looks like exactly but it's a general direction"). It corrects the first voice pass, which framed the position as rejecting data collection.

## The direction, plainly

- We don't take money from investors who aren't members. Members will be some kind of owners, not shareholders. What that means in detail is undecided.
- The platform is not a way for a small few to get rich by taking advantage of members.
- We can use the same tools other platforms use (data, targeting, personalization, analytics, AI, ranking). We point them at the people they come from, not at shareholders, executives, partners or us.

## A question to ask while building

Not a gate, not lint-checked. When a feature collects or uses member data, or borrows a technique built to extract, ask:

1. **Whose is it?** The members it comes from.
2. **Who gains?** Ideally those members, in a way they can see and turn off. If the honest answer is someone else, or only us, pause and tell Don.

This is a judgment prompt, not a rule. It does not reverse anything settled (no shareholders, no selling member data, members are the investors).

## What to call it

Recommend **"Reclaim"**: a verb, so it reads as a practice; admits the tools are the same ones; pairs with the one allowed "never extractive". Alternatives: "Common Use", "Same Tools, Our Side". Internal name only for now; it need not appear in the product.

## Where agents will find it

Smallest useful step, all internal and easy to undo:

1. A short "Direction" paragraph in `product/foundation/what-this-is.md` (or `goals.md`), marked as direction, not promise.
2. A one-line pointer from `CLAUDE.md`, so a new agent reads it at the start.
3. Optional later: the question as a seventh line in `value-test.md`, if Don wants it enforced. Not proposed now.

Not proposed: a `DECISIONS.md` binding, a product absolute, public copy, or Terms and Privacy changes. Those wait until Don says what it looks like.

## Places the direction touches (for judgment, not action)

Where existing docs refuse a *tool* outright, this direction cares about the *aim*. An agent should know these are now judgment calls to raise with Don, not settled yeses:

- `monetization.md` § Refused outright: behaviorally targeted ads, data sales or licensing. Selling to others still fits poorly; targeting that serves the member it is about may be open.
- `model.md` § Personalized means interests, and `discovery.md`: personalization limited to declared interests.
- `metrics.md` anti-metrics and `ROADMAP.md` Won't: streaks and pull-back notifications fail the question and stay out; the rest are case by case.
- `goals.md` promise 3 ("No selling member data"): consistent, narrower than the direction.
- Already in line: F089 search demand (Don, 2026-09-15), venue attribution (2026-09-30), give-back in `contributions.md`, `impact-diagnostic.md`.

What the app collects today, worth knowing while building: email, phone check (Twilio), legal name, zip, 18+ box; IP and time on posts and uploads (kept a year, operators only); Sentry error tracking; saved searches, follows, RSVPs; reports with an Anthropic first pass; geocoding and map lookups; unclaimed business Pages built from public info (#353), the hardest case. The legal starter lists Vercel Analytics but the app has no analytics package, so one is out of date.

## Not read

Foundation, systems, legal and decision files were read; scenarios F048 to F102 were searched by keyword only.
