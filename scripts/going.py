#!/usr/bin/env python3
"""The dashboard's "Where we're going" section: four fixed lanes, generated (Don, 2026-10-12).
  Now          being built (scenario status building/approved)
  Next         settled: approved and sequenced (scenarios only)
  Considering  a likely candidate, not approved or through council
  Later        an eventual part of the platform
A scenario carries its lane as frontmatter `horizon:` (+ `rank`); an IMAGINE.md entry as one `[lane: considering|later]` marker
under its `###` heading. Scenarios may sit in any lane; IMAGINE items only in Considering or Later. Considering -> Next needs Don's yes.
  going.py --check             proves the section on scripts/fixtures/going (run from lint.sh)
  going.py --lint [DIR]        lane rules over DIR (default `.`); --lint-check proves the lint on scripts/fixtures/going-lint
  going.py --list <lane>       one line per scenario in that lane, by rank (README)"""
import glob, os, re, sys

LANES = ('now', 'next', 'considering', 'later')
IMAGINE_LANES = ('considering', 'later')
LANE_MARK = re.compile(r'\[lane: ([^\]]*)\]')


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


BULLET = re.compile(r'^- \*\*(.+?)\*\*')


def imagine(path):
    """(lane, title) per IMAGINE.md entry (a `###` heading or a `- **Title.**` bullet) carrying a `[lane: …]` marker; others are not on the roadmap."""
    if not os.path.exists(path):
        return []
    out, title = [], None
    for l in open(path).read().split('\n'):
        b = BULLET.match(l)
        if l.startswith('### '):
            title = l[4:].strip()
        elif b:
            title = b.group(1).strip().rstrip('.')
        elif l.startswith('## '):
            title = None
        if title:
            for m in LANE_MARK.finditer(l):
                out.append((m.group(1).strip(), title))
    return out


def section(scen, now_open, later_issues, now_name='Beta 11-06', later_name='After beta', ideas=()):
    def lst(h):
        rows = sorted((s for s in scen if s['horizon'] == h), key=lambda s: (s['rank'], s['id']))
        return [f"{i}. {s['id']} {s['title']} *({s['status']})*" for i, s in enumerate(rows, 1)]
    def idea(h):
        return [f'- {t} *(IMAGINE)*' for l, t in ideas if l == h]
    n = len(later_issues)
    o = ['## Where we\'re going', '',
         '*Four fixed lanes, generated from each scenario\'s `horizon` and `rank`, IMAGINE.md\'s `[lane: …]` markers and the socialus-web milestones. To change it, change those; never this section. Moving an item from Considering to Next needs Don\'s yes.*', '',
         f'### Now · {now_name} ({now_open} open Issues) · being built', *(lst('now') or ['- none']), '',
         '### Next · settled: approved and sequenced', *(lst('next') or ['- none']), '',
         '### Considering · a likely candidate, not approved or through council', *(lst('considering') + idea('considering') or ['- none']), '',
         f'### Later · an eventual part of the platform · {later_name} ({n} open Issue{"" if n == 1 else "s"})', *lst('later'), *idea('later'),
         *[f"- [#{i['number']} {i['title']}]({i['url']})" for i in sorted(later_issues, key=lambda i: i['number'])]]
    if not lst('later') and not idea('later') and not later_issues:
        o.append('- none')
    loose = [s for s in scen if s['horizon'] not in LANES]
    if loose:
        o += ['', '### Not sorted yet (no `horizon`)', *[f"- {s['id']} {s['title']} *({s['status']})*" for s in loose]]
    return o


def lint(d, imagine_path):
    """One lane per item, only the four words; scenarios any lane, IMAGINE only considering/later; next/now need an approved scenario."""
    errs = []
    for p in sorted(glob.glob(os.path.join(d, 'scenario-F*.md'))):
        fm = re.match(r'---\n(.*?)\n---', open(p).read(), re.S)
        body = fm.group(1) if fm else ''
        hs = re.findall(r'^horizon:\s*(.*)$', body, re.M)
        st = (re.findall(r'^status:\s*(.*)$', body, re.M) or ['?'])[0].strip()
        if len(hs) > 1:
            errs.append(f'{p}: more than one `horizon:` — one lane per item')
        for h in hs[:1]:
            if h.strip() not in LANES:
                errs.append(f'{p}: lane `{h.strip()}` is not one of {", ".join(LANES)}')
            elif h.strip() in ('now', 'next') and st not in ('approved', 'building'):
                errs.append(f'{p}: lane {h.strip()} needs an approved scenario (status is {st}) — Considering until Don says yes')
    if os.path.exists(imagine_path):
        title, seen = None, 0
        for n, l in enumerate(open(imagine_path).read().split('\n'), 1):
            b = BULLET.match(l)
            if l.startswith('## ') or l.startswith('### ') or b:
                title, seen = (l if not b else b.group(1)), 0
            for m in LANE_MARK.finditer(l):
                lane = m.group(1).strip()
                seen += 1
                if not title or l.startswith('## '):
                    errs.append(f'{imagine_path}:{n}: a lane marker belongs under an entry (a ### heading or a - **Title.** bullet)')
                elif lane not in IMAGINE_LANES:
                    errs.append(f'{imagine_path}:{n}: IMAGINE lane `{lane}` must be one of {", ".join(IMAGINE_LANES)}')
                if seen > 1:
                    errs.append(f'{imagine_path}:{n}: more than one lane marker under {title} — one lane per item')
    return errs


if __name__ == '__main__' and sys.argv[1:2] == ['--list']:
    for s in sorted((s for s in scenarios(sys.argv[3] if len(sys.argv) > 3 else 'planning') if s['horizon'] == sys.argv[2]), key=lambda s: (s['rank'], s['id'])):
        print(f"- {s['id']}: {s['title']}")
elif __name__ == '__main__' and sys.argv[1:] == ['--check']:
    d = os.path.join(os.path.dirname(__file__), 'fixtures', 'going')
    got = '\n'.join(section(scenarios(d), 3, [{'number': 7, 'title': 'A deferred thing', 'url': 'https://github.com/x/y/issues/7'}], ideas=imagine(os.path.join(d, 'IMAGINE.md')))) + '\n'
    want = open(os.path.join(d, 'expected.md')).read()
    if got != want:
        sys.exit('going: section does not match scripts/fixtures/going/expected.md\n' + got)
elif __name__ == '__main__' and sys.argv[1:2] == ['--lint']:
    root = sys.argv[2] if len(sys.argv) > 2 else '.'
    e = lint(os.path.join(root, 'planning'), os.path.join(root, 'IMAGINE.md'))
    print('\n'.join(e))
    sys.exit(1 if e else 0)
elif __name__ == '__main__' and sys.argv[1:] == ['--lint-check']:
    f = os.path.join(os.path.dirname(__file__), 'fixtures', 'going-lint')
    bad = len(lint(os.path.join(f, 'bad'), os.path.join(f, 'bad', 'IMAGINE.md')))
    good = lint(os.path.join(f, 'good'), os.path.join(f, 'good', 'IMAGINE.md'))
    if bad != 5 or good:
        sys.exit(f'going: lane lint is inert or wrong (bad fixture gave {bad} of 5 faults; good gave {good})')
