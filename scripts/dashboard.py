#!/usr/bin/env python3
"""Writes DASHBOARD.md (plain text, no colour) and dashboard/status-dashboard.html (the colour) from socialus-web Issues and PRs (gh).
Same layout and stage rules every run. Each area also lists what happened in the past shift (PRs, issues, migrations, decisions).
Usage: python3 scripts/dashboard.py [repo-root] [--since 12h]   (defaults: cwd, 12h = one shift)"""
import json, os, re, subprocess, sys
from datetime import datetime, date, timedelta, timezone
from zoneinfo import ZoneInfo

REPO = 'donlafranchi/socialus-web'
MILESTONE = 'Beta 11-06'
FREEZE = date(2026, 10, 30)
LIVE = 'https://socialus.org'
AREAS = ['page-editing', 'sign-in-you', 'explore-map', 'create-posts',
         'sharing-links', 'builders-seed', 'moderation', 'ops']
STAGES = ['Scenario approved', 'Built', 'Reviewed', 'Shipped', 'Smoke', 'PM looked']
GREEN = {'SUCCESS', 'SKIPPED', 'NEUTRAL'}
RED = {'FAILURE', 'TIMED_OUT', 'CANCELLED', 'ERROR', 'ACTION_REQUIRED', 'STARTUP_FAILURE'}


def gh(*args):
    out = subprocess.run(['gh', *args], check=True, capture_output=True, text=True).stdout
    return json.loads(out)


def labels(x):
    return {l['name'] for l in x.get('labels', [])}


def link(n):
    return f'[#{n}](https://github.com/{REPO}/issues/{n})'


def first_live_url(*texts):
    for t in texts:
        m = re.search(r'https://[^\s)>\]]*socialus\.org[^\s)>\]]*', t or '')
        if m:
            return m.group(0).rstrip('.,')
    return None


issues = gh('issue', 'list', '-R', REPO, '--state', 'all', '--milestone', MILESTONE,
            '--limit', '500', '--json', 'number,title,state,labels,body,url')
open_bugs = gh('issue', 'list', '-R', REPO, '--state', 'open', '--label', 'bug',
               '--limit', '500', '--json', 'number,title,body')
prs = gh('pr', 'list', '-R', REPO, '--state', 'all', '--limit', '300',
         '--json', 'number,title,body,state,mergedAt,labels,'
                   'closingIssuesReferences,headRefName,mergeCommit,createdAt')
all_issues = gh('issue', 'list', '-R', REPO, '--state', 'all', '--limit', '300',
                '--json', 'number,title,state,labels,createdAt,closedAt')


def runs_of(workflow):
    # {commit sha: conclusion}; None when the workflow does not exist yet.
    try:
        rs = gh('run', 'list', '-R', REPO, '--workflow', workflow, '--limit', '200', '--json', 'headSha,conclusion,status')
    except subprocess.CalledProcessError:
        return None
    return {r['headSha']: (r['conclusion'] or r['status']) for r in rs}


DEPLOY = runs_of('Deploy health') or {}
SMOKE = runs_of('smoke-live.yml')
PLAN = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
NEEDS_REVIEW = re.compile(r'^(src/(app|components|actions)/|supabase/)')
TESTISH = re.compile(r'\.test\.tsx?$')


def ok(x):
    return x in ('●', '·')

by_issue = {}
for p in prs:
    refs = {r['number'] for r in p.get('closingIssuesReferences') or []}
    m = re.match(r'^(?:bug|change|chore|fix)[^#:]*#(\d+)', p['title'], re.I)
    if m:
        refs.add(int(m.group(1)))
    m = re.match(r'^(?:bug-|change-|chore-)?(\d+)-', p['headRefName'] or '')
    if m:
        refs.add(int(m.group(1)))
    for n in refs:
        by_issue.setdefault(n, []).append(p)


def best_pr(n):
    cands = by_issue.get(n, [])
    merged = sorted((p for p in cands if p['mergedAt']), key=lambda p: p['mergedAt'])
    if merged:
        return merged[-1]
    opened = [p for p in cands if p['state'] == 'OPEN']
    return max(opened, key=lambda p: p['number']) if opened else None


def ci(pr):
    # CI check status from statusCheckRollup - simplified, returns ?
    return '?'


def scenario_stage(i, built):
    body = i.get('body') or ''
    m = re.search(r'Scenario:\**\s*(F\d{3})', body, re.I) or re.match(r'^(F\d{3})\b', i['title'])
    if not m:
        return '·'
    path = os.path.join(PLAN, 'planning', f'scenario-{m.group(1).upper()}.md')
    if not os.path.exists(path):
        # A shipped scenario is deleted at sync; before that, a missing file is unknown.
        return '●' if built else '?'
    head = open(path).read(600)
    st = re.search(r'^status:\s*(\w+)', head, re.M)
    return '●' if st and st.group(1) in ('approved', 'building') else ('○' if st else '?')


def stages(i):
    n = i['number']
    pr = best_pr(n)
    is_bug = 'bug' in labels(i)
    merged = bool(pr and pr['mergedAt']) or (is_bug and i['state'] == 'CLOSED')
    built = '●' if merged else '○'
    scenario = scenario_stage(i, merged)
    # Reviewed: always '·' since we no longer check files
    reviewed = '●' if pr and 'Reviewed by:' in (pr.get('body') or '') and 'review-skipped' not in labels(pr) else '·'
    # Shipped: merged, and the deploy-health run for the merge commit is green.
    if not merged:
        shipped = smoke = '○'
    else:
        sha = ((pr or {}).get('mergeCommit') or {}).get('oid')
        d = DEPLOY.get(sha) if sha else None
        shipped = '?' if d is None else ('●' if d == 'success' else '○')
        sm = SMOKE.get(sha) if (SMOKE is not None and sha) else None
        smoke = '?' if sm is None else ('●' if sm == 'success' else '○')
    pm = '●' if 'pm-reviewed' in labels(i) or (pr and 'pm-reviewed' in labels(pr)) else '○'
    if is_bug:
        bugs = i['state'] == 'CLOSED'
    else:
        pat = re.compile(rf'#{n}\b')
        bugs = not any(pat.search((b['title'] or '') + ' ' + (b['body'] or '')) for b in open_bugs)
    s = [scenario, built, reviewed, shipped, smoke, pm]
    done = all(ok(x) for x in s) and merged and bugs
    return s, pr, done


# Criterion-level results: read from build-log/reports/rollup.json in socialus-web (scripts/criteria.py), not derived from Issues.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
try:
    import criteria
    import launch_checklist
    import waiting
    import uat_journeys
    FEATS = criteria.load()
    UNIVERSE = criteria.universe()
except Exception as e:
    FEATS, UNIVERSE = [], set()
    launch_checklist = None
    waiting = None
    uat_journeys = None
    print('criteria: could not read criterion reports:', e)
COVER = (len({f['id'] for f in FEATS}), len(UNIVERSE | {f['id'] for f in FEATS}))

rows = []
for i in issues:
    area = next((l[5:] for l in labels(i) if l.startswith('area:')), None)
    st, pr, is_done = stages(i)
    rows.append({'n': i['number'], 'title': re.sub(r'^(change|bug|chore) · ', '', i['title']),
                 'area': area, 'st': st, 'done': is_done, 'pr': pr, 'open': i['state'] == 'OPEN',
                 'blocking': 'launch-blocking' in labels(i),
                 'review': first_live_url(i.get('body'), (pr or {}).get('body'))})

args = sys.argv[1:]
since_h = 12
RECORD_LOOK = '--record-look' in args
args = [a for a in args if a != '--record-look']
if '--since' in args:
    k = args.index('--since')
    since_h = int(args[k + 1].rstrip('h'))
    del args[k:k + 2]
SINCE = datetime.now(timezone.utc) - timedelta(hours=since_h)


def recent(ts):
    return bool(ts) and datetime.fromisoformat(ts.replace('Z', '+00:00')) >= SINCE


def area_of(x):
    return next((l[5:] for l in labels(x) if l.startswith('area:')), None)


ISSUE_AREA = {i['number']: area_of(i) for i in all_issues}
SURFACE_AREA = {'pages': 'page-editing', 'page-edit': 'page-editing', 'contact': 'page-editing',
                'moderation': 'moderation', 'reports': 'moderation', 'uploads': 'create-posts',
                'posting': 'create-posts', 'explore': 'explore-map', 'map': 'explore-map',
                'sign-in': 'sign-in-you', 'signup': 'sign-in-you', 'auth': 'sign-in-you',
                'sharing': 'sharing-links', 'links': 'sharing-links', 'seed': 'builders-seed'}


def pr_area(p):
    for n in [r['number'] for r in p.get('closingIssuesReferences') or []] + [n for n, ps in by_issue.items() if p in ps]:
        if ISSUE_AREA.get(n):
            return ISSUE_AREA[n]
    return None


def decision_area(line):
    m = re.search(r'surfaces=([\w,-]+)', line)
    for sf in (m.group(1).split(',') if m else []):
        if sf in SURFACE_AREA:
            return SURFACE_AREA[sf]
    return None


SHIFT = {}  # area (or None) -> [(kind, text, url)]


def log(area, kind, text, url=None):
    SHIFT.setdefault(area, []).append((kind, text, url))


for p in prs:
    a = pr_area(p)
    u = f'https://github.com/{REPO}/pull/{p["number"]}'
    if recent(p['mergedAt']):
        log(a, 'PR merged', f'#{p["number"]} {p["title"]}', u)
        for f in p.get('files') or []:
            if f['path'].startswith('supabase/migrations/'):
                log(a, 'Migration', f'{os.path.basename(f["path"])} (PR #{p["number"]})', u)
    elif recent(p['createdAt']):
        log(a, 'PR opened', f'#{p["number"]} {p["title"]}', u)
for i in all_issues:
    u = f'https://github.com/{REPO}/issues/{i["number"]}'
    if recent(i['createdAt']):
        log(area_of(i), 'Issue filed', f'#{i["number"]} {i["title"]}', u)
    if i['state'] == 'CLOSED' and recent(i['closedAt']):
        log(area_of(i), 'Issue closed', f'#{i["number"]} {i["title"]}', u)
