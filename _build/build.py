#!/usr/bin/env python3
"""Builds the TEMIS static site (GitHub Pages) from page bodies in pages/."""
import pathlib
ROOT = pathlib.Path(__file__).parent

def B(en, es):
    return f'<span class="en">{en}</span><span class="es">{es}</span>'

SEAL = '''<svg viewBox="0 0 64 64" aria-hidden="true"><circle cx="32" cy="32" r="30" fill="none" stroke="currentColor" stroke-width="1.4" opacity=".55"/><circle cx="32" cy="32" r="26" fill="none" stroke="currentColor" stroke-width=".8" opacity=".35"/><g fill="none" stroke="#A9844B" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M32 15v32M24 48h16"/><path d="M17 22h30"/><path d="M17 22l-5 11h10zM47 22l-5 11h10z"/><path d="M12 33a5 3 0 0 0 10 0M42 33a5 3 0 0 0 10 0"/></g><circle cx="32" cy="15" r="2.4" fill="#A9844B"/></svg>'''

COLUMNS = '''<svg class="columns" viewBox="0 0 520 300" aria-hidden="true" fill="none" stroke="#fff" stroke-width="2"><path d="M20 90 L260 10 L500 90 Z"/><path d="M40 90h440M30 100h460"/>''' + ''.join(
    f'<path d="M{x} 110v150M{x+30} 110v150M{x-6} 104h42M{x-6} 266h42"/>' + ''.join(f'<path d="M{x+7+i*8} 114v142"/>' for i in range(2))
    for x in (60, 160, 260, 360, 440)) + '<path d="M20 280h480M10 292h500"/></svg>'

ICON = {
 'check': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>',
 'shield': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/></svg>',
 'book': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19V5a2 2 0 0 1 2-2h14v16H6a2 2 0 0 0-2 2zM20 19v2H6"/></svg>',
 'user': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="8" r="4"/><path d="M4 21c1-4 4-6 8-6s7 2 8 6"/></svg>',
 'car': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 16h14M3 16v-3l2-5h14l2 5v3"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/></svg>',
 'receipt': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6"/></svg>',
 'brief': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="7" width="18" height="13" rx="2"/><path d="M9 7V5a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2M3 13h18"/></svg>',
 'doc': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 3H6v18h12V7z"/><path d="M14 3v4h4M9 13h6M9 17h6"/></svg>',
 'chat': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.5A8 8 0 1 1 21 12z"/></svg>',
 'scale': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 4v16M8 20h8M5 7h14M5 7l-3 6h6zM19 7l-3 6h6z"/></svg>',
 'link': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg>',
 'pin': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 21s-7-6-7-11a7 7 0 0 1 14 0c0 5-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
 'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
 'clock': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
}

NAV = [
 ('index.html', 'Home', 'Inicio'),
 ('solution.html', 'Solution', 'Solución'),
 ('demo.html', 'Demo', 'Demo'),
 ('research.html', 'Research', 'Investigación'),
 ('video.html', 'Video', 'Video'),
 ('contact.html', 'Contact', 'Contacto'),
]

def header(active):
    links = ''.join(
        f'<a href="{h}"' + (' aria-current="page"' if h == active else '') + f'>{B(en, es)}</a>'
        for h, en, es in NAV)
    return f'''<div class="topbar"><div class="wrap"><span>{B("Universidad Militar Nueva Granada · Emerging technology proposal","Universidad Militar Nueva Granada · Propuesta de tecnología emergente")}</span>
<div class="lang" role="group" aria-label="Language"><button type="button" data-l="en" aria-pressed="true">EN</button><button type="button" data-l="es" aria-pressed="false">ES</button></div></div></div>
<header class="site"><div class="wrap">
<a class="logo" href="index.html" aria-label="TEMIS home" style="color:var(--navy)">{SEAL}<span><span class="name">TEMIS</span><span class="tagline">{B("Virtual legal clinic","Consultorio jurídico virtual")}</span></span></a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="mainnav">{B("Menu","Menú")}</button>
<nav class="main" id="mainnav" aria-label="Main">{links}</nav>
<a class="btn primary sm cta-nav" href="demo.html">{B("Try TEMIS","Probar TEMIS")}</a>
</div></header>'''

def footer():
    return f'''<footer class="site"><div class="wrap">
<div class="cols">
 <div><a class="logo" href="index.html" style="color:#fff">{SEAL}<span><span class="name">TEMIS</span><span class="tagline">{B("Virtual legal clinic","Consultorio jurídico virtual")}</span></span></a>
 <p style="margin-top:18px;max-width:38ch">{B("Clear legal guidance when you don't know where to start. Named after Themis, Greek goddess of justice.","Orientación jurídica clara cuando no sabes por dónde empezar. Inspirado en Temis, diosa griega de la justicia.")}</p></div>
 <div><h4>{B("Explore","Explora")}</h4><ul><li><a href="solution.html">{B("How it works","Cómo funciona")}</a></li><li><a href="demo.html">{B("Product demo","Demo del producto")}</a></li><li><a href="video.html">{B("Pitch video","Video pitch")}</a></li></ul></div>
 <div><h4>{B("Research","Investigación")}</h4><ul><li><a href="research.html#articles">{B("Articles","Artículos")}</a></li><li><a href="research.html#patents">{B("Patents","Patentes")}</a></li><li><a href="research.html#references">{B("References","Referencias")}</a></li></ul></div>
 <div><h4>{B("Contact","Contacto")}</h4><ul><li><a href="contact.html">{B("For people","Para personas")}</a></li><li><a href="contact.html#companies">{B("For firms &amp; institutions","Para bufetes e instituciones")}</a></li><li>Bogotá, Colombia</li></ul></div>
</div>
<div class="legal"><span>© 2026 TEMIS · Óscar Leonel Peña Báez · Laura Salazar · Rafael Garzon · UMNG</span><span>{B("TEMIS offers initial guidance and does not replace a lawyer.","TEMIS ofrece orientación inicial y no reemplaza a un abogado.")}</span></div>
</div></footer>'''

def page(fname, title, body, extra_js=''):
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="TEMIS: virtual legal clinic powered by generative AI. Clear legal guidance when you don't know where to start.">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect width='24' height='24' rx='6' fill='%230E2238'/%3E%3Cpath d='M12 5v13M9 18h6M6 8h12M6 8l-2.5 5h5zM18 8l-2.5 5h5z' fill='none' stroke='%23A9844B' stroke-width='1.6' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500&family=Manrope:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
{header(fname)}
<main>
{body}
</main>
{footer()}
<script src="assets/app.js"></script>
{extra_js}
</body>
</html>
'''
    (ROOT / fname).write_text(html, encoding='utf-8')

if __name__ == '__main__':
    import importlib.util
    spec = importlib.util.spec_from_file_location('bodies', ROOT / 'bodies.py')
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    for fname, title, body, js in m.pages(B, SEAL, COLUMNS, ICON):
        page(fname, title, body, js)
    print('built', [p[0] for p in m.pages(B, SEAL, COLUMNS, ICON)])
