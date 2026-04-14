/* =============================================
   JUTAVIT ROMANIA - AI Assistant (JutaBot)
   ============================================= */

(function() {
    const aiToggle = document.getElementById('aiToggle');
    const aiAssistant = document.getElementById('aiAssistant');
    const aiClose = document.getElementById('aiClose');
    const aiInput = document.getElementById('aiInput');
    const aiSend = document.getElementById('aiSend');
    const aiMessages = document.getElementById('aiMessages');

    // Toggle assistant
    aiToggle.addEventListener('click', () => {
        aiAssistant.classList.toggle('active');
        if (aiAssistant.classList.contains('active')) {
            setTimeout(() => aiInput.focus(), 300);
        }
    });

    aiClose.addEventListener('click', () => {
        aiAssistant.classList.remove('active');
    });

    // Suggestion buttons
    document.addEventListener('click', (e) => {
        if (e.target.classList.contains('ai-suggestion')) {
            const query = e.target.getAttribute('data-query');
            handleUserMessage(query);
        }
        if (e.target.closest('.ai-product-add')) {
            const id = parseInt(e.target.closest('.ai-product-add').getAttribute('data-id'));
            if (id && window.addToCart) {
                window.addToCart(id);
            }
        }
        if (e.target.closest('.ai-product-card') && !e.target.closest('.ai-product-add')) {
            const id = parseInt(e.target.closest('.ai-product-card').getAttribute('data-id'));
            if (id && window.viewProduct) {
                window.viewProduct(id);
            }
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
        }, 800 + Math.random() * 700);
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
                        ${p.price ? `<button class="ai-product-add" data-id="${p.id}" title="Adauga in cos"><i class="fas fa-plus"></i></button>` : ''}
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
                <div class="ai-typing">
                    <span></span><span></span><span></span>
                </div>
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

        // Greetings
        if (/^(buna|salut|hello|hi|hey|ciao)/.test(q)) {
            return {
                text: 'Buna! Ma bucur sa te vad. Cu ce te pot ajuta astazi? Cauti un produs anume sau vrei o recomandare?',
                products: [],
                suggestions: ['Cauta vitamine', 'Produse pentru imunitate', 'Care sunt ofertele?']
            };
        }

        // Offers
        if (q.includes('ofert') || q.includes('promotii') || q.includes('reduceri') || q.includes('discount')) {
            const offers = products.filter(p => p.offer).slice(0, 5);
            return {
                text: `Am gasit <strong>${products.filter(p => p.offer).length}</strong> produse cu oferte speciale! Iata cateva dintre ele:`,
                products: offers,
                suggestions: ['Mai multe oferte', 'Adauga toate in cos']
            };
        }

        // Immunity
        if (q.includes('imunit') || q.includes('raceala') || q.includes('gripa') || q.includes('imun')) {
            const immun = products.filter(p => {
                const n = p.name.toLowerCase();
                return n.includes('imuno') || n.includes('vitamin c') || n.includes('zinc') ||
                       n.includes('propolis') || n.includes('echinac') || n.includes('gripovit');
            }).slice(0, 5);
            return {
                text: 'Pentru intarirea sistemului imunitar, iti recomand urmatoarele produse. Vitamina C, Zinc-ul si Propolis-ul sunt esentiale pentru imunitate:',
                products: immun,
                suggestions: ['Vitamina C', 'Zinc', 'Produse pentru copii']
            };
        }

        // Vitamins
        if (q.includes('vitamin')) {
            let vitamins;
            if (q.includes('c')) {
                vitamins = products.filter(p => p.name.toLowerCase().includes('vitamina c') || p.name.toLowerCase().includes('vitamin c')).slice(0, 5);
                return { text: 'Iata gama noastra de Vitamina C - esentiala pentru imunitate si sanatate:', products: vitamins, suggestions: ['Vitamina D', 'Multivitamine'] };
            }
            if (q.includes('d')) {
                vitamins = products.filter(p => p.name.toLowerCase().includes('vitamina d') || p.name.toLowerCase().includes('vitamin d')).slice(0, 5);
                return { text: 'Vitamina D este esentiala pentru oase, dinti si imunitate. Iata optiunile noastre:', products: vitamins, suggestions: ['Vitamina C', 'Calciu + D3'] };
            }
            if (q.includes('b')) {
                vitamins = products.filter(p => /vitamin[a]?\s*b/i.test(p.name)).slice(0, 5);
                return { text: 'Vitaminele din grupa B sunt esentiale pentru metabolism si sistem nervos:', products: vitamins, suggestions: ['B Complex', 'Magneziu'] };
            }
            vitamins = products.filter(p => p.name.toLowerCase().includes('vitamin') || p.name.toLowerCase().includes('multivitamin')).slice(0, 5);
            return { text: 'Avem o gama variata de vitamine. Ce tip de vitamina te intereseaza?', products: vitamins, suggestions: ['Vitamina C', 'Vitamina D', 'Multivitamine'] };
        }

        // Magnesium
        if (q.includes('magneziu')) {
            const mag = products.filter(p => p.name.toLowerCase().includes('magneziu') || p.name.toLowerCase().includes('maximag')).slice(0, 5);
            return { text: 'Magneziul este important pentru muschi, sistem nervos si reducerea oboselii. Iata optiunile noastre:', products: mag, suggestions: ['Zinc', 'Calciu'] };
        }

        // Omega
        if (q.includes('omega') || q.includes('ulei de peste')) {
            const omega = products.filter(p => p.name.toLowerCase().includes('omega') || p.name.toLowerCase().includes('ulei de krill')).slice(0, 5);
            return { text: 'Acizii grasi Omega 3 sunt esentiali pentru inima, creier si vederea normala:', products: omega, suggestions: ['Coenzima Q10', 'Lecitina'] };
        }

        // Collagen
        if (q.includes('colagen') || q.includes('collagen') || q.includes('piele') || q.includes('riduri')) {
            const col = products.filter(p => {
                const n = p.name.toLowerCase();
                return n.includes('collagen') || n.includes('colagen') || n.includes('hialuron') || n.includes('hair');
            }).slice(0, 5);
            return { text: 'Pentru frumusetea si sanatatea pielii, iti recomand produsele noastre cu colagen si acid hialuronic:', products: col, suggestions: ['Hair Caps', 'Hialuron Forte'] };
        }

        // Kids
        if (q.includes('copii') || q.includes('copil') || q.includes('bebelus') || q.includes('junior')) {
            const kids = products.filter(p => {
                const n = p.name.toLowerCase();
                return n.includes('copii') || n.includes('kid') || n.includes('junior') || n.includes('baby');
            }).slice(0, 5);
            return { text: 'Avem o gama speciala de produse pentru cei mici, formulate special pentru nevoile lor:', products: kids, suggestions: ['Multivitamine copii', 'Vitamina D picaturi'] };
        }

        // Digestion
        if (q.includes('digestie') || q.includes('stomac') || q.includes('intestin') || q.includes('probiotic')) {
            const dig = products.filter(p => {
                const n = p.name.toLowerCase();
                return n.includes('probiotic') || n.includes('digestiv') || n.includes('enzim') || n.includes('lactaz') || n.includes('pelin');
            }).slice(0, 5);
            return { text: 'Pentru sanatatea digestiva, iti recomand urmatoarele produse:', products: dig, suggestions: ['Probiotice', 'Enzime digestive'] };
        }

        // Joints
        if (q.includes('articulat') || q.includes('genunchi') || q.includes('oase') || q.includes('glucozamin')) {
            const joints = products.filter(p => {
                const n = p.name.toLowerCase();
                return n.includes('glucozamin') || n.includes('condroitin') || n.includes('collagen') || n.includes('calciu');
            }).slice(0, 5);
            return { text: 'Pentru sanatatea articulatiilor si oaselor, iti recomand:', products: joints, suggestions: ['Colagen', 'Calciu + D3'] };
        }

        // Sleep / Stress
        if (q.includes('somn') || q.includes('stres') || q.includes('anxietate') || q.includes('relaxare') || q.includes('calm')) {
            const sleep = products.filter(p => {
                const n = p.name.toLowerCase();
                return n.includes('valeriana') || n.includes('harmony') || n.includes('antistres') || n.includes('magneziu');
            }).slice(0, 5);
            return { text: 'Pentru relaxare si un somn odihnitor, iti recomand:', products: sleep, suggestions: ['Magneziu', 'Valeriana'] };
        }

        // Prostate
        if (q.includes('prostat') || q.includes('barbati')) {
            const prost = products.filter(p => p.name.toLowerCase().includes('prosta')).slice(0, 5);
            return { text: 'Pentru sanatatea prostatei, avem urmatoarele produse specializate:', products: prost, suggestions: ['Zinc', 'Seleniu'] };
        }

        // Eyes
        if (q.includes('ochi') || q.includes('vedere') || q.includes('lutein')) {
            const eyes = products.filter(p => {
                const n = p.name.toLowerCase();
                return n.includes('lutein') || n.includes('opti') || n.includes('afin');
            }).slice(0, 5);
            return { text: 'Pentru sanatatea ochilor si mentinerea vederii normale:', products: eyes, suggestions: ['Omega 3', 'Vitamina A'] };
        }

        // Slimming
        if (q.includes('slab') || q.includes('diet') || q.includes('greutate') || q.includes('slim') || q.includes('kilo')) {
            const slim = products.filter(p => {
                const n = p.name.toLowerCase();
                return n.includes('slim') || n.includes('slabit') || n.includes('glucomanan') || n.includes('cafea verde') || n.includes('apuretin');
            }).slice(0, 5);
            return { text: 'Pentru sustinerea unui program de slabire sanatos, iti recomand:', products: slim, suggestions: ['Slim Lady', 'Glucomanan'] };
        }

        // Price inquiry
        if (q.includes('pret') || q.includes('costa') || q.includes('cat')) {
            return {
                text: 'Poti vedea preturile tuturor produselor in <a href="#shop" style="color:var(--primary); font-weight:600">sectiunea Magazine</a>. Spune-mi numele produsului si iti dau pretul exact!',
                products: [],
                suggestions: ['Vitamina C pret', 'Omega 3 pret', 'Magneziu pret']
            };
        }

        // Delivery
        if (q.includes('livr') || q.includes('transport') || q.includes('curier')) {
            return {
                text: 'Oferim doua optiuni de livrare:<br><br><strong>Livrare Standard</strong> - 2-4 zile lucratoare, 15.99 Lei<br><strong>Livrare Express</strong> - 1-2 zile lucratoare, 29.99 Lei<br><br>Livrarea este gratuita pentru comenzi peste 200 Lei!',
                products: [],
                suggestions: ['Cum plasez o comanda?', 'Metode de plata']
            };
        }

        // Payment
        if (q.includes('plata') || q.includes('plat') || q.includes('card') || q.includes('ramburs')) {
            return {
                text: 'Acceptam urmatoarele metode de plata:<br><br><strong>Card Bancar</strong> - Visa, Mastercard (securizat)<br><strong>Ramburs la Curier</strong> - platesti cand primesti coletul<br><strong>Transfer Bancar</strong> - in contul nostru bancar',
                products: [],
                suggestions: ['Informatii livrare', 'Politica de retur']
            };
        }

        // Return
        if (q.includes('retur') || q.includes('return') || q.includes('schimb')) {
            return {
                text: 'Oferim retur gratuit in 30 de zile de la primire. Produsele trebuie sa fie in ambalajul original, neschimbate. Contacteaza-ne la <strong>contact@jutavit.ro</strong> pentru a initia un retur.',
                products: [],
                suggestions: ['Contact', 'Livrare']
            };
        }

        // Brand search
        const brands = ['jutavit', 'medica', 'zdrovit', 'cosmopharm', 'dacia plant', 'bioeel'];
        const brandMatch = brands.find(b => q.includes(b));
        if (brandMatch) {
            const brandProducts = products.filter(p => p.brand.toLowerCase() === brandMatch).slice(0, 5);
            return {
                text: `Iata produsele disponibile de la <strong>${brandMatch.charAt(0).toUpperCase() + brandMatch.slice(1)}</strong>:`,
                products: brandProducts,
                suggestions: ['Vezi toate produsele', 'Oferte speciale']
            };
        }

        // General product search
        const searchResults = products.filter(p =>
            p.name.toLowerCase().includes(q) ||
            q.split(' ').every(word => p.name.toLowerCase().includes(word))
        ).slice(0, 5);

        if (searchResults.length > 0) {
            return {
                text: `Am gasit ${searchResults.length} ${searchResults.length === 1 ? 'produs' : 'produse'} pentru "<strong>${query}</strong>":`,
                products: searchResults,
                suggestions: ['Cauta alt produs', 'Vezi toate produsele']
            };
        }

        // Default / not found
        return {
            text: `Nu am gasit rezultate pentru "<strong>${query}</strong>". Incearca sa cauti dupa numele produsului, vitamina sau categorie. Te pot ajuta cu orice intrebare!`,
            products: [],
            suggestions: ['Vitamine', 'Imunitate', 'Oferte speciale', 'Informatii livrare']
        };
    }
})();
