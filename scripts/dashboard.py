#!/usr/bin/env python3
"""Writes DASHBOARD.md (plain text) and dashboard/status-dashboard.html (colour).
Criterion fulfillment comes only from socialus-web's build-log/reports/rollup.json (written by criteria.py); never from the reports.
Usage: python3 scripts/dashboard.py [repo-root] [--rollup PATH] [--since 12h]; then node scripts/dashboard_check.cjs
  --rollup  read a local rollup.json (e.g. a branch checkout) instead of socialus-web main. Exits 1 if the roll-up is missing or unreadable."""
import json, os, re, subprocess, sys
from datetime import datetime, date, timedelta, timezone
from zoneinfo import ZoneInfo

REPO = 'donlafranchi/socialus-web'
MILESTONE = 'Beta 11-06'
FREEZE = date(2026, 10, 30)
ROLLUP = 'build-log/reports/rollup.json'
PHASE_LABEL = {'built': 'Built', 'checked': 'Checked', 'reviewed': 'Reviewed', 'shipped': 'Shipped', 'smoked': 'Smoked', 'pm_looked': 'PM looked'}
SETTLED = '> **SETTLED — do not re-raise:** members are the investors and the only people paid out. "Ownership, not profit-share" is rejected. Legal/securities questions about this go to `socialus-legal` for counsel and never come back to the PM as a decision. SocialUs takes transaction income; any \'no fee\' language is retired.'


def gh(*args):
    return json.loads(subprocess.run(['gh', *args], check=True, capture_output=True, text=True).stdout)


def fail(msg):
    print(f'dashboard: {msg}', file=sys.stderr)
    sys.exit(1)


args = sys.argv[1:]
opt = lambda k, d=None: (args.pop(args.index(k) + 1), args.remove(k))[0] if k in args else d
local = opt('--rollup')
since_h = int(str(opt('--since', '12')).rstrip('h'))
root = args[0] if args else '.'
PLAN = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

# 1. The roll-up: the only source for criteria.
try:
    if local:
        R, source = json.load(open(local)), 'a local rollup.json (--rollup, not main)'
    else:
        raw = subprocess.run(['gh', 'api', '-H', 'Accept: application/vnd.github.raw', f'repos/{REPO}/contents/{ROLLUP}?ref=main'],
                             check=True, capture_output=True, text=True).stdout
        R, source = json.loads(raw), f'{REPO}@main:{ROLLUP}'
except (OSError, ValueError, subprocess.CalledProcessError) as x:
    fail(f'cannot read the roll-up ({x}). Run `python3 scripts/criteria.py rollup build-log/reports` in socialus-web, merge it, or pass --rollup.')
if R.get('schema') != 1 or 'features' not in R or R.get('phases') != list(PHASE_LABEL):
    fail(f'roll-up from {source} is not schema 1 with the six phases; refusing to guess')
PHASES = R['phases']
features = R['features']
live = [f for f in features if not f['retired']]
reached = max((c['score'] for f in live for c in f['criteria'] if c['status'] != 'retired'), default=0)
never = [p for p in PHASES if R['all']['totals'][p]['yes'] == 0]

# 2. Planning: approved scenarios with no report are a data problem.
reported = {f['feature'] for f in features}
no_report = []
for fn in sorted(os.listdir(os.path.join(PLAN, 'planning'))):
    m = re.match(r'scenario-(F\d{3})\.md$', fn)
    if not m or m.group(1) in reported:
        continue
    head = open(os.path.join(PLAN, 'planning', fn)).read(800)
    st = re.search(r'^status:\s*(\w+)', head, re.M)
    if st and st.group(1) in ('approved', 'building'):
        g = re.search(r'^gates:\s*(\w+)', head, re.M)
        no_report.append({'f': m.group(1), 'status': st.group(1), 'gates': g.group(1) if g else 'none'})

# 3. Live testing: one uat Issue per feature, one box per criterion (record-pm-review).
uat = []
for i in gh('issue', 'list', '-R', REPO, '-l', 'uat', '-s', 'all', '-L', '200', '--json', 'number,title,state,body,url'):
    m = re.search(r'\b(F\d{3})-', i['body'] or '') or re.search(r'\b(F\d{3})\b', i['title'])
    boxes = re.findall(r'^\s*- \[([ xX])\]', i['body'] or '', re.M)
    uat.append({'n': i['number'], 'title': i['title'], 'state': i['state'], 'url': i['url'], 'f': m.group(1) if m else None,
                'done': sum(1 for b in boxes if b != ' '), 'boxes': len(boxes)})