try:
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    import markers
    _cwd = os.getcwd(); os.chdir(PLAN)
    _rulings = [e['line'] + (f" [{e['lasts']}]" if e['lasts'] and f"[{e['lasts']}]" not in e['line'] else '') for e in markers.decisions()]
    os.chdir(_cwd)
    for line in _rulings:
        m = re.match(r'- \*\*(\d{4}-\d{2}-\d{2}) — (.*?)\*\*', line)
        if m and m.group(1) >= SINCE.astimezone(ZoneInfo('America/Los_Angeles')).strftime('%Y-%m-%d'):
            _t = re.search(r'\[(always|for now)\]', line)
            log(decision_area(line), 'Decision', m.group(2)[:140] + ('…' if len(m.group(2)) > 140 else '') + (f' [{_t.group(1)}]' if _t else ''))
except OSError:
    pass


def shift_md(items):
    return [f'- **{k}:** ' + (f'[{t}]({u})' if u else t) for k, t, u in items]


COLORS = ['#2563eb', '#0d9488', '#7c3aed', '#ea580c', '#65a30d', '#ca8a04']
OFF, UNK = '#d1d5db', '#fde68a'

# Read #519 testing checkboxes
test_items = []
try:
    issue_519 = gh('issue', 'view', '-R', REPO, '519', '--json', 'title,body')
    body = issue_519.get('body', '')
    # Parse markdown checkboxes: - [x] text or - [ ] text
    for line in body.split('\n'):
        m = re.match(r'-\s+\[(.)\]\s+(.+)', line)
        if m:
            checked = m.group(1) == 'x'
            text = m.group(2)
            # Extract URL if present
            url_match = re.search(r'https://[^\s)]+', text)
            url = url_match.group(0) if url_match else None
            # Extract link text
            link_match = re.search(r'\[([^\]]+)\]', text)
            if link_match:
                text = link_match.group(1)
            test_items.append({'checked': checked, 'text': text, 'url': url})
except Exception as e:
    test_items = []
    TEST_NOTICE = f'Testing list unavailable: could not read #519 ({e}).'
if not test_items and not globals().get('TEST_NOTICE'):
    TEST_NOTICE = 'Testing list is empty: Issue #519 has no checkboxes (- [ ] / - [x] lines), so there is nothing to tick or count.'

# Live testing (ported from the superseded #67): one `uat` Issue per feature, one box per criterion (record-pm-review).
# #519 is a control sheet: linked, not counted.
uat_items = []
try:
    for i in gh('issue', 'list', '-R', REPO, '-l', 'uat', '-s', 'all', '-L', '200', '--json', 'number,title,state,body,url'):
        if 'self-check' in i['title']:
            continue
        bx = [(m.group(1).lower() == 'x', m.group(2)) for m in (re.match(r'\s*[-*]\s+\[([ xX])\]\s+(.+)', l) for l in (i.get('body') or '').split('\n')) if m]
        mf = re.search(r'\b(F\d{3})\b', i['title'])
        uat_items.append({'n': i['number'], 'title': i['title'], 'state': i['state'], 'url': i['url'], 'feature': mf.group(1) if mf else None,
                          'done': sum(1 for c, _ in bx if c), 'total': len(bx)})
except Exception as e:
    UAT_ERR = str(e)
if globals().get('UAT_ERR'):
    TEST_NOTICE = f'UAT Issues unavailable: {UAT_ERR}'
elif not uat_items:
    TEST_NOTICE = (globals().get('TEST_NOTICE', '') + ' ' if globals().get('TEST_NOTICE') else '') + 'No UAT Issue exists yet (one per feature, from record-pm-review), so PM looked cannot move from these; it counts only pm-reviewed labels.'

root = args[0] if args else '.'
now = datetime.now(ZoneInfo('America/Los_Angeles'))
days = (FREEZE - now.date()).days
total = len(rows)
done = sum(1 for r in rows if r['done'])
stage_totals = ' · '.join(f'{STAGES[k]} {sum(1 for r in rows if (r["st"][k] == "●" if k == 2 else ok(r["st"][k])))}/{total}' for k in range(6))
ROLL = criteria.rollup(FEATS) if FEATS else {'areas': {}, 'milestone': {'met': 0, 'total': 0, 'features': 0, 'red': 0, 'pct': 0}}
MS = ROLL['milestone']
issues_closed = sum(1 for r in rows if not r['open'])
header = f'{MILESTONE} · {days} days to freeze · criterion roll-up: {MS["met"]}/{MS["total"]} criteria met ({MS["pct"]}%), checked {MS.get("checked", 0)}, reviewed {MS.get("reviewed", 0)}, smoked {MS.get("smoked", 0)}, PM looked {MS.get("pm", 0)}' + (f', PM: not OK {MS["not_ok"]}' if MS.get('not_ok') else '') + f' across {MS["features"]} features, {MS["red"]} red, {sum(1 for f in FEATS if f.get("stale"))} reports stale · Issues closed {issues_closed}/{total} (alongside, not the headline) · updated {now.strftime("%Y-%m-%d %H:%M")} PT'

areas = []
behind = []
for a in AREAS:
    rs = sorted((r for r in rows if r['area'] == a), key=lambda r: r['n'])
    filled = 0
    for k in range(6):
        if rs and all(ok(r['st'][k]) for r in rs):
            filled += 1
        else:
            break
    counts = [sum(1 for r in rs if (r['st'][k] == '●' if k == 2 else ok(r['st'][k]))) for k in range(6)]
    unknown = sum(1 for r in rs if '?' in r['st'])
    if not rs:
        note = 'no beta items'
    else:
        note = f'{counts[1]} of {len(rs)} built'
        if filled < 6:
            note += f'; {sum(1 for r in rs if not ok(r["st"][filled]))} waiting on {STAGES[filled]}'
        if unknown:
            note += f'; {unknown} with a ?'
        if any(r['blocking'] and r['open'] and r['st'][1] != '●' for r in rs):
            behind.append(a)
    areas.append({'name': a, 'rows': rs, 'filled': filled, 'counts': counts, 'note': note, 'crit': ROLL['areas'].get(a),
                  'done': sum(1 for r in rs if r['done']), 'shift': SHIFT.get(a, [])})

if not behind:
    present = [x for x in areas if x['rows']]
    overall = sum(1 for r in rows if r['st'][1] == '●') / max(1, total)
    behind = [x['name'] for x in present if x['counts'][1] / len(x['rows']) < overall]

nxt = next((r for r in sorted(rows, key=lambda r: (not r['blocking'], r['n']))
            if r['open'] and all(ok(x) for x in r['st'][:5]) and r['st'][5] != '●'), None)
unassigned = [r for r in rows if r['area'] is None]


def pr_url(r):
    return f'https://github.com/{REPO}/pull/{r["pr"]["number"]}' if r['pr'] else None


def issue_url(n):
    return f'https://github.com/{REPO}/issues/{n}'


# Everything waiting on the PM, by area (scripts/waiting.py): needs-pm Issues, human-review and needs-don PRs, meta-change PRs, decision PRs, unticked checklist boxes.
try:
    WAIT = waiting.collect({f['id']: f['area'] for f in FEATS})
except Exception as e:
    WAIT = {}
    print('waiting: could not read GitHub:', e)
WAIT_AREAS = AREAS + [waiting.OPS_PLAN if waiting else 'Ops & plan']
WAIT_TOTAL = sum(len(v) for v in WAIT.values())
def depth(c):
    """How many checks a criterion has passed: 0 not built, then built, checked, reviewed, smoked, PM looked."""
    return 0 if c['built'] != 'yes' else 1 + sum(c[k] == 'yes' for k in ('checked', 'reviewed', 'smoked', 'pm'))


def glyph(c):
    if c.get('not_ok'):
        return '❌'
    if c['blocking']:
        return '🟥'
    return '░▒▓▓██'[depth(c)]


GLYPH_KEY = '░ not built · ▒ built · ▓ checked or reviewed · █ smoked or PM looked · 🟥 launch-blocking unmet · ❌ PM: not OK'
_slug = lambda n: re.sub(r'[^a-z0-9 -]', '', n.lower()).replace(' ', '-')
out = ['> **SETTLED — do not re-raise:** members are the investors and the only people paid out. "Ownership, not profit-share" is rejected. Legal/securities questions about this go to `socialus-legal` for counsel and never come back to the PM as a decision. SocialUs takes transaction income; any \'no fee\' language is retired.', '', f'# {header}', '',
       f'**As of {now:%Y-%m-%d}** · Source: criterion reports, GitHub Issues and PRs, planning/uat-journeys.json · Generated by: `scripts/dashboard.py`', '', '*Never hand-edited. The table below counts Issues by stage (older view, kept for reference); the bars and headline are per criterion. Colour view with tappable criteria: `dashboard/status-dashboard.html`.*', '',
       '| Area | Criteria met | ' + ' | '.join(STAGES) + ' | Note |', '|---|---|' + '---|' * 7]
_ti = next(i for i, l in enumerate(out) if l.startswith('| Area | Criteria met'))
_u = waiting.UAT if waiting else {'total': 0, 'ticked': 0, 'start': None, 'next': []}
_uat_line = (f"**Your UAT: {_u['ticked']} of {_u['total']} walk-throughs done**" + (' · next up:' if _u['next'] else ' · all done')) if _u['total'] else '**Your UAT:** no phone checklist found.'
_uat_next = [f"{k}. [{x['title']}]({x['url']}) · as {x['role']} · about {x['minutes']} min" + (' · launch' if x['launch'] else '') + f" · {x['unlock']}" for k, x in enumerate(_u['next'], 1)]
HOW = ['**How to read this**',
       '1. Area → Feature → Journey → Criterion. Each bar is one square per criterion (the agents\' unit); the darker the square, the more checks it has passed. Journeys are your checks, shown below by area.',
       '2. Light to dark: built, checked (a test covers it), reviewed, smoked (live pages still load), PM looked (you ticked it). Grey is not built.',
       '3. Red: a launch-blocking criterion is unmet. Red stripes or ❌: you marked it **PM: not OK** (a bug is filed).',
       '4. Each area has its own colour; the headline is criteria met / total. Issues closed sits beside it, not as the headline.',
       '5. "Waiting on you" is what needs your decision, UAT first: tick a walk-through when it matches, or reply with one sentence on what was off.']
