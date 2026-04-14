/* =============================================
   JUTAVIT ROMANIA - Main Application
   ============================================= */

document.addEventListener('DOMContentLoaded', () => {
    // Preloader
    const preloader = document.getElementById('preloader');
    window.addEventListener('load', () => {
        setTimeout(() => preloader.classList.add('loaded'), 1600);
    });
    // Fallback - quick hide
    setTimeout(() => preloader.classList.add('loaded'), 2000);

    // Dark Mode Toggle
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = document.getElementById('themeIcon');
    const savedTheme = localStorage.getItem('jutavit_theme') || 'light';
    if (savedTheme === 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        themeIcon.classList.replace('fa-moon', 'fa-sun');
    }
    themeToggle.addEventListener('click', () => {
        const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
        if (isDark) {
            document.documentElement.removeAttribute('data-theme');
            themeIcon.classList.replace('fa-sun', 'fa-moon');
            localStorage.setItem('jutavit_theme', 'light');
        } else {
            document.documentElement.setAttribute('data-theme', 'dark');
            themeIcon.classList.replace('fa-moon', 'fa-sun');
            localStorage.setItem('jutavit_theme', 'dark');
        }
    });

    // Navbar scroll effect
    const navbar = document.getElementById('navbar');
    const handleScroll = () => {
        navbar.classList.toggle('scrolled', window.scrollY > 50);
        // Back to top
        const backToTop = document.getElementById('backToTop');
        if (backToTop) backToTop.classList.toggle('show', window.scrollY > 500);
        // Active nav link
        updateActiveNav();
    };
    window.addEventListener('scroll', handleScroll, { passive: true });

    // Mobile menu
    const mobileToggle = document.getElementById('mobileToggle');
    const navMenu = document.getElementById('navMenu');
    mobileToggle.addEventListener('click', () => {
        navMenu.classList.toggle('active');
        mobileToggle.classList.toggle('active');
    });

    // Close mobile menu on link click
    document.querySelectorAll('.nav-link').forEach(link => {
        link.addEventListener('click', () => {
            navMenu.classList.remove('active');
            mobileToggle.classList.remove('active');
        });
    });

    // Search toggle
    const searchToggle = document.getElementById('searchToggle');
    const searchOverlay = document.getElementById('searchOverlay');
    const searchClose = document.getElementById('searchClose');
    const searchInput = document.getElementById('searchInput');

    searchToggle.addEventListener('click', () => {
        searchOverlay.classList.toggle('active');
        if (searchOverlay.classList.contains('active')) {
            setTimeout(() => searchInput.focus(), 300);
        }
    });

    searchClose.addEventListener('click', () => {
        searchOverlay.classList.remove('active');
        searchInput.value = '';
        document.getElementById('searchResults').innerHTML = '';
    });

    // Search functionality
    searchInput.addEventListener('input', (e) => {
        const query = e.target.value.toLowerCase().trim();
        const resultsContainer = document.getElementById('searchResults');

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

    // Back to top
    const backToTop = document.getElementById('backToTop');
    if (backToTop) {
        backToTop.addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });
    }

    // Active nav link on scroll
    function updateActiveNav() {
        const sections = document.querySelectorAll('section[id]');
        const scrollY = window.scrollY + 100;
        sections.forEach(section => {
            const top = section.offsetTop;
            const height = section.offsetHeight;
            const id = section.getAttribute('id');
            const link = document.querySelector(`.nav-link[href="#${id}"]`);
            if (link) {
                link.classList.toggle('active', scrollY >= top && scrollY < top + height);
            }
        });
    }

    // Animate on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1, rootMargin: '0px 0px -50px 0px' });

    document.querySelectorAll('[data-animate]').forEach(el => observer.observe(el));

    // Counter animation
    const counterObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const counters = entry.target.querySelectorAll('.stat-number');
                counters.forEach(counter => animateCounter(counter));
                counterObserver.unobserve(entry.target);
            }
        });
    }, { threshold: 0.5 });

    const heroStats = document.querySelector('.hero-stats');
    if (heroStats) counterObserver.observe(heroStats);

    function animateCounter(el) {
        const target = parseInt(el.getAttribute('data-count'));
        const duration = 2000;
        const step = target / (duration / 16);
        let current = 0;
        const timer = setInterval(() => {
            current += step;
            if (current >= target) {
                current = target;
                clearInterval(timer);
            }
            el.textContent = Math.floor(current).toLocaleString();
        }, 16);
    }

    // Hero particles
    createParticles();

    // Newsletter form
    const newsletterForm = document.getElementById('newsletterForm');
    if (newsletterForm) {
        newsletterForm.addEventListener('submit', (e) => {
            e.preventDefault();
            showToast('Te-ai abonat cu succes! Multumim!', 'success');
            newsletterForm.reset();
        });
    }

    // Contact form
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            showToast('Mesajul a fost trimis cu succes!', 'success');
            contactForm.reset();
        });
    }

    // Category cards click
    document.querySelectorAll('.category-card').forEach(card => {
        card.addEventListener('click', () => {
            const category = card.getAttribute('data-category');
            document.getElementById('shop').scrollIntoView({ behavior: 'smooth' });
            setTimeout(() => {
                if (typeof filterByCategory === 'function') {
                    filterByCategory(category);
                }
            }, 500);
        });
    });
});

// Helper functions
function createParticles() {
    const container = document.getElementById('heroParticles');
    if (!container) return;
    const colors = ['#0B6E4F', '#14A76C', '#D4A843', '#1B4965'];
    for (let i = 0; i < 10; i++) {
        const particle = document.createElement('div');
        particle.className = 'hero-particle';
        const size = Math.random() * 60 + 20;
        particle.style.cssText = `
            width: ${size}px;
            height: ${size}px;
            left: ${Math.random() * 100}%;
            top: ${Math.random() * 100}%;
            background: ${colors[Math.floor(Math.random() * colors.length)]};
            animation-delay: ${Math.random() * 20}s;
            animation-duration: ${Math.random() * 20 + 15}s;
        `;
        container.appendChild(particle);
    }
}

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
    if (n.includes('probiotic') || n.includes('enzim') || n.includes('digestiv') || n.includes('lactaz')) return 'fas fa-stomach';
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
