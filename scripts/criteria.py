#!/usr/bin/env python3
"""Reads the criterion reports in socialus-web (build-log/reports/<area>/F###-*.md, on main, via gh) and returns one
record per feature: criteria met / total, the unmet launch-blocking criteria, and a link to the report.
Also the reportable universe (approved or building scenarios, plus shipped features whose scenario was retired) so coverage is X of Y.
Usage: python3 scripts/criteria.py [--json | --capabilities]"""
import base64, glob, json, os, re, subprocess, sys

WEB = 'donlafranchi/socialus-web'
PLAN = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')


def gh(*a):
    return subprocess.run(['gh', *a], capture_output=True, text=True).stdout


def cells(line):
    return [c.strip() for c in line.strip().strip('|').split('|')]


def strip(c):
    return re.sub(r'[*`]', '', c).strip().lower()


def parse(text, launch_blocking):
    rows = []
    sec = text.split('## Per criterion', 1)
    if len(sec) < 2:
        return rows
    lines = []
    for l in sec[1].split('\n')[1:]:
        if l.startswith('|'):
            lines.append(l)
        elif lines:
            break
    if len(lines) < 3:
        return rows
    head = [strip(c) for c in cells(lines[0])]
    bi = next((i for i, h in enumerate(head) if h.startswith('built')), None)
    ri = next((i for i, h in enumerate(head) if h.startswith('reviewed')), None)
    if bi is None:
        return rows
    for l in lines[2:]:
        c = cells(l)
        if len(c) <= bi or not re.match(r'^\d+', c[0]):
            continue
        built = strip(c[bi])
        met = built.startswith('yes')
        refs = [int(n) for n in re.findall(r'#(\d+)', l)]
        rows.append({'n': c[0], 'text': re.sub(r'[*`]', '', c[1])[:160], 'built': 'yes' if met else ('unknown' if built.startswith('unk') else 'no'),
                     'reviewed_txt': (('yes' if strip(c[ri]).startswith('yes') else ('unknown' if strip(c[ri]).startswith('unk') else 'no')) if ri is not None and len(c) > ri else 'unknown'),
                     'blocking': (not met) and any(r in launch_blocking for r in refs), 'issues': sorted(set(refs))[:4]})
    return rows


def coverage(fid):
    """The one definition of Checked: a guards marker (F###.N) on a test covers the WHOLE criterion. Same source and same
    count as STATUS.md's Guard coverage (scripts/markers.py). Returns {criterion number: 'yes' | 'partial' | 'no'}."""
    args = ['python3', os.path.join(PLAN, 'scripts', 'markers.py'), 'coverage', fid]
    if os.environ.get('STATUS_CODE'):
        args += ['--code', os.environ['STATUS_CODE']]
    out = subprocess.run(args, capture_output=True, text=True, cwd=PLAN).stdout
    res = {}
    for l in out.split('\n'):
        m = re.match(r'- \*\*(\d+)\*\* — (.*)', l)
        if m:
            res[m.group(1)] = 'no' if 'no marked check' in m.group(2) else ('partial' if '**partial**' in m.group(2) else 'yes')
    return res


def pm_looked_set():
    """Issue and PR numbers carrying pm-reviewed (the PM's own look, recorded by record-pm-review or a closed UAT Issue)."""
    out = set()
    for kind in ('issue', 'pr'):
        for i in json.loads(gh(kind, 'list', '-R', WEB, '-s', 'all', '-l', 'pm-reviewed', '-L', '500', '--json', 'number') or '[]'):
            out.add(i['number'])
    return out


def uat_boxes():
    """Every `uat` Issue (the phone checklist #519 and any per-feature UAT Issue): lines like `- [x] F081.3 · ...`.
    A ticked box is the PM looking at that criterion. Returns ({(fid, n)}, {(fid, n)}) = (ticked, listed)."""
    ticked, listed = set(), set()
    for i in json.loads(gh('issue', 'list', '-R', WEB, '-l', 'uat', '-s', 'all', '-L', '200', '--json', 'number,title,body') or '[]'):
        if 'self-check' in i['title']:
            continue
        for m in re.finditer(r'^\s*[-*]\s+\[([ xX])\]\s+(F\d+)\.(\d+)\b', i.get('body') or '', re.M):
            listed.add((m.group(2), m.group(3)))
            if m.group(1).lower() == 'x':
                ticked.add((m.group(2), m.group(3)))
    return ticked, listed


