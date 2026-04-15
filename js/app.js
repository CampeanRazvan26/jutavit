/* =============================================
   PATRICECOM - Main Application
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {
    // Dark Mode Toggle
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const savedTheme = localStorage.getItem('patricecom_theme') || 'light';
    if (savedTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        themeIcon.classList.replace('fa-moon', 'fa-sun');
    }
    themeToggle.addEventListener('click', () => {
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        if (isDark) {
            document.documentElement.removeAttribute('data-theme');
            themeIcon.classList.replace('fa-sun', 'fa-moon');
            localStorage.setItem('patricecom_theme', 'light');
        } else {
            document.documentElement.setAttribute('data-theme', 'dark');
            themeIcon.classList.replace('fa-moon', 'fa-sun');
            localStorage.setItem('patricecom_theme', 'dark');
        }
    });

    // Navbar scroll effect
    const navbar = document.getElementById('navbar');
    const backToTop = document.getElementById('backToTop');
    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 10);
        if (backToTop) backToTop.classList.toggle('show', window.scrollY > 500);
    }, { passive: true });

    // Back to top
    if (backToTop) {
        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Mobile search toggle
    const mobileSearchBtn = document.getElementById('mobileSearchBtn');
    const mobileSearch = document.getElementById('mobileSearch');
    const mobileSearchInput = document.getElementById('mobileSearchInput');
    if (mobileSearchBtn && mobileSearch) {
        mobileSearchBtn.addEventListener('click', () => {
            mobileSearch.classList.toggle('active');
            if (mobileSearch.classList.contains('active')) {
                setTimeout(() => mobileSearchInput.focus(), 100);
            }
        });
    }

    // Mobile menu toggle (sidebar)
    const mobileMenuBtn = document.getElementById('mobileMenuBtn');
    const sidebar = document.getElementById('sidebar');
    const sidebarOverlay = document.getElementById('sidebarOverlay');

    if (mobileMenuBtn && sidebar) {
        mobileMenuBtn.addEventListener('click', () => {
            sidebar.classList.toggle('active');
            sidebarOverlay.classList.toggle('active');
            document.body.style.overflow = sidebar.classList.contains('active') ? 'hidden' : '';
        });
    }

    // Filter mobile button
    const filterMobileBtn = document.getElementById('filterMobileBtn');
    if (filterMobileBtn && sidebar) {
        filterMobileBtn.addEventListener('click', () => {
            sidebar.classList.add('active');
            sidebarOverlay.classList.add('active');
            document.body.style.overflow = 'hidden';
        });
    }

    if (sidebarOverlay) {
        sidebarOverlay.addEventListener('click', () => {
            sidebar.classList.remove('active');
            sidebarOverlay.classList.remove('active');
            document.body.style.overflow = '';
        });
    }

    // Search functionality (shared between desktop & mobile)
    function setupSearch(input, resultsContainer) {
        if (!input || !resultsContainer) return;
        input.addEventListener('input', (e) => {
            const query = e.target.value.toLowerCase().trim();
            if (query.length < 2) {
                resultsContainer.innerHTML = '';
                return;
            }
            const results = window.allProducts
                ? window.allProducts.filter(p =>
                    p.name.toLowerCase().includes(query) ||
                    p.brand.toLowerCase().includes(query)
                ).slice(0, 8)
                : [];

            resultsContainer.innerHTML = results.map(p => `
                <div class="search-result-item" onclick="viewProduct(${p.id})">
                    <div class="search-result-icon">
                        <i class="${getCategoryIcon(p.name)}"></i>
                    </div>
                    <div class="search-result-info">
                        <h4>${highlightMatch(p.name, query)}</h4>
                        <span>${p.brand} - ${p.quantity}</span>
                    </div>
                    ${p.price ? `<span class="search-result-price">${p.price.toFixed(2)} Lei</span>` : ''}
                </div>
            `).join('');
        });
    }

    setupSearch(
        document.getElementById('searchInput'),
        document.getElementById('searchResults')
    );
    setupSearch(
        document.getElementById('mobileSearchInput'),
        document.getElementById('mobileSearchResults')
    );

    // Close search on click outside
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.nav-search')) {
            const sr = document.getElementById('searchResults');
            if (sr) sr.innerHTML = '';
        }
        if (!e.target.closest('.mobile-search')) {
            const msr = document.getElementById('mobileSearchResults');
            if (msr) msr.innerHTML = '';
        }
    });

    // Category Nav - clicks
    const catNavItems = document.querySelectorAll('.cat-nav-item');
    catNavItems.forEach(item => {
        item.addEventListener('click', (e) => {
            e.preventDefault();
            catNavItems.forEach(i => i.classList.remove('active'));
            item.classList.add('active');
            const cat = item.getAttribute('data-cat');
            if (typeof window.filterByCategory === 'function') {
                window.filterByCategory(cat);
            }
        });
    });

    // Footer category links
    document.querySelectorAll('.footer-links a[data-cat]').forEach(link => {
        link.addEventListener('click', (e) => {
            e.preventDefault();
            const cat = link.getAttribute('data-cat');
            window.scrollTo({ top: 0, behavior: 'smooth' });
            setTimeout(() => {
                catNavItems.forEach(i => i.classList.remove('active'));
                const target = document.querySelector(`.cat-nav-item[data-cat="${cat}"]`);
                if (target) target.classList.add('active');
                if (typeof window.filterByCategory === 'function') {
                    window.filterByCategory(cat);
                }
            }, 300);
        });
    });
});

// Helper functions (global)
function highlightMatch(text, query) {
    const regex = new RegExp(`(${query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')})`, 'gi');
    return text.replace(regex, '<strong style="color:var(--primary)">$1</strong>');
}

function getCategoryIcon(name) {
    const n = name.toLowerCase();
    if (n.includes('vitamin')) return 'fas fa-sun';
    if (n.includes('omega') || n.includes('ulei')) return 'fas fa-fish';
    if (n.includes('magneziu') || n.includes('zinc') || n.includes('seleniu') || n.includes('calciu') || n.includes('crom')) return 'fas fa-gem';
    if (n.includes('collagen') || n.includes('hialuron') || n.includes('hair')) return 'fas fa-spa';
    if (n.includes('probiotic') || n.includes('enzim') || n.includes('digestiv') || n.includes('lactaz')) return 'fas fa-leaf';
    if (n.includes('glucozamin') || n.includes('condroitin')) return 'fas fa-bone';
    if (n.includes('imuno') || n.includes('propolis') || n.includes('echinac')) return 'fas fa-shield-virus';
    if (n.includes('sirop') || n.includes('copii') || n.includes('kid') || n.includes('junior')) return 'fas fa-baby';
    if (n.includes('gel') || n.includes('balsam') || n.includes('spray') || n.includes('crema')) return 'fas fa-pump-medical';
    if (n.includes('coenzima') || n.includes('ginseng') || n.includes('energie')) return 'fas fa-bolt';
    if (n.includes('lacalut') || n.includes('apa de gura')) return 'fas fa-tooth';
    if (n.includes('slim') || n.includes('slabit') || n.includes('glucomanan')) return 'fas fa-weight';
    if (n.includes('valeriana') || n.includes('harmony')) return 'fas fa-moon';
    if (n.includes('prosta')) return 'fas fa-male';
    if (n.includes('lutein') || n.includes('opti')) return 'fas fa-eye';
    if (n.includes('armurariu') || n.includes('silimarin')) return 'fas fa-leaf';
    if (n.includes('usturoi')) return 'fas fa-seedling';
    if (n.includes('merisor')) return 'fas fa-apple-alt';
    if (n.includes('ceai') || n.includes('tea')) return 'fas fa-mug-hot';
    return 'fas fa-capsules';
}

function getProductColor(name) {
    const n = name.toLowerCase();
    if (n.includes('vitamin c')) return { bg: '#FFF3E0', color: '#FF9800' };
    if (n.includes('vitamin d')) return { bg: '#FFF9C4', color: '#FBC02D' };
    if (n.includes('vitamin b')) return { bg: '#E8EAF6', color: '#5C6BC0' };
    if (n.includes('vitamin a')) return { bg: '#FBE9E7', color: '#FF5722' };
    if (n.includes('vitamin k')) return { bg: '#E8F5E9', color: '#4CAF50' };
    if (n.includes('omega')) return { bg: '#E1F5FE', color: '#03A9F4' };
    if (n.includes('magneziu')) return { bg: '#F3E5F5', color: '#9C27B0' };
    if (n.includes('zinc')) return { bg: '#E0F2F1', color: '#009688' };
    if (n.includes('collagen') || n.includes('hialuron')) return { bg: '#FCE4EC', color: '#E91E63' };
    if (n.includes('probiotic')) return { bg: '#E8F5E9', color: '#4CAF50' };
    if (n.includes('coenzima')) return { bg: '#FFF3E0', color: '#E65100' };
    if (n.includes('gel') || n.includes('balsam')) return { bg: '#E0F7FA', color: '#00ACC1' };
    if (n.includes('lacalut')) return { bg: '#E3F2FD', color: '#1E88E5' };
    if (n.includes('ceai')) return { bg: '#F1F8E9', color: '#689F38' };
    return { bg: '#E8F5F0', color: '#0B6E4F' };
}

function showToast(message, type = 'success') {
    const existing = document.querySelector('.toast');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.innerHTML = `<i class="fas fa-${type === 'success' ? 'check-circle' : 'exclamation-circle'}"></i> ${message}`;
    document.body.appendChild(toast);
    requestAnimationFrame(() => toast.classList.add('show'));
    setTimeout(() => {
        toast.classList.remove('show');
        setTimeout(() => toast.remove(), 300);
    }, 3000);
}
