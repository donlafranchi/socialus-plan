#!/usr/bin/env python3
"""Writes DASHBOARD.md, dashboard/bars/*.svg and dashboard/index.html from socialus-web Issues and PRs (gh).
Same layout and stage rules every run. Usage: python3 scripts/dashboard.py [repo-root]   (default: cwd)"""
import json, os, re, shutil, subprocess, sys
from datetime import datetime, date
from zoneinfo import ZoneInfo

REPO = 'donlafranchi/socialus-web'
MILESTONE = 'Beta 10-30'
FREEZE = date(2026, 10, 23)
LIVE = 'https://socialus.org'
AREAS = ['page-editing', 'sign-in-you', 'explore-map', 'create-posts',
         'sharing-links', 'builders-seed', 'moderation', 'ops']
STAGES = ['Built', 'Tested', 'Agent-reviewed', 'PM reviewed', 'Bugs clear', 'Done']
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
prs = gh('pr', 'list', '-R', REPO, '--state', 'all', '--limit', '400',
         '--json', 'number,title,body,state,mergedAt,labels,statusCheckRollup,'
                   'closingIssuesReferences,headRefName')

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
    roll = pr.get('statusCheckRollup') or []
    if not roll:
        return '?'
    states = [(c.get('conclusion') or c.get('state') or c.get('status') or '').upper() for c in roll]
    if any(s in RED for s in states):
        return '○'
    return '●' if all(s in GREEN for s in states) else '○'


def stages(i):
    n = i['number']
    pr = best_pr(n)
    is_bug = 'bug' in labels(i)
    built = '●' if pr and pr['mergedAt'] else '○'
    if is_bug and i['state'] == 'CLOSED':
        built = '●'
    tested = (ci(pr) if built == '●' and pr else '○')
    if built == '●' and not pr:
        tested = '?'
    if pr:
        reviewed = '●' if 'Reviewed by:' in (pr.get('body') or '') and 'review-skipped' not in labels(pr) else '○'
    else:
        reviewed = '○'
    pm = '●' if 'pm-reviewed' in labels(i) or (pr and 'pm-reviewed' in labels(pr)) else '○'
    if is_bug:
        bugs = '●' if i['state'] == 'CLOSED' else '○'
    else:
        pat = re.compile(rf'#{n}\b')
        bugs = '○' if any(pat.search((b['title'] or '') + ' ' + (b['body'] or '')) for b in open_bugs) else '●'
    if built != '●':
        bugs = '○'
    s = [built, tested, reviewed, pm, bugs]
    done = '●' if all(x == '●' for x in s) else ('○' if '○' in s else '?')
    return s + [done], pr


rows = []
for i in issues:
    area = next((l[5:] for l in labels(i) if l.startswith('area:')), None)
    st, pr = stages(i)
    rows.append({'n': i['number'], 'title': re.sub(r'^(change|bug|chore) · ', '', i['title']),
                 'area': area, 'st': st, 'pr': pr, 'open': i['state'] == 'OPEN',
                 'blocking': 'launch-blocking' in labels(i),
                 'review': first_live_url(i.get('body'), (pr or {}).get('body'))})

COLORS = ['#2563eb', '#0d9488', '#7c3aed', '#ea580c', '#65a30d', '#ca8a04']
OFF, UNK = '#d1d5db', '#fde68a'
root = sys.argv[1] if len(sys.argv) > 1 else '.'
now = datetime.now(ZoneInfo('America/Los_Angeles'))
days = (FREEZE - now.date()).days
total = len(rows)
done = sum(1 for r in rows if r['st'][5] == '●')
header = f'{MILESTONE} · {days} days to freeze · {done} of {total} beta items done · updated {now.strftime("%Y-%m-%d %H:%M")} PT'

