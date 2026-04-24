# -*- coding: utf-8 -*-
"""Fetch product images from Bing Image Search (HTML scraping) for each product.
Saves progress to product_images.json so it's resumable.
"""
import requests, re, json, time, os, sys, random
from urllib.parse import quote

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Accept-Language': 'en-US,en;q=0.9,ro;q=0.8',
}

PRODUCTS_JS = r'D:\Jutavit\js\products.js'
CACHE_JSON  = r'D:\Jutavit\product_images.json'

def load_products():
    with open(PRODUCTS_JS, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'window\.allProducts\s*=\s*(\[.*?\]);', content, re.DOTALL)
    if not m:
        raise RuntimeError('Could not parse products array')
    return json.loads(m.group(1))

def load_cache():
    if os.path.exists(CACHE_JSON):
        with open(CACHE_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_JSON, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=1)

def pick_image_url(urls):
    # Prefer Romanian pharmacy sites & product-like URLs
    preferred_hosts = ('catena.ro','drmax.ro','farmaciatei.ro','helpnet.ro','sensiblu.com','farmacia-alphega.ro','esteto.ro','donafarmacia.ro','farma-line.ro','acatea.ro','farmacieonline.ro','planteea.ro','bebetei.ro')
    for u in urls:
        if any(h in u for h in preferred_hosts) and u.lower().endswith(('.jpg','.jpeg','.png','.webp')):
            return u
    for u in urls:
        if u.lower().endswith(('.jpg','.jpeg','.png','.webp')):
            return u
    return urls[0] if urls else None

def search_image(query, retries=2):
    url = f'https://www.bing.com/images/search?q={quote(query)}&form=HDRSC2&first=1'
    for attempt in range(retries + 1):
        try:
            r = requests.get(url, headers=HEADERS, timeout=12)
            if r.status_code != 200:
                time.sleep(2 + attempt * 3)
                continue
            matches = re.findall(r'murl&quot;:&quot;([^&]+)&quot;', r.text)
            if matches:
                return pick_image_url(matches)
        except Exception as e:
            time.sleep(2 + attempt * 3)
    return None

def build_query(p):
    name = p.get('name','').strip()
    brand = p.get('brand','').strip()
    q = f'{brand} {name}'.strip()
    # Strip weird chars
    q = re.sub(r'\s+', ' ', q)
    return q

def main():
    products = load_products()
    cache = load_cache()
    print(f'Loaded {len(products)} products, {len(cache)} already cached.')

    n_done, n_new, n_fail = 0, 0, 0
    try:
        for i, p in enumerate(products):
            pid = str(p['id'])
            if pid in cache and cache[pid]:
                n_done += 1
                continue
            q = build_query(p)
            url = search_image(q)
            if url:
                cache[pid] = url
                n_new += 1
            else:
                cache[pid] = None
                n_fail += 1
            # Save progress every 20 products
            if (i + 1) % 20 == 0:
                save_cache(cache)
                print(f'[{i+1}/{len(products)}] ok={n_new+n_done} new={n_new} fail={n_fail}  last="{q[:50]}"')
            # Polite delay + jitter
            time.sleep(0.3 + random.uniform(0.1, 0.5))
    except KeyboardInterrupt:
        print('Interrupted, saving progress...')
    finally:
        save_cache(cache)
        print(f'Done. cached={len(cache)} new_this_run={n_new} failures_this_run={n_fail}')

if __name__ == '__main__':
    main()
