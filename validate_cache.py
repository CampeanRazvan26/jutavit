# -*- coding: utf-8 -*-
"""Re-validate cached images with the new strict rules. Clear bad matches."""
import json, re, sys
sys.path.insert(0, r'D:\Jutavit')
from strict_image_fetch import pick_strict, host, PHARM_RE, tokens, slugify

with open(r'D:\Jutavit\strict_images.json', encoding='utf-8') as f:
    cache = json.load(f)

with open(r'D:\Jutavit\js\products.js', encoding='utf-8') as f:
    content = f.read()
m = re.search(r'window\.allProducts\s*=\s*(\[.*?\]);', content, re.DOTALL)
products = json.loads(m.group(1))

products_by_id = {str(p['id']): p for p in products}

kept = 0
cleared = 0
for pid, url in list(cache.items()):
    if not url:
        continue
    p = products_by_id.get(pid)
    if not p:
        continue
    # Strip HTML entities from cached URLs
    if '&' in url or '"' in url:
        url = re.split(r'[&"]', url)[0]
    name = p['name']
    brand = p.get('brand', '')
    # Re-validate single URL using same logic as picker
    result = pick_strict([url], name, brand)
    if result:
        cache[pid] = result
        kept += 1
    else:
        cache[pid] = ''
        cleared += 1

with open(r'D:\Jutavit\strict_images.json', 'w', encoding='utf-8') as f:
    json.dump(cache, f, ensure_ascii=False, indent=1)

print(f'Kept: {kept}  Cleared: {cleared}')
