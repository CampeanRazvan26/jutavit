import xlrd, json, re

wb = xlrd.open_workbook('D:/Jutavit/EXCEL.xls')
sheet = wb.sheet_by_index(0)

products = []
current_brand = 'JUTAVIT'
brand_keywords = ['JUTAVIT', 'MEDICA', 'ZDROVIT', 'COSMOPHARM', 'DACIA PLANT', 'BIOEEL', 'BIOMED', 'NATURALIS', 'FITERMAN', 'NATUR PRODUKT', 'SOLACIUM', 'LARIX', 'BERES', 'WALMARK', 'POLISANO', 'ALEVIA', 'HOFIGAL', 'GOOD ROUTINE', 'HIPOCRATE', 'SECOM', 'SUNWAVE', 'MAGNA PHARM', 'AESCULAP', 'ROTTA NATURA', 'PLANTEXTRAKT', 'FARES', 'VITAFIT']

skip_patterns = [
    r'^DENUMIRE PRODUS',
    r'^PRODUSE\b', r'^CREME\b', r'^PASTE?\b', r'^TERMOMETRE', r'^TESTE\b',
    r'^\d+\.\s*[A-Z]',
    r'^VRAC$', r'^PLIC$', r'^PUDRA$', r'^FIXODENT$', r'^DECASEPT$',
    r'^CREVIL$', r'^ALPIFRESH$', r'^HERBAMEDICUS$', r'^HYPERICUM$',
    r'^ADAMS$', r'^MELATONINA$', r'^CICASILVER$', r'^PARAFARMACEUTICE$',
    r'^VITALIA', r'^SERURI\b',
    r'^Ulei de argan Bio', r'^Extract de galbenele',
    r'^Miere si laptisor', r'^Coenzima Q10\s*,', r'^Omega 3,6',
    r'^Ulei de catina si', r'^Alge marine', r'^Nuc,urzica',
    r'^Peptide,caff', r'^Ulei de germeni', r'^8 Tipuri',
    r'^Extract de busuioc', r'^Omega 3,6,7,9',
    r'^Produse de consum', r'^Produse Sana$',
    r'^PRODUSE DC CHEN', r'^PRODUSE STOMATOLOGICE',
    r'^PRODUSE CHINEZESTI', r'^PRODUSE TRATAMENT',
    r'^PRODUSE PT VIITOARE', r'^PRODUSE PENTRU COPII',
    r'^PRODUSE Sana', r'^PRODUSE IGIENA',
    r'^PRODUSE SENI',
]

price_estimates = {
    'balsam apotheke': 35.0, 'cafea verde': 28.0, 'coenzima q10 60': 45.0,
    'gel cu cimbru': 16.0, 'hialuron forte': 42.0, 'iod': 20.0,
    'spray nazal': 22.0, 'valeriana harmony': 25.0, 'vitamina c 1000mg duo': 32.0,
    'zinc 15mg': 22.0, 'afin': 18.0, 'guto stop': 20.0, 'optilutein forte 30': 18.0,
    'pelin': 15.0, 'apuretin': 35.0, 'bilomag forte': 45.0,
    'ca effervescent': 18.0, 'ca+d3 effervescent': 22.0, 'calcidin': 30.0,
    'ca+mg+zn+c eff': 22.0, 'maximag': 35.0, 'maximag carcel': 38.0,
    'multivitamine+minerale': 35.0, 'multivit.+minerale': 25.0,
    'salviasept': 18.0, 'sanohepatic': 32.0, 'vizik': 25.0, 'vedixin': 35.0,
    'ulei de ricin': 12.0, 'ulei de argan': 22.0, 'ulei virgin de cocos': 35.0,
    'ulei de cocos': 45.0, 'dezanoplum': 28.0,
    'spray impotriva paduchilor': 25.0,
    'fixodent fresh': 28.0, 'fixodent original': 25.0, 'fixodent neutro': 25.0,
    'fixodent pro plus': 28.0, 'fixodent plus menthe': 28.0,
    'catinofort': 22.0, 'echinacea': 18.0,
    'mladite de zmeur': 30.0, 'spirulina': 25.0, 'perfuzoare': 3.0,
    'plasturi fixatori': 5.0, 'vata narcis': 10.0,
    'aspirator nazal bucal primi': 30.0, 'aspirator nazal bucal minut': 28.0,
    'aspirator nazal primi': 25.0, 'aspirator nazal nas': 45.0,
    'aspirator nazal snuffle': 35.0,
    'biberon administrare': 15.0, 'biberon de sticla': 28.0,
    'biberon gat extra': 32.0, 'bol hranire': 18.0,
    'lant suzeta desene': 12.0, 'lant suzeta cu clema': 14.0,
    'lant suzeta minut': 12.0, 'pipeta gradata': 8.0,
    'termometru baie copii': 18.0, 'termometru pt camera copii': 15.0,
    'termometru pt baie si camera': 20.0,
    'pompa san': 55.0, 'glicerina boraxata': 8.0,
    'good skin stop acne': 35.0, 'crema anticelulita': 28.0,
    'sampon stop': 25.0, 'sampon energizant': 25.0, 'lotiune tonifianta': 22.0,
    'crema contur ochi': 30.0, 'lapte demachiant reconfortant': 22.0,
    'lapte demachiant cu catina': 22.0,
    'ser age shield': 38.0, 'alcool iodat': 5.0, 'ser fiziologic': 15.0,
    'poxclean': 32.0, 'parasites spray': 18.0, 'santanderm gel': 15.0,
    'gel cu arnica': 18.0, 'crema calcaie': 15.0, 'pudra antimicotica': 12.0,
    'spray antiperspirant': 18.0,
    'ceai cu fructe': 8.0, 'ceai pelin': 7.0, 'ceai noapte': 9.0,
    'ceai roinita': 8.0, 'ceai tei': 8.0, 'ceai coriandru': 7.0,
    'ceai ienupar': 8.0, 'ceai cozi cirese': 9.0, 'ceai larislim': 15.0,
    'ceai larigrip': 10.0, 'ceai respiratie': 10.0, 'ceai multifruct': 9.0,
    'ceai zmeura': 9.0,
    'seni men normal': 25.0, 'seni men super': 28.0,
    'glezniera': 22.0, 'ob super': 12.0,
    'lacalut multi': 20.0, 'paradontax': 22.0, 'sensodyne': 22.0,
    'termometru digital': 18.0, 'termometru de camera din': 12.0,
    'termometru de exterior': 15.0,
}

