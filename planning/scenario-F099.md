---
id: F099
title: Every post shows a picture, and every Page can have a Page picture
status: approved
date: 2026-10-05
depends: [F070, F072, F078, F080, F093]
approved: 2026-10-05 — Don's answers, "keep it simple": one Page picture for every kind; the kind placeholder when none is set; the beta slice, gallery after beta; one photo per post; today's Page photo stays the Page's photo and the Page picture starts empty. Same fields, flow and copy for every kind.
---
## Story

Maya's bakery sets a Page picture, a round loaf on blue. On Thursday she posts that the bread class is on and attaches a photo of the dough; it shows on that post and does not join her Page. Her Saturday "sourdough is back" post has no photo, so it shows her Page picture. The cycling group down the street hasn't set one, so its posts show the cycling-group placeholder, and anyone scanning Explore can tell a group from a shop at a glance. The steps, fields and words were the same for both.

## Acceptance

1. **Every Page, of every kind, may set one optional Page picture.** Same field, same flow, same copy for every kind. A Page without one publishes and shows as today.
2. **A Page with no Page picture shows its kind's placeholder image** (F070 criterion 4), identical on every load, to every viewer.
3. **A post may carry one photo of its own.** The composer completes without one; a second is refused.
4. **A post's photo belongs to that post only.** It does not appear on the Page as a Page photo.
5. **The Page picture and a post photo use the existing upload path:** WebP only, metadata stripped, the uploader's own folder, 5 MB at most, verified against the stored bytes, as F070 criteria 2 and 3.
6. **Every post card shows exactly one image**, on its Page, in browse and on Home: the post's visible photo; else the Page's visible Page picture; else the kind placeholder. No post card renders without an image.
7. **Visible means neither hidden nor removed, resolved in SQL,** so a hidden or removed URL does not reach the browser and the card falls to the next image in criterion 6.
8. **The Page picture and each post photo are reportable on their own** (F078). A report hides that one image only, and the poster's notice names which.
9. **Adding either image shows the sensitive-content ask at the moment of upload** (F080).
10. **Every rendered image has alt text.** Page picture and placeholder: the Page's name. Post photo: the owner's words, else the default built from title, date and place (F072 criterion 6).
11. **Signed out (F093), no post photo is in any response.** The Page picture or placeholder shows wherever the Page's name does; the withheld card is unchanged (2026-09-27).
12. **Removing either image records an event,** and it stops showing on every surface on the next load.
13. **A Page's current photo stays its photo, shown where it shows today.** The Page picture starts empty, so the placeholder shows on its posts until the owner sets one.

## Not this

More than one photo on a Page or a post, and any gallery: after beta, its own scenario. Reordering, captions, or cropping beyond F070's centre-crop. Video. A cover or banner. Photos added by visitors. Member avatars. Kind-specific fields or wording. Purging removed bytes (the accepted risk below).

## Why

**Don, 2026-10-05:** *"A page should have a logo option and a few photos. and then posts get at least one photo per post and perhaps a post has a logo from the page or an avatar if it isn't a business or doesn't have a logo and the post can have it's own image that will not necessarily be saved with on the page."* His answers the same day closed the four questions this draft raised: keep it simple; a logo and a Page avatar are one image, for every kind; no image means the kind's placeholder; the beta slice, gallery after; one photo per post; today's Page photo stays the Page's photo and the Page picture starts empty.

**The word is "Page picture",** one term for every kind. Facebook calls a Page's image its profile picture for businesses and groups alike ([help](https://www.facebook.com/help/284445998278828)); "logo" reads as business-only and "avatar" as a person. "Page picture" says whose picture it is in plain words, and is still draft copy ([public-is-draft]).

**Path: new territory.** It touches moderation, member trust and launch scope, and it moves two lines: F070's Not this no longer refuses a second image per Page, and F072's no longer refuses images. Both are amended in the same change.

### Precedent

- **Facebook Pages:** a profile picture shown on every post the Page makes ([profile picture](https://www.facebook.com/help/284445998278828), [cover](https://www.facebook.com/help/333543230019115)). The fallback from post to Page picture comes from here.
- **Google Business Profile:** a logo, a cover and business photos ([help](https://support.google.com/business/answer/6103862)). The gallery after beta comes from here.
- **Meetup:** one featured photo per event ([help](https://help.meetup.com/hc/en-us/articles/40378101429389-How-to-set-and-edit-an-event-s-cover-photo)). One photo per post comes from here.
- **Instagram:** 1 to 20 photos per post ([Social Media Today](https://www.socialmediatoday.com/news/instagram-expands-carousels-to-20-frames/723792/)). The upper bound, not a target.

### What changes against today (read in `socialus-web` main, 2026-10-05)

- **A Page has one photo:** `groups.photo_url`, hidden or removed through `groups.photo_hidden_at`, `photo_removed_at` and `photo_hide_locked_url`, read through `visiblePhotoUrl()` (`src/lib/groups/visible-photo-url.ts`). It stays the Page's photo. The Page picture is a second image with its own hide and remove state.
- **A post has no image column.** `browse_posts`, as first written (`20260914202752_page_posts.sql`), projects the Page's `groups.photo_url` onto each post. Criterion 6 replaces that projection with the Page picture.
- **The `media` bucket is reused unchanged** (`039_media_bucket.sql`). **`items.photo_url` (`036_item_photo_url.sql`) is not reused;** it belongs to the retired Item model.
- **`reports.subject_kind` started as `'group'` only**; F078 widens it, and criterion 8 needs the Page picture and a post photo as subjects.

### Interactions

- **Reports (F078):** a reported post photo hides and the post falls back to the Page picture; the post stays up unless reported itself.
- **Removed bytes stay fetchable (accepted risk, review due 2026-10-16):** post photos add images that can be removed yet stay downloadable by direct URL. Recommend the 10-16 review settles the purge path (`socialus-web` `docs/purge-proposal.md`) before post photos reach production.
- **Alt text:** F072 criterion 6 already asks for default alt text on a dated post's image; this gives it an image.
- **Signed out (F093):** posts are withheld, so their photos are too.

[platform photos: the owner picks a Page picture or a post photo from the library; each is resized and re-encoded to WebP on the device, as the Page photo is today]

### Size

**About 3 build days, in the beta (2026-10-30):** the Page picture and post-photo columns with their hide and remove state (half a day); the Page picture on Page edit and the photo step in the composer, with the ask and alt text (1 day); the fallback in every read that shows a post (1 day); per-image report and hide (half a day). The gallery, about 2 to 3 more days, follows after beta. The navy and gold palette stays in beta scope.

**Scope signal:** this is the fifth launch addition since 2026-10-01 with nothing removed. If beta tightens, the first candidates to push are Home's wildcard row and older-picks tap (F098 criteria 7 and 9), then the Badges & values section, then narrowing in a modal (F092).
