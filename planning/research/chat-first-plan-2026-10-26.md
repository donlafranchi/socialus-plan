# Chat-first plan

**A member says what they want, and SocialUs answers with the few tools they need, each one filled in and editable. We get there in steps. First, every screen opens from a link with its details filled in, which nobody sees. Next comes one ➕ and an Ask box. Chat as the home screen comes after the soft launch.** Search analysis runs nightly on Claude Haiku from the start.

**Your one call:** none now. The direction is ruled. The next step is F119, which is approved and sequenced after the current work.

*Don, 2026-10-26:* "I like C. Let's use that as our direction and the users question opens one of these pages e.g. /you or /explore or other pages for example." Then: "So the direction should start with a user prompt and then turn into a "workflow" that opens up a surface that allows more fine tuning. … I like the one plus button for things too in this app. I also want to know how something like Haiku or DeepSeek could help us triage users searches. I want our search to be highly analyzed and used to help our members who create or organize."

## The UX principle: stable widgets, composed by intent, always editable, pin what works

*Don, 2026-10-26:* "would it be a good use case to say if a user could ask a multi-part question that required multiple widgets, that we deliver them those multiple widgets as their return results so they can accomplish whatever they're intending to accomplish? the widgets may be more important for a creator or organizer than for a consumer follower. … instead of us deciding where things go, that the user's question can return widgets based on their prompt."

- **From navigation to composition.** Today we decide where things live. Instead, the person's intent assembles the tools they need.
- **A fixed library of well-designed widgets:** the post composer, calendar, map, search-demand card, Wonder tracker, reminders, a vendor list, and so on. The AI only picks, orders and fills them in. It never generates new UI.
- **Every widget arrives filled in and editable.** Any action needs a confirm tap.
- **The fewest widgets that get the job done**, with one main action.
- **Predictable.** The same question gives the same layout. A member can pin a set that works as their own workspace, like an organizer's "my Saturday market".
- **Other ways in stay:** the ➕, search and suggested prompts. Asking is the fast path, not the only one.
- **Followers usually get one or two widgets.** Organizers get workspaces with several.
- **Designed against** getting lost, model mistakes and features nobody can find.

## The path

| Step | When | What a member sees |
|---|---|---|
| 1. Every widget opens from a link with its details filled in, plus a widget registry | Now to the soft launch | Nothing new; this is plumbing |
| 2. One ➕ and an Ask box | Next (F119) | "Weekly run club Saturday mornings" opens the composer already set to weekly, Saturday, 7am, near you |
| 3. Finding works the same way | Next (F119) | "Anything fun this Saturday near Midtown?" opens Explore already filtered; they adjust from there |
| 4. Multi-step workflows | Later (F120) | A Wonder bulk-buy walks through sizes, then roles, one editable widget at a time |
| 5. Chat as home | Later (F120) | Answers arrive as widgets inline or full screen; actions run on a confirm tap |
| 6. Search analysis | Next, beside step 2 | Organizers see what neighbours are looking for and don't find |

<details><summary>Step 1: every widget reachable, and the widget registry</summary>

- Each widget gets a link with its settings filled in: Explore's filters (date, category, place), a Page, You's settings, the composer (text, kind, schedule) and a Wonder.
- **The widget registry** is one list in the code. It names each widget, its link and the settings it accepts. The Ask box can only open what the registry lists, which is how the AI is kept from inventing UI.
- Members see no difference; this also makes sharing and notification links more exact.
</details>

<details><summary>Steps 2 and 3: the ➕, the Ask box and finding</summary>

- **The ➕ is the one place to start anything:** a post, an event, a Wonder, a Page. One button replaces the scattered create buttons.
- **The Ask box sits with it.** One cheap model call turns a prompt into a workflow: which widgets to open, in what order, and what to fill in. If the call fails or finds nothing, the prompt runs as an ordinary search, so the member always lands somewhere.
- Finding is the same move. A question opens Explore already filtered, and the member adjusts the filters.
- Nothing is posted or joined for the member. A filled-in draft waits for their tap.
</details>

<details><summary>Step 4: multi-step workflows</summary>

- One prompt can need several widgets in a row. A Wonder bulk-buy goes from the Wonder, to sizes, to roles.
- They come one editable widget at a time, each finished before the next opens. An organizer can pin the set as a workspace.
</details>

<details><summary>Step 5: chat as home, after the soft launch</summary>

- The conversation becomes the first screen. Widgets appear inline, or full screen when there's work to do. Every page stays reachable directly.
- **Actions use the existing action registry as their tools**, each shown in plain words and run only on a confirm tap.
- **Memory is visible:** a member can see it, delete it, or switch it off.
- Voice comes later, on the same path.
- A daily limit per member keeps the cost down. Past it, the pages still work.
- Privacy and moderation: chats are never used to profile or sell. Anything the assistant posts for a member goes through the same moderation as their own posts.
- The ethos: AI helps and never replaces a person, and the benefit goes to members.
</details>

## Search analysis: Claude Haiku, nightly, in batches

**Decided:** Claude Haiku 5.5 through the Batch API, once a night. **Not DeepSeek's hosted API.** Member searches would go to a provider based in China, which clashes with member trust. Running DeepSeek ourselves would avoid that, but it adds servers to keep up, for no saving at this size.

- **Each search gets tagged** with its intent, category, place, time window, whether it found anything, and a normalised wording of the query.
- **Once a week, unmet demand is clustered per area:** what people looked for and didn't find.
- **Organizers and creators see it** on the owner card, in a "what neighbours are looking for" list, and as suggested Wonders.
- **The privacy rules are the existing search-demand rules (socialus-web #923, F089):** anonymous and aggregated, with a floor of ten members and one metro; raw rows are deleted after 30 days; never tied to a member in anything shown; one setting opts out. This builds on that log rather than starting a new one.

<details><summary>Rough cost</summary>

- Haiku 5.5 costs $0.10 per million tokens in and $0.50 out; the Batch API halves that to $0.05 and $0.25 (Anthropic's price list, 2026-10).
- **Assumed:** about 300 tokens in and 60 out per search, with the instructions cached.
- That works out to about **$30 per million searches**. At soft-launch volume, with an assumed 30,000 searches a month, it's **about $1 a month**.
- The weekly clustering is one call per area: cents.
- The Ask box's live routing (step 2) is a separate, real-time call. It has the same per-search size at full price, about $60 per million prompts, under a daily limit per member.
</details>

## Where this lives

- The direction and the UX principle: `product/foundation/what-this-is.md` § Rulings.
- Steps 1–3 and search analysis: F119 (Next). Steps 4–5: F120 (Later). Both show on the dashboard under "Where we're going".
- What a conversation is as a thing, still unshaped: `IMAGINE.md` § Chat-first SocialUs.

Precedents: Google's App Actions (a request opens an app's deep link already filled in), Airbnb's and Expedia's natural-language search filling filters, Linear's command bar, Notion's pinned pages. Path: well-worn for steps 1–3; new territory for chat as home, which is why it waits for after the soft launch.
