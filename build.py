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
import already                                              # noqa: E402
import install                                              # noqa: E402
from i18n import CONTINENT, GAME, LANG_NAME, LANGS, LOCALE, T   # noqa: E402

SITE_URL = 'https://worldofswos.com'
REPO = 'https://github.com/aminta/swos-9697-mod'
# 4.0 is not released yet: both point to the releases page (at release: /releases/latest/download/swos-9697-mod-patcher.html)
PATCHER = REPO + '/releases/download/v4.0/swos-9697-mod-patcher.html'
RELEASE_PAGE = REPO + '/releases/tag/v4.0'
PATCHER_MD5 = '923bf8ee35e4174cdb486c1f4e22b9cd'        # the released patcher's md5, shown under the download when set (Regia gives it at the flip)
WINNERS = 'full'        # 'none': no page tonight (4.0.1 lists the page) · 'page': page without season-end titles (block on,
                        # 4.0.1 lists the titles) · 'full': page + titles (block on, nothing in 4.0.1)
WINNERS_40 = WINNERS in ('page', 'full')
# saved careers with 4.0 (the Regia's verified results): row -> 'ok' | 'pending' | 'beta'
SAVES = [('orig', 'ok'), ('v1', 'ok'), ('v2', 'ok'), ('v3', 'ok'), ('beta', 'beta')]   # verified on the 4.0 release build (Regia 2026-10-22)
RELEASES = REPO + '/releases'
CONTENT_40 = True   # the 4.0 content (cups, main menu, news page, 4.0.1 list): live since Davide's OK 2026-10-22
RELEASED = True   # 4.0 released 2026-10-22 20:10 UTC (Davide's OK via the Regia)   # THE switch (env for the local preview only). False until 4.0 is on GitHub: download buttons and the install section say "Coming soon"
TWELVE_BIT_URL = 'https://www.facebook.com/retrogaming12bit'   # https://12bit.it when the new site is out
_tb = '<img class="assoc-logo" src="/static/img/12bit.png" width="64" height="80" alt="12 Bit Retrogaming, associazione culturale (Trieste)">'
TWELVE_BIT = f'<a href="{TWELVE_BIT_URL}">{_tb}</a>' if TWELVE_BIT_URL else _tb
GOATCOUNTER = 'worldofswos'  # GoatCounter code (https://<code>.goatcounter.com): cookieless visit counter; '' = none
DATA = os.path.join(ROOT, 'data')
OUT = os.environ.get('WOS_OUT') or os.path.join(ROOT, 'site')
# the 'How to install' page goes live with 4.0 (after Davide's Chrome test): preview only until then,
# WOS_INSTALL=1 WOS_OUT=site-preview python3 build.py  (site-preview/ is git-ignored)
INSTALL_PAGE = os.environ.get('WOS_INSTALL', '1') == '1'   # live since 2026-10-20 (Davide's ok via the Regia)
GUIDE_PATCHER = REPO + '/releases/download/v3.3.6/swos-9697-mod-patcher.html'   # the public one-click patcher (3.3.6)
GUIDE_DONE_SHOTS = False    # the 'done' shots show 4.0 text (MOD_BACKUP\4.0): off until there are 3.3.6 ones
# frames off the site until retaken (Regia's audit 2026-10-20: old names / old frames / old FORMAT style):
# 'name' = every language, 'name-xx' = that language only
SPLITS_OK = True      # the rc5 split frames checked against their captions
SHOTS_HOLD = set() if SPLITS_OK else {'split-scotland', 'split-austria'}   # rc2 retakes passed 2026-10-21; splits wait for rc3


def held(base, lang):
    return base in SHOTS_HOLD or f'{base}-{lang}' in SHOTS_HOLD
NEXT_TEXTS = True      # the World page and the competitions list from data/next/ (the 4.0 notes; Davide's ok 2026-10-20)
CUPS_HEADS = ('Continental club cups 2026-27', 'Coppe continentali per club 2026-27',
              'Les coupes continentales de clubs 2026-27', 'Die Kontinentalpokale der Vereine 2026-27')
CUPS = os.environ.get('WOS_CUPS') == '1' or CONTENT_40           # the continental cups section: preview only until the Regia's go
CUPS_HOLD = set()
CUPS_TEXT = {'fifa-intercontinental'}   # no 4.0 screenshot: a text tile   # rc2 IC frame is a test artifact (Palmeiras forced into the CAF place): retake in rc3
CONTS = ['europe', 'north_america', 'south_america', 'asia', 'oceania', 'africa']
CONT_MD = {'Europe': 'europe', 'North and Central America': 'north_america', 'South America': 'south_america',
           'Asia': 'asia', 'Oceania': 'oceania', 'Africa': 'africa', 'Europa': 'europe',
           'Nord e Centro America': 'north_america', 'Sud America': 'south_america'}


