# Phone check: tying a member to a real mobile number

**It's already built and switched off. Signup has a "Verify your phone" step that texts a code and refuses internet numbers like Google Voice. It's waiting on the Twilio keys you owe (web #707). It's already ruled to happen at signup (2026-10-01). Your 10-31 note gives it a new reason, accountability, which raises one question: when to ask.**

**Your one call:** when the check is required (A, B or C, at the bottom). I recommend **B: before a member's first post, message, claim or report.**

*The PM, 2026-10-31:* "I think we are going to add a phone number check. I want to be able to tie a person to their actual phone number in case anyone wants to do anything harmful or disruptive."

**Path: new territory.** It touches privacy, member trust and a new recurring cost. Research only; nothing changes until you pick.

## 1. What's in the code today

- **Built (F081), behind one switch** that's off: `PHONE_VERIFICATION_REQUIRED`.
  - Onboarding asks for the phone after the email code. Builder accounts skip it.
  - The words are written: "Verify your phone", then "Everyone here is a real person. We'll text you a code to check. Your number is never shown to anyone."
  - Before any code is sent, a lookup refuses internet numbers (Google Voice and the like). It asks for "a mobile number" instead (ruled 2026-10-05).
- **Waiting on you** (web #707): the Twilio account keys in Vercel, and Twilio as the phone provider in Supabase.
  - The VoIP lookup is a stub until those keys exist, and it never blocks anyone when Twilio is down.
- **Sign-in doesn't change.** It stays email then code (ruled 2026-10-18). The phone is a one-time check. Supabase records when it was confirmed, and the member never signs in with it.
- **Not built:**
  - One account per number, which is how a banned person is kept from coming back.
  - A staff view of the number.
  - A re-check when a member changes their number.

## 2. What other apps do

**Apps that use the phone as an accountability check ask at the first action others can see, not at signup. Apps where the phone is the account ask at signup. None of them shows the number to other users.**

| App | When they ask | VoIP numbers | Shown to others |
|---|---|---|---|
| **Craigslist** | Only for some posts, as a trigger | Refused; one account per number | No |
| **Airbnb** | Before a host's first listing or a guest's first booking | Unconfirmed | Only to the other party after a booking is confirmed |
| **Nextdoor** | At signup, as one way to verify your address (a postcard is the other) | Unconfirmed | Unconfirmed |
| **WhatsApp** | At signup; the number is the account | Refused | It's the account |
| **Signal** | At signup; the number is the account | Not evidently blocked | Hidden by default since usernames (2024) |
| **Bumble / Hinge** | At signup | Reported refused (blogs only) | Unconfirmed |
| **Uber** | At signup (unconfirmed) | Fails inconsistently (forum reports) | No: calls between rider and driver are masked |

**What they tell people:** Craigslist only warns that anyone asking for your code outside the posting step is a scammer. Airbnb says the number keeps your account safe. Signal says you can connect with people without sharing your number. We already say "never shown to anyone", which is stronger than any of them.

<details><summary>Sources and gaps</summary>

- [Craigslist: phone verification](https://www.craigslist.org/about/help/posting/verify/phone)
- [Airbnb help 277](https://www.airbnb.com/help/article/277)
- [Signal: phone number privacy and usernames](https://signal.org/blog/phone-number-privacy-usernames/)
- [Signal support: deeper dive](https://support.signal.org/hc/en-us/articles/6829998083994-Phone-Number-Privacy-and-Usernames-Deeper-Dive)
- [Uber: phone anonymisation](https://www.uber.com/in/en/newsroom/keep-your-number-private-with-phone-anonymisation/)
- [Bumble: verifying your phone number](https://support.bumble.com/hc/en-us/articles/28949524382877-Verifying-your-phone-number) (the page returned 403)
- [Nextdoor verification (third-party guide)](https://gethuman.com/customer-service/Nextdoor/faq/How-does-Nextdoor-verify-members/tJzp49)

Nextdoor's, Bumble's, Hinge's and Uber's own help pages couldn't be loaded, so those cells are marked unconfirmed. Check the live apps before copying a detail.

</details>

## 3. Privacy fit

**Member to member: strict. The number is never shown to any member, on any surface.** This keeps the 2026-10-05 ruling: legal name, email and phone are seen only by operators.

**Member to staff, as needed:**
- **What staff see:** the number and when it was verified, on an operator-only member view. It's never listed or exported in bulk.
- **When it's used:**
  - **Repeat or harmful reports:** a removed member can't sign up again with the same number.
  - **Valid legal process:** the 2026-10-01 ruling says we disclose only for that.
  - **Threat of harm reports:** the existing operator text path (F078) is unchanged.
- **Never used for:** marketing, texts other than the code, matching members to each other, or anything a member sees.
- **Retention:** it's already in the legal starter kit as "life of the account plus 4 years". That's for counsel to confirm (§5).

## 4. Cost: a new recurring cost

**About $66 a month at 1,000 checks, and about $660 at 10,000. Each check is about 6.6 cents.** Beta volume is likely to stay well under 1,000 a month.

| Provider | Per check | Notes |
|---|---|---|
| **Twilio Verify + Lookup (built for)** | ~$0.066: $0.05 verify + $0.0083 SMS + $0.008 VoIP lookup | Failed checks still pay the SMS. Already wired into the code and into the Terms draft ("Twilio Verify, toll-free") |
| Vonage Verify | ~$0.057 plus the SMS | No VoIP lookup included |
| AWS SNS / End User Messaging | Cheapest per text, but the price isn't published (it's a CSV) | We'd build the code logic ourselves. About $17 one-time registration, plus $2–10 a month |
| Supabase phone providers | Twilio, Twilio Verify, MessageBird, Vonage, Textlocal | Built for signing in with a phone. We only use it to send the one code |

**Recommendation on provider: stay with Twilio** (well-worn, already built). It costs nothing until it's switched on. Asking at B instead of A cuts the cost to members who actually post.

<details><summary>Sources</summary>

- [Twilio Verify pricing](https://www.twilio.com/en-us/verify/pricing)
- [Twilio Lookup pricing](https://www.twilio.com/en-us/user-authentication-identity/pricing/lookup)
- [Twilio Line Type Intelligence](https://www.twilio.com/docs/lookup/v2-api/line-type-intelligence)
- [Vonage Verify charges](https://api.support.vonage.com/hc/en-us/articles/14842100202268-What-are-the-charges-for-using-Verify-API-V2)
- [AWS SNS SMS pricing](https://aws.amazon.com/sns/sms-pricing/)
- [Supabase phone login](https://supabase.com/docs/guides/auth/phone-login)

</details>

## 5. Legal: for counsel, not for you

The questions for counsel are in the legal repo: whether TCPA consent wording is needed for a one-time code, the CCPA notice, retention, and using the number to stop a removed member from returning. The starter kit already covers most of this. Nothing here needs a call from you.

## Your call: when the check is required

- **A — At signup, for everyone (ruled 2026-10-01; built).** Everyone is accountable from day one, but every browser pays the friction and the cost, while we're trying to reach 1,000 supporters per market.
- **B — Before a member's first post, message, Page claim, Wonder or report (Craigslist, Airbnb).** Ties the number to every action that can harm someone, and browsing, following and saving stay free of friction.
- **C — Only on a trigger: a report against them, or a removal (Craigslist's "some postings").** Least friction and cost, but a bad actor's first harmful post comes before any check.

**Recommend B.** It's the accountability pattern Craigslist and Airbnb use, it covers every action that could harm someone, and it keeps signup at what it is today. In code, it moves an existing gate; nothing new gets built.