areas = []
behind = []
for a in AREAS:
    rs = sorted((r for r in rows if r['area'] == a), key=lambda r: r['n'])
    filled = 0
    for k in range(6):
        if rs and all(r['st'][k] == '●' for r in rs):
            filled += 1
        else:
            break
    counts = [sum(1 for r in rs if r['st'][k] == '●') for k in range(6)]
    unknown = sum(1 for r in rs if '?' in r['st'])
    if not rs:
        note = 'no beta items'
    else:
        note = f'{counts[0]} of {len(rs)} built'
        if filled < 6:
            note += f'; {sum(1 for r in rs if r["st"][filled] != "●")} waiting on {STAGES[filled]}'
        if unknown:
            note += f'; {unknown} with a ?'
        if any(r['blocking'] and r['open'] and r['st'][0] != '●' for r in rs):
            behind.append(a)
    areas.append({'name': a, 'rows': rs, 'filled': filled, 'counts': counts, 'note': note,
                  'done': counts[5]})

if not behind:
    present = [x for x in areas if x['rows']]
    overall = sum(1 for r in rows if r['st'][0] == '●') / max(1, total)
    behind = [x['name'] for x in present if x['counts'][0] / len(x['rows']) < overall]

nxt = next((r for r in sorted(rows, key=lambda r: (not r['blocking'], r['n']))
            if r['open'] and r['st'][:3] == ['●', '●', '●'] and r['st'][3] != '●'), None)
unassigned = [r for r in rows if r['area'] is None]


def pr_url(r):
    return f'https://github.com/{REPO}/pull/{r["pr"]["number"]}' if r['pr'] else None


def issue_url(n):
    return f'https://github.com/{REPO}/issues/{n}'


def area_svg(x):
    w, h, g = 72, 26, 3
    n = len(x['rows'])
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{6*w+5*g}" height="{h}" viewBox="0 0 {6*w+5*g} {h}" role="img">']
    for k in range(6):
        px = k * (w + g)
        frac = x['counts'][k] / n if n else 0
        tx = '#ffffff' if frac == 1 else '#1f2937'
        label = f'{x["counts"][k]}/{n}' if n else '-'
        parts.append(f'<rect x="{px}" y="0" width="{w}" height="{h}" rx="4" fill="{OFF}"/>')
        if frac:
            parts.append(f'<clipPath id="c{k}"><rect x="{px}" y="0" width="{w}" height="{h}" rx="4"/></clipPath>'
                         f'<rect x="{px}" y="0" width="{w*frac:.1f}" height="{h}" fill="{COLORS[k]}" clip-path="url(#c{k})"/>')
        parts.append(f'<text x="{px+w/2}" y="17" font-family="-apple-system,Helvetica,Arial,sans-serif" font-size="12" font-weight="700" text-anchor="middle" fill="{tx}">{label}</text>')
    parts.append('</svg>')
    return ''.join(parts)


def strip_svg(st):
    c, g = 16, 3
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{6*c+5*g}" height="{c}" viewBox="0 0 {6*c+5*g} {c}" role="img">']
    for k, v in enumerate(st):
        fill = COLORS[k] if v == '●' else (UNK if v == '?' else OFF)
        parts.append(f'<rect x="{k*(c+g)}" y="0" width="{c}" height="{c}" rx="3" fill="{fill}"/>')
        if v == '?':
            parts.append(f'<text x="{k*(c+g)+c/2}" y="12" font-family="Helvetica,Arial,sans-serif" font-size="11" font-weight="700" text-anchor="middle" fill="#92400e">?</text>')
    parts.append('</svg>')
    return ''.join(parts)


bars = os.path.join(root, 'dashboard', 'bars')
shutil.rmtree(bars, ignore_errors=True)
os.makedirs(bars)
for x in areas:
    open(os.path.join(bars, f'{x["name"]}.svg'), 'w').write(area_svg(x))
    for r in x['rows']:
        open(os.path.join(bars, f'{x["name"]}-{r["n"]}.svg'), 'w').write(strip_svg(r['st']))

out = [f'# {header}', '',
       '*Generated by `scripts/dashboard.py`; never hand-edited. Each bar segment fills with its stage colour in proportion to the items that reached it; a feature box is coloured when it has. Grey is not yet, yellow `?` is unknown (the data to tell was not found).*', '',
       '| Area | Progress | Done | Note |', '|---|---|---|---|']