# ------------------------------------------------------------------------------------------------ refresh (import)
# the in-game FORMAT page's text as fmtgame.write() builds it (4.0: paragraphs of prose, then the colours' lines);
# old tools (a plain list of lines) still work
STATS_CODE = """
# the site's numbers, counted from the release data (what each one counts: see the stats texts in i18n.py)
import csv, complist
dirs = [os.path.join(d, x) for x in sorted(os.listdir(d)) if os.path.exists(os.path.join(d, x, 'pack.json'))]
per = {}
for dd in dirs:                                   # (one country at a time: the model is sorted by its own order)
    comps = complist.from_packs([dd])[0]['comps']
    divs = sum(len(lv) for comp in comps if comp['kind'] == 'league' for lv in comp['levels'])
    cups = sum(1 for comp in comps if comp['kind'] in ('cup', 'league_cup'))
    rows = list(csv.DictReader(open(os.path.join(dd, 'clubs.csv'), encoding='utf-8')))
    per[os.path.basename(dd)] = dict(divisions=divs, cups=cups, states=len({r['division'] for r in rows if r['file'] == 'states'}) and 0,
                                     league_clubs=sum(r['file'] == 'league' for r in rows),
                                     state_clubs=sum(r['file'] == 'states' for r in rows),
                                     pool=sum(r['file'] == 'pool' for r in rows))
guests = sum(len(json.load(open(os.path.join(d, 'guests', f)))['clubs']) for f in os.listdir(os.path.join(d, 'guests'))) \\
    if os.path.isdir(os.path.join(d, 'guests')) else 0
json.dump(dict(per=per, guests=guests), open(os.path.join(os.path.dirname(sys.argv[3]), 'stats.json'), 'w'), indent=0)
"""
PAGE_CODE = """
def page(world, titles, lines, lang):
    try:
        import fmtprose
    except ImportError:
        return [x if isinstance(x, str) else ' '.join(x) for x in lines]
    h = fmtgame.ZT[lang]['head']
    if isinstance(lines, dict):
        prose, tail = lines['prose'], lines['tail']
    else:
        tail = lines[lines.index(h):] if h in lines else []
        prose = fmtprose.sentences(lines[:len(lines) - len(tail)])
    hand = fmtprose.text(world, titles['it'], lang)
    if hand and isinstance(lines, dict) and lines.get('real'):
        hand = [lines['real']] + hand
    if hand and not isinstance(lines, dict):
        rc = [x for x in lines if x.startswith(fmtgame.TEXTS[lang]['real_cup'].split('{')[0]) or
              x.startswith(fmtgame.TEXTS[lang]['real_in'])]
        if rc:
            hand = fmtprose.sentences(rc) + hand
    prose = hand or prose
    if hand:
        tail = [x for x in tail if x not in fmtgame.CONFED_NOTES[lang].values()]
    out = []
    for para in prose:
        out += [fmtgame.ascii_up(para, lang), '']
    out += [fmtgame.ascii_up(t, lang) for t in tail]
    while out and out[-1] == '':
        out.pop()
    return out
"""

