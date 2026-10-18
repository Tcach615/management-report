import json

with open('scratch/pages_dump.json', 'r', encoding='utf-8') as f:
    pages = json.load(f)

with open('scratch/full_report_text.txt', 'w', encoding='utf-8') as out:
    for p in pages:
        out.write(f"\n\n==================== PAGE {p['page_number']} ====================\n\n")
        out.write(p['text'])

print("Full text written to scratch/full_report_text.txt")
