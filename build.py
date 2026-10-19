#!/usr/bin/env python3
"""worldofswos.com: a static site generated from the SWOS 96/97 Mod's own release data.

  python3 build.py --refresh   read the mod's release texts into data/ (read-only on ~/swos-mod), then build
  python3 build.py             build site/ from data/ (no access to the mod's repo needed)

data/ holds only public texts: the release notes and competition lists without their HTML comments (staged and
internal parts), and the in-game FORMAT page texts (FMTxx), which ship with the patcher anyway.
Environment: SWOS_MOD (default ~/swos-mod), SWOS_REF (default world-2025-26), FMT_PACKS (the release build's world
packs, for the FORMAT texts and the countries' names in the four languages).
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.abspath(__file__))
import hashlib  # noqa: E402
VER = hashlib.md5(b''.join(open(os.path.join(ROOT, 'static', f), 'rb').read() for f in ('style.css', 'site.js'))).hexdigest()[:8]
sys.path.insert(0, os.path.join(ROOT, 'gen'))
import md                                                   # noqa: E402
import tr                                                   # noqa: E402
import classic                                              # noqa: E402
import ogimage                                              # noqa: E402
from i18n import CONTINENT, GAME, LANG_NAME, LANGS, LOCALE, T   # noqa: E402

SITE_URL = 'https://worldofswos.com'
REPO = 'https://github.com/aminta/swos-9697-mod'
# 4.0 is not released yet: both point to the releases page (at release: /releases/latest/download/swos-9697-mod-patcher.html)
PATCHER = REPO + '/releases/latest/download/swos-9697-mod-patcher.html'
RELEASES = REPO + '/releases'
RELEASED = False        # False until 4.0 is on GitHub: download buttons and the install section say "Coming soon"
TWELVE_BIT_URL = 'https://www.facebook.com/retrogaming12bit'   # https://12bit.it when the new site is out
_tb = '<img class="assoc-logo" src="/static/img/12bit.png" width="64" height="80" alt="12 Bit Retrogaming, associazione culturale (Trieste)">'
TWELVE_BIT = f'<a href="{TWELVE_BIT_URL}">{_tb}</a>' if TWELVE_BIT_URL else _tb
GOATCOUNTER = 'worldofswos'  # GoatCounter code (https://<code>.goatcounter.com): cookieless visit counter; '' = none
DATA = os.path.join(ROOT, 'data')
OUT = os.path.join(ROOT, 'site')
CONTS = ['europe', 'north_america', 'south_america', 'asia', 'oceania', 'africa']
CONT_MD = {'Europe': 'europe', 'North and Central America': 'north_america', 'South America': 'south_america',
           'Asia': 'asia', 'Oceania': 'oceania', 'Africa': 'africa', 'Europa': 'europe',
           'Nord e Centro America': 'north_america', 'Sud America': 'south_america'}


# ------------------------------------------------------------------------------------------------ refresh (import)
def refresh():
    mod = os.path.expanduser(os.environ.get('SWOS_MOD', '~/swos-mod'))
    ref = os.environ.get('SWOS_REF', 'world-2025-26')
    # the world data dir of the FINAL release build c/REL40 (Regia, 2026-10-19 evening)
    packs = os.environ.get('FMT_PACKS') or os.path.join(mod, 'internal', 'world2526', 'world5tm-rel40-names-2200')
    packs = os.path.expanduser(packs)
    os.makedirs(DATA, exist_ok=True)

    def show(path):
        return subprocess.run(['git', '-C', mod, 'show', f'{ref}:{path}'], check=True, capture_output=True,
                              text=True).stdout

    sha = subprocess.run(['git', '-C', mod, 'rev-parse', '--short', ref], check=True, capture_output=True,
                         text=True).stdout.strip()
    for src, dst in [('release/notes-world-2026-27.md', 'notes-world-2026-27.md'),
                     ('release/world-2026-27-competitions.md', 'competitions.md')]:
        open(os.path.join(DATA, dst), 'w', encoding='utf-8').write(md.strip_comments(show(src)))
    # the in-game FORMAT texts and the countries' names, with the mod's own tools (exported, never run in the repo)
    with tempfile.TemporaryDirectory() as tmp:
        tref = os.environ.get('FMT_TOOLS_REF', ref)    # (a fix branch of tools/fmtgame.py not merged yet)
        arch = subprocess.run(['git', '-C', mod, 'archive', tref, 'tools', 'packs'], check=True,
                              capture_output=True).stdout
        subprocess.run(['tar', '-x', '-C', tmp], input=arch, check=True)
        code = ('import sys, os, json\nsys.path.insert(0, sys.argv[1])\nimport fmtgame\nd = sys.argv[2]\nout = {}\n'
                'for s in sorted(os.listdir(d)):\n'
                '    p = os.path.join(d, s, "pack.json")\n'
                '    if not os.path.exists(p): continue\n'
                '    pk = json.load(open(p))\n'
                '    items = [{"title": t, "text": {l: [x if isinstance(x, str) else " ".join(x) for x in tx[l]] '
                'for l in tx}} for w, cid, t, tx in fmtgame.from_pack(os.path.join(d, s))]\n'
                '    out[s] = {"names": pk["button_names"], "continent": pk["continent"], "fmt": items}\n'
                'json.dump(out, open(sys.argv[3], "w"), ensure_ascii=False, indent=0)\n')
        dst = os.path.join(DATA, 'countries.json')
        subprocess.run([sys.executable, '-I', '-c', code, os.path.join(tmp, 'tools'), packs, dst], check=True,
                       cwd=tmp)
    ver = open(os.path.join(packs, 'VERSION.txt')).read().split('\n')[0] if os.path.exists(
        os.path.join(packs, 'VERSION.txt')) else ''
    json.dump({'ref': ref, 'tools': os.environ.get('FMT_TOOLS_REF', ref), 'sha': sha, 'packs': os.path.basename(packs), 'packs_date': ver},
              open(os.path.join(DATA, 'source.json'), 'w'), indent=1)
    print(f'data/: {ref} {sha}, FORMAT texts from {os.path.basename(packs)}')


# ------------------------------------------------------------------------------------------------ data model
def split_langs(text):
    """The notes: '## English' and '## Italiano' parts."""
    parts, cur = {}, None
    for line in text.split('\n'):
        if line.strip() == '## English':
            cur = 'en'
            parts[cur] = []
            continue
        if line.strip() == '## Italiano':
            cur = 'it'
            parts[cur] = []
            continue
        if cur:
            parts[cur].append(line)
    return {k: '\n'.join(v) for k, v in parts.items()}


def load():
    countries = json.load(open(os.path.join(DATA, 'countries.json'), encoding='utf-8'))
    by_en = {v['names']['en'].upper(): k for k, v in countries.items()}
    comp = open(os.path.join(DATA, 'competitions.md'), encoding='utf-8').read()
    halves = re.split(r'^## ', comp, flags=re.M)
    lists = {}
    for h in halves[1:]:
        lang = 'en' if h.startswith('Every country') else 'it'
        conts, cont, cur = [], None, None
        for b in md.blocks('## ' + h):
            if b[0] == 'h' and b[1] == 3:
                cont = CONT_MD.get(b[2], b[2])
            elif b[0] == 'h' and b[1] == 4:
                cur = {'name': b[2], 'cont': cont, 'items': []}
                conts.append(cur)
            elif b[0] == 'list' and cur:
                cur['items'] += b[1]
        lists[lang] = conts
    order = []
    for i, c in enumerate(lists['en']):
        code = by_en.get(c['name'].upper())
        if not code:
            raise SystemExit(f'country not found in the packs: {c["name"]}')
        order.append(code)
        countries[code]['md'] = {'en': c['items'], 'it': lists['it'][i]['items']}
        countries[code]['cont'] = c['cont']
    notes = split_langs(open(os.path.join(DATA, 'notes-world-2026-27.md'), encoding='utf-8').read())
    src = json.load(open(os.path.join(DATA, 'source.json')))
    stats = {}
    m = re.search(r'(\d+) countries, (\d+) league divisions, (\d+) national cups, (\d+) league cups', notes['en'] + notes['it'])
    if m:
        stats = dict(zip(['countries', 'divisions', 'cups', 'lcups'], m.groups()))
    m = re.search(r'([\d,]+) clubs', notes['en'])
    stats['clubs'] = m.group(1) if m else ''
    return dict(countries=countries, order=order, notes=notes, stats=stats, src=src)


# ------------------------------------------------------------------------------------------------ page shell
def esc(s):
    return html.escape(s, quote=True)


def logo_svg(size=44, title=None):
    """A pixel football that is also a planet, with an orbit: World of SWOS's own mark."""
    art = ['.....WWWWWW.....',
           '...WWWWBBWWWWS..',
           '..WWWWBBBBWWWWS.',
           '.WBWWWWBBWWWWBS.',
           '.WBBWWWWWWWWBBS.',
           'WBBBWWWWWWWWBBBS',
           'WWBWWWBBBBWWWBWS',
           'WWWWWBBBBBBWWWWS',
           'WWWWWBBBBBBWWWSS',
           'WWWWWWBBBBWWWWSS',
           'WBWWWWWWWWWWWBSS',
           'WBBWWWWWWWWWBBSS',
           '.WBBWWWBBWWBBSS.',
           '..WWWWBBBBWWSS..',
           '...WWWWBBWSSS...',
           '.....SSSSSS.....']
    col = {'W': '#e8edff', 'B': '#0b1d7a', 'S': '#8fa2ee'}
    px = ''.join(f'<rect x="{x + 4}" y="{y + 4}" width="1.02" height="1.02" fill="{col[c]}"/>'
                 for y, row in enumerate(art) for x, c in enumerate(row) if c in col)
    t = f'<title>{esc(title)}</title>' if title else ''
    ring = '<ellipse cx="12" cy="12" rx="11.3" ry="3.6" transform="rotate(-24 12 12)" fill="none" ' \
           'stroke="#ffd84a" stroke-width="1.3"'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="{size}" height="{size}" '
            f'shape-rendering="crispEdges" role="img"{" aria-hidden=\"true\"" if not title else ""}>{t}'
            f'{ring} stroke-dasharray="0 17.6 40"/>{px}{ring} stroke-dasharray="17.6 40"/>'
            '<rect x="20" y="5" width="2" height="2" fill="#ff9a3c"/></svg>')