def refresh():
    mod = os.path.expanduser(os.environ.get('SWOS_MOD', '~/swos-mod'))
    ref = os.environ.get('SWOS_REF', 'world-2025-26')
    # the world data dir of the FINAL release build c/REL40 (Regia, 2026-10-19 evening)
    packs = os.environ.get('FMT_PACKS') or os.path.join(mod, 'internal', 'world2526', 'world5tm-rel40-cupd-1955')
    packs = os.path.expanduser(packs)
    os.makedirs(DATA, exist_ok=True)

    def show(path):
        return subprocess.run(['git', '-C', mod, 'show', f'{ref}:{path}'], check=True, capture_output=True,
                              text=True).stdout

    sha = subprocess.run(['git', '-C', mod, 'rev-parse', '--short', ref], check=True, capture_output=True,
                         text=True).stdout.strip()
    # the notes and the competitions list are 4.0 texts (world-2025-26 is local, unpushed): into data/next/, published
    # only when RELEASED; data/*.md is the frozen version already public (Regia, 2026-10-20)
    os.makedirs(os.path.join(DATA, 'next'), exist_ok=True)
    for src, dst in [('release/notes-world-2026-27.md', 'notes-world-2026-27.md'),
                     ('release/world-2026-27-competitions.md', 'competitions.md'),
                     ('release/notes-4.0.md', 'notes-4.0.md')]:
        open(os.path.join(DATA, 'next', dst), 'w', encoding='utf-8').write(md.strip_comments(show(src)))
    # the in-game FORMAT texts and the countries' names, with the mod's own tools (exported, never run in the repo)
    with tempfile.TemporaryDirectory() as tmp:
        tref = os.environ.get('FMT_TOOLS_REF', ref)    # (a fix branch of tools/fmtgame.py not merged yet)
        arch = subprocess.run(['git', '-C', mod, 'archive', tref, 'tools', 'packs'], check=True,
                              capture_output=True).stdout
        subprocess.run(['tar', '-x', '-C', tmp], input=arch, check=True)
        code = ('import sys, os, json\nsys.path.insert(0, sys.argv[1])\nimport fmtgame\nd = sys.argv[2]\nout = {}\n'
                + PAGE_CODE +
                'for s in sorted(os.listdir(d)):\n'
                '    p = os.path.join(d, s, "pack.json")\n'
                '    if not os.path.exists(p): continue\n'
                '    pk = json.load(open(p))\n'
                '    items = [{"title": t, "text": {l: page(w, t, tx[l], l) for l in fmtgame.LANGS}} '
                'for w, cid, t, tx in fmtgame.from_pack(os.path.join(d, s))]\n'
                '    out[s] = {"names": pk["button_names"], "continent": pk["continent"], "fmt": items}\n'
                'json.dump(out, open(sys.argv[3], "w"), ensure_ascii=False, indent=0)\n'
                + STATS_CODE)
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
    texts = os.path.join(DATA, 'next') if RELEASED or NEXT_TEXTS else DATA
    comp = open(os.path.join(texts, 'competitions.md'), encoding='utf-8').read()
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
    notes = split_langs(open(os.path.join(texts, 'notes-world-2026-27.md'), encoding='utf-8').read())
    src = json.load(open(os.path.join(DATA, 'source.json')))
    pp = os.path.join(DATA, 'places.json')            # continental places by association (the data session)
    places = json.load(open(pp))['countries'] if os.path.exists(pp) else {}
    # the numbers, counted from the release data (data/stats.json, written by --refresh)
    st = json.load(open(os.path.join(DATA, 'stats.json')))
    for code, c in countries.items():
        it = c['names']['it']
        extra = sum(1 for i in c['fmt'] if code == 'bra' and i['title']['it'].startswith(it + ' CAMPEONATO ')   # states
                    or i['title']['it'] == it + ' COPPA ITALIA SERIE D')
        x = st['per'][code]
        c['ncomps'] = x['divisions'] + x['cups'] + extra
    m = re.search(r'\*\*(\d+) continental competitions', notes['en'])
    new_conti = int(m.group(1)) if m else 0          # the non-UEFA continental competitions, new in 4.0
    conti = 3 + new_conti                            # + the 3 UEFA cups
    per = list(st['per'].values())
    league, states, pool = (sum(x[k] for x in per) for k in ('league_clubs', 'state_clubs', 'pool'))
    stats = dict(countries=len(countries), clubs=league + states + pool + st['guests'], guests=st['guests'],
                 comps=sum(c['ncomps'] for c in countries.values()) + conti, conti=conti, new_conti=new_conti,
                 league=league, states=states, pool=pool)
    return dict(countries=countries, order=order, notes=notes, stats=stats, src=src, places=places)


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
        if key == 'install' and INSTALL_PAGE:
            p = 'install/'
        href = f'/{lang}/' + ('' if p.startswith('#') else p) + (p if p.startswith('#') else '')
        cur = ' aria-current="page"' if key == active else ''
        nav.append(f'<a href="{href}"{cur}>{esc(t["nav_" + key])}</a>')
    sw = ''.join(f'<a href="/{l}/{path}" hreflang="{l}" lang="{l}" title="{LANG_NAME[l]}"'
                 f'{" aria-current=\"true\"" if l == lang else ""}>{l.upper()}</a>' for l in langs)
    alt = ''.join(f'<link rel="alternate" hreflang="{l}" href="{SITE_URL}/{l}/{path}">' for l in langs)
    alt += f'<link rel="alternate" hreflang="x-default" href="{SITE_URL}/en/{path}">'
    og_title = t['og_title'] if path == '' else f'{title} · {t["site"]}'
    og_desc = t['tagline']
    full = f'{title} · {t["site"]}' if title != t['site'] else f'{t["site"]} · {t["sub"]}'
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc or t['meta_home'])}">
<link rel="canonical" href="{SITE_URL}{url}">{alt}
<meta property="og:title" content="{esc(og_title)}">
<meta property="og:description" content="{esc(og_desc)}">
<meta property="og:type" content="website"><meta property="og:url" content="{SITE_URL}{url}">
<meta property="og:locale" content="{LOCALE[lang]}">
<meta property="og:image" content="{SITE_URL}/static/og-{lang}.png?v=41"><meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630"><meta property="og:image:alt" content="{esc(t['tagline'])}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(og_title)}">
<meta name="twitter:description" content="{esc(og_desc)}"><meta name="twitter:image" content="{SITE_URL}/static/og-{lang}.png?v=41">
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
<p><a class="btn orange" href="/{lang}/bug/">{esc(t['bug_title'])}</a></p>
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


FRAMES_OK = set(json.load(open(os.path.join(DATA, 'frames_ok.json')))) if os.path.exists(
    os.path.join(DATA, 'frames_ok.json')) else None


def have(f):
    """A frame goes on the site only when it exists AND was checked (data/frames_ok.json: added by hand after the
    check: mid-season data, the right structure, real legend, title and caption matching)."""
    return os.path.exists(os.path.join(ROOT, 'static', 'img', f + '.png')) and (FRAMES_OK is None or f in FRAMES_OK)


def winners_block(lang, head='h2'):
    """4.0's WINNERS page (STAT > VINCITORI / WINNERS / VAINQUEURS / SIEGER), with its own-language frame when checked."""
    if not (RELEASED and WINNERS_40):
        return ''
    t = T[lang]
    wf = f'winners-{lang}'
    shot = (f'<figure class="shot" style="max-width:640px;margin:12px 0"><img src="/static/img/{wf}.png" width="1600" '
            f'height="1200" loading="lazy" alt="{esc(t["h_winners"])}"></figure>') if have(wf) else ''
    return f'<{head} id="winners">{esc(t["h_winners"])}</{head}><p>{esc(t["winners_text"])}</p>{shot}'


def main_menu(lang):
    """4.0's lead image: the game's main menu with the green 2026-27 career button (release only)."""
    if not CONTENT_40:
        return ''
    t = T[lang]
    f = f'main-menu-{lang}'
    if not have(f):
        return ''
    return (f'<section class="wrap"><figure class="shot lead-shot"><img src="/static/img/{f}.png" width="1600" height="1200" '
            f'alt="{esc(t["menu_cap"])}"><figcaption class="px">{esc(t["menu_cap"])}</figcaption></figure></section>')