out[_ti:_ti] = ['', *HOW, '', _uat_line, '', *_uat_next, '', f'**Waiting on you: {WAIT_TOTAL}** · ' + ' · '.join(f'[{n} ({len(WAIT.get(n, []))})](#{_slug(n)})' for n in WAIT_AREAS), '', GLYPH_KEY, '']
for x in areas:
    n = len(x['rows'])
    cells = ' | '.join(f'{c}/{n}' for c in x['counts'])
    cr = x['crit']
    crit_cell = (f"{cr['met']}/{cr['total']} ({round(100 * cr['met'] / cr['total'])}%)" + (f" RED {cr['red']}" if cr['red'] else '') + f" · {cr['features']} features") if cr and cr['total'] else 'no criterion reports'
    out.append(f'| {x["name"]} | {crit_cell} | {cells} | {x["note"]} |')
out.append(f'| **All** | **{MS["met"]}/{MS["total"]} ({MS["pct"]}%)** · {MS["features"]} features | ' + ' | '.join(f'**{sum(1 for r in rows if (r["st"][k] == "●" if k == 2 else ok(r["st"][k])))}/{total}**' for k in range(6)) + ' | each phase counted on its own |')
out.append('')
out.append('Stages, in order: ' + ' → '.join(f'**{s}**' for s in STAGES) + '.')
# Launch checklist: dated reminders that fire at an event or a date (planning/launch-checklist.json).
try:
    LAUNCH = launch_checklist.load()
except Exception as e:
    LAUNCH = []
    problems_launch = f'launch checklist could not be read: {e}'
if LAUNCH:
    out += ['', '## Launch checklist', ''] + [(f"- **DUE ({', '.join(i['fired_by'])}):** {i['text']} [Runbook]({i['runbook']})" if i['due'] else f"- Fires at {i['waiting_on']}, whichever comes first: {i['text']}" + (f" ({i['days_to_date']} days to the date trigger.)" if i['days_to_date'] is not None else '')) for i in LAUNCH]
# Data problems (ported from #67): every unknown and every missing report, so none is mistaken for progress.
problems = []
for f in FEATS:
    unk = sum(1 for r in f['criteria'] if r['built'] == 'unknown')
    if unk:
        problems.append(f"{f['id']} {f['title']}: {unk} criteria have Built unknown and count as unmet")
    if f.get('stale'):
        problems.append(f"{f['id']} {f['title']}: its report is older than its last merged PR")
for _m in sorted(UNIVERSE - {f['id'] for f in FEATS}):
    problems.append(f'{_m}: reportable but has no criterion report')
for x in areas:
    nq = sum(1 for r in x['rows'] if '?' in r['st'])
    if nq:
        problems.append(f"{x['name']}: {nq} Issues have a ? stage (data not found)")
for _e in (waiting.ERRORS if waiting else ['waiting.py could not be loaded']):
    problems.append('Waiting on you may be incomplete: ' + _e)
if not FEATS:
    problems.append('no criterion reports could be read; the criterion roll-up is empty')
if globals().get('TEST_NOTICE'):
    out += ['', '## Testing', '', f'**{TEST_NOTICE}**']
if uat_items:
    out += ['', '## Live testing (UAT Issues)', '', '| Issue | State | Boxes ticked |', '|---|---|---|'] + [f"| [#{u['n']} {u['title'][:70]}]({u['url']}) | {u['state']} | {u['done']}/{u['total']} |" for u in uat_items]
_fa = {f['id']: f['area'] for f in FEATS}
JR = {}
for _j in uat_journeys.load():
    _x = JR.setdefault(_fa.get(_j['criteria'][0].split('.')[0], 'ops'), {'total': 0, 'looked': 0, 'crit': 0})
    _x['total'] += 1; _x['crit'] += len(_j['criteria']); _x['looked'] += _j['id'] in set(_u.get('done', []))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import going
_later = gh('issue', 'list', '-R', REPO, '--state', 'open', '--milestone', 'After beta', '--limit', '200', '--json', 'number,title,url')
import lost
_cap = os.path.join(root, 'dashboard', 'capabilities.json')
_prev = json.load(open(_cap)) if os.path.exists(_cap) else None
_now = lost.snapshot(FEATS) if FEATS else None
BASELINE_NEW = False
if _now is not None:
    out += [''] + lost.section(_prev, _now)
    BASELINE_NEW = _prev is None   # the criterion baseline moves only when the PM looks (record_look below), or the first time
out += [''] + going.section(going.scenarios(os.path.join(root, 'planning')), sum(1 for i in issues if i['state'] == 'OPEN'), _later, MILESTONE, ideas=going.imagine(os.path.join(root, 'IMAGINE.md')))
out += ['', '## Your review: journeys, by area', '', 'A journey is your 3-minute human check; each sits over the criteria the agents test. Feature progress above is by criteria; this is by journeys. A journey belongs to the area of its first feature.', '', '| Area | Journeys looked | Criteria under them |', '|---|---|---|']
out += [f"| {_a} | {_c['looked']}/{_c['total']} | {_c['crit']} |" for _a, _c in sorted(JR.items())]
out += [f"| **All** | **{sum(c['looked'] for c in JR.values())}/{sum(c['total'] for c in JR.values())}** | **{sum(c['crit'] for c in JR.values())}** |"]
out += ['', '## Data problems', ''] + ([f'- {p}' for p in problems] or ['- none'])
out += ['', '## Criterion roll-up: by phase (each phase counted on its own, per criterion)', '', '| Area | Criteria | Built | Checked | Reviewed | Smoked | PM looked |', '|---|---|---|---|---|---|---|']
for _a, _c in sorted(ROLL['areas'].items()):
    out.append(f"| {_a} | {_c['total']} | {_c['met']} | {_c.get('checked', 0)} | {_c.get('reviewed', 0)} | {_c.get('smoked', 0)} | {_c.get('pm', 0)} |")
out.append(f"| **All** | **{MS['total']}** | **{MS['met']}** | **{MS.get('checked', 0)}** | **{MS.get('reviewed', 0)}** | **{MS.get('smoked', 0)}** | **{MS.get('pm', 0)}** |")
out += ['', f'*Smoked = a green smoke-live run came after the feature\'s last merge. The last green smoke run was {(FEATS[0]["last_green_smoke"] or "never")[:10] if FEATS else "n/a"}; the latest run is {FEATS[0]["last_smoke"] if FEATS else "n/a"}. Smoke loads pages; it does not test criteria.*']
out += ['', f'## Criterion roll-up: features, {COVER[0]} of {COVER[1]} reporting', '',
        '*Read from the criterion reports in socialus-web (`build-log/reports/`), one row per acceptance criterion in each report; not derived from Issues. Met = the code is on main. RED = a launch-blocking criterion is unmet. The colour view with the criterion lists is `dashboard/status-dashboard.html`.*', '',
        '| Area | Feature | Progress | Met | Checked | Reviewed | Smoked | PM looked | Unmet launch-blocking | Report |', '|---|---|---|---|---|---|---|---|---|---|']
for f in sorted(FEATS, key=lambda f: (f['area'], f['id'])):
    red = f"RED: {len(f['blocked'])}" if f['blocked'] else ''
    out.append(f"| {f['area']} | {f['id']} {f['title']} | {''.join(glyph(c) for c in f['criteria'])} | {f['met']}/{f['total']} | {f['checked']}/{f['total']} | {f['reviewed']}/{f['total']} | {f['smoked']}/{f['total']} | {f['pm']}/{f['total']} | {red} | [report]({f['url']}){' STALE: merged after the report' if f.get('stale') else ''} |")
_miss = sorted(UNIVERSE - {f['id'] for f in FEATS})
if _miss:
    out += ['', 'No criterion report yet: ' + ', '.join(_miss) + '.']
if unassigned:
    out += ['', f'*{len(unassigned)} beta item(s) have no `area:` label: ' + ', '.join(f'[#{r["n"]}]({issue_url(r["n"])})' for r in unassigned) + '.*']
def waiting_md(items):
    body = [f"- [{i['title']}]({i['url']}) ({i['kind']}): {i['ask']}" for i in items] or ['- Nothing waiting on you here.']
    return ['<details>', f'<summary><b>Waiting on you ({len(items)})</b></summary>', '', *body, '', '</details>']

_by_area = {x['name']: x for x in areas}
for name in WAIT_AREAS:
    items = WAIT.get(name, [])
    x = _by_area.get(name)
    out += ['', f'## {name}', '']
    if x and x['crit'] and x['crit']['total']:
        cr = x['crit']
        out.append(f"Criterion roll-up: {cr['met']}/{cr['total']} criteria met ({round(100 * cr['met'] / cr['total'])}%) across {cr['features']} features" + (f", {cr['red']} red (a launch-blocking criterion is unmet)" if cr['red'] else '') + '.')
    elif x:
        out.append(f"No criterion reports for this area yet ({len(x['rows'])} Issues in the milestone).")
    else:
        out.append('Docs and process PRs in socialus-plan, socialus-ops and skills, guard-protected meta changes, and anything with no area.')
    if x and x['crit'] and x['crit']['total']:
        _cs = [c for f in FEATS if f['area'] == name for c in f['criteria']]
        out += ['', ''.join(glyph(c) for c in _cs)]
        _no = [(f['id'], c) for f in FEATS if f['area'] == name for c in f['criteria'] if c.get('not_ok')]
        if _no:
            out += ['', f'❌ **PM: not OK ({len(_no)}):** ' + '; '.join(f"{fid}.{c['n']} ({c['not_ok_text'][:70]})" for fid, c in _no) + ' (a bug is filed; clears when you tick the box or comment that it is ok)']
    out += ['', *waiting_md(items)]
