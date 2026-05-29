# -*- coding: utf-8 -*-
"""Merge product_images.json back into products.js as an 'image' field on each product.
Preserves the existing window.productCategories and window.productSubcategories blocks.
"""
import json, re

PRODUCTS_JS = r'D:\Jutavit\js\products.js'
CACHE_JSON  = r'D:\Jutavit\strict_images.json'

with open(PRODUCTS_JS, 'r', encoding='utf-8') as f:
    content = f.read()

m = re.search(r'(window\.allProducts\s*=\s*)(\[.*?\])(;)', content, re.DOTALL)
if not m:
    raise RuntimeError('Could not parse products array')

products = json.loads(m.group(2))
with open(CACHE_JSON, 'r', encoding='utf-8') as f:
    cache = json.load(f)

hit = 0
for p in products:
    url = cache.get(str(p['id']))
    if url:
        p['image'] = url
        hit += 1
    else:
        p['image'] = ''

print(f'Attached image to {hit}/{len(products)} products.')

new_array = json.dumps(products, ensure_ascii=False, separators=(',', ':'))
new_content = content[:m.start(2)] + new_array + content[m.end(2):]

with open(PRODUCTS_JS, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f'Wrote {PRODUCTS_JS}')