RELEASED_401 = False    # flip when 4.0.1 is on GitHub: Joypad headline + 'what's new' instead of 'the upcoming 4.0.1'
WARN_FOREIGN = False   # urgent notice: remove when the fixed 4.0 is out (Regia 2026-10-22)


def warn_banner(lang):
    if not WARN_FOREIGN:
        return ''
    return (f'<div class="warn" role="alert"><b class="px">!</b><p>{esc(T[lang]["warn_foreign"])}</p></div>')


def home(d, lang):
    t, s = T[lang], d['stats']
    stats = ''.join(f'<div class="stat"><b>{fmt_num(s[k], lang)}</b><span>{esc(t["s_" + k].format(n=s["new_conti"]))}</span></div>'
                    for k in ['countries', 'clubs', 'comps', 'conti', 'guests'] if s.get(k))
    cards = ''.join(f'<article class="card"><h3>{esc(h)}</h3><p>{esc(p)}'
                    + (f' {esc(t["tables_row"])}' if RELEASED and i == len(t['cards']) - 1 else '') + '</p></article>'
                    for i, (h, p) in enumerate(t['cards']))
    steps = ''.join('<li>' + st.format(careers=f'<strong>{GAME["careers"][lang]}</strong>',
                                         world=f'<strong>{GAME["world"][lang]}</strong>') + '</li>'
                    for st in t['steps'])
    shots = ''                                      # groups of frames; a frame not captured yet is left out
    for g, items in t['shots']:
        figs = ''
        for f, c in items:
            if held(f[:-3], lang):
                continue                            # taken off until retaken                          # name-it: this language's capture when there is one
            fl = f[:-3] + '-' + lang if f.endswith('-it') and have(f[:-3] + '-' + lang) else f
            if CONTENT_40 and f.endswith('-it') and fl != f[:-3] + '-' + lang:
                continue                            # released: a slot only in its own language (Davide)
            if CONTENT_40 and not have(fl):
                continue                            # released: no 'coming soon' tiles
            if have(fl):
                figs += (f'<figure class="shot"><img src="/static/img/{fl}.png" width="1600" height="1200" '
                         f'loading="lazy" alt="{esc(c)}"><figcaption>{esc(c)}</figcaption></figure>')
            else:
                figs += (f'<figure class="shot soon"><div class="soon-box"><span>{esc(t["soon_tile"])}</span></div>'
                         f'<figcaption>{esc(c)}</figcaption></figure>')
        if figs:                                    # (a group with every tile held disappears)
            shots += (f'<h3>{esc(g)}</h3><div class="cards" style="grid-template-columns:repeat(auto-fill,'
                      f'minmax(min(100%,440px),1fr))">{figs}</div>')
    winners = winners_block(lang)
    cups = ''
    if CUPS:
        tiles = ''
        for f, c in t['cups']:
            fl = f'{f}-{lang}' if have(f'{f}-{lang}') else (f'{f}-it' if not CONTENT_40 else '')
            if f in CUPS_TEXT:
                tiles += (f'<figure class="shot"><div class="soon-box" style="padding:18px;text-align:center">'
                          f'<p class="px" style="color:var(--gold);font-size:18px;margin:0 0 10px">{esc(t["ic_tile"])}</p>'
                          f'<p style="margin:0;font-size:14px">{esc(t["ic_line"])}</p></div><figcaption>{esc(c)}</figcaption></figure>')
            elif f not in CUPS_HOLD and have(fl):
                tiles += (f'<figure class="shot"><img src="/static/img/{fl}.png" width="1600" height="1200" loading="lazy" '
                          f'alt="{esc(c)}"><figcaption>{esc(c)}</figcaption></figure>')
            else:
                tiles += (f'<figure class="shot soon"><div class="soon-box"><span>{esc(t["soon_tile"])}</span></div>'
                          f'<figcaption>{esc(c)}</figcaption></figure>')
        soon40 = '' if RELEASED else f'<p class="note"><span class="next-tag px" style="font-size:11px">4.0</span> {esc(t["with40"])}</p>'
        cups = f'<h2 id="cups">{esc(t["h_cups"])}</h2>{soon40}<div class="cards cups">{tiles}</div>'
    if RELEASED:
        dl_btn = f'<a class="btn green" href="{PATCHER}">{esc(t["dl"])}<small>{esc(t["dl_small"])}</small></a>'
        dl_btn2 = f'<a class="btn green" href="{PATCHER}">{esc(t["dl"])}</a>'
        soon_inst = ''
    else:
        dl_btn = dl_btn2 = ''                       # the red "coming soon" sticker at the top of the page instead
        soon_inst = f'<p class="panel"><strong class="px" style="color:var(--gold)">{esc(t["soon"])}</strong> {esc(t["soon_install"])}</p>'
    sticker = (f'<p class="soon-sticker out" role="note"><b>{esc(t["out_now"])}</b><span>{esc(t["out_sub"])}</span></p>'
               if RELEASED else (f'<p class="soon-sticker" role="note"><b>{esc(t["soon"])}</b>'
                                   f'<span>{esc(t["soon_dl"])}</span><i>{esc(t["soon_test"])}</i></p>'))
    body = f'''<section class="hero"><div class="wrap">{sticker}
{logo_svg(240, t['site']).replace('<svg ', '<svg class="logo" ', 1)}
{warn_banner(lang)}<p class="px" style="color:var(--dim);margin:0 0 14px">{esc(t['kicker'])}</p>
<h1>{esc(t['tagline'])}</h1>
<p class="tagline">{esc(t['concept'])}</p>
<p class="lead">{esc(t['lead'])}</p>
<div class="cta">
{dl_btn}
{f'<a class="btn blue" href="/{lang}/news/">{esc(t["news_title"])}</a>' if CONTENT_40 else ''}
<a class="btn orange" href="#install">{esc(t['how'])}</a>
<a class="btn blue" href="/{lang}/countries/">{esc(t['see_world'])}</a>
</div>
<div class="stats">{stats}</div>
<p class="note" style="max-width:820px;margin:8px auto 0">{esc(t['stats_note'].format(**{k: fmt_num(v, lang) for k, v in s.items()}))}</p>
</div></section>
{main_menu(lang)}
<section class="wrap"><div class="bug-cta"><p class="px">{esc(t['bug_cta'])}</p>
<a class="btn orange" href="/{lang}/bug/">{esc(t['bug_title'])}</a></div></section>
<section class="wrap">
<h2>{esc(t['h_what'])}</h2>
{''.join(f'<p>{p}</p>' for p in t['what'])}
<h2>{esc(t['h_high'])}</h2>
<div class="cards">{cards}</div>
{winners}{cups}<h2 id="already">{esc(already.A[lang][0])}</h2>
<div class="cards">{''.join(f'<article class="card"><h3>{esc(h)}</h3><p>{esc(p)}</p></article>' for h, p in already.A[lang][1])}</div>
<h2 id="next">{esc(t['h_next'])}</h2>
<div class="panel next">{(f'<p><span class="next-tag px">4.0.1</span> <strong>{esc(t["joy_h"])}</strong></p><p>{esc(t["joy_text"])}</p>') if RELEASED_401 else ''}{(f'<p><span class="next-tag px">4.0.1</span> <strong>{esc(t["next401_h"])}</strong></p><ul>'
  + ''.join(f'<li>{esc(x)}</li>' for x in (([t['next401_cups']] if RELEASED else []) + t['next401']) + (t['next401_rc12'] + [t['next401_cal']] if RELEASED else []) + ([t['next401_winners_page' if WINNERS == 'none' else 'next401_winners']] if RELEASED and WINNERS != 'full' else [])) + '</ul>') if CONTENT_40 else ''}<p><span class="next-tag px">5.0</span> {esc(t['next_text'])}</p>
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


HOW = {
    'cup winner': {'en': 'cup winner', 'it': 'vincitrice della coppa', 'fr': 'vainqueur de la coupe', 'de': 'Pokalsieger'},
    'Apertura champion': {'en': 'Apertura champion', 'it': 'campione dell\'Apertura', 'fr': "champion de l'Apertura",
                          'de': 'Apertura-Meister'},
    'Clausura champion': {'en': 'Clausura champion', 'it': 'campione della Clausura', 'fr': 'champion de la Clausura',
                          'de': 'Clausura-Meister'},
    'next by league place': {'en': 'next by league place', 'it': 'la successiva in classifica',
                             'fr': 'le suivant au classement', 'de': 'der Nächste in der Tabelle'},
    'best placed not yet qualified': {'en': 'best placed not yet qualified', 'it': 'la meglio piazzata non ancora qualificata',
                                      'fr': 'le mieux classé pas encore qualifié', 'de': 'der Bestplatzierte, der noch nicht qualifiziert ist'},
    'next {n} best placed not yet qualified': {'en': 'next {n} best placed not yet qualified',
                                               'it': 'le {n} meglio piazzate non ancora qualificate',
                                               'fr': 'les {n} mieux classés pas encore qualifiés',
                                               'de': 'die {n} Bestplatzierten, die noch nicht qualifiziert sind'},
    '{n} x {o}': {'en': '{n} × {o}', 'it': '{n} × {o}', 'fr': '{n} × {o}', 'de': '{n} × {o}'},
}


def _ord(n, lang):
    n = int(n)
    return {'en': f'{n}{complist_sfx(n)}', 'it': f'{n}º', 'fr': '1er' if n == 1 else f'{n}e', 'de': f'{n}.'}[lang]


def complist_sfx(n):
    return 'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')


def how_text(how, lang):
    out = []
    for part in how.split(', '):
        m = re.fullmatch(r'(\d+)(?:st|nd|rd|th)(?:-(\d+)(?:st|nd|rd|th))?', part)
        if m:
            out.append(_ord(m.group(1), lang) + (f'-{_ord(m.group(2), lang)}' if m.group(2) else ''))
            continue
        m = re.fullmatch(r'(\d+) x (\d+)(?:st|nd|rd|th)', part)
        if m:
            out.append(HOW['{n} x {o}'][lang].format(n=m.group(1), o=_ord(m.group(2), lang)))
            continue
        m = re.fullmatch(r'next (\d+) best placed not yet qualified', part)
        if m:
            out.append(HOW['next {n} best placed not yet qualified'][lang].format(n=m.group(1)))
            continue
        out.append(HOW.get(part, {}).get(lang, part))
    return ', '.join(out)


def places_html(d, code, lang):
    t = T[lang]
    pl = d['places'].get(code) if d.get('places') else None
    if pl is None:
        return ''
    if not pl:
        return f'<p class="note">{esc(t["places_none"])}</p>'
    tag = '' if RELEASED else ' <span class="next-tag px" style="font-size:11px">4.0</span>'
    li = ''.join(f'<li><strong>{esc(x["comp"])}</strong>: {x["places"]} ({esc(how_text(x["how"], lang))})'
                 + (tag if not x['comp'].startswith('UEFA') else '') + '</li>' for x in pl)
    return f'<div class="panel"><strong class="px" style="color:var(--gold)">{esc(t["places_h"])}</strong><ul style="margin:.5em 0 0">{li}</ul></div>'


def country(d, code, lang):
    t, c = T[lang], d['countries'][code]
    name = c['names'][lang]
    head = f'''<div class="wrap page-head">
