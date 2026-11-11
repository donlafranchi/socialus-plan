---
id: research-storyboard-owners-create-edit-2026-10-11
purpose: Every join, create, edit and composer screen the owner wording touches, at phone width, with the draft copy under each shot, for Don's review before anything goes public.
layer: research
status: draft
authored: Claude agent, 2026-10-11, at Don's request (copy report §10)
---

# Storyboard: owners, creating, editing and joining (2026-10-11)

**Draft, not shipped.** Every line of copy here is a draft on a branch (branch `copy/owners-create-edit-draft`, draft PR [socialus-web#692](https://github.com/donlafranchi/socialus-web/pull/692), not merged). Don reviews it in context first. Phone width (390px), a local database seeded with test members, so names like "QA Corner Bakery" are test data. The dev server's round "N" badge is hidden in these shots; it is not part of the app.

The product, service and gathering composers and the old Page walkthrough are kept but not linked from the app today (the /you/sell route redirects to Create). They were shown through a throwaway dev page with stub saves, not committed, so the words are real and nothing was saved. The report's 41 changes are all applied.

## Things you will notice (need your call)

1. **Legal flags.** 10.1 and 10.2 drop the "no charge to create a Page" lines entirely (the report's proposal), so the old claim is gone; counsel should confirm it is out. 10.36 changes "gone for good" to "it can't be restored" after 14 days, which is still a hard promise about deleting data; counsel should confirm retention matches. Nothing else was added.
2. **Two places in the same sheets still say the old words** (not in the report): the add-a-place drawer still has the field label "Location name" and the error "Name is required" (shots 9, 10 and 35), and the map credit line still spells "Neighbourhoods:" (shot 10). Options: A) add them to this pass ("Place name", "Add a name.", "Neighborhoods:"); B) leave them. The credit line sits next to a dated ruling about visible credit, so it may want your eye.
3. **The service pricing error was not in the report.** Shot 32 shows "Enter a rate, or mark it free" while the product one became "Add a price, or mark it free." (10.27). Say the word and the service one becomes "Add a rate, or mark it free."
4. **"This photo has no children in it."** shows twice on the Basics sheet and once in the walkthrough's About step (shots 12 and 44). It is not in §10; flagging it because it sits right next to the new photo error.
5. **Photo error wording** (shot 44): "That photo didn't upload. That file is not a readable image. Mind trying again? You can also go on without one." The middle sentence is the existing upload message; the §6 draft (web#688) rewrites it ("That file doesn't look like a photo."), so the two drafts compose cleanly once both land. When there is no reason to give, the line is "That photo didn't upload. Mind trying again? You can also go on without one." (the report only gave the with-reason form).
6. **I also stripped the code prefix** from the two "links could not be read" / "not https" edit errors and the opening-hours error, since they have the same "group.update:" prefix as the lines the report names (10.34). Easy to back out if you want only the named ones.
7. **Not pictured, applied on the branch:** the two error lines in Create (10.5) and the publish checklist (10.8) and the composer fallbacks (10.9, 10.10), which only show when a save fails for no known reason. The publishing messages (10.6, 10.7) cannot be shown because the Publish button stays off until every item is done, so a person never sees them; they are applied. Typing the wrong name to delete (10.35) is also blocked by the button, so it is applied only. The "Untitled place" label (10.13) and the "Locally Made" claim lines (10.24 and 10.25, shown in shots 27 and 28) were shown where reachable. The accessibility labels (10.11 "Create something", the "Place options" lists in 10.14) are not visible on screen.

## 1. /join, signed out

![/join, signed out](owners-create-edit-2026-10-11/01-join-signed-out.png)

Copy on this screen (10.1 to 10.4):

> Start a Page
> Run a shop or a group? Get a Page.
> SocialUs helps people find you any day of the week.
> Sign up and start a Page
> Easy to follow: People who liked what you made on Saturday can find you again on Wednesday.
> People who keep it local: People here already like keeping it local. You're not pitching strangers. You're getting introduced.
> Sign up: Use your email. It takes a minute.
> Tell people who you are: Your name, a line about what you do, and where to find you.
> Your Page goes live: People can find it on Explore and the map.
> People follow you: They get your updates in the app. No more "what was that stall called?"
> Start my Page
> Share this page: Know someone who should be on here? Send them this link.

The "no charge" card is gone, so there are two benefit cards (see "Things you will notice", 1).

## 2. /join, signed in

![/join, signed in](owners-create-edit-2026-10-11/02-join-signed-in.png)

Copy on this screen:

> Create my Page

Everything else is as above.

## 3. Create: What are you starting?

![Create: What are you starting?](owners-create-edit-2026-10-11/03-create-what-are-you-starting.png)

Unchanged on screen. Its failure line, "That didn't go through. Mind trying again?", is not pictured (see 7).

## 4. A new Page, before publishing

![A new Page, before publishing](owners-create-edit-2026-10-11/50-draft-page.png)

Unchanged. The Publish button stays off until the four things are done, so the publish error lines (10.6, 10.7) are applied but cannot show.

## 5. Page walkthrough: first question

![Page walkthrough: first question](owners-create-edit-2026-10-11/04-walk-purpose.png)

![Page walkthrough: first question, nothing picked](owners-create-edit-2026-10-11/05-walk-purpose-error.png)

Copy on this screen:

> Pick one first.

## 6. Page walkthrough: name

![Page walkthrough: name, left empty](owners-create-edit-2026-10-11/06-walk-name-error.png)

Copy on this screen:

> Add a name.

## 7. Page walkthrough: Where is it?

![Page walkthrough: Where is it?](owners-create-edit-2026-10-11/07-walk-where-is-it.png)

![Page walkthrough: Where is it? nothing picked](owners-create-edit-2026-10-11/08-walk-where-error.png)

Copy on this screen:

> Where is it?
> + Add a new place
> Pick a place or add one

## 8. Add a place drawer

![Add a place drawer](owners-create-edit-2026-10-11/09-add-a-place-drawer.png)

![Add a place drawer, neighborhood, nothing chosen](owners-create-edit-2026-10-11/10-add-a-place-errors.png)

Copy on this screen:

> Add a place
> Signed-in visitors see this address. Rather not? Give a neighborhood instead.
> Rather give a neighborhood?
> Neighborhood or town
> Or tap your neighborhood on the map.
> Only the neighborhood shows to visitors, with its pin at the center.
> Choose a neighborhood

(The labels "Location name" and "Name is required" and the credit line are old; see 2 above.)

## 9. Page walkthrough: tags, About and review

![Tags, nothing added](owners-create-edit-2026-10-11/11-walk-tags-error.png)

![About step](owners-create-edit-2026-10-11/12-walk-about.png)

![Review](owners-create-edit-2026-10-11/13-walk-review.png)

Copy on these screens:

> Add at least one word for what you do.
> A short description anyone can read (optional).
> Name: Maya's Bakery
> Place: QA Corner Bakery

## 10. Host a gathering

![Kind step](owners-create-edit-2026-10-11/14-gather-kind.png)

![Kind step, nothing picked](owners-create-edit-2026-10-11/15-gather-kind-error.png)

![Details, left empty](owners-create-edit-2026-10-11/16-gather-details-errors.png)

![When, open meetup](owners-create-edit-2026-10-11/17-gather-open-meetup-when.png)

![When, one-time event](owners-create-edit-2026-10-11/18-gather-one-time-when.png)

![When, nothing picked](owners-create-edit-2026-10-11/19-gather-when-error.png)

![When, a date in the past](owners-create-edit-2026-10-11/20-gather-past-error.png)

![When, end before start](owners-create-edit-2026-10-11/21-gather-end-before-start.png)

![Review](owners-create-edit-2026-10-11/22-gather-review.png)

Copy on these screens:

> Drop in anytime. No fixed schedule.
> Pick which kind it is.
> Add a title. / Add a description.
> Open meetups have no fixed schedule. People drop in whenever. You can add times later from the gathering page.
> Cost (optional, leave blank if free)
> Pick a date and time.
> Pick a time that's still ahead.
> The end time needs to come after the start.
> Where: (no place yet)

## 11. Add a product

![Details](owners-create-edit-2026-10-11/23-product-details.png)

![Details, left empty](owners-create-edit-2026-10-11/24-product-details-errors.png)

![Pickup](owners-create-edit-2026-10-11/25-product-pickup.png)

![Pickup, nothing picked](owners-create-edit-2026-10-11/26-product-pickup-error.png)

![Where is this made?](owners-create-edit-2026-10-11/27-product-made.png)

![Review](owners-create-edit-2026-10-11/28-product-review.png)

Copy on these screens:

> Add a title. / Add a description. / Add a price, or mark it free.
> Pick a pickup spot or add one.
> Say where it's made if you like. You can skip this and add it later from the product page.
> This part isn't ready yet. Skip it for now and you can add it later.
> Locally Made: not yet

## 12. Add a service

![Details](owners-create-edit-2026-10-11/29-service-details.png)

![Details, left empty](owners-create-edit-2026-10-11/30-service-details-errors.png)

![Pricing](owners-create-edit-2026-10-11/31-service-pricing.png)

![Pricing, no rate](owners-create-edit-2026-10-11/32-service-pricing-error.png)

![Service area](owners-create-edit-2026-10-11/33-service-area.png)

![Service area, nothing picked](owners-create-edit-2026-10-11/34-service-area-errors.png)

![Add a place from the service area](owners-create-edit-2026-10-11/35-service-add-a-place.png)

![Review](owners-create-edit-2026-10-11/36-service-review.png)

Copy on these screens:

> Piano lessons, 30 min (the title hint)
> How you charge
> Where do you offer this? Pick a starting place and how far you travel.
> Pick a place or add one. / Add how far you travel, in miles.
> Starting place: QA Corner Bakery
> Pricing: Per hour, 45 (comma instead of the dash)

## 13. Edit a Page

![Edit a Page](owners-create-edit-2026-10-11/40-edit-page.png)

Copy on this screen (10.37):

> Values & badges / Not here yet.
> A place to show what you're about and what you stand for.

## 14. Delete a Page

![Delete a Page](owners-create-edit-2026-10-11/41-delete-sheet.png)

Copy on this screen (10.36, legal flag in 1):

> QA Corner Bakery and its posts disappear for everyone right away. You can restore it from You until October 25. After that, it can't be restored.

## 15. Edit errors

![A bad phone number](owners-create-edit-2026-10-11/43-phone-error.png)

![A photo that will not upload](owners-create-edit-2026-10-11/44-photo-error.png)

![Saving after the session ended](owners-create-edit-2026-10-11/45-save-signed-out.png)

Copy on these screens (10.32, 10.34, 10.41):

> Enter a US phone number, like (916) 555-0142.
> That photo didn't upload. That file is not a readable image. Mind trying again? You can also go on without one.
> Sign in and try again.

The "Sign in and try again." shot was captured by clearing the cookies under an open sheet, the way a session expiring in another tab would look.

## 16. Where it is, in a Page's edit

![Where it is: how people find you](owners-create-edit-2026-10-11/51-edit-location-sheet.png)

![Where it is: neighborhood picked](owners-create-edit-2026-10-11/53-edit-location-neighborhood-picked.png)

Copy on these screens (10.38, 10.39):

> Or type a neighborhood
> Show only my neighborhood
> Visitors see Curtis Park, with its pin at the center, not your address.
