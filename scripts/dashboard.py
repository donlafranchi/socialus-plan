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
    for line in open(os.path.join(PLAN, 'DECISIONS.md')):
        m = re.match(r'- \*\*(\d{4}-\d{2}-\d{2}) — (.*?)\*\*', line)
        if m and m.group(1) >= SINCE.astimezone(ZoneInfo('America/Los_Angeles')).strftime('%Y-%m-%d'):
            log(decision_area(line), 'Decision', m.group(2)[:140] + ('…' if len(m.group(2)) > 140 else ''))
except OSError:
    pass


def shift_md(items):
    return [f'- **{k}:** ' + (f'[{t}]({u})' if u else t) for k, t, u in items]


COLORS = ['#2563eb', '#0d9488', '#7c3aed', '#ea580c', '#65a30d', '#ca8a04']
OFF, UNK = '#d1d5db', '#fde68a'

# Layer 3: live testing, the checkboxes in #519 (body and comments)
TEST_ISSUE = 519
test_items = []
try:
    t = gh('issue', 'view', '-R', REPO, str(TEST_ISSUE), '--json', 'body,comments')
    for text in [t.get('body') or ''] + [c.get('body') or '' for c in t.get('comments') or []]:
        for line in text.split('\n'):
            m = re.match(r'\s*[-*]\s+\[([ xX])\]\s+(.+)', line)
            if m:
                u = re.search(r'https://[^\s)]+', m.group(2))
                lt = re.search(r'\[([^\]]+)\]', m.group(2))
                test_items.append({'checked': m.group(1) != ' ', 'text': lt.group(1) if lt else m.group(2), 'url': u.group(0) if u else None})
except subprocess.CalledProcessError:
    test_items = None

# Layer 1: criterion fulfillment. Scenario criteria x the phases a feature report records.
PHASES = ['built', 'checked', 'reviewed', 'shipped', 'smoked', 'pm']
PROJECTS = os.environ.get('PROJECTS', os.path.expanduser('~/Projects'))
REPORTS = os.path.join(PROJECTS, 'socialus-web', 'build-log', 'reports')


def meta(path):
    head = open(path).read(1500)
    g = lambda k: (re.search(rf'^{k}:\s*(.+)$', head, re.M) or [None, ''])[1].strip()
    return g('status'), g('gates'), g('title')


def n_criteria(path):
    body = open(path).read().split('## Acceptance', 1)[-1].split('\n## ', 1)[0]
    return len(re.findall(r'^\d+\.\s', body, re.M))


def cells(row):
    return [c.strip() for c in row.strip().strip('|').split('|')]


def yes(v):
    return v.lower().lstrip('*').startswith('yes')


def parse_report(path):
    txt = open(path).read()
    roll = {}
    m = re.search(r'\|\s*\d+ criteria\s*\|(.+)\|', txt)
    if m:
        c = [re.match(r'\d+', x.strip()) for x in m.group(1).split('|')]
        roll = {k: int(v.group(0)) for k, v in zip(PHASES, c) if v}
    sec = txt.split('## Per criterion', 1)[-1].split('\n## ', 1)[0]
    lines = [l for l in sec.split('\n') if l.startswith('|')]
    if len(lines) < 3:
        return None
    head = [h.lower() for h in cells(lines[0])]
    col = lambda name: next((i for i, h in enumerate(head) if h.startswith(name)), None)
    ix = {k: col(n) for k, n in zip(('built', 'checked', 'smoked', 'pm'), ('built', 'checked', 'smoked', 'pm'))}
    crits = []
    for l in lines[2:]:
        c = cells(l)
        if not c[0].isdigit():
            continue
        g = lambda k: c[ix[k]] if ix[k] is not None and ix[k] < len(c) else 'unknown'
        built = yes(g('built'))
        st = {'built': built, 'checked': yes(g('checked')), 'smoked': yes(g('smoked')), 'pm': yes(g('pm'))}
        n_built = roll.get('built', 0)
        for k in ('reviewed', 'shipped'):
            st[k] = built and roll.get(k, 0) >= n_built
        unknown = any(g(k).lower().startswith('unknown') for k in ('built', 'checked'))
        crits.append({'n': int(c[0]), 'text': c[1], 'done': sum(st[k] for k in PHASES),
                      'built': built, 'unknown': unknown})
    return crits


reports = {}
if os.path.isdir(REPORTS):
    for d, _, fs in os.walk(REPORTS):
        for f in fs:
            m = re.match(r'(F\d{3})-.*\.md$', f)
            if m:
                reports[m.group(1)] = os.path.join(d, f)

