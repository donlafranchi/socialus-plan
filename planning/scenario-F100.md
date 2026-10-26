---
id: F100
title: An AI reads every reported Post first, and a person still makes the call
status: approved
horizon: now
rank: 170
gates: launch
date: 2026-10-05
depends: [F078, F080, F099]
approved: 2026-10-05 — the PM's ruling: AI first-pass review, shadow mode in beta, live suggestions in production; Haiku (text + vision) first, Sonnet on low confidence; a person decides anything permanent; an evaluation harness and prompt tuning before it goes live.
---
## Story

**The constraint behind this design: one person runs the platform alongside a day job, and is mostly unavailable Tuesday to Thursday. Moderation has to run itself, and the PM's work is minimal and batched Friday to Monday.**

A Post with a photo is reported as harassment on a Tuesday. It hides at once, as today. Seconds later Claude Haiku has read the Post's text and photo against the platform's rules: harassment, severity 2, confidence 0.58, "Insults a neighbour by street name." Confidence is low, so Claude Sonnet reads it too and agrees at 0.81. The poster rebuts that evening; the AI reads the rebuttal as well. In beta nothing happens because of either read. On Saturday the PM sees the suggestion on the row, decides in one tap, and the app logs whether the person and the AI agreed. Before production, a labelled test set says how often the AI is right, and the prompt is tuned until it clears the bar.

## Acceptance

1. **Every new report, and every poster rebuttal (F102), triggers one AI assessment of the reported Post, photo, Page or Page picture**, after the report is stored and hidden; the report path does not wait on it, and a failed or slow call leaves the report exactly as F078 handles it.
2. **The first pass is Claude Haiku with text and vision**, returning structured output: a category (F078's seven, with sensitive content split into child and other), a severity 1–4 (F101's scale), a confidence 0–1, a suggested outcome (approve or remove) and a reason of 140 characters at most.
3. **Below the escalation threshold (start: confidence < 0.70) Claude Sonnet gives a second opinion**; both reads are stored and the shown suggestion is the second.
4. **What is sent is the content, the reporter's chosen reason and the poster's rebuttal only**: no member name, handle or email; the rules text sent is versioned.
5. **Each assessment stores** model, prompt version, category, severity, confidence, suggested outcome, reason, latency and time, in a table with RLS on and no policies, like `reports`.
6. **Shadow mode (beta): an assessment changes nothing.** It does not hide, restore, remove, notify, text, reorder or move a metro's bar; the operator sees it on the row (F101). The one exception is F102's narrow severity-4 auto-restore (ruled B, F102 criterion 12).
7. **When a person decides, agreement is logged** (AI suggestion vs. decision), so accuracy per category and severity is a query.
8. **Live mode (production) is a switch the PM flips as data, not a deploy.** Live means the AI's severity can raise a row's severity and order (F101); remove, restore and strikes stay a person's tap.
9. **An evaluation harness runs the current prompt and models against a labelled test set** and prints recall, false-alarm rate, severity accuracy, latency and cost per case; it runs on every prompt change.
10. **Builder agents build the test set**: clean, borderline and violating cases, each labelled with category, severity and outcome. Photos only from licensed or stock sources, licence recorded per photo. No real or synthetic image of a minor in any sensitive context; the children rule is tested with ordinary public-setting stock photos. No sexual imagery of anyone; the adult category is tested with text and non-explicit borderline stock.
11. **Live mode needs the harness to show ≥ 95% recall on violating cases, 100% on severity-1 cases and < 10% false alarms on clean ones**, plus two weeks of shadow agreement the PM has read.
12. **Suspected severity-1 content is never sent to an AI provider** (the PM, 2026-10-05). A report whose category is severity 1 (child safety or illegal, F101) skips the AI call; any image is first checked against known-CSAM hashes (Cloudflare's CSAM Scanning Tool), and the row goes to a person with the hash result.

## Not this

The AI hiding or removing anything on its own. Raising a metro's hide bar on the AI's score in beta. Classifying content nobody reported. Fine-tuning a model. Showing the AI's read to members.

## Why

**The PM, 2026-10-05:** AI first-pass review, shadow in beta, live suggestions in production, a person decides anything permanent. This is the agent F078 criterion 1 already names ("a submitted report triggers agent classification"); F100 says which agent and how it earns trust. The 2026-09-14 ruling, that an agent triages and a person decides, stands. **The operating constraint** (one person, a day job, mostly away Tuesday to Thursday) is why the AI reads every report the moment it lands: by Friday every row already carries a suggestion, and the PM's batch is confirming, not investigating.

**Path: new territory.** It sends member content to a third party: a privacy exposure and a member-trust call, which the PM ruled.

### What changes against today (read in `socialus-web` main, 2026-10-05)

- **No classification exists.** `report.create` (`src/actions/report/create.ts`) stores free text and hides the Page photo; there is no category, score or model call in the report path.
- **Reports cover Page photos only:** `reports.subject_kind` is `'group'` with a free-text `body`. F078 (approved, not yet built) widens it to Posts and adds the seven categories; F100 builds on that shape, so it comes after.
- **New:** an assessments table beside `reports` and `report_decisions`, an async call after the report commits, and agreement as a join of the latest decision to the latest assessment.
- **Unchanged:** the hide on report, F078's text to the PM on children and threat-of-harm categories (the reporter's category), and every permanent decision being a person's.

