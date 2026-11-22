---
id: brief-2026-11-22-sacramento-launch-campaign
status: awaiting-approval
size: L
path: new territory
concept: CO-0070
fits: the town launch (F076 ruling 2026-11-22); story map JY-LAUNCH; conditions CN-0001 to CN-0016; builds on The town before it opens (CO-0065), F136, F081, F076
criteria:
  - The Sacramento area opens to real sign-ups only when every must-have part of CN-0001 on the picked cut line is met; nothing below the line holds the opening.
  - A person anywhere asks the homepage whether their town is open and gets a straight yes (to sign-up) or not yet (to the waitlist), decided by their zip; a test with an out-of-area zip proves no code is texted, seen failing first.
  - No email goes to anyone who didn't ask for it or isn't a public business contact, and every email carries a one-click opt-out.
---

# The Sacramento launch campaign

**As of 2026-11-22** · Source: the PM's words below; F076, F081, F136, The town before it opens (CO-0065), socialus-web Issues and the Beta milestone, INFRASTRUCTURE, the 2026-11-20 launch report, the socialus-legal launch plan, the knowledge store · Maintained by: hand (brief; deleted at 30 days or once ruled and placed)

*The PM, 2026-11-21/22:* "these couple things belong to a campaign that we should add to the knowledge store and the campaign is a launch campaign and the launch campaign is going to comprise of the new chat search, oriented homepage, and it will also include some sample prompts that teach the users how they can use the site teach the users what the site is intended to be for and tells users whether their market is open or not and this will also include emails that go out to vendors and pay traders [patrons] to let them know what we're about and where to find us and why they would want to use us and then I'm also thinking about some kind of outreach campaign alongside this that includes some kind of stickers for businesses to put up to say find us here and there may be more things"

*Then:* "this is the town launch. I'm thinking the sacramento area and for January 1 or so."

**Bottom line: January 1 with everything on the list is not realistic: six weeks, two holidays, about a dozen open build tickets and a new homepage that isn't designed yet. Open Wednesday January 6 with a must-have cut, and let stickers, the second email wave and Google/Apple sign-in follow in January.**

**Your call:** which cut line and date: **B, must-haves and open Wednesday January 6 (recommended)**, A, everything by January 1, or C, the smallest open on January 1 with the new homepage following?

