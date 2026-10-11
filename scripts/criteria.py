#!/usr/bin/env python3
"""Reads the per-criterion feature reports in socialus-web (build-log/reports/<area>/F###-*.md, on main, via gh) and returns one
record per feature: criteria met / total, the unmet launch-blocking criteria, and a link to the report.
Also the reportable universe (approved or building scenarios, plus shipped features whose scenario was retired) so coverage is X of Y.
Usage: python3 scripts/criteria.py [--json | --capabilities]"""
import base64, json, os, re, subprocess, sys

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
                     'blocking': (not met) and any(r in launch_blocking for r in refs), 'issues': sorted(set(refs))[:4]})
    return rows


def load():
    lb = {i['number'] for i in json.loads(gh('issue', 'list', '-R', WEB, '-s', 'open', '-l', 'launch-blocking', '-L', '500', '--json', 'number') or '[]')}
    tree = json.loads(gh('api', f'repos/{WEB}/git/trees/main?recursive=1') or '{}').get('tree', [])
    files = [t['path'] for t in tree if re.match(r'^build-log/reports/[^/]+/F\d+-.*\.md$', t['path'])]
    feats = []
    for p in sorted(files):
        raw = gh('api', f'repos/{WEB}/contents/{p}')
        try:
            text = base64.b64decode(json.loads(raw)['content']).decode()
        except Exception:
            continue
        m = re.match(r'^# (F\d+):?\s*(.*)', text)
        area = p.split('/')[2]
        rows = parse(text, lb)
        met = sum(1 for r in rows if r['built'] == 'yes')
        feats.append({'id': m.group(1) if m else os.path.basename(p)[:4], 'title': (m.group(2) if m else '').strip()[:90], 'area': area,
                      'total': len(rows), 'met': met, 'blocked': [r for r in rows if r['blocking']], 'criteria': rows,
                      'url': f'https://github.com/{WEB}/blob/main/{p}'})
    return feats


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


if __name__ == '__main__':
    f = load()
    if '--json' in sys.argv:
        print(json.dumps(f, indent=1))
    elif '--capabilities' in sys.argv:
        out = ['# What the app can and cannot do', '', 'Generated from the per-criterion feature reports (`scripts/criteria.py --capabilities`). Never hand-edited. Built means the code is on main; it says nothing about review or smoke.', '']
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
