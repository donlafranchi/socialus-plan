# Phone sign-up and the anti-bot layers: vendor facts and precedents

**As of 2026-11-12** · Evidence behind F081 criteria 1, 9, 11–16, F102 criteria 15–16 and F078 criterion 5 · Maintained by: hand (research; pruned when the build ships)

## Vendor facts (checked in the vendors' own docs, 2026-11-12)

| Fact | Source |
|---|---|
| Lookup Line Type Intelligence returns `mobile`, `landline`, `fixedVoip`, `nonFixedVoip`, `personal`, `tollFree`, `premium`, `sharedCost`, `uan`, `voicemail`, `pager`, `unknown`. Google Voice and Enflick (TextNow) are named as `nonFixedVoip`. | [Twilio docs](https://www.twilio.com/docs/lookup/v2-api/line-type-intelligence) |
| Lookup costs $0.008 a check. | [pricing](https://www.twilio.com/en-us/lookup/pricing) |
| Lookup before the code, refusing VoIP, is Twilio's own pattern: two calls, not a Verify setting. | [Twilio blog](https://www.twilio.com/en-us/blog/filter-voip-before-otp-verification) |
| Verify: $0.05 per successful verification plus the US SMS fee ($0.0083), about $0.058. A managed number pool is included; no number to buy. Fraud Guard is included. | [pricing](https://www.twilio.com/en-us/verify/pricing) |
| Verify needs no A2P 10DLC brand or campaign registration. | [Twilio 10DLC docs](https://www.twilio.com/docs/messaging/compliance/a2p-10dlc/direct-sole-proprietor-registration-overview-new-experience) |
| Fraud Guard blocks prefixes that look like SMS pumping (error 60410); levels Basic, Standard (default), Max; chosen when the service is created. | [Fraud Guard](https://www.twilio.com/docs/verify/preventing-toll-fraud/sms-fraud-guard) |
| Geo Permissions allow or block each country per channel, immediately. | [Geo Permissions](https://www.twilio.com/docs/verify/preventing-toll-fraud/verify-geo-permissions) |
| Supabase phone sign-in has a Twilio Verify provider, separate from plain Twilio. | [Supabase](https://supabase.com/docs/guides/auth/phone-login) |
| Supabase sends at most 30 texts an hour per project by default (adjustable); one code request a minute per number; verify is limited to 30 tries per 5 minutes per IP. | [rate limits](https://supabase.com/docs/guides/auth/rate-limits) |
| Supabase sessions never expire by default (1-hour access tokens, single-use refresh tokens). Time-boxing and inactivity timeouts are Pro features we don't need. | [sessions](https://supabase.com/docs/guides/auth/sessions) |
| A signed-in member can add an email later with `updateUser({ email })`. | [Supabase](https://supabase.com/docs/reference/javascript/auth-updateuser) |
| Supabase supports Cloudflare Turnstile natively; Turnstile's free plan is unlimited. | [Supabase CAPTCHA](https://supabase.com/docs/guides/auth/auth-captcha), [Turnstile plans](https://developers.cloudflare.com/turnstile/plans/) |
| SMS pumping: Twilio's guidance. | [anti-fraud guide](https://www.twilio.com/docs/usage/anti-fraud-developer-guide) |

**About $0.066 per new sign-up** (Lookup plus one code); a returning member on the same device costs nothing.

## Not confirmed

- How Lookup classifies ported and prepaid numbers. Prepaid mobiles should read `mobile`; watch refusals after launch.
- Whether Supabase's built-in CAPTCHA covers `signInWithOtp` for phone. If it doesn't, the server checks the Turnstile token itself (Cloudflare `siteverify`) before sending, which is criterion 12 either way.
- Verify has no single "US only" switch: untick every other country.

## Precedents

- **Craigslist:** a code by text before posting; refuses VoIP and international numbers; one account per number; one code request every 5 minutes. [help](https://www.craigslist.org/about/help/posting/verify/phone)
- **Signal, WhatsApp:** the phone number is the account. Signal added usernames (2024) so the number need not be shown. [TechCrunch](https://techcrunch.com/2024/03/04/why-signal-turned-our-architecture-inside-out-for-its-latest-privacy-feature)
- **New-account limits:** Facebook Marketplace and Reddit limit new accounts but publish no numbers (third-party reports only). F102's starting values (3 posts and 10 first messages a day for 7 days) are set low enough to stop a fresh bot and high enough that a real new member rarely meets them; tune from what we see.

## Corrections to the 2026-11-12 brief to this session

- "No Twilio number to buy" holds for sign-in codes, and Verify also removes the 10DLC registration the old steps required. Two things used a number: the urgent-report alert to the PM (moves to its built email fallback, F078) and Page claim codes by text (move to Verify, #1280).
- Fraud Guard's default level is Standard; we keep it.
- "Real mobile only" is stricter than the 2026-10-05 ruling (which refused `nonFixedVoip` only): landlines, fixed VoIP and `unknown` are refused too.
