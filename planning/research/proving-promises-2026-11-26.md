**As of 2026-11-26** · Source: the PM's video summary (below); pstack, TLA+, Apalache, Quint, fast-check, pgTAP, pgrls and Bend repos and docs; Hillel Wayne, SIGOPS 2026, arXiv 2606.05792; `socialus-web` main read 2026-11-26 · Maintained by: hand (research note; deleted at 30 days or once ruled and placed)

# Proving our promises: a method review

*The PM, 2026-11-26, sharing a video summary:* "I've even recently heard how agents can use math proofs to check code to make it more bullet proof." The summary: agents can use formal verification (model checking with TLA+) to prove a rule like "a customer is never charged twice" holds in every case, not just the ones a test thought of; Lauren Tan's pstack plugin has an agent pick the costliest promises, prove them, see the check fail first, and re-check on every change; Bend 2 bakes "laws" into the language.

**Bottom line: the idea is real and the tool is free and works with Claude Code, but our costliest promises aren't built yet. After January 6, try the lighter version first: one test that throws thousands of random sign-up, phone-change and ban sequences at the real code. Keep the full proof tool for payments.**

**Your call:** after January 6, which pilot: **A, random-sequence tests on sign-up and bans (recommended)**, B, the full proof tool on the same flow, or C, nothing until payments?

## What the video gets right and wrong

| Claim | Verdict |
|---|---|
| pstack is Lauren Tan's plugin that picks promises to prove and keeps them current | **Verified.** Free, MIT licence, in Cursor's plugin repo; a create skill and a maintain skill, about 5 weeks old, version 0.15 |
| Installed from the Cursor marketplace | **Verified, and not Cursor-only:** the same repo ships an official Claude Code build |
| It proves with TLA+ | **Partly.** TLA+ is its default for "things in the wrong order"; it picks other checkers, or random-input tests, where they fit |
| It must see the check fail before trusting it | **Verified.** Same as our own absolute: a check never seen failing proves nothing |
| TLA+ is proven in industry | **Verified:** Amazon since 2011, Azure Cosmos DB, MongoDB (the Amazon paper itself refused automated reading) |
| Bend 2 stops an AI shipping changes that break laws | **True as described, unusable for us:** an experimental language with no web, JSON or database support and an unaudited compiler |
| AI writes good proofs | **Not on its own.** Three 2026 sources: models write specs that compile but often don't match the real system, so a person or a fail-first check has to catch it |

Links: [pstack](https://github.com/cursor/plugins/tree/main/pstack) · [TLA+](https://github.com/tlaplus/tlaplus) · [Apalache](https://github.com/apalache-mc/apalache) · [Quint](https://github.com/informalsystems/quint) · [fast-check model-based testing](https://fast-check.dev/docs/advanced/model-based-testing/) · [Supabase RLS testing with pgTAP](https://supabase.com/docs/guides/database/postgres/testing-row-level-security) · [pgrls](https://pgrls.github.io/pgrls-docs/) · [Bend](https://github.com/bendlang/bend) · [TLA+ in industry](https://foundation.tlapl.us/industry) · [Hillel Wayne, 2026-03-10](https://buttondown.com/hillelwayne/archive/llms-are-bad-at-vibing-specifications) · [SIGOPS 2026](https://sigops.org/2026/can-llms-model-real-world-systems-in-tla) · [arXiv 2606.05792](https://arxiv.org/html/2606.05792v1)

## Our promises, and what guards them today

Two shapes. **"Who may see what"** promises are checked well by database tests, which we already run. **"Things over time"** promises (retries, re-sign-ups, races) are where proofs and random-sequence tests earn their keep.

| Promise | Shape | Guarded today | Fit |
|---|---|---|---|
| One account per mobile number | Over time | Only the sign-in provider's own rule; no test | Random sequences, then a proof. Being built for Jan 6 |
| No text to a zip outside an open market | Over time | Texting is off until the SMS keys exist; today's sign-up asks the phone before the zip. The Jan 6 sign-up rework (ruled 11-12) puts the zip first | Random sequences, after the rework |
| A banned number stays banned | Over time | Not built; Jan 6 | Random sequences, then a proof |
| Waitlist answers staff-only | Who sees what | Database test | Covered |
| Find never reordered by payment | Who sees what | Nothing pays today; no test pins the order | One cheap test that the order uses only relevance and date |
| No member can piece together another's pattern | Mostly who sees what | Database tests, one table at a time | Gap: nothing checks that combining what's visible can't rebuild someone's week. Worth its own review |
| Search history only its owner's | Who sees what | Nothing per member is kept; saved searches have no database test | Add a database test |
| Page owners see search counts only past the floor | Both | Code shows a term at 3 searches, which could be one person; your 11-15 ruling says 10 different members. Not on any screen yet; ticketed | Fix in its ticket |
| Never charged twice | Over time | No payments | The textbook case for a proof, when payments come |

## Options: one pilot, after January 6

| | A (recommended) | B | C |
|---|---|---|---|
| What | A test that runs thousands of random sequences (sign up, change phone, delete, re-sign-up, ban) against the real code and database, checking "one account per number" and "banned stays banned" after every step | pstack's proof skill on the same flow: a TLA+ model, seen failing on a broken copy, re-checked when those files change | Keep today's fail-first tests; revisit when payments are built |
| New tool | One free test library (fast-check), no plugin | A third-party plugin plus Java in CI | None |
| Cost | About half a day of agent time; a few minutes added to CI | About a day; long sessions; CI adds a Java step (seconds to minutes, not measured) | None |
| Catches | Orderings nobody wrote a test for, in the real code | Every ordering, but only in the model, which can drift from the code | What we thought of |
| Kept current by | The build agent who touches sign-up, like any test | The plugin's maintain skill, run when those files change | — |
| A person later | A trust-and-safety engineer reads the sequences each quarter | Someone who reads TLA+ reviews the model | — |

**Why A:** the flows are new and changing, so a proof of a model would chase the code. A tests the code itself, uses the test runner we have, and needs no plugin install. B becomes the right call for payments, where a model is worth the upkeep. Precedents: fast-check's model-based testing, Amazon's TLA+ use for its hardest core flows.

**Not this:** installing anything before you pick; Bend; slowing any January 6 work.

## Verified and assumed

**Verified:** every row in the first table against the tool's own repo or docs, 2026-11-26; every row in the promises table against `socialus-web` main, read by code.
**Assumed:** time and CI costs (no published figures); that the Jan 6 sign-up tickets land as ruled.
