# One strike for anyone trying to get over: research, 2026-11-06

Research only. Nothing here is ruled. Don, verbatim: *"a new kind of policy that says, we are not putting up with any nonsense. I'm thinking of having a 1 strike rule for anyone trying to get over."*

## Bottom line for Don

**Recommend A: one strike for deliberate deceit or targeting a person, and courtesy-first for everything else.** Someone who scams, fakes a Page, poses as someone else, comes back after removal, buys or fakes reactions, or harasses a person is removed the first time. Someone who gets something wrong keeps today's courtesy notice and the chance to fix it. Removal is always a person's call, and the removed person gets one reply, which you read.

The first version needs no build. It needs a ruling, one line in the Terms (copy you approve), and the operator removing the account by hand. The phone check makes the removal stick, because the phone number stays on the removed account.

**Your call: A, B or C (below).**

## What "trying to get over" covers

The line is intent: **deliberate deceit for gain, or targeting a person.** An honest mistake isn't covered.

| One strike (deliberate) | Courtesy first (a mistake) |
|---|---|
| A scam: taking money or details under false pretences | A wrong price, date or address |
| A fake Page or listing: a business, event or item that doesn't exist | A post in the wrong kind or the wrong place |
| Impersonation: posing as another person or business, or claiming a Page that isn't yours | A claim filed in good faith that turns out to belong to a partner or ex-owner |
| Spam: bulk or repeated posts, or links to sell elsewhere | One promotional post too many |
| Ban evasion: a new account after a removal | A second account made by mistake |
| Fake engagement: bought or traded hearts, reports or "I'm in"s | Asking friends to look at a Page |
| Harassment: targeting a person, including false reports aimed at them | A heated or rude reply, once |

Threat of harm and sensitive content already hide at once (F078 criterion 8). They would also get one strike under A.

## How others handle zero tolerance

**Everyone runs two tracks: a ladder for ordinary violations, and removal on the first offence for the worst.** They differ on how wide the second track is. Every one of them keeps a way to appeal.

- **Meta (Facebook, Marketplace).** Strikes climb from a warning to time-limited limits to removal. Some violations, child exploitation for example, disable the account "after one occurrence" ([counting strikes](https://transparency.meta.com/enforcement/taking-action/counting-strikes/), [disabling accounts](https://transparency.meta.com/enforcement/taking-action/disabling-accounts/)). The Oversight Board criticised the vague line between the two tracks ([Oversight Board](https://www.oversightboard.com/news/accounts-pilot-case-upholds-metas-decision-but-shows-critical-improvements-needed-for-social-media)). Marketplace access can be restricted on its own, with a request for review **[unverified, from memory]**.
- **Airbnb.** It may suspend or remove an account for "repeated or severe" violations. A removal can be appealed by a stated date ([Airbnb help 1303](https://airbnb.com/help/article/1303)).
- **Uber.** Access can be lost "temporarily or permanently, depending on the seriousness". Fraud is "deliberate deception to secure unfair or unlawful gain". In the UK, a person reviews before any deactivation. Some fraud cases get warnings first ([community guidelines](https://www.uber.com/br/en/drive/basics/uber-community-guidelines), [deactivation policy](https://www.uber.com/pr/en/legal/deactivation-policy/), [Sea-Tac fraud](https://www.uber.com/blog/seattle/sea-tac-fraud/)).
- **Reddit.** Coming back on another account after a ban is its own violation, and it can bring a sitewide ban ([Reddit help](https://support.reddithelp.com/hc/en-us/articles/360045734511-My-account-was-banned-for-violating-Reddit-s-rules)).
- **Etsy.** A suspension notice names the policy broken, and there is an appeal. Opening a new shop to get around a suspension isn't allowed **[from forum and third-party guides, unverified]** ([Etsy community](https://community.etsy.com/t5/Technical-Issues/Etsy-account-has-been-permanently-suspended/m-p/148630268)).
- **Nextdoor.** Removed content comes with the guideline it broke and a chance to appeal ([Nextdoor's report to the California AG](https://oag.ca.gov/sites/default/files/Nextdoor%20California%20ToS%20Report%2C%20Q4%202023%2C%20with%20attachments.pdf/Nextdoor%20California%20ToS%20Report%2C%20Q4%202023%2C%20with%20attachments.pdf)). No official page covers appealing a permanent removal.
- **Craigslist.** Community flags take posts down, and the terms allow blocking a user. There is no formal appeal **[from memory, unverified]**.

**Legal norms.** In the US, platforms may remove in good faith, and no law requires an appeal (Section 230(c)(2)). The EU's Digital Services Act is the stricter model, though it doesn't bind us today. It requires:
- a statement of reasons (Art. 17)
- an internal complaint route (Art. 20)
- suspension only after a warning, and only for "frequent" manifestly illegal content (Art. 23)

Telling the person why and giving one reply keeps us close to that model at almost no cost. Anything that touches money or a sale goes to counsel, as usual.

## How it fits our stances

- **Phone check [always].** It is what makes one strike work. A removed account keeps its phone number, and a phone confirms only one account, so coming back costs a new phone. Without Twilio live, a removal is only as strong as an email address, so this waits on the dashboard's "Do next".
- **One operator.** One strike adds removals, not reviews: the report flow already sends cases to you. The reply is one message per removal, read once, and kept only in your queue.
- **Self-correct first and courtesy-first (2026-10-11, F078).** Under A, these still govern every honest mistake. A adds a third exception beside threat of harm and sensitive content: deliberate deceit. Under B, they would end.
- **Decent by default (soul).** "We assume the best of each other… and keep simple ways to handle the times they aren't." A is that simple way. B assumes the worst of every reported mistake.
- **AI first read (F100).** Removal stays a person's tap. The AI can rank a suspected scam higher, but it never removes anyone.

## Options

- **A (recommended): one strike for deliberate deceit or targeting a person.** The categories are the left column above. The removal is a person's call, the person is told why, and they get one reply. Everything else stays courtesy-first.
  - Precedents: Meta's one-and-done track, Uber's fraud deactivation, Reddit's ban evasion.
- **B: one strike for any upheld report.** The simplest to say, but it punishes honest mistakes. It ends courtesy-first and self-correct, and it turns false reports into a weapon against the people they target.
- **C: keep the ladder (warning, cool-down, removal on a third offence).** One strike only for threat of harm and sensitive content. Kind, but scammers get three tries.

**The smallest first version of A, with no build:**
- A dated ruling.
- One line in the Terms and on the report screen (copy for Don).
- The operator bans the account in Supabase Auth (it can't sign in) and hides its Pages and posts with the existing tools.
- The account is never deleted, so its phone number stays taken.
- The removal notice and the reply go by email from the operator.

A "Removed" state and an in-app reply wait until the build freeze lifts.

**Rulings that would change under A:**
- **F078.** The courtesy-first ruling (2026-10-11) gains a third exception, deliberate deceit.
- **F058.** Its "Not this" line, "Appeals, strikes, or bans", becomes one strike with one reply.
- **`policy.md` § How good faith is enforced.** "Community and peer pressure, not platform policing" gains: except deliberate deceit, which the platform removes.
- **F102.** The cool-down for misused reports stays as it is. A false report aimed at a person counts as harassment.
- **Terms.** One new line, which is copy for Don.
