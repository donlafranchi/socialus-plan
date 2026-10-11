#!/usr/bin/env python3
"""The PM's phone UAT is a short list of journeys; the criteria stay underneath as the agents' layer.
planning/uat-journeys.json maps each journey to its criteria. One tick on a journey = "PM looked" on every criterion under it.
The PM only ever sees the next SHOW unticked journeys: the ones that unlock the most items first, launch-blocking breaking ties. Usage:
  python3 scripts/uat_journeys.py --check          every UAT criterion is in exactly one journey, <=5 look-for points
  python3 scripts/uat_journeys.py --body           print the new #519 body (keeps ticks read from the live Issue)
  python3 scripts/uat_journeys.py --edit [--issue N]  write that body to #519"""
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


def open_issues():
    """Open socialus-web Issues named `F### · ...`: (number, fid, criterion numbers named in the title, launch-blocking)."""
    r = subprocess.run(['gh', 'issue', 'list', '-R', WEB, '-s', 'open', '-L', '600', '--json', 'number,title,labels'], capture_output=True, text=True)
    out = []
    for i in json.loads(r.stdout or '[]'):
        m = re.match(r'^(F\d{3}) · (.*)', i['title'])
        if not m or any(l['name'] == 'uat' for l in i['labels']):
            continue
        nums = set(re.findall(r'\d+', re.sub(r'^.*?criteri(?:on|a)', '', m.group(2))[:60])) if re.search(r'criteri', m.group(2)) else set()
        out.append((i['number'], m.group(1), nums, any(l['name'] == 'launch-blocking' for l in i['labels'])))
    return out


def unlock(j, todo, issues):
    """What the PM's tick on journey j moves. criteria: marked "PM looked". closes: open Issues (check, guard or build tickets, closed by agents) naming one of those criteria.
    queued: other open Issues on a feature whose last unlooked criteria this journey covers (the feature is then fully looked)."""
    mine = {tuple(c.split('.', 1)) for c in j['criteria']}
    left = {tuple(c.split('.', 1)) for t in todo for c in t['criteria']}
    fids = {f for f, _ in mine}
    done_feats = {f for f in fids if {k for k in left if k[0] == f} <= mine}
    closes = {n for n, f, nums, _ in issues if any((f, x) in mine for x in nums)}
    queued = {n for n, f, nums, _ in issues if f in done_feats and n not in closes}
    return {'criteria': len(mine), 'closes': len(closes), 'queued': len(queued), 'items': len(mine) + len(closes) + len(queued)}


def unlock_line(u):
    return f"Unlocks: {u['items']} items ({u['criteria']} checks marked looked, {u['closes']} open Issues on them, {u['queued']} build tickets queued behind them)"


def nxt(done, journeys=None, n=SHOW, issues=None):
    """The next n unticked journeys: most items unlocked first, launch-blocking breaking ties, file order after that.
    Recomputed from the live ticks and open Issues every time, so it re-ranks after each tick."""
    js = journeys or load()
    todo = [j for j in js if j['id'] not in done]
    for j in todo:
        j['unlock'] = unlock(j, todo, issues or [])
    return sorted(todo, key=lambda j: (-j['unlock']['items'], not j['launch']))[:n]


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
    show = nxt(done, js, n, open_issues())
    out = [HEAD, '# Phone UAT: your next checks', '',
           f"{len(done)} of {len(js)} walk-throughs done. Each is about 3 minutes. **Tick a box when what you see matches the points under it.** "
           "Something off? Leave it empty and reply here with one sentence; the agents find the exact check and file the bug.", '',
           '**Anything that reports, removes, hides or publishes: do it on a Page you made for testing, never a real one.** Signed-out steps: use a private tab.', '']
    for j in show:
        out.append(f"- [ ] {j['id']} · **{j['title']}** · as {j['role']} · ~{j['minutes']} min · [open]({j['link']})" + (' · launch' if j['launch'] else ''))
        out += [f"  - {p}" for p in j['look']] + [f"  - _{unlock_line(j['unlock'])}_"]
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
    if '--issue' in a:
        ISSUE = int(a[a.index('--issue') + 1])
    n = SHOW
    if '--check' in a:
        bad = check()
        print('\n'.join(bad) or f'ok: {len(load())} journeys, {sum(len(j["criteria"]) for j in load())} criteria, each in exactly one')
        sys.exit(1 if bad else 0)
    if '--body' in a:
        print(body(live_done(), n))
    if '--edit' in a:
        b = body(live_done(), n)
        cur = subprocess.run(['gh', 'issue', 'view', str(ISSUE), '-R', WEB, '--json', 'body', '-q', '.body'], capture_output=True, text=True).stdout
        if cur.strip() == b.strip():
            print('unchanged'); sys.exit(0)
        subprocess.run(['gh', 'issue', 'edit', str(ISSUE), '-R', WEB, '--body', b], check=True)
        print('edited', ISSUE)
