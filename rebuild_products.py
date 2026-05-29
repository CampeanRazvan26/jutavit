# -*- coding: utf-8 -*-
"""Rebuild products.js from photo extraction ONLY. Clean garbage entries."""
import json, re

with open(r'D:\Jutavit\extracted_products.json', encoding='utf-8') as f:
    extracted = json.load(f)

# Non-product noise to skip
NOISE = (
    'reducere', 'stand ', 'stand-', 'stand_', 'taxa termo', 'cheltuieli',
    'pres servicii', 'revista hofigal', 'masina etichetat', 'matrita dubla',
    'cliseu digital', 'discount unguent', 'discount rectostop',
    'kit pentru indepartarea capuselor',
)

def is_noise(name):
    n = name.lower()
    for kw in NOISE:
        if kw in n:
            return True
    return False

def clean_name(name):
    s = name.strip()
    # Title-case but preserve brand all-caps
    return s

# Filter and dedupe
seen = {}
filtered = []
for p in extracted:
    name = clean_name(p['name'])
    if is_noise(name):
        continue
    key = re.sub(r'[\s\-\*\.\,\(\)/\\&\+\']+', ' ', name.lower()).strip()
    if key in seen:
        continue
    seen[key] = True
    filtered.append(p)

print(f'Extracted   : {len(extracted)}')
print(f'After clean : {len(filtered)}')

# Apply categorization (use the same rules)
import sys; sys.path.insert(0, r'D:\Jutavit')
from categorize_new import RULES

def categorize(name):
    n = name.lower()
    for cat, sub, kws in RULES:
        for kw in kws:
            if kw and kw in n:
                return cat, sub
    return 'suplimente', 'Articole Diverse'

for p in filtered:
    cat, sub = categorize(p['name'])
    p['category'] = cat
    p['subcategory'] = sub

# Build final list
out = []
for i, p in enumerate(filtered, start=1):
    out.append({
        'id': i,
        'name': p['name'],
        'brand': p.get('brand', 'PATRICECOM'),
        'quantity': p.get('quantity', ''),
        'price': float(p.get('price', 0.0)),
        'offer': '',
        'category': p['category'],
        'subcategory': p['subcategory'],
        'image': ''
    })

# Load existing products.js to preserve categories/subcategories section
with open(r'D:\Jutavit\js\products.js', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'window\.allProducts\s*=\s*(\[.*?\]);\s*\nwindow\.productCategories', content, re.DOTALL)
rest = content[m.end():]

new_content = f'window.allProducts = {json.dumps(out, ensure_ascii=False)};\nwindow.productCategories{rest}'

with open(r'D:\Jutavit\js\products.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'Wrote {len(out)} products to products.js')

# Cat stats
from collections import Counter
cats = Counter(p['category'] for p in out)
print('\nCategory counts:')
for k, v in sorted(cats.items(), key=lambda x: -x[1]):
    print(f'  {k:14}: {v}')
