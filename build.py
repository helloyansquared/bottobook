#!/usr/bin/env python3
"""Build the public site from src/index.html.
Usage: python3 build.py https://your-domain/ [pdt_PRODUCTID]
Writes public/index.html, public/robots.txt, public/sitemap.xml, and puts the Dodo product id
into public/index.html and functions/api/license.js."""
import sys, re, datetime, pathlib
site = sys.argv[1].rstrip('/') + '/'
product = sys.argv[2] if len(sys.argv) > 2 else None
root = pathlib.Path(__file__).parent
s = (root / 'src/index.html').read_text()
s = re.sub(r'<link rel="preconnect"[^\n]*\n<link href="https://fonts.googleapis.com[^\n]*\n', '<link rel="preload" href="fonts/fraunces-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>\n', s)
faces = ''.join(f'@font-face{{font-family:"{fam}";src:url(fonts/{f}.woff2) format("woff2");font-weight:{w};font-display:swap}}\n'
  for fam, f, w in [("Fraunces","fraunces-latin-600-normal",600),("Fraunces","fraunces-latin-700-normal",700),
                    ("Instrument Sans","instrument-sans-latin-400-normal",400),("Instrument Sans","instrument-sans-latin-500-normal",500),("Instrument Sans","instrument-sans-latin-600-normal",600)])
s = s.replace('<style>\n', '<style>\n' + faces, 1)
head = (f'<link rel="canonical" href="{site}">\n<link rel="icon" href="favicon.svg" type="image/svg+xml">\n'
        f'<meta property="og:url" content="{site}">\n<meta property="og:image" content="{site}og.png">\n'
        '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">\n<meta name="twitter:card" content="summary_large_image">')
assert '<!--SEO-HEAD-->' in s
s = s.replace('<!--SEO-HEAD-->', head)
if product:
    assert re.fullmatch(r'pdt_[A-Za-z0-9]+', product)
    s = s.replace('__PRODUCT_ID__', product)
    fn = root / 'functions/api/license.js'
    fn.write_text(re.sub(r'const PRODUCT_ID = "[^"]*";', f'const PRODUCT_ID = "{product}";', fn.read_text()))
(root / 'public/index.html').write_text(s)
(root / 'public/robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {site}sitemap.xml\n')
(root / 'public/sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>{site}</loc><lastmod>{datetime.date.today()}</lastmod></url>\n</urlset>\n')
print('built for', site, 'product', product or '(none yet)')
