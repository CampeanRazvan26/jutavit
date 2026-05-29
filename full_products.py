# -*- coding: utf-8 -*-
"""
Complete product extraction from all 19 WhatsApp photos in D:\\Jutavit\\produse.
Each entry: (name, price_cu_TVA). Brand inferred from name keywords.
Prices in RON. Quantity from text where present.
"""

# All products extracted from the 19 photos. Format: "name|price_with_VAT"
RAW = """
9 vita 100drj|26.02
ALCOL SANITAR X500ML ROAPOTECA|5.75
ALCOOL BORICAT 4% 20 GR|6.17
Bandaj autoadeziv elastic 10cm x4.5m|9.80
Bandaj autoadeziv elastic 15cm x4.5m|15.73
Bandaj autoadeziv elastic 2,5 x4.5m|3.87
Bandaj autoadeziv elastic 5cm x4.5m|6.66
Bandaj autoadeziv elastic 7,5cm x4.5m|8.47
CALCIU+D3 50 compr|0.00
CALCIU+D3 50 comprimate|35.70
CALCIU+MG+ZN+vit.C-50 compr zdrovit|42.35
CALCIU,MAG,ZN,C x50cpr zdrovit|0.01
CAPSULA PROSTAYoL k 023|50.82
CARBOVITA S001|10.41
CEAI PROSTATA-DOZE fares|9.99
CEAI VERDE CPS 30cps 1+1 fmn|23.60
CREMA ARNICA LARIX 40 gr|10.29
CREMA SUNATOARE LARIX 40 gr|6.17
CREVIL VITAL GEL PUTEREA CALULUI+CANNABIS 250 ml|18.15
Ceai anason|5.55
Ceai hapciu-antiraceala|8.33
Crema catina 40 gr -larix|8.23
Detrical D3 2000 IU*60cpr|45.98
Dischete demachiante 70/pac|4.72
GEL MASAJ bingo 500 ml|22.02
GRIPOVIT JUNIOR 10plicuri|43.56
INDULCITOR-erythriol+xylitol+stevia 250 gr|17.76
INSTALATORI STICLA CU POMPA CAUCIUC|1.33
JB baby lotion 300 ml|15.73
JB oils -regular 300 ml|16.34
JUTAVIT B COMPLEX+ACID FOLIC 100 BUC/CUTIE|23.96
Jutavit Magneziu eff 275mg 16tb|19.97
Jutavit extract de curcuma 60 caps|33.88
Jutavit lecitin pro 1200mg 30 buc|22.99
Jutavit prostalong 320mg 60 buc/cut|46.59
Jutavit scortisoara+crom+ghimbir+marar 120 tb|36.91
Jutavit vit.C 1000mg efervescenta 20/cut|20.33
Jutavit vit.C 200mg -gust portocale 100 b|31.46
Jutavit vit.C 500mg +d3+zn+ex.maciese-100tb|35.70
Jutavit vit.C 500mg -masticabil +d3 si ex.maciese-100tb|34.49
Jutavit vit.C+maciese+ex.acerola 1500ml/100tb|53.85
Jutavit vit.D3 3000 ne 100 capsule|37.51
Jutavit vit.D3 4000 ne cu ulei de masline|41.02
KIN PERIUTA DE DINTI MEDIUM|0.00
KIT GLUCOMETRU DR LIFE 2cutii teste 2 cutii ace 1 glucometru|52.64
Kidimag 3ani+ magneziu ionic 20 plicuri|39.32
Kit pentru indepartarea capuselor de life|18.15
LiSTERIN-apa de gura 500ml spermint|18.15
LiSTERIN-apa de gura 500ml mild minty|18.15
MARATON 4 pt cresterea potentei|72.60
MARATON FOTRE 20 pt cresterea potentei|290.40
MY HAIR ser stop cadere|30.86
MY HAIR no grei- ser stop incaruntire|28.44
MY HAIR strong- ser stop despicare|23.65
MY HAIR clean-ser stop matreata|33.88
Mini irigator medo|6.29
NEGRO-classic 79gr|7.02
NEGRO-extra 79 grame|7.02
NEGRO-mentol 79 gr|7.02
NEGRO-miere 79 grame|7.02
NOAPTE BUNA 30 CPS|35.52
PD.colgate max white cristal 100 ml|8.35
PROSTAGOOD ON 30 CPS*625MG|62.92
PROSTAGOOD on 60comp 625mg|102.85
PROSTAGOOD FORTE 30 comp 1520mg|89.54
PROSTAGOOD 30 comp 1520mg|25.41
Plosca medicala|18.15
SENI SOFT super 90 X60 A-5|75.61
SENI SOFT 90/60A 30 BUC|56.87
SENI SOFT NORMAL 60/60 *30|108.78
SENI SOFT SUPER 90/170 30 BUC|15.97
SENSODYNE-BLANCHEUR 75 ML|15.97
SENSODYNE-complet protection 75 ML|23.60
SIROP TUSE 100-ML Vitalia|212.36
SN biocrema arnica ice cu efect rece,dozator 500 ml|141.57
SN biocrema arnica ice cu efect rece 250 ml|62.92
SN biocrema arnica ice cu efect rece flacon airless*100 ml|181.50
SN gel arnica extra cu glucozamina,boswellia si gh diavolului*500ml|180.90
SN biogel arnica 99% 500 ml|62.92
SN biogel calendula 90 % flacon airless*100 ml|102.85
SN biounguent rxtract de salvie de melc 50% flacon airless*75 ml|13.61
SOLITEINT DERMAX SAPUN LICHID 300 ML|9.67
SOLITEINT FOND DE TEN NR 2 BEIGE 30 ml|9.67
SOLITEINT FOND DE TEN NR 4 NOON 30 ml|9.67
SOLITEINT FOND DE TEN NR 5 HONEY 30 ml|76.23
STOP TICK SET|43.12
Seni care crema curatare corp 3 in 1 1000ml|35.09
Spray cu d-panthenol 5% santaderm 100 ml|24.08
Spray pentru gat septiclean-20 ml|360.58
TERMOMETRU CU INFRAROSU|6.66
TETINA SILICON gat larg bt104 nr 1 +18 luni|6.05
TETINA SILICON anatomica anticolica bt099 nr 1 0-6 luni|41.14
Test rapid proteina C reactiva|47.19
Test rapid Strip A|58.08
Test rapid intoleranta gluten|83.49
Wortie sprai-50 ml contra negilor|24.20
acnesol-lotiune antiacneica 60|0.11
acoperitor pantofi 100|17.54
afin 60 cps medica|3.99
alcol sanitar Mona 200 ML 70%|19.97
alifie cu galbenele alpifresch-250|16.65
antistres FORTE cps 60cps|11.86
apa de mare izotona septimar baby-30 ml|19.97
apa micelara 300 ml vitamin C PLUS|14.52
apa oxigenata 3% 1000ml|4.60
apa oxigenata 3% 200 ml|6.90
apa oxigenata 3% cu pulverizator 200g|16.34
apasator limba lemn steril 100 buc|66.55
apuretin SLIM*60cps zdrovit|9.56
aspirator nazal MEDDO|11.25
aspirator nazal minut|9.68
aspirator nazal-34005 bt185|15.73
aspirator nazal-asp.bucala minut|53.85
bakuchiol anti-ageing elixir-serum|52.64
bakuchiol hydra&firming cream|55.66
bakuchiol wrinkle repair cream|6.66
balsam 27 ml|8.11
balsam buze cu ulei de jojoba 5.5 ml vegan|8.47
balsam buze cu acid hialuronic 5.5 ml vegan|8.23
balsam buze cu vit e spf-30|0.73
balsam china 3 G|7.26
balsam china 18 g|6.05
balsam cu ex de musetel|6.05
balsam cu extract galg+propolis|8.59
balsam cu galbenele 30 ml|7.14
bandaj elastic autoadeziv MINUT 10CM*4.5M neutru|9.07
bandaj elastic autoadeziv MINUT 7.5cm*4.5m|7.50
batista bebelusului|32.97
batiste FINE LIFE 10/SET|5.69
bavete copii 2|0.02
bazna relax gel 150 ml|12.74
bebble crema pt fundulet rosu 60 ml|25.41
bebble gel gingival 20 ml|28.44
bebble sampon si gel de dus pentru corp musetel si tei 400 ml|20.81
bebble sampon si gel pentru baita 2 in 1 200 ml|15.13
bebble sampon si gel pentru baita 2 in 1 400 ml|25.41
bebble sapun crema cu lavanda 75 gr|6.29
bebble sapun crema cu musetel 75 gr|6.29
bebble ulei pentru corp 150 ml|17.91
bella tampo mini*16|11.62
bella tampo regular*16|11.62
benzi curatate pori nas cu carbune 6 buc|13.31
benzi de nas cu extract de arbore de ceai 6 buc|13.92
benzi natale respiri usor 10 buc|11.62
betisoare cu ata interdentara cu carbune|9.07
betisoare urechi copii minut 55/cut|3.99
betisoare urechi cutie de soleil-100 buc|2.66
betisoare urechi cutie*200 dr soleil|4.60
biberon sticla borosilicat 250ml 3+ minut|16.34
biberon 125cu maner minut|13.07
biberon 125ml simplu minut|9.92
biberon 250cu maner minut|15.49
biberon 250ml simplu minut|11.62
biberon borosilicat 125 ml minut|13.92
biberon cu maner 125 ml|10.65
biberon cu maner 250 ml|10.77
biberon cutie 250 ml tr101-02|10.89
biberon gat larg,tetina,manere 150ml 0+|14.52
biberon gat larg,tetina,manere 270ml 3+|15.73
biberon pp cu maner BT 070 150 ML|14.28
biberon pp cu maner BT069 250 ml|15.25
biberon pp cu maner BT065 250 ml|11.13
biberon ppcu tetina silicon 250 ml|10.77
bicarbonat de sodiu 50 gr|2.54
bingo gel 500ml pic,grele,vene si varice|22.02
biomicin forte cps|38.85
biomicin urinar cps moi|37.74
bisglicinat de magneziu 1000mg 3bls x 10cpr film|42.35
bitter 'Taina Plantelor , 200 ml -cu balsam taina plantelor|38.12
bitter 'Taina Plantelor , fara alcool|50.82
boneta antipaduchi 2 buc-multicare|0.15
boneta medicala cu elastic u.f.|3.51
bratara antitantari|15.13
bratara aromatica piele -2 buc|15.73
bratara aromatica silicon *2 rez|7.20
bratara aromatizata minut -roz|7.20
bratara aromatizata minut -verde|16.34
cana cu maner si cioc silicon 6+ 300ml min2019026|19.97
cana cu pai si manere 210 ml min2018006 6+|10.29
cana decorata cu manere,cioc rabatabil|163.35
cantar electronic bebelusi king2510805|68.97
caps.PROBICUM 7FORTE 60buc|60.50
caps.KURKUMA KOLLAGEN FORTE K144|62.92
capsula ceai virgin forte 80 caps|30.25
capsule cu usturoi-paducel+vasc 30cps 1+1 gratis|6.77
ceai earl grey suprapilc|0.00
ceai Hepatil-af hepato-bil. LARIX|8.88
ceai Laxativ L|8.47
ceai MIX 6sortimente sprapilc|14.99
ceai afine frunze larix|7.26
ceai anghinare|5.93
ceai antiadipos Yong Kang|12.15
ceai antiadipos cu ginseng|7.02
ceai antiadipos sanye|9.68
ceai antiadipos strong|6.78
ceai antibronsitic doze|7.33
ceai antistres-FARES af.minore|10.16
ceai armurariu|5.02
ceai babycalm-doze|7.44
ceai chimion|5.88
ceai cimbrisor|5.33
ceai coada calului larix|5.32
ceai coada calului-doze LARIX|4.60
ceai coada soricelului|5.32
ceai coada soricelului doze|4.72
ceai colesterol doze|10.55
ceai colon sanatos punga fares|15.43
ceai cozi cirese DOZE-larix|5.57
ceai cozi de cirese|6.53
ceai cretisoara pg 50gr|10.53
ceai crusin doze|4.60
ceai crusin vrac-larix|5.08
ceai cu afine-doze fares|5.44
ceai cu fructe de padure fares|11.13
ceai curatare colon doze -fares|7.22
ceai de iarna fares|8.33
ceai digestie usoara 20 pl'|8.83
ceai digestiv doze -larix|11.66
ceai diurosept-doze fares|5.45
ceai fenicul|11.98
ceai fructe de catina|4.77
ceai fructe de padure doze|6.88
ceai fructe de padure suprapilc|6.17
ceai galbenele Larix|4.60
ceai galbenele doze LARIX|10.43
ceai gastric doze FARES|8.33
ceai ghimbir cu lamaie larix|4.77
ceai ghimbir vrac hypericum|17.30
ceai ghimpe|4.11
ceai glicostat-doze fares|9.25
ceai hepatocol doze fares|8.71
ceai larediab DOZE|8.88
ceai larediab vrac|7.66
ceai laricol contra colici copii|4.90
ceai laxativ-doze larix|9.77
ceai laxativ-doze larix b|8.88
ceai maciese|4.84
ceai maciese - 75 gr|7.14
ceai mar-scortisoara larix|6.99
ceai matase de porumb-FARES DOZE|7.26
ceai menta|4.60
ceai menta suprapilc|6.90
ceai menta vrac|5.69
ceai momordica-vrac hypericum|11.66
ceai muguri de pin larix|2.78
ceai musetel|4.60
ceai musetel vrac-LARIX|9.25
ceai obligeana|6.41
ceai paducel|5.93
ceai paducel doze|4.60
ceai papadie frunze Larix|5.81
ceai pedicuta vrac-hypericum|12.77
ceai pelin vrac hypericum|7.44
ceai plantusin DOZE-FARES|9.66
ceai prostatic|7.66
ceai prostatic doze-larix|8.88
ceai prostatic-vrac|8.35
ceai pufulita cu flori mici|5.81
ceai pufulita cu flori mici FARES-DOZE|6.29
ceai renal L|7.55
ceai renal-doze larix|8.88
ceai roinita larix|4.60
ceai salvie larix|5.32
ceai salvie doze|4.60
ceai senna fz fares|9.07
ceai silueta perfecta +drenaj|8.10
ceai silueta perfecta contra greutatii|9.56
ceai soc-flori 50 gr|5.81
ceai somn limistit|9.21
ceai stimularea lactatiei|8.44
ceai sunatoare|4.60
ceai sveltaflor- doze-fares|10.65
ceai sveltaflor-punga fares|10.88
ceai tei doze-larix|7.50
ceai tei vrac|11.50
ceai tensiune-doze fares|10.99
ceai trei frati patati larix|4.90
ceai urzica|5.32
ceai urzica doze|4.60
ceai vasc- FARES|10.16
ceai verde|4.33
ceai verde cu lamaie|4.22
ceai verde lamaie suprapilc|6.33
ceai verde frunze 100 gr|6.53
ceai zmeura si capsuni- suprapilc|6.99
ceai zmeura si capsuni-LARIX doze|4.22
chelstop 200 ml hofigal|22.99
cheltuieli de expeditie|16.00
cicoare solubila 75 gr|7.88
clipAir dilatator nazal*3 S,M,L diminueaza congestia nazala si sforaitul|72.00
coprocultor cu spatula pe meddo|0.73
cotiera L minut-2 buc|12.71
cotiera M minut-2 buc|12.71
cotiera S minut-2 buc|12.71
cr.anticelulita-200ml termoactiva cu ardei iute|23.60
cr.pt.depigmentare-hid. me%mom 50ml|22.39
cr.reparatoare pt maini galbenele|15.49
creion nazal creioneel|8.95
crema albire cu efect instant spf 20|56.87
crema albirea tenului galbenele|19.12
crema antiacnee cu salvie si sulf 50 ml|16.70
crema anticelulita 500 ml|33.88
crema anticelulita forte cu ex de cafea verde|22.39
crema antirid colagen plus SPF 15|30.25
crema antirid -galbenele+pantenol 50 ml|18.51
crema antirid nutritiva cu ulei de masline si vit A E F|22.39
crema antirid tonifianta cu acid hialuronic si bujor|24.20
crema antirid-ulei catina+masline de noapte|17.54
crema calcaie crapate 50ml santaderm|19.36
crema calciie-tub 100 ml cosmetic|15.13
crema contur ochi Q10 mineral complex-30ml|23.60
crema contur ochi anticearcan -catina|19.97
crema corp hranitoare omega plus|19.36
crema cu galbenele santaderm 50 ml|11.98
crema cu untul pamantului 70 ML|19.36
crema cu uree 15% santaderm 50 ml|18.15
crema cu uree 30% santaderm 50 ml|20.57
crema cu vit A 40 ML|11.01
crema cu vitamina A+E+C santaderm 50 ml|18.15
crema fundulet me%mom 150 ml|23.38
crema galbenele larix 20 gr|7.38
crema galbenele larix 40 gr|9.92
crema gel hidratare colagen plus|29.04
crema hidratanta calmanta cu musetel si alantoina|21.18
crema hidratanta delicata ci acid hialuronic si bujor|24.20
crema hidratanta nutritiva cu ulei de masline si pantenol|22.87
crema hidratanta-galb+pantenol 50 ml|18.51
crema maini Q10 mineral complex 100 ml cp|13.07
crema maini hidratanta bujor si vit e|12.83
crema maini intens hidratanta miere|13.07
crema maini si unghii argan cp|12.71
crema noapte miere si laptisor matca|19.36
crema noapte Q10mineral complex 50 ml|24.20
crema panthenol forte 6% santaderm 50 ml|21.18
crema plaja copii ozon spf50|26.62
crema propolis larix 40 gr|9.07
crema propolis&galbebele 40 gr|10.04
crema protectiva antimicrobiana permetrina 5% -50 ml parasstes|32.07
crema pt ingrijirea calcaielor 40 ml|10.29
crema regeneranta zi argan+aloe vera 40 ml|22.39
crema restructuranta noapte argan+aloe vera|22.39
crema rostopasca larix 40 gr|7.87
crema tataneasa larix 40 gr|8.47
crema vitaminizanta ulei catina+masline|17.54
crema zi catifelanta miere si laptisor matca|21.78
crevil crema venifera 250 ml-|18.76
crevil-forta ursului polar 250 gr|18.76
crevil-gheara dracului 250 gr-balsam|16.94
crevil-gheara dracului 250 gr-gel|16.94
crevil-puterea calului 250 gr|17.54
crevil-puterea calului chili 250 gr|29.97
curcuma plus 60cps-medica|25.53
curcuma x60 cps medica|0.88
cutii farmaceutice 10 ml|1.63
cutii farmaceutice 100 ml|1.82
cutii farmaceutice 150 ml|1.11
cutii farmaceutice 20 gr|1.33
cutii farmaceutice 30 gr|1.33
cutii farmaceutice 50 gr|18.39
dalin spray pieptanare usoara 200 ml|17.54
decasept 24 cpr|26.62
decasept SPRAY 20 ML|15.97
decasept cu propolis 24 cpr|26.62
decasept junior SPRAY 20 ML|16.34
decasept lamaie 24cpr|0.00
deo dove 150 original|14.28
depil cr.cu ex.galbenele|14.28
depil cr.cu ex.musetel|14.28
depil cr.rapida cu ex de aloe vera cp|14.28
dezarcit sol.tratament ciuperca unghiei 5 ml|96.80
discount rectostop ointment unguent pharmacy laboratories|11.60
discount unguent b-cure 75 ml|8.29
dischete demachiante 120 buc|7.14
dispozitiv curatare urechi demicso|73.81
distonoplant-cps fares|54.95
durex love 3 buc|9.07
dus gel dove 450 ml fresch cucumbe|15.73
emulsie plaja adulti FP 30|19.35
frectie galenica 100 ml|13.31
frectie cu hamamelis*100 1 DIANA|24.22
fructe de goji 100 g|9.44
garlicaps-30 caps 1+1 FMN|16.31
gel aloe vera larix|15.55
gel antiacneic busuioc 30 ml|16.34
gel anticelulitic larix|15.73
gel antireumatic 100ml larix|16.34
gel arnika-larix 150 ml|13.92
gel calmant pt intepaturi si insecte santaderm-30 ml|27.83
gel cu tataneasa 350 gr|21.18
gel din tataneasa 200 ml|18.15
gel igiena intima-cu ex de nalba DR.SOLEIL 300 ml|16.34
gel impotriva intep,de insecte roll on 10 ml|24.08
gel picioare usoare 150ml larix|14.52
gel pt baturi-santanderm 20 ml|21.78
gel pt curatarea fetei HYDRA GEL DR.SOLEIL -200 ml|13.07
gel pt iritatii fesiere bebelus baby calm|13.07
gel taina ursilor alpifresch-250|18.76
gel tataneasa-150 ml larix|14.52
gel-balsam ghiara diavolului 250-alpifresch|15.37
gemod.mladite de catina hofigal|18.09
genunchiera MINUT L-2 BUC|14.88
genunchiera MINUT SMOLL|14.46
genunchiera MINUT medie-2 buc|15.13
gingo b.&Ginseng & royal jelly 1000+200+300mg|17.54
gingo biloba&ginseng 10 fiole/10ml 1000+1500mg|17.42
ginseng and royal jelly 10fi/10ml 200+300mg|17.54
glezniera MINUT L-2 buc|15.13
glezniera MINUT M 2 BUC|15.13
glezniera MINUT S 2 BUC|15.13
glicerina boraxata 10% 25 gr|5.32
good skin-gleansing gel|21.78
good skin-hydra boost gel-crem|19.91
good skin-protect &mattify cream|24.74
gripovit MAX C hot lemon 10plicuri|43.56
gripovit MAX C hot lemon fara zahar-10 pl|43.56
hyper stevia rebaudiana 170 tablete|14.43
hyper stevia rebaudiana HYPERICUM-50 ml|14.99
inel dentitie cu apa tru 3+|8.11
irigator|15.73
irigator burduf deea|12.10
irigator nazal tip seringa 2 buc minut|10.65
jutavit BISGLICINAT DE MAGNEZIU 100 CPS|60.26
jutavit DIGESTIVE ENZYME 30 CPS|30.25
jutavit CALCIU+D3 GUMATA gust de zmeura fara zahar-50 buc|27.83
jutavit Glucomannan|48.40
jutavit K2 120mg+D3 2200NE+K1 700ug 60 cps|46.59
jutavit Magneziu 250mg+B6+D3 retard 45 tab|22.99
jutavit VIT D3 2000UI masline 100 cps|32.67
jutavit biotina B7 900mcg 100 tb|39.57
jutavit calciu 550mg efervescent gust lamaie 16 buc|18.76
jutavit caps,usturoi 420mg*100/cut|22.99
jutavit coenzima Q10+E 35mg 40 cps|50.82
jutavit collagen complex 60 tb|39.32
jutavit collagen gumat+hialuron acid fara zahar x60|48.04
jutavit complex sirop MERISOR+ex.splinuta 150 ml|33.88
jutavit cpr.de supt gust lamaie-24tb|21.54
jutavit crema dernored 100 g|22.99
jutavit enzima lactaza 6500FCCU 60 tab|29.65
jutavit fier organic 18mg+acid folic+zinc+vit c|35.09
jutavit gumata C gust de banane 60tb|32.07
jutavit gumataD3 gust de zmeura 60tb|32.67
jutavit hair caps plus 60 cps moi|35.09
jutavit herbal hot drink 12 plicuri|36.06
jutavit herbal hot drink kids 12 plicuri|36.06
jutavit omega 3 kid 45 tb moi gust portocala|29.04
jutavit omega 3 ulei peste 120mg+vit E 100cps|39.33
jutavit picaturi D3 30 ml|19.97
jutavit picaturi vitamina c 30 ml|19.97
jutavit prosta intense 60cps|45.98
jutavit sirop patlagina ingusta 150 ml|22.99
jutavit vit .C 1000mg ex maciese+D3*60 tb|34.39
jutavit vit .C 1000mg-retard ex maciese+D3*100 tb|36.30
jutavit vit. B12 1000ug 60tb|34.49
jutavit vit. B6 12mg 100tb|20.57
jutavit vit.c 1000mg ex maciese+D3*45buc|27.84
jutavit vitamina B1-10MG 60 TAB|20.57
jutavit vitamina A 10000NE 50 caps|33.88
kartilin crema 50 ml|11.50
kin apa de gura fluorkin calcium 500 ml|44.17
kin apa de gura sensikin 250 ml|37.51
kin oro tablete de curatare 30 buc|35.70
kin apa de gura gingival complex 2 x 1 litru|205.70
kin apa de gura periokin 250ml 0.20%clorhexidina+0.1% cpc|66.55
kin gel pentru gingii periokin 30ml|34.39
kin gel pentru gingii periokin acid hialuronic 1% 30ml|79.86
kin gel pt gingii Sensikin 15ml|23.96
kin pasta de dinti fluorkin calcium 75 ml|22.39
kin pasta de dinti gingival complex 75 ml|36.06
kin pasta de dinti pentru albire progresiva 75 ml|27.84
kin pasta de dinti sensikin 75 ml|19.10
kin periuta de dinti medium|0.00
kin periuta de dinti JUNIOR|0.00
kin periuta de dinti SOFT|19.10
kin periuta de dinti si gingii|3.02
kit coprocultor|5.20
kit coprocultor cu mediu CARRY BLAIR|27.83
lacalut SENSITIV apa de gura micelara 500 ml|24.20
lacalut aktiv set pasta*75ml+balsam buze|27.83
lacalut sensitive antiplaque apa 300 ml|24.20
lacalut sensitive+ata dentara 75 ml|25.41
ladies dream 2 cps|8.47
lantisor rotund pt suzete minut2018014|16.34
lapte demach.vitaminizant cu catina|14.52
lecitina forte 1+1 30capsule|9.32
lingurita cu varf de silicon 4+ minut|33.88
lipostop 60cps 1+1|19.36
lot. pt. picioare-mebra|18.76
lotiune antiacneica-busuioc cosm. plant|17.54
lotiune astringenta cu ulei de salvie|21.18
lotiune corp hidratanta complex de hidratare si bujor|17.54
lotiune picioare cosm.plant|17.54
lotiune tonica -castraveti 200 ml|0.00
lotiune tonifianta par-spray 150ml cosm plant|15.97
lubrifiant natural cu 100 ml- virde|12.22
lubrigrl-gel lubrifiant DR.SOLEIL-100 ml|11.37
mami&bebe,biosept 30CAPS|41.07
mami&bebe,biosept SIROP FRUCTOZA 100 ML|42.96
manseta cu deget minut L|13.07
manseta cu deget minut M|13.07
manseta cu deget minut S|13.07
manseta-MINUT L|9.56
manseta-MINUT MEDIE|12.10
manseta-MINUT SMOOL|9.98
manusi ex.latex pudrate 5.0g L minut|21.78
manusi examinare nitri nepudrate XS|18.76
maraton gel 50 ml|30.25
masca chirurg.-cu elastic|0.24
masca oxigen adulti|4.11
microclisme adulti alphalax|29.04
microperfuzoare 21 G|0.54
microperfuzoare 23 g|0.53
mini benzi cu ceara dep.la rece 36 buc|12.10
mixtura mentolata vitalia 100 ml|7.26
mobilin gel calmant ROLL-ON 50 ML|27.83
molekin imuno 4 ani+ 12 acadele cu aroma de citrice|42.96
narcis bandaj elastic autoadeziv 4.5cm/4.5cm|5.74
narcis bandaj elastic autoadeziv 5cm/4.5m|4.04
nebulizator compact|145.20
nebulizator delfin|145.20
nebulizator minut handyneb classic cu piston|155.85
negro coacaze negre 79 GR-|7.02
nivea gel dus 500ml|11.80
nosko mouth-aspirator nazal|35.94
nosko ser fiziologic 20 monodoze*5ml|28.44
omega 3ulei de peste 1+1 parapharm|16.34
omega plus-balsam si masca reparator si protector cu omega 3,6,7,9%ulei de avocado|18.39
omega plus-crema antirid hranitoare si rev cu omega 3,6,7,9%ulei de avocado|30.25
omega plus-crema hid.emolienta,catifelanta cu omega 3,6,7,9%ulei de avocado|30.25
omega plus-crema maini|0.12
omega plus-crema maini hranitoare|11.50
omega plus-sampon reparator si protector cu omega 3,6,7,9%ulei de avocado|18.76
oral-B pasta complete protect&clin 75 ml|9.80
oral-B pasta kids 0-6 ani 50 ml|11.13
oto cleaner HA 50 ml|4.84
organizator med.zilnic sana|16.34
organizator medicamente 7/14 zile|9.07
organizator medicamente liniar|24.20
panax ginseng 2000mg 10 fiole *10 ml|17.54
parasoftin sosete exfoliante|42.35
pasta dinti cu carbune activ 125 ml|11.50
pd colgate baby strawberry 50 ml 0-2 ani|0.00
pd.colgate Advanced white 100ml|8.23
pd.colgate triple action 100 ml|7.14
pediform*100 ml bioeell|21.78
penseta pt scos capuse dr schick|16.70
pepon-caps.cu ulei de dovleac 30cps 1+1|27.23
peri de dinti colgate clasic|3.09
peri de dinti colgate extra clean mediu|3.21
peri de dinti colgate premier|2.84
perie biberon+tetina minut baby pl307|7.87
perii dinti colgate zig zag mediu|3.75
periuta copii pinguin 2 buc|9.56
periuta de dinti cu carbune ultra|6.96
periuta interdentara +10 micro capete|11.37
picaturi propolis 30 ml|21.78
picaturi propolis glicolic 30 ml|21.78
plantusin 0.25 ml|32.07
plantusin forte 0.25 ml|41.14
plast .sutura*8 buc|5.20
plast .sutura*8 BUC 5-3x75mm; 3-6.4x80mm|4.96
plast .sutura*8 BUC 5-64x108mm;--12,7-108mm|7.99
plast.aquastop elastic 20 buc|5.20
plast.aquastop transparent 4 buc|6.53
plast.clasici 20 buc|3.63
plast.clasici cu pans. antiseptic 30 buc|5.57
plast.clasici cu pans.hemostatic 30 buc|5.45
plast.hidroclorid pt vezicule si bataturi|8.17
plast.impotriva durerii mensruale barza-3 buc|33.88
plasture economic de prim ajutor octacare 5 buc|5.08
plasture impotriva acneei octacare 36buc|27.35
plasture prim ajutor sensitivi 15/25mm*72mm octacare 14 buc|5.08
plasture antireumatic -HOT AND STRONG 12*18|2.66
plasture impotriva durerii-mobilin cu ulei natural de pelin|27.23
plasturi cu desene de prim ajutor octacare 20*amb|3.75
plasturi de prim ajutor asortati octacare 20*amb|5.08
plasturi de prim ajutor colorat octacare 20*amb|5.38
plasturi rotunzi de prim ajutor octacare 20*amb|3.21
plasturi copii pt rani emoticon*20 buc|5.08
plasturi cu arnica si gh.draculuui 9*14|2.78
plasturi medicinali Minut Plast 12 buc/cutie|1.82
plasturi pt ochii adulti 10/cut MINUT|9.44
plasturi pt ochii copii 10/cut MINUT|9.20
plasturi rotunzi de injectie 100/cutie|7.14
plasturi standard prim ajutor 19mm*72mm octacare 20*amb|4.60
plasturi sterili 15/9CM octa care|2.00
plasturi sterili 7.5cm*5cm octa care|0.76
pompa lapte MEDDO|15.73
pompa piriforma nr 11 minut 210 ml|13.31
pompa piriforma nr 9 minut 135 ml|11.92
pompa san electrica cu bloc de comanda digital dr life|140.36
pompa san manuala MINUT|87.12
poxclin-spray contra varicelei 100 ml|72.00
pres servicii marketing conorm contract|0.00
prevomit KIDS*3ani+ 6 acadele-aroma de lamaie|30.25
propolis cu galbenele spray 25 ml|21.18
pudra antimicotica 75 gr|10.84
pudra corp baby CAONATUR 100gr|10.65
pudra cu propolis MEBRA 75 gr|10.29
pudra fructata|10.29
pudra mentolata|10.29
pudra mentolata impotriva transpiratiei|17.32
pufulita*60CPS medica|0.64
punga urina pediatrica 100 ml|2.24
pungi urina cu valva se scurgere Germanmed- in T|10.77
quartett balsam gh diavolului 250 ml|12.95
quartett melkfett unguent vaselina+galbenele 250ml|58.08
raniseptol arsuri spuma 150nl|0.00
reducere|0.00
reducere luna iunie nr 58|0.00
revista hofigal nr 58|4.84
rivanol 1% - vitalia 200 g|7.87
rivanol 1% -cu pulverizator vitalia 200 g|7.87
royal jelly extractum 300mg-10fiole-|17.42
salprogel 20 ml|24.56
sampon antimatreata sulf + urzica|16.94
sampon antiparaitar DR.SOLEIL|22.39
sampon fortifiant cu nuc|15.97
sampon pentru par gras larix musetel si urzica|10.77
sampon pentru par uscat larix cimbrisor si aloe vera|10.65
sampon regenerator cu ulei de argan BIO|18.15
sampon seboreglator cosmetic plant|20.57
sampon tratament paduchi santaderm 150 ml|58.08
sampon tratament paduchi santaderm 50 ml|29.04
sana cotiera L x 2buc|21.78
sana cotiera M- 2 buc lot 535|22.39
sana cotiera S-2 buc lot 535|19.97
sana genunchiera EL XL X2|25.41
sana genunchiera EL large x2|25.41
sana genunchiera EL medium x2buc|25.41
sana genunchiera EL smoll x2|25.41
sana spray impotriva tantarilor-capuse|16.94
santaderm roll on repelent tantari & capuse 60ml|32.71
sapun cu sulf 100 gr|8.47
sapun lichid cu galbenele 500 ml|9.56
sapun protex cream 4*90gr|15.13
sapun protex deo 4*90gr|15.13
sapun vegetal -hofigal|21.78
sare amara 125 gr,springmarkt|7.77
sare amara 500 gr,springmarkt|20.54
sare terapeutica de bazna 900 gr|30.25
scutec adulti-dr comfort jumbo CHILOT LARGE*30|94.38
scutec adulti-dr comfort jumbo CHILOT MEDIU*30|83.49
scutec adulti-dr comfort jumbo LARGE 30/pac|78.65
scutec adulti-dr comfort jumbo MEDIU 30/pac|73.81
semite chia 100 gr|4.77
semite chia 500 grame|21.65
semite chia pg 1 kg|38.85
seminte de dovleac 100 gr|6.27
seni Man super level 5 15+|29.04
seni activ clasic*30 chilot* SMALL|89.54
seni activ clasic*30 extra large|114.95
seni activ clasic*30 large|102.85
seni activ clasic*30 mediu|94.38
seni care emulsie piele uscata 500 ml|32.67
seni care-servetele umede *48|15.73
septiclean sol.hidroalcolica cu apa oxigenata 100ml|18.45
ser antirid intens hidratant collagen plus|33.88
ser fiziologic 60 monodoze X 5 ML|0.12
serv.umede BARZA cu bicarbonat de sodiu 12 buc|0.00
serv.umede antib.clasic 15 buc|2.42
serv.umede antib.kids 15 buc|2.42
serv.umede pt curatat ochelarii 30 buc|7.87
servetele intime bella sensitive A 20|6.90
servetele umede copii capac Naturel monuk'all-72buc|4.11
servetele umede copii pink monuk'all-72buc|4.11
servetele umede demachiante 25 buc|3.03
servetele umede intime 20 buc|44.77
set cadou VIT C plus set ingrijire skin boost 30+|47.19
set cadou VIT C plus set ingrijire skin boost 40+|47.19
set cadou VIT C plus set ingrijire skin boost 50+|10.53
set manichiura 3 piese tr10805|26.62
sirop afin 500ml|24.98
sirop afin fara zahar 500ml|23.60
sirop brad cu zahar 500ml hypericum|24.81
sirop catina alba cu zahar-500 ml|24.42
sirop catina alba fara zahar 500 ml|26.62
sirop coacaz negru 500 ml|24.42
sirop coacaz negru fara zahar 500 ml|23.31
sirop contra tusei-250ml fara zahar|21.78
sirop contra tusei-250ml hypericum|35.09
sirop laxativ 100 ml lot 01|21.18
sirop merisor cu zahar 500 ml|18.76
sirop muguri de pin si brad vitalia 100 ml|25.41
sirop muguri pin FARES|15.13
sirop patlagina 100 ml vitalia|23.60
sirop patlagina FARES|50.82
slabofitcat SLIM 30 cps|9.92
spliter pastile cu depozitare|9.07
spray antibacterian TOUCH 59 ml|9.07
spray antibacterian TOUCH 59 ml-exotic|29.04
spray antimicotic pt picioare 4feet -santaderm|0.00
stand BEBBLE|0.00
stand OCHELARI NARCIS 30 BUC|0.00
stand octacare|20.57
stick calm pentru capk 3.6g|49.95
stomac sanatos-63 cps D49|13.01
supozitoare Laxaclean adulti *10 buc|12.77
supozitoare Laxaclean copii 10 buc|9.07
suzeta silicon 6+ minut|6.53
suzeta silicon 0+ ro339|9.07
suzeta silicon 0+ tr2011460|9.07
suzeta silicon 3+ tr2011460|6.53
suzeta silicon 6+ ro337|8.95
suzeta silicon ortodontica 12+ minut baby|8.71
suzeta silicon rotunda minut baby 0-6 luni|8.95
suzeta silicon rotunda minut baby 12 +luni|7.38
suzeta silicon rotunda tr-ppp005 0+|7.38
suzeta silicon rotunda tr-ppp005 3+|53.24
tab.maciese vit C 1200MG X 80cps|5.93
tamp.discreet 20 ocean|7.50
tamp.libresse-10 FRESCH natural|8.71
tampoane cu alcol 100buc/cutie|16.94
tampoane pentru sani 30buc|0.22
taxa termo verde/buc. cat 5.5 term.infrarosu|128.26
tensiometru atomat pt brat DLRAK 289|217.80
tensiometru auromat de brat CU VOCE dr life RAK298|72.60
tensiometru cu stetoscom-minut|145.20
tensiometru digital atomat pt brat dr life DLRAK288|151.25
tensiometru pentru brat dr life|107.69
tensiometru pt.incheietura mainii dr. life|6.53
termometre camera lemn Minut temp|4.84
termometre camera suport plastic Minut|8.23
termometru baie 504|8.17
termometru camera copii-minut|17.06
termometru clasic cu disp.de resreare cool med|14.52
termometru digital cool med varf flexibil|15.13
termometru digital flexibil copii- termax|102.85
termometru digital infrarosu MINUT|335.78
termometru digital infrarosu berrcom|19.36
termometru digital varf flexibil cap animalete dr life|9.32
termometru frigider|26.62
test Veneris de infectie urinara|10.65
test antigen rapid SAFECARE COMBO gripa A/B si covid 19|16.94
test menopauza BARZA banda|14.52
test ovulatie minut 5buc+test sarcina|32.67
test rapid depistare droguri 10 parametri din urina|0.00
test rapid vitamina D|71.39
test rapid vitamina D self care|0.00
test sarcina BARZA-caseta ultrasensibil+serv.intime|18.15
teste de sarcina -BARZA|0.00
teste de sarcina -BARZA BANDA|12.10
teste de sarcina -BARZA CASETA|15.13
teste de sarcina -BARZA CASETA -ULTRASENSIBIL|17.71
teste de sarcina -BARZA CASETA -p|0.01
teste de sarcina -BARZA CASETA*ULTRASENSIBIL|0.01
teste de sarcina -BARZA STILOU|19.36
teste de sarcina -BARZA ultrasensibil banda|15.10
teste de sarcina -BARZA ultrasensibil banda-p|0.01
teste sarcina blue dream|1.73
tetina latex-rotunda 1-2 buc|6.05
tetina silicon x 2 tr2011006 0+|8.95
tetina silicon x 2 tr2011006 3+|9.07
tetina silicon x 2 tr2011006 6+|8.95
tetina silicon 442 6+ luni3/bl|7.99
tetina silicon orto 0+ minut|8.47
tetina silicon orto 3+ minut|8.47
tetina silicon orto 6+ minut|8.47
tetina silicon super fin 3+ MINUT|7.99
tetina silicon super fin 6+ minut|7.99
tinctura antialcol|16.34
tinctura de iod 2% vitalia 40 g|7.26
trusa mica chirurgie SUTURI steril set|9.68
uRINAR CU PALNIE MEDDO|18.15
ulei de argan virgin 10 ml|9.80
ulei de levantica macerat cps|27.75
ulei de masaj cu vit.E si ulei din sambure de stru 260 ml|21.18
ulei de parafina 40 gr|4.36
ulei de ricin-40 gr vitalia|6.29
ulei de salvie macerat cps moi-hofigal|17.18
ung galbenele-20gr viva|3.33
ung.pt ameliorare arsuri b-cure 75 ml|11.50
unghiera inox xl|8.47
unguent cu sulf 10% santaderm 30 ml|16.94
unguent ihtiolat*30 ml santaderm 10% lot 01|15.49
urinar meddo|16.94
urocultoare sterile 120 ml|0.87
urocultoare sterile 60 ml cu eticheta|0.82
valeriana - 40 CPS|20.54
vapour rub 50GR adulti si copii 3 an+|18.15
vapour rub 6luni+ 50 gr|18.15
vata med,tip BC IZIS 100 gr|5.02
vata med,tip BC IZIS 200 gr|8.41
violet de gentiana vitalia 25 g|4.48
vivapore pansament adeziv steril 10cm/9cm|1.69
vivapore pansament adeziv steril 15cm x9 cm|2.30
vivapore pansament adeziv steril 20 cm x10 cm|3.21
vivapore pansament adeziv steril 5cm x 7 cm|0.97
vivapore pansament adeziv steril 6 cm/10cm|1.39
vizik allergy pic.de ochi 10 ml|49.61
DUREX- 3 BUC extra safe|9.07
DUREX- 3 BUC pleasuremax|8.83
DUREX- 6 buc extended pleasure|15.13
JUTAVIT COMPLEX D-MANDOZA 500mg 90 tb|49.61
PULSOXIMETRU CU BATERI|66.55
Plasturi THERAPY STOPDOL tensiuni musculare artrit 10*13 cm|5.32
QPlaster transparent *16 buc|4.84
Semimasca bumbac doua straturi|8.29
Seni care servetele umede alantoina&vit.E*80|22.87
Servetele umede copii fresch qcare*56|5.20
Servetele umede copii sensitive qcare*56|5.20
Servetele umede copii soft qcare*56|5.20
Set perie si piaptan primi pasi|8.71
absorbante Bella perfecta slim BLUE A10|8.35
absorbante zilnice panty soft *20|5.45
absorbante zilnice soft deo *20|5.45
alezin plus crema 50 g|9.68
always tampone sens 10 buc ultra plus|10.29
ata interdentara ceruita 100 m|10.59
balsam buze ARGAN|6.17
balsam buze BIO fructe|6.17
beb039 my friend spray pt pieptanare usoara 150 ml|18.76
beb042 my friend sampon si dus gel 2 in 1 250 ml pepene verde|17.54
biberon forma broasca,ursulet ,rata 250 ml|10.16
biberon PP decor 125 ml|7.02
biberon pp decor 250 ml|7.26
boneta cu sampon multi care comfort|18.15
brozz spray max imp.tantari si capuse 90 ml F2|21.18
cana anticurgere cu maner si capac primi pasi|10.53
cana cu maner si cioc silicon anticurgere 250ml|12.10
cana cu pai primi pasi|10.89
caola balsam de maini 300 ML|22.39
caola pudra talk ALOE VERA 100GR|10.84
caola pudra talk musetel 100 gr|11.19
cimmerin plus gel 7 g|11.50
cliseu digital eticheta zarinil|578.38
creion pt.rani minore dup barbierit|7.50
crema galbenele-schmees 250ml|11.86
crema gh dracului 250 ML herbamedicus|10.65
crema protectoare pt fata OLIV spf 50|28.44
crema zi Q10-50ML mineral complex|24.20
gel aloe vera cu d-pantenol 200 ml|19.36
halls colors|3.03
halls coolwave|3.33
halls honey lemon|3.33
halls lime fresh|3.57
halls-cola|3.57
halls-extra strong|3.03
halls-fructe de padure|3.57
halls-miere si lamaie|3.57
halls-original|3.57
jutavit Natural K2 120mg 60TB|39.32
jutavit calcimax forte 60 tab|31.46
jutavit caps.pt.sanatatea ficatului armurariu- 60 cps|38.72
jutavit colagen +hialuron articulati 400 g capsuni si zmeura|84.70
jutavit colagen +hialuron articulati 400 g fructe de padure|84.70
jutavit colagen ananas 400 g|110.11
jutavit diosmin+hesperidina 30 tb|39.32
jutavit glucozamina condroitina +colagen+msm|50.82
jutavit glucozamina condroitina +colagen+msm-120 buc|78.65
jutavit lutein forte 12 mg 60cps|50.82
jutavit multiv.50+ 45 buc/cut|31.46
jutavit multiv.imunocomplex pt copii-45buc.masticabil|30.25
jutavit multivitamina adulti retard 45 buc/cut|33.88
jutavit multivitamine gumate gust zahar-50 buc|29.04
jutavit pic.suedeze 40plante fara alcol|23.60
jutavit probium+inulina 15 cps|33.88
jutavit seleniu organic 100ug 100 tab|36.30
jutavit ulei de dovleac 600mg/100 buc|82.28
jutavit ulei krill 1500mg 60cps|23.60
jutavit valeriana 45 caps|35.70
jutavit zinc organic 25 mg*100 tb|5.75
lingurita moale pt biberon primi pasi|49.01
litorsal SENIOR *24 cpr eff.|47.19
litorsal electroliti GRAPEFRUIT *24 cpr eff.|21.66
manusi ex.nitril 12 cuti M|4.949.00
masina etichetat metro 50.0s|4.779.50
matrita dubla PET 300 ml|31.22
mixer electric biberon ro902|41.75
nail repel myco clean stift 3 ml|2.78
pansament steril MINUT PORE 10 cm x30 cm|11.50
pasta de dinti pt copii active oral care fresch&fr cu fluor ,fara zahar x100ml|11.50
pasta dinti curatare zilnica si completa a dintilor fumatorilor|11.50
pasta dinti protectie zilnica a smaltului dintilor sensibili *100 ml|9.56
periuta de dinti voiaj 2 buc|21.78
picaturi grapefruit 30 ml|5.32
plast.indepartare bataturi 6buc|14.52
plasture antiherpetic 15 buc|2.60
plasture antireumatic mentol 12/18 minut|2.60
plasture antireumatic mentol 12/18 minut bis|4.24
plasture cu aloe vera *25 buc|7.14
plasturi pt flictene(basici) 5buc minut|16.94
protectie din silicon pt mamelon minut baby|3.15
protectoare auditive spuma-cu snur|1.75
protectoare auditive spuma-fara snur|22.99
punga cu gel terapie cald-rece|0.00
samp.gel bubchen 230-copii|24.81
sampon antiparazitar-DR HAPPY +piapten gratis|2.78
sanitaband-plasturi antirematici ardei iute|10.89
schmees balsam puterea ursului 250ml|19.00
schmees balsam-500ml herbamedicus|21.78
schmees balsam-500ml herbamedicus-HOT|11.62
schmees cr.herbamedicus castane+vita de vie 250ml|11.62
schmees glucosamin crema 250ml|84.10
seni activ plus 2 XL*10|41.14
seni active pull up normal small*10|55.66
seni active'clasic chilot extralarge*10|49.01
seni active'clasic chilot large*10|44.17
seni active'clasic chilot mediun*10|56.27
seni active'pull up' normal large*10|64.13
seni basic small 30 buc|26.21
seni care spuma ingrijire corp 500 ml|36.30
seni clasic air large *10|30.86
seni clasic air mediu *10|95.59
seni clasic plus air large 30/buc|93.17
seni extra large-basic 30/pach|21.66
seni lady EXTRA PLUS 15/pac|27.23
seni lady PLUS 15|17.54
seni lady extra slim A15|15.73
seni lady slim MINI PLUS 20/pach|13.07
seni lady slim mini 20/pach|16.94
seni lady slim normal 20/pach|22.39
seni lady super 15 BUC|84.03
seni large-basic 30/pach|70.18
seni medium-basic 30/pach|18.15
serv.umede igiena corporala-50buc multi care comfort|0.00
servetele umede BARZA cu bicarbonat de sodiu|9.68
set cadouOMEGA plus cr hidratanta 50ml+crema corp200ml|42.35
set hranire bebbe silicon linguruta,cioc,rezervor|33.28
set linguruta si furculita ro567|6.41
set manichiura 3 piese primi pasi|9.20
set perie dinti -3 varste primi pasi|11.92
spray aloe vera 100% 50ml|15.37
spray cu gheata 150 ml|15.13
spray cu gheata 300 ml|24.20
spray de pantofi 150 ml|11.74
spray de picioare bf|11.74
spray protectiv tantari &capuse spf 50 -100ml|70.79
spray repelent tantari &capuse 100 ml santaderm|0.00
spray repelent tantari&capuse 100 ml santaderm|30.29
spray tratament paduchi santaderm 100 ml|57.48
stiker antitantari|3.63
tamp OB proc. mini-16|13.61
tamp always ultra day super 7/pac|9.20
tamp.Alway Ultra sens. 10|9.68
tamp.always duo day night 14|15.25
test barza amnio test 3 buc/cutie|76.23
test ovulatie barza 5+1 test de sarcina|26.62
test ovulatie x5 blueCROSS +test sarcina|10.89
tetina gat extralarg curg.rapida 2valve,anticolici-b buc/6luniv|18.15
transderm GIO sol.coloidala pt indepartarea negilor si bataturilor|31.46
transderm-pl.cu efect keratolitic 6/cutie|9.80
ulei canabis 30 cps|59.29
ulei catina-600mg cps moi hofigal|43.56
ulei catina-900mg cps moi hofigal|43.56
ulei esential de citronella 10 ml|14.52
unguent protectie antiherperica 10ml|11.13
zgarda impotriva puricilor si capuselor caini 65 cm|16.77
Ace 25g 0.5x25 minut|0.15
COMPRESE NESTERILE TIFON 10/20*8 pliuri-100 buc|24.20
FASA TIFON -40 GR. 10M/15CM|3.57
FASA TIFON -40 GR. 10M/20CM|1.51
Leucoplast 2,5cm x1.M MINUT|4.72
Leucoplast 2.5cm x5 m MINUT PLAST|12.10
Plas.pt.rau de miscare narcis 10 buc|9.80
TIFON HIDROFIL 5 M/PACH-roval|9.07
TIFON METRAJ NARCIS 19GR/2,90cm*5cm|11.25
VITAMINA C-500 K145|0.27
ace 27 g bd 0.4 x13|14.52
ace intramusculare 20GX1 1/4|14.52
ace intramusculare 21G x1 1/2|14.52
ace intramusculare 22G 1 1/2 negre|14.52
ace intramusculare 23GX1 1/4|0.15
ace stomatologice 0.45/16|4.48
albastru de metil 1% vitalia|8.59
alcool camforat 10% flacon 40 gr|8.59
alcool iodat 2% fl.40 g -vitalia|7.99
alcool mentolat 1% fl.40 ml|16.94
banda adeziva HELP PORE 10/10|21.78
banda adeziva HELP PORE 15cm/10m|8.47
banda adeziva HELP PORE 5 CM/10M|0.94
banda adeziva rivanol 8 cm x 6 cm|0.27
banda adeziva rivanol cutie|0.27
bandaj elastic cu cleme 10cm/4.5m help|5.45
bandaj elastic cu cleme 15cm/4.5m help|7.02
bandaj elastic cu cleme 5cm/4.5m help|3.15
bandaj elastic cu cleme 7.5/4.5 help|4.84
biosept forte 20 cps moi|47.74
biosept-cps fares|36.06
biosept-sirop fares|0.12
botosei U.F|0.97
branula 16 G|0.97
branula cu valva 18 g verde|0.97
branula cu valva 20 g roz|0.96
branula cu valva 22 g albastra|1.08
branule 24G|0.96
branule 14 g|1.09
branule cu valva 26G|19.36
burete hemostatic surgipon 70*50*10mm 10buc/amb|47.19
centura spate pt zona lombara|50.82
cicaSilver CREMA tub 50ml|86.03
cicaSilver spray 125 ml|89.36
coenzima Q10 forte in uleiul de catina hofigal|21.18
coenzima Q10 forte plus in uleiul de catina|1.21
compresa cald rece 13*27cm qplaster|1.21
comprese sterile-Help 10/8|9.44
comprese sterile-prodcomfarm 10/8cm x 50 str|7.14
conuri auriculare|18.43
dalin sampon fara lacrimi 100 ml|2.54
echinacea cps hofigal|3.03
fasa 10/10 40 gr.|1.20
fasa 10/20 Help|1.63
fesi 5/8|2.30
fesi HELP 10/10|12.84
fesi-help 10/15|3.99
fitodiab cpr-|19.87
forfecuta copii 34045|17.21
giardinofug-medica 30cps|27.35
giardinofug-medica 50ml herbal drops|2.54
gutostop*60cps medica|56.27
halat unica folosinta tip vizitator|40.53
jutavit complex9 cartilaj os&muschi cu 9 subst.active|35.09
jutavit diab control 80tb/cutie|49.61
jutavit merisor ex.de splinuta 800mg 100tb|27.23
jutavit slim lady 100 cps|1.15
laxaclean miniclisme cu glicerina -copii|2.36
leucoplast hartie -Minut 1.5/5m|4.24
leucoplast hartie -Minut 2.5/5|4.84
leucoplast hartie -Minut 5/5|2.66
leucoplast matase -minut 1.5/5m|8.77
leucoplast matase 5 x5 minut|8.86
leucoplast Minut Plast 5 cm x 5 m|5.81
leucoplast Minut Plast 5cm x3 m|1.75
leucoplast transparent Minut Plast 1.5/5m|3.14
leucoplast transparent Minut Plast 2.5/5 m|5.81
leucoplast transparent Minut Plast 5/5|7.26
lips stick CAPSUNI 5.7 ml|7.26
lips stick clasic 5.7 ml|27.50
mag-anghinar 60 cpr|1.81
manusi chir.sterile NR 7.5|2.17
manusi chir.sterile nr 6.5|1.81
manusi chir.sterile nr 7|2.17
manusi chir.sterile nr 8|2.17
manusi ex.latex nepudrate large|22.75
manusi ex.nitril SMALL|18.15
manusi ex.nitril SMALL NEGRE|21.78
manusi ex.nitril large|21.66
manusi ex.nitril medii NEGRE|21.78
manusi exam. nitril-extra large x100 nepudrate|17.54
manusi examinare 100 buc XS|22.99
manusi examinare 100 buc medii-top glove|21.18
manusi examinare 100 buc smoll|21.78
melatonina pura spray 20 ml|49.61
melatonina pura 3mg 120 tb|78.65
melatonina pura 5mg 60TB|45.99
melatonina pura cu extracte vegetale 60 jeleuri|70.18
melatonina pura junior 1mg 40ml|61.71
mentholin-spray gura 25 ml|15.49
milk thisle+colina 30 cps|0.00
milk thisle+colina 30 cps zdrovit|64.13
nazomer forte 30 ml cu nebulizatoru|13.31
nazomer junior 30ml|9.68
nazomer propolis 30ml cu nebulizator|13.07
nazomer-30ml cu nebulizator|9.68
nazomer-HA 30 ml|12.71
ochelari de citit clasici 888 N 1.00+|26.00
ochelari de citit clasici 888 N 1.5+|26.00
ochelari de citit clasici 888 N 1.75+|26.00
ochelari de citit clasici 888 N 2.75+|26.00
ochelari de citit clasici 888 N 4.00+|26.00
ochelari de citit clasici 888N 2.25+|26.00
ochelari de citit clasici 888N 3,5+|26.00
ochelari de citit clasici 888N 4.5+|26.00
ochelari de citit clasici 888N*1.25|26.00
ochelari de citit clasici 888N*5.00|26.00
ochelari de citit modern 880 n 3.25|27.00
ochelari de citit modern narcis style 1.25 +|26.00
ochelari de citit modern 1 880 n 3.75|27.00
ocluzoare sterile QPlaster -10buc|13.92
optisomn*28 cpr|62.92
optolutein forte 60 cps|33.33
optolutein forte 60 cps medica|77.44
org.medicamente lunar *4 casete colorate/zi|61.71
org.medicamente lunar x2 casete colorate/zi|23.96
organiz.medicamente 4 x 7 casete colorate|21.09
paducel 40cps hofigal|18.15
paducel*60cps medica|0.91
pansament adeziv Help-pore 10 cm x 10 cm|1.57
pansament adeziv Help-pore 10cm x 15cm|1.88
pansament adeziv Help-pore 10cm x 20 cm|2.42
pansament adeziv Help-pore 10cm/30|0.61
pansament adeziv Help-pore 5cm x 7 cm|1.21
perfuzor HELPSET lock ac plastic|42.35
picaturi suedeze 100 ml|77.44
picaturi suedeze 250 ml|133.10
picaturi suedeze 500 ml|5.45
plasturi copii tattoo efect fantasy 16 buc|7.02
plasturi cu rivanol 2cm/7cm 20 buc narcis|8.73
plasturi hidroclorid pt vezicule si bataturi*5|3.93
plasturi rez.la apa minut*10 buc|7.99
plasturi sterili 19/72mm 100/cutie|70.18
pompa san nimo surpunp-mnl|22.99
punga de depozitare lapte matern 20 buc|29.04
redigest 50 CPS|27.83
redigest cpr hofigal|17.00
relaxirem 2bls X 20cpr|16.94
relaxirem forte 2bls x 15 cpr film|25.41
relaxirem noapte 2BLS*15 CPR FILM|29.04
salviasept KIDS gat acadele-6/cut|42.35
salviasept KIDS-TUSE acadele-6/cut|42.35
sana bandaj- manseta- L-2buc|13.31
sana bandaj- manseta- S-2buc|13.31
sana bandaj- manseta-M 2 buc|13.31
sana burtiera NR 2|42.35
sana burtiera NR 3|42.35
sana burtiera NR 8|42.35
sana burtiera nr 10|39.93
sana burtiera nr 4|42.35
sana burtiera nr 6|42.35
sana burtiera nr 7|42.35
sana conuri pt.curatarea urechi mici|9.56
sana glezniera elast. 2 buc XL|23.60
sana glezniera elast. L 2 buc|23.60
sana glezniera elast. M 2 buc|23.60
sana glezniera elast. smoll 2 buc|23.60
sana recipient pt lapte praf si gustari|19.60
sana recipient pt lapte praf si gustari sana|0.00
sanytayaki plast.antireumatic|2.78
saruri de rehidratare 20pliculete|21.78
senna 30 cps-parafarm|26.46
seringa 1 ml cu ac|0.29
seringa 1 ml ac 27g1/2 minut|0.39
seringa 50 ml cu ac|1.57
seringa 50 ml fara ac pentru irigatii|1.45
seringi cu ac 10ml -helm|0.39
seringi cu ac 20ml -helm|0.61
seringi cu ac 2ml -helm|0.25
seringi cu ac 5ml -helm|0.28
sirop ridiche-neagra fares|24.81
sonde foley cu 2 cai CH 16|4.36
sonde foley cu 2 cai CH 20|4.36
sonde foley cu 2 cai CH22|4.54
sonde foley B CH 14|4.36
sonde foley ch 24|38.85
spirulina 1000 mg cpr|21.20
spirulina 500 cps|10.77
termometru digital cool med varf rigid|32.67
test rapid afectiuni ale rinichilor self care|42.35
test rapid alergii self care|54.45
test rapid boala lyme self care|25.41
test rapid streptococ A|4.82
teste de sarcina-caseta sm MINUT INTIM|1.94
teste de sarcina-minut intim banda 2.5mm|3.75
vata medicinala GH 100 gr|5.93
vata medicinala GH 200 gr|25.41
vermicin capsule|28.44
verolit forte-sol.negi|16.94
verolit-sol.negi|26.02
vitamina A 10 ml-zanna|4.60
vivaqua pans.rezistent la apa 20cm x 10 cm|7.50
"""

