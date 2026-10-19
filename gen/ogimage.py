"""The social preview card (Open Graph, 1200x630) per language: the SWOS menu look, the pixel ball-planet,
the tagline, and the red "coming soon" sticker until 4.0 is out."""
import math
import os

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
W, H = 1200, 630
BALL = ['.....WWWWWW.....', '...WWWWBBWWWWS..', '..WWWWBBBBWWWWS.', '.WBWWWWBBWWWWBS.', '.WBBWWWWWWWWBBS.',
        'WBBBWWWWWWWWBBBS', 'WWBWWWBBBBWWWBWS', 'WWWWWBBBBBBWWWWS', 'WWWWWBBBBBBWWWSS', 'WWWWWWBBBBWWWWSS',
        'WBWWWWWWWWWWWBSS', 'WBBWWWWWWWWWBBSS', '.WBBWWWBBWWBBSS.', '..WWWWBBBBWWSS..', '...WWWWBBWSSS...',
        '.....SSSSSS.....']
COL = {'W': (232, 237, 255), 'B': (11, 29, 122), 'S': (143, 162, 238)}


def font(size, bold=True):
    return ImageFont.truetype(os.path.join(HERE, 'fonts', 'Silkscreen-Bold.ttf' if bold else 'Silkscreen-Regular.ttf'), size)


def shadow_text(d, xy, text, f, fill, shadow=(0, 3, 24), off=4, anchor='la'):
    x, y = xy
    d.text((x + off, y + off), text, font=f, fill=shadow, anchor=anchor)
    d.text((x, y), text, font=f, fill=fill, anchor=anchor)


def wrap(text, f, width, d):
    words, lines, cur = text.split(), [], ''
    for w in words:
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= width:
            cur = t
        else:
            lines.append(cur)
            cur = w
    return lines + [cur] if cur else lines


def card(path, tagline, concept, soon, soon_sub):
    im = Image.new('RGB', (W, H), (3, 10, 51))
    px = im.load()
    for y in range(H):                                   # radial blue, as the site's background
        for x in range(0, W, 2):
            r = math.hypot((x - 330) / 900, (y - 200) / 560)
            t = max(0.0, min(1.0, r))
            c = (int(26 + (3 - 26) * t), int(58 + (10 - 58) * t), int(208 + (51 - 208) * t))
            px[x, y] = c
            if x + 1 < W:
                px[x + 1, y] = c
    d = ImageDraw.Draw(im)
    for k in range(1, 9):                                # faint meridians and parallels
        d.ellipse([330 - k * 120, 200 - k * 50, 330 + k * 120, 200 + k * 50], outline=(60, 90, 220), width=1)
    for x in range(-60, W, 110):
        d.line([(x, 0), (x, H)], fill=(40, 70, 200), width=1)
    # the pixel ball-planet with its orbit
    s, ox, oy = 14, 70, 70
    d.ellipse([ox - 40, oy + 70, ox + 16 * s + 40, oy + 16 * s - 70], outline=(255, 216, 74), width=10)
    for y, row in enumerate(BALL):
        for x, c in enumerate(row):
            if c in COL:
                d.rectangle([ox + x * s, oy + y * s, ox + x * s + s - 1, oy + y * s + s - 1], fill=COL[c])
    d.arc([ox - 40, oy + 70, ox + 16 * s + 40, oy + 16 * s - 70], 200, 340, fill=(255, 216, 74), width=10)
    d.rectangle([ox + 15 * s, oy + s, ox + 16 * s + 6, oy + 2 * s + 6], fill=(255, 154, 60))
    # wordmark and tagline
    shadow_text(d, (360, 92), 'WORLD OF SWOS', font(64), (255, 255, 255))
    shadow_text(d, (364, 172), 'SWOS 96/97 MOD 4.0', font(28, False), (180, 188, 230), off=3)
    f = font(34)
    y = 270
    for line in wrap(tagline.upper(), f, 780, d):
        shadow_text(d, (360, y), line, f, (255, 255, 255), off=3)
        y += 46
    f2 = font(24, False)
    y += 14
    for line in wrap(concept.upper(), f2, 780, d):
        shadow_text(d, (360, y), line, f2, (255, 216, 74), off=3)
        y += 34
    shadow_text(d, (W - 40, H - 34), 'WORLDOFSWOS.COM', font(26), (255, 255, 255), off=3, anchor='rs')
    # the red diagonal sticker, under the ball (the left column)
    if soon:
        sw, sh = 300, 150
        st = Image.new('RGBA', (sw + 10, sh + 10), (0, 0, 0, 0))
        sd = ImageDraw.Draw(st)
        sd.rectangle([10, 10, sw + 9, sh + 9], fill=(0, 3, 24, 255))
        for i in range(sh):
            t = i / (sh - 1)
            sd.line([(0, i), (sw - 1, i)], fill=(int(255 - 117 * t), int(74 - 68 * t), int(58 - 42 * t), 255))
        sd.rectangle([0, 0, sw - 1, sh - 1], outline=(255, 154, 138, 255), width=4)
        fs = font(40)
        words = soon.upper().split()
        shadow_text(sd, (sw // 2, 38), words[0], fs, (255, 255, 255), shadow=(74, 2, 6), off=4, anchor='mm')
        shadow_text(sd, (sw // 2, 80), ' '.join(words[1:]), fs, (255, 255, 255), shadow=(74, 2, 6), off=4, anchor='mm')
        f3 = font(15, False)
        yy = 112
        for line in wrap(soon_sub.upper(), f3, sw - 24, sd)[:2]:
            shadow_text(sd, (sw // 2, yy), line, f3, (255, 255, 255), shadow=(74, 2, 6), off=2, anchor='mm')
            yy += 20
        st = st.rotate(6, expand=True, resample=Image.BICUBIC)
        im.paste(st, (30, 360), st)
    im.save(path, optimize=True)