for x in areas:
    bar = ('▰' * x['filled']) + ('▱' * (6 - x['filled']))
    out.append(f'| {x["name"]} | ![{bar}](dashboard/bars/{x["name"]}.svg) | {x["done"]} of {len(x["rows"])} | {x["note"]} |')
out.append('')
out.append('Stages, in order: ' + ' → '.join(f'**{s}**' for s in STAGES) + '.')
if unassigned:
    out += ['', f'*{len(unassigned)} beta item(s) have no `area:` label: ' + ', '.join(f'[#{r["n"]}]({issue_url(r["n"])})' for r in unassigned) + '.*']
for x in areas:
    out += ['', f'<details><summary><b>{x["name"]}</b> · {len(x["rows"])} item(s)</summary>', '',
            '| Stages | Feature | Review | Link |', '|---|---|---|---|']
    for r in x['rows']:
        alt = ''.join(r['st'])
        pr = f' · [PR #{r["pr"]["number"]}]({pr_url(r)})' if r['pr'] else ''
        rv = f'[Review]({r["review"]})' if r['review'] else '?'
        out.append(f'| ![{alt}](dashboard/bars/{x["name"]}-{r["n"]}.svg) | {r["title"]} | {rv} | [#{r["n"]}]({issue_url(r["n"])}){pr} |')
    if not x['rows']:
        out.append('| | none yet | | |')
    out += ['', '</details>']
out += ['', '**Behind:** ' + (', '.join(behind) if behind else 'none') +
        ' *(an open launch-blocking item not yet built; else below the overall built share)*', '']
if nxt:
    cta = f'Review {nxt["title"]} ([#{nxt["n"]}]({issue_url(nxt["n"])}))' + (f' at [the live page]({nxt["review"]})' if nxt['review'] else '') + ', then label it `pm-reviewed`.'
else:
    cta = 'none: nothing is waiting on you.'
out.append(f'**Your next action:** {cta}')
open(os.path.join(root, 'DASHBOARD.md'), 'w').write('\n'.join(out) + '\n')