_ID = re.compile(r'\bF\d{3}\.\d+[a-z]?\b')
_NOT_OK = re.compile(r"not\s*ok\b|✗|✘|\bwrong\b|\bbroken\b|\bfails?\b|\bfailed\b|doesn'?t work", re.I)
_OK = re.compile(r'\b(?:is |looks? |works? |all )?(?:ok|okay|fine|good|works)\b', re.I)


def uat_not_ok(ticked):
    """The PM's comments on `uat` Issues (the phone checklist). A line naming a criterion id and saying it is not ok marks that criterion
    `PM: not OK`; a later line saying it is ok, or a ticked box, clears it. Same grammar as socialus-web scripts/uat-comment.cjs, which files
    the bug. Returns {(fid, n): {'text', 'url'}}."""
    state = {}
    for i in json.loads(gh('issue', 'list', '-R', WEB, '-l', 'uat', '-s', 'all', '-L', '200', '--json', 'number,title,comments') or '[]'):
        if 'self-check' in i['title']:
            continue
        for c in sorted(i.get('comments') or [], key=lambda c: c.get('createdAt', '')):
            body = c.get('body') or ''
            if body.startswith('Marked PM: not OK'):
                continue  # the workflow's own reply, not the PM
            for line in body.split('\n'):
                ids = _ID.findall(line)
                if not ids:
                    continue
                for fid_n in set(ids):
                    fid, n = fid_n.split('.', 1)
                    if _NOT_OK.search(line):
                        state[(fid, n)] = {'text': re.sub(r'^[\s>*-]+', '', line).strip()[:160], 'url': c.get('url')}
                    elif _OK.search(line):
                        state.pop((fid, n), None)
    return {k: v for k, v in state.items() if k not in ticked}


def smoke_state():
    """(last green smoke-live run time, last run conclusion). Smoke loads pages; it does not test criteria, so it is evidence of
    'still loads after the merge', not of behaviour."""
    runs = json.loads(gh('run', 'list', '-R', WEB, '-w', 'smoke-live.yml', '-L', '60', '--json', 'conclusion,createdAt') or '[]')
    green = max((r['createdAt'] for r in runs if r['conclusion'] == 'success'), default=None)
    return green, (runs[0]['conclusion'] if runs else None)


def last_merge(fid):
    prs = json.loads(gh('pr', 'list', '-R', WEB, '-s', 'merged', '-S', f'{fid} in:title,body', '-L', '40', '--json', 'mergedAt') or '[]')
    return max((p['mergedAt'] for p in prs if p.get('mergedAt')), default=None)


