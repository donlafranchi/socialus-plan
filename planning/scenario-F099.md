---
id: F099
title: Every post shows a picture, and a Page has a logo and a few photos
status: draft
date: 2026-10-05
depends: [F070, F072, F078, F080, F093]
---
## Story

Maya's bakery Page has a logo, a round loaf on blue, and four photos: the counter, the oven, Saturday's line, the sourdough. On Thursday she posts that the bread class is on and attaches a photo of the dough; it shows on that post and does not join her Page's photos. Her Saturday "sourdough is back" post has no photo, so it shows her logo. The cycling group down the street has no logo, so its posts show its own default face. Signed out, a stranger sees the bakery's logo and first photo, and the card saying there is more inside.

## Acceptance

1. **A Page may carry one optional logo, separate from its photos.** A Page without one publishes and shows as it does today.
2. **A Page holds up to 6 photos.** A 7th upload is refused with words that say the limit. The owner removes any one in one action; photos show in upload order.
3. **Every logo, Page photo and post photo uses the existing upload path:** WebP only, metadata stripped, the uploader's own folder, 5 MB at most, verified against the stored bytes, as F070 criteria 2 and 3.
4. **A post may carry its own photo, up to the per-post limit the open question below settles.** The composer completes without one.
5. **A post's own photo belongs to that post only.** It does not appear in the Page's photos and does not count toward the 6.
6. **Every post card shows exactly one lead image**, on its Page, in browse, on Home and on the signed-in card: the post's first visible photo; else the Page's visible logo; else the Page's default face (F070 criterion 4). No post card renders without an image.
7. **Visible means neither hidden nor removed.** A hidden post photo falls back to the logo; a hidden logo falls back to the face. Resolved in SQL, so a hidden or removed URL does not reach the browser.
8. **Each logo, Page photo and post photo is reportable on its own** (F078). A report hides that one image only, and the poster's notice names which image.
9. **Adding any photo shows the no-pictures-of-children ask at the moment of upload** (F080).
10. **Every rendered image carries alt text.** A logo: "<Page name> logo". A post photo: the owner's words, else the default built from title, date and place (F072 criterion 6). A Page photo: the owner's words, else "Photo from <Page name>". The default face is decorative.
11. **Signed out (F093), a visitor sees a Page's logo or face and its first photo only.** No post photo and no other Page photo is in a signed-out response. The withheld card shows the first photo, else the logo, else the face.
12. **Removing a photo from a Page or a post records an event,** and the image stops showing on every surface on the next load.
13. **Every Page that has a photo today still shows it after the change,** placed as the open question below settles.

## Not this

Reordering, captions, or cropping beyond F070's fixed centre-crop. Video. A cover or banner separate from the logo. Albums. Photos added by visitors to someone else's Page. Member avatars. More than one image on a card. Purging removed bytes (the accepted risk below).

## Why

**Dispatch's reading of Don's request (2026-10-05); Don can correct it.** Don: *"A page should have a logo option and a few photos. and then posts get at least one photo per post and perhaps a post has a logo from the page or an avatar if it isn't a business or doesn't have a logo and the post can have it's own image that will not necessarily be saved with on the page."* Read as: a Page gets an optional logo and a small gallery; every post shows an image, its own if attached, else the Page's logo, else the Page's default face; a post's own photo stays with the post. **"Avatar" is read as the Page's default face (F070), not the founder's member avatar:** the front door currently does not show the founder, and nothing writes `members.avatar_url`.

**Path: new territory.** It touches moderation, member trust and launch scope, and it reverses two lines: F070's Not this ("Multiple images per Page") and F072's Not this ("Images"). Approval needs a dated `DECISIONS.md` line naming both.

### Precedent

