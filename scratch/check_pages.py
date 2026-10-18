import json

with open('scratch/pages_dump.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages:
    lines = [l.strip() for l in p['text'].split('\n') if l.strip()]
    first_few = ' // '.join(lines[:3]) if lines else 'EMPTY'
    pnum = p['page_number']
    chars = len(p['text'])
    print(f"P.{pnum:02d} ({chars}c): {first_few[:120]}")
