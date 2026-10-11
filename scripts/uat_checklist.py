#!/usr/bin/env python3
"""Compares the phone UAT checklist (the `uat` Issues, mainly #519 in socialus-web) with the built criteria in the criterion reports.
Usage: python3 scripts/uat_checklist.py [--json]
Prints: boxes listed and ticked; built criteria with no box (to write, unless they are rules with no screen); boxes whose criterion is no longer built."""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import criteria

ticked, listed = criteria.uat_boxes()
feats = criteria.load()
built = {(f['id'], r['n']): (f, r) for f in feats for r in f['criteria'] if r['built'] == 'yes'}
missing = sorted(k for k in built if k not in listed)
gone = sorted(k for k in listed if k not in built)
res = {'listed': len(listed), 'ticked': len(ticked), 'built': len(built), 'built_without_box': [f'{a}.{b}' for a, b in missing], 'box_not_built': [f'{a}.{b}' for a, b in gone]}
if '--json' in sys.argv:
    print(json.dumps(res, indent=1))
else:
    print(f"{res['listed']} boxes listed, {res['ticked']} ticked; {res['built']} criteria built")
    print(f"built, no box ({len(missing)}; write a line for each unless it is a rule with no screen):", ', '.join(res['built_without_box']) or 'none')
    print(f"box for a criterion that is no longer built ({len(gone)}):", ', '.join(res['box_not_built']) or 'none')
