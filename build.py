#!/usr/bin/env python3
"""Build the public site.
Usage: python3 build.py https://your-domain/ [pdt_PRODUCTID]
- public/index.html from src/index.html (+ FAQ, JSON-LD, facts table from src/content.py)
- one page per guide in src/content.py, plus /privacy/
- robots.txt, sitemap.xml, llms.txt
Puts the Dodo product id into public/index.html and functions/api/license.js when given."""
import sys, re, json, pathlib, html as H
sys.path.insert(0, str(pathlib.Path(__file__).parent / 'src'))
import content as C

site = sys.argv[1].rstrip('/') + '/'
product = sys.argv[2] if len(sys.argv) > 2 else None
root = pathlib.Path(__file__).parent
pub = root / 'public'
esc = lambda s: H.escape(s, quote=True)
tx = lambda s: H.escape(s, quote=False)
U = lambda slug='': site + (slug + '/' if slug else '')
upd_human = __import__('datetime').date.fromisoformat(C.LAST_UPDATED).strftime('%B %-d, %Y')

FONT_FACES = ''.join(f'@font-face{{font-family:"{fam}";src:url(/fonts/{f}.woff2) format("woff2");font-weight:{w};font-display:swap}}\n'
  for fam, f, w in [("Fraunces","fraunces-latin-600-normal",600),("Fraunces","fraunces-latin-700-normal",700),
                    ("Instrument Sans","instrument-sans-latin-400-normal",400),("Instrument Sans","instrument-sans-latin-500-normal",500),("Instrument Sans","instrument-sans-latin-600-normal",600)])
ORG = {"@type": "Organization", "@id": U() + "#org", "name": "BotToBook", "url": U(), "logo": U() + "icon-512.png", "email": C.EMAIL, "sameAs": [C.GITHUB]}

def faq_html(keys):
    return '\n'.join(f'  <details{" open" if i == 0 else ""}><summary>{tx(C.QA[k][0])}</summary><p>{tx(C.QA[k][1])}</p></details>' for i, k in enumerate(keys))