def load():
    lb = {i['number'] for i in json.loads(gh('issue', 'list', '-R', WEB, '-s', 'open', '-l', 'launch-blocking', '-L', '500', '--json', 'number') or '[]')}
    tree = json.loads(gh('api', f'repos/{WEB}/git/trees/main?recursive=1') or '{}').get('tree', [])
    files = [t['path'] for t in tree if re.match(r'^build-log/reports/[^/]+/F\d+-.*\.md$', t['path'])]
    feats = []
    pmset = pm_looked_set()
    ticked, listed = uat_boxes()
    not_ok = uat_not_ok(ticked)
    green, last_conc = smoke_state()
    parents = {}
    for i in json.loads(gh('issue', 'list', '-R', WEB, '-s', 'all', '-L', '600', '--json', 'number,title') or '[]'):
        mp = re.match(r'^(F\d{3}) · (?!criterion|check|guard)', i['title'], re.I)
        if mp:
            parents.setdefault(mp.group(1), set()).add(i['number'])
    for p in sorted(files):
        raw = gh('api', f'repos/{WEB}/contents/{p}')
        try:
            text = base64.b64decode(json.loads(raw)['content']).decode()
        except Exception:
            continue
        m = re.match(r'^# (F\d+):?\s*(.*)', text)
        area = p.split('/')[2]
        rows = parse(text, lb)
        cov = coverage(m.group(1) if m else os.path.basename(p)[:4])
        fid0 = m.group(1) if m else os.path.basename(p)[:4]
        rep_date = (gh('api', f'repos/{WEB}/commits?path={p}&per_page=1', '-q', '.[0].commit.committer.date') or '').strip()
        lm = last_merge(fid0)
        smoked_feat = bool(green and lm and green > lm)
        pm_parent = bool(parents.get(fid0, set()) & pmset)
        for r in rows:
            r['checked'] = cov.get(r['n'], 'no')
            r['reviewed'] = r['reviewed_txt'] if r['built'] == 'yes' else 'no'
            r['smoked'] = 'yes' if (r['built'] == 'yes' and smoked_feat) else 'no'
            r['pm'] = 'yes' if (r['built'] == 'yes' and (pm_parent or any(n in pmset for n in r['issues']) or (fid0, r['n']) in ticked)) else 'no'
            r['not_ok'] = (fid0, r['n']) in not_ok
            r['not_ok_text'] = not_ok.get((fid0, r['n']), {}).get('text', '')
            r['uat'] = 'ticked' if (fid0, r['n']) in ticked else ('listed' if (fid0, r['n']) in listed else '')
        met = sum(1 for r in rows if r['built'] == 'yes')
        feats.append({'id': m.group(1) if m else os.path.basename(p)[:4], 'title': (m.group(2) if m else '').strip()[:90], 'area': area,
                      'total': len(rows), 'met': met, 'checked': sum(1 for r in rows if r['checked'] == 'yes'), 'reviewed': sum(1 for r in rows if r['reviewed'] == 'yes'), 'smoked': sum(1 for r in rows if r['smoked'] == 'yes'), 'pm': sum(1 for r in rows if r['pm'] == 'yes'), 'not_ok': sum(1 for r in rows if r['not_ok']), 'uat_ticked': sum(1 for r in rows if r['uat'] == 'ticked'), 'uat_listed': sum(1 for r in rows if r['uat']), 'last_merge': lm, 'report_date': rep_date, 'stale': bool(lm and rep_date and lm > rep_date), 'last_green_smoke': green, 'last_smoke': last_conc, 'blocked': [r for r in rows if r['blocking']], 'criteria': rows,
                      'url': f'https://github.com/{WEB}/blob/main/{p}'})
    return feats


def rollup(feats):
    """criterion -> feature -> area -> milestone. A criterion counts as met only when Built is yes (unknown is unmet).
    Area and milestone are plain sums of criteria, never averages of features, and never counts of Issues."""
    areas = {}
    for f in feats:
        a = areas.setdefault(f['area'], {'met': 0, 'total': 0, 'features': 0, 'red': 0})
        a['not_ok'] = a.get('not_ok', 0) + f['not_ok']; a['met'] += f['met']; a['total'] += f['total']; a['checked'] = a.get('checked', 0) + f['checked']; a['reviewed'] = a.get('reviewed', 0) + f['reviewed']; a['smoked'] = a.get('smoked', 0) + f['smoked']; a['pm'] = a.get('pm', 0) + f['pm']; a['features'] += 1; a['red'] += 1 if f['blocked'] else 0
    ms = {'not_ok': sum(f['not_ok'] for f in feats), 'reviewed': sum(f['reviewed'] for f in feats), 'smoked': sum(f['smoked'] for f in feats), 'pm': sum(f['pm'] for f in feats), 'checked': sum(f['checked'] for f in feats), 'met': sum(f['met'] for f in feats), 'total': sum(f['total'] for f in feats), 'features': len(feats), 'red': sum(1 for f in feats if f['blocked'])}
    ms['pct'] = round(100 * ms['met'] / ms['total']) if ms['total'] else 0
    return {'areas': areas, 'milestone': ms}


def universe():
    ids = set()
    pdir = os.path.join(PLAN, 'planning')
    for fn in os.listdir(pdir) if os.path.isdir(pdir) else []:
        m = re.match(r'scenario-(F\d{3})\.md$', fn)
        if m:
            st = re.search(r'^status:\s*(\w+)', open(os.path.join(pdir, fn)).read(800), re.M)
            if st and st.group(1) in ('approved', 'building'):
                ids.add(m.group(1))
    have = {re.match(r'scenario-(F\d{3})', f).group(1) for f in os.listdir(pdir) if re.match(r'scenario-F\d{3}', f)} if os.path.isdir(pdir) else set()
    for i in json.loads(gh('issue', 'list', '-R', WEB, '-s', 'closed', '-L', '600', '--json', 'title') or '[]'):
        m = re.match(r'^(F\d{3})\b', i['title'])
        if m and m.group(1) not in have:
            ids.add(m.group(1))
    return ids