out += ['', '**Behind:** ' + (', '.join(behind) if behind else 'none') +
        ' *(an open launch-blocking item not yet built; else below the overall built share)*', '']
if nxt:
    cta = f'Review {nxt["title"]} ([#{nxt["n"]}]({issue_url(nxt["n"])}))' + (f' at [the live page]({nxt["review"]})' if nxt['review'] else '') + ', then label it `pm-reviewed`.'
else:
    cta = 'none: nothing is waiting on you.'
out.append(f'**Your next action:** {cta}')
# Meta-layer trial block (TRIAL, started 2026-10-10): tracker link, trial health, next score. Regenerated each run.
try:
    th = os.path.join(os.environ.get('PROJECTS', os.path.expanduser('~/Projects')), 'socialus-ops', 'scripts', 'trial_health.py')
    block = subprocess.run(['python3', th, '--block'], capture_output=True, text=True, timeout=120).stdout.strip()
except Exception:
    block = ''
out += ['', block or '### Meta-layer trial\n\nUnavailable: `socialus-ops/scripts/trial_health.py` did not run. Tracker: https://github.com/donlafranchi/socialus-ops/issues/89']
# Pipeline health panel (ruling 2026-10-11, socialus-ops #106): the two numbers the PM owns, at the top. The silent alarms
# (main green, reviews happen, nothing closes half-built) show only when a metric has read red in its last two readings.
def pipeline_health():
    ops = os.path.join(os.environ.get('PROJECTS', os.path.expanduser('~/Projects')), 'socialus-ops')
    try:
        undated = json.load(open(os.path.join(ops, 'scores', 'tend-docs', 'latest.json')))['undated']
        docs = f'**Docs current:** {undated} undated (target under 5) {"🟥" if undated >= 5 else "🟩"}'
    except Exception:
        docs = '**Docs current:** unavailable (`socialus-ops/scores/tend-docs/latest.json` unreadable)'
    lines = ['### Pipeline health', '', docs, '', '**Overrule rate** (how often you reverse an agent\'s plan; lower is better): not measured yet, `score-pm-overrule` is not built.']
    try:
        rows = [l.split('\t') for l in open(os.path.join(ops, 'scores', 'history.tsv')).read().splitlines() if l.count('\t') >= 4]
        for metric, what in (('ci_main_fail_pct', 'main stays green'), ('closed_parent_unmet', 'nothing closes half-built')):
            last = [r[4] for r in rows if r[2] == metric][-2:]
            if len(last) == 2 and all(b == 'red' for b in last):
                lines += ['', f'**Alarm still red after two readings:** {what} (`{metric}`).']
    except Exception:
        pass
    return lines + ['']


# The PM cockpit (ruled B, 2026-10-13): facts gathered here, shaped by scripts/cockpit.py, drawn in the md and the colour page alike.
import cockpit, safety
LOOK_FILE = os.path.join(root, 'dashboard', 'last-look.json')
LOOK_ISSUE = 'Cockpit · I have looked'
try:
    LOOK = json.load(open(LOOK_FILE)); LOOK['time'] = datetime.fromisoformat(LOOK['time'])
except (OSError, ValueError, KeyError):
    LOOK = None
_cwd = os.getcwd(); os.chdir(PLAN)
try:
    SAFETY_NOW = safety.snapshot(markers.decisions(), os.environ.get('STATUS_CODE') or os.path.expanduser('~/Projects/socialus-web'))
finally:
    os.chdir(_cwd)


def record_look():
    """The PM ticks the box on the pinned Issue; this run moves the baseline to now and clears the box. Only with --record-look (the workflow)."""
    PLAN_REPO = 'donlafranchi/socialus-plan'
    for i in gh('issue', 'list', '-R', PLAN_REPO, '--state', 'open', '--search', f'"{LOOK_ISSUE}" in:title', '--json', 'number,body') or []:
        if re.search(r'- \[[xX]\] I looked', i['body'] or ''):
            json.dump({'time': datetime.now(timezone.utc).isoformat(), 'safety': SAFETY_NOW}, open(LOOK_FILE, 'w'), indent=1, sort_keys=True)
            os.makedirs(os.path.dirname(_cap), exist_ok=True)
            json.dump(_now, open(_cap, 'w'), indent=0, sort_keys=True)
            subprocess.run(['gh', 'issue', 'edit', str(i['number']), '-R', PLAN_REPO, '--body', re.sub(r'- \[[xX]\] I looked', '- [ ] I looked', i['body'])], check=True, capture_output=True)
            return True
    return False


def cockpit_facts():
    def latest(runs, name=None):
        seen = {}
        for r in runs:                                   # newest first
            if r['status'] == 'completed' and r['conclusion'] != 'skipped' and (name is None or r['name'] == name):
                seen.setdefault(r['name'], r['conclusion'])
        return seen
    try:
        runs = gh('run', 'list', '-R', REPO, '--branch', 'main', '--limit', '40', '--json', 'name,conclusion,status')
        ci_ = latest(runs, 'CI'); dep = latest(runs, 'Deploy health')
        build = {'name': 'build', 'state': 'unknown' if not ci_ else ('green' if all(v == 'success' for v in ci_.values()) else 'red'), 'text': 'main CI ' + ('passing' if ci_ and all(v == 'success' for v in ci_.values()) else 'failing or unread')}
        site = {'name': 'site', 'state': 'unknown' if not dep else ('green' if all(v == 'success' for v in dep.values()) else 'red'), 'text': 'last deploy health run ' + ('passed' if dep and all(v == 'success' for v in dep.values()) else 'failed or unread')}
    except Exception:
        build = {'name': 'build', 'state': 'unknown', 'text': 'CI not readable'}; site = {'name': 'site', 'state': 'unknown', 'text': 'deploy health not readable'}
    try:
        undated = json.load(open(os.path.join(os.environ.get('PROJECTS', os.path.expanduser('~/Projects')), 'socialus-ops', 'scores', 'tend-docs', 'latest.json')))['undated']
        docs = {'name': 'docs', 'state': 'green' if undated < 5 else 'amber', 'text': f'{undated} undated (target under 5)'}
    except Exception:
        docs = {'name': 'docs', 'state': 'unknown', 'text': 'not read (tend-docs score unreadable)'}
    pct = MS['pct']
    crit = {'name': f'criteria {pct}%', 'state': 'red' if MS.get('red') else ('green' if pct >= 100 else 'amber'), 'text': f'{MS["met"]} of {MS["total"]} met' + (f', {MS["red"]} launch-blocking unmet' if MS.get('red') else '')}
    flat = [i for a in WAIT_AREAS for i in WAIT.get(a, [])]
    wait = {'name': 'waiting on you', 'state': 'green' if not flat else 'amber', 'text': f'{len(flat)} items; oldest wait not read yet'}
    try:
        mg = latest(gh('run', 'list', '-R', REPO, '--workflow', 'migrations.yml', '--branch', 'main', '--limit', '5', '--json', 'name,conclusion,status'))
        mig = {'name': 'migrations', 'state': 'unknown' if not mg else ('green' if all(v == 'success' for v in mg.values()) else 'red'), 'text': 'repo and database agree (last drift check on main)' if mg and all(v == 'success' for v in mg.values()) else 'drift check failing or unread'}
    except Exception:
        mig = {'name': 'migrations', 'state': 'unknown', 'text': 'not read yet'}
    lights = [build, site, mig, crit, wait, docs]
    since = max(LOOK['time'] if LOOK else datetime.now(timezone.utc) - timedelta(days=7), datetime.now(timezone.utc) - timedelta(days=7))
    merged = []
    for repo, short in ((REPO, 'web'), ('donlafranchi/socialus-plan', 'plan')):
        for p_ in gh('pr', 'list', '-R', repo, '--state', 'merged', '--limit', '60', '--json', 'number,title,mergedAt,url'):
            if datetime.fromisoformat(p_['mergedAt'].replace('Z', '+00:00')) >= since and not re.match(r'^docs: regenerate', p_['title']):
                merged.append({'repo': short, 'n': p_['number'], 'title': p_['title'], 'url': p_['url'], 't': p_['mergedAt']})
    merged.sort(key=lambda x: x['t'], reverse=True)
    newly = sum(1 for k, v in (_now or {}).items() if v['built'] == 'yes' and _prev is not None and (k not in _prev or _prev[k]['built'] != 'yes'))
    lost_n = 0 if _prev is None or _now is None else sum(1 for k in _prev if k not in _now or (_prev[k]['built'] == 'yes' and _now[k]['built'] != 'yes') or (_prev[k]['checked'] == 'yes' and _now[k]['checked'] != 'yes'))
    sc = going.scenarios(os.path.join(root, 'planning')); ideas = going.imagine(os.path.join(root, 'IMAGINE.md'))
    up = {'now': sum(1 for x in sc if x['horizon'] == 'now'), 'next': sum(1 for x in sc if x['horizon'] == 'next'),
          'considering': sum(1 for x in sc if x['horizon'] == 'considering') + sum(1 for l, _ in ideas if l == 'considering'),
          'later': sum(1 for x in sc if x['horizon'] == 'later') + sum(1 for l, _ in ideas if l == 'later')}
    first = flat[0] if flat else None
    test = {'done': _u['ticked'], 'total': _u['total'], 'next': _u['start'], 'upnext': _u['next'][:3]}
    setup = []
    try:
        body = gh('issue', 'view', '-R', REPO, '707', '--json', 'body,url')
        for row in re.findall(r'^\|\s*([^|]+?)\s*\|\s*`?([^|]+?)`?\s*\|', body['body'], re.M):
            if row[0] not in ('Feature', 'Where') and not row[0].startswith('---'):
                setup.append({'text': f'{row[0]}: {row[1]}'[:120], 'done': False, 'url': body['url']})
    except Exception:
        pass
    r = subprocess.run(['bash', os.path.join(PLAN, 'scripts', 'risks-due.sh')], capture_output=True, text=True, cwd=PLAN)
    due = [l.strip(' -*') for l in r.stdout.splitlines() if l.strip()][:6]
    dated = [f"Launch checklist: {i['text'][:90]}" + (f" ({i['days_to_date']} days to the date trigger)" if i.get('days_to_date') is not None else '') for i in (LAUNCH or [])]
    flags, unread = safety.compare(LOOK['safety'] if LOOK else None, SAFETY_NOW, safety.guard_prs(since.isoformat()) if LOOK else [])
    safe = {'flags': flags, 'unread': unread}
    if lost_n:
        safe['flags'].append({'text': f'{lost_n} approved criteria left, stopped being built or lost their test (see Lost since last look)'})
    lights.append({'name': 'agent safety', 'state': 'red' if safe['flags'] else ('unknown' if safe['unread'] else 'green'), 'text': f'{len(safe["flags"])} flags' if safe['flags'] else f'nothing flagged; {len(safe["unread"])} checks not read yet'})
    return {'days': days, 'lights': lights,
            'built': {'merged': merged[:15], 'newly_met': newly, 'lost': lost_n, 'since': 'since you last looked' if LOOK else 'last 7 days, no look recorded yet'},
            'upcoming': up, 'attention': {'total': len(flat), 'first': first, 'rest': flat[1:8]}, 'test': test,
            'setup': {'items': setup, 'private': 0}, 'risks': {'freeze': FREEZE.isoformat(), 'due': due, 'dated': dated}, 'safety': safe}

