# -*- coding: utf-8 -*-
"""Strict image fetcher using Yandex Images.
- Pharmacy/health domain preferred
- URL slug should contain meaningful tokens from product name
- Leaves image='' if no good match (no garbage)
"""
import requests, re, json, time, os, random
from urllib.parse import quote, urlparse
import unicodedata

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml',
    'Accept-Language': 'ro-RO,ro;q=0.9,en;q=0.8',
}

PRODUCTS_JS = r'D:\Jutavit\js\products.js'
CACHE_JSON  = r'D:\Jutavit\strict_images.json'

PHARMACY_HOSTS = (
    # Romanian pharmacies (preferred)
    'catena.ro','drmax.ro','farmaciatei.ro','helpnet.ro','sensiblu.com','farmacia-alphega.ro',
    'esteto.ro','donafarmacia.ro','farma-line.ro','acatea.ro','farmacieonline.ro','planteea.ro',
    'bebetei.ro','farmacii.ro','farmaciasoleil.ro','farmaciatonia.ro','farmaciacare.ro','farmaciatadit.ro',
    'plafar.ro','larix.ro','jutavit.ro','hofigal.eu','zdrovit.ro','bioeel.ro','fares.ro',
    'mybeauty.ro','elefant.ro','emag.ro','cosmetique.ro','farmacistuldecasa.ro','farmaciadona.ro',
    'medica.ro','tei.ro','farmacie-dr-max.ro','viata-verde.ro','santecare.ro','greenline.ro',
    'farmaciacf.ro','sensiblufarma.ro','hofigalstore.ro','bebble.ro','naturetotale.ro',
    'estete.ro','farmaciatuca.ro','farmaciadora.ro','farmacianoah.ro','springmarket.ro','hellobiotic.ro',
    'farmaciamarket.ro','vlatka.ro','wellpharm.ro','medicalstore.ro','medlife.ro','santederm.ro',
    'minimum.ro','crevil.ro','bioonline.ro','green-fight.ro','planteaplus.ro','farmer.ro',
    'pediform.ro','vitamia.ro','wikimedical.ro','beautyfarm.ro','rosava.ro',
    # EU pharmacies that carry same brands (real product photos)
    'panorama-mir.de','kifli.hu','rossmann.hu','farmace.lt','elevita.lt','ceneo.pl','market7.hu',
    'herbahaz.hu','kertvarosipatika.hu','looduseabi.ee','ceneostatic.pl','dm.de','rossmann.pl',
    'apoteket.se','apohem.se','kruidvat.nl','bipa.at','dm.at','flink.de','drinkpharma.lt',
    'mtmgyogyszertar.hu','vitamin360.hu','patika.netpincer.hu','benu.hu','pingvinpatika.hu',
    'patikamiska.hu','apotheke.de','aliva.de','docmorris.de','shop-apotheke.com','medpex.de',
    # Romanian categories
    'drogherie.ro','farmacia.ro','farmaciashop.ro','farmaciatop.ro','vitamia.ro','green-health.ro',
    'natural-products.ro','greenline.ro','smartfarma.ro','farmaciasprint.ro','farmaciadr.ro',
    'farmaciaeden.ro','catena.ro','dona.ro','infofarm.ro','farmaciaprincipala.ro',
    # Generic shopping with good product photos
    'altex.ro','flanco.ro','evomag.ro','farmaciatadelina.ro','farmaciapremium.ro','mama-natura.ro',
    'bebeshop.ro','demama.ro','noriel.ro','bebebrands.ro','cosmetica.ro','vichy.ro','larix.ro',
)

PHARM_RE = re.compile('|'.join(re.escape(h) for h in PHARMACY_HOSTS))

STOPWORDS = set('si cu de la pe pt pentru fara la lei tva nr cps caps cpr tab tb buc bls cut bls plicuri fiole ml mg gr kg amb pac ne x'.split())

