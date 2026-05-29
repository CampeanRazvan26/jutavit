# -*- coding: utf-8 -*-
"""Merge new categorized products into products.js, then trigger image fetch."""
import json, re

with open(r'D:\Jutavit\new_products_categorized.json', encoding='utf-8') as f:
    new_products = json.load(f)

with open(r'D:\Jutavit\js\products.js', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'window\.allProducts\s*=\s*(\[.*?\]);\s*\nwindow\.productCategories', content, re.DOTALL)
current = json.loads(m.group(1))

# Find max id
max_id = max(p.get('id', 0) for p in current)

# Append new products
for i, np in enumerate(new_products):
    current.append({
        'id': max_id + 1 + i,
        'name': np['name'],
        'brand': np['brand'],
        'quantity': np['quantity'] or '',
        'price': np['price'],
        'offer': '',
        'category': np['category'],
        'subcategory': np['subcategory'],
        'image': ''
    })

print(f'Total products after merge: {len(current)}')

# Write back: preserve productCategories and productSubcategories sections
all_products_js = json.dumps(current, ensure_ascii=False)

# Extract the rest of the file (categories + subcategories)
rest = content[m.end():]

new_content = f'window.allProducts = {all_products_js};\nwindow.productCategories{rest}'

with open(r'D:\Jutavit\js\products.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Wrote products.js')
