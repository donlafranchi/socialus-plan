# Setting up a second machine

**As of 2026-10-23** · Source: hand-written, checked against the repos · Maintained by: hand (the owner confirms on next edit)

Checklist. Where this disagrees with the repos, the repos are right. **Git is the handoff:** every machine clones from GitHub, every machine pushes, main is the truth.

## 1. Clone as siblings

```
~/Projects/
  socialus-plan/    git@github.com:donlafranchi/socialus-plan.git   # this repo
  socialus-web/     git@github.com:donlafranchi/socialus-web.git
  socialus-ops/     git@github.com:donlafranchi/socialus-ops.git    # the method
  skills/           git@github.com:donlafranchi/skills.git          # then: bash skills/link.sh
```

`socialus-design` has no remote yet. **Siblings, under any parent folder:** `scripts/state.sh` resolves the code repo at `../socialus-web` and dies with `FATAL` otherwise, and `scripts/lint.sh` reads the process absolutes from `$METHOD_REPO` or an `../ops-pattern` sibling, so export `METHOD_REPO=~/Projects/socialus-ops` (or keep the older `ops-pattern` checkout). The repos are public [for now] (2026-10-01); private would mean an account with access per machine.

## 2. Tooling

| Tool | Why | Version |
|---|---|---|
| `git` | | any current |
| `gh` | `state.sh`, `status.sh` and `view.sh` fail closed without `gh auth login` | any current |
| `python3`, `jq` | `scripts/` | 3.x; any |
| Node, `npm` | `socialus-web`; `package-lock.json` means npm, not pnpm or yarn | **20**, what every workflow uses. Nothing enforces it locally (no `engines` field), so set it yourself |
| Supabase CLI | `npm run db:push`; `supabase start` for the write-bound tests | **2.117.0**, pinned in the workflows |
| Docker Desktop | `supabase start` only | never OrbStack (`~/.claude/CLAUDE.md`) |

## 3. Secrets

No `.env` is committed (`.gitignore` covers `.env*`). **The authoritative list is `socialus-web/.env.local.example`:** copy it to `.env.local` and fill it in. Where the values come from: Supabase (project settings → API: URL, publishable key, secret key); Mapbox (a public `pk.` token and a server-only geocoding token); Resend (follow email); `CRON_SECRET` (`openssl rand -hex 32`); `OPERATOR_MEMBER_ID` (your `members.id`; unset authorises nobody, so `/admin/reports` stays closed until set).

Faster: `npx vercel login`, `npx vercel link` (the checkout is not linked), `npx vercel env pull .env.local`.

Never paste a secret into a doc, a scenario, an Issue or a chat. `SUPABASE_SECRET_KEY` bypasses row-level security.

## 4. Supabase: hosted, not local

`npm run dev` reads the hosted project (`NEXT_PUBLIC_SUPABASE_URL` is a `https://<ref>.supabase.co` host). A local stack is only for the write-bound suites, which refuse any database not marked disposable: `supabase start`, `supabase status -o env` for the keys, `SUPABASE_TEST_EPHEMERAL=1` in `.env.test.local`; ports are in `supabase/config.toml` (API 54321, database 54322).

Migrations are applied through `apply.yml` before the merge, never by the merge [production-asks-don]: a merge that landed ahead of its migration took production down (2026-09-21).

## 5. Windows

- No symlinks in this repo, so `core.symlinks` and developer mode are not needed.
- Neither repo has a `.gitattributes`: `git config --global core.autocrlf input` before cloning, or every `.sh` in `scripts/` fails with `bad interpreter`.
- Run the scripts under WSL or Git Bash (`#!/usr/bin/env bash`, `set -euo pipefail`), not PowerShell.

## 6. Claude Code permissions

`.claude/settings.json` allows `gh pr merge` and `gh pr edit`, so Code merges green PRs without an unblock per PR. It is committed on purpose: `.gitignore` ignores `.claude/*` and re-includes that one file. `.claude/skills/` stays ignored; `bash ~/Projects/skills/link.sh` symlinks skills per machine.

## 7. What does not travel

Scheduled tasks, installed skills, plugins, Claude Code settings beyond the committed file, `gh` auth, every `.env`. Set each machine up once; none of it syncs.

## 8. Handoff

Pull before you start and push before you stop, every repo, branches included: a branch left local is work the other machine cannot see.

## Verify

```
cd ~/Projects/socialus-plan && bash scripts/lint.sh          # expect: lint: clean
cd ~/Projects/socialus-plan && bash scripts/status.sh >/dev/null && echo ok
cd ~/Projects/socialus-web && npm ci && npm test && npm run build
```

If `status.sh` fails, in this order: `gh` not authenticated, the repos not siblings, `jq` or `python3` missing.