NAV = [('home', ''), ('world', 'world/'), ('countries', 'countries/'), ('classic', 'classic/'), ('install', '#install'),
       ('credits', 'credits/')]


def counter(lang):
    if not GOATCOUNTER:
        return ''
    g = f'https://{GOATCOUNTER}.goatcounter.com'
    # counting only: the numbers are on Davide's GoatCounter dashboard, not shown on the site
    return f'<script data-goatcounter="{g}/count" async src="https://gc.zgo.at/count.js"></script>'


def page(lang, path, title, body, desc='', active=None, langs=None):
    """path: the page's path after /<lang>/ ('' = home). langs: the languages this page exists in."""
    t = T[lang]
    langs = langs or LANGS
    url = f'/{lang}/{path}'
    nav = []
    for key, p in NAV:
        href = f'/{lang}/' + ('' if p.startswith('#') else p) + (p if p.startswith('#') else '')
        cur = ' aria-current="page"' if key == active else ''
        nav.append(f'<a href="{href}"{cur}>{esc(t["nav_" + key])}</a>')
    sw = ''.join(f'<a href="/{l}/{path}" hreflang="{l}" lang="{l}" title="{LANG_NAME[l]}"'
                 f'{" aria-current=\"true\"" if l == lang else ""}>{l.upper()}</a>' for l in langs)
    alt = ''.join(f'<link rel="alternate" hreflang="{l}" href="{SITE_URL}/{l}/{path}">' for l in langs)
    alt += f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/en/{path}">'
    full = f'{title} · {t["site"]}' if title != t['site'] else f'{t["site"]} · {t["sub"]}'
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc or t['meta_home'])}">
<link rel="canonical" href="{SITE_URL}{url}">{alt}
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc or t['meta_home'])}">
<meta property="og:type" content="website"><meta property="og:url" content="{SITE_URL}{url}">
<meta property="og:locale" content="{LOCALE[lang]}">
<meta property="og:image" content="{SITE_URL}/static/og-{lang}.png"><meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630"><meta property="og:image:alt" content="{esc(t['tagline'])}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0a1a6e">
<link rel="icon" href="/static/logo.svg" type="image/svg+xml">
<link rel="preload" href="/static/fonts/silkscreen-700-latin.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/static/style.css?v={VER}">
<script src="/static/site.js?v={VER}" defer></script>
</head>
<body>
<a class="skip" href="#main">{esc(t['skip'])}</a>
<header class="top"><div class="wrap">
<a class="brand" href="/{lang}/"><img src="/static/logo.svg" alt="" width="44" height="44"><span>World of SWOS<small>{esc(t['sub'])}</small></span></a>
<button class="btn blue menu-btn" type="button" aria-expanded="false" aria-controls="nav">{esc(t['menu'])}</button>
<nav class="lang" aria-label="{esc(t['lang_label'])}">{sw}</nav>
<nav class="nav" id="nav" aria-label="{esc(t['menu'])}">{''.join(nav)}</nav>
</div></header>
<main id="main">
{body}
</main>
<footer class="foot"><div class="wrap">
<p><strong>{esc(t['unofficial'])}</strong></p>
<div class="assoc">{TWELVE_BIT}<p>{esc(t['by'])} <a href="{REPO}">{esc(t['source'])}</a>.</p></div>{counter(lang)}
</div></footer>
</body>
</html>
'''


# ------------------------------------------------------------------------------------------------ pages
def fmt_num(n, lang):
    n = str(n).replace(',', '')
    if not n.isdigit():
        return n
    sep = {'en': ',', 'it': '.', 'fr': ' ', 'de': '.'}[lang]
    return f'{int(n):,}'.replace(',', sep)


def home(d, lang):
    t, s = T[lang], d['stats']
    stats = ''.join(f'<div class="stat"><b>{fmt_num(s[k], lang)}</b><span>{esc(t["s_" + k])}</span></div>'
                    for k in ['countries', 'clubs', 'divisions', 'cups', 'lcups'] if s.get(k))
    cards = ''.join(f'<article class="card"><h3>{esc(h)}</h3><p>{esc(p)}</p></article>' for h, p in t['cards'])
    steps = ''.join('<li>' + st.format(careers=f'<strong>{GAME["careers"][lang]}</strong>',
                                         world=f'<strong>{GAME["world"][lang]}</strong>') + '</li>'
                    for st in t['steps'])
    shots = ''                                      # groups of frames; a frame not captured yet is left out
    def have(f):
        return os.path.exists(os.path.join(ROOT, 'static', 'img', f + '.png'))

    for g, items in t['shots']:
        figs = ''
        for f, c in items:                          # name-it: this language's capture when there is one
            fl = f[:-3] + '-' + lang if f.endswith('-it') and have(f[:-3] + '-' + lang) else f
            if have(fl):
                figs += (f'<figure class="shot"><img src="/static/img/{fl}.png" width="1600" height="1200" '
                         f'loading="lazy" alt="{esc(c)}"><figcaption>{esc(c)}</figcaption></figure>')
            else:
                figs += (f'<figure class="shot soon"><div class="soon-box"><span>{esc(t["soon"])}</span></div>'
                         f'<figcaption>{esc(c)}</figcaption></figure>')
        if figs:
            shots += (f'<h3>{esc(g)}</h3><div class="cards" style="grid-template-columns:repeat(auto-fill,'
                      f'minmax(min(100%,440px),1fr))">{figs}</div>')
    if RELEASED:
        dl_btn = f'<a class="btn green" href="{PATCHER}">{esc(t["dl"])}<small>{esc(t["dl_small"])}</small></a>'
        dl_btn2 = f'<a class="btn green" href="{PATCHER}">{esc(t["dl"])}</a>'
        soon_inst = ''
    else:
        dl_btn = dl_btn2 = ''                       # the red "coming soon" sticker at the top of the page instead
        soon_inst = f'<p class="panel"><strong class="px" style="color:var(--gold)">{esc(t["soon"])}</strong> {esc(t["soon_install"])}</p>'
    sticker = '' if RELEASED else (f'<p class="soon-sticker" role="note"><b>{esc(t["soon"])}</b>'
                                   f'<span>{esc(t["soon_dl"])}</span></p>')
    body = f'''<section class="hero"><div class="wrap">{sticker}
{logo_svg(240, t['site']).replace('<svg ', '<svg class="logo" ', 1)}
<p class="px" style="color:var(--dim);margin:0 0 14px">{esc(t['kicker'])}</p>
<h1>{esc(t['tagline'])}</h1>
<p class="tagline">{esc(t['concept'])}</p>
<p class="lead">{esc(t['lead'])}</p>
<div class="cta">
{dl_btn}
<a class="btn orange" href="#install">{esc(t['how'])}</a>
<a class="btn blue" href="/{lang}/countries/">{esc(t['see_world'])}</a>
</div>
<div class="stats">{stats}</div>
</div></section>
<section class="wrap">
<h2>{esc(t['h_what'])}</h2>
{''.join(f'<p>{p}</p>' for p in t['what'])}
<h2>{esc(t['h_high'])}</h2>
<div class="cards">{cards}</div>
<h2>{esc(t['h_classic'])}</h2>
<p>{t['classic']}</p>
<h2 id="next">{esc(t['h_next'])}</h2>
<div class="panel next"><p><span class="next-tag px">4.1</span> {esc(t['next41'])}</p>
<p><span class="next-tag px">4.2</span> {esc(t['next_text'])}</p>
<p class="note" style="margin:0">{esc(t['next_note'])}</p></div>
<h2>{esc(t['h_shots'])}</h2>
{shots}
<h2 id="install">{esc(t['h_install'])}</h2>
{soon_inst}<ol class="steps">{steps}</ol>
<p class="note" style="margin-top:14px">{esc(t['install_note'])}</p>
<p class="cta" style="justify-content:flex-start">{dl_btn2}
<a class="btn blue" href="{RELEASES}">GitHub Releases</a></p>
</section>'''
    return page(lang, '', t['site'], body, active='home')


def _split_top(s):
    """'a; b (c; d); e' -> ['a', 'b (c; d)', 'e']"""
    out, depth, cur = [], 0, ''
    for i, ch in enumerate(s):
        depth += ch == '('
        depth -= ch == ')'
        if ch == ';' and depth == 0 and s[i + 1:i + 2] == ' ':
            out.append(cur.strip())
            cur = ''
            continue
        cur += ch
    out.append(cur.strip())
    return [x for x in out if x]


def comp_cards(items, lang):
    t = T[lang]
    out = []
    for txt, kids in items:
        m = re.match(r'^(\*[^*]+\*|[^:]+?)(?: \(([^)]+)\))?: (.*)$', txt)
        if not m:
            out.append(f'<li class="comp"><p>{md.inline(txt)}</p></li>')
            continue
        name, kind, rest = m.groups()
        cls = 'comp approx' if name.startswith('*') else 'comp'
        name = name.strip('*')
        badge = f'<span class="kind">{esc(kind)}</span>' if kind else ''
        facts = ' · '.join(md.inline(x) for x in _split_top(rest))
        sub = ''
        for ktxt, _ in kids:
            km = re.match(r'^([^:]+?)(?: \(([^)]+)\))?: (.*)$', ktxt)
            if km:
                kb = f' <span class="kind">{esc(km.group(2))}</span>' if km.group(2) else ''
                sub += f'<li><strong>{md.inline(km.group(1))}</strong>{kb}: {md.inline(km.group(3))}</li>'
            else:
                sub += f'<li>{md.inline(ktxt)}</li>'
        out.append(f'<li class="{cls}"><span class="name">{md.inline(name)}</span>{badge}<p class="facts">{facts}</p>{f'<ul>{sub}</ul>' if sub else ''}</li>')
    return f'<ul class="comps">{"".join(out)}</ul>'


def screens(c, lang):
    name = c['names'][lang]
    out = []
    for it in c['fmt']:
        title = it['title'][lang]
        title = title[len(name) + 1:] if title.startswith(name + ' ') else title
        text = '\n'.join(it['text'][lang])
        out.append(f'<div class="screen"><span class="bar">{esc(title)}</span><pre>{esc(text)}</pre></div>')
    return f'<div class="screens">{"".join(out)}</div>'


def country(d, code, lang):
    t, c = T[lang], d['countries'][code]
    name = c['names'][lang]
    head = f'''<div class="wrap page-head">
