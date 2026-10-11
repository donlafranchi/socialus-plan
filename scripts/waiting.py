#!/usr/bin/env python3
"""Everything on GitHub that is waiting on the PM, grouped by area, each with a one-line "what you're deciding".
Sources: needs-pm Issues and open human-review / needs-don PRs in socialus-web; open meta-change PRs awaiting pm-approved and open
decision PRs in socialus-plan, socialus-ops and skills; the next unticked journeys of the phone checklist (the `uat` Issue #519).
Usage: python3 scripts/waiting.py [--json]"""
import json, os, re, subprocess, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uat_journeys

OWNER = 'donlafranchi'
WEB, PLAN, OPS, SKILLS = (f'{OWNER}/{r}' for r in ('socialus-web', 'socialus-plan', 'socialus-ops', 'skills'))
OPS_PLAN = 'Ops & plan'
DECISION = re.compile(r'A/B/C|waits? on the PM|waiting on the PM|for the PM\'s|the PM\'s (?:A/B|decision|OK|yes)|Don\'s decision|needs the PM|for Don|PM to (?:decide|rule|approve)', re.I)


ERRORS = []
UAT = {'total': 0, 'ticked': 0, 'start': None, 'next': []}   # the phone checklist as a whole, and the first sitting with an unticked box


def gh_slug(t):
    """GitHub's heading anchor: lower case, punctuation removed, each space a hyphen."""
    return re.sub(r'[^\w\- ]', '', t.strip().lower()).replace(' ', '-')


def gh(*a):
    """Returns parsed JSON. A call gh cannot make (a private repo the token cannot read, no network) is recorded in ERRORS, never swallowed."""
    r = subprocess.run(['gh', *a], capture_output=True, text=True)
    if r.returncode != 0:
        repo = a[a.index('-R') + 1] if '-R' in a else '?'
        ERRORS.append(f"{repo}: {a[0]} {a[1]} could not be read ({(r.stderr or 'no output').strip().splitlines()[-1][:90]})")
        return []
    try:
        return json.loads(r.stdout)
    except ValueError:
        return []


def clip(t, n=150):
    t = re.sub(r'\s+', ' ', re.sub(r'[*`]|\[([^\]]+)\]\([^)]*\)', lambda m: m.group(1) or '', t or '')).strip()
    return t if len(t) <= n else t[:n - 1].rstrip() + '…'


def ask(body, title):
    """The one line that says what the PM is deciding."""
    b = body or ''
    for pat in (r'Question for (?:Don|the PM):\**\s*(.+)', r'\*\*Decision for (?:the PM|you)\*\*:?\s*(.+)', r'Decision for (?:the PM|you):?\s*\n+\s*[-*]?\s*(.+)',
                r'needs-pm:\s*(.+)', r'Review on socialus\.org after merge:\**\s*(.+)'):
        m = re.search(pat, b, re.I)
        if m:
            return clip(m.group(1))
    lines = [l for l in b.split('\n') if l.strip() and not re.match(r'^\s*(\*\*)?(Kind|Scenario|Path|Gates|Refs|Closes)\b', l) and not l.startswith(('#', '>', '```'))]
    return clip(lines[0] if lines else title)


def area_of(labels):
    for l in labels:
        n = l['name'] if isinstance(l, dict) else l
        if n.startswith('area:'):
            return n[5:]
    return None


def collect(feat_area):
    """feat_area: {F###: area} from the criterion roll-up. Returns {area: [item]}."""
    out = {}
    def add(area, kind, title, url, why):
        out.setdefault(area or OPS_PLAN, []).append({'kind': kind, 'title': clip(title, 90), 'url': url, 'ask': why})
    # 1. needs-pm Issues
    for i in gh('issue', 'list', '-R', WEB, '-l', 'needs-pm', '-s', 'open', '-L', '200', '--json', 'number,title,body,labels,url'):
        add(area_of(i['labels']), 'needs-pm Issue', f"#{i['number']} {i['title']}", i['url'], ask(i['body'], i['title']))
    # 2. PRs labelled human-review or needs-don (open only: these are waiting)
    seen = set()
    for lab in ('human-review', 'needs-don'):
        for p in gh('pr', 'list', '-R', WEB, '-l', lab, '-s', 'open', '-L', '100', '--json', 'number,title,body,labels,url'):
            if p['number'] in seen:
                continue
            seen.add(p['number'])
            add(area_of(p['labels']), f'{lab} PR', f"PR #{p['number']} {p['title']}", p['url'], ask(p['body'], p['title']))
    # 3. meta-change PRs waiting on pm-approved, and 5. decision PRs in plan / ops / skills
    for repo in (PLAN, OPS, SKILLS, WEB):
        for p in gh('pr', 'list', '-R', repo, '-s', 'open', '-L', '100', '--json', 'number,title,body,labels,url,isDraft'):
            names = {l['name'] for l in p['labels']}
            short = repo.split('/')[1]
            if 'meta-change' in names and 'pm-approved' not in names:
                name = re.sub(r'^meta-change:\s*', '', p['title'])
                add(None, 'meta-change PR', f"{short} #{p['number']} {name}", p['url'],
                    'Approve by applying the pm-approved label, or close it.')
            elif repo != WEB and not p['isDraft'] and (DECISION.search(p['body'] or '') or names & {'needs-pm', 'human-review', 'needs-don'}):
                add(None, 'decision PR', f"{short} #{p['number']} {p['title']}", p['url'], ask(p['body'], p['title']))
    # 4. the phone checklist (UAT): journeys, only the next few unticked, launch-blocking first
    UAT.update({'total': 0, 'ticked': 0, 'start': None, 'next': []})
    js = uat_journeys.load()
    done, url = set(), None
    for i in gh('issue', 'list', '-R', WEB, '-l', 'uat', '-s', 'open', '-L', '50', '--json', 'number,title,body,url'):
        if 'self-check' in i['title']:
            continue
        done |= uat_journeys.ticks(i['body'])
        url = url or i['url']
    UAT.update({'total': len(js), 'ticked': len(done & {j['id'] for j in js}), 'done': sorted(done)})
    for j in uat_journeys.nxt(done, js, issues=uat_journeys.open_issues()):
        item = {'id': j['id'], 'title': j['title'], 'role': j['role'], 'minutes': j['minutes'], 'link': j['link'], 'look': j['look'], 'launch': j['launch'], 'url': url, 'unlock': uat_journeys.unlock_line(j['unlock'])}
        UAT['next'].append(item)
        a = feat_area.get(j['criteria'][0].split('.')[0])
        add(a, 'UAT', f"{j['title']} (as {j['role']}, about {j['minutes']} min)", url,
            'Tick it when it matches. If not, reply with one sentence on what you saw; the bug is filed for you.')
    UAT['start'] = UAT['next'][0] if UAT['next'] else None
    for items in out.values():   # UAT first in every list
        items.sort(key=lambda it: it['kind'] != 'UAT')
    return out


if __name__ == '__main__':
    print(json.dumps(collect({}), indent=1))
