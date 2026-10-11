---
id: explore-ai-moderation-scoring
purpose: Options for how AI moderation scoring could work for F078, F100 and F102, with how other platforms do it, sources, fit with our values, cost, false-hide risk and appeals, and a recommendation.
layer: exploration
status: options
date: 2026-10-11
---

# AI moderation scoring: options

**Options only; nothing here is ruled.** Sources were opened on 2026-10-11 unless marked *snippet* (a search summary, page not opened).

## Where we are (read from the scenarios and DECISIONS)

- A report hides the content at once. The hide bar is per metro and **starts at 0: every report hides** (F078 criteria 2, 6, 7; launch value chosen on #626).
- The AI reads every report **in shadow**: it changes nothing, it shows on the review row. Claude Haiku first; Sonnet gives a second opinion under 0.70 confidence. Output: category, severity 1 to 4, confidence 0 to 1, suggested outcome, a 140-character reason (F100 criteria 2, 3, 6).
- Live mode needs the harness at 95% recall, 100% on severity 1, under 10% false alarms, plus two weeks of shadow agreement the PM has read (F100 criterion 11).
- **Severity 1 (apparent child abuse) never goes to an AI provider.** Images are hash-checked first and go to a person (F100 criterion 12).
- Reporter counters (filed, upheld, dismissed, open) exist but are **never a score, rank or label on a person**; a dismissed report tightens that reporter's cap and a cool-down follows two (F102 criteria 5 to 7).
- A person always makes the call, except severity 4 restores itself in beta under narrow conditions (F102 criterion 12).

## How others do it

- **Reddit.** Mods write AutoModerator rules: remove, hold in the mod queue, or report. Crowd Control holds or collapses content from accounts with no standing in that community. *Snippet only; Reddit's help pages returned 403.* support.reddithelp.com, "Crowd Control".
- **Discord AutoMod.** Per rule: block the message, alert a private mod channel, or time the user out. No score; the admin picks the action. discord.com/safety/auto-moderation-in-discord.
- **Nextdoor.** A model flags a likely uncivil reply before it posts and shows a **Kindness Reminder** (edit, read the guidelines, or don't post). Its 2019 test: 1 in 5 reminded neighbours edited, 20% fewer negative comments. Reports go to volunteer reviewers by vote; staff handle accounts and sensitive reports. 2023 report: 36% of prompted neighbours revised or withheld, about 200,000 volunteers reviewed 90% of reported content, median removal 5.3 hours. blog.nextdoor.com/2019/09/18/announcing-our-new-feature-to-promote-kindness-in-neighborhoods; blog.nextdoor.com/2024/02/13/nextdoor-2023-transparency-report. The model threshold is not published.
- **Bluesky.** Labelers publish labels (reversible, with expiry); each person picks hide, warn or ignore per label. Reports go to a chosen labeler; Ozone gives reviewers a queue and an audit log. 2024: automated labelling 99.90% accurate, about 100 moderators, about 205,000 appeals. atproto.com/guides/labels; bsky.social/about/blog/01-17-2025-moderation-2024.
- **Meta.** Technology acts or sends content to people; the human queue is ranked by severity, spread and likelihood of violating. Appeals go to a different reviewer, then the Oversight Board; extreme child-safety cases are not appealable. No numeric thresholds published. transparency.meta.com/enforcement/detecting-violations/how-review-teams-work.
- **YouTube.** Machine learning flags; in most cases a trained person reviews first. Warning first, then strikes; one free appeal, with no extra penalty for losing. No thresholds published. support.google.com/youtube/answer/13304829 and /185111.
- **Perspective API (Google Jigsaw).** One score per attribute, the caller picks the cutoff. **Being shut down after 2026; do not build on it.** perspectiveapi.com. (Attribute list and recommended thresholds could not be read.)
- **OpenAI moderation endpoint.** Per-category `flagged` plus `category_scores` from 0 to 1, text and images, **free**. Its docs call the scores "signals", not an automatic blocking decision, and publish no thresholds. developers.openai.com/api/docs/guides/moderation.
- **Hive.** Per-class confidence; text severity 0 to 3 per class. Published price: text $0.50 and visual $3.00 per 1,000 requests. docs.thehive.ai/docs/text-moderation; thehive.ai/pricing.
- **Anthropic's own guide.** Use risk tiers, not yes or no: high blocks, medium goes to a human queue, low is allowed or monitored; add an explanation field. platform.claude.com/docs/en/about-claude/use-case-guides/content-moderation.
- **Community platforms.** Mastodon: people act on reports, no central AI, appeal within 20 days (docs.joinmastodon.org/admin/moderation/). Wikipedia: model scores only **prioritise** human review, with documented bias against new users (mediawiki.org/wiki/ORES). Front Porch Forum: its help page says professional community managers moderate every forum; its pre-publication review and numbers came from press, not opened (help.frontporchforum.com/is-fpf-moderated).

## Four ways to score

**1. One severity score (today's design).** A category plus severity 1 to 4 plus confidence; hide when the score meets the metro bar.
- Fit: simple, and the reason shown to the poster keeps it kind. Matches Anthropic's tier guidance.
- Cost: Haiku 5.5 is $0.10 in and $0.50 out per million tokens, Sonnet 5.5 $2 and $10 (pricing page). At an assumed 800 tokens in and 120 out: about $0.00014 per Haiku read, $0.0028 per Sonnet read. With 30% sent to Sonnet, **about $1 per 1,000 reports**. Token sizes are my assumption, not measured.
- False-hide risk: at bar 0 it comes from reports, not the AI (the AI is shadow). F102's caps and cool-downs are the guard. In live mode the AI only reorders.
- Appeal: F102 as written: fix and repost, or say the report is wrong; unanswered closes in 14 days.

**2. Per-category scores and cutoffs.** Each category (harassment, nudity, spam, violence, threat of harm) has its own score and its own bar; threats and children hide regardless (F078 criterion 8 already does this).
- Fit: lets us be strictest where harm is worst and gentlest on spam. Examples: OpenAI per-category scores, Hive per-class, Perspective per-attribute.
- Cost: free first pass (OpenAI endpoint) or the same Haiku call as model 1 returning per-category numbers.
- False-hide risk: more cutoffs, more places to be wrong; vendor categories are not our seven, and local tone is not theirs.
- Appeal: the notice already names the category (F078 criterion 3); the appeal is unchanged.

**3. AI score plus report weight.** Combine the AI's severity and confidence with how many people reported, how old they are, and how often that reporter was upheld.
- Fit: **reporter standing as a score conflicts with F102** ("never a score, rank or label on a person"). Caps and cool-downs, which exist, are the allowed form. Report count invites pile-ons; F102 criterion 8 already flags coordinated reports. Examples: Reddit's Crowd Control weighs standing; Meta ranks by severity, spread and likelihood.
- Cost: same as model 1.
- False-hide risk: lower for one malicious reporter, higher for a brigade if count weighs heavily.
- Appeal: unchanged.

**4. Bands with a soft middle, and a kindness nudge before posting.** Three lanes (hide, human queue, ignore) plus a soft lane: stays up with a cover or "under review". Plus Nextdoor's pre-post reminder for likely-unkind drafts.
- Fit: best with *kind and gracious* and *members first*: it prevents instead of punishing, and a wrong call in the soft lane costs the poster nothing. Examples: Bluesky's warn band, Nextdoor's reminder, Anthropic's three tiers, Wikipedia's use of scores to prioritise.
- Cost: the nudge reads every draft, not only reports: about $0.14 per 1,000 drafts with Haiku at the same assumed sizes, or free with the OpenAI endpoint for text.
- **New territory:** reading unreported drafts is a new data flow and needs its own ruling (member privacy first).
- False-hide risk: lowest; the soft lane needs no appeal because nothing was removed.

## Borrow whatever we pick

Log every score so cutoffs come from our own data (OpenAI and Wikipedia both say scores are signals to tune). Rank the human queue by severity, spread, then age (Meta; F101 already does). A different reviewer on any appeal. Keep people, not scores, as the last word.

## Recommendation

- **A (recommended):** launch as ruled (bar 0, AI in shadow). Read two weeks of shadow data, then go live with **model 1 plus bands** (hide, queue, ignore) using cutoffs from our own log, and move to per-category cutoffs only for a category the log shows is noisy. Scope the kindness nudge (model 4's cheap half) as its own scenario, as new territory. Reason: Meta, YouTube and OpenAI publish no thresholds, so our log is the only honest source, and F100 criterion 11 already requires it.
- **B:** per-category cutoffs from the first day of live mode (model 2).
- **C:** a combined AI-and-report score (model 3). Not recommended: it pulls against F102.

## Not verified

Reddit's Crowd Control levels and appeal window (page blocked), Discord appeal path, Perspective's attributes and thresholds, Meta and YouTube numeric thresholds (none published on pages opened), Front Porch Forum's review process and costs, Nextdoor's model threshold.
