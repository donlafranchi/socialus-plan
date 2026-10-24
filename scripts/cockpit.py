#!/usr/bin/env python3
"""The PM cockpit: eight sections on the HTML dashboard (the PM's dashboard, 2026-10-15), under Your to-do (ruled B, 2026-10-13; research/pm-cockpit-2026-10-12.md).
Pure: dashboard.py gathers the facts and passes them in; this turns them into sections, so the md and the html draw the same data.
A light is green, amber, red or unknown (a signal that is not read yet says so, never green). Nothing here is hand-kept.
  cockpit.py --check   proves the section on scripts/fixtures/cockpit (run from lint.sh)"""
import json, os, sys

DOT = {'green': '🟢', 'amber': '🟡', 'red': '🔴', 'unknown': '⚪'}


def lights_line(lights):
    return ' · '.join(f"{DOT[l['state']]} {l['name']}" for l in lights)


def build(f):
    """f: facts (see scripts/fixtures/cockpit/facts.json). Returns [{id, title, bold, items:[{text, url?}]}]; items fold under the bold line."""
    L = f['lights']
    s = [{'id': 'where', 'title': 'Where we are',
          'bold': f"Beta runs until April 2027 · {lights_line(L)}",
          'items': [{'text': f"{DOT[l['state']]} {l['name']}: {l['text']}"} for l in L]}]
    b = f['built']
    s.append({'id': 'built', 'title': 'Built since last look',
              'bold': f"{len(b['merged'])} PRs merged, {b['newly_met']} criteria newly met, " + ('nothing lost' if not b['lost'] else f"{b['lost']} lost") + f", {b['since']}",
              'items': [{'text': f"{p['repo']} #{p['n']} {p['title']}", 'url': p['url']} for p in b['merged']]})
    u = f['upcoming']
    s.append({'id': 'upcoming', 'title': 'Upcoming',
              'bold': f"Now: {u['now']} being built · Next: {u['next']} settled · Considering: {u['considering']} · Later: {u['later']}",
              'items': [{'text': 'The lanes in full are under Where we\'re going.'}]})
    a = f['attention']
    first = a['first']
    s.append({'id': 'attention', 'title': 'Needs your attention',
              'bold': f"1 of {a['total']}: {first['title']}" if first else 'Nothing waits on you.',
              'items': ([{'text': f"**Next:** {first['title']} ({first['kind']}). {first['ask']}", 'url': first['url']}] if first else []) +
                       [{'text': f"{i['title']} ({i['kind']})", 'url': i['url']} for i in a['rest']]})
    t = f['test']
    nx = t['next']
    s.append({'id': 'test', 'title': 'What to test',
              'bold': (f"Next walk-through: {nx['minutes']} min, as {nx['role']}. {t['done']} of {t['total']} done" if nx else f"{t['done']} of {t['total']} walk-throughs done"),
              'items': [{'text': f"{x['title']} (as {x['role']}, about {x['minutes']} min)", 'url': x['url']} for x in t['upnext']]})
    k = f['setup']
    todo = [i for i in k['items'] if not i['done']]
    s.append({'id': 'setup', 'title': 'Accounts, keys and APIs',
              'bold': f"{len(todo)} to set up before beta" + (f" · {k['private']} more in the private repo" if k['private'] else ''),
              'items': [{'text': ('✅ ' if i['done'] else '☐ ') + i['text'], 'url': i.get('url')} for i in k['items']]})
    r = f['risks']
    s.append({'id': 'risks', 'title': 'Risks and deadlines',
              'bold': f"{len(r['due'])} due soon",
              'items': [{'text': x} for x in r['due'] + r['dated']]})
    sf = f['safety']
    s.append({'id': 'safety', 'title': 'Agent safety',
              'bold': ('All clear' if not sf['unread'] else f"Nothing flagged, but {len(sf['unread'])} check{'s' if len(sf['unread']) != 1 else ''} not read yet") if not sf['flags'] else f"{len(sf['flags'])} things agents removed or weakened",
              'items': [{'text': x['text'], 'url': x.get('url')} for x in sf['flags']] + [{'text': f"Not read yet: {x}"} for x in sf['unread']]})
    return s


def md(sections):
    o = ['## The cockpit', '', '*One generated page: a bold line per section, the detail folded. Nothing in it is hand-kept; the safety panel reads GitHub, not agent reports.*', '']
    for n, x in enumerate(sections, 1):
        o += ['<details>', f"<summary><b>{n}. {x['title']}</b> — {x['bold']}</summary>", '']
        o += [f"- [{i['text']}]({i['url']})" if i.get('url') else f"- {i['text']}" for i in x['items']] or ['- nothing']
        o += ['', '</details>', '']
    return o


if __name__ == '__main__' and sys.argv[1:] == ['--check']:
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'cockpit')
    got = '\n'.join(md(build(json.load(open(os.path.join(d, 'facts.json')))))) + '\n'
    if got != open(os.path.join(d, 'expected.md')).read():
        sys.exit('cockpit: section does not match scripts/fixtures/cockpit/expected.md\n' + got)