<p class="crumbs"><a href="/{lang}/countries/">{esc(t['c_back'])}</a> › {esc(CONTINENT[c['cont']][lang])}</p>
<h1>{esc(name)}</h1>
<p>{esc(t['c_lead'].format(name=name))}</p></div>'''
    game = f'<p class="note">{esc(t["c_game_note"])}</p>{screens(c, lang)}'
    if lang in ('en', 'it'):
        body = (f'<div class="wrap">{comp_cards(c["md"][lang], lang)}'
                f'<details><summary>{esc(t["c_game"])}</summary>{game}</details></div>')
    else:
        body = (f'<div class="wrap"><h2>{esc(t["c_game"])}</h2>{game}'
                f'<details><summary>{esc(t["c_details"])}</summary>{comp_cards(c["md"]["en"], "en")}</details></div>')
    return page(lang, f'countries/{code}/', name, head + body, desc=t['c_lead'].format(name=name),
                active='countries')


def countries_index(d, lang):
    t = T[lang]
    secs = []
    for cont in CONTS:
        codes = [c for c in d['order'] if d['countries'][c]['cont'] == cont]
        if not codes:
            continue
        li = ''.join(f'<li><a href="/{lang}/countries/{c}/">{esc(d["countries"][c]["names"][lang])}'
                     f'<small>{esc(t["comps_n"].format(n=len(d["countries"][c]["fmt"])))}</small></a></li>'
                     for c in codes)
        secs.append(f'<section class="cont"><h2>{esc(CONTINENT[cont][lang])}</h2><ul class="grid-countries">{li}</ul>'
                    '</section>')
    body = (f'<div class="wrap page-head"><h1>{esc(t["h_countries"])}</h1>'
            f'<p>{esc(t["countries_lead"].format(n=len(d["order"])))}</p></div><div class="wrap">{"".join(secs)}</div>')
    return page(lang, 'countries/', t['h_countries'], body, active='countries')


def _notes_link(lang):
    def link(u):
        if u.endswith('world-2026-27-competitions.md'):
            return f'/{lang}/countries/'
        if u.startswith('http'):
            return u
        return None
    return link


def notes_part(d, lang):
    """The notes in this language (EN for FR / DE until translated), without the title line and credits."""
    src = d['notes']['it' if lang == 'it' else 'en']   # FR / DE: the English, translated block by block (gen/tr.py)
    bl = md.blocks(src)
    if bl and bl[0][0] == 'p' and bl[0][1].startswith('**'):
        bl = bl[1:]                                   # the release title line
    main, cred = bl, []
    for i, b in enumerate(bl):
        if b[0] == 'h' and b[1] == 4 and b[2] in ('Data and credits', 'Dati e crediti'):
            main, cred = bl[:i], bl[i:]
            break
    if lang in ('fr', 'de'):
        main, m1 = tr.translate(main, lang)
        cred, m2 = tr.translate(cred, lang)
        return main, cred, m1 + m2
    return main, cred, 0


# the harness frames per language; until a language's frame is right, the Italian one stands in
FRAMES = ['careers-menu', 'europe-countries', 'serie-a-table', 'cl-league-phase']   # (name-<lang>.png, Italian fallback)


def frames(lang):
    out = []
    for f, cap in zip(FRAMES, T[lang]['frames']):
        fl = lang if os.path.exists(os.path.join(ROOT, 'static', 'img', f'{f}-{lang}.png')) else 'it'
        out.append(f'<figure class="shot"><img src="/static/img/{f}-{fl}.png" width="1600" height="1200" '
                   f'loading="lazy" alt="{esc(cap)}"><figcaption>{esc(cap)}</figcaption></figure>')
    return f'<div class="cards" style="margin:18px 0 26px;grid-template-columns:repeat(auto-fill,minmax(min(100%,440px),1fr))">{"".join(out)}</div>'


def world(d, lang):
    t = T[lang]
    main, _, miss = notes_part(d, lang)
    heads = [(md.slug(b[2]), b[2]) for b in main if b[0] == 'h' and b[1] in (3, 4)]
    toc = ''.join(f'<li><a href="#{s}">{md.inline(h)}</a></li>' for s, h in heads)
    wip = f'<p class="panel">{esc(t["lang_wip"])}</p>' if miss else ''
    l2 = lang
    body = f'''<div class="wrap page-head"><h1>{esc(t['h_world'])}</h1><p class="tagline px" style="color:var(--gold)">
{esc(t['world_lead'])}</p></div>
<div class="wrap">{frames(lang)}</div>
<div class="wrap doc" lang="{l2}">{wip}<nav class="panel" aria-label="{esc(t['toc'])}"><strong>{esc(t['toc'])}</strong>
<ul class="toc">{toc}</ul></nav>
{md.render(main, _notes_link(lang), shift=-1, ids=md.slug)}</div>'''
    return page(lang, 'world/', t['h_world'], body, desc=t['meta_world'], active='world')


def credits(d, lang):
    t = T[lang]
    _, cred, miss = notes_part(d, lang)
    wip = f'<p class="panel">{esc(t["lang_wip"])}</p>' if miss else ''
    body = f'''<div class="wrap page-head"><h1>{esc(t['h_credits'])}</h1><p>{esc(t['credits_lead'])}</p></div>
