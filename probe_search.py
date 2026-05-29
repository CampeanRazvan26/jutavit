import requests, re
from urllib.parse import urlparse
H = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

# Yandex direct
r = requests.get('https://yandex.com/images/search?text=jutavit+armurariu', headers=H, timeout=10)
print('yandex size:', len(r.text))
urls = re.findall(r'https?://[^\s"<>\\]+\.(?:jpg|jpeg|png|webp)', r.text)
hosts = {}
for u in urls:
    h = urlparse(u).netloc
    hosts[h] = hosts.get(h, 0) + 1
print('total found:', len(urls))
for h, c in sorted(hosts.items(), key=lambda x:-x[1])[:15]:
    print(f'  {c:3} {h}')
print()
print('Sample URLs:')
for u in urls[:10]:
    print(' ', u[:120])
