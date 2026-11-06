# One strike for taking advantage: research, 2026-11-06

Research only; nothing here is ruled. Don, verbatim:
- *"a new kind of policy that says, we are not putting up with any nonsense. I'm thinking of having a 1 strike rule for anyone trying to get over."*
- *"The one strike rule is to discourage anyone from taking advantage. It only applies when someone actually does something against the rules and one of the rules is to not abuse the reporting button. If someone gets reported and it's a false flag then nothing will happen to the person who got reported."*

## Bottom line for Don

**Recommend A: a strike is a confirmed rule break, and it removes the account. Bad-faith reporting is one of those breaks. A false flag clears completely.**
- **Who confirms:** you, by a tap on the review page, from what the content or our records show. A report alone never confirms anything, and neither does a count of reports or the AI.
- **What it does:** the account is removed. It gets one reply within 14 days, which you read. If you uphold the removal, it is permanent, and the phone number stays with the removed account so it can't come back.
- **False flags:** what was hidden comes back, any notice is marked cleared, and nothing stays against the person.
- **An honest wrong report is not a strike.** Today's cool-down for dismissed reports already handles that.

The first version needs no build: a ruling, the Terms and report-screen lines (copy for you), and you removing accounts by hand in Supabase. It holds only once the Twilio phone check is live.

**Your call: A, B or C (below).**

## The frame

1. **The strike applies only to a confirmed rule break, never to a report alone.** How many people reported something doesn't matter.
2. **Abusing the report button is itself a rule break.** A confirmed bad-faith report earns the reporter the strike.
3. **A false flag leaves the reported person untouched.** Anything hidden in the meantime is restored, and no record is held against them.

## How "confirmed" is decided, with one operator

**Who:** the operator, a person. Today that is you, on the review page (F101). The AI's first read (F100) ranks the queue and can suggest, but it never confirms a break. That is already ruled: "remove, restore and strikes stay a person's tap".

**What counts as evidence:** something you can point to, not a judgement of character.

