# World of SWOS

The website of the **SWOS 96/97 Mod** (an unofficial, free fan mod of Sensible World of Soccer 96/97):
https://worldofswos.com, in Italian, English, French and German.

A static site generated from the mod's own release data by `build.py` (plain Python 3, no framework):

```bash
python3 build.py --refresh   # re-read the mod's release texts into data/ (needs the mod's repo), then build
python3 build.py             # build site/ from data/
```

- `data/`: the release notes and competition lists (public parts only) and the in-game FORMAT texts.
- `data/tr/`: the French and German translations of the notes, block by block (`python3 gen/tr.py todo fr|de`).
- `gen/`: texts in the four languages (`i18n.py`, `classic.py`), the small Markdown reader, the translations tool.
- `static/`: style, script, the Silkscreen pixel font (SIL OFL 1.1), game screens.
- `site/`: the generated site, published by GitHub Pages (`.github/workflows/pages.yml`).

Sensible World of Soccer and all club, league and competition names belong to their owners; this site is not
affiliated with or endorsed by any of them. The mod itself: https://github.com/aminta/swos-9697-mod
