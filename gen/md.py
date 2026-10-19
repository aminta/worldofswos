"""A small Markdown reader for the mod's own release texts (notes, competition lists, pack guides).

What they use: ##/###/#### headings, **bold** lines as headings, *italic* lines as sub-headings, nested '- ' lists
(two-space indents, continuation lines), paragraphs of wrapped lines, **bold**, *italic*, `code`, [text](link).
HTML comments are dropped (staged / internal parts of the notes never reach the site).
"""
import html
import re

COMMENT = re.compile(r'<!--.*?-->', re.S)


def strip_comments(text):
    return COMMENT.sub('', text)


def inline(s, link=None):
    """Inline markup -> HTML. link(url) maps a link target (e.g. a .md in the repo) to a site URL, or None to unlink."""
    out, pos = [], 0
    for m in re.finditer(r'\[([^\]]+)\]\(([^)\s]+)\)', s):
        out.append(_fmt(s[pos:m.start()]))
        url = link(m.group(2)) if link else m.group(2)
        txt = _fmt(m.group(1))
        out.append(f'<a href="{html.escape(url)}">{txt}</a>' if url else txt)
        pos = m.end()
    out.append(_fmt(s[pos:]))
    return ''.join(out)


def _fmt(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    s = re.sub(r'(?<![\w"=/])(https?://[^\s<)]+[^\s<).,;:])', r'<a href="\1">\1</a>', s)
    return s


def blocks(text):
    """Text -> [('h', level, text) | ('p', text) | ('sub', text) | ('list', items)]; item = [text, children items]."""
    lines = strip_comments(text).split('\n')
    out, para, stack = [], [], None          # stack: [(indent, items)] of the open list

    def flush_para():
        if para:
            out.append(('p', ' '.join(x.strip() for x in para)))
            para.clear()

    def close_list():
        nonlocal stack
        stack = None

    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            flush_para()
            close_list()
            continue
        ind = len(line) - len(line.lstrip(' '))
        s = line.strip()
        m = re.match(r'(#{1,6})\s+(.*)', s)
        if m and ind == 0:
            flush_para(), close_list()
            out.append(('h', len(m.group(1)), m.group(2)))
            continue
        if s.startswith('- ') or s.startswith('* ') and not s.startswith('**'):
            flush_para()
            item = [s[2:], []]
            if stack is None:
                items = []
                out.append(('list', items))
                stack = [(ind, items)]
            while len(stack) > 1 and ind < stack[-1][0]:
                stack.pop()
            if ind > stack[-1][0]:
                parent = stack[-1][1][-1] if stack[-1][1] else None
                if parent is not None:
                    stack.append((ind, parent[1]))
            elif ind < stack[-1][0]:
                stack[-1] = (ind, stack[-1][1])
            stack[-1][1].append(item)
            continue
        if stack is not None and ind > 0:       # continuation of the last item
            last = stack[-1][1][-1]
            last[0] += ' ' + s
            continue
        close_list()
        if re.fullmatch(r'\*\*[^*]+\*\*', s) and not para:
            out.append(('h', 4, s[2:-2]))
            continue
        if re.fullmatch(r'\*[^*].*[^*]\*', s) and not para:
            out.append(('sub', s[1:-1]))
            continue
        if re.fullmatch(r'\*[^*].*[^*]\*', s):
            flush_para()
            out.append(('sub', s[1:-1]))
            continue
        para.append(s)
    flush_para()
    return out


def render_items(items, link=None):
    li = []
    for txt, kids in items:
        li.append('<li>' + inline(txt, link) + (render_items(kids, link) if kids else '') + '</li>')
    return '<ul>' + ''.join(li) + '</ul>'


def render(bl, link=None, shift=0, ids=None):
    """Blocks -> HTML. shift: added to heading levels (a '##' document inside a page with its own h1)."""
    out = []
    for b in bl:
        if b[0] == 'h':
            lv = min(6, max(2, b[1] + shift))
            hid = f' id="{ids(b[2])}"' if ids else ''
            out.append(f'<h{lv}{hid}>{inline(b[2], link)}</h{lv}>')
        elif b[0] == 'p':
            out.append(f'<p>{inline(b[1], link)}</p>')
        elif b[0] == 'sub':
            out.append(f'<p><em class="sub">{inline(b[1], link)}</em></p>')
        elif b[0] == 'list':
            out.append(render_items(b[1], link))
    return '\n'.join(out)


def slug(s):
    s = re.sub(r'<[^>]+>|\*', '', s).lower()
    s = re.sub(r"[^a-z0-9àèéìòùäöüßçâêîôûœ]+", '-', s).strip('-')
    return s or 'x'
