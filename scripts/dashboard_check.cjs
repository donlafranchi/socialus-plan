// Runs the dashboard page's script in jsdom (from the socialus-web checkout) and checks it drew every criterion. Exit 1 on any script error.
const {JSDOM,VirtualConsole}=require(require('path').join(process.env.PROJECTS||require('os').homedir()+'/Projects','socialus-web/node_modules/jsdom'));
const fs=require('fs');const html=fs.readFileSync(process.argv[2]||'dashboard/status-dashboard.html','utf8');const errs=[];
const vc=new VirtualConsole();vc.on('jsdomError',e=>errs.push(e.message));vc.on('error',e=>errs.push(String(e)));
const dom=new JSDOM(html,{runScripts:'dangerously',virtualConsole:vc});const d=dom.window.document;
const D=JSON.parse(d.getElementById('data').textContent);
const want=D.features.reduce((n,f)=>n+f.criteria.length,0), got=d.querySelectorAll('#grid .c').length;
const checks={'no script errors':errs.length===0,'header set':d.getElementById('h').textContent.includes('criteria'),
 'one cell per criterion':got===want,'red cells = launch blockers':d.querySelectorAll('#grid .c.red').length===D.features.reduce((n,f)=>n+f.red,0),
 'area table rows':d.querySelectorAll('#areas tr').length===Object.keys(D.areas).length+2,'trial block':d.getElementById('trial').textContent.includes('Trial health'),
 'problems listed':d.querySelectorAll('#problems li').length===D.problems.length,'live testing':d.getElementById('uat').textContent.length>50};
for(const[k,v]of Object.entries(checks))console.log((v?'ok  ':'FAIL')+' '+k);if(errs.length)console.log(errs);
console.log(`cells ${got}/${want}`);process.exit(Object.values(checks).every(Boolean)?0:1);