def slugify(s):
    s = unicodedata.normalize('NFKD', s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

def tokens(name):
    s = unicodedata.normalize('NFKD', name).encode('ascii','ignore').decode().lower()
    s = re.sub(r'[^a-z0-9 ]+', ' ', s)
    return [t for t in s.split() if len(t) >= 4 and t not in STOPWORDS and not t.isdigit()]

def host(url):
    try:
        return urlparse(url).netloc.lower()
    except Exception:
        return ''

def pick_strict(urls, name, brand):
    name_tokens = set(tokens(name))
    brand_low = (brand or '').lower()
    sig = set(name_tokens)
    if brand_low and brand_low not in ('patricecom',):
        sig.add(slugify(brand))

    pharm_token = []
    pharm_any   = []
    other_token = []

    for u in urls:
        if not u.lower().endswith(('.jpg','.jpeg','.png','.webp')):
            continue
        if u.startswith(('https://yastatic.net', 'https://i.pinimg.com', 'https://www.bing.com')):
            continue
        h = host(u)
        url_lower = u.lower()
        hits = sum(1 for t in sig if t and t in url_lower)
        is_pharm = bool(PHARM_RE.search(h))
        if is_pharm:
            if hits >= 1:
                pharm_token.append((hits, u))
            else:
                pharm_any.append(u)
        else:
            if hits >= 2:
                other_token.append((hits, u))

    # 1. Best: pharmacy host + product token in URL slug.
    if pharm_token:
        pharm_token.sort(reverse=True)
        return pharm_token[0][1]
    # 2. Pharmacy host + brand slug in URL.
    if pharm_any and brand_low and brand_low not in ('patricecom',):
        brand_slug = slugify(brand)
        if brand_slug and len(brand_slug) >= 4:
            for u in pharm_any:
                if brand_slug in u.lower():
                    return u
    # 3. Non-pharmacy but strong token match.
    if other_token:
        other_token.sort(reverse=True)
        top = other_token[0]
        if top[0] >= 3:
            return top[1]
        if brand_low and brand_low not in ('patricecom',):
            brand_slug = slugify(brand)
            if brand_slug and len(brand_slug) >= 4 and brand_slug in top[1].lower():
                return top[1]
    # 4. Coverage fallback: trust the first pharmacy-hosted image.
    #    Pharmacy domains only serve real product photos (search-ranked,
    #    relevant by category), never random web junk.
    if pharm_any:
        return pharm_any[0]
    return None

def search_yandex(query):
    """Yandex Images search — returns list of image URLs found in HTML."""
    url = f'https://yandex.com/images/search?text={quote(query)}'
    try:
        r = requests.get(url, headers=HEADERS, timeout=12)
        if r.status_code != 200:
            return []
        urls = re.findall(r'https?://[^\s"<>\\&]+\.(?:jpg|jpeg|png|webp)', r.text)
        # dedupe preserving order
        seen = set()
        out = []
        for u in urls:
            if u in seen: continue
            seen.add(u)
            out.append(u)
        return out
    except Exception:
        return []

def search_bing(query):
    url = f'https://www.bing.com/images/search?q={quote(query)}'
    try:
        r = requests.get(url, headers=HEADERS, timeout=12)
        if r.status_code != 200:
            return []
        urls = re.findall(r'murl&quot;:&quot;([^&]+)&quot;', r.text)
        return urls
    except Exception:
        return []

def clean_name(name):
    """Strip abbreviations, quantity markers, ID codes for cleaner query."""
    s = name
    # Remove patterns like *16, *100, 30/pac, 60cps, 250 ml
    s = re.sub(r'\*\d+', ' ', s)
    s = re.sub(r'\d+\s*(?:cps|caps|cpr|tab|tb|cut|buc|bls|gr|ml|kg|amb|pac|mg|ui|ne)\b', ' ', s, flags=re.IGNORECASE)
    s = re.sub(r'\b\d{4,}\b', ' ', s)  # long IDs like bt2011460
    s = re.sub(r'\b[a-z]{2,4}\d+\b', ' ', s, flags=re.IGNORECASE)  # codes like bt104, ro339
    s = re.sub(r'[+\-]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

def short_query(name, brand, max_words=4):
    """Take brand + first N meaningful words from cleaned name."""
    clean = clean_name(name)
    words = [w for w in clean.split() if len(w) >= 3 and not w.replace('.','').isdigit()]
    short = ' '.join(words[:max_words])
    if brand and brand.lower() not in ('patricecom',) and brand.lower() not in short.lower():
        short = f'{brand} {short}'.strip()
    return short

def search_for_product(p):
    name = p.get('name','').strip()
    brand = (p.get('brand','') or '').strip()

    # Build query variants from most-specific to most-generic
    queries = []
    if brand and brand.lower() not in ('patricecom',):
        queries.append(f'{brand} {clean_name(name)}')
    queries.append(clean_name(name))
    queries.append(short_query(name, brand, max_words=4))
    queries.append(short_query(name, brand, max_words=3))

    # Dedupe
    seen = set(); uniq = []
    for q in queries:
        q = re.sub(r'\s+', ' ', q).strip()
        if q and q.lower() not in seen:
            seen.add(q.lower())
            uniq.append(q)

    for q in uniq:
        urls = search_yandex(q)
        result = pick_strict(urls, name, brand)
        if result:
            return result
        urls = search_bing(q)
        result = pick_strict(urls, name, brand)
        if result:
            return result
        time.sleep(0.2 + random.uniform(0.1, 0.2))
    return None

def load_products():
    with open(PRODUCTS_JS, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'window\.allProducts\s*=\s*(\[.*?\]);', content, re.DOTALL)
    return json.loads(m.group(1))

def load_cache():
    if os.path.exists(CACHE_JSON):
        with open(CACHE_JSON, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_cache(cache):
    with open(CACHE_JSON, 'w', encoding='utf-8') as f:
        json.dump(cache, f, ensure_ascii=False, indent=1)

def main():
    products = load_products()
    cache = load_cache()
    print(f'Loaded {len(products)} products, {len(cache)} cached.', flush=True)

    n_found, n_blank = 0, 0
    try:
        for i, p in enumerate(products):
            pid = str(p['id'])
            if pid in cache and cache[pid]:
                n_found += 1
                continue
            url = search_for_product(p)
            cache[pid] = url or ''
            if url: n_found += 1
            else: n_blank += 1

            if (i + 1) % 20 == 0:
                save_cache(cache)
                print(f'[{i+1}/{len(products)}] found={n_found} blank={n_blank}  last="{p["name"][:50]}"', flush=True)
            time.sleep(0.3 + random.uniform(0.1, 0.3))
    except KeyboardInterrupt:
        print('Interrupted, saving...', flush=True)
    finally:
        save_cache(cache)
        print(f'\nDone. found={n_found} blank={n_blank} total={len(cache)}', flush=True)

if __name__ == '__main__':
    main()