<p class="crumbs"><a href="/{lang}/countries/">{esc(t['c_back'])}</a> › {esc(CONTINENT[c['cont']][lang])}</p>
<h1>{esc(name)}</h1>
<p>{esc(t['c_lead'].format(name=name))}</p>{places_html(d, code, lang)}</div>'''
    game = f'<p class="note">{esc(t["c_game_note"])}</p>{screens(c, lang)}'
    if lang in ('en', 'it'):
        body = (f'<div class="wrap">{comp_cards(c["md"][lang], lang)}'
                f'<details><summary>{esc(t["c_game"])}</summary>{game}</details></div>')
    else:
        body = (f'<div class="wrap"><h2>{esc(t["c_game"])}</h2>{game}'
                f'<details><summary>{esc(t["c_details"])}</summary>{comp_cards(c["md"]["en"], "en")}</details></div>')
    return page(lang, f'countries/{code}/', name, head + body, desc=t['c_lead'].format(name=name),
                active='countries')


def conti_block(d, lang):
    """The continental competitions by confederation, from the notes' continental cups item (data/next)."""
    t = T[lang]
    main, _, _ = notes_part(d, lang)
    kids = next((k for b in main if b[0] == 'list' for _, k in b[1] if any(x[0].startswith('CONMEBOL') for x in k)), [])
    rows = [('UEFA', [('**UEFA Champions League** · **UEFA Europa League** · **UEFA Conference League**', t['uefa_line'])], False)]
    for txt, _ in kids:
        conf, rest = txt.split(':', 1)
        rows.append((conf.strip(), [(rest.strip(), '')], True))
    new = '' if RELEASED else f' <span class="next-tag px" style="font-size:11px">4.0</span>'
    li = ''.join(f'<li class="comp"><span class="name">{esc(conf)}</span>{new if is_new else ""}'
                 + ''.join(f'<p class="facts">{md.inline(a)}' + (f'<br>{esc(b)}' if b else '') + '</p>' for a, b in items)
                 + '</li>' for conf, items, is_new in rows)
    note = '' if RELEASED else f'<p class="note"><span class="next-tag px" style="font-size:11px">4.0</span> {esc(t["with40"])}</p>'
    return f'<section class="cont"><h2 id="continental">{esc(t["h_conti"])}</h2>{note}<ul class="comps">{li}</ul></section>'


def countries_index(d, lang):
    t = T[lang]
    secs = [conti_block(d, lang)]
    for cont in CONTS:
        codes = [c for c in d['order'] if d['countries'][c]['cont'] == cont]
        if not codes:
            continue
        li = ''.join(f'<li><a href="/{lang}/countries/{c}/">{esc(d["countries"][c]["names"][lang])}'
                     f'<small>{esc(t["comps_n"].format(n=d["countries"][c]["ncomps"]))}</small></a></li>'
                     for c in codes)
        if cont == 'oceania' and 'aus' in d['countries'] and d['countries']['aus']['cont'] != 'oceania':
            li += (f'<li><a href="/{lang}/countries/aus/">{esc(d["countries"]["aus"]["names"][lang])}'
                   f'<small>{esc(t["aus_note"])}</small></a></li>')      # Australia: AFC since 2006, looked for here
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
        if held(f, lang):
            continue
        fl = lang if have(f'{f}-{lang}') else 'it'
        if CONTENT_40 and fl != lang:
            continue
        out.append(f'<figure class="shot"><img src="/static/img/{f}-{fl}.png" width="1600" height="1200" '
                   f'loading="lazy" alt="{esc(cap)}"><figcaption>{esc(cap)}</figcaption></figure>')
    return f'<div class="cards" style="margin:18px 0 26px;grid-template-columns:repeat(auto-fill,minmax(min(100%,440px),1fr))">{"".join(out)}</div>'


def world(d, lang):
    t = T[lang]
    main, _, miss = notes_part(d, lang)
    if not RELEASED:                                # 'coming with 4.0' under the continental cups heading
        out = []
        for b in main:
            out.append(b)
            if b[0] in ('sub', 'h') and b[-1] in CUPS_HEADS:
                out.append(('p', '**' + t['with40'] + '**'))
        main = out
    heads = [(md.slug(b[2]), b[2]) for b in main if b[0] == 'h' and b[1] in (3, 4)]
    toc = ''.join(f'<li><a href="#{s}">{md.inline(h)}</a></li>' for s, h in heads)
    wip = f'<p class="panel">{esc(t["lang_wip"])}</p>' if miss else ''
    l2 = lang
    body = f'''<div class="wrap page-head"><h1>{esc(t['h_world'])}</h1><p class="tagline px" style="color:var(--gold)">
{esc(t['world_lead'])}</p></div>
<div class="wrap">{frames(lang)}{winners_block(lang)}</div>
<div class="wrap doc" lang="{l2}">{wip}{'' if RELEASED else f'<p class="panel next"><span class="next-tag px">4.0</span> {esc(t["with40"])}</p>'}<nav class="panel" aria-label="{esc(t['toc'])}"><strong>{esc(t['toc'])}</strong>
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


