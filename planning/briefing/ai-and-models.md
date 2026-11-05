# AI and models

Briefing for idea chats, written 2026-11-05 from the plan, ops and web repos. It stands alone. **[unverified]** marks anything not checked against the code or a provider's own page.

## Where AI is used today

**Two places, both Anthropic, both off unless a key is set. Nothing else in the app calls a model.**

1. **First read of reported posts** (moderation).
   - When someone reports a post or Page, Claude Haiku 4.5 reads it after the report is saved, so nobody waits. If it's unsure (under 70% confident) Claude Sonnet 5.5 takes a second look.
   - It runs in **shadow**: it records a verdict, and a person decides. In live mode it could only ever put something back up, never take anything down, and only when both models agree at 95% or more.
   - It sees the post's title, text, photo and the report reason. It never sees names, handles or emails; a test plants a member and fails if they appear in the request.
   - Suspected child-safety reports are never sent. Reports by test accounts aren't read.
   - Whether the key is set in production, and the live/shadow setting there, is **[unverified]**. The eval harness has never recorded a run because the key isn't a GitHub secret.
2. **Sorting members' bug reports.** Every 30 minutes a GitHub job files in-app problem reports as Issues; Haiku 4.5 labels them and spots duplicates. Emails, phones and zip-like numbers are cut first. Its key has a hard monthly cap.

Not AI: the seeders, importers, test accounts, search, shelves and label suggestions (a word match) use no model.

## Where AI is planned

**Five ideas in the plan, none built. All assume a small Claude model.**

- **Auto-sorting posts into labels** [#1182, plan #273]. Ruled B on 11-05: a 100-post test of Jev (from TypeSafe) against Haiku 5.5, 90 of 100 right to pass, sending only the words and one small photo. Jev can't see member posts until TypeSafe confirms its data retention in writing and Don approves a privacy line. Otherwise Haiku; the word match stays as the fallback.
- **Taste chat.** An optional short chat to correct your interest profile. The profile itself is weighted counts computed nightly, not a trained model. Research only.
- **Ask bar** (F119, approved, not built). One call to the smallest Claude model routes a question to the right page, with a daily cap per member and a fallback to search.
- **Chat-first** (F120, draft, later). Actions only on a confirm tap; memory the member can see; never sold or trained on.
- **Dictionary suggestions** (F071). A job proposes new search words into a review queue.
- **Seeding and research** are done by agents in Claude Code sessions and committed as lists; no app code calls a model for them **[unverified who made each list]**.

## Costs known

**Pennies today. The plan's prices are mixed and some don't match the code.**

| Model | Input / output per million tokens | Source |
|---|---|---|
| Haiku 4.5 (in the code) | $1 / $5 | code comment, "check before quoting" |
| Sonnet 5.5 | $3 / $15 (code) or $2 / $10 (plan doc) | conflicting **[unverified]** |
| Haiku 5.5 | $0.10 / $0.50 | plan docs **[unverified]** |
| Jev 1.14.0 | $0.042 input, output free | TypeSafe pricing, read 11-04 |

- Moderation: about $1 per 1,000 reports (plan estimate).
- Auto-sorting: about $0.00014 a post with Haiku 5.5, about $0.0001 with Jev (photo pricing unknown).
- Taste chat: about $0.01 per member per month, about $11/month at 1,000 weekly users (estimate).
- The whole platform was budgeted at about $48/month at launch, with a Vercel spend alert at $60. No AI budget figure has been set by Don.
- **Mismatch:** the code calls Haiku 4.5, while the plan's cost estimates assume Haiku 5.5.

## Privacy rules any model must follow

**Content only, never who. Never child-safety content. Never sold, never trained on, and the member owns what an assistant learns.**

- **[always]** AI helps people and doesn't replace them. A person decides anything that affects a member.
- **[always]** What an assistant knows about a member belongs to the member: visible, exportable, deletable, never sold, never used to train anyone else's model.
- **[always]** Suspected child-safety content never goes to any AI provider. It is hash-checked through Cloudflare first (Cloudflare setup is still Don's to-do).
- Never send names, handles, emails, phone numbers or exact locations. Nothing finer than the market.
- Never infer health, politics, religion, sexuality or money (planned guardrail for the taste chat and sorting).
- Each provider must be named on the privacy page. Today it names Anthropic as processor, "only on our behalf and on our instructions." A new provider needs a new line Don approves.
- Retention matters: Anthropic's API keeps inputs 30 days (up to 2 years if flagged) per the plan research **[unverified]**. Jev's terms state no retention period and keep telemetry "in perpetuity."
- A processor agreement with Anthropic is not yet signed; it's on the counsel list.
- Question logs for the Ask bar would be anonymous, shown only for 10+ members, raw rows deleted after 30 days.

## Hosting limits

**Everything runs on free tiers with no GPU and no long-running server. Any model we host ourselves would live somewhere new.**

- **Vercel Hobby** (free) per the ops docs **[unverified against the dashboard]**. Hobby forbids commercial use; Pro is $20/month per seat. Functions are short-lived; no route sets a longer time limit, and Hobby's exact limit isn't recorded in the repos **[unverified]**. Logs keep about an hour.
- **Supabase Free.** Rate limits, pauses after 7 idle days, no backups. Pro ($25/month) is planned two weeks before launch. pgvector is installed and two embedding tables exist, empty.
- **No GPU, no worker, no queue.** Background work is either a GitHub Action on a schedule or a step that runs right after a request on Vercel.
- **GitHub Actions** is the only scheduler. Jobs can run minutes long but not instantly on demand from the app **[unverified]**.

## Seed: on-demand open-weight models

**Don's idea, 11-05: spin up an open-weight model only when needed to help members who need assistance, and use free models alongside paid ones. Facts and open questions only; no recommendation.**

Facts from the repos:
- Nothing open-weight, self-hosted or GPU-based exists or is mentioned anywhere in plan or ops.
- Every model call today is a plain web request with a 20-second timeout, made after the member's action finishes. Swapping the address it calls is a small change; the guard test only allows three files to name a provider.
- The app has no place to run a model itself. Any open-weight model would need an outside host (a pay-per-second GPU service, a serverless inference provider, or a machine we run).
- A cold start (spinning up on demand) takes time. Moderation and sorting can wait; a member asking for help in the moment can't wait long **[unverified how long cold starts take]**.
- Rulings already constrain any model: content only, no child-safety content, a named processor on the privacy page, member-owned memory, a person decides.
- "Free" models are free to use but not free to run. Hosted free tiers usually have rate limits and their own data terms **[unverified]**.

Open questions:
1. What does "assistance" mean first? Helping someone write a post or set up a Page, finding something, explaining the app, or reading reports?
2. Who is the help for? Members who struggle with tech, owners setting up, operators?
3. Which uses can wait seconds or minutes (cold start fine) and which must answer right away?
4. Which uses are allowed to be free-and-slower and which need the best answer? Should a member ever choose?
5. Where would the model run, and does that host keep what it's sent? It would need a privacy-page line.
6. Does running our own model fit "never extractive" and member ownership better than a paid API, for example by keeping member text off third parties entirely?
7. What's the monthly ceiling Don will set for AI, and per-member daily caps?
8. How do we test quality? The sorting test (100 posts, 90 right) is a template.
9. Does it change the Hobby/Free hosting plan, which forbids commercial use on Vercel?
10. Who watches it? Today's AI work has no live run recorded yet.
