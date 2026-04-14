/* =============================================
   JUTAVIT ROMANIA - Shop & Cart Logic
   ============================================= */

(function() {
    let cart = JSON.parse(localStorage.getItem('jutavit_cart') || '[]');
    let currentFilter = 'all';
    let currentSort = 'name-asc';
    let displayedCount = 0;
    const ITEMS_PER_PAGE = 16;
    let filteredProducts = [];

    // Initialize shop
    function initShop() {
        if (!window.allProducts || !window.allProducts.length) {
            setTimeout(initShop, 100);
            return;
        }

        filteredProducts = [...window.allProducts];
        displayedCount = 0;
        renderProducts();
        setupFilters();
        setupCart();
        updateCartUI();
    }

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
            card.style.animationDelay = `${i * 0.05}s`;
            grid.appendChild(card);
        });

        displayedCount += batch.length;

        // Update load more button
        const loadMore = document.getElementById('loadMore');
        if (loadMore) {
            loadMore.style.display = displayedCount >= sorted.length ? 'none' : 'inline-flex';
        }
    }

    // Create product card
    function createProductCard(product) {
        const colors = getProductColor(product.name);
        const icon = getCategoryIcon(product.name);
        const inCart = cart.find(c => c.id === product.id);

        const card = document.createElement('div');
        card.className = 'product-card';
        card.style.animation = 'fadeInUp 0.5s ease forwards';
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

    // Sort products
    function sortProducts(products, sort) {
        const sorted = [...products];
        switch(sort) {
            case 'name-asc':
                return sorted.sort((a, b) => a.name.localeCompare(b.name, 'ro'));
            case 'name-desc':
                return sorted.sort((a, b) => b.name.localeCompare(a.name, 'ro'));
            case 'price-asc':
                return sorted.sort((a, b) => (a.price || 999) - (b.price || 999));
            case 'price-desc':
                return sorted.sort((a, b) => (b.price || 0) - (a.price || 0));
            default:
                return sorted;
        }
    }

    // Setup filters
    function setupFilters() {
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', () => {
                document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                currentFilter = btn.getAttribute('data-filter');
                applyFilter();
            });
        });

        const sortSelect = document.getElementById('sortSelect');
        if (sortSelect) {
            sortSelect.addEventListener('change', (e) => {
                currentSort = e.target.value;
                renderProducts(true);
            });
        }

        const loadMore = document.getElementById('loadMore');
        if (loadMore) {
            loadMore.addEventListener('click', () => renderProducts(false));
        }
    }

    function applyFilter() {
        if (currentFilter === 'all') {
            filteredProducts = [...window.allProducts];
        } else if (currentFilter === 'offer') {
            filteredProducts = window.allProducts.filter(p => p.offer);
        } else {
            filteredProducts = window.allProducts.filter(p =>
                p.brand.toUpperCase() === currentFilter.toUpperCase()
            );
        }
        renderProducts(true);
    }

    // Filter by category (called from category cards)
    window.filterByCategory = function(category) {
        const categoryMap = {
            'vitamine': ['vitamin', 'vitamina'],
            'minerale': ['magneziu', 'zinc', 'seleniu', 'calciu', 'crom', 'iod', 'fier'],
            'imunitate': ['imuno', 'propolis', 'echinac', 'gripovit', 'herbal hot'],
            'digestie': ['probiotic', 'enzim', 'digestiv', 'lactaz', 'pelin'],
            'articulatii': ['glucozamin', 'condroitin', 'colagen', 'collagen', 'msm'],
            'frumusete': ['collagen', 'hialuron', 'hair', 'colagen', 'biotin'],
            'energie': ['omega', 'coenzima', 'ginseng', 'lecitina', 'energy'],
            'copii': ['copii', 'kid', 'junior', 'baby']
        };

        const keywords = categoryMap[category] || [];
        if (keywords.length) {
            filteredProducts = window.allProducts.filter(p =>
                keywords.some(kw => p.name.toLowerCase().includes(kw))
            );
        } else {
            filteredProducts = [...window.allProducts];
        }

        // Reset filter buttons
        document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
        document.querySelector('.filter-btn[data-filter="all"]')?.classList.add('active');

        renderProducts(true);
    };

    // Setup cart
    function setupCart() {
        const cartToggle = document.getElementById('cartToggle');
        const cartOverlay = document.getElementById('cartOverlay');
        const cartClose = document.getElementById('cartClose');
        const cartSidebar = document.getElementById('cartSidebar');

        cartToggle.addEventListener('click', () => openCart());
        cartOverlay.addEventListener('click', () => closeCart());
        cartClose.addEventListener('click', () => closeCart());

        // Checkout
        const checkoutBtn = document.getElementById('checkoutBtn');
        if (checkoutBtn) {
            checkoutBtn.addEventListener('click', openCheckout);
        }

        const checkoutClose = document.getElementById('checkoutClose');
        if (checkoutClose) {
            checkoutClose.addEventListener('click', () => {
                document.getElementById('checkoutModal').classList.remove('active');
            });
        }

        const placeOrderBtn = document.getElementById('placeOrderBtn');
        if (placeOrderBtn) {
            placeOrderBtn.addEventListener('click', placeOrder);
        }
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

    // Add to cart
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

        // Update button state
        const btns = document.querySelectorAll(`.add-to-cart-btn`);
        btns.forEach(btn => {
            if (btn.closest('.product-card')) {
                const cardName = btn.closest('.product-card').querySelector('.product-name')?.textContent;
                if (cardName === product.name) {
                    btn.classList.add('added');
                    btn.innerHTML = '<i class="fas fa-check"></i>';
                }
            }
        });
    };

    // Update cart quantity
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

    // Remove from cart
    window.removeFromCart = function(productId) {
        cart = cart.filter(c => c.id !== productId);
        saveCart();
        updateCartUI();
    };

    function saveCart() {
        localStorage.setItem('jutavit_cart', JSON.stringify(cart));
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
                    <a href="#shop" class="btn btn-primary" onclick="document.getElementById('cartSidebar').classList.remove('active'); document.getElementById('cartOverlay').classList.remove('active'); document.body.style.overflow='';">Incepe Cumparaturile</a>
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
                                <button class="qty-btn" onclick="updateCartQty(${product.id}, -1)">
                                    <i class="fas fa-minus"></i>
                                </button>
                                <span class="qty-value">${item.qty}</span>
                                <button class="qty-btn" onclick="updateCartQty(${product.id}, 1)">
                                    <i class="fas fa-plus"></i>
                                </button>
                            </div>
                            <span class="cart-item-price">${itemTotal.toFixed(2)} Lei</span>
                        </div>
                    </div>
                    <button class="cart-item-remove" onclick="removeFromCart(${product.id})">
                        <i class="fas fa-trash-alt"></i>
                    </button>
                </div>
            `;
        }).join('');

        cartTotal.textContent = totalPrice.toFixed(2) + ' Lei';
        cartFooter.style.display = 'block';
    }

    // View product modal
    window.viewProduct = function(productId) {
        const product = window.allProducts.find(p => p.id === productId);
        if (!product) return;

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
                        ${features.map(f => `
                            <div class="pm-feature">
                                <i class="fas fa-check-circle"></i>
                                <span>${f}</span>
                            </div>
                        `).join('')}
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
        if (n.includes('vitamin c')) return 'Vitamina C contribuie la functionarea normala a sistemului imunitar si la protejarea celulelor impotriva stresului oxidativ. Esentiala pentru sanatatea pielii si absorbtia fierului.';
        if (n.includes('vitamin d')) return 'Vitamina D contribuie la mentinerea oaselor si dintilor normali, la functionarea normala a sistemului imunitar si la absorbtia normala a calciului.';
        if (n.includes('vitamin b')) return 'Vitaminele din complexul B contribuie la metabolismul energetic normal, la functionarea normala a sistemului nervos si la reducerea oboselii.';
        if (n.includes('omega')) return 'Acizii grasi Omega 3 contribuie la functionarea normala a inimii, creierului si mentinerea vederii normale. Sursa naturala de EPA si DHA.';
        if (n.includes('magneziu')) return 'Magneziul contribuie la functionarea normala a sistemului nervos, la functionarea normala a muschilor si la reducerea oboselii si extenuarii.';
        if (n.includes('collagen') || n.includes('colagen')) return 'Colagenul este o proteina structurala esentiala pentru sanatatea pielii, articulatiilor si oaselor. Contribuie la mentinerea elasticitatii pielii.';
        if (n.includes('probiotic')) return 'Probioticele contribuie la mentinerea echilibrului florei intestinale si la functionarea normala a sistemului digestiv.';
        if (n.includes('zinc')) return 'Zincul contribuie la functionarea normala a sistemului imunitar, la mentinerea oaselor normale si la protejarea celulelor impotriva stresului oxidativ.';
        if (n.includes('glucozamin')) return 'Glucozamina si condroitina contribuie la mentinerea mobilitatii articulare si la sanatatea cartilajelor. Formula complexa cu MSM.';
        return `${product.name} de la ${product.brand} - supliment alimentar de calitate premium. Produs testat si certificat conform standardelor europene.`;
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

    // Checkout
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
            html += `
                <div class="order-summary-item">
                    <span>${product.name} x${item.qty}</span>
                    <span>${itemTotal.toFixed(2)} Lei</span>
                </div>
            `;
        });

        const delivery = document.querySelector('input[name="delivery"]:checked')?.value;
        const deliveryCost = delivery === 'express' ? 29.99 : 15.99;

        html += `
            <div class="order-summary-item">
                <span>Livrare (${delivery === 'express' ? 'Express' : 'Standard'})</span>
                <span>${deliveryCost.toFixed(2)} Lei</span>
            </div>
            <div class="order-summary-total">
                <span>Total</span>
                <span>${(total + deliveryCost).toFixed(2)} Lei</span>
            </div>
        `;

        summary.innerHTML = html;
    }

    function placeOrder() {
        const orderNumber = 'JTV-' + Date.now().toString(36).toUpperCase();
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

    // CSS animation
    const style = document.createElement('style');
    style.textContent = `
        @keyframes fadeInUp {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
    `;
    document.head.appendChild(style);

    // Init
    initShop();
})();
