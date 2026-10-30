---
id: lifecycle-emails-2026-10-26
title: Lifecycle emails, reference copy
status: reference
date: 2026-10-26
---

# Lifecycle emails, reference copy

**Reference only: nothing here turns a send on or changes one.** This is Don's copy as given on 2026-10-26. Building or changing a send is separate work, with its own ticket. Landing copy these match: `landing-copy-draft5-2026-10-26.md`.

## Working rules

Short, useful, warm. Say what happened, give the useful detail, offer one next step. No guilt about being away, manufactured urgency, follower hype or promises of friendship. Never sign as Don. Sender display name: SocialUs (sending and reply-to addresses not set yet). Square brackets are data fields.

## 1. First signup

- **Subject:** Welcome to SocialUs
- **Preview:** Find people, places, and something worth showing up for.
- **Body:**
  > You're all set. Welcome to SocialUs.
  >
  > Find groups and events around your interests. Get to know the local places and people behind them. Or bring people together around something you care about.
  >
  > If you're in Sacramento, see what's happening nearby.
- **Button:** Explore SocialUs
- **Outside-market last paragraph:** "We're not open in [area] yet. You can still join. If enough people there join, we could open yours next."

## 2. Coming back

Optional, after sign-in; not an inactivity campaign.

- **Subject:** Welcome back to SocialUs
- **Preview:** Pick up where you left off.
- **Body:**
  > Welcome back.
  >
  > A familiar place. A new group. Something you've been meaning to get going.
  >
  > Come back to SocialUs and see what you want to be part of.
- **Button:** Open SocialUs

## 3. Weekly gathering reminder

Only for people who chose a recurring reminder; use the next occurrence.

- **Subject:** [Gathering name] is coming up
- **Preview:** [Day, date] at [time] · [place]
- **Body:**
  > Your reminder for [gathering name].
  >
  > [Day, date] at [time and time zone]
  > [Venue or meeting place]
  > [Address, if available]
  >
  > You asked for a reminder each time. Here are the details for the next gathering.
- **Button:** View gathering
- No RSVP or reserved-place claims.

## 4. "Remind me" follow-up

When a one-time reminder is due.

- **Subject:** Your reminder: [event name]
- **Preview:** [Day, date] at [time] · [place]
- **Body:**
  > You wanted a reminder about [event name].
  >
  > [details]
  >
  > Take a look at the details before you head out.
- **Button:** View event

## 5. New follower

To the Page owner.

- **Subject:** Someone new is following [Page name]
- **Preview:** [Display name] followed your Page.
- **Body:**
  > [Display name] is now following [Page name].
  >
  > Another person interested in what you're doing.
  >
  > Keep your Page current with what's coming up.
- **Button:** View your Page
- **Privacy fallback:** subject "Your Page has a new follower"; body opens "Someone new is following [Page name]."

## 6. Wonder: someone taps "I'm in"

To the creator.

- **Subject:** [Wonder name] has someone new in
- **Preview:** [Display name] is in.
- **Body:**
  > [Display name] tapped "I'm in" on [Wonder name].
  >
  > [Current count] of [goal count] people are in.
  >
  > Take a look at how it's coming along.
- **Button:** View Wonder

## 7. Wonder: goal reached

To the creator, once.

- **Subject:** [Wonder name] reached its goal
- **Preview:** The goal you set has been reached.
- **Body:**
  > [Wonder name] reached its goal.
  >
  > [Goal summary]
  >
  > The interest is there. What happens next is up to you.
- **Button:** View Wonder

## 8. Sign-in code

- **Subject:** Your SocialUs sign-in code
- **Preview:** Use this code to sign in to SocialUs.
- **Body:**
  > [6-digit code]
  >
  > Enter this code to continue to SocialUs.
  >
  > If you didn't request it, you can ignore this email.
- Don't invent an expiry; the code stays as live text.

### The live sign-in email differs (unchanged until Don OKs wording)

This one is already sending (socialus-web `supabase/templates/magic-link.html`; a near-copy, `confirmation.html`, goes to first-time sign-ups).

| | Live now | This copy |
|---|---|---|
| Subject | Your SocialUs sign-in code | same |
| Preview | none set | "Use this code to sign in to SocialUs." |
| Above the code | "Your SocialUs code:" | nothing; the code leads |
| After the code | "Enter it on the sign-in screen." (first sign-up: "…to finish.") | "Enter this code to continue to SocialUs." |
| Sign-in link | "Or tap here to sign in. The code and the link work in any browser or app, and only once." | no link |
| Ignore line | "If you didn't ask for this, ignore this email." | "If you didn't request it, you can ignore this email." |
| Expiry | not stated | not stated |

Don's call: dropping the tap-to-sign-in link removes a way in that works across browsers and apps, so keep it unless he wants it gone. The password-code email (`recovery.html`) has no counterpart here.

## Before any of these go live

- Pick reminder timing.
- Dedupe one-time vs recurring reminders.
- Re-check event status before sending.
- Confirm recipients and identity visibility.
- Every button goes to a real destination.
- The recipient's local time, with time zone.
- Footer, privacy and unsubscribe per the email provider.
- Keep marketing separate from codes and reminders.
