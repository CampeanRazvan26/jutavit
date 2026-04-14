/* =============================================
   JUTAVIT - Product Image Generator
   Lightweight cached SVG product illustrations
   ============================================= */

(function() {
    const cache = {};

    window.getProductImage = function(product) {
        const config = getImageConfig(product.name.toLowerCase(), product.brand);
        const key = config.type + '-' + config.color1;
        if (!cache[key]) {
            cache[key] = buildSVG(config);
        }
        return cache[key];
    };

    function getImageConfig(name, brand) {
        if (name.includes('vitamina c') || name.includes('vitamin c')) return { type: 'bottle', color1: '#FF9800', color2: '#FFB74D', icon: 'C', accent: '#FFF3E0' };
        if (name.includes('vitamina d') || name.includes('vitamin d')) return { type: 'bottle', color1: '#FBC02D', color2: '#FFF176', icon: 'D', accent: '#FFF9C4' };
        if (name.includes('vitamina b') || name.includes('b complex')) return { type: 'bottle', color1: '#5C6BC0', color2: '#9FA8DA', icon: 'B', accent: '#E8EAF6' };
        if (name.includes('vitamina a')) return { type: 'bottle', color1: '#FF5722', color2: '#FF8A65', icon: 'A', accent: '#FBE9E7' };
        if (name.includes('vitamina k') || name.includes('vitamin k')) return { type: 'bottle', color1: '#4CAF50', color2: '#81C784', icon: 'K', accent: '#E8F5E9' };
        if (name.includes('vitamina e')) return { type: 'bottle', color1: '#E91E63', color2: '#F48FB1', icon: 'E', accent: '#FCE4EC' };
        if (name.includes('multivitamin')) return { type: 'bottle', color1: '#9C27B0', color2: '#CE93D8', icon: 'M', accent: '#F3E5F5' };
        if (name.includes('magneziu') || name.includes('maximag')) return { type: 'bottle', color1: '#7B1FA2', color2: '#BA68C8', icon: 'Mg', accent: '#F3E5F5' };
        if (name.includes('zinc')) return { type: 'bottle', color1: '#009688', color2: '#4DB6AC', icon: 'Zn', accent: '#E0F2F1' };
        if (name.includes('seleniu')) return { type: 'bottle', color1: '#607D8B', color2: '#90A4AE', icon: 'Se', accent: '#ECEFF1' };
        if (name.includes('calciu') || name.includes('calcidin') || name.includes('ca+')) return { type: 'bottle', color1: '#78909C', color2: '#B0BEC5', icon: 'Ca', accent: '#ECEFF1' };
        if (name.includes('crom')) return { type: 'bottle', color1: '#546E7A', color2: '#90A4AE', icon: 'Cr', accent: '#ECEFF1' };
        if (name.includes('iod')) return { type: 'bottle', color1: '#5D4037', color2: '#8D6E63', icon: 'I', accent: '#EFEBE9' };
        if (name.includes('omega') || name.includes('ulei de krill')) return { type: 'softgel', color1: '#0288D1', color2: '#4FC3F7', icon: '', accent: '#E1F5FE' };
        if (name.includes('lecitina')) return { type: 'softgel', color1: '#F9A825', color2: '#FDD835', icon: '', accent: '#FFF9C4' };
        if (name.includes('ulei de dovleac')) return { type: 'softgel', color1: '#388E3C', color2: '#66BB6A', icon: '', accent: '#E8F5E9' };
        if (name.includes('collagen') || name.includes('colagen')) return { type: 'powder', color1: '#E91E63', color2: '#F48FB1', icon: '', accent: '#FCE4EC' };
        if (name.includes('hialuron')) return { type: 'bottle', color1: '#E040FB', color2: '#EA80FC', icon: 'HA', accent: '#F3E5F5' };
        if (name.includes('hair') || name.includes('biotin')) return { type: 'bottle', color1: '#AD1457', color2: '#EC407A', icon: '', accent: '#FCE4EC' };
        if (name.includes('probiotic')) return { type: 'capsule', color1: '#43A047', color2: '#81C784', icon: '', accent: '#E8F5E9' };
        if (name.includes('digestiv') || name.includes('enzim')) return { type: 'capsule', color1: '#66BB6A', color2: '#A5D6A7', icon: '', accent: '#E8F5E9' };
        if (name.includes('lactaz')) return { type: 'bottle', color1: '#26A69A', color2: '#80CBC4', icon: 'L', accent: '#E0F2F1' };
        if (name.includes('glucozamin') || name.includes('condroitin')) return { type: 'bottle', color1: '#1565C0', color2: '#42A5F5', icon: '', accent: '#E3F2FD' };
        if (name.includes('imuno') || name.includes('echinac')) return { type: 'bottle', color1: '#2E7D32', color2: '#66BB6A', icon: '', accent: '#E8F5E9' };
        if (name.includes('propolis')) return { type: 'spray', color1: '#F57F17', color2: '#FFD54F', icon: '', accent: '#FFF8E1' };
        if (name.includes('gripovit')) return { type: 'sachet', color1: '#FF6F00', color2: '#FFB300', icon: '', accent: '#FFF8E1' };
        if (name.includes('ceai')) return { type: 'tea', color1: '#33691E', color2: '#689F38', icon: '', accent: '#F1F8E9' };
        if (name.includes('sirop')) return { type: 'syrup', color1: '#6A1B9A', color2: '#AB47BC', icon: '', accent: '#F3E5F5' };
        if (name.includes('picaturi')) return { type: 'drops', color1: '#00838F', color2: '#26C6DA', icon: '', accent: '#E0F7FA' };
        if (name.includes('gel') || name.includes('balsam')) return { type: 'tube', color1: '#00ACC1', color2: '#4DD0E1', icon: '', accent: '#E0F7FA' };
        if (name.includes('crema')) return { type: 'tube', color1: '#EC407A', color2: '#F48FB1', icon: '', accent: '#FCE4EC' };
        if (name.includes('spray')) return { type: 'spray', color1: '#0097A7', color2: '#4DD0E1', icon: '', accent: '#E0F7FA' };
        if (name.includes('sampon')) return { type: 'tube', color1: '#7C4DFF', color2: '#B388FF', icon: '', accent: '#EDE7F6' };
        if (name.includes('lacalut') || name.includes('paradontax') || name.includes('sensodyne')) return { type: 'tube', color1: '#1E88E5', color2: '#64B5F6', icon: '', accent: '#E3F2FD' };
        if (name.includes('valeriana') || name.includes('harmony') || name.includes('noapte')) return { type: 'bottle', color1: '#283593', color2: '#5C6BC0', icon: '', accent: '#E8EAF6' };
        if (name.includes('antistres')) return { type: 'bottle', color1: '#4527A0', color2: '#7E57C2', icon: '', accent: '#EDE7F6' };
        if (name.includes('coenzima') || name.includes('q10')) return { type: 'softgel', color1: '#E65100', color2: '#FF8F00', icon: '', accent: '#FFF3E0' };
        if (name.includes('lutein') || name.includes('opti')) return { type: 'bottle', color1: '#F57C00', color2: '#FFB74D', icon: '', accent: '#FFF3E0' };
        if (name.includes('prosta')) return { type: 'capsule', color1: '#1565C0', color2: '#42A5F5', icon: '', accent: '#E3F2FD' };
        if (name.includes('slim') || name.includes('slabit') || name.includes('glucomanan')) return { type: 'capsule', color1: '#00C853', color2: '#69F0AE', icon: '', accent: '#E8F5E9' };
        if (name.includes('copii') || name.includes('kid') || name.includes('junior')) return { type: 'bottle', color1: '#FF7043', color2: '#FFAB91', icon: '', accent: '#FBE9E7' };
        if (name.includes('termometru')) return { type: 'device', color1: '#546E7A', color2: '#90A4AE', icon: '', accent: '#ECEFF1' };
        if (name.includes('aspirator') || name.includes('biberon') || name.includes('suzeta') || name.includes('pipeta')) return { type: 'device', color1: '#42A5F5', color2: '#90CAF9', icon: '', accent: '#E3F2FD' };
        if (name.includes('plasturi') || name.includes('vata') || name.includes('ser fiziologic') || name.includes('perfuzoare')) return { type: 'device', color1: '#EF5350', color2: '#EF9A9A', icon: '', accent: '#FFEBEE' };
        if (name.includes('armurariu') || name.includes('silimarin')) return { type: 'capsule', color1: '#558B2F', color2: '#8BC34A', icon: '', accent: '#F1F8E9' };
        if (name.includes('usturoi')) return { type: 'capsule', color1: '#827717', color2: '#C0CA33', icon: '', accent: '#F9FBE7' };
        if (name.includes('merisor') || name.includes('splinuta')) return { type: 'bottle', color1: '#C62828', color2: '#EF5350', icon: '', accent: '#FFEBEE' };
        if (name.includes('curcuma')) return { type: 'capsule', color1: '#FF8F00', color2: '#FFB300', icon: '', accent: '#FFF8E1' };
        if (name.includes('scortisoara')) return { type: 'bottle', color1: '#795548', color2: '#A1887F', icon: '', accent: '#EFEBE9' };
        if (name.includes('ulei')) return { type: 'drops', color1: '#F9A825', color2: '#FDD835', icon: '', accent: '#FFF9C4' };
        // Brand defaults
        if (brand === 'BIOEEL') return { type: 'tube', color1: '#26A69A', color2: '#80CBC4', icon: '', accent: '#E0F2F1' };
        if (brand === 'FARES') return { type: 'tea', color1: '#2E7D32', color2: '#66BB6A', icon: '', accent: '#E8F5E9' };
        if (brand === 'HOFIGAL') return { type: 'bottle', color1: '#1B5E20', color2: '#43A047', icon: '', accent: '#E8F5E9' };
        if (brand === 'LARIX') return { type: 'capsule', color1: '#4E342E', color2: '#795548', icon: '', accent: '#EFEBE9' };
        return { type: 'bottle', color1: '#0B6E4F', color2: '#14A76C', icon: '', accent: '#E8F5F0' };
    }

    function buildSVG(c) {
        const shapes = {
            bottle: `<rect x="76" y="44" width="48" height="10" rx="3" fill="${c.color1}" opacity=".9"/>
                <rect x="68" y="54" width="64" height="100" rx="10" fill="${c.color1}"/>
                <rect x="68" y="54" width="64" height="100" rx="10" fill="url(#g)" opacity=".6"/>
                <rect x="68" y="54" width="64" height="28" rx="10" fill="${c.color1}" opacity=".25"/>
                <rect x="76" y="80" width="48" height="36" rx="4" fill="#fff" opacity=".88"/>
                ${c.icon ? `<text x="100" y="106" text-anchor="middle" font-size="18" font-weight="800" fill="${c.color1}" font-family="sans-serif">${c.icon}</text>` :
                `<rect x="82" y="90" width="36" height="3.5" rx="2" fill="${c.color1}" opacity=".3"/>
                 <rect x="86" y="97" width="28" height="3" rx="1.5" fill="${c.color1}" opacity=".2"/>
                 <rect x="89" y="104" width="22" height="2.5" rx="1" fill="${c.color1}" opacity=".15"/>`}
                <ellipse cx="100" cy="155" rx="32" ry="3.5" fill="rgba(0,0,0,.06)"/>`,

            softgel: `<ellipse cx="80" cy="95" rx="32" ry="18" fill="${c.color1}" transform="rotate(-15 80 95)" opacity=".85"/>
                <ellipse cx="80" cy="95" rx="24" ry="12" fill="#fff" transform="rotate(-15 80 95)" opacity=".15"/>
                <ellipse cx="72" cy="89" rx="7" ry="4" fill="#fff" transform="rotate(-15 72 89)" opacity=".3"/>
                <ellipse cx="120" cy="80" rx="26" ry="15" fill="${c.color1}" transform="rotate(-30 120 80)" opacity=".55"/>
                <ellipse cx="100" cy="115" rx="28" ry="16" fill="${c.color1}" transform="rotate(10 100 115)" opacity=".45"/>
                <ellipse cx="100" cy="150" rx="36" ry="3" fill="rgba(0,0,0,.05)"/>`,

            capsule: `<rect x="68" y="44" width="64" height="12" rx="3" fill="${c.color1}" opacity=".8"/>
                <rect x="62" y="56" width="76" height="98" rx="12" fill="${c.color1}"/>
                <rect x="62" y="56" width="76" height="98" rx="12" fill="url(#g)" opacity=".5"/>
                <rect x="62" y="56" width="76" height="32" rx="12" fill="${c.color1}" opacity=".2"/>
                <rect x="72" y="92" width="56" height="26" rx="4" fill="#fff" opacity=".85"/>
                <rect x="80" y="100" width="40" height="3" rx="1.5" fill="${c.color1}" opacity=".3"/>
                <rect x="84" y="107" width="32" height="2.5" rx="1" fill="${c.color1}" opacity=".2"/>
                <ellipse cx="100" cy="155" rx="38" ry="3.5" fill="rgba(0,0,0,.06)"/>`,

            tube: `<rect x="86" y="32" width="28" height="16" rx="4" fill="${c.color1}" opacity=".9"/>
                <rect x="92" y="24" width="16" height="12" rx="3" fill="${c.color2}"/>
                <rect x="72" y="48" width="56" height="96" rx="14" fill="${c.color1}"/>
                <rect x="72" y="48" width="56" height="96" rx="14" fill="url(#g)" opacity=".5"/>
                <rect x="80" y="78" width="40" height="30" rx="4" fill="#fff" opacity=".85"/>
                <rect x="86" y="86" width="28" height="3" rx="1.5" fill="${c.color1}" opacity=".3"/>
                <rect x="88" y="93" width="24" height="2.5" rx="1" fill="${c.color1}" opacity=".2"/>
                <rect x="90" y="99" width="20" height="2.5" rx="1" fill="${c.color1}" opacity=".15"/>
                <ellipse cx="100" cy="146" rx="28" ry="3" fill="rgba(0,0,0,.06)"/>`,

            spray: `<rect x="86" y="32" width="28" height="20" rx="4" fill="${c.color1}" opacity=".9"/>
                <rect x="92" y="24" width="16" height="12" rx="3" fill="${c.color2}"/>
                <rect x="96" y="18" width="8" height="10" rx="2" fill="${c.color1}"/>
                <rect x="78" y="52" width="44" height="98" rx="8" fill="${c.color1}"/>
                <rect x="78" y="52" width="44" height="98" rx="8" fill="url(#g)" opacity=".5"/>
                <rect x="84" y="76" width="32" height="38" rx="3" fill="#fff" opacity=".85"/>
                <rect x="89" y="86" width="22" height="3" rx="1.5" fill="${c.color1}" opacity=".3"/>
                <rect x="90" y="93" width="20" height="2.5" rx="1" fill="${c.color1}" opacity=".2"/>
                <ellipse cx="100" cy="152" rx="22" ry="3" fill="rgba(0,0,0,.06)"/>`,

            tea: `<rect x="62" y="46" width="76" height="100" rx="6" fill="${c.color1}"/>
                <rect x="62" y="46" width="76" height="100" rx="6" fill="url(#g)" opacity=".5"/>
                <rect x="62" y="46" width="76" height="26" rx="6" fill="${c.color1}" opacity=".25"/>
                <rect x="62" y="66" width="76" height="5" fill="${c.color1}" opacity=".12"/>
                <rect x="72" y="80" width="56" height="30" rx="4" fill="#fff" opacity=".85"/>
                <rect x="80" y="88" width="40" height="3" rx="1.5" fill="${c.color1}" opacity=".3"/>
                <rect x="84" y="95" width="32" height="2.5" rx="1" fill="${c.color1}" opacity=".2"/>
                <ellipse cx="100" cy="148" rx="38" ry="3" fill="rgba(0,0,0,.05)"/>`,

            syrup: `<rect x="84" y="36" width="32" height="14" rx="6" fill="${c.color1}" opacity=".9"/>
                <rect x="74" y="50" width="52" height="100" rx="10" fill="${c.color1}"/>
                <rect x="74" y="50" width="52" height="100" rx="10" fill="url(#g)" opacity=".5"/>
                <rect x="80" y="72" width="40" height="40" rx="4" fill="#fff" opacity=".85"/>
                <rect x="86" y="84" width="28" height="3" rx="1.5" fill="${c.color1}" opacity=".3"/>
                <rect x="88" y="91" width="24" height="2.5" rx="1" fill="${c.color1}" opacity=".2"/>
                <ellipse cx="100" cy="152" rx="26" ry="3" fill="rgba(0,0,0,.06)"/>`,

            drops: `<rect x="88" y="30" width="24" height="18" rx="4" fill="${c.color1}" opacity=".9"/>
                <rect x="94" y="22" width="12" height="12" rx="2" fill="${c.color2}"/>
                <rect x="82" y="48" width="36" height="104" rx="8" fill="${c.color1}"/>
                <rect x="82" y="48" width="36" height="104" rx="8" fill="url(#g)" opacity=".5"/>
                <rect x="86" y="76" width="28" height="36" rx="3" fill="#fff" opacity=".85"/>
                <rect x="90" y="86" width="20" height="3" rx="1.5" fill="${c.color1}" opacity=".3"/>
                <rect x="92" y="93" width="16" height="2.5" rx="1" fill="${c.color1}" opacity=".2"/>
                <ellipse cx="100" cy="154" rx="18" ry="2.5" fill="rgba(0,0,0,.06)"/>`,

            sachet: `<rect x="58" y="50" width="84" height="58" rx="6" fill="${c.color1}"/>
                <rect x="58" y="50" width="84" height="58" rx="6" fill="url(#g)" opacity=".5"/>
                <path d="M58 50 L100 44 L142 50" fill="${c.color1}" opacity=".3"/>
                <rect x="68" y="64" width="64" height="24" rx="4" fill="#fff" opacity=".85"/>
                <rect x="78" y="72" width="44" height="3" rx="1.5" fill="${c.color1}" opacity=".3"/>
                <rect x="82" y="79" width="36" height="2.5" rx="1" fill="${c.color1}" opacity=".2"/>
                <rect x="62" y="116" width="76" height="34" rx="6" fill="${c.color1}" opacity=".4" transform="rotate(4 100 133)"/>
                <ellipse cx="100" cy="155" rx="42" ry="3" fill="rgba(0,0,0,.05)"/>`,

            powder: `<rect x="64" y="48" width="72" height="96" rx="10" fill="${c.color1}"/>
                <rect x="64" y="48" width="72" height="96" rx="10" fill="url(#g)" opacity=".5"/>
                <rect x="64" y="48" width="72" height="24" rx="10" fill="${c.color1}" opacity=".2"/>
                <rect x="74" y="82" width="52" height="28" rx="4" fill="#fff" opacity=".85"/>
                <rect x="82" y="90" width="36" height="3" rx="1.5" fill="${c.color1}" opacity=".3"/>
                <rect x="86" y="97" width="28" height="2.5" rx="1" fill="${c.color1}" opacity=".2"/>
                <ellipse cx="100" cy="146" rx="36" ry="3.5" fill="rgba(0,0,0,.06)"/>`,

            device: `<rect x="68" y="46" width="64" height="100" rx="12" fill="#F5F5F5" stroke="${c.color1}" stroke-width="2"/>
                <rect x="78" y="58" width="44" height="44" rx="6" fill="${c.accent}"/>
                <circle cx="100" cy="80" r="14" fill="${c.color1}" opacity=".7"/>
                <circle cx="100" cy="80" r="8" fill="#fff" opacity=".3"/>
                <rect x="80" y="112" width="40" height="3" rx="1.5" fill="${c.color1}" opacity=".3"/>
                <rect x="84" y="119" width="32" height="2.5" rx="1" fill="${c.color1}" opacity=".2"/>
                <ellipse cx="100" cy="148" rx="32" ry="3" fill="rgba(0,0,0,.05)"/>`,
        };

        const shape = shapes[c.type] || shapes.bottle;
        const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 170">
            <defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="${c.color2}" stop-opacity=".6"/><stop offset="100%" stop-color="${c.color1}" stop-opacity=".2"/></linearGradient></defs>
            <rect width="200" height="170" fill="${c.accent}" rx="12"/>
            <circle cx="160" cy="36" r="14" fill="${c.color1}" opacity=".08"/>
            <circle cx="40" cy="140" r="10" fill="${c.color2}" opacity=".06"/>
            ${shape}
        </svg>`;

        return 'data:image/svg+xml,' + encodeURIComponent(svg);
    }
})();