crit_rows = []
for f in sorted(os.listdir(os.path.join(PLAN, 'planning'))):
    m = re.match(r'scenario-(F\d{3})\.md$', f)
    if not m:
        continue
    fid = m.group(1)
    path = os.path.join(PLAN, 'planning', f)
    status, gates, title = meta(path)
    if status not in ('approved', 'building'):
        continue
    crits = parse_report(reports[fid]) if fid in reports else None
    crit_rows.append({'id': fid, 'title': title, 'gates': gates, 'report': crits is not None,
                      'n': len(crits) if crits else n_criteria(path),
                      'cells': [{**c, 'blocker': gates == 'launch' and not c['built'] and not c['unknown']} for c in crits] if crits else []})
no_report = [r['id'] for r in crit_rows if not r['report']]
unknown_cells = sum(1 for r in crit_rows for c in r['cells'] if c['unknown'])
for r in crit_rows:
    for c in r['cells']:
        c['rank'] = 'blocker' if c['blocker'] else c['done']

root = args[0] if args else '.'
now = datetime.now(ZoneInfo('America/Los_Angeles'))
days = (FREEZE - now.date()).days
total = len(rows)
done = sum(1 for r in rows if r['done'])
stage_totals = ' · '.join(f'{STAGES[k]} {sum(1 for r in rows if ok(r["st"][k]))}/{total}' for k in range(6))
header = f'{MILESTONE} · {days} days to freeze · {total} beta items · updated {now.strftime("%Y-%m-%d %H:%M")} PT'

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
    counts = [sum(1 for r in rs if ok(r['st'][k])) for k in range(6)]
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
    areas.append({'name': a, 'rows': rs, 'filled': filled, 'counts': counts, 'note': note,
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


out = ['> **SETTLED — do not re-raise:** members are the investors and the only people paid out. "Ownership, not profit-share" is rejected. Legal/securities questions about this go to `socialus-legal` for counsel and never come back to the PM as a decision. SocialUs takes transaction income; any \'no fee\' language is retired.', '', f'# {header}', '',
       '*Generated by `scripts/dashboard.py`; never hand-edited. `▰` is a stage every item in the area has reached; `●` a stage reached, `○` not yet, `?` the data to tell was not found. Colour: `dashboard/status-dashboard.html`.*', '',
       '| Area | ' + ' | '.join(STAGES) + ' | Note |', '|---|' + '---|' * 7]
for x in areas:
    n = len(x['rows'])
    cells = ' | '.join(f'{c}/{n}' for c in x['counts'])
    out.append(f'| {x["name"]} | {cells} | {x["note"]} |')
out.append(f'| **All** | ' + ' | '.join(f'**{sum(1 for r in rows if ok(r["st"][k]))}/{total}**' for k in range(6)) + ' | each phase counted on its own |')
out.append('')
out.append('Stages, in order: ' + ' → '.join(f'**{s}**' for s in STAGES) + '.')
if unassigned:
    out += ['', f'*{len(unassigned)} beta item(s) have no `area:` label: ' + ', '.join(f'[#{r["n"]}]({issue_url(r["n"])})' for r in unassigned) + '.*']
for x in areas:
    out += ['', f'<details><summary><b>{x["name"]}</b> · {len(x["rows"])} item(s)</summary>', '',
            f'**Past {since_h}h:** ' + ('nothing.' if not x['shift'] else ''), *shift_md(x['shift']), '',
            '| Stages | Feature | Review | Link |', '|---|---|---|---|']
    for r in x['rows']:
        alt = ''.join(r['st'])
        pr = f' · [PR #{r["pr"]["number"]}]({pr_url(r)})' if r['pr'] else ''
        rv = f'[Review]({r["review"]})' if r['review'] else '?'
        out.append(f'| `{alt}` | {r["title"]} | {rv} | [#{r["n"]}]({issue_url(r["n"])}){pr} |')
    if not x['rows']:
        out.append('| | none yet | | |')
    out += ['', '</details>']
if SHIFT.get(None):
    out += ['', f'<details><summary><b>No area</b> · past {since_h}h · {len(SHIFT[None])} event(s)</summary>', '', *shift_md(SHIFT[None]), '', '</details>']
out += ['', '**Behind:** ' + (', '.join(behind) if behind else 'none') +
        ' *(an open launch-blocking item not yet built; else below the overall built share)*', '']
if nxt:
    cta = f'Review {nxt["title"]} ([#{nxt["n"]}]({issue_url(nxt["n"])}))' + (f' at [the live page]({nxt["review"]})' if nxt['review'] else '') + ', then label it `pm-reviewed`.'
else:
    cta = 'none: nothing is waiting on you.'
out.append(f'**Your next action:** {cta}')
# Layer 2: meta-layer trial block (TRIAL, started 2026-10-10). Regenerated each run.
try:
    th = os.path.join(PROJECTS, 'socialus-ops', 'scripts', 'trial_health.py')
    block = subprocess.run(['python3', th, '--block'], capture_output=True, text=True, timeout=120).stdout.strip()
except Exception:
    block = ''
block = block or '### Meta-layer trial\n\nUnavailable: `socialus-ops/scripts/trial_health.py` did not run. Tracker: https://github.com/donlafranchi/socialus-ops/issues/89'

maxc = max([r['n'] for r in crit_rows] + [1])
L1 = ['## Criterion fulfillment', '',
      '*One row per approved or building scenario, one column per criterion. Cell = phases passed of 6 (built, checked, reviewed, shipped, smoked, PM looked): `0` none started, `6` all passed, `X` a launch-gating criterion not built, `?` the report could not tell, `-` no such criterion, `n/r` no feature report yet. Source: `socialus-web/build-log/reports/`.*', '',
      '| Scenario | Gate | ' + ' | '.join(str(i) for i in range(1, maxc + 1)) + ' |', '|---|---|' + '---|' * maxc]
for r in crit_rows:
    if r['report']:
        cs = [('?' if c['unknown'] else ('X' if c['blocker'] else str(c['done']))) for c in r['cells']]
    else:
        cs = ['n/r'] * r['n']
    cs += ['-'] * (maxc - len(cs))
    L1.append(f'| {r["id"]} {r["title"][:60]} | {r["gates"] or "-"} | ' + ' | '.join(cs) + ' |')
L1 += ['', f'**Data gaps:** {len(no_report)} of {len(crit_rows)} scenarios have no feature report ({", ".join(no_report) or "none"}) - run `regen-feature-report`; {unknown_cells} `?` cell(s) in reports that exist. A `?` or `n/r` is a data problem, not progress.', '']
L3 = ['## Live testing', '']
if test_items is None:
    L3.append(f'Could not read #{TEST_ISSUE}.')
elif not test_items:
    L3.append(f'No checkboxes found in [#{TEST_ISSUE}](https://github.com/{REPO}/issues/{TEST_ISSUE}) (body or comments): nothing to show. The click-through sheet lives outside the Issue; put one `- [ ] screen` line per screen in the Issue to feed this.')
else:
    L3.append(f'{sum(t["checked"] for t in test_items)} of {len(test_items)} screens checked.')
    L3 += ['', *[f'- [{"x" if t["checked"] else " "}] ' + (f'[{t["text"]}]({t["url"]})' if t['url'] else t['text']) for t in test_items]]
L3.append('')
next_line = out.pop()
final = out[:4] + [next_line, ''] + L1 + L3 + ['<details><summary><b>By ticket</b> · stages per area (the earlier view)</summary>', ''] + out[4:] + ['', '</details>', '', block]
out = final
open(os.path.join(root, 'DASHBOARD.md'), 'w').write('\n'.join(out) + '\n')

data = {
    'since': since_h, 'noarea': [{'k': k, 't': t, 'u': u} for k, t, u in SHIFT.get(None, [])],
    'header': header, 'crit': crit_rows, 'maxc': maxc, 'gaps': {'no_report': no_report, 'unknown': unknown_cells}, 'block': block, 'test_issue': TEST_ISSUE, 'stages': STAGES, 'colors': COLORS, 'behind': behind, 'test_items': test_items or [], 'test_ok': test_items is not None,
    'next': ({'title': nxt['title'], 'url': issue_url(nxt['n']), 'n': nxt['n'], 'review': nxt['review']} if nxt else None),
    'areas': [{'name': x['name'], 'filled': x['filled'], 'counts': x['counts'], 'total': len(x['rows']),
               'done': x['done'], 'note': x['note'], 'shift': [{'k': k, 't': t, 'u': u} for k, t, u in x['shift']],
               'rows': [{'n': r['n'], 'title': r['title'], 'st': r['st'], 'review': r['review'],
                         'issue': issue_url(r['n']), 'pr': pr_url(r), 'prn': r['pr']['number'] if r['pr'] else None}
                        for r in x['rows']]} for x in areas],
}
PAGE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Beta dashboard</title>
<style>
:root{--bg:#f8fafc;--card:#fff;--ink:#0f172a;--mute:#64748b;--off:#d1d5db;--unk:#fde68a;--line:#e2e8f0}
@media(prefers-color-scheme:dark){:root{--bg:#0b1220;--card:#111a2e;--ink:#e5e7eb;--mute:#94a3b8;--off:#334155;--unk:#854d0e;--line:#1e293b}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
main{max-width:960px;margin:0 auto;padding:20px 16px 60px}h1{font-size:1.25rem;margin:0 0 4px}
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
.foot{margin-top:18px;padding:14px;border-radius:12px;background:var(--card);border:1px solid var(--line)}.foot p{margin:4px 0}
table.crit{border-collapse:separate;border-spacing:3px;width:100%;font-size:.78rem}table.crit th{font-weight:600;color:var(--mute);text-align:center}table.crit td.sc{text-align:left;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;max-width:260px}
table.crit td.c{width:30px;height:26px;text-align:center;border-radius:4px;font-weight:700;color:#fff}.gap{margin:8px 0;padding:8px 10px;border-radius:8px;background:var(--unk);font-size:.82rem}
.trial{background:var(--card);border:1px solid var(--line);border-radius:12px;padding:6px 14px;margin:14px 0;font-size:.85rem}.trial h3{font-size:.95rem;margin:10px 0 4px}.trial p,.trial li{margin:4px 0}
@media(max-width:560px){summary{grid-template-columns:1fr}}
</style></head><body><main>
<p class="settled"><b>SETTLED — do not re-raise:</b> members are the investors and the only people paid out. “Ownership, not profit-share” is rejected. Legal/securities questions about this go to socialus-legal for counsel and never come back to the PM as a decision. SocialUs takes transaction income; any 'no fee' language is retired.</p><h1 id="h"></h1><p class="sub">Generated by scripts/dashboard.py. Tap an area to open it. A coloured box is a stage reached, grey is not yet, yellow ? is unknown.</p>
<div class="legend" id="legend"></div><div id="areas"></div><div class="foot" id="foot"></div>
<script id="data" type="application/json">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('data').textContent);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
document.getElementById('h').textContent=D.header;document.title=D.header;
const RAMP=['#b91c1c','#d97706','#ca8a04','#65a30d','#15803d'];const ramp=f=>RAMP[Math.min(4,Math.floor(f*5))];
document.getElementById('legend').innerHTML=D.stages.map((s,i)=>`<span><i class="dot" style="background:${D.colors[i]}"></i>${esc(s)}</span>`).join('')+`<span>Area edge, mean of the six phases: <span class="ramp">${RAMP.map(c=>`<i style="background:${c}"></i>`).join('')}</span> 0% to 100%</span>`;
const shiftBox=l=>`<div class="shift"><b>Past ${D.since}h</b>${l.length?l.map(e=>`<div><i>${esc(e.k)}:</i> ${e.u?`<a href="${esc(e.u)}">${esc(e.t)}</a>`:esc(e.t)}</div>`).join(''):'<div><i>nothing</i></div>'}</div>`;
const GREEN=['#e2e8f0','#dbeafe','#bfdbfe','#93c5fd','#60a5fa','#2563eb','#15803d'];
const cellStyle=c=>c.blocker?'background:#b91c1c':c.unknown?'background:repeating-linear-gradient(45deg,var(--unk),var(--unk) 4px,var(--off) 4px,var(--off) 8px);color:var(--ink)':`background:${GREEN[c.done]};${c.done<3?'color:var(--ink)':''}`;
const critHtml=`<h2 style="font-size:1.05rem;margin:18px 0 6px">Criterion fulfillment</h2><div class="legend"><span>Pale = none started</span><span>${GREEN.slice(1).map(c=>`<i class="dot" style="background:${c}"></i>`).join('')} full = built, checked, reviewed, shipped, smoked, PM looked</span><span><i class="dot" style="background:#b91c1c"></i>launch-gating criterion not built</span><span><i class="dot" style="background:var(--unk)"></i>? unknown</span></div><div style="overflow-x:auto"><table class="crit"><tr><th></th>${Array.from({length:D.maxc},(_,i)=>`<th>${i+1}</th>`).join('')}</tr>${D.crit.map(r=>`<tr><td class="sc" title="${esc(r.title)}"><b>${esc(r.id)}</b> ${esc(r.title)}${r.gates?' ·'+esc(r.gates):''}</td>${Array.from({length:D.maxc},(_,i)=>{if(!r.report)return i<r.n?`<td class="c" style="background:var(--off);color:var(--mute);font-size:.6rem">n/r</td>`:'<td></td>';const c=r.cells[i];return c?`<td class="c" style="${cellStyle(c)}" title="${esc(c.text)}">${c.unknown?'?':c.blocker?'X':c.done}</td>`:'<td></td>'}).join('')}</tr>`).join('')}</table></div><div class="gap"><b>Data gaps:</b> ${D.gaps.no_report.length} of ${D.crit.length} scenarios have no feature report (${esc(D.gaps.no_report.join(', ')||'none')}); ${D.gaps.unknown} ? cell(s) in reports that exist. n/r and ? are data problems, not progress. Run regen-feature-report.</div>`;
const md=t=>esc(t).replace(/\[([^\]]+)\]\((https?:[^)\s]+)\)/g,'<a href="$2">$1</a>').replace(/\*\*([^*]+)\*\*/g,'<b>$1</b>').replace(/`([^`]+)`/g,'<code>$1</code>');
const trialHtml='<div class="trial">'+D.block.split('\n').map(l=>l.startsWith('#')?`<h3>${md(l.replace(/^#+\s*/,''))}</h3>`:l.startsWith('- ')?`<li>${md(l.slice(2))}</li>`:l.trim()?`<p>${md(l)}</p>`:'').join('')+'</div>';
const testHtml=`<details><summary><span class="name">Live testing</span><span class="note">${!D.test_ok?'could not read #'+D.test_issue:D.test_items.length?D.test_items.filter(t=>t.checked).length+' of '+D.test_items.length+' screens checked':'no checkboxes found in #'+D.test_issue+' (body or comments)'}</span></summary><div class="rows">${D.test_items.map(t=>`<div class="row"><div class="title"><input type="checkbox" ${t.checked?'checked':''} disabled style="margin-right:8px"/>${t.url?`<a href="${esc(t.url)}">${esc(t.text)}</a>`:esc(t.text)}</div></div>`).join('')}</div></details>`;
document.getElementById('areas').innerHTML=critHtml+testHtml+'<h2 style="font-size:1.05rem;margin:18px 0 6px">By ticket</h2>'+D.areas.map(a=>{
 const bar=[0,1,2,3,4,5].map(k=>{const f=a.total?a.counts[k]/a.total:0;return `<div class="seg ${f===1?'on':''}" style="${f?'background:linear-gradient(90deg,'+D.colors[k]+' '+f*100+'%,var(--off) '+f*100+'%)':''}">${a.total?a.counts[k]+'/'+a.total:'-'}</div>`}).join('');
 const rows=shiftBox(a.shift)+(a.rows.length?a.rows.map(r=>`<div class="row"><div class="strip">${r.st.map((v,k)=>`<span class="box ${v==='?'?'unk':''}" style="${v==='●'?'background:'+D.colors[k]:(v==='·'?'background:'+D.colors[k]+';opacity:.35':'')}">${v==='?'?'?':''}</span>`).join('')}</div><div class="title">${esc(r.title)}</div><div class="links">${r.review?`<a href="${esc(r.review)}">Review</a>`:'Review ?'} · <a href="${esc(r.issue)}">#${r.n}</a>${r.pr?` · <a href="${esc(r.pr)}">PR #${r.prn}</a>`:''}</div></div>`).join(''):'<div class="row"><div class="title">none yet</div></div>');
 const mean=a.total?a.counts.reduce((x,y)=>x+y,0)/(6*a.total):0;return `<details style="border-left-color:${ramp(mean)}"><summary><span class="name">${esc(a.name)}</span><div class="bar">${bar}</div><span class="note">${Math.round(mean*100)}% overall · ${D.stages.map((n,k)=>n+' '+a.counts[k]+'/'+a.total).join(' · ')} · ${esc(a.note)} · ${a.shift.length} event(s) in the past ${D.since}h</span></summary><div class="rows">${rows}</div></details>`}).join('')+(D.noarea.length?`<details><summary><span class="name">No area</span><span class="note">${D.noarea.length} event(s) in the past ${D.since}h</span></summary><div class="rows">${shiftBox(D.noarea)}</div></details>`:'');
document.getElementById('foot').insertAdjacentHTML('beforebegin',trialHtml);document.getElementById('foot').innerHTML=`<p><b>Behind:</b> ${D.behind.length?esc(D.behind.join(', ')):'none'}</p><p><b>Your next action:</b> ${D.next?`Review ${esc(D.next.title)} (<a href="${esc(D.next.url)}">#${D.next.n}</a>)${D.next.review?` at <a href="${esc(D.next.review)}">the live page</a>`:''}, then label it <code>pm-reviewed</code>.`:'none: nothing is waiting on you.'}</p>`;
</script></main></body></html>
"""
blob = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
open(os.path.join(root, 'dashboard', 'status-dashboard.html'), 'w').write(PAGE.replace('__DATA__', blob))
print(f'wrote DASHBOARD.md, dashboard/status-dashboard.html: {total} items; ' + stage_totals)