ROLLUP_NOTE = '*Roll-up generated from the criterion rows below by `scripts/criteria.py --rewrite-reports`; never typed. Built = the row says yes. Checked = a guards marker covers the whole criterion (`markers.py coverage`, the same count as STATUS). Reviewed = the row says yes. Smoked = a green smoke-live run came after the feature\'s last merge (pages load; not behaviour). PM looked = a ticked box in a `uat` Issue (the phone checklist), or a linked Issue or the feature Issue carries pm-reviewed.*'


def rewrite_reports(webdir):
    """Regenerates every report's Roll-up table, and the README Features table, from the per-criterion rows."""
    changed = 0
    table = []
    byid = {f['id']: f for f in load()}
    for pth in sorted(glob.glob(os.path.join(webdir, 'build-log', 'reports', '*', 'F*.md'))):
        text = open(pth).read()
        mt = re.match(r'^# (F\d+):?\s*(.*)', text)
        fid = mt.group(1) if mt else os.path.basename(pth)[:4]
        rows = parse(text, set())
        cov = coverage(fid)
        b = sum(1 for r in rows if r['built'] == 'yes'); c = sum(1 for r in rows if cov.get(r['n']) == 'yes')
        ff = byid.get(fid, {})
        gen = f'| | built | checked | reviewed | smoked | PM looked |\n|---|---|---|---|---|---|\n| {len(rows)} criteria | {b} | {c} | {ff.get("reviewed", 0)} | {ff.get("smoked", 0)} | {ff.get("pm", 0)} |'
        m = re.search(r'(## Roll-up\n\n)((?:\|.*\n)+)(\n\*Roll-up generated[^\n]*\*\n)?', text)
        if m:
            new = text[:m.start(2)] + gen + '\n\n' + ROLLUP_NOTE + '\n' + text[m.end():]
            if new != text:
                open(pth, 'w').write(new); changed += 1
        table.append((pth.split('/')[-2], fid, (mt.group(2) if mt else '')[:60], os.path.relpath(pth, os.path.join(webdir, 'build-log', 'reports')), len(rows), b, c))
    rd = os.path.join(webdir, 'build-log', 'reports', 'README.md')
    if os.path.exists(rd):
        txt = open(rd).read()
        body = ['| Area | Feature | Criteria | Built | Checked | Reviewed | Smoked | PM looked |', '|---|---|---|---|---|---|---|---|'] + [f'| {a} | [{fid} {t}]({rel}) | {n} | {b} | {c} | {byid.get(fid, {}).get("reviewed", 0)} | {byid.get(fid, {}).get("smoked", 0)} | {byid.get(fid, {}).get("pm", 0)} |' for a, fid, t, rel, n, b, c in table]
        m = re.search(r'(## Features\n\n)((?:\|.*\n)+)', txt)
        if m:
            txt2 = txt[:m.start(2)] + '\n'.join(body) + '\n' + txt[m.end(2):]
            if txt2 != txt:
                open(rd, 'w').write(txt2); changed += 1
    return changed


if __name__ == '__main__' and '--rewrite-reports' in sys.argv:
    print('rewrote', rewrite_reports(sys.argv[sys.argv.index('--rewrite-reports') + 1]), 'files')
    sys.exit(0)

if __name__ == '__main__':
    f = load()
    if '--json' in sys.argv:
        print(json.dumps(f, indent=1))
    elif '--capabilities' in sys.argv:
        out = ['# What the app can and cannot do', '', 'Generated from the criterion reports (`scripts/criteria.py --capabilities`). Never hand-edited. Built means the code is on main; it says nothing about review or smoke.', '']
        for x in f:
            can = [r for r in x['criteria'] if r['built'] == 'yes']
            cant = [r for r in x['criteria'] if r['built'] != 'yes']
            out += [f"## {x['id']} {x['title']} ({x['area']}): {x['met']} of {x['total']}", '']
            out += [f"- Can: {r['text']}" for r in can] + [f"- Cannot yet: {r['text']}" + (' (launch-blocking)' if r['blocking'] else '') for r in cant] + ['']
        print('\n'.join(out))
    else:
        u = universe()
        got = {x['id'] for x in f}
        print(f'{len(got)} features with a criterion report; reportable universe {len(u)}; missing: {sorted(u - got)}')
