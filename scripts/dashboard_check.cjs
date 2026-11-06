// Runs the dashboard page's script in jsdom and fails on any script error or missing section (ported from the superseded #67).
// jsdom comes from JSDOM_PATH, else the socialus-web checkout's node_modules. Usage: node scripts/dashboard_check.cjs [html]
const path = require('path'), fs = require('fs'), os = require('os')
const { JSDOM, VirtualConsole } = require(process.env.JSDOM_PATH || path.join(process.env.PROJECTS || os.homedir() + '/Projects', 'socialus-web/node_modules/jsdom'))
const html = fs.readFileSync(process.argv[2] || 'dashboard/status-dashboard.html', 'utf8')
const errs = []
const vc = new VirtualConsole(); vc.on('jsdomError', (e) => errs.push(e.message)); vc.on('error', (e) => errs.push(String(e)))
const dom = new JSDOM(html, { runScripts: 'dangerously', virtualConsole: vc })
const d = dom.window.document
const D = JSON.parse(d.getElementById('data').textContent)
const crit = D.features.reduce((n, f) => n + f.criteria.length, 0)
const cards = d.querySelectorAll('details').length
// Don, 2026-11-06: the page is "Do next" (one item) and FYI groups, folded, each with a count; no instructions on it.
const fyi = [...d.querySelectorAll('details.fyi')]
const grp = (id) => d.getElementById(id)
const cnt = (id) => grp(id)?.querySelector(':scope > summary .cnt')?.textContent
const T = D.todos || []
const checks = {
  'no script errors': errs.length === 0,
  'header leads with the date, criteria right under it': (d.getElementById('h').textContent + ' ' + (d.getElementById('h').nextElementSibling?.textContent || '')).includes('criteria met'),
  'do next comes first: one item, a priority, no how-to': d.querySelector('section.sec')?.id === 'todo' && T.length <= 1 && d.querySelectorAll('#todo .todo').length === T.length && d.querySelectorAll('#todo .todo .pri').length === T.length && T.every((t) => [1, 2, 3].includes(t.p) && t.text && (!t.how || !d.body.textContent.includes(t.how.slice(0, 40)))),
  'no instructions or contents menu on the page': !d.getElementById('how') && !d.getElementById('toc') && !d.querySelector('ol.how'),
  'every FYI group is folded and shows a count': fyi.length >= 10 && fyi.every((x) => !x.open && x.querySelector(':scope > summary .cnt')?.textContent.trim() !== ''),
  'blocking the beta: first FYI group, its count, every item linked': (() => {
    const L = D.launch_left
    return !!L && fyi[0]?.id === 'soft-launch' && cnt('soft-launch') === String(L.issues.length + L.calls.length) && grp('soft-launch').querySelectorAll('li a[href]').length >= L.issues.length + L.calls.filter((c) => c.url).length
  })(),
  'a card per feature, one row per criterion': d.querySelectorAll('#features details:not(.fyi)').length >= D.features.length && d.querySelectorAll('#features details .rows .row .title').length >= crit,
  'one segment per criterion in the feature bars': d.querySelectorAll('.segbar i').length === crit,
  'waiting on your review drawn with its count': cnt('waiting') === String(D.wait_total) && d.querySelectorAll('#waiting details').length === D.wait_areas.length,
  'cockpit facts read, eight parts': D.cockpit.length === 8,
  'on hold lists the held lanes': cnt('going') === String(D.lanes.next.length + D.lanes.considering.length + D.lanes.later.length),
  // #904 — the notification counts group is always drawn: each kind, or why there are none yet.
  'notifications: each kind, or the reason it has no counts yet': (() => {
    const s = grp('notify')
    if (!s) return false
    return D.notify && D.notify.state ? D.notify.kinds.every((k) => s.textContent.includes(k.kind === 'weekend' ? 'This weekend near me' : 'New posts from Pages I follow')) : s.textContent.includes('No notification counts')
  })(),
  // #536 — slow response: the five slowest taps with their trend, or why there are none.
  'slow response: the five slowest with their trend': (() => {
    const S = D.speed, s = grp('speed')
    if (!s) return false
    if (!S || !S.state) return s.textContent.includes('No tap-speed')
    return s.querySelectorAll('.row.speed').length === Math.min(5, S.slowest.length) && S.slowest.every((x) => x.trend.length <= 7) && cnt('speed') === String((S.red || 0) + (S.amber || 0))
  })(),
  'broken checks and out-of-date reports drawn': !!grp('broken') && cnt('stale') === String(D.problems.length) && D.problems.every((p) => grp('stale').textContent.includes(p.slice(0, 30))),
}
for (const [k, v] of Object.entries(checks)) console.log((v ? 'ok   ' : 'FAIL ') + k)
if (errs.length) console.log(errs)
console.log(`features ${D.features.length}, criteria ${crit}, cards ${cards}`)
process.exit(Object.values(checks).every(Boolean) ? 0 : 1)