def saves_table(lang):
    if not RELEASED:
        return ''
    t = T[lang]
    rows = ''.join(f'<tr><td>{esc(t["saves_rows"][k])}</td><td>{esc(t["saves_status"][v])}</td></tr>' for k, v in SAVES)
    return (f'<h2 id="saves">{esc(t["saves_h"])}</h2><table class="saves"><thead><tr><th>{esc(t["saves_cols"][0])}</th>'
            f'<th>{esc(t["saves_cols"][1])}</th></tr></thead><tbody>{rows}</tbody></table><p><strong>{esc(t["saves_tip"])}</strong></p>')


def launch_block(lang):
    x = install.EXTRA[lang]
    bat = install.BATLANG[lang]
    code = ('@echo off\ncd /d "%~dp0DOSBOX"\nstart "" DOSBox.exe -conf "..\\dosbox_SWOS.conf" '
            f'-conf "..\\dosbox_SWOS_single_{bat}.conf" -noconsole -c "exit"')
    return (f'<h2 id="launch">{esc(x["lh"])}</h2><p class="panel next">{esc(x["no64"])}</p><p>{x["lt"][0]}</p><pre class="panel" style="white-space:pre-wrap;'
            f'overflow-wrap:anywhere;font-size:14px">{esc(code)}</pre><p>{x["lt"][1]}</p>')


