---
id: F118
title: Open your town — neighbours bring in the makers they love until their market opens
status: approved
horizon: next
rank: 1
date: 2026-10-26
approved: 2026-10-26 — the PM: 100/1,000 and the first 3; after the soft launch; v1 is one form
depends: [F076, F103]
---
## Story

*2026-10-26, verbatim:* "We are gatekeeping other markets but we also want end users to have more control. What we want is a few dozen businesses by kind and 10x the consumers side. What would be ideal is if we allow users to work to open their community by adding businesses they love and seeing if those businesses will also sign up. similar to how I asked you to populate some businesses. It would be a sort of soft sign-up where early adopters share this platform with local businesses or local makers and have them sign up and if they sign up as a maker/organizer/business they count towards a goal and if they sign up as a supporter/consumer/meet-up-goer they count towards the other goal. And every market should have it's own page where users can see how many have signed up and how many still to go. essentially help people be the change and empowered to get this going. … Perhaps we limit it to the first 3 that meet the criteria to help us grow etc."

*Then:* "I'd like 100 and 1000. and three towns is good." *On timing:* "Town pages will come after we soft launch and before hard launch."

*v1 scope:* "Open your town could be a simple form that asks are you a business or maker or creator or are you here mainly to find and support those who create or sell or plan meet ups. We ask for emails and urls for the creators or their socials for where to be found and where they live and play."

Someone in Vacaville hears about SocialUs, which isn't open there yet. They fill in one short form: they're here to find and support makers, here's their email, they live in Vacaville and spend weekends in Davis. A baker in Dixon fills in the same form: she makes and sells, here's her site and Instagram. Later, after the soft launch, the market's page shows two bars filling toward 100 makers and 1,000 supporters, and neighbours start adding the makers they love.

## Acceptance

Draft pass/fail criteria. **v1, the form (the MVP):**
1. One form asks a role, with neither choice pre-selected: "I make, sell or organize" (a business, maker, creator or organizer) or "I'm here to find and support them and show up".
2. It asks for an email.
3. A maker also gives their website or social profile URLs, where they can be found.
4. Everyone gives their town or towns: where they live, and where they play or spend time.
5. **Privacy:** these answers go from the member to staff only. The email is never shown to another member. Opting out is one easy step and removes the answers.
**Later, building on that data (after the soft launch):**
6. **Market pages** at `/open/<market>`, plus an `/open` index. Each has two bars, makers X of 100 (across kinds) and supporters Y of 1,000, each with how many are still to go.
7. **Soft sign-up:** a supporter account tied to a market. They can add makers and invite people, and get the full app when the market opens.
8. **Add a maker you love:** it becomes an unclaimed Page under the seeder rules (own site or socials only, credited photos, no children in photos, Samples labelled). It is matched against existing Pages first. The supporter shares "Claim your free Page on SocialUs"; a claim counts toward makers and credits the inviter.
9. **Variety:** a market shows its makers by kind (food, shops, makers, services, groups and events), so neighbours can see which kinds are missing.
10. **First 3 open:** the first 3 markets to reach both goals open in this round. Each is notified (the ruled "SocialUs is open in {market}" message) and opened by a person.
11. **Spam and abuse:** assume the best. Anyone signed in may add a maker, with a daily limit per member, and the existing report and remove-my-Page paths. Test and builder accounts never count, and each person counts once.
12. **Funding (a note only, no action now):** opening more markets needs money, first donations or investment, then transaction income after growth.

## Not this

Nothing beyond the landing page now: this comes after the soft launch, before the hard launch. **Built ahead of schedule:** `socialus-web` #1093 (town pages, add a maker, counting, the daily ready-town check, onboarding to the town page) **merged and is live** at `/open`. It went further than wanted now and counts per county rather than per market. It is parked: after the soft launch it is reworked to the market definition, or reverted. Which of the two is open below.


Open questions:
[open-question owner=cowork raised=2026-10-26] What is a market for counting: the market definition is still being researched. #1093 counts per county.
[open-question owner=don raised=2026-10-26] Should #1093 stay live, parked behind a flag, or be reverted until the soft launch?
[open-question owner=code raised=2026-10-26] Where does the v1 form live: the landing page's existing list form, extended, or a form of its own?
[open-question owner=cowork raised=2026-10-26] Do a supporter's "places they play" count toward those markets, or only where they live?
[open-question owner=cowork raised=2026-10-26] Are neighbour invites credited, or only maker invites that end in a claim?

## Why

- **Lives somewhere better?** No: Nextdoor's founding-member gate and Kickstarter's goal bar exist, but neither lets neighbours bring in their own makers.
- **Only locals know?** Yes: which bakery, which maker, which run club.
- **Gets people together?** Yes: neighbours recruit the people they already buy from.
- **Stays fresh on its own?** Yes: counts move with sign-ups and claims; nobody edits them.
- **Who keeps it current?** The members, by signing up, adding makers and claiming Pages.
- **Better as more people join?** Yes: that is the whole mechanic.

Soul: `#out-of-the-way`, `#you-choose`, `#decent`. **Path: well-worn.** Precedents: Nextdoor's founding-member threshold (help.nextdoor.com), Kickstarter's goal bar (kickstarter.com/help/handbook), DoorDash's city-request pages (doordash.com/cities).

[platform none]

## Rulings
- **2026-10-26 — A market opens when it reaches 100 makers (businesses, makers or organizers who sign up or claim their Page) and 1,000 supporters (neighbours who sign up as members); only the first 3 to reach both open in this round. Sacramento is the launch market and is already open.** The PM. [for now] [replaces 2026-09-14: A metro opens on 50 creators and 250 patrons, gated on the creators] [binds tiers=planning,code surfaces=waitlist,open-your-town build=none]
- **2026-10-26 — Open your town comes after the soft launch and before the hard launch; only the landing page is in scope now.** The PM. [for now] [replaces none] [binds tiers=planning,code surfaces=open-your-town build=none]
- **2026-10-26 — Open your town v1 is one simple form: make-sell-organize or find-and-support, an email, a maker's site or social URLs, and the towns where a person lives and plays. Answers go to staff only, and opting out is one step.** The PM. [for now] [replaces none] [binds tiers=planning,code surfaces=open-your-town,landing build=none]
- **2026-10-26 — The counting unit is the market (a region), not a town or county; its definition is still being researched.** The PM. [for now] [replaces 2026-10-26: A town on the Open page is a waiting market in the coverage area] [binds tiers=planning,code surfaces=open-your-town build=none]
- **2026-10-27 — Open your town is built but held back: one flag, off until after the soft launch. /open, /open/<town>, the signup redirect to town pages and the daily town round are inert; ring-county zips take the same waiting screen as any out-of-market zip. Code and migrations stay.** The PM ("A", on the merge of web #1093 by mistake). Built by web #1100. [for now] [replaces none] [binds tiers=planning,code surfaces=open-your-town build=none]
