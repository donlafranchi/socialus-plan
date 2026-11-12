#!/usr/bin/env python3
"""The PM's to-do list, read from TODO.md (the PM, 2026-11-11: "Perhaps it can just remain in a document").
The focus section's items come first (p 1), then everything else (p 2). Each item: text (the bold part),
unlocks (the rest of the line, links removed), url (its first link, made absolute). Used by dashboard.py.
Usage: python3 scripts/todo.py [root]   (prints the items as JSON)"""
import json, os, re, sys

BLOB = 'https://github.com/donlafranchi/socialus-plan/blob/main/'


def load(root='.'):
    path = os.path.join(root, 'TODO.md')
    if not os.path.exists(path):
        return []
    items, p = [], None
    for line in open(path):
        if line.startswith('## '):
            h = line[3:].strip().lower()
            p = 1 if h.startswith('focus') else 2 if h.startswith('everything else') or h.startswith('now') else None
            continue
        m = re.match(r'^\d+\.\s+(.*)', line)
        if p is None or not m:
            continue
        body = m.group(1).strip()
        b = re.match(r'\*\*(.+?)\*\*\s*(.*)', body)
        text, rest = (b.group(1), b.group(2)) if b else (body, '')
        link = re.search(r'\]\(([^)]+)\)', body)
        url = link.group(1) if link else None
        if url and not url.startswith('http'):
            url = BLOB + url
        unlocks = re.sub(r'\(?\[[^\]]+\]\([^)]*\)\)?', '', rest).replace('`', '').strip()
        items.append({'p': p, 'text': text.rstrip(' .,:'), 'unlocks': unlocks, 'url': url})
    return items


if __name__ == '__main__':
    print(json.dumps(load(sys.argv[1] if len(sys.argv) > 1 else '.'), indent=1))