def faq_ld(keys):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": C.QA[k][0], "acceptedAnswer": {"@type": "Answer", "text": C.QA[k][1]}} for k in keys]}
def ld(nodes):
    return '<script type="application/ld+json">\n' + json.dumps(nodes, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/') + '\n</script>'

PAGES = {p['slug']: p for p in C.PAGES}
FOOTLINKS = '<nav class="foot" aria-label="Guides">' + ''.join(f'<a href="/{p["slug"]}/">{esc(p["crumb"])}</a>' for p in C.PAGES) + '<a href="/privacy/">Privacy &amp; refunds</a><a href="https://fictoepub.pages.dev/">FicToEpub</a><a href="https://ficwrapped.yansquared.com/">FicWrapped</a></nav>'

# ── Home ──────────────────────────────────────────────────────────────────────
s = (root / 'src/index.html').read_text()
s = re.sub(r'<link rel="preconnect"[^\n]*\n<link href="https://fonts.googleapis.com[^\n]*\n', '<link rel="preload" href="/fonts/fraunces-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>\n', s)
s = s.replace('<style>\n', '<style>\n' + FONT_FACES, 1)
head = (f'<link rel="canonical" href="{site}">\n<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n'
        f'<meta property="og:url" content="{site}">\n<meta property="og:image" content="{site}og.png">\n'
        '<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">\n<meta name="twitter:card" content="summary_large_image">')
app = {"@type": "WebApplication", "@id": U() + "#app", "name": "BotToBook", "alternateName": "BotToBook Character.AI export viewer", "url": U(),
       "description": "Browser-based viewer for Character.AI data exports that turns chats into PDF, EPUB or HTML books. Files are processed on the device and never uploaded.",
       "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any", "browserRequirements": "Requires JavaScript. Current Chrome, Edge, Firefox or Safari.",
       "image": U() + "og.png", "isAccessibleForFree": True, "inLanguage": "en-US", "datePublished": C.PUBLISHED, "dateModified": C.LAST_UPDATED,
       "publisher": {"@id": U() + "#org"},
       "featureList": ["Opens the password-protected Character.AI export ZIP in the browser", "Reads message.json, character.json and user.json",
                       "Reads CAI Tools JSON, Tavern JSONL and SillyTavern .jsonl", "PDF book with cover, chapters and page numbers",
                       "EPUB 3 for Kindle, Kobo and Apple Books", "Single-file HTML book", "Plain text export"],
       "offers": [{"@type": "Offer", "name": "Viewer and text export", "price": "0", "priceCurrency": "USD"},
                  {"@type": "Offer", "name": "BotToBook Pro (PDF, EPUB and HTML books)", "price": "4.99", "priceCurrency": "USD", "url": U()}]}
home_ld = ld([{"@context": "https://schema.org", **ORG},
              {"@context": "https://schema.org", "@type": "WebSite", "@id": U() + "#site", "name": "BotToBook", "url": U(), "inLanguage": "en-US", "publisher": {"@id": U() + "#org"}},
              {"@context": "https://schema.org", **app}, faq_ld(C.HOME_FAQ)])
for k, v in {'<!--SEO-HEAD-->': head, '<!--LDJSON-->': home_ld, '<!--HOME-FAQ-->': faq_html(C.HOME_FAQ), '<!--FACTS-->': C.facts_table(),
             '<!--FOOTLINKS-->': FOOTLINKS, '<!--UPDATED-->': upd_human, '{GITHUB}': C.GITHUB, '{EMAIL}': C.EMAIL}.items():
    assert k in s, k
    s = s.replace(k, v)
if product:
    assert re.fullmatch(r'pdt_[A-Za-z0-9]+', product)
    s = s.replace('__PRODUCT_ID__', product)
    fn = root / 'functions/api/license.js'
    fn.write_text(re.sub(r'const PRODUCT_ID = "[^"]*";', f'const PRODUCT_ID = "{product}";', fn.read_text()))
(pub / 'index.html').write_text(s)

# ── Sub-pages ─────────────────────────────────────────────────────────────────
PAGE_CSS = FONT_FACES + """:root{color-scheme:light dark;--bg:light-dark(#fffdf9,#120c18);--ink:light-dark(#21182b,#f1eaf6);--soft:light-dark(#6a5e74,#b5a8c0);--paper:light-dark(#f7f1e7,#1c1424);--line:light-dark(#e6dccd,#352944);--cloth:#3b2350;--cloth2:light-dark(#2c1a3d,#1a1024);--gold:#f2b33d;--goldink:light-dark(#9a5f00,#f6c76a)}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.65 "Instrument Sans",system-ui,sans-serif}
a{color:var(--goldink)}h1,h2{font-family:Fraunces,Georgia,serif;line-height:1.12;text-wrap:balance}
.top{background:var(--cloth);color:#fff;padding:18px 0 34px}.top a{color:#fff;text-decoration:none}
.wrap{max-width:780px;margin:0 auto;padding:0 max(4vw,18px)}
.brand{font-weight:600;display:inline-flex;gap:8px;align-items:center}.brand i{width:20px;height:15px;background:#fff;border-radius:3px;box-shadow:inset -5px 0 0 var(--gold)}
.crumbs{font-size:14px;color:#dccfe8;margin:18px 0 6px}.crumbs a{color:#eadff3;text-decoration:underline}
.top h1{font-size:clamp(30px,4.6vw,44px);margin:6px 0 0}
main{padding:28px 0 40px}.answer{font-size:19px;line-height:1.6;border-left:4px solid var(--gold);padding:4px 0 4px 16px;margin:0 0 18px}
.cta{display:inline-flex;align-items:center;min-height:48px;padding:0 22px;border-radius:12px;background:var(--gold);color:#2a1a00;font-weight:600;text-decoration:none}
.meta{font-size:14px;color:var(--soft);margin:14px 0 26px}
h2{font-size:clamp(23px,3vw,29px);margin:34px 0 10px}li{margin:6px 0}
code{font:.9em ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;background:var(--paper);padding:1px 5px;border-radius:5px}
pre{background:var(--paper);border:1px solid var(--line);border-radius:10px;padding:14px;overflow:auto}pre code{background:none;padding:0}
.facts{border-collapse:collapse;width:100%;margin:12px 0;border:1px solid var(--line);font-size:15px}.facts caption{text-align:left;color:var(--soft);font-size:13px;padding-bottom:6px}
.facts th,.facts td{padding:9px 12px;border-top:1px solid var(--line);text-align:left;vertical-align:top}.facts th{width:30%}
figure{margin:18px 0}figure img{width:100%;height:auto;border:1px solid var(--line);border-radius:10px;background:#888}figcaption{font-size:14px;color:var(--soft);margin-top:6px}
details{border-bottom:1px solid var(--line);padding:4px 0}summary{cursor:pointer;font-weight:600;min-height:44px;display:flex;align-items:center}details p{margin:2px 0 14px;color:var(--soft)}
.related{background:var(--paper);border-radius:12px;padding:16px 18px;margin-top:30px}.related ul{margin:6px 0 0;padding-left:20px}
footer{background:var(--cloth2);color:#dccfe8;font-size:14px;padding:24px 0}footer a{color:#fff}.foot{display:flex;flex-wrap:wrap;gap:6px 16px;margin-bottom:10px}
a:focus-visible,summary:focus-visible{outline:3px solid var(--gold);outline-offset:2px}"""

def shell(title, desc, canon, h1, crumb, body_html, ldnodes):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{tx(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<meta property="og:type" content="article"><meta property="og:site_name" content="BotToBook"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}"><meta property="og:image" content="{site}og.png"><meta name="twitter:card" content="summary_large_image">
<link rel="preload" href="/fonts/fraunces-latin-700-normal.woff2" as="font" type="font/woff2" crossorigin>
{ld(ldnodes)}
<style>{PAGE_CSS}</style>
<script src="/found.js" defer></script>
</head>
<body>
<header class="top"><div class="wrap">
  <a class="brand" href="/"><i></i>BotToBook</a>
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">BotToBook</a> › {tx(crumb)}</nav>
  <h1>{tx(h1)}</h1>
</div></header>
<main class="wrap">
{body_html}
</main>
<footer><div class="wrap">{FOOTLINKS}BotToBook is an independent tool. It is not affiliated with, endorsed by or connected to Character Technologies, Inc. or Character.AI. Questions: <a href="mailto:{C.EMAIL}">{C.EMAIL}</a> · Last updated: {upd_human}</div></footer>
</body>
</html>
"""

def crumbs_ld(name, url):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "BotToBook", "item": U()},
        {"@type": "ListItem", "position": 2, "name": name, "item": url}]}

for p in C.PAGES:
    url = U(p['slug'])
    body = (f'<p class="answer">{tx(p["answer"])}</p>\n<a class="cta" href="/">Open my export in BotToBook</a>\n'
            f'<p class="meta">Last updated: <time datetime="{C.LAST_UPDATED}">{upd_human}</time> · Free to read, nothing uploaded</p>\n'
            + p['body'].replace('{FACTS}', C.facts_table())
            + f'\n<h2>Questions</h2>\n{faq_html(p["faq"])}\n'
            + '<aside class="related"><b>Related guides</b><ul>' + ''.join(f'<li><a href="/{s}/">{tx(PAGES[s]["title"])}</a></li>' for s in p['links'])
            + '<li><a href="/">BotToBook: Character.AI chat to PDF &amp; EPUB</a></li></ul></aside>')
    article = {"@context": "https://schema.org", "@type": "TechArticle", "headline": p['title'], "description": p['description'], "url": url,
               "inLanguage": "en-US", "datePublished": C.PUBLISHED, "dateModified": C.LAST_UPDATED,
               "author": {"@id": U() + "#org"}, "publisher": {"@context": "https://schema.org", **ORG}, "mainEntityOfPage": url}
    out = pub / p['slug']; out.mkdir(exist_ok=True)
    (out / 'index.html').write_text(shell(p['title'], p['description'], url, p['h1'], p['crumb'], body, [crumbs_ld(p['crumb'], url), article, faq_ld(p['faq'])]))

# Privacy & refunds
priv = f"""<p class="answer">BotToBook opens your Character.AI export and makes your books inside your own browser. Your chats are never uploaded, stored or seen by us. This page explains the few things that do leave your device.</p>
<p class="meta">Last updated: <time datetime="{C.LAST_UPDATED}">{upd_human}</time></p>
<h2>Your chats</h2><p>The ZIP or JSON files you open are read by JavaScript on the page. Decryption, reading and book-making all happen on your device. Nothing from your export is sent to a server.</p>
<h2>License keys</h2><p>When you activate BotToBook Pro, your license key is sent to our small checking service (a Cloudflare Pages Function), which asks Dodo Payments whether the key is valid for BotToBook. The key and an activation ID are saved in your browser's local storage so Pro stays unlocked. We don't receive your chats, and the checking service doesn't keep the key.</p>
<h2>Payments</h2><p>Payments are processed by Dodo Payments, the merchant of record, which handles your card details, sales tax and receipts under its own privacy policy. We never see your card number.</p>
<h2>Hosting and logs</h2><p>The site is hosted on Cloudflare Pages. Like any web host, Cloudflare processes standard request data such as IP addresses to deliver and protect the site. BotToBook uses no cookies, ads or third-party analytics. To learn which sites and AI assistants send visitors, the first page you open sends one anonymous note to our own server: the name of the site you came from (such as “google” or “chatgpt”, never the full address), the page and your country. After you save a book or file, a small optional card asks how you found the site; if you answer, your choice and anything you type in the optional box are stored the same way. None of this includes your chats, your export, your IP address or any ID.</p>
<h2>Refunds</h2><p>If BotToBook doesn't work with your export, email <a href="mailto:{C.EMAIL}">{C.EMAIL}</a> within 14 days of buying and we'll refund you.</p>
<h2>Contact</h2><p>BotToBook is an independent tool by YanSquared. Email <a href="mailto:{C.EMAIL}">{C.EMAIL}</a>.</p>"""
(pub / 'privacy').mkdir(exist_ok=True)
(pub / 'privacy/index.html').write_text(shell('Privacy & Refunds | BotToBook', 'How BotToBook handles your Character.AI export (it stays on your device), license keys, payments and refunds.',
                                             U('privacy'), 'Privacy & refunds', 'Privacy & refunds', priv, [crumbs_ld('Privacy & refunds', U('privacy'))]))

# ── robots, sitemap, llms.txt ─────────────────────────────────────────────────
(pub / 'robots.txt').write_text(f"""User-agent: *
Allow: /

User-agent: GPTBot
User-agent: OAI-SearchBot
User-agent: ChatGPT-User
User-agent: ClaudeBot
User-agent: Claude-SearchBot
User-agent: Claude-User
User-agent: PerplexityBot
User-agent: Perplexity-User
User-agent: Google-Extended
User-agent: Applebot-Extended
User-agent: CCBot
Allow: /

Sitemap: {site}sitemap.xml
""")
urls = [U()] + [U(p['slug']) for p in C.PAGES] + [U('privacy')]
(pub / 'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    + ''.join(f'  <url><loc>{u}</loc><lastmod>{C.LAST_UPDATED}</lastmod></url>\n' for u in urls) + '</urlset>\n')
facts_txt = '\n'.join(f'- {re.sub("<[^>]+>", "", a)}: {re.sub("<[^>]+>", "", b)}' for a, b in C.FACTS_ROWS)
(pub / 'llms.txt').write_text(f"""# BotToBook

> BotToBook is a free browser-based viewer for Character.AI data exports. It opens the password-protected export ZIP or message.json on the user's device and can turn the chats into a PDF, EPUB or HTML book. Nothing is uploaded. Viewing and text export are free; full books cost $4.99 once. Not affiliated with Character Technologies, Inc.

## Key facts about the Character.AI data export (checked November 2026)
{facts_txt}

## Who it's for
{C.QA["forwho"][1]}

## Questions and answers
""" + ''.join(f"### {q}\n{a}\n\n" for q, a in C.QA.values()) + f"""## Pages
- [Tool: Character.AI chat to PDF and EPUB]({U()})
""" + ''.join(f"- [{p['crumb']}]({U(p['slug'])}): {p['description']}\n" for p in C.PAGES) + f"- [Privacy and refunds]({U('privacy')})\n\n## Also by the same maker\n- [FicToEpub](https://fictoepub.pages.dev/): AO3 HTML to EPUB converter\n- [FicWrapped](https://ficwrapped.yansquared.com/): AO3 Wrapped from your own reading history\n\nLast updated: {C.LAST_UPDATED}. Contact: {C.EMAIL}\n")
print('built for', site, 'product', product or '(none yet)', '·', len(urls), 'urls')
