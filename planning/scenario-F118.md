---
id: F118
title: Neighbours open their own town by bringing in the makers they love
status: approved
horizon: now
rank: 6
date: 2026-10-26
approved: 2026-10-26 — the PM's ruling (100 makers and 1,000 supporters; the first 3 towns)
depends: [F076, F103]
---
## Story

Someone in Vacaville hears about SocialUs. Vacaville is not open yet. They open "Help open your town", find Solano County, and see two bars: 4 of 100 makers, 61 of 1,000 supporters, and that 2 of this round's 3 places are still free. They sign up with their email and a code, and count as a supporter. They add the bakery they love by its name and its own website; it becomes an unclaimed Page, and they text the owner a link to claim it free. The owner claims it, Solano moves to 5 makers, and the neighbour's first name shows among the people opening Solano.

## Acceptance

1. **A town is a waiting market inside the coverage area** (F103: counties and county subdivisions; the places table names their towns). `/open` lists every one, closest to opening first; `/open/<town>` is its page. A person finds theirs by town name or zip; a zip outside the list goes to the landing waitlist, a zip in an open market goes in.
2. **The town page shows two bars**, makers X of 100 and supporters Y of 1,000, each with how many are still to go; a breakdown of its makers by kind (food, shops, makers, services, groups and events); the people opening it by first name, top 10, each able to hide their name; and how many of this round's 3 places are left.
3. **A supporter is a member whose town it is**, by zip or by choosing it on the town page. Signing up is the existing email and 6-digit code. Until their town opens a supporter can add makers and invite people, and sees the town page rather than the full app.
4. **Add a maker you love:** name, town, and its own website or social profile. It becomes an unclaimed Page under the seeder rules (own site or socials only; no photos are added by a supporter, so no photo can show a child or go uncredited). A Page already on SocialUs with that site or that name in that town is offered instead of a second one. Each member may add 10 a day; any added Page is reportable like any other.
5. **Invite:** each added Page gives a share link, "Claim your free Page on SocialUs", to the existing self-serve claim. When the Page is claimed, it counts toward makers and the member who added it is credited.
6. **Counting:** makers are the distinct people who created or claimed a Page of a maker kind in that town; supporters are the other members whose town it is. Each person counts once. Test and builder accounts never count. The figures are cached, never recomputed in answer to the reader's own action (F076 criterion 14).
7. **When a town reaches both goals** it is marked ready, in order, and the round closes once 3 are ready; a fourth is not marked. A ready town is logged as an Issue for a person to open it with the existing open-market script, which sends the ruled "SocialUs is open in {town}" message.
8. **The landing page's "Help open your town" goes to `/open`.**

## Not this

Payments, donations or investment (a pointer for the Launch Coach, in the legal repo). Opening a town with no person running the script. Towns outside the coverage area. Ranking or showing who joined beyond the opt-out first names of the top 10.

## Why

- **Lives somewhere better?** No: Nextdoor's founding-member gate and Kickstarter's goal bar exist, but neither lets neighbours bring in their own makers.
- **Only locals know?** Yes: which bakery, which maker, which group.
- **Gets people together?** Yes: neighbours recruit the people they already buy from.
- **Stays fresh on its own?** Yes: counts move with sign-ups and claims; nobody edits them.
- **Who keeps it current?** The members, by signing up, adding and claiming.
- **Better as more people join?** Yes: that is the whole mechanic.

Soul: `#out-of-the-way` (members open their own town), `#you-choose` (they pick the makers and whether their name shows), `#decent` (anyone can add a maker; limits and reports handle the rest). Sins: none.

**Path: well-worn, scope ruled.** Precedents: Nextdoor's founding-member threshold before a neighbourhood launches (help.nextdoor.com), Kickstarter's goal bar (kickstarter.com/help/handbook), city-request pages such as Uber's and DoorDash's "request your city" (doordash.com/cities). Funding: opening more towns needs money (donations or investment, then transactions after growth); that pointer is the Launch Coach's, in the legal repo.

[platform none]

## Rulings
- **2026-10-26 — A town opens when it reaches 100 makers (businesses, makers or organizers who sign up or claim their Page) and 1,000 supporters (neighbours who sign up as members); only the first 3 towns to reach both open in this round. Sacramento is the launch market and is already open.** The PM. [for now] [replaces 2026-09-14: A metro opens on 50 creators and 250 patrons, gated on the creators] [binds tiers=planning,code surfaces=waitlist,open-your-town build=none]
- **2026-10-26 — A town on the Open page is a waiting market in the coverage area, named for its county or region and listing the towns inside it; the market stays the unit that opens.** Decided by the agent under the 2026-10-25 decision rights (well-worn: F103 made the market a set of towns, and the feed, the waitlist and the open-market script all work on markets). [for now] [replaces none] [binds tiers=planning,code surfaces=open-your-town build=none]
- **2026-10-26 — The town page shows its two counts in public, makers and supporters separately, cached; the combined "300" is retired with its thresholds.** Decided by the agent: the counts are of verified accounts and claimed Pages, and a cached figure carries F076 criterion 14. [for now] [replaces none] [binds tiers=planning,code surfaces=open-your-town,waitlist build=none]
