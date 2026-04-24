/* =============================================
   PATRICECOM - AI Assistant (Chatbot)
   ============================================= */

(function() {
    const aiFab = document.getElementById('aiFab');
    const aiAssistant = document.getElementById('aiAssistant');
    const aiClose = document.getElementById('aiClose');
    const aiInput = document.getElementById('aiInput');
    const aiSend = document.getElementById('aiSend');
    const aiMessages = document.getElementById('aiMessages');

    // Multilingual UI strings
    const aiLang = {
        ro: {
            title: 'Asistent Patricecom',
            status: 'Online - Cauta orice produs',
            placeholder: 'Scrie un mesaj...',
            sendTitle: 'Trimite',
            welcome: 'Buna ziua! Sunt asistentul virtual Patricecom. Pot sa te ajut sa gasesti produse, sa iti dau informatii despre livrare sau sa iti fac recomandari personalizate.',
            welcomeSuggestions: ['Vitamine', 'Produse imunitate', 'Oferte speciale'],
            greet: 'Buna! Sunt asistentul Patricecom. Cu ce te pot ajuta? Cauti un produs sau vrei o recomandare?',
            greetSuggestions: ['Cauta vitamine', 'Produse pentru imunitate', 'Care sunt ofertele?'],
            offersText: (n) => `Am gasit <strong>${n}</strong> produse cu oferte speciale!`,
            offersSuggestions: ['Mai multe oferte', 'Adauga toate in cos'],
            immunText: 'Pentru imunitate, iti recomand Vitamina C, Zinc si Propolis:',
            immunSuggestions: ['Vitamina C', 'Zinc', 'Produse pentru copii'],
            vitCText: 'Gama noastra de Vitamina C:',
            vitDText: 'Vitamina D - esentiala pentru oase si imunitate:',
            vitBText: 'Vitaminele B - pentru metabolism si sistem nervos:',
            vitText: 'Avem o gama variata de vitamine:',
            vitSuggestions: ['Vitamina C', 'Vitamina D', 'Multivitamine'],
            magText: 'Magneziu - pentru muschi, nervi si reducerea oboselii:',
            magSuggestions: ['Zinc', 'Calciu'],
            omegaText: 'Omega 3 - pentru inima, creier si vedere:',
            omegaSuggestions: ['Coenzima Q10', 'Lecitina'],
            colText: 'Produse pentru frumusete - colagen si acid hialuronic:',
            colSuggestions: ['Hair Caps', 'Hialuron Forte'],
            kidsText: 'Produse speciale pentru cei mici:',
            kidsSuggestions: ['Multivitamine copii', 'Vitamina D picaturi'],
            digText: 'Pentru sanatatea digestiva:',
            digSuggestions: ['Probiotice', 'Enzime digestive'],
            jointsText: 'Pentru articulatii si oase:',
            jointsSuggestions: ['Colagen', 'Calciu + D3'],
            sleepText: 'Pentru relaxare si somn odihnitor:',
            sleepSuggestions: ['Magneziu', 'Valeriana'],
            prostText: 'Produse pentru sanatatea prostatei:',
            prostSuggestions: ['Zinc', 'Seleniu'],
            eyesText: 'Pentru sanatatea ochilor:',
            eyesSuggestions: ['Omega 3', 'Vitamina A'],
            slimText: 'Produse pentru un program de slabire sanatos:',
            slimSuggestions: ['Slim Lady', 'Glucomanan'],
            priceText: 'Preturile sunt afisate la fiecare produs. Spune-mi numele produsului si iti dau pretul exact!',
            priceSuggestions: ['Vitamina C pret', 'Omega 3 pret', 'Magneziu pret'],
            deliveryText: 'Patricecom livreaza in toata Romania:<br><br><strong>Standard</strong> - 2-4 zile, 15.99 Lei<br><strong>Express</strong> - 1-2 zile, 29.99 Lei<br><br>Livrare gratuita pentru comenzi peste 200 Lei!',
            deliverySuggestions: ['Cum plasez o comanda?', 'Metode de plata'],
            paymentText: 'Metode de plata acceptate:<br><br><strong>Ramburs la Curier</strong><br><strong>Card Bancar</strong> (Visa, Mastercard)<br><strong>Transfer Bancar</strong>',
            paymentSuggestions: ['Informatii livrare', 'Politica de retur'],
            returnText: 'Retur gratuit in 30 de zile. Produsele trebuie sa fie in ambalajul original. Contacteaza-ne la <strong>contact@patricecom.ro</strong>.',
            returnSuggestions: ['Contact', 'Livrare'],
            brandText: (b) => `Produse de la <strong>${b}</strong>:`,
            brandSuggestions: ['Vezi toate produsele', 'Oferte speciale'],
            foundText: (n, q) => `Am gasit ${n} ${n === 1 ? 'produs' : 'produse'} pentru "<strong>${q}</strong>":`,
            foundSuggestions: ['Cauta alt produs', 'Vezi toate produsele'],
            notFoundText: (q) => `Nu am gasit rezultate pentru "<strong>${q}</strong>". Incearca sa cauti dupa numele produsului sau categorie.`,
            notFoundSuggestions: ['Vitamine', 'Imunitate', 'Oferte speciale', 'Informatii livrare'],
        },
        en: {
            title: 'Patricecom Assistant',
            status: 'Online - Search any product',
            placeholder: 'Type a message...',
            sendTitle: 'Send',
            welcome: 'Hello! I am the Patricecom virtual assistant. I can help you find products, provide delivery information, or make personalized recommendations.',
            welcomeSuggestions: ['Vitamins', 'Immunity products', 'Special offers'],
            greet: 'Hi! I\'m the Patricecom assistant. How can I help you? Looking for a product or want a recommendation?',
            greetSuggestions: ['Search vitamins', 'Immunity products', 'What are the offers?'],
            offersText: (n) => `Found <strong>${n}</strong> products with special offers!`,
            offersSuggestions: ['More offers', 'Add all to cart'],
            immunText: 'For immunity, I recommend Vitamin C, Zinc and Propolis:',
            immunSuggestions: ['Vitamin C', 'Zinc', 'Products for kids'],
            vitCText: 'Our Vitamin C range:',
            vitDText: 'Vitamin D - essential for bones and immunity:',
            vitBText: 'B Vitamins - for metabolism and nervous system:',
            vitText: 'We have a wide range of vitamins:',
            vitSuggestions: ['Vitamin C', 'Vitamin D', 'Multivitamins'],
            magText: 'Magnesium - for muscles, nerves and reducing fatigue:',
            magSuggestions: ['Zinc', 'Calcium'],
            omegaText: 'Omega 3 - for heart, brain and vision:',
            omegaSuggestions: ['Coenzyme Q10', 'Lecithin'],
            colText: 'Beauty products - collagen and hyaluronic acid:',
            colSuggestions: ['Hair Caps', 'Hyaluronic Forte'],
            kidsText: 'Special products for children:',
            kidsSuggestions: ['Kids multivitamins', 'Vitamin D drops'],
            digText: 'For digestive health:',
            digSuggestions: ['Probiotics', 'Digestive enzymes'],
            jointsText: 'For joints and bones:',
            jointsSuggestions: ['Collagen', 'Calcium + D3'],
            sleepText: 'For relaxation and restful sleep:',
            sleepSuggestions: ['Magnesium', 'Valerian'],
            prostText: 'Products for prostate health:',
            prostSuggestions: ['Zinc', 'Selenium'],
            eyesText: 'For eye health:',
            eyesSuggestions: ['Omega 3', 'Vitamin A'],
            slimText: 'Products for a healthy weight loss program:',
            slimSuggestions: ['Slim Lady', 'Glucomannan'],
            priceText: 'Prices are shown on each product. Tell me the product name and I\'ll give you the exact price!',
            priceSuggestions: ['Vitamin C price', 'Omega 3 price', 'Magnesium price'],
            deliveryText: 'Patricecom delivers all over Romania:<br><br><strong>Standard</strong> - 2-4 days, 15.99 Lei<br><strong>Express</strong> - 1-2 days, 29.99 Lei<br><br>Free delivery for orders over 200 Lei!',
            deliverySuggestions: ['How to place an order?', 'Payment methods'],
            paymentText: 'Accepted payment methods:<br><br><strong>Cash on Delivery</strong><br><strong>Bank Card</strong> (Visa, Mastercard)<br><strong>Bank Transfer</strong>',
            paymentSuggestions: ['Delivery info', 'Return policy'],
            returnText: 'Free return within 30 days. Products must be in original packaging. Contact us at <strong>contact@patricecom.ro</strong>.',
            returnSuggestions: ['Contact', 'Delivery'],
            brandText: (b) => `Products from <strong>${b}</strong>:`,
            brandSuggestions: ['View all products', 'Special offers'],
            foundText: (n, q) => `Found ${n} ${n === 1 ? 'product' : 'products'} for "<strong>${q}</strong>":`,
            foundSuggestions: ['Search another product', 'View all products'],
            notFoundText: (q) => `No results found for "<strong>${q}</strong>". Try searching by product name or category.`,
            notFoundSuggestions: ['Vitamins', 'Immunity', 'Special offers', 'Delivery info'],
        },
        hu: {
            title: 'Patricecom Asszisztens',
            status: 'Online - Keressen bármely terméket',
            placeholder: 'Írjon üzenetet...',
            sendTitle: 'Küldés',
            welcome: 'Jó napot! Én a Patricecom virtuális asszisztense vagyok. Segíthetek termékeket találni, szállítási információkat adni vagy személyre szabott ajánlásokat tenni.',
            welcomeSuggestions: ['Vitaminok', 'Immunerősítők', 'Akciós termékek'],
            greet: 'Szia! A Patricecom asszisztense vagyok. Miben segíthetek? Terméket keres vagy ajánlást szeretne?',
            greetSuggestions: ['Vitaminok keresése', 'Immunerősítő termékek', 'Milyen akciók vannak?'],
            offersText: (n) => `<strong>${n}</strong> akciós terméket találtam!`,
            offersSuggestions: ['Több akció', 'Mindet kosárba'],
            immunText: 'Az immunrendszer erősítéséhez C-vitamint, cinket és propoliszt ajánlok:',
            immunSuggestions: ['C-vitamin', 'Cink', 'Gyerekeknek való termékek'],
            vitCText: 'C-vitamin kínálatunk:',
            vitDText: 'D-vitamin - elengedhetetlen a csontoknak és az immunrendszernek:',
            vitBText: 'B-vitaminok - az anyagcseréhez és az idegrendszerhez:',
            vitText: 'Széles vitamin választékunk van:',
            vitSuggestions: ['C-vitamin', 'D-vitamin', 'Multivitaminok'],
            magText: 'Magnézium - izmoknak, idegeknek és fáradtság csökkentésére:',
            magSuggestions: ['Cink', 'Kalcium'],
            omegaText: 'Omega 3 - szívnek, agynak és látásnak:',
            omegaSuggestions: ['Q10 Koenzim', 'Lecitin'],
            colText: 'Szépségápolási termékek - kollagén és hialuronsav:',
            colSuggestions: ['Hair Caps', 'Hialuronsav Forte'],
            kidsText: 'Gyermekeknek szánt termékek:',
            kidsSuggestions: ['Gyerek multivitamin', 'D-vitamin cseppek'],
            digText: 'Az emésztőrendszer egészségéért:',
            digSuggestions: ['Probiotikumok', 'Emésztő enzimek'],
            jointsText: 'Ízületeknek és csontoknak:',
            jointsSuggestions: ['Kollagén', 'Kalcium + D3'],
            sleepText: 'Relaxációhoz és pihentető alváshoz:',
            sleepSuggestions: ['Magnézium', 'Macskagyökér'],
            prostText: 'Prosztatagészség termékek:',
            prostSuggestions: ['Cink', 'Szelén'],
            eyesText: 'A szemek egészségéért:',
            eyesSuggestions: ['Omega 3', 'A-vitamin'],
            slimText: 'Termékek az egészséges fogyáshoz:',
            slimSuggestions: ['Slim Lady', 'Glükomannán'],
            priceText: 'Az árak minden terméknél feltüntetésre kerülnek. Mondja meg a termék nevét és megadom a pontos árat!',
            priceSuggestions: ['C-vitamin ára', 'Omega 3 ára', 'Magnézium ára'],
            deliveryText: 'A Patricecom egész Romániában szállít:<br><br><strong>Standard</strong> - 2-4 nap, 15.99 Lei<br><strong>Expressz</strong> - 1-2 nap, 29.99 Lei<br><br>Ingyenes szállítás 200 Lei feletti rendelésnél!',
            deliverySuggestions: ['Hogyan rendelek?', 'Fizetési módok'],
            paymentText: 'Elfogadott fizetési módok:<br><br><strong>Utánvét</strong><br><strong>Bankkártya</strong> (Visa, Mastercard)<br><strong>Banki átutalás</strong>',
            paymentSuggestions: ['Szállítási info', 'Visszaküldési szabályzat'],
            returnText: '30 napon belül ingyenes visszaküldés. A termékeknek eredeti csomagolásban kell lenniük. Írjon nekünk: <strong>contact@patricecom.ro</strong>.',
            returnSuggestions: ['Kapcsolat', 'Szállítás'],
            brandText: (b) => `Termékek a <strong>${b}</strong> márkától:`,
            brandSuggestions: ['Összes termék megtekintése', 'Akciós ajánlatok'],
            foundText: (n, q) => `${n} terméket találtam a "<strong>${q}</strong>" keresésre:`,
            foundSuggestions: ['Másik termék keresése', 'Összes termék'],
            notFoundText: (q) => `Nem találtam eredményt a "<strong>${q}</strong>" keresésre. Próbáljon terméknév vagy kategória szerint keresni.`,
            notFoundSuggestions: ['Vitaminok', 'Immunerősítők', 'Akciók', 'Szállítási info'],
        },
        de: {
            title: 'Patricecom Assistent',
            status: 'Online - Suchen Sie beliebige Produkte',
            placeholder: 'Nachricht schreiben...',
            sendTitle: 'Senden',
            welcome: 'Guten Tag! Ich bin der virtuelle Assistent von Patricecom. Ich kann Ihnen helfen, Produkte zu finden, Lieferinformationen zu geben oder personalisierte Empfehlungen zu machen.',
            welcomeSuggestions: ['Vitamine', 'Immunprodukte', 'Sonderangebote'],
            greet: 'Hallo! Ich bin der Patricecom Assistent. Wie kann ich helfen? Suchen Sie ein Produkt oder möchten Sie eine Empfehlung?',
            greetSuggestions: ['Vitamine suchen', 'Immunprodukte', 'Welche Angebote gibt es?'],
            offersText: (n) => `<strong>${n}</strong> Produkte mit Sonderangeboten gefunden!`,
            offersSuggestions: ['Mehr Angebote', 'Alle in den Warenkorb'],
            immunText: 'Für die Immunität empfehle ich Vitamin C, Zink und Propolis:',
            immunSuggestions: ['Vitamin C', 'Zink', 'Produkte für Kinder'],
            vitCText: 'Unser Vitamin C Sortiment:',
            vitDText: 'Vitamin D - essentiell für Knochen und Immunität:',
            vitBText: 'B-Vitamine - für Stoffwechsel und Nervensystem:',
            vitText: 'Wir haben ein breites Vitaminsortiment:',
            vitSuggestions: ['Vitamin C', 'Vitamin D', 'Multivitamine'],
            magText: 'Magnesium - für Muskeln, Nerven und Müdigkeitsreduktion:',
            magSuggestions: ['Zink', 'Kalzium'],
            omegaText: 'Omega 3 - für Herz, Gehirn und Sehvermögen:',
            omegaSuggestions: ['Coenzym Q10', 'Lecithin'],
            colText: 'Schönheitsprodukte - Kollagen und Hyaluronsäure:',
            colSuggestions: ['Hair Caps', 'Hyaluron Forte'],
            kidsText: 'Spezielle Produkte für Kinder:',
            kidsSuggestions: ['Kinder-Multivitamine', 'Vitamin D Tropfen'],
            digText: 'Für die Verdauungsgesundheit:',
            digSuggestions: ['Probiotika', 'Verdauungsenzyme'],
            jointsText: 'Für Gelenke und Knochen:',
            jointsSuggestions: ['Kollagen', 'Kalzium + D3'],
            sleepText: 'Für Entspannung und erholsamen Schlaf:',
            sleepSuggestions: ['Magnesium', 'Baldrian'],
            prostText: 'Produkte für die Prostatagesundheit:',
            prostSuggestions: ['Zink', 'Selen'],
            eyesText: 'Für die Augengesundheit:',
            eyesSuggestions: ['Omega 3', 'Vitamin A'],
            slimText: 'Produkte für ein gesundes Abnehmprogramm:',
            slimSuggestions: ['Slim Lady', 'Glucomannan'],
            priceText: 'Preise sind bei jedem Produkt angegeben. Nennen Sie mir den Produktnamen und ich gebe Ihnen den genauen Preis!',
            priceSuggestions: ['Vitamin C Preis', 'Omega 3 Preis', 'Magnesium Preis'],
            deliveryText: 'Patricecom liefert in ganz Rumänien:<br><br><strong>Standard</strong> - 2-4 Tage, 15,99 Lei<br><strong>Express</strong> - 1-2 Tage, 29,99 Lei<br><br>Kostenlose Lieferung ab 200 Lei!',
            deliverySuggestions: ['Wie bestelle ich?', 'Zahlungsmethoden'],
            paymentText: 'Akzeptierte Zahlungsmethoden:<br><br><strong>Nachnahme</strong><br><strong>Bankkarte</strong> (Visa, Mastercard)<br><strong>Banküberweisung</strong>',
            paymentSuggestions: ['Lieferinfo', 'Rückgaberichtlinie'],
            returnText: 'Kostenlose Rücksendung innerhalb von 30 Tagen. Produkte müssen in der Originalverpackung sein. Kontaktieren Sie uns: <strong>contact@patricecom.ro</strong>.',
            returnSuggestions: ['Kontakt', 'Lieferung'],
            brandText: (b) => `Produkte von <strong>${b}</strong>:`,
            brandSuggestions: ['Alle Produkte ansehen', 'Sonderangebote'],
            foundText: (n, q) => `${n} ${n === 1 ? 'Produkt' : 'Produkte'} für "<strong>${q}</strong>" gefunden:`,
            foundSuggestions: ['Anderes Produkt suchen', 'Alle Produkte'],
            notFoundText: (q) => `Keine Ergebnisse für "<strong>${q}</strong>" gefunden. Suchen Sie nach Produktname oder Kategorie.`,
            notFoundSuggestions: ['Vitamine', 'Immunität', 'Sonderangebote', 'Lieferinfo'],
        }
    };

    function getLang() {
        return aiLang[window.currentLang] || aiLang.ro;
    }

    // Update chatbot UI text when language changes
    function updateChatbotUI() {
        const t = getLang();
        const titleEl = aiAssistant.querySelector('.ai-header-info h3');
        const statusEl = aiAssistant.querySelector('.ai-status');
        if (titleEl) titleEl.textContent = t.title;
        if (statusEl) statusEl.textContent = t.status;
        if (aiInput) aiInput.placeholder = t.placeholder;
        if (aiSend) aiSend.title = t.sendTitle;
    }

    // Listen for language changes
    document.addEventListener('langChanged', updateChatbotUI);
    updateChatbotUI();

    // Toggle assistant via FAB
    aiFab.addEventListener('click', () => {
        aiAssistant.classList.toggle('active');
        aiFab.classList.toggle('hidden');
        if (aiAssistant.classList.contains('active')) {
            setTimeout(() => aiInput.focus(), 300);
            // Show welcome if no messages yet
            if (aiMessages.children.length === 0) {
                const t = getLang();
                addMessage(t.welcome, 'bot', [], t.welcomeSuggestions);
            }
        }
    });

    aiClose.addEventListener('click', () => {
        aiAssistant.classList.remove('active');
        aiFab.classList.remove('hidden');
    });

    // Suggestion buttons
    document.addEventListener('click', (e) => {
        if (e.target.classList.contains('ai-suggestion')) {
            const query = e.target.getAttribute('data-query');
            handleUserMessage(query);
        }
        if (e.target.closest('.ai-product-add')) {
            const id = parseInt(e.target.closest('.ai-product-add').getAttribute('data-id'));
            if (id && window.addToCart) window.addToCart(id);
        }
        if (e.target.closest('.ai-product-card') && !e.target.closest('.ai-product-add')) {
            const id = parseInt(e.target.closest('.ai-product-card').getAttribute('data-id'));
            if (id && window.viewProduct) window.viewProduct(id);
        }
    });

    // Send message
    aiSend.addEventListener('click', sendMessage);
    aiInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') sendMessage();
    });

    function sendMessage() {
        const text = aiInput.value.trim();
        if (!text) return;
        handleUserMessage(text);
        aiInput.value = '';
    }

    function handleUserMessage(text) {
        addMessage(text, 'user');
        showTyping();
        setTimeout(() => {
            removeTyping();
            const response = generateResponse(text);
            addMessage(response.text, 'bot', response.products, response.suggestions);
        }, 600 + Math.random() * 500);
    }

    function addMessage(text, sender, products = [], suggestions = []) {
        const msg = document.createElement('div');
        msg.className = `ai-message ${sender}`;

        let content = `<p>${text}</p>`;

        if (products.length > 0) {
            content += products.map(p => {
                const colors = getProductColor(p.name);
                const icon = getCategoryIcon(p.name);
                return `
                    <div class="ai-product-card" data-id="${p.id}">
                        <div class="ai-product-icon" style="background:${colors.bg}; overflow:hidden; border-radius:8px">
                            ${window.getProductImage ? `<img src="${window.getProductImage(p)}" alt="" style="width:100%;height:100%;object-fit:contain;"/>` : `<i class="${icon}" style="color:${colors.color}"></i>`}
                        </div>
                        <div class="ai-product-info">
                            <strong>${p.name}</strong>
                            <span>${p.brand} - ${p.quantity}</span>
                        </div>
                        ${p.price ? `<span class="ai-product-price">${p.price.toFixed(2)} Lei</span>` : ''}
                        ${p.price ? `<button class="ai-product-add" data-id="${p.id}" title="Add to cart"><i class="fas fa-plus"></i></button>` : ''}
                    </div>
                `;
            }).join('');
        }

        if (suggestions.length > 0) {
            content += `<div class="ai-suggestions">
                ${suggestions.map(s => `<button class="ai-suggestion" data-query="${s}">${s}</button>`).join('')}
            </div>`;
        }

        msg.innerHTML = `
            <div class="ai-message-avatar">
                <i class="fas fa-${sender === 'bot' ? 'robot' : 'user'}"></i>
            </div>
            <div class="ai-message-content">${content}</div>
        `;

        aiMessages.appendChild(msg);
        aiMessages.scrollTop = aiMessages.scrollHeight;
    }

    function showTyping() {
        const typing = document.createElement('div');
        typing.className = 'ai-message bot';
        typing.id = 'aiTyping';
        typing.innerHTML = `
            <div class="ai-message-avatar"><i class="fas fa-robot"></i></div>
            <div class="ai-message-content">
                <div class="ai-typing"><span></span><span></span><span></span></div>
            </div>
        `;
        aiMessages.appendChild(typing);
        aiMessages.scrollTop = aiMessages.scrollHeight;
    }

    function removeTyping() {
        const typing = document.getElementById('aiTyping');
        if (typing) typing.remove();
    }

    // AI Response logic
    function generateResponse(query) {
        const q = query.toLowerCase().trim();
        const products = window.allProducts || [];
        const t = getLang();

        // Greetings (all languages)
        if (/^(buna|salut|hello|hi|hey|ciao|hallo|szia|servus|guten|bonjour)/.test(q)) {
            return { text: t.greet, products: [], suggestions: t.greetSuggestions };
        }

        // Offers
        if (/ofert|promotii|reduceri|discount|offer|sale|akci|angebot|sonder/.test(q)) {
            const offers = products.filter(p => p.offer).slice(0, 5);
            return { text: t.offersText(products.filter(p => p.offer).length), products: offers, suggestions: t.offersSuggestions };
        }

        // Immunity
        if (/imunit|raceala|gripa|imun|immun|immunity|immunitat/.test(q)) {
            const immun = products.filter(p => {
                const n = p.name.toLowerCase();
                return n.includes('imuno') || n.includes('vitamin c') || n.includes('zinc') ||
                       n.includes('propolis') || n.includes('echinac') || n.includes('gripovit');
            }).slice(0, 5);
            return { text: t.immunText, products: immun, suggestions: t.immunSuggestions };
        }

        // Vitamins
        if (/vitamin|vitamine|vitamina/.test(q)) {
            let vitamins;
            if (/vitamin.*c|\bc\b.*vitamin/.test(q)) {
                vitamins = products.filter(p => /vitamin.{0,2}c/i.test(p.name)).slice(0, 5);
                return { text: t.vitCText, products: vitamins, suggestions: t.vitSuggestions };
            }
            if (/vitamin.*d|\bd\b.*vitamin/.test(q)) {
                vitamins = products.filter(p => /vitamin.{0,2}d/i.test(p.name)).slice(0, 5);
                return { text: t.vitDText, products: vitamins, suggestions: t.vitSuggestions };
            }
            if (/vitamin.*b|\bb\b.*vitamin/.test(q)) {
                vitamins = products.filter(p => /vitamin[a]?\s*b/i.test(p.name)).slice(0, 5);
                return { text: t.vitBText, products: vitamins, suggestions: t.vitSuggestions };
            }
            vitamins = products.filter(p => /vitamin|multivitamin/i.test(p.name)).slice(0, 5);
            return { text: t.vitText, products: vitamins, suggestions: t.vitSuggestions };
        }

        // Magnesium
        if (/magneziu|magnesium|magnez|magnézium/.test(q)) {
            const mag = products.filter(p => /magneziu|maximag/i.test(p.name)).slice(0, 5);
            return { text: t.magText, products: mag, suggestions: t.magSuggestions };
        }

        // Omega
        if (/omega|ulei de peste|fish oil|fischöl/.test(q)) {
            const omega = products.filter(p => /omega|ulei de krill/i.test(p.name)).slice(0, 5);
            return { text: t.omegaText, products: omega, suggestions: t.omegaSuggestions };
        }

        // Collagen / Beauty
        if (/colagen|collagen|piele|riduri|hialuron|beauty|schönheit/.test(q)) {
            const col = products.filter(p => /collagen|colagen|hialuron|hair/i.test(p.name)).slice(0, 5);
            return { text: t.colText, products: col, suggestions: t.colSuggestions };
        }

        // Kids
        if (/copii|copil|bebelus|junior|kid|kinder|gyerek/.test(q)) {
            const kids = products.filter(p => /copii|kid|junior|baby/i.test(p.name)).slice(0, 5);
            return { text: t.kidsText, products: kids, suggestions: t.kidsSuggestions };
        }

        // Digestion
        if (/digestie|stomac|intestin|probiotic|verdauung|emésztés/.test(q)) {
            const dig = products.filter(p => /probiotic|digestiv|enzim|lactaz|pelin/i.test(p.name)).slice(0, 5);
            return { text: t.digText, products: dig, suggestions: t.digSuggestions };
        }

        // Joints
        if (/articulat|genunchi|oase|glucozamin|gelenk|ízület/.test(q)) {
            const joints = products.filter(p => /glucozamin|condroitin|collagen|calciu/i.test(p.name)).slice(0, 5);
            return { text: t.jointsText, products: joints, suggestions: t.jointsSuggestions };
        }

        // Sleep / Stress
        if (/somn|stres|anxietate|relaxare|calm|sleep|stress|schlaf|alvás/.test(q)) {
            const sleep = products.filter(p => /valeriana|harmony|antistres|magneziu/i.test(p.name)).slice(0, 5);
            return { text: t.sleepText, products: sleep, suggestions: t.sleepSuggestions };
        }

        // Prostate
        if (/prostat|barbati|männer|prosztat/.test(q)) {
            const prost = products.filter(p => /prosta/i.test(p.name)).slice(0, 5);
            return { text: t.prostText, products: prost, suggestions: t.prostSuggestions };
        }

        // Eyes
        if (/ochi|vedere|lutein|auge|szem/.test(q)) {
            const eyes = products.filter(p => /lutein|opti|afin/i.test(p.name)).slice(0, 5);
            return { text: t.eyesText, products: eyes, suggestions: t.eyesSuggestions };
        }

        // Slimming
        if (/slab|diet|greutate|slim|kilo|abnehm|fogyás/.test(q)) {
            const slim = products.filter(p => /slim|slabit|glucomanan|cafea verde|apuretin/i.test(p.name)).slice(0, 5);
            return { text: t.slimText, products: slim, suggestions: t.slimSuggestions };
        }

        // Price
        if (/pret|costa|cat |price|kosten|ár/.test(q)) {
            return { text: t.priceText, products: [], suggestions: t.priceSuggestions };
        }

        // Delivery
        if (/livr|transport|curier|deliver|versand|szállít/.test(q)) {
            return { text: t.deliveryText, products: [], suggestions: t.deliverySuggestions };
        }

        // Payment
        if (/plata|plat|card|ramburs|payment|zahlung|fizetés/.test(q)) {
            return { text: t.paymentText, products: [], suggestions: t.paymentSuggestions };
        }

        // Return
        if (/retur|return|schimb|rückgabe|visszaküld/.test(q)) {
            return { text: t.returnText, products: [], suggestions: t.returnSuggestions };
        }

        // Brand search
        const brands = ['jutavit', 'hofigal', 'larix', 'zdrovit', 'bioeel', 'fares', 'medica'];
        const brandMatch = brands.find(b => q.includes(b));
        if (brandMatch) {
            const brandProducts = products.filter(p => p.brand.toLowerCase() === brandMatch).slice(0, 5);
            return {
                text: t.brandText(brandMatch.charAt(0).toUpperCase() + brandMatch.slice(1)),
                products: brandProducts,
                suggestions: t.brandSuggestions
            };
        }

        // General search
        const searchResults = products.filter(p =>
            p.name.toLowerCase().includes(q) ||
            q.split(' ').every(word => p.name.toLowerCase().includes(word))
        ).slice(0, 5);

        if (searchResults.length > 0) {
            return { text: t.foundText(searchResults.length, query), products: searchResults, suggestions: t.foundSuggestions };
        }

        return { text: t.notFoundText(query), products: [], suggestions: t.notFoundSuggestions };
    }
})();
