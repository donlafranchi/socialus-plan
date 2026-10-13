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
const checks = {
  'no script errors': errs.length === 0,
  'header leads with criteria': d.getElementById('h').textContent.includes('criteria met'),
  'a card per feature and area': cards >= D.features.length + D.areas.length,
  'one row per criterion': d.querySelectorAll('details .rows .row .title').length >= crit,
  'launch checklist drawn': !D.launch || D.launch.length === 0 || d.body.textContent.includes('Launch checklist'),
  'waiting on you drawn': d.body.textContent.includes('Waiting on you: ' + D.wait_total) && d.querySelectorAll('summary b').length >= D.wait_areas.length,
  'one segment per criterion, in every feature and area bar': d.querySelectorAll('.segbar i').length === 2 * crit,
  'how to read, five lines': d.querySelectorAll('ol.how li').length === 5,
  'your UAT line': d.body.textContent.includes('Your UAT: ' + D.your_uat.ticked + ' of ' + D.your_uat.total + ' walk-throughs done'),
  'cockpit drawn, eight sections': D.cockpit.length === 8 && d.querySelectorAll('[id^=cockpit-]').length === 8,
  'data problems drawn': d.body.textContent.includes('Data problems'),
  'a testing notice when the list is empty': !D.test_notice || d.body.textContent.includes(D.test_notice.slice(0, 30)),
}
for (const [k, v] of Object.entries(checks)) console.log((v ? 'ok   ' : 'FAIL ') + k)
if (errs.length) console.log(errs)
console.log(`features ${D.features.length}, criteria ${crit}, cards ${cards}`)
process.exit(Object.values(checks).every(Boolean) ? 0 : 1)