def joypad_block(lang):
    x = install.EXTRA[lang]
    return f'<h2 id="joypad">{esc(x["jh"])}</h2><ul>' + ''.join(f'<li>{i}</li>' for i in x['jt']) + '</ul>'


def install_page(d, lang):
    g, t = install.G[lang], T[lang]

    def shot(name):
        fl = lang if os.path.exists(os.path.join(ROOT, 'static', 'img', 'patcher', f'{name}-{lang}.jpg')) else 'it'
        return (f'<figure class="shot" style="max-width:640px;margin:12px 0"><img src="/static/img/patcher/{name}-{fl}.jpg" '
                f'width="640" height="480" loading="lazy" alt=""></figure>')

    def text(x):
        out = ''
        for part in re.split(r'(\[SHOT [a-z-]+\])', x):
            m = re.fullmatch(r'\[SHOT ([a-z-]+)\]', part)
            out += shot(m.group(1)) if m else esc(part)
        return out
    common = [x if GUIDE_DONE_SHOTS else x.replace(' [SHOT patcher-done]', '') for x in g['common']]
    if RELEASED:                                    # with 4.0: the release's patcher
        dl = (f'<p style="margin:10px 0 0"><a class="btn green" href="{PATCHER}">{esc(t["dl"])}</a></p>'
              f'<p class="note" style="margin:8px 0 0"><a href="{RELEASE_PAGE}">{esc(t["cur40"])}</a>'
              + (f' · MD5 <code>{PATCHER_MD5}</code>' if PATCHER_MD5 else '') + '</p>')
    else:                                           # until then: disabled, and the current 3.3.6 on GitHub
        dl = (f'<p style="margin:10px 0 0"><span class="btn green soon-btn disabled" aria-disabled="true">{esc(t["dl"])}'
              f'<small>{esc(t["dl_with40"])}</small></span></p>'
              f'<p class="note" style="margin:8px 0 0"><a href="{REPO}/releases/tag/v3.3.6">{esc(t["cur336"])}</a></p>')
    steps = ''.join(f'<li>{text(x)}' + (dl if i == 0 else '') + '</li>' for i, x in enumerate(common))
    cases = ''.join(f'<h2>{esc(h)}</h2><ul>' + ''.join(f'<li>{text(x)}</li>' for x in items) + '</ul>'
                    for h, items in g['cases'] if 'MISTER_DRAFT' not in items)       # MiSTer: held
    body = f'''<div class="wrap page-head"><h1>{esc(g['title'])}</h1>{warn_banner(lang)}<p>{esc(g['lead'])}</p></div>
<div class="wrap doc"><h2>{esc(g['section'])}</h2><ol class="steps">{steps}</ol>
<p class="panel" style="margin-top:16px">{esc(g['fallback'])}{(' ' + esc(t['progfiles_manual'])) if RELEASED else ''}</p>
{f'<p class="panel next" id="progfiles">{esc(t["progfiles"])}</p>' if RELEASED else ''}{cases}{launch_block(lang)}{saves_table(lang)}{joypad_block(lang)}</div>'''
    return page(lang, 'install/', g['title'], body, active='install')


