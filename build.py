# -*- coding: utf-8 -*-
"""
Build a self-contained index.html by inlining CSS + JS.

Source of truth: css/*.css and js/*.js (edit these).
index.html has marker comments; this script replaces the content between them
with inline <style>/<script> blocks so the page renders in ANY context
(file://, sandboxed webview with no base URL, HTTP, Vercel).

Re-run after editing any css/ or js/ file:  python build.py
"""
import re, io

INDEX = r'D:\Jutavit\index.html'

CSS_FILES = ['css/style.css', 'css/shop.css', 'css/assistant.css', 'css/dark-mode.css']
JS_FILES  = ['js/products.js', 'js/product-images.js', 'js/app.js', 'js/shop.js', 'js/assistant.js']

def read(path):
    with io.open('D:/Jutavit/' + path, 'r', encoding='utf-8') as f:
        return f.read()

def build_css_block():
    parts = ['    <!-- BUILD:CSS:START -->']
    for f in CSS_FILES:
        parts.append('    <style data-src="%s">' % f)
        parts.append(read(f))
        parts.append('    </style>')
    parts.append('    <!-- BUILD:CSS:END -->')
    return '\n'.join(parts)

def build_js_block():
    parts = ['    <!-- BUILD:JS:START -->']
    for f in JS_FILES:
        parts.append('    <script data-src="%s">' % f)
        parts.append(read(f))
        parts.append('    </script>')
    parts.append('    <!-- BUILD:JS:END -->')
    return '\n'.join(parts)

def replace_block(html, start, end, new_block):
    pattern = re.compile(re.escape(start) + r'.*?' + re.escape(end), re.DOTALL)
    if not pattern.search(html):
        raise SystemExit('Markers %s ... %s not found in index.html' % (start, end))
    return pattern.sub(lambda m: new_block, html, count=1)

def main():
    with io.open(INDEX, 'r', encoding='utf-8') as f:
        html = f.read()

    html = replace_block(html, '<!-- BUILD:CSS:START -->', '<!-- BUILD:CSS:END -->', build_css_block())
    html = replace_block(html, '<!-- BUILD:JS:START -->', '<!-- BUILD:JS:END -->', build_js_block())

    with io.open(INDEX, 'w', encoding='utf-8') as f:
        f.write(html)

    kb = len(html.encode('utf-8')) / 1024
    print('Built self-contained index.html (%.0f KB)' % kb)
    print('Inlined CSS: %s' % ', '.join(CSS_FILES))
    print('Inlined JS : %s' % ', '.join(JS_FILES))

if __name__ == '__main__':
    main()