# 4. The PM's queue and the past shift.
needs_pm = gh('issue', 'list', '-R', REPO, '-l', 'needs-pm', '-s', 'open', '-L', '100', '--json', 'number,title,url,milestone')
needs_pm.sort(key=lambda i: (not i['milestone'], i['number']))
SINCE = datetime.now(timezone.utc) - timedelta(hours=since_h)
recent = lambda ts: bool(ts) and datetime.fromisoformat(ts.replace('Z', '+00:00')) >= SINCE
shift = []
for p in gh('pr', 'list', '-R', REPO, '-s', 'all', '-L', '100', '--json', 'number,title,url,mergedAt,createdAt'):
    if recent(p['mergedAt']):
        shift.append(('PR merged', f'#{p["number"]} {p["title"]}', p['url']))
    elif recent(p['createdAt']):
        shift.append(('PR opened', f'#{p["number"]} {p["title"]}', p['url']))
for i in gh('issue', 'list', '-R', REPO, '-s', 'all', '-L', '200', '--json', 'number,title,url,state,createdAt,closedAt'):
    if recent(i['createdAt']):
        shift.append(('Issue filed', f'#{i["number"]} {i["title"]}', i['url']))
    if i['state'] == 'CLOSED' and recent(i['closedAt']):
        shift.append(('Issue closed', f'#{i["number"]} {i["title"]}', i['url']))

problems = list(R['problems'])
problems += [f'{x["f"]}: scenario {x["status"]}' + (' (gates: launch)' if x['gates'] == 'launch' else '') + ': no report' for x in no_report]
problems += [f'UAT #{u["n"]} "{u["title"]}" names no feature; not counted' for u in uat if not u['f']]

now = datetime.now(ZoneInfo('America/Los_Angeles'))
days = (FREEZE - now.date()).days
A = R['all']
header = f'{MILESTONE} · {days} days to freeze · {A["n"]} criteria in {A["features"]} features · {A["red"]} launch blockers · updated {now.strftime("%Y-%m-%d %H:%M")} PT'
frac = lambda t, n: f'{t["yes"]}/{n}' + (f' ({t["unknown"]}?)' if t['unknown'] else '')
ceiling = (f'Best any criterion reaches today: {reached} of 6.'
           + (f' {", ".join(PHASE_LABEL[p] for p in never)} {"is" if len(never) == 1 else "are"} 0 everywhere, so no cell can be full yet.' if never else ''))
nxt = next((i for i in needs_pm if i['milestone']), needs_pm[0] if needs_pm else None)
blocker = next(((f, c) for f in live for c in f['criteria'] if c['red']), None)
if nxt:
    cta_md = f'answer [#{nxt["number"]}]({nxt["url"]}) {nxt["title"]}' + (' (launch)' if nxt['milestone'] else '') + '.'
elif blocker:
    cta_md = f'nothing needs you; agents take {blocker[0]["feature"]}.{blocker[1]["id"]} next.'
else:
    cta_md = 'none: nothing is waiting on you.'


def strip(f):
    out = []
    for c in f['criteria']:
        if c['status'] == 'retired':
            out.append('-')
        else:
            out.append(f'{c["score"]}' + ('!' if c['red'] else '') + ('?' if c['built'] == 'unknown' else ''))
    return ' '.join(out)


md = [SETTLED, '', f'# {header}', '',
      f'*Generated by `scripts/dashboard.py` from `{source}` (as-of {R["as_of"]}); never hand-edited. Colour: `dashboard/status-dashboard.html`.*', '',
      '## 1. Criterion fulfillment', '',
      'Each cell is criteria at `yes` out of criteria counted; `(n?)` are `unknown`, never counted as yes. ' + ceiling, '',
      '| Area | Criteria | ' + ' | '.join(PHASE_LABEL[p] for p in PHASES) + ' | Launch blockers |', '|---' * (len(PHASES) + 3) + '|']
for a, x in sorted(R['areas'].items()):
    md.append(f'| {a} | {x["n"]} | ' + ' | '.join(frac(x['totals'][p], x['n']) for p in PHASES) + f' | {x["red"]} |')
md.append(f'| **All** | {A["n"]} | ' + ' | '.join(f'**{frac(A["totals"][p], A["n"])}**' for p in PHASES) + f' | **{A["red"]}** |')
md += ['', 'Per criterion, the number is phases passed out of 6 (0 none started, 6 all passed); `!` a launch blocker (gates: launch and not built, or an invariant with no guard); `?` built unknown; `-` retired.', '']
for a in sorted({f['area'] for f in features}):
    fs = [f for f in features if f['area'] == a]
    md += [f'<details><summary><b>{a}</b> · {sum(f["n"] for f in fs if not f["retired"])} criteria · {sum(f["red"] for f in fs)} launch blockers</summary>', '',
           '| Feature | Gates | Built | Criteria (phases passed) |', '|---|---|---|---|']
    for f in fs:
        name = f'{f["feature"]} {f["title"]}' + (' (retired, not counted)' if f['retired'] else '')
        md.append(f'| {name} | {f["gates"]} | {frac(f["totals"]["built"], f["n"])} | `{strip(f)}` |')
    md += ['', '</details>']