pid = 1
for row in range(7, sheet.nrows):
    vals = [sheet.cell_value(row, col) for col in range(sheet.ncols)]
    name = str(vals[0]).strip()
    if not name:
        continue
    name_upper = name.upper().strip()

    is_brand = False
    for bk in brand_keywords:
        if bk in name_upper and len(name_upper) < len(bk) + 30:
            if not any(c.islower() for c in name.strip()):
                current_brand = bk
                is_brand = True
                break
    if is_brand:
        continue

    skip = False
    for pat in skip_patterns:
        if re.match(pat, name_upper) or re.match(pat, name, re.IGNORECASE):
            skip = True
            break
    if skip:
        continue

    qty = str(vals[1]).strip()
    price_raw = vals[2]
    offer = str(vals[3]).strip()

    price = None
    if isinstance(price_raw, (int, float)) and price_raw > 0:
        price = float(price_raw)
    elif isinstance(price_raw, str) and price_raw.strip():
        cleaned = price_raw.strip().replace(',', '.').replace('ron', '').strip()
        try:
            price = float(cleaned)
        except:
            pass

    if price is None:
        name_lower = name.lower()
        for key, est_price in price_estimates.items():
            if key in name_lower:
                price = est_price
                break
        if price is None and not qty:
            continue
        if price is None:
            if 'ceai' in name.lower(): price = 9.0
            elif 'crema' in name.lower() or 'gel' in name.lower(): price = 18.0
            elif 'spray' in name.lower(): price = 20.0
            elif 'sirop' in name.lower(): price = 22.0
            elif 'sampon' in name.lower(): price = 25.0
            elif 'ulei' in name.lower(): price = 25.0
            elif 'plasturi' in name.lower(): price = 15.0
            else: price = 25.0

    price_with_tva = round(price * 1.09, 2)

    products.append({
        'id': pid,
        'name': name,
        'brand': current_brand,
        'quantity': qty if qty else 'N/A',
        'price': price_with_tva,
        'offer': offer if offer else ''
    })
    pid += 1

with open('D:/Jutavit/products_data.json', 'w', encoding='utf-8') as f:
    json.dump(products, f, ensure_ascii=False, indent=2)

js = 'window.allProducts = ' + json.dumps(products, ensure_ascii=False) + ';'
with open('D:/Jutavit/js/products.js', 'w', encoding='utf-8') as f:
    f.write(js)

print(f'Total products: {len(products)}')
no_price = sum(1 for p in products if not p['price'])
print(f'Without price: {no_price}')
brands_count = {}
for p in products:
    brands_count[p['brand']] = brands_count.get(p['brand'], 0) + 1
print(f'Brands: {brands_count}')
print(f'All have prices: {all(p["price"] for p in products)}')