def bug_page(d, lang):
    t = T[lang]
    f = t['bug_form']
    body = f'''<div class="wrap page-head"><h1>{esc(t['bug_title'])}</h1><p>{esc(t['bug_lead'])}</p>
<p class="note">{esc(t['bug_privacy'])} <a href="{REPO}/issues">{esc(t['bug_github'])}</a>.</p></div>
<div class="wrap"><div class="panel" style="background:#fff;padding:12px">
<iframe src="https://tally.so/embed/{f}?alignLeft=1&amp;hideTitle=1&amp;dynamicHeight=1" data-tally-src="https://tally.so/embed/{f}?alignLeft=1&amp;hideTitle=1&amp;dynamicHeight=1" loading="lazy"
 width="100%" height="900" frameborder="0" marginheight="0" marginwidth="0" title="{esc(t['bug_title'])}"></iframe>
<noscript><a href="https://tally.so/r/{f}">{esc(t['bug_title'])}</a></noscript></div></div>
<script src="https://tally.so/widgets/embed.js" async></script>'''
    return page(lang, 'bug/', t['bug_title'], body)


def news_page(d, lang):
    """'What's new in 4.0' from release/notes-4.0.md (EN / IT; FR / DE translated block by block)."""
    t = T[lang]
    src = split_langs(open(os.path.join(DATA, 'next', 'notes-4.0.md'), encoding='utf-8').read())
    bl = md.blocks(src['it' if lang == 'it' else 'en'])
    if bl and bl[0][0] == 'h':
        bl = bl[1:]                                  # the release title
    if lang in ('fr', 'de'):
        bl, _ = tr.translate(bl, lang)
    bl = [b for b in bl if not (b[0] == 'p' and b[1].strip() == '---')]
    body = (f'<div class="wrap page-head"><h1>{esc(t["news_title"])}</h1>{warn_banner(lang)}</div><div class="wrap doc">'
            + (f'<p><a class="btn green" href="{PATCHER}">{esc(t["dl"])}</a></p>' if RELEASED else
               f'<p class="panel next"><span class="next-tag px">4.0</span> {esc(t["with40"])}</p>'
               f'<p><span class="btn green soon-btn disabled" aria-disabled="true">{esc(t["dl"])}<small>{esc(t["dl_with40"])}</small></span></p>')
            + f'{main_menu(lang).replace("<section class=\"wrap\">", "").replace("</section>", "")}{winners_block(lang)}'
            f'{md.render(bl, _notes_link(lang), shift=-1)}</div>')
    return page(lang, 'news/', t['news_title'], body)


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
<meta property="og:image" content="{SITE_URL}/static/og-en.png?v=41"><meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:image" content="{SITE_URL}/static/og-en.png?v=41">
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
        pend = os.path.join(ROOT, 'static', 'pending', f)   # a new take of an approved frame waits for its check
        ok = json.load(open(os.path.join(DATA, 'frames_ok.json'))) if os.path.exists(os.path.join(DATA, 'frames_ok.json')) else []
        target = pend if f[:-4] in ok and os.path.exists(dst) else dst
        newer = not os.path.exists(dst) or os.path.getmtime(dst) < os.path.getmtime(src)
        if f.endswith('.png') and newer and (not os.path.exists(target) or os.path.getmtime(target) < os.path.getmtime(src)):
            from PIL import Image
            os.makedirs(os.path.dirname(target), exist_ok=True)
            im = Image.open(src)
            im.resize((im.width * 5, im.height * 6), Image.NEAREST).save(target, optimize=True)
            print(f'frame: {f}' + (' (pending: approve with build.py --approve NAME)' if target == pend else ''))


def build():
    frames_in()
    d = load()
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(os.path.join(ROOT, 'static'), os.path.join(OUT, 'static'), ignore=shutil.ignore_patterns('pending'))
    write('static/logo.svg', logo_svg(64, 'World of SWOS'))
    if FRAMES_OK is not None:                       # unchecked frames are not published at all
        img = os.path.join(OUT, 'static', 'img')
        for f in os.listdir(img):
            if f.endswith('.png') and f != '12bit.png' and f[:-4] not in FRAMES_OK:
                os.remove(os.path.join(img, f))
    for lang in LANGS:                              # the social preview cards
        t = T[lang]
        ogimage.card(os.path.join(OUT, 'static', f'og-{lang}.png'), t['tagline'], t['concept'],
                     t['out_now'] if RELEASED else t['soon'], t['out_sub'] if RELEASED else t['soon_dl'],
                     '' if RELEASED else t['soon_test'], green=RELEASED)
    urls = []
    for lang in LANGS:
        pages = {'': home(d, lang), 'countries/': countries_index(d, lang), 'world/': world(d, lang),
                 'credits/': credits(d, lang), 'classic/': classic_page(d, lang), 'bug/': bug_page(d, lang)}
        if INSTALL_PAGE:
            pages['install/'] = install_page(d, lang)
        if CONTENT_40:
            pages['news/'] = news_page(d, lang)
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
    if '--approve' in sys.argv:                      # build.py --approve name-xx [name-yy ...]: a checked new take goes live
        for n in sys.argv[sys.argv.index('--approve') + 1:]:
            pend = os.path.join(ROOT, 'static', 'pending', n + '.png')
            if os.path.exists(pend):
                os.replace(pend, os.path.join(ROOT, 'static', 'img', n + '.png'))
            ok = set(json.load(open(os.path.join(DATA, 'frames_ok.json'))))
            ok.add(n)
            json.dump(sorted(ok), open(os.path.join(DATA, 'frames_ok.json'), 'w'), indent=0)
            print('approved', n)
        sys.exit(0)
    if '--refresh' in sys.argv:
        refresh()
    build()
