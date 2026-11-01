# Cold-start brief: shelf catalog + a new name for "Wonder"

Home: `socialus-plan`. Deliverable: one research doc, `planning/research/shelf-catalog-and-wonder-name-2026-10-31.md`, in PM format (bold bottom line, the one call, the picture, folded detail). Work on your own worktree at `../worktrees/socialus-plan/process-2026-10-31-shelf-catalog`. Open it as a PR, `docs: research — shelf catalog and a new name for Wonder`, and self-merge with `gh pr merge --squash --auto` once lint passes. Lint has a budget per file, so keep the doc lean and fold the tables. End with the three-line report naming the top shelves and the recommended name, plus a SAFE TO CLOSE line. Delete this brief when you're done.

## Context already settled (don't re-research)
- **F121 is approved and merged (plan #234).** Shelves are data: a name, a query, a lead time and season dates. Order rotates per member per day, with a weekly scoreboard. Every view starts with the timely items from followed Pages. No chips or pills.
- **2026-10-31:** Find may sort and filter by interests, likes and interaction, so interest shelves can go on Explore too. The ruling is in F059.
- **Research to build on:** plan #230 (`planning/research/explore-shelves-and-shelf-life-2026-10-27.md`), which gives the shelf-life table and the gap where real posts have no kind field.

## Don, verbatim (2026-10-31)
"approve. also have the session look at what's in there? there could be many categories, New and interesting, Something Unique. Play with Farm Animals. There could be dozens. Can you have a session see what we have in there now and see what we could create. Meet up with folks, Go out and play. Move your body. Try something new. How about a class? Want to learn something? Who's got a 'Wonder'. Lastly I don't like the term 'a wonder'. We need something new for that?"

## Item 2: the shelf catalog
1. **Inventory, read-only.** Code is `~/Projects/socialus-web`, at `origin/main`, read with `git show` and `git grep`; don't check it out at the root. The database is Supabase `socialus-db`, read through the Supabase MCP `execute_sql` using SELECTs only. Gather:
   - Page collections: the eleven collections and how many Pages each has in the Sacramento market.
   - Interest tags: `src/ontology/registry.json` and the interests table.
   - Post kinds, per web #1126 (read the Issue).
   - The kinds of venue show in the scraped feeds.
   - Seeded themes: samples and market days.
   - Counts of upcoming dated posts, next 7 and 30 days, by kind and collection.
2. **Propose dozens of shelves** (aim for 30–40). Use warm names in Don's style, like "Meet up with folks", "Go out and play", "Move your body", "Try something new", "How about a class?", "Play with farm animals", "Something unique". Focus on people doing things together, planning ahead and seasonal shelves. Say "locals", never "neighbors". For each shelf give: name | query (kind, collection, tags, interest, date window, season) | lead time | today's count, or what's missing (e.g. it needs a post kind or a tag).
3. **Mark the 10–15 strongest for the F121 rotation**, and say why: the data fills it, it's timely, it gets people together.

## Item 3: a new name for "Wonder"
- **What it is:** web #1081 and plan #213 (read both). Someone asks "who's in?" before making something happen. People say they're in, with a size or an option. Others offer to help in roles. A progress bar fills toward a goal.
- **Give 6–8 names.** For each: one line on why, and how it reads in "Post a ___", "12 of 30 in" and "Who's got a ___?". Do a quick trademark and app-name conflict check on each (USPTO search, App Store).
- **Recommend one.** The words are Don's: present the options as his call.
- "Count me in" is already a draft shelf name in F121, so note any overlap.