data = {
    'header': header, 'stages': STAGES, 'colors': COLORS, 'behind': behind,
    'next': ({'title': nxt['title'], 'url': issue_url(nxt['n']), 'n': nxt['n'], 'review': nxt['review']} if nxt else None),
    'areas': [{'name': x['name'], 'filled': x['filled'], 'counts': x['counts'], 'total': len(x['rows']),
               'done': x['done'], 'note': x['note'],
               'rows': [{'n': r['n'], 'title': r['title'], 'st': r['st'], 'review': r['review'],
                         'issue': issue_url(r['n']), 'pr': pr_url(r), 'prn': r['pr']['number'] if r['pr'] else None}
                        for r in x['rows']]} for x in areas],
}
PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Beta dashboard</title>
<style>
:root{--bg:#f8fafc;--card:#fff;--ink:#0f172a;--mute:#64748b;--off:#d1d5db;--unk:#fde68a;--line:#e2e8f0}
@media(prefers-color-scheme:dark){:root{--bg:#0b1220;--card:#111a2e;--ink:#e5e7eb;--mute:#94a3b8;--off:#334155;--unk:#854d0e;--line:#1e293b}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
main{max-width:960px;margin:0 auto;padding:20px 16px 60px}h1{font-size:1.25rem;margin:0 0 4px}
.sub{color:var(--mute);font-size:.85rem;margin:0 0 18px}.legend{display:flex;flex-wrap:wrap;gap:6px 14px;font-size:.8rem;margin-bottom:18px}
.legend span{display:inline-flex;align-items:center;gap:6px}.dot{width:12px;height:12px;border-radius:3px;display:inline-block}
details{background:var(--card);border:1px solid var(--line);border-radius:12px;margin:10px 0}
summary{list-style:none;cursor:pointer;padding:12px 14px;display:grid;grid-template-columns:minmax(110px,150px) 1fr;gap:6px 14px;align-items:center}
summary::-webkit-details-marker{display:none}.name{font-weight:650}.note{grid-column:1/-1;color:var(--mute);font-size:.82rem}
.bar{display:grid;grid-template-columns:repeat(6,1fr);gap:3px}.seg{height:26px;border-radius:5px;background:var(--off);color:var(--ink);font-size:.72rem;font-weight:650;display:flex;align-items:center;justify-content:center}
.seg.on{color:#fff}.rows{border-top:1px solid var(--line);padding:4px 14px 10px}
.row{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;padding:9px 0;border-bottom:1px solid var(--line);align-items:center}.row:last-child{border:0}
.strip{display:flex;gap:3px}.box{width:16px;height:16px;border-radius:3px;background:var(--off);font-size:.7rem;font-weight:800;color:#92400e;text-align:center;line-height:16px}
.box.unk{background:var(--unk)}.title{font-size:.92rem}.links{grid-column:2;font-size:.8rem;color:var(--mute)}a{color:#2563eb}
.foot{margin-top:18px;padding:14px;border-radius:12px;background:var(--card);border:1px solid var(--line)}.foot p{margin:4px 0}
@media(max-width:560px){summary{grid-template-columns:1fr}}
</style></head><body><main>
<h1 id="h"></h1><p class="sub">Generated by scripts/dashboard.py. Tap an area to open it. A coloured box is a stage reached, grey is not yet, yellow ? is unknown.</p>
<div class="legend" id="legend"></div><div id="areas"></div><div class="foot" id="foot"></div>
<script id="data" type="application/json">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('data').textContent);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
document.getElementById('h').textContent=D.header;document.title=D.header;
document.getElementById('legend').innerHTML=D.stages.map((s,i)=>`<span><i class="dot" style="background:${D.colors[i]}"></i>${esc(s)}</span>`).join('');
document.getElementById('areas').innerHTML=D.areas.map(a=>{
 const bar=[0,1,2,3,4,5].map(k=>{const f=a.total?a.counts[k]/a.total:0;return `<div class="seg ${f===1?'on':''}" style="${f?'background:linear-gradient(90deg,'+D.colors[k]+' '+f*100+'%,var(--off) '+f*100+'%)':''}">${a.total?a.counts[k]+'/'+a.total:'-'}</div>`}).join('');
 const rows=a.rows.length?a.rows.map(r=>`<div class="row"><div class="strip">${r.st.map((v,k)=>`<span class="box ${v==='?'?'unk':''}" style="${v==='●'?'background:'+D.colors[k]:''}">${v==='?'?'?':''}</span>`).join('')}</div><div class="title">${esc(r.title)}</div><div class="links">${r.review?`<a href="${esc(r.review)}">Review</a>`:'Review ?'} · <a href="${esc(r.issue)}">#${r.n}</a>${r.pr?` · <a href="${esc(r.pr)}">PR #${r.prn}</a>`:''}</div></div>`).join(''):'<div class="row"><div class="title">none yet</div></div>';
 return `<details><summary><span class="name">${esc(a.name)}</span><div class="bar">${bar}</div><span class="note">${a.done} of ${a.total} done · ${esc(a.note)}</span></summary><div class="rows">${rows}</div></details>`}).join('');
document.getElementById('foot').innerHTML=`<p><b>Behind:</b> ${D.behind.length?esc(D.behind.join(', ')):'none'}</p><p><b>Your next action:</b> ${D.next?`Review ${esc(D.next.title)} (<a href="${esc(D.next.url)}">#${D.next.n}</a>)${D.next.review?` at <a href="${esc(D.next.review)}">the live page</a>`:''}, then label it <code>pm-reviewed</code>.`:'none: nothing is waiting on you.'}</p>`;
</script></main></body></html>
"""
blob = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
open(os.path.join(root, 'dashboard', 'index.html'), 'w').write(PAGE.replace('__DATA__', blob))
print(f'wrote DASHBOARD.md, dashboard/index.html, {len(os.listdir(bars))} svgs: {done} of {total} done')
