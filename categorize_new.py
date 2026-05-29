# -*- coding: utf-8 -*-
"""Categorize new products using rules from categorize_products.py logic."""
import json

with open(r'D:\Jutavit\new_products.json', encoding='utf-8') as f:
    new_products = json.load(f)

# Same rules as before — first match wins
RULES = [
    # category, subcategory, keywords (lower)
    ('intime', 'Prezervative', ['durex', 'condom', 'prezervativ']),
    ('intime', 'Teste Sarcina', ['test sarcina', 'sarcina', 'sarcina-', 'sarcina*']),
    ('intime', 'Teste Rapide', ['test rapid', 'test antigen', 'test menopauza', 'test ovulatie', 'test veneris', 'test rapid streptococ', 'test rapid alergii', 'test rapid boala', 'test rapid afectiuni', 'test rapid vitamina', 'test rapid depistare']),
    ('intime', 'Absorbante', ['absorbante', 'always', 'libresse', 'discreet']),
    ('intime', 'Igiena Intima', ['igiena intima', 'lubrifiant', 'gel igiena', 'gel intima', 'servetele intime']),
    ('copii', 'Scutece', ['scutec', 'pampers', 'seni soft super', 'seni soft normal', 'seni soft 90', 'seni man super', 'seni activ', 'seni active', 'seni basic', 'seni clasic', 'seni extra large', 'seni large', 'seni medium', 'seni lady']),
    ('copii', 'Biberoane', ['biberon', 'mixer biberon']),
    ('copii', 'Suzete', ['suzeta', 'suzete']),
    ('copii', 'Tetine', ['tetina']),
    ('copii', 'Servetele Umede', ['servetele umede copii', 'servetele copii', 'serv.umede']),
    ('copii', 'Igiena Copii', ['baby', 'kids', 'bebe', 'bebble', 'bebelus', 'copii', 'junior', 'pediform', 'dalin', 'baita', 'mami&bebe', 'caola', 'molekin']),
    ('copii', 'Accesorii Bebe', ['lantisor', 'inel dentitie', 'lingurita', 'cana cu maner', 'cana cu pai', 'set hranire', 'set linguri', 'set perie', 'forfecuta', 'unghiera', 'matrita', 'cantar bebe', 'cliseu digital eticheta']),
    ('imunitate', 'Propolis', ['propolis']),
    ('imunitate', 'Echinacea', ['echinacea', 'echinac']),
    ('imunitate', 'Raceala & Gripa', ['gripa', 'racela', 'raceala', 'hapciu', 'gripovit', 'herbal hot', 'halls']),
    ('imunitate', 'Suplimente Imunitate', ['imuno', 'imunitate']),
    ('digestie', 'Probiotice', ['probiotic', 'probium']),
    ('digestie', 'Enzime Digestive', ['enzime', 'enzima', 'digestive enzyme', 'lactaz']),
    ('digestie', 'Stomac', ['stomac', 'pelin', 'menthol', 'mentholin', 'maciese', 'gastric', 'gastr', 'fitodiab', 'diab control']),
    ('digestie', 'Laxative', ['laxativ', 'laxaclean', 'crusin', 'rectostop', 'senna', 'supozitor']),
    ('digestie', 'Ficat', ['ficat', 'silimarin', 'milk thisle', 'milk thistle', 'armurariu', 'anghinar', 'hepato', 'hepatic', 'colina', 'colin ']),
    ('digestie', 'Curatare Colon', ['colon', 'curatare colon']),
    ('digestie', 'Antibalonare', ['biomicin']),
    ('digestie', 'Antidiareice', ['carbovita', 'carbune medic']),
    ('digestie', 'Antiparazitar', ['giardinofug', 'vermicin', 'antiparazitar', 'antiparait']),
    ('digestie', 'Acidoza', ['saruri rehidratare', 'litorsal', 'electroliti']),
    ('articulatii', 'Colagen', ['collagen', 'colagen', 'collagen complex', 'col.agen']),
    ('articulatii', 'Glucozamina', ['glucozam', 'glucosam', 'condroitin']),
    ('articulatii', 'Calciu D3', ['calciu d3', 'calciu+d3', 'calciu &d3', 'calcimax']),
    ('articulatii', 'Balsamuri', ['balsam ', 'ghiara dracului', 'gheara dracului', 'gheara draculuui', 'tataneasa', 'puterea calului', 'puterea ursului', 'forta ursului', 'arnica', 'arnika', 'crevil', 'schmees', 'herbamedicus']),
    ('somn', 'Melatonina', ['melatonin']),
    ('somn', 'Valeriana', ['valeriana']),
    ('somn', 'Antistres', ['antistres', 'somn limistit', 'noapte buna', 'optisomn', 'relaxirem', 'roinita']),
    ('igiena_orala', 'Paste Dinti', ['pasta de dinti', 'pasta dinti', 'pd.colgate', 'pd colgate', 'oral-b pasta', 'lacalut aktiv', 'kin pasta']),
    ('igiena_orala', 'Periute Dinti', ['periuta', 'periute', 'peri de dinti', 'perii dinti']),
    ('igiena_orala', 'Apa Gura', ['apa de gura', 'apa gura', 'listerin', 'lacalut sensitive', 'lacalut sensitiv', 'kin apa']),
    ('igiena_orala', 'Alte Orale', ['ata interdentara', 'betisoare cu ata', 'kin gel', 'kin oro', 'sensodyne', 'gel gingival', 'mobilin']),
    ('pansamente', 'Plasturi', ['plaster', 'plasture', 'plasturi', 'plast.', 'leucoplast', 'qplaster', 'qplast', 'transderm', 'sanitaband', 'sanytayaki', 'compresa']),
    ('pansamente', 'Fese & Bandaje', ['bandaj', 'fasa', 'fasa', 'fesi', 'fese', 'tifon', 'compres', 'banda adeziva']),
    ('pansamente', 'Vata', ['vata med', 'vata ', 'tampoane pt', 'tampoane cu', 'tampoane pentru', 'tamp.', 'tamp ']),
    ('pansamente', 'Genunchiera', ['genunchier', 'cotiera', 'glezniera', 'manseta', 'centura spate', 'burtiera', 'sana bandaj']),
    ('aparatura', 'Tensiometre', ['tensiometru', 'tensio']),
    ('aparatura', 'Termometre', ['termometru', 'termometre', 'thermax']),
    ('aparatura', 'Glucometre', ['glucometru', 'glucometre', 'kit glucometru']),
    ('aparatura', 'Nebulizatoare', ['nebulizator', 'nazomer']),
    ('aparatura', 'Pulsoximetre', ['pulsoximetru', 'pulsoxim']),
    ('aparatura', 'Inhalatoare', ['inhalator', 'inhalat']),
    ('aparatura', 'Aspiratoare Nazale', ['aspirator nazal', 'aspirator nasal', 'nosko']),
    ('aparatura', 'Irigatoare', ['irigator', 'irigatoare', 'pompa lapte', 'pompa san', 'pompa piriforma', 'pompa nimo', 'instalatori sticla']),
    ('cosmetice', 'Creme Fata', ['crema contur', 'crema antirid', 'crema hidratanta', 'crema antiacnee', 'crema vit', 'crema cu vit', 'crema panthenol', 'crema albir', 'crema gel', 'crema maini', 'crema noapte', 'crema regener', 'crema restruct', 'crema z', 'crema ', 'cr.anticelul', 'cr.pt.depig', 'cr.reparat', 'cicasilver', 'bakuchiol', 'ser antirid']),
    ('cosmetice', 'Creme Corp', ['crema corp', 'lotiune corp', 'crema plaja', 'omega plus', 'emulsie plaja']),
    ('cosmetice', 'Samponuri', ['sampon', 'samp.gel']),
    ('cosmetice', 'Sapunuri', ['sapun', 'soliteint dermax']),
    ('cosmetice', 'Demachiante', ['demachi', 'dischete', 'lapte demach']),
    ('cosmetice', 'Hair Care', ['my hair', 'dalin spray', 'lotiune tonifianta par', 'sampon par', 'jutavit hair']),
    ('cosmetice', 'Buze', ['balsam buze', 'lips stick', 'creion pt.rani']),
    ('cosmetice', 'Anti-celulita', ['anticelul', 'anti-celul']),
    ('cosmetice', 'Deodorante', ['deo dove', 'deodorant']),
    ('cosmetice', 'Make Up', ['soliteint fond', 'fond de ten']),
    ('cosmetice', 'Anti-tantari', ['tantari', 'tantar', 'capuse', 'parasit', 'paduchi', 'antitantari', 'antiparait', 'bratara antit', 'bratara aromatic', 'bratara aromat', 'spray repelent', 'spray protectiv', 'stiker antitantar', 'antiherp', 'zgarda impotr']),
    ('cosmetice', 'Epilare', ['depil ', 'mini benzi cu ceara']),
    ('cosmetice', 'Picioare', ['parasoftin', 'spray de picioare', 'spray de pantofi', 'lotiune picioare', 'gel picioare', 'lot. pt. picioare', 'sosete', 'acoperitor pantofi', 'crema pt ingrijirea calc']),
    ('cosmetice', 'Anti-Aging', ['good skin', 'anti-ageing', 'cica ', 'cica-', 'creion nazal']),
    ('vitamine', 'Vitamina C', ['vit.c', 'vit c', 'vitamina c', 'vit c ', 'vit. c', 'maciese', 'acerola', 'vitamin c plus']),
    ('vitamine', 'Vitamina D', ['vit.d', 'vit d', 'vitamina d', 'vit.d3', 'd3', 'vit d3', 'detrical', 'd-mandoza']),
    ('vitamine', 'Vitamina B', ['vit.b', 'vit b', 'vitamina b', 'b complex', 'biotina', 'biotin']),
    ('vitamine', 'Vitamina A&E', ['vit a', 'vit.a', 'vitamina a', 'vit e', 'vit.e', 'vitamina e']),
    ('vitamine', 'Vitamina K', ['vit k', 'vit.k', 'k2 ', 'natural k2', 'vitamina k']),
    ('vitamine', 'Multivitamine', ['multiv', 'multivit']),
    ('vitamine', 'Vitamine Efervescente', ['efervescent', 'eff']),
    ('minerale', 'Magneziu', ['magneziu', 'maximag', 'kidimag', 'bisglicinat']),
    ('minerale', 'Calciu', ['calciu', 'calcium', 'fluorkin']),
    ('minerale', 'Zinc', ['zinc']),
    ('minerale', 'Fier', ['fier ', 'fier organic']),
    ('minerale', 'Seleniu', ['seleniu']),
    ('minerale', 'Crom', ['crom ', 'crom organic']),
    ('minerale', 'Iod', ['iod ', 'tinctura de iod']),
    ('minerale', 'Alte Minerale', ['mineral', 'royal jelly']),
    ('ceaiuri', 'Ceai Digestiv', ['ceai digestiv', 'ceai gastric', 'ceai digestie']),
    ('ceaiuri', 'Ceai Relaxare', ['ceai antistres', 'ceai relaxare', 'ceai roinita', 'ceai somn']),
    ('ceaiuri', 'Ceai Imunitate', ['ceai musetel', 'ceai antiviral', 'ceai imunit', 'ceai vasc', 'ceai macies']),
    ('ceaiuri', 'Ceai Slabit', ['ceai antiadipos', 'ceai silueta', 'ceai svelta', 'ceai sveltaflor']),
    ('ceaiuri', 'Ceai Renal', ['ceai renal', 'ceai diur', 'ceai pufulita', 'ceai cretisoara']),
    ('ceaiuri', 'Ceai Respirator', ['ceai antibronsit', 'ceai plantusin', 'ceai patlagina', 'ceai trei frati', 'ceai galbenele', 'ceai sunatoare']),
    ('ceaiuri', 'Ceai Prostata', ['ceai prostat']),
    ('ceaiuri', 'Ceai Femei', ['ceai stimularea', 'ceai lactati']),
    ('ceaiuri', 'Ceai Diverse', ['ceai ', 'ceai-']),
    ('ochi', 'Suplimente Ochi', ['lutein', 'optolutein', 'opti ', 'optisomn', 'afin ', 'afin*', 'afine ']),
    ('ochi', 'Picaturi Ochi', ['picaturi de ochi', 'pic.de ochi', 'pic ochi', 'pic.ochi', 'vizik allergy']),
    ('ochi', 'Ochelari Citit', ['ochelari de citit', 'ochelari citit']),
    ('prostata', 'Suplimente Prostata', ['prosta', 'prostat', 'capsula prostay', 'maraton']),
    ('slabit', 'Slim Produse', ['slim ', 'slim-', 'slabit', 'slabofit', 'slim lady']),
    ('slabit', 'Glucomannan', ['glucomannan', 'glucoman']),
    ('slabit', 'Cafea Verde', ['cafea verde', 'green coffee']),
    ('slabit', 'Apuretin', ['apuretin', 'lipostop']),
    ('dezinfect', 'Alcool', ['alcool', 'alcol', 'alcool sanitar', 'alcool boricat', 'alcool camforat', 'alcool iodat', 'alcool mentolat', 'alcol sanitar', 'septiclean']),
    ('dezinfect', 'Spray Dezinfect', ['spray antibacterian', 'decasept spray', 'spray antimicotic']),
    ('dezinfect', 'Solutii Dezinfect', ['rivanol', 'apa oxigenata', 'glicerina boraxata', 'decasept', 'biosept']),
    ('suplimente', 'Omega 3', ['omega 3', 'omega3', 'ulei de peste', 'ulei krill', 'omega-3', 'fish oil']),
    ('suplimente', 'Coenzima Q10', ['coenzima', 'q10']),
    ('suplimente', 'Lecitina', ['lecitin']),
    ('suplimente', 'Curcuma', ['curcuma', 'kurkuma', 'curcumin']),
    ('suplimente', 'Ginseng', ['ginseng', 'panax']),
    ('suplimente', 'Royal Jelly', ['royal jelly', 'laptisor matca', 'laptisor de matca']),
    ('suplimente', 'Spirulina', ['spirulina']),
    ('suplimente', 'Uleiuri Naturale', ['ulei de argan', 'ulei de levantica', 'ulei de masaj', 'ulei de parafina', 'ulei de ricin', 'ulei de salvie', 'ulei canabis', 'ulei catina', 'ulei esential', 'ulei de dovleac', 'ulei krill']),
    ('suplimente', 'Chia & Seminte', ['chia', 'seminte', 'fructe de goji']),
    ('suplimente', 'Siropuri', ['sirop ', 'sirop-', 'sirop,', 'jb oils']),
    ('suplimente', 'Tincturi', ['tinctura', 'frectie']),
    ('suplimente', 'Articole Diverse', []),  # fallback
]

def categorize(name):
    n = name.lower()
    for cat, sub, kws in RULES:
        for kw in kws:
            if kw and kw in n:
                return cat, sub
    return 'suplimente', 'Articole Diverse'

for p in new_products:
    cat, sub = categorize(p['name'])
    p['category'] = cat
    p['subcategory'] = sub

with open(r'D:\Jutavit\new_products_categorized.json', 'w', encoding='utf-8') as f:
    json.dump(new_products, f, ensure_ascii=False, indent=1)

# stats
from collections import Counter
cats = Counter(p['category'] for p in new_products)
print('=== Category counts ===')
for k, v in sorted(cats.items(), key=lambda x: -x[1]):
    print(f'  {k:14}: {v}')
print(f'\nTotal categorized: {len(new_products)}')