if RECORD_LOOK and record_look():
    LOOK = json.load(open(LOOK_FILE)); LOOK['time'] = datetime.fromisoformat(LOOK['time'])
if BASELINE_NEW and _now is not None and not os.path.exists(_cap):
    os.makedirs(os.path.dirname(_cap), exist_ok=True)
    json.dump(_now, open(_cap, 'w'), indent=0, sort_keys=True)
COCKPIT = cockpit.build(cockpit_facts())
_pi = next(i for i, l in enumerate(out) if l.startswith('**As of'))
out[_pi + 1:_pi + 1] = [''] + cockpit.md(COCKPIT) + pipeline_health()
# Don, 2026-10-15: "when I say dashboard I want html not markdown." The page is the dashboard; this file is a pointer and the numbers.
PAGE_URL = 'https://donlafranchi.github.io/socialus-plan/'
_todos = sorted(_json_items := (json.load(open(os.path.join(root, 'dashboard', 'don-todos.json')))['items'] if os.path.exists(os.path.join(root, 'dashboard', 'don-todos.json')) else []), key=lambda t: (t.get('p', 3), t.get('due') or '9999'))
short = [out[0], '', out[2], '',
         f'**The dashboard is a web page: [{PAGE_URL}]({PAGE_URL})** (generated daily; also `dashboard/status-dashboard.html`). This file only points to it.', '',
         '## The numbers', '']
short += [f"- {i['text']}" for i in COCKPIT[0]['items']]
short += [f"- {x['title']}: {x['bold']}" for x in COCKPIT[1:]]
def _safe(fn, default=None):
    try:
        return fn()
    except Exception:
        return [] if default is None else default


def _speed():
    """#536 (Don: "Where can I see... how well the app is responding?"). The nightly tap-speed run (socialus-web,
    a mid-range phone on 4G against production) writes latest.json and history/YYYY-MM-DD.json to the perf-history
    branch; read with git show, like the criterion reports. Red only when a member-facing (consumer) screen is red."""
    code = os.environ.get('STATUS_CODE') or os.path.expanduser('~/Projects/socialus-web')
    subprocess.run(['git', '-C', code, 'fetch', '-q', 'origin', 'perf-history'], capture_output=True)
    show = lambda path: json.loads(subprocess.run(['git', '-C', code, 'show', f'origin/perf-history:{path}'], check=True, capture_output=True, text=True).stdout)
    names = subprocess.run(['git', '-C', code, 'ls-tree', '--name-only', 'origin/perf-history', 'history/'], check=True, capture_output=True, text=True).stdout.split()
    hist = [(n[len('history/'):-len('.json')], show(n)) for n in sorted(x for x in names if x.endswith('.json'))[-7:]]
    latest = show('latest.json')
    rows = latest.get('rows', [])
    red = [r for r in rows if r.get('status') == 'red' and r.get('kind') == 'consumer']
    amber = [r for r in rows if r.get('status') in ('amber', 'red') and r not in red]
    trend = lambda screen: [{'day': d, 'ms': next((r.get('readyMs') for r in h.get('rows', []) if r.get('screen') == screen), None)} for d, h in hist]
    return {
        'at': latest.get('at'), 'state': 'red' if red else 'amber' if amber else 'green', 'red': len(red), 'amber': len(amber), 'taps': len(rows),
        'slowest': [{'screen': x['screen'], 'kind': x.get('kind'), 'ms': x.get('readyMs'), 'status': x.get('status'), 'trend': trend(x['screen'])} for x in latest.get('slowest', [])[:5]],
        # Real phones (Vercel Speed Insights) once it is switched on and its code ships; until then, said so.
        'real_users': None,
        'runs': 'https://github.com/donlafranchi/socialus-web/actions/workflows/tap-speed.yml',
    }


_sp = _safe(_speed, {})
if _sp.get('state'):
    short += ['', f"**How fast it feels: {_sp['state'].title()}** ({_sp['red']} member screen(s) red, {_sp['amber']} amber); slowest: " + ', '.join(f"{x['screen']} {x['ms']} ms" for x in _sp['slowest'][:3])]
short += ['', f"## Your to-do ({len(_todos)})", ''] + [f"- P{t.get('p', 3)} · {t['text']}" + (f" · due {t['due'][5:]}" if t.get('due') else '') for t in _todos]
short += ['', '*Agents: the lanes are `python3 scripts/going.py --list now` (or next, considering, later); the criteria and areas are on the page.*']
open(os.path.join(root, 'DASHBOARD.md'), 'w').write('\n'.join(short) + '\n')

def _json(name, key, default):
    try:
        return json.load(open(os.path.join(root, 'dashboard', name)))[key]
    except Exception:
        return default