*In the store:* the campaign is a story map (JY-LAUNCH: hear about it → ask the front door → learn what it's for → find out if my town is open → join), each step naming the condition it waits on (CN-0001, "Sacramento is ready to open", and its parts CN-0002 to CN-0016). The campaign is its own concept (CO-0070). Your pick becomes the map's slices.

## The picture

Five steps, one story. A vendor gets an email and a shopper sees a "Find us here" sticker in a shop window. Both land on the homepage, a single box. A sample prompt shows what SocialUs is for. "Is my town open?" answers yes for a Sacramento-area zip and sends them to sign up with a mobile number; any other zip joins the waitlist. Behind the door sit phone sign-up, screening every post, the invite emails and a database that doesn't pause.

## What must be true to open (readiness against January 1)

| What must be true | Who | Where it stands | Waits on | Cut |
|---|---|---|---|---|
| Twilio account with a Verify service | You | Not opened | nothing | Must |
| Phone sign-up: texted code, real mobiles only, anti-bot layers | Agents | Not started; the code is still email-first | Twilio | Must |
| New accounts start small for their first week | Agents | Not started | nothing | Must |
| Every post and photo screened before it shows; the safety package after removal | Agents | Not started; screening runs in shadow first, about a week | nothing | Must |
| Waitlist invites by email when Sacramento opens | You, then agents | Resend not set up; the opened-email send is open | Your Resend step | Must |
| Supabase Pro with the spend cap on | You | Free plan: pauses after a quiet week, no daily backups | nothing | Must |
| Terms and Privacy ready for real sign-ups | You, counsel | Beta drafts live, written for email sign-in; counsel was planned before production, not before opening | A counsel answer (asked in the legal repo) | Must |
| The launch-blocking checks pass (waitlist, phone, posting rules, reports) | Agents | 12 open | nothing | Must |
| Alerts reach you (Sentry, UptimeRobot, Vercel spend) | You | Monitoring built 11-16; your alert steps pending | nothing | Must |
| Someone watches the report queue in opening week | You | Not set | nothing | Must |
| The homepage is chat-search, rules only, no AI model, with "is my town open?" | Agents | Not started; its brief awaits your pick | Your pick (A) and its words | Must in B |
| Homepage words, sample prompts, town-open answers | Copywriter, you | The 11-21 draft copy brief and intent brief aren't in the repos yet | You handing them over | Must in B |
| Emails to vendors and patrons, first wave | Copywriter, you, agents | Not started; Resend sends 100 a day free | Words; Resend | Must in B |
| Out of memory at 1,000 viewers | Agents | Fixed 11-22: it was the test runner's Node; 1,000 signed-out viewers 83% served, no crash | — | Done |
| The 3-connection pool | Agents | Raised to 10; it never ran dry under load | — | Done |
| The Sacramento area's edges | — | Settled: the market as it stands (the 10-27 one-hour reach) | — | Done |
| "Find us here" stickers | You, copywriter | Not started; printing is new spend | Final words and the scan target | January |
| Item tags lead search | Agents | Open, needs a fix | nothing | January |
| Google and Apple to sign in next time | You, agents | No ticket; linking a phone account to Google or Apple needs a trial first | Your Apple account ($99) and a Google client | January |
| The company (LLC) | You | Legal plan: early January | — | Not a gate under the legal plan; counsel asked |
| NCMEC CyberTipline registration | You | The beta uses the public form (no images); registration needs the company | The company | Not a gate; by April |
| AI chat, values and the blue dot, town pulse map, floating wishes | — | Briefs only | Opening first | Later |

## Five Deadly Sins, plainly

- **Unrealistic schedule:** six weeks with Thanksgiving and Christmas in them; January 1 is a Friday holiday, businesses are shut and inboxes are full. Everything by then: no. A cut by January 6: yes, if your account steps land by November 29.
- **Scope creep:** stickers, two email waves, AI chat, values and the map all ride on one date. Only what opening needs rides on it.
- **Gold plating:** the full widget library (pulse map, floating wishes, dashboard) isn't needed to open; results, "is my town open?" and Browse are.
- **Vague requirements:** the two homepage copy briefs aren't in the repos; how many sample prompts and who gets the emails aren't set. The words come from your copywriter; the email list is the waitlist plus public business contacts.
- **Unclear acceptance:** "ready to open" is a condition with parts; it's met when the parts on your line are, and not before.

## Options: the cut line and the date

- **A. Everything by January 1.** The whole list, stickers and both email waves included. Misses on time almost surely; a holiday opening lands in shut shops and full inboxes.
- **B. Must-haves, open Wednesday January 6 (recommended).** Everything marked Must, plus the rules-only homepage, its words and the first email wave. The week of December 28 is a private dry run with a handful of invited testers, not the waitlist. Stickers, item tags and Google/Apple follow in January; AI chat, values and the map later. People are back at work, shops are open, and moderation isn't over Christmas.
- **C. The smallest open on January 1.** Today's front door plus "is my town open?" and phone sign-up; the chat-search homepage, emails and stickers follow in January. Opens on the date, but the campaign arrives after the opening it was meant to announce.

**Soft open in late December or open January 6–10?** January 6. A late-December soft open pulls every must-have forward by nine days and puts the first real sign-ups and reports over Christmas, when nobody is watching the queue. A private dry run that week gets most of the learning without the exposure.

## Checked against the rulings

- **Sign-up is phone first and zip-gated:** "is my town open?" is the same zip gate, said out loud.
- **No new paid tool before go-live:** Supabase Pro and Twilio are already your planned exceptions; stickers are new spend, so they wait for your yes.
- **Nothing a member contributes goes live without a report-and-takedown path:** screening and the safety package are must-haves.
- **Wealth circulates, it is never extracted:** the emails and stickers invite; no list is bought or sold.

## Precedents

- **Launching one town at a time:** [Nextdoor](https://en.wikipedia.org/wiki/Nextdoor) opened neighbourhoods with founding members; [Uber](https://en.wikipedia.org/wiki/Uber) and [DoorDash](https://en.wikipedia.org/wiki/DoorDash) opened city by city.
- **Stickers in shop windows:** [Yelp](https://en.wikipedia.org/wiki/Yelp)'s "People love us on Yelp" window clings and [Google's marketing kit](https://marketingkit.withgoogle.com/) stickers for Business Profiles.
- **Release slices and readiness:** [Jeff Patton's story mapping](https://jpattonassociates.com/wp-content/uploads/2015/03/story_mapping.pdf) (the walking skeleton opens first); [Google's launch checklists](https://sre.google/sre-book/reliable-product-launches/).
- **Sending to businesses:** the [FTC's CAN-SPAM guide](https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business): an honest subject, who we are, a working opt-out.

<details><summary>Ticket numbers behind the table</summary>

- Twilio: web #707. Phone sign-up: #1280, #1289, #1290, #1291. New accounts: #1292. Screening and safety: #1288, #1295. Invites: #616.
- Launch-blocking checks: #1376, #1377, #1118, #616 (F076); #1403, #1404 (F081); #1112 (F103); #1202–#1204 (F082); #1206 (F102); #220 (F078).
- Load and pool: #1346 (closed 11-22), #1269. Front door: #1328 (F136). Item tags: #1318.
- The story map: web #1416. Linking map steps to their conditions in the store: web #1418.

</details>