def brand_from(name):
    n = name.upper()
    brands = ['JUTAVIT','HOFIGAL','LARIX','ZDROVIT','BIOEEL','BIOEELL','FARES','MEDICA','BEBBLE',
              'SENI','KIN','LACALUT','LISTERIN','SENSODYNE','SANTADERM','SANTANDERM','SOLEIL','COLGATE','ORAL-B','HELP',
              'MINUT','NARCIS','OCTACARE','QPLASTER','QPLAST','OMEGA PLUS','GOOD SKIN','SOLITEINT','MARATON',
              'NEGRO','MY HAIR','BAKUCHIOL','HALLS','BELLA','SCHMEES','HERBAMEDICUS','HYPERICUM','VITALIA','VIVA','SANA',
              'BARZA','MEDDO','MINUT','DR.LIFE','LIFE','DUREX','GRIPOVIT','PROSTAGOOD','PARASOFT','MELA','MAMI&BEBE',
              'KARTILIN','CREVIL','PROBICUM','KURKUMA','NIVEA','DALIN','SN ','CICAFILER','CICASILVER','CAOLA','MOBILIN',
              'KIDIMAG','PAX','PANAX','ALPIFRESCH','ESTETO','VIROBLOC','CARROT','OPTOLUTEIN','MEMBRA','MEBRA','VITAMINA','PROSTAGOOD',
              'GIARDINOFUG','HYPER STEVIA','DIANA','SANYE','FARMACITE','BIOSEPT','VEROLIT','SPIRULINA','SENNA','MILK THISLE','MELATONINA',
              'PEPON','PEDIFORM','PD.COLGATE','LIPOSTOP','APURETIN','MOLEKIN','HERBAL','PUFULITA','SLABOFIT','SLIM','REDIGEST','GUTOSTOP',
              'BIOMICIN','BISGLICINAT','BITTER','BURETE','CARRY BLAIR','DR HAPPY','DR SCHICK','DR SOLEIL','DR LIFE',
              'PARASOFTIN','PARAPHARM','THERAPY','PRIMI PASI','PRIMIPASI','THERMAX','BERRCOM','DLRAK','RAK','SANYE','MERA','SEMINTE']
    for b in brands:
        if b in n:
            return b.replace('BIOEELL','BIOEEL').replace('SANTANDERM','SANTADERM').strip()
    return 'PATRICECOM'

def quantity_from(name):
    import re
    # find common quantity patterns
    pats = [
        r'\d+\s*(?:cps|caps|cpr|tab|tb|cut|buc|gr|ml|kg|g)\b',
        r'\d+x\d+(?:ml|gr|cps)?\b',
        r'\d+/\d+',
    ]
    n = name.lower()
    for p in pats:
        m = re.search(p, n)
        if m:
            return m.group(0)
    return ''

if __name__ == '__main__':
    rows = [r.strip() for r in RAW.strip().split('\n') if r.strip() and '|' in r]
    out = []
    for r in rows:
        name, price = r.rsplit('|', 1)
        name = name.strip()
        try:
            p = float(price.replace(',', '.'))
        except ValueError:
            p = 0.0
        out.append({'name': name, 'price': p, 'brand': brand_from(name), 'quantity': quantity_from(name)})
    print(f'Total extracted: {len(out)}')
    import json
    with open(r'D:\Jutavit\extracted_products.json', 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print('Saved to extracted_products.json')
