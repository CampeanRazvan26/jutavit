# -*- coding: utf-8 -*-
"""Compare extracted products vs current products.js. Find missing."""
import json, re, sys

with open(r'D:\Jutavit\extracted_products.json', encoding='utf-8') as f:
    extracted = json.load(f)

with open(r'D:\Jutavit\js\products.js', encoding='utf-8') as f:
    content = f.read()
m = re.search(r'window\.allProducts\s*=\s*(\[.*?\]);\s*\nwindow\.productCategories', content, re.DOTALL)
current = json.loads(m.group(1))

def norm(s):
    s = s.lower().strip()
    # strip whitespace, common punctuation differences
    s = re.sub(r'[\s\-\*\,\.\(\)\[\]/\\&\+\']+', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

current_norm = {norm(p['name']): p for p in current}

new_products = []
matched = 0
for e in extracted:
    n = norm(e['name'])
    if n in current_norm:
        matched += 1
        continue
    # try partial match: first 6 words
    words = n.split()
    if len(words) >= 4:
        prefix = ' '.join(words[:4])
        found = any(ck.startswith(prefix) for ck in current_norm)
        if found:
            matched += 1
            continue
    new_products.append(e)

print(f'Extracted: {len(extracted)}')
print(f'Current  : {len(current)}')
print(f'Matched  : {matched}')
print(f'New      : {len(new_products)}')

# Save the new list
with open(r'D:\Jutavit\new_products.json', 'w', encoding='utf-8') as f:
    json.dump(new_products, f, ensure_ascii=False, indent=1)
print('\nSaved new_products.json')
print('\nFirst 10 new:')
for p in new_products[:10]:
    print(' -', p['name'])