<div class="wrap doc">{wip}{md.render(cred[1:], _notes_link(lang))}
<h2>{esc(t['testers'])}</h2><p>{t['testers_p']}</p>
<p>{t['thanks_dani']}</p></div>'''
    return page(lang, 'credits/', t['h_credits'], body, active='credits')


def classic_page(d, lang):
    t, c = T[lang], classic.C[lang]
    names = {k: f'<strong>{esc(GAME[k][lang])}</strong>' for k in ('careers', 'seasons', 'tourneys')}
    secs = ''.join(f'<h2>{esc(h)}</h2><p>{intro.format(**names)}</p><ul>' + ''.join(f'<li>{b}</li>' for b in bl) + '</ul>'
                   for h, intro, bl in c['secs'])
    body = (f'<div class="wrap page-head"><h1>{esc(t["h_classic_page"])}</h1><p>{esc(c["lead"])}</p></div>'
            f'<div class="wrap doc">{secs}<figure class="shot" style="max-width:640px;margin-top:24px"><img '
            f'src="/static/img/zones_final_first84.png" width="1600" height="1200" loading="lazy" alt=""><figcaption>'
            f'{esc(GAME["e84"][lang])}</figcaption></figure></div>')
    return page(lang, 'classic/', t['h_classic_page'], body, active='classic')


def not_found():
    t = T['en']
    body = (f'<div class="wrap page-head" style="text-align:center"><h1>{esc(t["notfound"])}</h1>'
            f'<p>{esc(t["notfound_p"])}</p><p class="cta">' +
            ''.join(f'<a class="btn blue" href="/{l}/">{esc(T[l]["back_home"])}</a>' for l in LANGS) + '</p></div>')
    return page('en', '', t['notfound'], body)


def root_index():
    links = ''.join(f'<a class="btn blue" href="/{l}/" hreflang="{l}" lang="{l}">{LANG_NAME[l]}</a>' for l in LANGS)
    alt = ''.join(f'<link rel="alternate" hreflang="{l}" href="{SITE_URL}/{l}/">' for l in LANGS)
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>World of SWOS · SWOS 96/97 Mod</title>
<meta name="description" content="{esc(T['en']['meta_home'])}">
<link rel="canonical" href="{SITE_URL}/en/">{alt}<link rel="alternate" hreflang="x-default" href="{SITE_URL}/">
<meta property="og:title" content="World of SWOS · SWOS 96/97 Mod"><meta property="og:type" content="website">
<meta property="og:description" content="{esc(T['en']['meta_home'])}"><meta property="og:url" content="{SITE_URL}/">
<meta property="og:image" content="{SITE_URL}/static/og-en.png"><meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/static/logo.svg" type="image/svg+xml"><link rel="stylesheet" href="/static/style.css">
<script>
(function () {{
  var L = {json.dumps(LANGS)}, l = null;
  try {{ l = localStorage.getItem('lang'); }} catch (e) {{}}
  if (L.indexOf(l) < 0) {{
    var n = (navigator.languages || [navigator.language || 'en']);
    for (var i = 0; i < n.length && !l; i++) {{ var c = (n[i] || '').slice(0, 2).toLowerCase(); if (L.indexOf(c) >= 0) l = c; }}
  }}
  location.replace('/' + (l || 'en') + '/');
}})();
</script></head>
<body><main class="wrap hero">{logo_svg(160, 'World of SWOS').replace('<svg ', '<svg class="logo" ', 1)}
<h1>World of SWOS</h1><p class="cta">{links}</p></main></body></html>
'''