- **Google Business Profile:** a logo, a cover photo, and business photos, three separate kinds ([help](https://support.google.com/business/answer/6103862)). The logo-plus-gallery shape comes from here.
- **Facebook Pages:** a profile picture that shows on every post the Page makes, plus a cover ([profile picture](https://www.facebook.com/help/284445998278828), [cover](https://www.facebook.com/help/333543230019115)). The fallback from post to Page picture comes from here.
- **Meetup:** one featured photo per event, set in the create flow ([help](https://help.meetup.com/hc/en-us/articles/40378101429389-How-to-set-and-edit-an-event-s-cover-photo)). The basis for one photo per post at beta.
- **Instagram:** 1 to 20 photos per post ([Social Media Today](https://www.socialmediatoday.com/news/instagram-expands-carousels-to-20-frames/723792/)). The upper bound, not a target.
- **The cap of 6 is ours, not a precedent's:** none of these caps a business gallery that low. Every image is something Don may have to review (F078), and 6 keeps that and the page weight small.

### What changes against today (read in `socialus-web` main, 2026-10-05)

- **A Page has one photo:** `groups.photo_url`, hidden or removed through `groups.photo_hidden_at`, `photo_removed_at` and `photo_hide_locked_url`, read through `visiblePhotoUrl()` (`src/lib/groups/visible-photo-url.ts`). Those columns are per Page, so hiding one image of several needs a row per image.
- **A post has no image column.** `page_posts` carries body, time, place and state; `browse_posts`, as first written (`20260914202752_page_posts.sql`), projects the Page's `groups.photo_url` onto each post. Criterion 6 replaces that projection.
- **The `media` bucket is reused unchanged** (`039_media_bucket.sql`): public read, WebP only, 5 MB, own-folder writes.
- **`items.photo_url` and `item_products.photo_urls` (`036_item_photo_url.sql`) are not reused.** They belong to the retired Item model; item-level photos stay in `ROADMAP.md` § Later.
- **`reports.subject_kind` started as `'group'` only** (`20260913211209_reports_and_photo_hiding.sql`); F078 widens it, and criterion 8 needs a subject per image.

### Interactions

- **Reports and hiding (F078):** a report on a post photo hides the photo and the post falls back to the logo; the post itself stays up unless reported.
- **Removed bytes stay fetchable (accepted risk, review due 2026-10-16):** this multiplies the images that can be removed yet stay downloadable by direct URL, and post photos are the likeliest place for a bad one. Recommend the 10-16 review settles the purge path in `socialus-web` `docs/purge-proposal.md` before post photos reach production.
- **Alt text:** F072 criterion 6 already asks for default alt text on a dated post's image; this gives it an image to attach to.
- **Signed-out front door (F093):** posts are withheld signed out, so their photos are too; the Page's first photo stands in for the single photo F093 shows today.
- **Native apps:** picking and taking photos needs the `photos` and `camera` platform needs; the markers go on at approval.

### Size, and whether it fits before beta (2026-10-30)

**About 5 to 6 build days for Code, honestly sized:** image rows for Pages and posts plus a carry-over of today's photo (1 day); logo and 6-photo upload and remove on Page edit (1 day); the composer photo step with the children ask and alt text (1 day); the fallback resolver in every read that shows a post, signed in and out (1 day); per-image report, hide and notice wired into F078 (1 day); tests (half to 1 day).

**Scope signal: launch scope keeps growing with nothing leaving.** Home rows (F098), Page kinds and badges, tags on posts, and end time with add-to-calendar all entered `ROADMAP.md` § Next marked "nothing was removed to make room". This is another, 25 days out.

**A beta slice fits about 3 days:** the logo, one photo per post, and the fallback (criteria 1, 3 to 10 without the gallery, 12). The gallery (criterion 2, and 11's first photo) follows after beta.

**If beta is tight, this would push, in this order (the navy and gold palette stays in scope):**
1. The Page gallery itself, the slice above.
2. Home's wildcard row and the older-picks tap (F098 criteria 7 and 9); Tonight, This weekend and the stop card stay.
3. The Badges & values section on Pages; the kind line stays.
4. Narrowing in a modal that writes text (F092).

[open-question owner=don raised=2026-10-05] How much of this goes into the beta on 2026-10-30?
A) **Slice (recommended):** logo, one photo per post, and the fallback in beta; the gallery after. About 3 days, and every post has a picture on day one.
B) All of it in beta, about 5 to 6 days, pushing item 1 to 3 of the list above.
C) All of it after beta; posts keep showing the Page's single photo as today.

[open-question owner=don raised=2026-10-05] How many photos may one post carry?
A) **One (recommended),** as Meetup's featured photo. Simplest composer, one image per card, least to review.
B) Up to 4. A small set, still one lead image on the card.
C) Up to 10 or more, as Instagram. Needs a carousel, which Not this excludes.

[open-question owner=don raised=2026-10-05] Which Page kinds get a logo?
A) **Every kind (recommended):** a cycling club has a logo as often as a shop; any Facebook Page has a profile picture. Kinds without one show their face.
B) Businesses only; groups always show their face. Matches "if it isn't a business" literally.

[open-question owner=don raised=2026-10-05] Where does a Page's current single photo go?
A) **It becomes photo 1 of the gallery; the logo starts empty (recommended).** Today's photos are of places and things, like F070's counter.
B) It becomes the logo. Posts gain a picture at once, but a counter photo makes a poor logo.
C) The owner chooses on their next edit; until then it stays photo 1.