| Rule break | What confirms it |
|---|---|
| Scam, fake Page or listing | The content itself, or a member's screenshots or messages, plus the place or business not existing (no site, address or record) |
| Impersonation, false claim | The claim record (a website email that isn't theirs), or the real owner coming forward with proof |
| Spam | The posts themselves: bulk, repeated, or links to sell elsewhere |
| Coming back after removal | The same phone (the phone check), or the same IP and device on uploads, which are already recorded for a year, operator-only (F102 criterion 13) |
| Fake engagement | Hearts or "I'm in"s from new accounts that only touch one Page, or the same IP across accounts |
| Harassment | The posts or messages aimed at one person |
| Bad-faith reporting | See the next section |

**The standard:** clear from the evidence. If you are unsure, the content can stay hidden and nobody gets a strike. Doubt goes to the member, which keeps the soul's "assume the best of each other".

**With one operator**, the volume stays small because a strike needs your tap. The one reply (below) catches your rare wrong call. Nothing goes to a second person until there is one.

## Bad-faith report or honest mistake

**The test: could a reasonable person have thought this broke a rule?** If yes, the report was honest even if it was wrong, and nothing happens beyond today's cool-down. If no, and there is a sign of intent, it's bad faith.

**Signs of bad faith** (any one, confirmed by you):
- **The reason plainly doesn't fit the content.** "Sensitive content" on a photo of a cake, or "threat of harm" on an opening-hours update. This matters most because those two reasons hide at once.
- **Targeting:** reports aimed at one person or Page across several posts, or after a dispute between the two.
- **Coordination:** the "Possible coordinated reporting" flag (F102 criterion 8: three or more reports on one poster in 24 hours, two or more from accounts under 7 days old), confirmed by the accounts' records.
- **Pattern:** repeat reports on content that breaks no rule after earlier ones were dismissed.

**Not bad faith:** one dismissed report, a wrong category picked honestly, or reporting something that turns out to be allowed.

**Precedents:**
- **Reddit** treats reporting content that broke no rule, or using reports to harass moderators, as "report abuse", and it can lead to suspension. It runs a separate path for reporting report abuse ([Reddit admin, r/ModSupport, 2020](https://reddit.birdcat.cafe/r/ModSupport/comments/epn2lp/weaponized_reporting_what_were_seeing_and_what/fekjfw9); [the 2019 report-abuse report](https://reddit.rtrace.io/r/modnews/comments/cgxuep/were_rolling_out_a_new_way_to_report_abuse_of_the/eumrxfx/?context=3)). Users say enforcement is slow and uneven, so a written rule alone doesn't deter.
- **YouTube** uses flaggers' accuracy as a measure of trust. It removed a trusted flagger for "a pattern of problematic notices" ([Tubefilter](https://www.tubefilter.com/2021/10/20/shifted-focus-youtube-trusted-flagger-upset-participants/)). It publishes no penalty for ordinary users who flag falsely.
- **Nextdoor:** neighbours report, and volunteer moderators and staff decide. Authors whose content was removed are told the guideline and can appeal. Moderators who misuse their role can be reported to staff ([Nextdoor's report to the California AG](https://oag.ca.gov/sites/default/files/Nextdoor%20California%20ToS%20Report%2C%20Q4%202023%2C%20with%20attachments.pdf/Nextdoor%20California%20ToS%20Report%2C%20Q4%202023%2C%20with%20attachments.pdf)). It publishes no rule on false reports by members.
- Taken together, everyone separates the dismissed report (no penalty) from the abusive pattern (a penalty). Ours would be clearer than any of them by naming it a rule break with one consequence.

## What the strike does

| | What happens | Precedent |
|---|---|---|
| The account | Removed: it can't sign in, and its Pages and posts are hidden | Airbnb, Uber and Meta's one-and-done track |
| How long | Permanent once you uphold it, or if no reply comes in 14 days | Meta disables "after one occurrence" for the worst breaks ([Meta](https://transparency.meta.com/enforcement/taking-action/counting-strikes/)) |
| Coming back | The phone number stays on the removed account (a phone confirms one account), so a new account needs a new phone. Coming back is itself a break | Reddit's ban evasion ([Reddit help](https://support.reddithelp.com/hc/en-us/articles/360045734511-My-account-was-banned-for-violating-Reddit-s-rules)) |
| Told why | A short notice naming the rule and what showed it | Etsy names the policy; the EU's DSA requires a statement of reasons (Art. 17) |
| One reply | Within 14 days, read by you, decided once | Airbnb removal appeals ([Airbnb help 1303](https://airbnb.com/help/article/1303)), Uber, YouTube's one appeal per strike |

Every platform we looked at keeps an appeal, and the EU's DSA requires one (Art. 20), though it doesn't bind us. In the US, removal in good faith needs none (Section 230(c)(2)). One reply costs you one read per removal.

## How today's flow changes

Today (F078, F102):
- A first report leaves the post up and sends its owner a courtesy notice.
- A second report from a different member hides it.
- Threat of harm and Sensitive content hide at once.
- The poster gets one answer.
- A reporter with dismissed reports loses the power to hide for a while: three rejected reports and their reports stop hiding.

| Step | Today | Under A |
|---|---|---|
| First report, most categories | Post stays up, courtesy notice | Same. If the report is dismissed, the notice shows as cleared and nothing is kept against the poster |
| Second report, or Threat or Sensitive | Hides until a person decides | Same interim hide, for safety. Dismissed means restored at once, notice cleared, no record on the poster |
| Your decision on the row | Remove or restore | Restore (false flag) · Remove (content goes, no strike: a mistake) · **Remove and strike the poster** (confirmed break) · **Strike the reporter** (confirmed bad faith) |
| Reporter warning (F078 criterion 10) | "Each report Don rejects is a strike; after three, reports stop hiding" | "Reporting in bad faith is against the rules, and one confirmed bad-faith report removes your account." Honest wrong reports keep today's cool-down, which is renamed so it isn't called a strike |
| Records on the reported person | The report history sits on the review row | A dismissed report is closed and leaves no count, flag or mark on the person. The year-long upload IP log is unchanged; it covers every upload, not reports |
| The poster's answer (F102) | One answer per hide | Unchanged; it is evidence on the row |

## Options

- **A (recommended): a confirmed break removes the account, with one reply.** It covers every rule break, bad-faith reporting included, and false flags clear completely. It discourages taking advantage the most while the one reply catches a wrong call by one operator.
- **B: a confirmed break suspends for 30 days, and the next one removes.** Softer, and closer to Meta's ladder for ordinary breaks. But it gives a scammer a second go, which isn't "one strike".
- **C: a confirmed break removes the account, with no reply.** The simplest, and the fastest for you. But a wrong call can't be caught, every precedent keeps an appeal, and a wrongly removed honest member is the worst outcome for trust.

**The smallest first version of A (no build, fits the freeze):**
- A dated ruling.
- The Terms line and the report-screen warning (copy for you).
- On the review page you use today's Remove for a confirmed break, then ban the account in Supabase Auth by hand. Supabase's own user ban stops sign-in, and the account is never deleted, so its phone stays taken.
- The notice and the one reply go by email from the operator.

The "Remove and strike" and "Strike the reporter" buttons, and an in-app reply, wait until the freeze lifts.

**Depends on:** the Twilio phone check being live (the dashboard's "Do next"). Without it a removal only costs a new email address.

## Rulings that would change under A

- **F078 criterion 10 and its 2026-09-30 ruling ("misusing reports: three strikes").** "Strike" is renamed for honest wrong reports (cool-down only), and confirmed bad-faith reporting becomes a one-strike break.
- **F078's courtesy-first ruling (2026-10-11).** It stands. It gains "a dismissed report clears the notice and leaves no record".
- **F058's "Not this" line** ("Appeals, strikes, or bans") becomes one strike with one reply.
- **F102.** The cool-down (criterion 7) is renamed, not a strike. The coordinated-reporting flag (criterion 8) becomes evidence of bad faith.
- **`policy.md` § How good faith is enforced.** "Community and peer pressure, not platform policing" gains: except a confirmed rule break, which removes the account.
- **Terms.** One new line, which is copy for you.