# ------------------------------------------------------------------------------------------------ build
def write(path, text):
    p = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(text)


def frames_in():
    """incoming/*.png (raw 320x200 harness frames) -> static/img, pixel-crisp 5x / 6x (the game's 4:3), when newer."""
    inc = os.path.join(ROOT, 'incoming')
    for f in sorted(os.listdir(inc)) if os.path.isdir(inc) else []:
        src, dst = os.path.join(inc, f), os.path.join(ROOT, 'static', 'img', f)
        if f.endswith('.png') and (not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src)):
            from PIL import Image
            im = Image.open(src)
            im.resize((im.width * 5, im.height * 6), Image.NEAREST).save(dst, optimize=True)
            print(f'frame: {f}')


def build():
    frames_in()
    d = load()
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(os.path.join(ROOT, 'static'), os.path.join(OUT, 'static'))
    write('static/logo.svg', logo_svg(64, 'World of SWOS'))
    for lang in LANGS:                              # the social preview cards
        t = T[lang]
        ogimage.card(os.path.join(OUT, 'static', f'og-{lang}.png'), t['tagline'], t['concept'],
                     '' if RELEASED else t['soon'], t['soon_dl'])
    urls = []
    for lang in LANGS:
        pages = {'': home(d, lang), 'countries/': countries_index(d, lang), 'world/': world(d, lang),
                 'credits/': credits(d, lang), 'classic/': classic_page(d, lang)}
        for code in d['order']:
            pages[f'countries/{code}/'] = country(d, code, lang)
        for p, text in pages.items():
            write(f'{lang}/{p}index.html', text)
            urls.append(f'{SITE_URL}/{lang}/{p}')
    write('index.html', root_index())
    write('404.html', not_found())
    write('CNAME', 'worldofswos.com\n')
    write('robots.txt', f'User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n')
    write('sitemap.xml', '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/'
          'sitemap/0.9">\n' + ''.join(f'<url><loc>{u}</loc></url>\n' for u in urls) + '</urlset>\n')
    open(os.path.join(OUT, '.nojekyll'), 'w').close()
    print(f'site/: {len(urls)} pages, {len(d["order"])} countries; data {d["src"]}')


if __name__ == '__main__':
    if '--refresh' in sys.argv:
        refresh()
    build()