md += ['', '**Gaps by type** (computed from the cells): ' + ' · '.join(f'{g} {len(v)}' for g, v in R['gaps'].items()) + '.', '',
       '**PM queue** (`needs-pm`, launch first): ' + ('; '.join(f'[#{i["number"]}]({i["url"]}) {i["title"]}' for i in needs_pm) if needs_pm else 'empty') + '.', '',
       f'**Your next action:** {cta_md}', '']
try:
    th = os.path.join(os.environ.get('PROJECTS', os.path.expanduser('~/Projects')), 'socialus-ops', 'scripts', 'trial_health.py')
    block = subprocess.run(['python3', th, '--block'], capture_output=True, text=True, timeout=120).stdout.strip()
except Exception:
    block = ''
block = block or 'Unavailable: `socialus-ops/scripts/trial_health.py` did not run. Tracker: https://github.com/donlafranchi/socialus-ops/issues/89'
md += ['## 2. Meta-layer trial', '', re.sub(r'^### .*\n+', '', block), '']
md += ['## 3. Live testing', '',
       'Source: one `uat` Issue per feature with a box per criterion (`record-pm-review`); a ticked box is that criterion\'s PM looked. '
       'The click-through sheet (#519) checks controls, not criteria, so it is linked from UAT Issues and not counted here.', '']
tied = [u for u in uat if u['f']]
md += [f'- [#{u["n"]}]({u["url"]}) {u["f"]}: {u["done"]} of {u["boxes"]} boxes ({u["state"].lower()})' for u in tied] or ['- No UAT Issue names a feature yet: live testing is 0 for every feature.']
md += ['', '## Data problems', '', 'Every `?` and every missing report, so none is mistaken for progress.', ''] + [f'- {p}' for p in problems] + ['']
md += [f'<details><summary><b>Past {since_h}h</b> · {len(shift)} event(s)</summary>', ''] + [f'- **{k}:** [{t}]({u})' for k, t, u in shift] + ['', '</details>']
os.makedirs(os.path.join(root, 'dashboard'), exist_ok=True)
open(os.path.join(root, 'DASHBOARD.md'), 'w').write('\n'.join(md) + '\n')

data = {'header': header, 'source': source, 'as_of': R['as_of'], 'phases': [PHASE_LABEL[p] for p in PHASES], 'keys': PHASES,
        'ceiling': ceiling, 'areas': R['areas'], 'all': A, 'gaps': {g: len(v) for g, v in R['gaps'].items()},
        'features': [{k: f[k] for k in ('feature', 'title', 'area', 'gates', 'retired', 'n', 'red', 'totals', 'path')}
                     | {'criteria': [{k: c[k] for k in ('id', 'text', 'status', 'score', 'red', 'built', 'issues', *PHASES)} for c in f['criteria']]}
                     for f in features],
        'needs_pm': [{'n': i['number'], 't': i['title'], 'u': i['url'], 'launch': bool(i['milestone'])} for i in needs_pm],
        'cta': {'n': nxt['number'], 't': nxt['title'], 'u': nxt['url']} if nxt else None,
        'trial': block, 'uat': tied, 'problems': problems, 'since': since_h, 'shift': [{'k': k, 't': t, 'u': u} for k, t, u in shift],
        'report_base': f'https://github.com/{REPO}/blob/main/build-log/reports/'}
PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Beta dashboard</title>
<style>
:root{--bg:#f8fafc;--card:#fff;--ink:#0f172a;--mute:#64748b;--line:#e2e8f0;--fill:37,99,235;--red:#dc2626;--warn:#fde68a}
@media(prefers-color-scheme:dark){:root{--bg:#0b1220;--card:#111a2e;--ink:#e5e7eb;--mute:#94a3b8;--line:#1e293b;--fill:96,165,250;--red:#f87171;--warn:#854d0e}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.45 -apple-system,BlinkMacSystemFont,"Segoe UI",Helvetica,Arial,sans-serif}
main{max-width:980px;margin:0 auto;padding:20px 16px 60px}h1{font-size:1.2rem;margin:0 0 4px}h2{font-size:1.05rem;margin:26px 0 8px}
.settled{margin:0 0 14px;padding:10px 12px;border-radius:8px;background:var(--warn);font-size:.85rem}.sub{color:var(--mute);font-size:.85rem;margin:0 0 12px}
table{border-collapse:collapse;width:100%;font-size:.85rem;background:var(--card)}th,td{padding:6px 8px;border-bottom:1px solid var(--line);text-align:left}th{font-weight:600;color:var(--mute)}
.scroll{overflow-x:auto}details{background:var(--card);border:1px solid var(--line);border-radius:12px;margin:8px 0}summary{cursor:pointer;padding:10px 14px;font-weight:600}summary span{font-weight:400;color:var(--mute);font-size:.85rem}
.feat{display:grid;grid-template-columns:minmax(160px,260px) 1fr;gap:6px 12px;padding:8px 14px;border-top:1px solid var(--line);align-items:center}.feat.retired{opacity:.45}
.fname{font-size:.88rem}.fname small{display:block;color:var(--mute)}.cells{display:flex;flex-wrap:wrap;gap:3px}
.c{width:22px;height:22px;border-radius:4px;border:1px solid rgba(var(--fill),.35);font-size:.62rem;display:flex;align-items:center;justify-content:center;color:var(--ink)}
.c.red{border:2px solid var(--red)}.c.unk{background-image:repeating-linear-gradient(45deg,transparent 0 3px,rgba(127,127,127,.35) 3px 5px)}.c.ret{border-style:dashed;opacity:.5}
.legend{display:flex;flex-wrap:wrap;gap:6px 16px;font-size:.8rem;margin:8px 0}.legend span{display:inline-flex;align-items:center;gap:6px}
.box{padding:12px 14px;border-radius:12px;background:var(--card);border:1px solid var(--line);font-size:.9rem}.box p{margin:6px 0}ul{margin:6px 0;padding-left:20px;font-size:.88rem}a{color:rgb(var(--fill))}
@media(max-width:560px){.feat{grid-template-columns:1fr}}
</style></head><body><main>
<p class="settled"><b>SETTLED — do not re-raise:</b> members are the investors and the only people paid out. “Ownership, not profit-share” is rejected. Legal/securities questions about this go to socialus-legal for counsel and never come back to the PM as a decision. SocialUs takes transaction income; any 'no fee' language is retired.</p>
<h1 id="h"></h1><p class="sub" id="src"></p>
<h2>1. Criterion fulfillment</h2><p class="sub" id="ceiling"></p><div class="scroll" id="areas"></div><div class="legend" id="legend"></div><div id="grid"></div><div class="box" id="queue"></div>
<h2>2. Meta-layer trial</h2><div class="box" id="trial"></div>
<h2>3. Live testing</h2><div class="box" id="uat"></div>
<h2>Data problems</h2><div class="box"><ul id="problems"></ul></div>
<details id="shift"></details>
<script id="data" type="application/json">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('data').textContent);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const md=s=>esc(s).replace(/\\*\\*(.+?)\\*\\*/g,'<b>$1</b>').replace(/`([^`]+)`/g,'<code>$1</code>').replace(/\\[([^\\]]+)\\]\\((https?:[^)]+)\\)/g,'<a href="$2">$1</a>').replace(/(^|\\s)(https:\\/\\/\\S+)/g,'$1<a href="$2">$2</a>');
const frac=(t,n)=>`${t.yes}/${n}`+(t.unknown?` <small>(${t.unknown}?)</small>`:'');
document.getElementById('h').textContent=D.header;document.title=D.header;
document.getElementById('src').textContent=`Generated by scripts/dashboard.py from ${D.source} (as-of ${D.as_of}). Never hand-edited.`;
document.getElementById('ceiling').textContent='Each cell is criteria at yes; (n?) are unknown, never counted as yes. '+D.ceiling;
const row=(name,x)=>`<tr><td>${name}</td><td>${x.n}</td>${D.keys.map(k=>`<td>${frac(x.totals[k],x.n)}</td>`).join('')}<td>${x.red?`<b style="color:var(--red)">${x.red}</b>`:0}</td></tr>`;
document.getElementById('areas').innerHTML=`<table><tr><th>Area</th><th>Criteria</th>${D.phases.map(p=>`<th>${p}</th>`).join('')}<th>Launch blockers</th></tr>${Object.keys(D.areas).sort().map(a=>row(esc(a),D.areas[a])).join('')}${row('<b>All</b>',D.all)}</table>`;
const shade=s=>s?`background:rgba(var(--fill),${(0.12+0.88*s/6).toFixed(2)});color:${s>=4?'#fff':'inherit'}`:'';
document.getElementById('legend').innerHTML='<span>Each square is one criterion (its number). Phases passed: 0 '+[0,1,2,3,4,5,6].map(s=>`<i class="c" style="${shade(s)}"></i>`).join('')+' 6</span>'+'<span><i class="c red"></i>launch blocker</span><span><i class="c unk"></i>built unknown</span><span><i class="c ret"></i>retired</span>';
const tip=c=>`${c.id}: ${c.text}\\n`+D.keys.map((k,i)=>`${D.phases[i]}: ${c[k]}`).join(' · ')+(c.issues.length?`\\nIssues: ${c.issues.map(n=>'#'+n).join(', ')}`:'')+(c.status!=='active'?`\\n${c.status}`:'');
document.getElementById('grid').innerHTML=Object.keys(D.areas).concat([...new Set(D.features.filter(f=>!D.areas[f.area]).map(f=>f.area))]).sort().map(a=>{
 const fs=D.features.filter(f=>f.area===a),x=D.areas[a];
 return `<details ${x&&x.red?'open':''}><summary>${esc(a)} <span>${x?x.n:0} criteria · ${x?x.red:0} launch blockers</span></summary>${fs.map(f=>`<div class="feat ${f.retired?'retired':''}"><div class="fname"><a href="${esc(D.report_base+f.path)}">${esc(f.feature)}</a> ${esc(f.title)}<small>${f.gates==='launch'?'gates launch · ':''}built ${frac(f.totals.built,f.n)}${f.retired?' · retired, not counted':''}</small></div><div class="cells">${f.criteria.map(c=>`<i class="c ${c.red?'red':''} ${c.built==='unknown'?'unk':''} ${c.status==='retired'||f.retired?'ret':''}" style="${shade(c.score)}" title="${esc(tip(c))}">${esc(c.id)}</i>`).join('')}</div></div>`).join('')}</details>`}).join('');
document.getElementById('queue').innerHTML=`<p><b>Gaps by type:</b> ${Object.entries(D.gaps).map(([g,n])=>`${esc(g)} ${n}`).join(' · ')}</p><p><b>PM queue</b> (needs-pm, launch first): ${D.needs_pm.length?D.needs_pm.map(i=>`<a href="${esc(i.u)}">#${i.n}</a> ${esc(i.t)}${i.launch?' <b>(launch)</b>':''}`).join('; '):'empty'}</p><p><b>Your next action:</b> ${D.cta?`answer <a href="${esc(D.cta.u)}">#${D.cta.n}</a> ${esc(D.cta.t)}.`:'none: nothing is waiting on you.'}</p>`;
document.getElementById('trial').innerHTML=D.trial.split(/\\n\\n+/).filter(p=>!p.startsWith('### ')).map(p=>p.startsWith('- ')||p.includes('\\n- ')?`<ul>${p.split('\\n').map(l=>l.startsWith('- ')?`<li>${md(l.slice(2))}</li>`:`</ul><p>${md(l)}</p><ul>`).join('')}</ul>`:`<p>${md(p)}</p>`).join('');
document.getElementById('uat').innerHTML='<p>Source: one <code>uat</code> Issue per feature with a box per criterion; a ticked box is that criterion\\'s PM looked. The click-through sheet (#519) checks controls, not criteria, so it is linked from UAT Issues and not counted here.</p>'+(D.uat.length?`<ul>${D.uat.map(u=>`<li><a href="${esc(u.url)}">#${u.n}</a> ${esc(u.f)}: ${u.done} of ${u.boxes} boxes (${esc(u.state.toLowerCase())})</li>`).join('')}</ul>`:'<p><b>No UAT Issue names a feature yet:</b> live testing is 0 for every feature.</p>');
document.getElementById('problems').innerHTML=D.problems.map(p=>`<li>${esc(p)}</li>`).join('')||'<li>none</li>';
document.getElementById('shift').innerHTML=`<summary>Past ${D.since}h <span>${D.shift.length} event(s)</span></summary><ul>${D.shift.map(e=>`<li><i>${esc(e.k)}:</i> <a href="${esc(e.u)}">${esc(e.t)}</a></li>`).join('')||'<li>nothing</li>'}</ul>`;
</script></main></body></html>
"""
blob = json.dumps(data, ensure_ascii=False).replace('</', '<\\/')
open(os.path.join(root, 'dashboard', 'status-dashboard.html'), 'w').write(PAGE.replace('__DATA__', blob))
print(f'wrote DASHBOARD.md, dashboard/status-dashboard.html from {source}: {A["n"]} criteria, {A["red"]} launch blockers, {len(problems)} data problems')