### Precedent

- **Meta** ranks content for human review by severity, virality and likelihood of violating; technology ranks and people decide the nuanced cases ([how Meta prioritizes content for review](https://transparency.meta.com/policies/improving/prioritizing-content-review/)). The split here comes from that.
- **Discord AutoMod** can send alerts to a private moderator channel instead of acting ([AutoMod FAQ](https://support.discord.com/hc/articles/4421269296535)). Shadow mode is its alert-only setting.
- **Hive** returns severity levels 0–3 per class ([text moderation classes](https://docs.thehive.ai/docs/detailed-class-descriptions-text-moderation)); **OpenAI's moderation model** scores text and images by category ([moderation guide](https://developers.openai.com/api/docs/guides/moderation)). Category, severity and confidence come from these. A general model given the platform's own rules is chosen over a fixed classifier because F080's rule (children, animals and pets, anyone who can't fend for themselves) is a stock category nowhere.

### Privacy and legal

- **The privacy draft must name the AI provider (Anthropic) as a service provider** that receives reported content for review. The legal docs live outside this repo; flagged in the PR description.
- Reported content only and no identity (criterion 4) keeps what leaves the platform to what review needs.
- The duty to report apparent child sexual abuse material is raised in F102 § Unattended time.

### Size

[platform none]

**About 3.5 build days, in the beta**, after F078's report shape: the model call, escalation and assessments table (1.5 days); the agreement log (half a day); the harness runner (1 day); the PM's read of the first results (half a day). Builder agents build the test set alongside. Live mode and prompt tuning follow after beta. What to push is in F101 § Size.

## Rulings
- **2026-10-11 — The Cloudflare CSAM Scanning Tool is set up before beta. Don sets up the socialus.org zone on Cloudflare and a verified reporting contact; agents build the hash-result field on the row, wire it in as soon as the tool is enabled, and write Don a short phone checklist of the setup steps.** The PM, 2026-10-11, option A on `socialus-web` #641 (F100 criterion 12). The 2026-10-05 ruling on severity-1 content and AI providers stands. [replaces none] [binds tiers=planning,code surfaces=moderation,uploads,ai] Issue: #641.
- **2026-10-11 — The live-mode gate for AI moderation is Don's own checklist with the numbers shown to him for beta, and software that refuses the live flip until a passing harness run is recorded and Don has marked the two-week shadow read before production. The numbers show as a staff-only "AI readiness" panel on the admin reports page and the same indicator on the ops/status dashboard: recall on violating cases (target 95% or better), severity-1 recall (target 100%), false alarms on clean cases (target under 10%), each with its last harness run date; shadow-agreement days out of 14 from `report_ai_agreement`; green, amber or red per number; and one overall "ready to go live" indicator.** The PM, 2026-10-11, option C on `socialus-web` #640 (F100 criterion 11); scope added by Don. [replaces none] [binds tiers=planning,code surfaces=moderation,ai,reports] Issue: #640.
- **2026-10-11 — AI moderation scoring launches as ruled (the bar is 0 and the AI runs in shadow). After two weeks of shadow data it goes live with a severity score and three lanes (hide, send to a person, leave up), with cutoffs set from our own log and per-category cutoffs only where the log shows noise.** The PM, 2026-10-11, option A on `product/exploration/ai-moderation-scoring.md`. Because a cutoff we have not measured is a guess, and one number is simpler to run than seven. The pre-post kindness pause is its own new-territory scenario (F108) and comes back to the PM. [replaces none] [binds tiers=planning surfaces=moderation,reports build=none]
- **2026-10-05 — Suspected severity-1 content (child safety or illegal) is never sent to an AI provider. Images are first checked against known-CSAM hashes (Cloudflare's CSAM Scanning Tool) and go to a person.** Scenario: F100 (criterion 12). [always] [binds tiers=planning,code surfaces=moderation,reports,ai,uploads]
- **2026-10-05 — An AI reads every reported Post first and a person makes the call. In beta it currently runs in shadow: its assessment changes nothing and only shows on the review row; in production its severity can raise a row's order, and remove, restore and strikes stay a person's tap.** Claude Haiku (text and vision) first, Claude Sonnet below a confidence threshold. Only the content, the reporter's reason and the poster's answer are sent, never a member's name, handle or email. Live mode needs an evaluation harness to clear F100's targets and two weeks of shadow agreement read by the PM. The 2026-09-14 ruling that an agent triages and a person decides stands. Scenario: F100. [for now] [binds tiers=planning,code surfaces=moderation,reports,ai]
