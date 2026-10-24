"""FR / DE translations of the English release notes, block by block.

A unit is a heading, a paragraph, an italic sub-heading or one top-level list item with its sub-items, as Markdown.
data/tr/<lang>.json maps sha1(English unit)[:12] -> {"en": English, "t": translation}. A unit whose English changed
has no translation: the page shows the English for it and `python3 gen/tr.py todo fr` lists what to translate.
"""
import hashlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import md  # noqa: E402

TR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'tr')


def _item_md(item, ind=0):
    txt, kids = item
    return '\n'.join([' ' * ind + '- ' + txt] + [_item_md(k, ind + 2) for k in kids])


def units(blocks):
    """[(key, kind, markdown)]; kind: h<level> / p / sub / li"""
    out = []
    for b in blocks:
        if b[0] == 'list':
            for it in b[1]:
                out.append(('li', _item_md(it)))
        elif b[0] == 'h':
            out.append((f'h{b[1]}', b[2]))
        else:
            out.append((b[0], b[1]))
    return [(hashlib.sha1(m.encode()).hexdigest()[:12], k, m) for k, m in out]


def load(lang):
    p = os.path.join(TR, f'{lang}.json')
    return json.load(open(p, encoding='utf-8')) if os.path.exists(p) else {}


def translate(blocks, lang):
    """English blocks -> blocks in lang (untranslated units stay English); returns (blocks, missing count)."""
    tr, out, miss = load(lang), [], 0
    for key, kind, m in units(blocks):
        t = tr.get(key, {}).get('t')
        if t is None:                          # the release payoff: always the home's own wording
            from i18n import T as _T
            core = m.strip().strip('*_').strip()
            if core == _T['en']['tagline']:
                t = m.replace(core, _T[lang]['tagline'])
        miss += t is None
        src = t if t is not None else m
        if kind == 'li':
            bl = md.blocks(src)
            items = bl[0][1] if bl and bl[0][0] == 'list' else [[src, []]]
            if out and out[-1][0] == 'list' and out[-1][2] == 'open':
                out[-1][1].extend(items)
            else:
                out.append(['list', list(items), 'open'])
            continue
        if out and out[-1][0] == 'list':
            out[-1][2] = 'closed'
        if kind.startswith('h'):
            out.append(('h', int(kind[1:]), src))
        else:
            out.append((kind, src))
    return [tuple(b[:2]) if b[0] == 'list' else b for b in out], miss


if __name__ == '__main__':
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    import build
    cmd, lang = sys.argv[1], sys.argv[2]
    build.RELEASED = True                    # translate the next notes (data/next/), the ones that go live with 4.0
    d = build.load()
    main, cred, _ = build.notes_part(d, "en")
    rel = os.path.join(build.DATA, 'next', 'notes-4.0.md')       # the 4.0 release notes ('What's new' page)
    if os.path.exists(rel):
        cred = cred + md.blocks(build.split_langs(open(rel, encoding='utf-8').read())['en'])
    rel1 = os.path.join(build.DATA, 'next', 'notes-4.0.1.md')    # the 4.0.1 release notes
    if os.path.exists(rel1):
        cred = cred + md.blocks(build.split_langs(open(rel1, encoding='utf-8').read())['en'])
    tr = load(lang)
    todo = [(k, kind, m) for k, kind, m in units(main + cred) if k not in tr]
    if cmd == 'todo':
        json.dump([{'key': k, 'en': m} for k, _, m in todo], sys.stdout, ensure_ascii=False, indent=1)
        print(f'\n{len(todo)} units to translate', file=sys.stderr)
    elif cmd == 'add':                       # add F: [{"key", "t"}] (en filled from the current notes)
        new = json.load(open(sys.argv[3], encoding='utf-8'))
        en = {k: m for k, _, m in units(main + cred)}
        for x in new:
            tr[x['key']] = {'en': en[x['key']], 't': x['t']}
        os.makedirs(TR, exist_ok=True)
        json.dump(tr, open(os.path.join(TR, f'{lang}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print(f'{lang}: {len(tr)} units')
