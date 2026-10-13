#!/usr/bin/env python3
"""The cockpit's agent-safety panel: what disappeared or got weaker since the PM last looked, read from git and GitHub, never from an agent's report.
The baseline is dashboard/last-look.json, advanced only when the PM ticks the "I looked" Issue (dashboard.py --record-look).
  safety.py --check   proves compare() on scripts/fixtures/safety (run from lint.sh)"""
import hashlib, json, os, re, subprocess, sys

SKIP = re.compile(r'\.(?:skip|todo|fixme)\(|\bskipIf\(|\bxit\(|\bxdescribe\(|\.only\(')
TESTFILE = re.compile(r'\.(?:test|spec)\.[jt]sx?$')
GUARD = re.compile(r'^(?:\.github/workflows/|scripts/(?:lint|budgets|markers|criteria|lost|cockpit|safety)|vitest[^/]*\.ts$|eslint\.config|playwright\.config|stryker|tests/(?:helpers|setup))')
REPOS = ('donlafranchi/socialus-web', 'donlafranchi/socialus-plan', 'donlafranchi/socialus-ops')


def gh(*a):
    r = subprocess.run(['gh', *a], capture_output=True, text=True)
    return json.loads(r.stdout) if r.returncode == 0 and r.stdout.strip() else None


def tests(web):
    """(test files, skipped-or-focused markers) in the code checkout; None when it is not there."""
    if not web or not os.path.isdir(web):
        return None
    files = skips = 0
    for d, dirs, fs in os.walk(web):
        dirs[:] = [x for x in dirs if x not in ('node_modules', '.next', '.git', 'build-log')]
        for f in fs:
            if TESTFILE.search(f):
                files += 1
                skips += len(SKIP.findall(open(os.path.join(d, f), errors='ignore').read()))
    return {'files': files, 'skips': skips}


def rulesets():
    out = {}
    for r in REPOS:
        rs = gh('api', f'repos/{r}/rulesets')
        if rs is None:
            continue
        full = [gh('api', f"repos/{r}/rulesets/{x['id']}") or x for x in rs]
        out[r.split('/')[1]] = hashlib.sha1(json.dumps([{k: x.get(k) for k in ('name', 'enforcement', 'rules', 'conditions', 'bypass_actors')} for x in full], sort_keys=True).encode()).hexdigest()[:10] if full else 'none'
    return out


def snapshot(decisions, web):
    tags = sum(len(re.findall(r'\[(?:always|for now)\]', e['line'])) for e in decisions)
    return {'rulings': len(decisions), 'tags': tags, 'tests': tests(web), 'rulesets': rulesets()}


def guard_prs(since):
    """Merged PRs since `since` (ISO) that touched CI, lint, guard or test-helper files: [(text, url)]."""
    out = []
    for r in REPOS:
        for p in gh('pr', 'list', '-R', r, '--state', 'merged', '--limit', '80', '--json', 'number,title,mergedAt,url,files') or []:
            hit = [f['path'] for f in p.get('files') or [] if GUARD.search(f['path'])]
            if hit and p['mergedAt'] >= since and not p['title'].startswith('docs: regenerate'):
                out.append((f"{r.split('/')[1]} #{p['number']} {p['title']} (touches {hit[0]}{' and more' if len(hit) > 1 else ''})", p['url']))
    return out[:10] + ([(f'… and {len(out) - 10} more PRs that touched CI, lint or guard files', None)] if len(out) > 10 else [])


def compare(base, now, guards=()):
    """Flags [{text, url?}] and the checks that could not be read. base None = first look: nothing to compare."""
    flags, unread = [], []
    if base is None:
        return flags, ['everything: no baseline yet; the first "I looked" tick sets it']
    if now['rulings'] < base['rulings']:
        flags.append({'text': f"Rulings removed: {base['rulings']} then, {now['rulings']} now"})
    if now['tags'] < base['tags']:
        flags.append({'text': f"[always]/[for now] tags dropped: {base['tags']} then, {now['tags']} now"})
    if now['tests'] is None or base.get('tests') is None:
        unread.append('tests deleted or skipped (code checkout not readable)')
    else:
        if now['tests']['files'] < base['tests']['files']:
            flags.append({'text': f"Test files deleted: {base['tests']['files']} then, {now['tests']['files']} now"})
        if now['tests']['skips'] > base['tests']['skips']:
            flags.append({'text': f"Tests skipped, todo'd or focused: {base['tests']['skips']} then, {now['tests']['skips']} now"})
    for r, h in (base.get('rulesets') or {}).items():
        if r in now['rulesets'] and now['rulesets'][r] != h:
            flags.append({'text': f'Ruleset changed on {r}'})
    for r, h in now['rulesets'].items():
        if h == 'none':
            flags.append({'text': f'{r} has no ruleset: nothing stops a direct push or a force push'})
    if not now['rulesets']:
        unread.append('rulesets (GitHub not readable)')
    flags += [{'text': t, 'url': u} for t, u in guards]
    return flags, unread


if __name__ == '__main__' and sys.argv[1:] == ['--check']:
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'safety')
    f = json.load(open(os.path.join(d, 'case.json')))
    got = compare(f['base'], f['now'], [tuple(g) for g in f['guards']])
    if json.loads(json.dumps(got)) != json.load(open(os.path.join(d, 'expected.json'))):
        sys.exit('safety: compare() does not match scripts/fixtures/safety/expected.json\n' + json.dumps(got, indent=1))
    if compare(None, f['now'])[0]:
        sys.exit('safety: a first look must flag nothing')
    if compare(f['base'], f['base'])[0]:
        sys.exit('safety: an unchanged repo must flag nothing')