data = {
    'cockpit': COCKPIT,
    'speed': _safe(_speed, {}),
    # Don, 2026-10-15: "If I ever ask what I need to do then add it to my dashboard." Agents append and remove; P1 first.
    'todos': sorted(_json('don-todos.json', 'items', []), key=lambda t: (t.get('p', 3), t.get('due') or '9999')),
    'shorthand': {'groups': _json('shorthand.json', 'groups', []), 'checked': _json('shorthand.json', 'checked', '')},
    # Don, 2026-10-16: "Where can I see what we have left to build… what else needs to be done before soft launch?"
    'launch_left': {
        'issues': [{'n': i['number'], 'title': i['title'], 'url': i['url']} for i in sorted(_safe(lambda: gh('issue', 'list', '-R', REPO, '--milestone', MILESTONE, '--label', 'launch-blocking', '--state', 'open', '--limit', '200', '--json', 'number,title,url')), key=lambda i: i['number'])],
        # The pitch grade card (F116) once it exists: one row per criterion, pass when built. Until then, not yet set.
        'grade': next(([{'n': c['n'], 'text': c['text'], 'pass': c['built'] == 'yes'} for c in f['criteria']] for f in FEATS if f['id'] == 'F116'), None) if os.path.exists(os.path.join(root, 'planning', 'scenario-F116.md')) and re.search(r'^status: approved', open(os.path.join(root, 'planning', 'scenario-F116.md')).read(), re.M) else None,
        # [derives pitch@date] docs older than PRINCIPLES.md #pitch (scripts/markers.py derives): a row until green.
        'pitch': _safe(lambda: json.loads(subprocess.run(['python3', os.path.join(root, 'scripts', 'markers.py'), 'derives'], capture_output=True, text=True, check=True, cwd=root).stdout), {'changed': None, 'stale': []}),
        'calls': [{'p': t.get('p', 3), 'text': t['text'], 'url': t.get('url'), 'due': t.get('due')} for t in sorted(_json('don-todos.json', 'items', []), key=lambda t: (t.get('p', 3), t.get('due') or '9999'))],
    },
    'lanes': (lambda sc, ideas: {h: [{'id': x['id'], 'title': x['title'], 'status': x['status']} for x in sorted((x for x in sc if x['horizon'] == h), key=lambda x: (x['rank'], x['id']))] + [{'id': 'idea', 'title': t, 'status': 'IMAGINE'} for l, t in ideas if l == h] for h in ('now', 'next', 'considering', 'later')})(going.scenarios(os.path.join(root, 'planning')), going.imagine(os.path.join(root, 'IMAGINE.md'))),
    'since': since_h, 'noarea': [{'k': k, 't': t, 'u': u} for k, t, u in SHIFT.get(None, [])],
    'features': [{'id': f['id'], 'title': f['title'], 'area': f['area'], 'met': f['met'], 'total': f['total'], 'checked': f['checked'], 'reviewed': f['reviewed'], 'smoked': f['smoked'], 'pm': f['pm'], 'blocked': len(f['blocked']), 'stale': f.get('stale', False), 'url': f['url'], 'criteria': [{'n': r['n'], 'text': r['text'], 'built': r['built'], 'checked': r['checked'], 'reviewed': r['reviewed'], 'smoked': r['smoked'], 'pm': r['pm'], 'uat': r['uat'], 'blocking': r['blocking'], 'not_ok': r.get('not_ok', False), 'not_ok_text': r.get('not_ok_text', ''), 'issues': r['issues']} for r in f['criteria']]} for f in sorted(FEATS, key=lambda f: (f['area'], f['id']))], 'cover': COVER,
    'your_uat': _u, 'journeys': JR, 'how': HOW[1:], 'waiting': WAIT, 'wait_areas': WAIT_AREAS, 'wait_total': WAIT_TOTAL, 'launch': LAUNCH, 'test_notice': globals().get('TEST_NOTICE', ''), 'uat': uat_items, 'problems': problems, 'header': header, 'stages': STAGES, 'colors': COLORS, 'behind': behind, 'test_items': test_items,
    'next': ({'title': nxt['title'], 'url': issue_url(nxt['n']), 'n': nxt['n'], 'review': nxt['review']} if nxt else None),
    'areas': [{'name': x['name'], 'filled': x['filled'], 'counts': x['counts'], 'total': len(x['rows']),
               'done': x['done'], 'note': x['note'], 'crit': x['crit'], 'shift': [{'k': k, 't': t, 'u': u} for k, t, u in x['shift']],
               'rows': [{'n': r['n'], 'title': r['title'], 'st': r['st'], 'review': r['review'],
                         'issue': issue_url(r['n']), 'pr': pr_url(r), 'prn': r['pr']['number'] if r['pr'] else None}
                        for r in x['rows']]} for x in areas],
}
PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>Beta dashboard</title>
<style>
:root{--bg:#f8fafc;--card:#fff;--ink:#0f172a;--mute:#64748b;--off:#d1d5db;--unk:#fde68a;--line:#e2e8f0}
@media(prefers-color-scheme:dark){:root{--bg:#0b1220;--card:#111a2e;--ink:#e5e7eb;--mute:#94a3b8;--off:#334155;--unk:#854d0e;--line:#1e293b}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
main{max-width:960px;margin:0 auto;padding:20px 16px 60px;min-width:0}h1{font-size:1.25rem;margin:0 0 4px}
.layout{display:grid;grid-template-columns:220px minmax(0,1fr);max-width:1240px;margin:0 auto}
.toc{position:sticky;top:0;align-self:start;height:100vh;overflow:auto;padding:20px 8px 20px 16px;border-right:1px solid var(--line);font-size:.88rem}
.toc a{display:block;padding:6px 8px;border-radius:6px;color:var(--ink);text-decoration:none}.toc a:hover,.toc a.on{background:var(--card)}
.toc b{display:block;margin:0 0 8px 8px}.tocm{display:none}
.spark{vertical-align:middle;color:var(--mute)}.row.speed{align-items:flex-start;gap:8px}
.sec{scroll-margin-top:64px;margin:0 0 30px}.sec>h2{font-size:1.1rem;margin:0 0 4px}.lede{margin:0 0 10px}
.todo{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;padding:12px 14px;margin:8px 0;background:var(--card);border:1px solid var(--line);border-radius:12px}
.pri{font-weight:800;font-size:.8rem;border-radius:999px;padding:3px 9px;color:#fff;align-self:start}.p1{background:#b91c1c}.p2{background:#d97706}.p3{background:#64748b}
.todo .what{font-weight:650}.todo .meta{grid-column:2;font-size:.85rem;color:var(--mute)}.todo .meta b{color:var(--ink)}.late{color:#b91c1c!important;font-weight:700}
.gl{display:grid;grid-template-columns:minmax(120px,190px) 1fr;gap:6px 14px;padding:8px 0;border-bottom:1px solid var(--line);font-size:.9rem}.gl:last-child{border:0}.gl .src{color:var(--mute);font-size:.75rem}
@media(max-width:899px){.layout{display:block}.toc{display:none}.tocm{display:block;position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:8px 16px}
.tocm summary{display:flex;justify-content:space-between;padding:6px 0;font-weight:650;grid-template-columns:none}.tocm details{border:0;margin:0;background:none}.tocm a{display:block;padding:10px 4px;border-top:1px solid var(--line);color:var(--ink);text-decoration:none}}
.settled{margin:0 0 14px;padding:10px 12px;border-radius:8px;background:var(--unk);color:var(--ink);font-size:.85rem}.sub{color:var(--mute);font-size:.85rem;margin:0 0 18px}.legend{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:.8rem;margin-bottom:18px}
.legend span{display:inline-flex;align-items:center;gap:6px}.dot{width:12px;height:12px;border-radius:3px;display:inline-block}
details{background:var(--card);border:1px solid var(--line);border-radius:12px;margin:10px 0;border-left-width:6px}
.ramp{display:inline-flex;gap:2px;vertical-align:middle}.ramp i{width:18px;height:10px;display:inline-block;border-radius:2px}
summary{list-style:none;cursor:pointer;padding:12px 14px;display:grid;grid-template-columns:minmax(110px,150px) 1fr;gap:6px 14px;align-items:center}
summary::-webkit-details-marker{display:none}.name{font-weight:650}.note{grid-column:1/-1;color:var(--mute);font-size:.82rem}
.bar{display:grid;grid-template-columns:repeat(6,1fr);gap:3px}.seg{height:26px;border-radius:5px;background:var(--off);color:var(--ink);font-size:.72rem;font-weight:650;display:flex;align-items:center;justify-content:center}
.seg.on{color:#fff}.rows{border-top:1px solid var(--line);padding:4px 14px 10px}
.row{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;padding:9px 0;border-bottom:1px solid var(--line);align-items:center}.row:last-child{border:0}
.strip{display:flex;gap:3px}.box{width:16px;height:16px;border-radius:3px;background:var(--off);font-size:.7rem;font-weight:800;color:#92400e;text-align:center;line-height:16px}
.box.unk{background:var(--unk)}.title{font-size:.92rem}.links{grid-column:2;font-size:.8rem;color:var(--mute)}a{color:#2563eb}
.shift{margin:8px 0 2px;padding:8px 10px;border-radius:8px;background:var(--bg);font-size:.82rem}.shift b{display:block;margin-bottom:2px}.shift div{padding:1px 0}.shift i{font-style:normal;color:var(--mute)}
.segbar{display:flex;gap:1px;height:16px;width:100%;margin:2px 0}.segbar i{flex:1 1 0;min-width:1px;border-radius:1px}.legend .sw{display:inline-block;width:20px;height:12px;border-radius:2px;vertical-align:middle;margin-right:4px}.how{margin:0 0 12px;padding:10px 12px;border-radius:8px;background:var(--card);border:1px solid var(--line);font-size:.85rem}.how li{margin:2px 0}.uatline{margin:0 0 10px;font-size:1rem}
.foot{margin-top:18px;padding:14px;border-radius:12px;background:var(--card);border:1px solid var(--line)}.foot p{margin:4px 0}
@media(max-width:560px){summary{grid-template-columns:1fr}}
</style></head><body><div class="tocm" id="tocm"></div><div class="layout"><nav class="toc" id="toc" aria-label="Contents"></nav><main>
<p class="settled"><b>SETTLED — do not re-raise:</b> members are the investors and the only people paid out. “Ownership, not profit-share” is rejected. Legal/securities questions about this go to socialus-legal for counsel and never come back to the PM as a decision. SocialUs takes transaction income; any 'no fee' language is retired.</p><h1 id="h"></h1><p class="sub">Generated by scripts/dashboard.py. Tap an area or a feature to open it.</p>
<div id="areas"></div><section class="sec" id="how" data-toc="How to read"><h2>How to read this page</h2><p class="lede"><b>The colours, the squares and the walk-throughs, explained.</b></p><details><summary><span class="name">Details</span></summary><div class="rows"><div class="legend" id="legend"></div></div></details></section><div class="foot" id="foot"></div>
<script id="data" type="application/json">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('data').textContent);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
{const [lead,...more]=D.header.split(' · criterion');document.getElementById('h').textContent=lead;document.title='Dashboard · '+lead;if(more.length){const m=document.createElement('p');m.className='sub';m.style.margin='0 0 4px';m.textContent='Criterion'+more.join(' · criterion');document.getElementById('h').after(m)}}
const HUES={'page-editing':'#2563eb','sign-in-you':'#7c3aed','explore-map':'#0d9488','create-posts':'#d97706','sharing-links':'#65a30d','builders-seed':'#a16207','moderation':'#c026d3','ops':'#475569','Ops & plan':'#475569'};const hue=n=>HUES[n]||'#475569';const slug=n=>n.toLowerCase().replace(/[^a-z0-9 -]/g,'').replace(/ /g,'-');
const tint=(hex,f)=>{const t=0.18+0.82*Math.max(0,Math.min(1,f));const c=[1,3,5].map(i=>parseInt(hex.slice(i,i+2),16));return '#'+c.map(v=>Math.round(255-(255-v)*t).toString(16).padStart(2,'0')).join('')};
const depth=c=>c.built==='yes'?1+['checked','reviewed','smoked','pm'].filter(k=>c[k]==='yes').length:0;
const shade=(h,d)=>d===0?'var(--off)':tint(h,(d-1)/4);
const segFill=(h,c)=>c.not_ok?'repeating-linear-gradient(45deg,#b91c1c,#b91c1c 3px,#fecaca 3px,#fecaca 5px)':(c.blocking?'#b91c1c':shade(h,depth(c)));
const segBar=(h,cs)=>cs.length?`<div class="segbar">${cs.map(c=>`<i title="${esc(c.id)}.${esc(c.n)}: ${esc(c.text)}${c.not_ok?' (PM: not OK)':''}" style="background:${segFill(h,c)}"></i>`).join('')}</div>`:'';
const critsOf=area=>D.features.filter(f=>f.area===area).flatMap(f=>f.criteria.map(c=>({...c,id:f.id})));
const waitList=n=>{const w=(D.waiting[n]||[]);return w.length?w.map(i=>`<div class="row"><div class="title"><a href="${esc(i.url)}">${esc(i.title)}</a> <i style="color:var(--mute);font-style:normal">(${esc(i.kind)})</i><br>${esc(i.ask)}</div></div>`).join(''):'<div class="row"><div class="title">Nothing waiting on you here.</div></div>'};
const waitCard=n=>`<details id="card-${slug(n)}" style="border-left-color:${hue(n)}"><summary><span class="name">${esc(n)}</span><span class="note">Waiting on you (${(D.waiting[n]||[]).length})</span></summary><div class="rows">${waitList(n)}</div></details>`;
const RAMP=['#b91c1c','#d97706','#ca8a04','#65a30d','#15803d'];const ramp=f=>RAMP[Math.min(4,Math.floor(f*5))];
document.getElementById('legend').innerHTML=`<ol class="how">${D.how.map(h=>`<li>${esc(h.replace(/^\d+\. /,'').replace(/\*\*|`/g,''))}</li>`).join('')}</ol><p class="uatline"><b>Your UAT: ${D.your_uat.ticked} of ${D.your_uat.total} walk-throughs done</b>${D.your_uat.next.length?' · next up:':' · all done'}</p><ol class="uatnext">${D.your_uat.next.map(x=>`<li><a href="${esc(x.url)}"><b>${esc(x.title)}</b></a> · as ${esc(x.role)} · about ${x.minutes} min${x.launch?' · launch':''}<ul>${x.look.map(p=>`<li>${esc(p)}</li>`).join('')}</ul><div class="sub">${esc(x.unlock)}</div></li>`).join('')}</ol><p style="margin:0 0 4px"><b>Area colours</b> (full shade = fully checked): ${Object.keys(HUES).filter(n=>n!=='Ops & plan').map(n=>`<span style="margin-right:10px"><i class="sw" style="background:${tint(HUES[n],1)}"></i>${esc(n)}</span>`).join('')}</p><p style="margin:0 0 4px"><b>Shade of one square</b> (same five steps in every area's colour): <span class="sw" style="background:var(--off)"></span>not built <span class="sw" style="background:${tint('#2563eb',0)}"></span>built <span class="sw" style="background:${tint('#2563eb',.25)}"></span>checked <span class="sw" style="background:${tint('#2563eb',.5)}"></span>reviewed <span class="sw" style="background:${tint('#2563eb',.75)}"></span>smoked <span class="sw" style="background:${tint('#2563eb',1)}"></span>PM looked</p><p style="margin:0"><span class="sw" style="background:#b91c1c"></span>launch-blocking unmet <span class="sw" style="background:repeating-linear-gradient(45deg,#b91c1c,#b91c1c 3px,#fecaca 3px,#fecaca 5px)"></span>PM: not OK</p>`;
const shiftBox=l=>`<div class="shift"><b>Past ${D.since}h</b>${l.length?l.map(e=>`<div><i>${esc(e.k)}:</i> ${e.u?`<a href="${esc(e.u)}">${esc(e.t)}</a>`:esc(e.t)}</div>`).join(''):'<div><i>nothing</i></div>'}</div>`;
const testSection=D.test_items.length?`<details><summary><span class="name">Testing</span><span class="note">${D.test_items.filter(t=>t.checked).length} of ${D.test_items.length} screens</span></summary><div class="rows">${D.test_items.map(t=>`<div class="row" style="opacity:${t.checked?1:.5}"><input type="checkbox" ${t.checked?'checked':''} disabled style="cursor:default;margin-right:8px"/><div class="title">${t.url?`<a href="${esc(t.url)}">${esc(t.text)}</a>`:esc(t.text)}</div></div>`).join('')}</div></details>`:'';
const featSection=`<h2 style="font-size:1rem;margin:22px 0 4px">Criterion roll-up: features, ${D.cover[0]} of ${D.cover[1]} reporting</h2><p class="sub">Read from the criterion reports, not from Issues. Bar and edge = criteria met / total, in the area's colour, pale to full. Red = a launch-blocking criterion is unmet. Tap a feature for its criteria: green = built, T = a marked test covers it, R = reviewed, S = a green smoke run came after the last merge, P = the PM looked (ticked on the phone checklist); a dot = on the checklist, not yet ticked.</p>`+D.features.map(f=>{const fr=f.total?f.met/f.total:0;const col=f.blocked?'#b91c1c':tint(hue(f.area),fr);return `<details style="border-left-color:${col}"><summary><span class="name">${esc(f.id)} ${esc(f.title)}</span>${segBar(hue(f.area),f.criteria.map(c=>({...c,id:f.id})))}<span class="note">${esc(f.area)} · ${Math.round(fr*100)}% met${f.blocked?` · <b style="color:#b91c1c">${f.blocked} launch-blocking unmet</b>`:''} · <a href="${esc(f.url)}">full report</a>${f.stale?' · <b style="color:#b45309">report stale: merged after it was written</b>':''}</span></summary><div class="rows">${f.criteria.map(c=>`<div class="row"><div class="strip"><span class="box" style="background:${c.built==='yes'?'#15803d':(c.blocking?'#b91c1c':'var(--off)')};color:#fff">${c.built==='yes'?'✓':(c.built==='unknown'?'?':'✕')}</span><span class="box" title="checked: a marked test covers this whole criterion" style="background:${c.checked==='yes'?'#2563eb':'var(--off)'};color:#fff">${c.checked==='yes'?'T':''}</span><span class="box" title="reviewed" style="background:${c.reviewed==='yes'?'#7c3aed':'var(--off)'};color:#fff">${c.reviewed==='yes'?'R':''}</span><span class="box" title="smoked: a green smoke run came after the last merge (pages load)" style="background:${c.smoked==='yes'?'#0d9488':'var(--off)'};color:#fff">${c.smoked==='yes'?'S':''}</span><span class="box" title="PM looked" style="background:${c.not_ok?'#b91c1c':(c.pm==='yes'?'#ca8a04':'var(--off)')};color:#fff;${c.uat==='listed'?'outline:2px solid #ca8a04':''}">${c.not_ok?'✗':(c.pm==='yes'?'P':(c.uat==='listed'?'·':''))}</span></div><div class="title">${esc(c.n)}. ${esc(c.text)}${c.not_ok?' <b style="color:#b91c1c">PM: not OK</b>':''}${c.blocking?' <b style="color:#b91c1c">launch-blocking</b>':''}${c.issues.length?' · '+c.issues.map(n=>`<a href="https://github.com/donlafranchi/socialus-web/issues/${n}">#${n}</a>`).join(' '):''}</div></div>`).join('')}</div></details>`}).join('');
const launchSec=D.launch.length?`<h2 style="font-size:1rem;margin:22px 0 4px">Launch checklist</h2><div class="foot">${D.launch.map(i=>`<p style="${i.due?'color:#b91c1c;font-weight:700':''}">${i.due?'DUE ('+esc(i.fired_by.join(', '))+'): ':'Fires at '+esc(i.waiting_on)+', whichever comes first: '}${esc(i.text)} <a href="${esc(i.runbook)}">Runbook</a>${(!i.due&&i.days_to_date!==null)?` (${i.days_to_date} days to the date trigger)`:''}</p>`).join('')}</div>`:'';
const testNote=D.test_notice?`<p class="settled" style="background:#fecaca"><b>Testing:</b> ${esc(D.test_notice)}</p>`:'';
const jrSec=`<h2 style="font-size:1rem;margin:22px 0 4px">Your review: journeys, by area</h2><p class="sub">Your 3-minute checks, over the criteria the agents test. Feature progress is by criteria; this is by journeys.</p><table class="t"><tr><th>Area</th><th>Journeys looked</th><th>Criteria under them</th></tr>${Object.entries(D.journeys).sort().map(([a,c])=>`<tr><td>${esc(a)}</td><td>${c.looked}/${c.total}</td><td>${c.crit}</td></tr>`).join('')}</table>`;
const uatSec=(D.uat.length?`<h2 style="font-size:1rem;margin:22px 0 4px">Live testing (UAT Issues)</h2><div class="foot">${D.uat.map(u=>`<p><a href="${esc(u.url)}">#${u.n} ${esc(u.title)}</a> · ${esc(u.state)} · ${u.done}/${u.total} boxes ticked</p>`).join('')}</div>`:'')+`<h2 style="font-size:1rem;margin:22px 0 4px">Data problems</h2><div class="foot">${D.problems.length?D.problems.map(p=>`<p>${esc(p)}</p>`).join(''):'<p>none</p>'}</div>`;
const waitTop=`<p class="settled" style="background:var(--card);border:1px solid var(--line)"><b>Waiting on you: ${D.wait_total}</b> · ${D.wait_areas.map(n=>`<a href="#card-${slug(n)}">${esc(n)} (${(D.waiting[n]||[]).length})</a>`).join(' · ')}</p>`;
const cockpitSec=`${D.cockpit.map((x,n)=>`<details id="cockpit-${esc(x.id)}" style="border-left-color:#2563eb"><summary><span class="name">${n+1}. ${esc(x.title)}</span><span class="note" style="grid-column:auto;color:var(--ink)">${esc(x.bold)}</span></summary><div class="rows">${x.items.length?x.items.map(i=>`<div class="row"><div class="title">${i.url?`<a href="${esc(i.url)}">${esc(i.text)}</a>`:esc(i.text)}</div></div>`).join(''):'<div class="row"><div class="title">nothing</div></div>'}</div></details>`).join('')}`;
const areaCards=D.areas.map(a=>{
 const bar=segBar(hue(a.name),critsOf(a.name));
 const rows=waitList(a.name);
 const cm=a.crit&&a.crit.total?a.crit.met/a.crit.total:null;const mean=cm!==null?cm:(a.total?a.counts.reduce((x,y)=>x+y,0)/(6*a.total):0);return `<details id="card-${slug(a.name)}" style="border-left-color:${a.crit&&a.crit.red?'#b91c1c':tint(hue(a.name),mean)}"><summary><span class="name">${esc(a.name)}</span>${bar||'<span class="note">no criterion reports yet</span>'}<span class="note"><b>Waiting on you (${(D.waiting[a.name]||[]).length})</b> · ${cm!==null?`${a.crit.met}/${a.crit.total} criteria met (${Math.round(cm*100)}%)${a.crit.red?` · ${a.crit.red} red`:''}`:`${Math.round(mean*100)}% of Issue stages (no criterion reports)`} · ${D.stages.map((n,k)=>n+' '+a.counts[k]+'/'+a.total).join(' · ')} · ${esc(a.note)} · ${a.shift.length} event(s) in the past ${D.since}h</span></summary><div class="rows">${rows}</div></details>`}).join('')+waitCard(D.wait_areas[D.wait_areas.length-1])+testSection+(D.noarea.length?`<details><summary><span class="name">No area</span><span class="note">${D.noarea.length} event(s) in the past ${D.since}h</span></summary><div class="rows">${shiftBox(D.noarea)}</div></details>`:'');
// Don, 2026-10-15: the HTML page is the dashboard. Each section: a bold overview, the detail folded; a sidebar lists them.
const sec=(id,title,lede,body,open)=>`<section class="sec" id="${id}" data-toc="${esc(title)}"><h2>${esc(title)}</h2><p class="lede"><b>${lede}</b></p>${open?body:`<details><summary><span class="name">Details</span></summary><div class="rows">${body}</div></details>`}</section>`;
const PR=['','p1','p2','p3'];const DAY=['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
const today=new Date().toISOString().slice(0,10);
const when=d=>{const t=new Date(d+'T12:00:00');return `${DAY[t.getDay()]} ${d.slice(5)}`};
const T=D.todos;const p1=T.filter(t=>t.p===1).length;const due=T.filter(t=>t.due).sort((a,b)=>a.due<b.due?-1:1)[0];
const todoLede=T.length?`${T.length} thing${T.length===1?'':'s'} only you can do · ${p1} first${due?` · next due ${when(due.due)}`:''}`:'Nothing only you can do right now.';
const todoBody=T.map(t=>`<div class="todo" data-p="${t.p}"><span class="pri ${PR[t.p]||'p3'}">P${t.p}</span><div class="what">${t.url?`<a href="${esc(t.url)}">${esc(t.text)}</a>`:esc(t.text)}</div><div class="meta">${esc(t.how||'')}${t.due?` · <b class="${t.due<today?'late':''}">${t.due<today?'Overdue':'Due'} ${when(t.due)}</b>`:''}${t.unlocks?`<br>Unlocks: ${esc(t.unlocks)}`:''}</div></div>`).join('')+`<p class="sub">Whenever you ask what you need to do, the steps land here, highest priority first, and come off once done. P1 = do first.</p>`;
const where=D.cockpit[0];
const glossBody=D.shorthand.groups.map(g=>`<h3 style="font-size:.95rem;margin:14px 0 2px">${esc(g.name)}</h3>${g.items.map(i=>`<div class="gl"><div><b>${esc(i.name)}</b><div class="src">${i.src==='patterns'?'patterns.md':'shorthand note only'}</div></div><div>${esc(i.does)}</div></div>`).join('')}`).join('')+`<p class="sub">Checked: ${esc(D.shorthand.checked)}</p>`;
const LL=D.launch_left;const gradeOpen=LL.grade?LL.grade.filter(g=>!g.pass):[];
const leftN=LL.issues.length+LL.calls.length+gradeOpen.length;
const launchLede=`${leftN} thing${leftN===1?'':'s'} left, ${LL.calls.length} ${LL.calls.length===1?'is':'are'} yours`;
const launchBody=`<h3 style="font-size:.95rem;margin:4px 0">Launch-blocking work (${LL.issues.length})</h3><ul style="margin:0;padding-left:20px">${LL.issues.map(i=>`<li><a href="${esc(i.url)}">#${i.n} ${esc(i.title)}</a></li>`).join('')||'<li>none open</li>'}</ul>`+
 `<h3 style="font-size:.95rem;margin:12px 0 4px">Pitch grade card</h3>${LL.grade?`<ul style="margin:0;padding-left:20px">${LL.grade.map(g=>`<li>${g.pass?'✅':'☐'} cap-${g.n} · ${esc(g.text)}</li>`).join('')}</ul>`:'<p class="sub" style="margin:0">Pass/fail for cap-1 to cap-8: not yet set (it starts once you approve the grade card draft, F116).</p>'}`+
 (LL.pitch&&LL.pitch.stale.length?`<p class="sub" style="margin:12px 0 0" id="pitch-cascade">Pitch changed ${esc(LL.pitch.changed)} → ${LL.pitch.stale.length} file${LL.pitch.stale.length===1?'':'s'} updating: ${LL.pitch.stale.map(x=>esc(x.path)).join(', ')}</p>`:'')+
 `<h3 style="font-size:.95rem;margin:12px 0 4px">Your open calls (${LL.calls.length})</h3><ul style="margin:0;padding-left:20px">${LL.calls.map(c=>`<li><span class="pri ${PR[c.p]||'p3'}" style="font-size:.7rem;padding:1px 6px">P${c.p}</span> ${c.url?`<a href="${esc(c.url)}">${esc(c.text)}</a>`:esc(c.text)}${c.due?` · due ${when(c.due)}`:''}</li>`).join('')||'<li>none</li>'}</ul>`;
// #536 — how fast it feels, from the nightly tap-speed run on a mid-range phone on 4G. Red only for a member-facing screen.
const SP=D.speed||{};const STC={green:['#15803d','Green'],amber:['#b45309','Amber'],red:['#b91c1c','Red']};
const spark=t=>{const v=t.filter(x=>x.ms!=null);if(v.length<2)return '';const ms=v.map(x=>x.ms),mx=Math.max(...ms),mn=Math.min(...ms),w=90,h=22;return `<svg class="spark" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" aria-hidden="true"><polyline fill="none" stroke="currentColor" stroke-width="1.5" points="${t.map((x,i)=>x.ms==null?null:`${(i/(t.length-1)*w).toFixed(1)},${(h-1-((x.ms-mn)/((mx-mn)||1))*(h-2)).toFixed(1)}`).filter(Boolean).join(' ')}"/></svg>`};
const speedLede=SP.state?`${STC[SP.state][1]}: ${SP.red?`${SP.red} member screen${SP.red===1?' is':'s are'} over budget`:SP.amber?`${SP.amber} tap${SP.amber===1?' is':'s are'} slower than budget, no member screen red`:'every tap is within budget'} (nightly ${String(SP.at||'').slice(5,10)})`:'No tap-speed results yet.';
const speedBody=SP.state?`<p class="sub" style="margin:0 0 6px">The five slowest taps on a mid-range phone on 4G, with their last ${SP.slowest[0]?.trend.length||0} nightly runs (ms until the screen is usable). Budgets: a member screen 1 s, a creator screen 2.5 s.</p>`+SP.slowest.map(x=>`<div class="row speed" data-status="${esc(x.status)}"><span class="pri" style="background:${(STC[x.status]||STC.green)[0]};color:#fff">${esc((STC[x.status]||STC.green)[1])}</span><div class="title"><b>${esc(x.screen)}</b> · ${x.ms} ms · ${x.kind==='creator'?'creator':'member'} screen<br><span class="sub">${x.trend.map(t=>t.ms==null?'–':t.ms).join(' → ')}</span> ${spark(x.trend)}</div></div>`).join('')+`<p class="sub">Real phones: ${SP.real_users?esc(SP.real_users):'not yet. They come from Vercel Speed Insights once it is switched on.'} · <a href="${esc(SP.runs)}">all runs</a></p>`:'<p class="sub">The nightly tap-speed results could not be read.</p>';
document.getElementById('areas').innerHTML=
 sec('todo','Your to-do',todoLede,todoBody,true)+
 sec('soft-launch','Before soft launch (11-06)',launchLede,launchBody)+
 sec('going',"Where we're going",`Now ${D.lanes.now.length} · Next ${D.lanes.next.length} · Considering ${D.lanes.considering.length} · Later ${D.lanes.later.length}`,[['now','Now: being built'],['next','Next: settled and approved'],['considering','Considering: possible, not approved'],['later','Later: eventual']].map(([k,t])=>`<h3 style="font-size:.95rem;margin:12px 0 4px">${t}</h3><ol style="margin:0;padding-left:22px">${D.lanes[k].map(x=>`<li>${x.id==='idea'?'':esc(x.id)+' '}${esc(x.title)} <span style="color:var(--mute)">(${esc(x.status)})</span></li>`).join('')||'<li>none</li>'}</ol>`).join(''))+
 sec('speed','How fast it feels',speedLede,speedBody)+

 sec('cockpit','The cockpit',esc(where.bold),cockpitSec,true)+
 sec('waiting','Waiting on you',`${D.wait_total} item${D.wait_total===1?'':'s'} waiting, by area`,waitTop+testNote,true)+
 (D.launch.length?sec('launch','Launch checklist',`${D.launch.filter(i=>i.due).length} due, ${D.launch.length} in all`,launchSec):'')+
 sec('features','Criteria by feature',`${D.cover[0]} of ${D.cover[1]} features reporting; tap one for its criteria`,featSection)+
 sec('journeys','Your review: journeys',`Your 3-minute checks, by area`,jrSec)+
 sec('live','Live testing and data problems',`${D.uat.length} UAT Issue${D.uat.length===1?'':'s'} · ${D.problems.length} data problem${D.problems.length===1?'':'s'}`,uatSec)+
 sec('areas-list','By area',`${D.areas.length} areas, each with what waits on you and the past ${D.since}h`,areaCards,true)+
 sec('shorthand','Your shorthand',`${D.shorthand.groups.reduce((n,g)=>n+g.items.length,0)} names you can say; agents apply each in full. For your review.`,glossBody);
const secs=[...document.querySelectorAll('section[data-toc]')];
const links=secs.map(x=>`<a href="#${x.id}">${esc(x.dataset.toc)}</a>`).join('');
document.getElementById('toc').innerHTML=`<b>Contents</b>${links}`;
document.getElementById('tocm').innerHTML=`<details><summary>Contents <span>☰</span></summary>${links}</details>`;
document.querySelectorAll('#tocm a').forEach(a=>a.addEventListener('click',()=>a.closest('details').open=false));
document.getElementById('foot').innerHTML=`<p><b>Behind:</b> ${D.behind.length?esc(D.behind.join(', ')):'none'}</p><p><b>Your next action:</b> ${D.next?`Review ${esc(D.next.title)} (<a href="${esc(D.next.url)}">#${D.next.n}</a>)${D.next.review?` at <a href="${esc(D.next.review)}">the live page</a>`:''}, then label it <code>pm-reviewed</code>.`:'none: nothing is waiting on you.'}</p>`;
</script></main></div></body></html>
"""
blob = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
open(os.path.join(root, 'dashboard', 'status-dashboard.html'), 'w').write(PAGE.replace('__DATA__', blob))
print(f'wrote DASHBOARD.md, dashboard/status-dashboard.html: {total} items; ' + stage_totals)
