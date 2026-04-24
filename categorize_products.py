# -*- coding: utf-8 -*-
"""Categorize products and write out new products.js with category + subcategory"""
import json
import re

# Load existing products
with open(r'D:\Jutavit\js\products.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the JSON array
m = re.search(r'window\.allProducts\s*=\s*(\[.*?\]);?\s*$', content, re.DOTALL)
if not m:
    m = re.search(r'window\.allProducts\s*=\s*(\[.*\])', content, re.DOTALL)
raw = m.group(1)
products = json.loads(raw)

# Category + subcategory rules (order matters - first match wins)
# Structure: (category, subcategory, keywords_list)
rules = [
    # INTIME (must come before "sensitive" for Bella etc)
    ('intime', 'Prezervative', ['durex', 'prezervativ', 'condom']),
    ('intime', 'Teste Sarcina', ['test sarcin', 'test ovulat', 'test de sarcin']),
    ('intime', 'Teste Rapide', ['test rapid', 'test streptoc', 'test chlamyd', 'test veneris', 'test alergii', 'test lyme', 'test intolerant']),
    ('intime', 'Absorbante', ['absorbant', 'alway', 'bella perfecta', 'bella clasic', 'bella sensitive', 'bella medica', 'bella classic', 'bella nov', 'bella in', 'bella tampo']),
    ('intime', 'Tampoane', ['tampon', 'tamp.', 'tamp ', 'ob proc', 'libresse', 'o.b.']),
    ('intime', 'Lubrifianti', ['lubrifiant', 'lubrigrl', 'lubrig']),
    ('intime', 'Igiena Intima', ['intim', 'dus intim', 'gel intim', 'lactacyd', 'lacalut sensi']),

    # COPII & BEBELUSI
    ('copii', 'Scutece', ['scutec', 'pampers', 'seni soft super', 'seni normal', 'seni super', 'seni classic', 'seni clasic', 'seni active', 'seni activ', 'seni basic', 'seni medium', 'seni large', 'chilot large', 'chilot mediu', 'seni lady']),
    ('copii', 'Biberoane', ['biberon']),
    ('copii', 'Suzete', ['suzet']),
    ('copii', 'Tetine', ['tetina', 'tetin']),
    ('copii', 'Servetele Umede', ['servetel', 'servetele umede', 'serv.umed', 'serv. umed', 'servete']),
    ('copii', 'Igiena Copii', ['baby lotion', 'bakuchiol', 'caonatur', 'bebe', 'copii', 'kid', 'junior', 'nou-nascut', 'infantil', 'bello', 'my friend', 'beb039', 'beb042', 'cimmerin']),
    ('copii', 'Vitamine Copii', ['picaturi vitamina', 'picaturi d3', 'multivit copii', 'multiv.copii', 'picaturi propolis', 'ceai babycalm', 'vitamina d picaturi']),
    ('copii', 'Accesorii Bebe', ['linguri', 'cana cu man', 'cana cu pai', 'cana decorata', 'farfurie', 'bavete', 'lantisor', 'organizer medicamente']),

    # IGIENA ORALA
    ('igiena_orala', 'Paste Dinti', ['pasta de dinti', 'pasta dinti', 'pasta.dinti', 'pd.colgate', 'pd colgate', 'oral-b pasta', 'colgate pasta', 'sensodyne', 'kin pasta', 'lacalut']),
    ('igiena_orala', 'Periute Dinti', ['perie de dint', 'perie biberon', 'periu', 'kin periu', 'jordan', 'peri ', 'kin periu']),
    ('igiena_orala', 'Apa Gura', ['apa de gura', 'apa gura', 'kin apa', 'listerin']),
    ('igiena_orala', 'Alte Orale', ['ata dentara', 'interdentar', 'cloraxidina', 'dentit', 'stomatolog', 'inel dentit']),

    # APARATURA
    ('aparatura', 'Tensiometre', ['tensiometru']),
    ('aparatura', 'Termometre', ['termometru', 'termometre']),
    ('aparatura', 'Glucometre', ['glucometr', 'glucoetru']),
    ('aparatura', 'Nebulizatoare', ['nebulizator', 'aerosol']),
    ('aparatura', 'Cantare', ['cantar']),
    ('aparatura', 'Pulsoximetre', ['pulsoximetru', 'pulsoxim']),
    ('aparatura', 'Inhalatoare', ['inhalator', 'vapour', 'vapor rub']),
    ('aparatura', 'Aspiratoare Nazale', ['aspirator naz', 'aspirator-nazal']),
    ('aparatura', 'Irigatoare', ['irigator', 'dus nazal', 'nazomer', 'nosko']),

    # PANSAMENTE
    ('pansamente', 'Plasturi', ['plasturi', 'plast.', 'plasture', 'plast ', 'plastur', 'plast .', 'qplaster', 'plaster']),
    ('pansamente', 'Fese & Bandaje', ['bandaj', 'fasa', 'fese', 'fasa ', 'fasa-help', 'fesi', 'sani bandaj', 'manseta', 'manset', 'tifon', 'compres']),
    ('pansamente', 'Leucoplast', ['leucoplast']),
    ('pansamente', 'Genunchiera', ['genunchier', 'genunchiera', 'glezniera', 'cotiera']),
    ('pansamente', 'Vata', ['vata med', 'vata ', 'vata medicinala']),

    # OCHI
    ('ochi', 'Suplimente Ochi', ['optolutein', 'lutein', 'ocluzo', 'jutavit lutein']),
    ('ochi', 'Ochelari Citit', ['ochelari de citit', 'ochelari ']),
    ('ochi', 'Picaturi Ochi', ['vizik', 'picatur ochi', 'picatur ochi', 'allergy pic.de ochi']),

    # PROSTATA
    ('prostata', 'Suplimente Prostata', ['prosta', 'prostata', 'prostat', 'prostagood', 'prostaful', 'saw palmetto']),

    # SLABIT
    ('slabit', 'Slim Produse', ['slim', 'slabit', 'slab ', 'jutavit slim']),
    ('slabit', 'Glucomannan', ['glucomanan', 'glucomannan']),
    ('slabit', 'Cafea Verde', ['cafea verde', 'green coffee']),
    ('slabit', 'Apuretin', ['apuretin']),

    # ARTICULATII
    ('articulatii', 'Colagen', ['collagen', 'colagen']),
    ('articulatii', 'Glucozamina', ['glucozamin', 'glucozamina', 'chondrosam', 'condroitin']),
    ('articulatii', 'Calciu D3', ['calciu+d3', 'calciu d3', 'caciu d3', 'calciu+mg', 'calcii-tub', 'cocos calciu', 'calciu natural', 'calcimax', 'jutavit calciu']),
    ('articulatii', 'Balsamuri', ['balsam piker', 'balsam calu', 'balsam puter', 'balsam urs', 'schmees balsam', 'crevil', 'ghear', 'gheara drac']),

    # DIGESTIE
    ('digestie', 'Probiotice', ['probiotic', 'probiofix', 'lactozil', 'enterol', 'bioseptil', 'biomicin', 'biosept', 'probium']),
    ('digestie', 'Enzime Digestive', ['enzima lact', 'enzima lactaza', 'enzime', 'digestive enzym', 'jutavit digestive']),
    ('digestie', 'Stomac', ['pelin', 'anason', 'stomac', 'hapciu', 'gastric', 'stomac sanatos']),
    ('digestie', 'Laxative', ['laxativ', 'laxaclean', 'laxativ-', 'laredib', 'laricol', 'salprogel']),
    ('digestie', 'Ficat', ['ficat', 'silimarina', 'hepato', 'hepatil', 'armurariu']),

    # IMUNITATE (put late - more specific keywords can match first)
    ('imunitate', 'Propolis', ['propolis', 'propolie', 'propol-']),
    ('imunitate', 'Echinacea', ['echinacea', 'echinac']),
    ('imunitate', 'Raceala & Gripa', ['raceala', 'gripa', 'gripovit', 'imuno', 'imun', 'halls', 'prevomit', 'strepsils', 'tick', 'stop tick', 'bebble sampon', 'halls']),
    ('imunitate', 'Suplimente Imunitate', ['imunit', 'imuno', 'multivit.imunocom', 'multiv.imunoc']),

    # SOMN & STRES
    ('somn', 'Melatonina', ['melatonin', 'noapte buna']),
    ('somn', 'Valeriana', ['valeriana']),
    ('somn', 'Antistres', ['antistres', 'harmony', 'calm', 'good night', 'sleep', 'somn limi']),

    # VITAMINE
    ('vitamine', 'Vitamina C', ['vitamina c', 'vit.c', 'vit c', 'c vitamin', 'c 1000', 'c-500', 'vitamin c', 'vita c', 'vitc', 'vita-c']),
    ('vitamine', 'Vitamina D', ['vitamina d', 'vit.d3', 'vit d3', 'd3 ', 'vit.d', 'vitamin d', 'detrical', 'vit d ', 'picaturi d3', 'd-manoza']),
    ('vitamine', 'Vitamina B', ['vitamina b', 'vit.b', 'vit b', 'vitamin b', 'b complex', 'b-complex', 'b-cure', 'biotina b7', 'biotin', 'biotin']),
    ('vitamine', 'Vitamina A&E', ['vitamina a', 'vit.a', 'vitamina e', 'vit.e', 'vit e', 'vitamin e', 'vit a', 'vitamin a']),
    ('vitamine', 'Vitamina K', ['vitamin k', 'vit.k', 'k2', 'natural k2']),
    ('vitamine', 'Multivitamine', ['multivitamin', 'multiv.', 'multivit', '9 vita', '8+1 vita']),
    ('vitamine', 'Vitamine Efervescente', ['efervescent', 'effervesc']),

    # MINERALE
    ('minerale', 'Magneziu', ['magneziu', 'magnesium', 'maximag', 'biglicin']),
    ('minerale', 'Calciu', ['calciu', 'calcium', 'calci', 'fluorkin']),
    ('minerale', 'Zinc', ['zinc']),
    ('minerale', 'Fier', ['fier organic', 'fier ', 'iron']),
    ('minerale', 'Seleniu', ['seleniu']),
    ('minerale', 'Crom', ['crom org', 'crom ']),
    ('minerale', 'Alte Minerale', ['molibden', 'iod', 'kalium']),

    # COSMETICE
    ('cosmetice', 'Creme Fata', ['crema antirid', 'crema hidratan', 'crema contur', 'crema fata', 'crema zi', 'crema noapte', 'crema ochi', 'spf', 'crema vit', 'crema anti', 'gel hidratant', 'crema catifel', 'crema nutrit', 'crema tonifi', 'crema colage', 'wrinkle', 'anti-ageing', 'hydra boost', 'gleansing', 'mattify', 'good skin']),
    ('cosmetice', 'Creme Corp', ['crema corp', 'crema maini', 'crema galbenele', 'crema maini', 'crema calcaie', 'crema picioare', 'crema protect', 'crema propolis', 'crema rostop', 'crema ureea', 'crema uree', 'crema ex.galb', 'crema ex.muse', 'crema vegetal', 'balsam buze', 'lips stick']),
    ('cosmetice', 'Samponuri', ['sampon', 'bebble sampon', 'bebble samp', 'bebble sapun']),
    ('cosmetice', 'Sapunuri', ['sapun']),
    ('cosmetice', 'Spumante & Geluri', ['gel dus', 'spumant', 'dus gel', 'cleanser']),
    ('cosmetice', 'Deodorante', ['deodorant', 'deo ', 'deo dove', 'deo ']),
    ('cosmetice', 'Demachiante', ['demachi', 'dischete', 'pepon-caps']),
    ('cosmetice', 'Hair Care', ['hair caps', 'my hair', 'ser stop', 'ser antirid', 'jutavit hair', 'cpr.de supt']),

    # CEAIURI
    ('ceaiuri', 'Ceai Digestiv', ['ceai digestiv', 'ceai gastric', 'ceai stomac', 'ceai curatare colon', 'ceai colon', 'ceai laxativ', 'ceai hepatic', 'ceai hepatocol', 'ceai hepatil', 'ceai crusin', 'ceai glicoocos', 'ceai glicocos']),
    ('ceaiuri', 'Ceai Relaxare', ['ceai tei', 'ceai valeri', 'ceai sun', 'ceai roini', 'ceai muguri', 'ceai somn', 'ceai salvie', 'ceai tensiune']),
    ('ceaiuri', 'Ceai Imunitate', ['ceai antirac', 'ceai antibro', 'ceai antist', 'ceai ghimb', 'ceai musete', 'ceai echinac', 'ceai verde', 'ceai cu frunze']),
    ('ceaiuri', 'Ceai Slabit', ['ceai sveltaflor', 'ceai siluet', 'ceai silue', 'ceai sveltaflor']),
    ('ceaiuri', 'Ceai Renal', ['ceai renal', 'ceai urzica', 'ceai diuros', 'ceai maciese']),
    ('ceaiuri', 'Ceai Respirator', ['ceai patlag', 'ceai plantus', 'ceai cimbri', 'ceai anghin']),
    ('ceaiuri', 'Ceai Prostata', ['ceai prostat', 'ceai pelin']),
    ('ceaiuri', 'Ceai Femei', ['ceai stimul', 'ceai laptelui', 'ceai lactat']),
    ('ceaiuri', 'Ceai Diverse', ['ceai ', 'ceai-']),

    # DEZINFECTANTI
    ('dezinfect', 'Alcool', ['alcool ', 'alcool-', 'alcool san', 'alcool bor', 'alcool camf', 'alcool iod', 'alcool mento', 'rivanol', 'albastru de metil']),
    ('dezinfect', 'Spray Dezinfect', ['septic', 'septice', 'decasept', 'spray antib', 'spray dezinf', 'spray antimic']),
    ('dezinfect', 'Solutii Dezinfect', ['iod', 'violet de gent', 'sol.coloidala', 'transderm g10', 'ranisept', 'rivanol']),

    # SUPLIMENTE GENERALE
    ('suplimente', 'Omega 3', ['omega', 'ulei de peste', 'ulei krill', 'fish oil']),
    ('suplimente', 'Coenzima Q10', ['coenzim', 'q10 ', 'q10-', 'q10mineral', 'q10 min', 'q10'], ),
    ('suplimente', 'Lecitina', ['lecitina', 'lecithin']),
    ('suplimente', 'Curcuma', ['curcum', 'kurkuma', 'turmeric']),
    ('suplimente', 'Ginseng', ['ginseng', 'ginko', 'ginkgo', 'panax']),
    ('suplimente', 'Royal Jelly', ['royal jelly', 'laptisor de matca']),
    ('suplimente', 'Spirulina', ['spirulina']),
    ('suplimente', 'Uleiuri Naturale', ['ulei de ', 'ulei catina', 'ulei argan', 'ulei levant', 'ulei parafina', 'ulei ricin', 'ulei salvie', 'uleiul ursului', 'ulei canabis', 'ulei cocos', 'ulei masline', 'virgin oil', 'ulei de dovlec', 'ulei jojob']),
    ('suplimente', 'Chia & Seminte', ['chia', 'seminte', 'seminte de dovleac']),
    ('suplimente', 'Siropuri', ['sirop ']),
    ('suplimente', 'Tincturi', ['tinctur']),
    ('suplimente', 'Articole Diverse', []),
]

# Category metadata (display name, icon, order)
categories_meta = {
    'vitamine':    {'name_ro': 'Vitamine',            'name_en': 'Vitamins',          'name_hu': 'Vitaminok',        'name_de': 'Vitamine',       'icon': 'fa-sun'},
    'minerale':    {'name_ro': 'Minerale',            'name_en': 'Minerals',          'name_hu': 'Asványok',        'name_de': 'Mineralien',     'icon': 'fa-gem'},
    'imunitate':   {'name_ro': 'Imunitate',           'name_en': 'Immunity',          'name_hu': 'Immunitás',       'name_de': 'Immunität',      'icon': 'fa-shield-virus'},
    'ceaiuri':     {'name_ro': 'Ceaiuri',             'name_en': 'Teas',              'name_hu': 'Teák',            'name_de': 'Tees',           'icon': 'fa-mug-hot'},
    'cosmetice':   {'name_ro': 'Cosmetice',           'name_en': 'Cosmetics',         'name_hu': 'Kozmetikumok',    'name_de': 'Kosmetik',       'icon': 'fa-leaf'},
    'digestie':    {'name_ro': 'Digestie',            'name_en': 'Digestion',         'name_hu': 'Emésztés',        'name_de': 'Verdauung',      'icon': 'fa-stomach'},
    'articulatii': {'name_ro': 'Articulatii',         'name_en': 'Joints',            'name_hu': 'Ízületek',        'name_de': 'Gelenke',        'icon': 'fa-bone'},
    'somn':        {'name_ro': 'Somn & Relaxare',     'name_en': 'Sleep & Relax',     'name_hu': 'Alvás & Relax',   'name_de': 'Schlaf',         'icon': 'fa-moon'},
    'copii':       {'name_ro': 'Copii & Bebelusi',    'name_en': 'Kids & Babies',     'name_hu': 'Gyermek',         'name_de': 'Kinder',         'icon': 'fa-baby'},
    'igiena_orala':{'name_ro': 'Igiena Orala',        'name_en': 'Oral Care',         'name_hu': 'Szájápolás',      'name_de': 'Mundpflege',     'icon': 'fa-tooth'},
    'intime':      {'name_ro': 'Intime',              'name_en': 'Intimate',          'name_hu': 'Intim',           'name_de': 'Intim',          'icon': 'fa-venus-mars'},
    'pansamente':  {'name_ro': 'Pansamente',          'name_en': 'Bandages',          'name_hu': 'Kötszerek',       'name_de': 'Verbände',       'icon': 'fa-bandage'},
    'aparatura':   {'name_ro': 'Aparatura Medicala',  'name_en': 'Medical Devices',   'name_hu': 'Orvosi Eszközök', 'name_de': 'Medizingeräte',  'icon': 'fa-stethoscope'},
    'ochi':        {'name_ro': 'Ochi & Vedere',       'name_en': 'Eyes & Vision',     'name_hu': 'Szem & Látás',    'name_de': 'Augen',          'icon': 'fa-eye'},
    'prostata':    {'name_ro': 'Prostata',            'name_en': 'Prostate',          'name_hu': 'Prosztata',       'name_de': 'Prostata',       'icon': 'fa-male'},
    'slabit':      {'name_ro': 'Slabit',              'name_en': 'Weight Loss',       'name_hu': 'Fogyás',          'name_de': 'Abnehmen',       'icon': 'fa-weight-scale'},
    'dezinfect':   {'name_ro': 'Dezinfectanti',       'name_en': 'Disinfectants',     'name_hu': 'Fertőtlenítők',   'name_de': 'Desinfektion',   'icon': 'fa-spray-can'},
    'suplimente':  {'name_ro': 'Suplimente',          'name_en': 'Supplements',       'name_hu': 'Táplálékkiegészítők','name_de': 'Ergänzungen', 'icon': 'fa-capsules'},
}

def categorize(product):
    name = product['name'].lower()
    brand = product.get('brand', '').lower()
    full = f"{brand} {name}"
    for rule in rules:
        cat, sub, keywords = rule
        for kw in keywords:
            if kw.lower() in full:
                return cat, sub
    return 'suplimente', 'Articole Diverse'

# Collect subcategories per category
cat_subcats = {}
for rule in rules:
    cat, sub, _ = rule
    cat_subcats.setdefault(cat, [])
    if sub not in cat_subcats[cat]:
        cat_subcats[cat].append(sub)

# Ensure every category has at least its subcategories registered
for cat in categories_meta:
    cat_subcats.setdefault(cat, [])

# Apply categories to products
for p in products:
    cat, sub = categorize(p)
    p['category'] = cat
    p['subcategory'] = sub

# Count
cat_counts = {}
subcat_counts = {}
for p in products:
    cat_counts[p['category']] = cat_counts.get(p['category'], 0) + 1
    key = (p['category'], p['subcategory'])
    subcat_counts[key] = subcat_counts.get(key, 0) + 1

print("=== Category counts ===")
for cat, meta in categories_meta.items():
    count = cat_counts.get(cat, 0)
    print(f"  {cat:12} ({meta['name_ro']:25}): {count}")

print("\n=== Subcategory counts ===")
for cat in categories_meta:
    print(f"\n[{cat.upper()} - {categories_meta[cat]['name_ro']}]")
    for sub in cat_subcats.get(cat, []):
        key = (cat, sub)
        print(f"  {sub:30}: {subcat_counts.get(key, 0)}")

# Write out new products.js
out_content = "window.allProducts = " + json.dumps(products, ensure_ascii=False, separators=(',', ':')) + ";\n\n"
out_content += "window.productCategories = " + json.dumps(categories_meta, ensure_ascii=False, indent=2) + ";\n\n"
out_content += "window.productSubcategories = " + json.dumps(cat_subcats, ensure_ascii=False, indent=2) + ";\n"

with open(r'D:\Jutavit\js\products.js', 'w', encoding='utf-8') as f:
    f.write(out_content)

print(f"\n\nTotal products: {len(products)}")
print(f"Total categories: {len(categories_meta)}")
print(f"Total subcategory groups: {sum(len(subs) for subs in cat_subcats.values())}")
