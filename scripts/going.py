#!/usr/bin/env python3
"""The dashboard's "Where we're going" section, from scenario frontmatter (`horizon: now|next|later`, `rank`)
and the socialus-web milestones. Replaces ROADMAP.md (the 2026-10-12 docs ruling).
  going.py --check             proves the section on scripts/fixtures/going (run from lint.sh)
  going.py --list <horizon>    one line per scenario in that horizon, by rank (README)"""
import glob, os, re, sys


def scenarios(d):
    out = []
    for p in sorted(glob.glob(os.path.join(d, 'scenario-F*.md'))):
        fm = re.match(r'---\n(.*?)\n---', open(p).read(), re.S)
        kv = dict(re.findall(r'^(\w+):\s*(.*)$', fm.group(1), re.M)) if fm else {}
        if kv.get('status') in ('shipped', 'done', 'superseded'):
            continue
        out.append({'id': kv.get('id', os.path.basename(p)[9:-3]), 'title': kv.get('title', ''), 'status': kv.get('status', '?'),
                    'horizon': kv.get('horizon'), 'rank': int(kv['rank']) if kv.get('rank', '').isdigit() else 999})
    return out


def section(scen, now_open, later_issues, now_name='Beta 11-06', later_name='After beta'):
    def lst(h):
        rows = sorted((s for s in scen if s['horizon'] == h), key=lambda s: (s['rank'], s['id']))
        return [f"{i}. {s['id']} {s['title']} *({s['status']})*" for i, s in enumerate(rows, 1)]
    n = len(later_issues)
    o = ['## Where we\'re going', '',
         '*Generated from each scenario\'s `horizon` and `rank` and the socialus-web milestones. To change it, change those; never this section.*', '',
         f'### Now · {now_name} ({now_open} open Issues)', *(lst('now') or ['- none']), '',
         '### Next', *(lst('next') or ['- none']), '',
         f'### Later · {later_name} ({n} open Issue{"" if n == 1 else "s"})', *lst('later'),
         *[f"- [#{i['number']} {i['title']}]({i['url']})" for i in sorted(later_issues, key=lambda i: i['number'])]]
    if not lst('later') and not later_issues:
        o.append('- none')
    loose = [s for s in scen if s['horizon'] not in ('now', 'next', 'later')]
    if loose:
        o += ['', '### Not sorted yet (no `horizon`)', *[f"- {s['id']} {s['title']} *({s['status']})*" for s in loose]]
    return o


if __name__ == '__main__' and sys.argv[1:2] == ['--list']:
    for s in sorted((s for s in scenarios(sys.argv[3] if len(sys.argv) > 3 else 'planning') if s['horizon'] == sys.argv[2]), key=lambda s: (s['rank'], s['id'])):
        print(f"- {s['id']}: {s['title']}")
elif __name__ == '__main__' and sys.argv[1:] == ['--check']:
    d = os.path.join(os.path.dirname(__file__), 'fixtures', 'going')
    got = '\n'.join(section(scenarios(d), 3, [{'number': 7, 'title': 'A deferred thing', 'url': 'https://github.com/x/y/issues/7'}])) + '\n'
    want = open(os.path.join(d, 'expected.md')).read()
    if got != want:
        sys.exit('going: section does not match scripts/fixtures/going/expected.md\n' + got)
