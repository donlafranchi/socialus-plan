#!/usr/bin/env python3
"""The dashboard's "Lost since last look": approved criteria that left, stopped being built, or lost their test since the
last dashboard. The PM's one safety view (ops-pattern/process/PM-AND-AGENTS.md). The last look is dashboard/capabilities.json.
  lost.py --check   proves the section on scripts/fixtures/lost (run from lint.sh)"""
import json, os, sys


def snapshot(feats):
    return {f"{f['id']}.{c['n']}": {'text': c['text'], 'built': c['built'], 'checked': c.get('checked', 'no')}
            for f in feats for c in f['criteria']}


def section(prev, now):
    if prev is None:
        return ["## Lost since last look", "", "*First look: nothing to compare yet. From the next dashboard on, anything approved that disappears or loses its test shows here.*"]
    gone = [k for k in prev if k not in now]
    unbuilt = [k for k in prev if k in now and prev[k]['built'] == 'yes' and now[k]['built'] != 'yes']
    untested = [k for k in prev if k in now and prev[k]['checked'] == 'yes' and now[k]['checked'] != 'yes']
    o = ["## Lost since last look", "",
         "*Every approved criterion is compared with the last dashboard. Anything here needs a reason: a ruling that retired it, or a fix.*", ""]
    rows = [f"- **Gone:** {k} {prev[k]['text']}" for k in sorted(gone)] + \
           [f"- **No longer built:** {k} {now[k]['text']}" for k in sorted(unbuilt)] + \
           [f"- **Lost its test:** {k} {now[k]['text']}" for k in sorted(untested)]
    return o + (rows or ["- nothing lost"])


if __name__ == '__main__' and sys.argv[1:] == ['--check']:
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'lost')
    prev, feats = json.load(open(os.path.join(d, 'prev.json'))), json.load(open(os.path.join(d, 'feats.json')))
    got = '\n'.join(section(prev, snapshot(feats))) + '\n'
    if got != open(os.path.join(d, 'expected.md')).read():
        sys.exit('lost: section does not match scripts/fixtures/lost/expected.md\n' + got)
