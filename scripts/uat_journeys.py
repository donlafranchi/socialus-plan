#!/usr/bin/env python3
"""The PM's phone UAT is a short list of journeys; the criteria stay underneath as the agents' layer.
planning/uat-journeys.json maps each journey to its criteria. One tick on a journey = "PM looked" on every criterion under it.
The PM only ever sees the next SHOW unticked journeys (launch-blocking first). Usage:
  python3 scripts/uat_journeys.py --check          every UAT criterion is in exactly one journey, <=5 look-for points
  python3 scripts/uat_journeys.py --body [N]       print the new #519 body (keeps ticks read from the live Issue)
  python3 scripts/uat_journeys.py --edit [N]       write that body to #519"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FILE = os.path.join(HERE, '..', 'planning', 'uat-journeys.json')
WEB, ISSUE, SHOW = 'donlafranchi/socialus-web', 519, 4
HEAD = ("**Kind:** chore\n**Scenario:** none\n**Path:** well-worn: a short click-through sign-off, as in a UAT sheet; GitHub task lists tick from a phone.\n")


def load():
    return json.load(open(FILE))


def ticks(body):
    return set(re.findall(r'^\s*[-*]\s+\[[xX]\]\s+(J\d\d)\b', body or '', re.M))


def criteria_of(jid, journeys=None):
    for j in journeys or load():
        if j['id'] == jid:
            return [tuple(c.split('.', 1)) for c in j['criteria']]
    return []


def nxt(done, journeys=None, n=SHOW):
    todo = [j for j in (journeys or load()) if j['id'] not in done]
    return sorted(todo, key=lambda j: not j['launch'])[:n]   # stable: file order within each group


def check(journeys=None):
    js = journeys or load()
    seen, bad = {}, []
    for j in js:
        if not 1 <= len(j['look']) <= 5:
            bad.append(f"{j['id']}: {len(j['look'])} look-for points (want 1-5)")
        for c in j['criteria']:
            if c in seen:
                bad.append(f"{c} in {seen[c]} and {j['id']}")
            seen[c] = j['id']
        if re.search(r'\bF\d{3}', ' '.join([j['title']] + j['look'])):
            bad.append(f"{j['id']}: a criterion id leaks into the PM's text")
    return bad


def body(done, n=SHOW):
    js = load()
    show = nxt(done, js, n)
    out = [HEAD, '# Phone UAT: your next checks', '',
           f"{len(done)} of {len(js)} walk-throughs done. Each is about 3 minutes. **Tick a box when what you see matches the points under it.** "
           "Something off? Leave it empty and reply here with one sentence; the agents find the exact check and file the bug.", '',
           '**Anything that reports, removes, hides or publishes: do it on a Page you made for testing, never a real one.** Signed-out steps: use a private tab.', '']
    for j in show:
        out.append(f"- [ ] {j['id']} · **{j['title']}** · as {j['role']} · ~{j['minutes']} min · [open]({j['link']})" + (' · launch' if j['launch'] else ''))
        out += [f"  - {p}" for p in j['look']]
    if not show:
        out.append('All walk-throughs done. Nothing waiting on you here.')
    rest = len(js) - len(done) - len(show)
    if rest > 0:
        out += ['', f"{rest} more come after these. They appear as you tick."]
    if done:
        out += ['', f"<details><summary>Done ({len(done)})</summary>", ''] + [f"- [x] {j['id']} · {j['title']}" for j in js if j['id'] in done] + ['', '</details>']
    out += ['', '_Kept by the `regen-uat-checklist` skill from `socialus-plan/planning/uat-journeys.json`. Ticks are kept; behind each walk-through the agents hold the individual checks._']
    return '\n'.join(out) + '\n'


def live_done():
    r = subprocess.run(['gh', 'issue', 'view', str(ISSUE), '-R', WEB, '--json', 'body', '-q', '.body'], capture_output=True, text=True)
    return ticks(r.stdout)


if __name__ == '__main__':
    a = sys.argv[1:]
    n = int(a[1]) if len(a) > 1 else SHOW
    if '--check' in a:
        bad = check()
        print('\n'.join(bad) or f'ok: {len(load())} journeys, {sum(len(j["criteria"]) for j in load())} criteria, each in exactly one')
        sys.exit(1 if bad else 0)
    if '--body' in a:
        print(body(live_done(), n))
    if '--edit' in a:
        b = body(live_done(), n)
        subprocess.run(['gh', 'issue', 'edit', str(ISSUE), '-R', WEB, '--body', b], check=True)
        print('edited', ISSUE)
