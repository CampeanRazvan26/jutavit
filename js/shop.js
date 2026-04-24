/* =============================================
   PATRICECOM - Shop & Cart Logic
   ============================================= */

(function() {
    let cart = JSON.parse(localStorage.getItem('patricecom_cart') || '[]');
    let currentCategory = 'all';
    let currentSubcategory = 'all';
    let currentSort = 'name-asc';
    let displayedCount = 0;
    const ITEMS_PER_PAGE = 24;
    let filteredProducts = [];

    function initShop() {
        if (!window.allProducts || !window.allProducts.length) {
            setTimeout(initShop, 100);
            return;
        }

        filteredProducts = [...window.allProducts];
        displayedCount = 0;

        renderSubcatFilters();
        renderProducts();
        setupSort();
        setupViewToggle();
        setupCart();
        setupLoadMore();
        updateCartUI();
    }

    // Called from app.js when a top-level category is chosen
    window.filterByCategory = function(category) {
        currentCategory = category;
        currentSubcategory = 'all';
        renderSubcatFilters();
        applyFilters();
    };

    // Called from app.js when a subcategory is clicked (mega menu or sidebar)
    window.filterBySubcategory = function(category, subcategory) {
        currentCategory = category;
        currentSubcategory = subcategory;

        // Sync cat-nav active state
        document.querySelectorAll('.cat-nav-item').forEach(i => i.classList.remove('active'));
        const navItem = document.querySelector(`.cat-nav-item[data-cat="${category}"]`);
        if (navItem) navItem.classList.add('active');

        renderSubcatFilters();
        applyFilters();

        // Scroll to products on mobile/desktop
        const grid = document.getElementById('productsGrid');
        if (grid) grid.scrollIntoView({ behavior: 'smooth', block: 'start' });
    };

    function applyFilters() {
        let products = [...window.allProducts];

        if (currentCategory === 'oferte') {
            products = products.filter(p => p.offer);
        } else if (currentCategory !== 'all') {
            products = products.filter(p => p.category === currentCategory);
            if (currentSubcategory && currentSubcategory !== 'all') {
                products = products.filter(p => p.subcategory === currentSubcategory);
            }
        }

        filteredProducts = products;
        renderProducts(true);
        updateResultsHeader();
    }

    function updateResultsHeader() {
        const title = document.getElementById('resultsTitle');
        const count = document.getElementById('resultsCount');
        const loadMoreInfo = document.getElementById('loadMoreInfo');
        const lang = window.currentLang || 'ro';

        if (title) {
            if (currentCategory === 'all') {
                title.textContent = (window.translations && window.translations[lang] && window.translations[lang].resultsAll) || 'Toate Produsele';
            } else {
                const catMeta = window.productCategories && window.productCategories[currentCategory];
                let catLabel = catMeta ? (catMeta['name_' + lang] || catMeta.name_ro) : currentCategory;
                if (currentSubcategory && currentSubcategory !== 'all') {
                    catLabel += ' • ' + currentSubcategory;
                }
                title.textContent = catLabel;
            }
        }

        if (count) {
            const word = (window.translations && window.translations[lang] && window.translations[lang].resultsProducts) || 'produse';
            count.textContent = `${filteredProducts.length} ${word}`;
        }

        if (loadMoreInfo) {
            const sorted = sortProducts(filteredProducts, currentSort);
            const showing = Math.min(displayedCount, sorted.length);
            const ofWord = (window.translations && window.translations[lang] && window.translations[lang].loadMoreInfo) || 'din';
            const word = (window.translations && window.translations[lang] && window.translations[lang].resultsProducts) || 'produse';
            loadMoreInfo.textContent = `${showing} ${ofWord} ${sorted.length} ${word}`;
        }
    }

    // Render subcategory filters in the sidebar based on currentCategory
    function renderSubcatFilters() {
        const container = document.getElementById('subcatFilters');
        const titleEl = document.getElementById('sidebarSubcatTitle');
        if (!container) return;

        const lang = window.currentLang || 'ro';

        if (currentCategory === 'all' || currentCategory === 'oferte') {
            // Show list of all categories when on "Toate" or "Oferte"
            if (titleEl) {
                titleEl.innerHTML = `<i class="fas fa-th-large"></i> ${lang === 'en' ? 'Categories' : lang === 'hu' ? 'Kategoriak' : lang === 'de' ? 'Kategorien' : 'Categorii'}`;
            }
            const cats = Object.keys(window.productCategories || {});
            const totalCount = window.allProducts.length;
            let html = `
                <label class="subcat-filter ${currentSubcategory === 'all' ? 'active' : ''}" data-subcat="all">
                    <span class="subcat-name"><i class="fas fa-th"></i>${lang === 'en' ? 'All Products' : lang === 'hu' ? 'Osszes Termek' : lang === 'de' ? 'Alle Produkte' : 'Toate Produsele'}</span>
                    <span class="subcat-count">${totalCount}</span>
                </label>
            `;
            cats.forEach(catKey => {
                const meta = window.productCategories[catKey];
                const label = meta['name_' + lang] || meta.name_ro;
                const cnt = window.allProducts.filter(p => p.category === catKey).length;
                if (cnt === 0) return;
                html += `
                    <label class="subcat-filter" data-cat-link="${catKey}">
                        <span class="subcat-name"><i class="${(meta.icon && meta.icon.startsWith('fa-') ? 'fas ' + meta.icon : (meta.icon || 'fas fa-circle'))}"></i>${label}</span>
                        <span class="subcat-count">${cnt}</span>
                    </label>
                `;
            });
            container.innerHTML = html;

            container.querySelectorAll('.subcat-filter[data-cat-link]').forEach(el => {
                el.addEventListener('click', () => {
                    const catKey = el.getAttribute('data-cat-link');
                    document.querySelectorAll('.cat-nav-item').forEach(i => i.classList.remove('active'));
                    const navItem = document.querySelector(`.cat-nav-item[data-cat="${catKey}"]`);
                    if (navItem) navItem.classList.add('active');
                    window.filterByCategory(catKey);
                });
            });
            container.querySelector('.subcat-filter[data-subcat="all"]')?.addEventListener('click', () => {
                currentSubcategory = 'all';
                applyFilters();
                renderSubcatFilters();
            });
            return;
        }

        const catMeta = window.productCategories && window.productCategories[currentCategory];
        const catLabel = catMeta ? (catMeta['name_' + lang] || catMeta.name_ro) : currentCategory;
        if (titleEl) {
            const titleIcon = catMeta && catMeta.icon ? (catMeta.icon.startsWith('fa-') ? 'fas ' + catMeta.icon : catMeta.icon) : 'fas fa-layer-group';
            titleEl.innerHTML = `<i class="${titleIcon}"></i> ${catLabel}`;
        }

        const subs = (window.productSubcategories && window.productSubcategories[currentCategory]) || [];
        const catProducts = window.allProducts.filter(p => p.category === currentCategory);

        let html = `
            <label class="subcat-filter ${currentSubcategory === 'all' ? 'active' : ''}" data-subcat="all">
                <span class="subcat-name"><i class="fas fa-th"></i>${lang === 'en' ? 'All' : lang === 'hu' ? 'Osszes' : lang === 'de' ? 'Alle' : 'Toate'}</span>
                <span class="subcat-count">${catProducts.length}</span>
            </label>
        `;

        subs.forEach(sub => {
            const cnt = catProducts.filter(p => p.subcategory === sub).length;
            if (cnt === 0) return;
            html += `
                <label class="subcat-filter ${currentSubcategory === sub ? 'active' : ''}" data-subcat="${sub}">
                    <span class="subcat-name"><i class="fas fa-chevron-right"></i>${sub}</span>
                    <span class="subcat-count">${cnt}</span>
                </label>
            `;
        });

        if (!subs.length) {
            html += `<div class="subcat-filters-empty">${lang === 'en' ? 'No subcategories' : lang === 'hu' ? 'Nincsenek alkategoriak' : lang === 'de' ? 'Keine Unterkategorien' : 'Fara subcategorii'}</div>`;
        }

        container.innerHTML = html;

        container.querySelectorAll('.subcat-filter[data-subcat]').forEach(el => {
            el.addEventListener('click', () => {
                container.querySelectorAll('.subcat-filter').forEach(e => e.classList.remove('active'));
                el.classList.add('active');
                currentSubcategory = el.getAttribute('data-subcat');
                applyFilters();
            });
        });
    }

    // Re-render sidebar on language change
    document.addEventListener('langChanged', () => {
        renderSubcatFilters();
        updateResultsHeader();
    });

    // Render products
    function renderProducts(reset = true) {
        const grid = document.getElementById('productsGrid');
        if (!grid) return;

        if (reset) {
            grid.innerHTML = '';
            displayedCount = 0;
        }

        const sorted = sortProducts(filteredProducts, currentSort);
        const batch = sorted.slice(displayedCount, displayedCount + ITEMS_PER_PAGE);

        batch.forEach((product, i) => {
            const card = createProductCard(product);
            card.style.animationDelay = `${i * 0.03}s`;
            grid.appendChild(card);
        });

        displayedCount += batch.length;

        const loadMore = document.getElementById('loadMore');
        if (loadMore) {
            loadMore.style.display = displayedCount >= sorted.length ? 'none' : 'inline-flex';
        }

        updateResultsHeader();
    }

    function createProductCard(product) {
        const colors = getProductColor(product.name);
        const icon = getCategoryIcon(product.name);
        const inCart = cart.find(c => c.id === product.id);

        const card = document.createElement('div');
        card.className = 'product-card';
        card.style.animation = 'fadeInUp 0.4s ease forwards';
        card.style.opacity = '0';

        const badges = [];
        if (product.offer) badges.push(`<span class="badge badge-offer">${product.offer}</span>`);
        if (product.id % 17 === 0) badges.push('<span class="badge badge-new">Nou</span>');
        if (product.id % 23 === 0) badges.push('<span class="badge badge-popular">Popular</span>');

        card.innerHTML = `
            ${badges.length ? `<div class="product-badge">${badges.join('')}</div>` : ''}
            <div class="product-image" onclick="viewProduct(${product.id})">
                <div class="product-image-bg" style="background:${colors.bg}">
                    ${window.getProductImage ? `<img src="${window.getProductImage(product)}" alt="${product.name}" style="width:100%;height:100%;object-fit:contain;" loading="lazy"/>` : `<i class="${icon}" style="color:${colors.color}"></i>`}
                </div>
                <div class="product-quick-actions">
                    <button class="quick-action-btn" onclick="event.stopPropagation(); viewProduct(${product.id})" title="Detalii">
                        <i class="fas fa-eye"></i>
                    </button>
                    ${product.price ? `
                    <button class="quick-action-btn" onclick="event.stopPropagation(); addToCart(${product.id})" title="Adauga in cos">
                        <i class="fas fa-cart-plus"></i>
                    </button>` : ''}
                </div>
            </div>
            <div class="product-info">
                <span class="product-brand">${product.brand}</span>
                <h3 class="product-name">${product.name}</h3>
                <span class="product-quantity">${product.quantity}</span>
                <div class="product-footer">
                    ${product.price
                        ? `<span class="product-price">${product.price.toFixed(2)} <span class="currency">Lei</span></span>`
                        : '<span class="product-price-unavailable">Pret la cerere</span>'
                    }
                    ${product.price ? `
                    <button class="add-to-cart-btn ${inCart ? 'added' : ''}" onclick="addToCart(${product.id})" title="Adauga in cos">
                        <i class="fas fa-${inCart ? 'check' : 'plus'}"></i>
                    </button>` : ''}
                </div>
            </div>
        `;

        return card;
    }

    function sortProducts(products, sort) {
        const sorted = [...products];
        switch(sort) {
            case 'name-asc': return sorted.sort((a, b) => a.name.localeCompare(b.name, 'ro'));
            case 'name-desc': return sorted.sort((a, b) => b.name.localeCompare(a.name, 'ro'));
            case 'price-asc': return sorted.sort((a, b) => (a.price || 999) - (b.price || 999));
            case 'price-desc': return sorted.sort((a, b) => (b.price || 0) - (a.price || 0));
            default: return sorted;
        }
    }

    function setupSort() {
        const sortSelect = document.getElementById('sortSelect');
        if (sortSelect) {
            sortSelect.addEventListener('change', (e) => {
                currentSort = e.target.value;
                renderProducts(true);
            });
        }
    }

    function setupLoadMore() {
        const loadMore = document.getElementById('loadMore');
        if (loadMore) {
            loadMore.addEventListener('click', () => renderProducts(false));
        }
    }

    function setupViewToggle() {
        const gridBtn = document.getElementById('gridViewBtn');
        const listBtn = document.getElementById('listViewBtn');
        const grid = document.getElementById('productsGrid');

        if (gridBtn && listBtn && grid) {
            gridBtn.addEventListener('click', () => {
                grid.classList.remove('list-view');
                gridBtn.classList.add('active');
                listBtn.classList.remove('active');
            });
            listBtn.addEventListener('click', () => {
                grid.classList.add('list-view');
                listBtn.classList.add('active');
                gridBtn.classList.remove('active');
            });
        }
    }

    function setupCart() {
        const cartToggle = document.getElementById('cartToggle');
        const cartOverlay = document.getElementById('cartOverlay');
        const cartClose = document.getElementById('cartClose');

        if (cartToggle) cartToggle.addEventListener('click', openCart);
        if (cartOverlay) cartOverlay.addEventListener('click', closeCart);
        if (cartClose) cartClose.addEventListener('click', closeCart);

        const checkoutBtn = document.getElementById('checkoutBtn');
        if (checkoutBtn) checkoutBtn.addEventListener('click', openCheckout);

        const checkoutClose = document.getElementById('checkoutClose');
        if (checkoutClose) {
            checkoutClose.addEventListener('click', () => {
                document.getElementById('checkoutModal').classList.remove('active');
            });
        }

        const placeOrderBtn = document.getElementById('placeOrderBtn');
        if (placeOrderBtn) placeOrderBtn.addEventListener('click', placeOrder);
    }

    function openCart() {
        document.getElementById('cartSidebar').classList.add('active');
        document.getElementById('cartOverlay').classList.add('active');
        document.body.style.overflow = 'hidden';
    }

    function closeCart() {
        document.getElementById('cartSidebar').classList.remove('active');
        document.getElementById('cartOverlay').classList.remove('active');
        document.body.style.overflow = '';
    }

    window.addToCart = function(productId) {
        const product = window.allProducts.find(p => p.id === productId);
        if (!product || !product.price) return;

        const existing = cart.find(c => c.id === productId);
        if (existing) {
            existing.qty++;
        } else {
            cart.push({ id: productId, qty: 1 });
        }

        saveCart();
        updateCartUI();
        showToast(`${product.name} a fost adaugat in cos!`, 'success');

        document.querySelectorAll('.add-to-cart-btn').forEach(btn => {
            if (btn.closest('.product-card')) {
                const cardName = btn.closest('.product-card').querySelector('.product-name')?.textContent;
                if (cardName === product.name) {
                    btn.classList.add('added');
                    btn.innerHTML = '<i class="fas fa-check"></i>';
                }
            }
        });
    };

    window.updateCartQty = function(productId, delta) {
        const item = cart.find(c => c.id === productId);
        if (!item) return;
        item.qty += delta;
        if (item.qty <= 0) {
            cart = cart.filter(c => c.id !== productId);
        }
        saveCart();
        updateCartUI();
    };

    window.removeFromCart = function(productId) {
        cart = cart.filter(c => c.id !== productId);
        saveCart();
        updateCartUI();
    };

    function saveCart() {
        localStorage.setItem('patricecom_cart', JSON.stringify(cart));
    }

    function updateCartUI() {
        const cartCount = document.getElementById('cartCount');
        const cartItems = document.getElementById('cartItems');
        const cartFooter = document.getElementById('cartFooter');
        const cartTotal = document.getElementById('cartTotal');

        const totalItems = cart.reduce((sum, c) => sum + c.qty, 0);
        cartCount.textContent = totalItems;
        cartCount.classList.toggle('show', totalItems > 0);

        if (cart.length === 0) {
            cartItems.innerHTML = `
                <div class="cart-empty">
                    <i class="fas fa-shopping-bag"></i>
                    <p>Cosul tau este gol</p>
                </div>
            `;
            cartFooter.style.display = 'none';
            return;
        }

        let totalPrice = 0;
        cartItems.innerHTML = cart.map(item => {
            const product = window.allProducts.find(p => p.id === item.id);
            if (!product) return '';
            const itemTotal = product.price * item.qty;
            totalPrice += itemTotal;
            const colors = getProductColor(product.name);
            const icon = getCategoryIcon(product.name);

            return `
                <div class="cart-item">
                    <div class="cart-item-image" style="background:${colors.bg}; overflow:hidden">
                        ${window.getProductImage ? `<img src="${window.getProductImage(product)}" alt="" style="width:100%;height:100%;object-fit:contain;"/>` : `<i class="${icon}" style="color:${colors.color}"></i>`}
                    </div>
                    <div class="cart-item-info">
                        <div class="cart-item-name">${product.name}</div>
                        <div class="cart-item-brand">${product.brand} - ${product.quantity}</div>
                        <div class="cart-item-bottom">
                            <div class="cart-item-qty">
                                <button class="qty-btn" onclick="updateCartQty(${product.id}, -1)"><i class="fas fa-minus"></i></button>
                                <span class="qty-value">${item.qty}</span>
                                <button class="qty-btn" onclick="updateCartQty(${product.id}, 1)"><i class="fas fa-plus"></i></button>
                            </div>
                            <span class="cart-item-price">${itemTotal.toFixed(2)} Lei</span>
                        </div>
                    </div>
                    <button class="cart-item-remove" onclick="removeFromCart(${product.id})"><i class="fas fa-trash-alt"></i></button>
                </div>
            `;
        }).join('');

        cartTotal.textContent = totalPrice.toFixed(2) + ' Lei';
        cartFooter.style.display = 'block';
    }

    window.viewProduct = function(productId) {
        const product = window.allProducts.find(p => p.id === productId);
        if (!product) return;

        document.getElementById('searchResults').innerHTML = '';
        const msr = document.getElementById('mobileSearchResults');
        if (msr) msr.innerHTML = '';

        const modal = document.getElementById('productModal');
        const body = document.getElementById('productModalBody');
        const colors = getProductColor(product.name);
        const icon = getCategoryIcon(product.name);
        const description = generateDescription(product);
        const features = generateFeatures(product);

        body.innerHTML = `
            <div class="pm-grid">
                <div class="pm-image" style="background:${colors.bg};">
                    ${window.getProductImage ? `<img src="${window.getProductImage(product)}" alt="${product.name}" style="width:100%;height:100%;object-fit:contain;border-radius:var(--radius)"/>` : `<i class="${icon}" style="color:${colors.color}; font-size:5rem"></i>`}
                </div>
                <div class="pm-info">
                    <span class="pm-brand">${product.brand}</span>
                    <h2 class="pm-name">${product.name}</h2>
                    <span class="pm-quantity">${product.quantity}</span>
                    ${product.price
                        ? `<div class="pm-price">${product.price.toFixed(2)} <span class="currency">Lei</span></div>`
                        : '<div class="pm-price" style="color:var(--gray-400); font-size:1.2rem">Pret la cerere</div>'
                    }
                    ${product.offer ? `<div style="background:var(--accent); color:white; display:inline-block; padding:4px 14px; border-radius:50px; font-size:0.85rem; font-weight:600; margin-bottom:16px">${product.offer}</div>` : ''}
                    <p class="pm-description">${description}</p>
                    <div class="pm-features">
                        ${features.map(f => `<div class="pm-feature"><i class="fas fa-check-circle"></i><span>${f}</span></div>`).join('')}
                    </div>
                    ${product.price ? `
                    <div class="pm-qty-row">
                        <div class="pm-qty-control">
                            <button class="pm-qty-btn" onclick="pmQtyChange(-1)"><i class="fas fa-minus"></i></button>
                            <span class="pm-qty-value" id="pmQtyValue">1</span>
                            <button class="pm-qty-btn" onclick="pmQtyChange(1)"><i class="fas fa-plus"></i></button>
                        </div>
                        <button class="btn btn-primary btn-lg pm-add-btn" onclick="addToCartFromModal(${product.id})">
                            <i class="fas fa-cart-plus"></i> Adauga in Cos
                        </button>
                    </div>` : ''}
                </div>
            </div>
        `;

        modal.classList.add('active');
        document.getElementById('productModalClose').onclick = () => modal.classList.remove('active');
        modal.addEventListener('click', (e) => {
            if (e.target === modal) modal.classList.remove('active');
        });
    };

    window.pmQtyChange = function(delta) {
        const el = document.getElementById('pmQtyValue');
        let val = parseInt(el.textContent) + delta;
        if (val < 1) val = 1;
        if (val > 99) val = 99;
        el.textContent = val;
    };

    window.addToCartFromModal = function(productId) {
        const qty = parseInt(document.getElementById('pmQtyValue')?.textContent || '1');
        const product = window.allProducts.find(p => p.id === productId);
        if (!product) return;

        const existing = cart.find(c => c.id === productId);
        if (existing) {
            existing.qty += qty;
        } else {
            cart.push({ id: productId, qty: qty });
        }

        saveCart();
        updateCartUI();
        document.getElementById('productModal').classList.remove('active');
        showToast(`${product.name} (x${qty}) a fost adaugat in cos!`, 'success');
    };

    function generateDescription(product) {
        const n = product.name.toLowerCase();
        if (n.includes('vitamin c')) return 'Vitamina C contribuie la functionarea normala a sistemului imunitar si la protejarea celulelor impotriva stresului oxidativ.';
        if (n.includes('vitamin d')) return 'Vitamina D contribuie la mentinerea oaselor si dintilor normali si la functionarea normala a sistemului imunitar.';
        if (n.includes('vitamin b')) return 'Vitaminele din complexul B contribuie la metabolismul energetic normal si la functionarea normala a sistemului nervos.';
        if (n.includes('omega')) return 'Acizii grasi Omega 3 contribuie la functionarea normala a inimii, creierului si mentinerea vederii normale.';
        if (n.includes('magneziu')) return 'Magneziul contribuie la functionarea normala a sistemului nervos, a muschilor si la reducerea oboselii.';
        if (n.includes('collagen') || n.includes('colagen')) return 'Colagenul este o proteina structurala esentiala pentru sanatatea pielii, articulatiilor si oaselor.';
        if (n.includes('probiotic')) return 'Probioticele contribuie la mentinerea echilibrului florei intestinale si la functionarea normala a sistemului digestiv.';
        if (n.includes('zinc')) return 'Zincul contribuie la functionarea normala a sistemului imunitar si la protejarea celulelor impotriva stresului oxidativ.';
        return `${product.name} de la ${product.brand} - produs de calitate premium, testat si certificat conform standardelor europene.`;
    }

    function generateFeatures(product) {
        const base = ['Produs certificat conform standardelor UE', 'Ingrediente de calitate premium'];
        const n = product.name.toLowerCase();
        if (n.includes('vitamin') || n.includes('mineral')) base.push('Formula optimizata pentru absorbtie maxima');
        if (n.includes('natural') || n.includes('plant') || n.includes('herbal')) base.push('Ingrediente 100% naturale');
        if (product.offer) base.push('Oferta speciala disponibila');
        base.push('Livrare rapida in toata Romania');
        return base;
    }

    function openCheckout() {
        closeCart();
        setTimeout(() => {
            document.getElementById('checkoutModal').classList.add('active');
            showStep(1);
        }, 300);
    }

    window.nextStep = function(step) {
        showStep(step);
    };

    function showStep(step) {
        document.querySelectorAll('.checkout-panel').forEach(p => p.classList.remove('active'));
        document.querySelectorAll('.checkout-step').forEach(s => {
            const sNum = parseInt(s.getAttribute('data-step'));
            s.classList.remove('active', 'done');
            if (sNum < step) s.classList.add('done');
            if (sNum === step) s.classList.add('active');
        });
        const panel = document.getElementById(`step${step}`);
        if (panel) panel.classList.add('active');
        if (step === 3) renderOrderSummary();
    }

    function renderOrderSummary() {
        const summary = document.getElementById('orderSummary');
        let total = 0;
        let html = '<h4>Sumar Comanda</h4>';

        cart.forEach(item => {
            const product = window.allProducts.find(p => p.id === item.id);
            if (!product) return;
            const itemTotal = product.price * item.qty;
            total += itemTotal;
            html += `<div class="order-summary-item"><span>${product.name} x${item.qty}</span><span>${itemTotal.toFixed(2)} Lei</span></div>`;
        });

        const delivery = document.querySelector('input[name="delivery"]:checked')?.value;
        const deliveryCost = delivery === 'express' ? 29.99 : 15.99;

        html += `
            <div class="order-summary-item"><span>Livrare (${delivery === 'express' ? 'Express' : 'Standard'})</span><span>${deliveryCost.toFixed(2)} Lei</span></div>
            <div class="order-summary-total"><span>Total</span><span>${(total + deliveryCost).toFixed(2)} Lei</span></div>
        `;
        summary.innerHTML = html;
    }

    function placeOrder() {
        const orderNumber = 'PCM-' + Date.now().toString(36).toUpperCase();
        document.getElementById('orderNumber').textContent = orderNumber;

        document.querySelectorAll('.checkout-panel').forEach(p => p.classList.remove('active'));
        document.querySelectorAll('.checkout-step').forEach(s => s.classList.add('done'));
        document.getElementById('stepSuccess').classList.add('active');

        cart = [];
        saveCart();
        updateCartUI();
    }

    window.closeCheckout = function() {
        document.getElementById('checkoutModal').classList.remove('active');
        showStep(1);
    };

    initShop();
})();
