import json

with open('scratch/pages_dump.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

for p in pages:
    pnum = p['page_number']
    txt = p['text'].strip()
    first_line = txt.split('\n')[0] if txt else ''
    last_line = txt.split('\n')[-1] if txt else ''
    print(f"=== PAGE {pnum:02d} ({len(txt)} chars) ===")
    print(f"START: {first_line[:90]}")
    print(f"END:   {last_line[:90]}")
