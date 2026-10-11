#!/usr/bin/env python3
"""Dated launch reminders from planning/launch-checklist.json. An item is DUE when any trigger has happened: an event whose
`happened_on` is set, or a date at or before today. Used by dashboard.py and the Friday launch report.
Usage: python3 scripts/launch_checklist.py [--block]   (--block prints the markdown block for the report)"""
import json, os, sys
from datetime import date

PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'planning', 'launch-checklist.json')


def load(today=None):
    today = today or date.today()
    out = []
    for it in json.load(open(PATH)):
        fired = [f for f in it['fires_at'] if f.get('happened_on') or (f.get('not_before') and f['not_before'] <= today.isoformat())]
        waiting = ' or '.join(f"{f['event']} (expected {f['expected']})" for f in it['fires_at'])
        nxt = min((f['not_before'] for f in it['fires_at'] if f.get('not_before') and not f.get('happened_on')), default=None)
        days = (date.fromisoformat(nxt) - today).days if nxt else None
        out.append({**it, 'due': bool(fired), 'fired_by': [f['event'] for f in fired], 'waiting_on': waiting, 'days_to_date': days})
    return out


def block(items=None):
    items = items if items is not None else load()
    lines = ['### Launch checklist', '']
    for it in items:
        if it['due']:
            lines.append(f"- **DUE ({', '.join(it['fired_by'])}):** {it['text']} Runbook: {it['runbook']}")
        else:
            lines.append(f"- Fires at {it['waiting_on']}, whichever comes first: {it['text']}" + (f" ({it['days_to_date']} days to the date trigger.)" if it['days_to_date'] is not None else ''))
    return '\n'.join(lines)


if __name__ == '__main__':
    print(block())
