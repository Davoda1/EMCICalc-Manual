#!/usr/bin/env python3
"""Bounded offline checks for the generated manual and its authored inputs."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit
import hashlib
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / 'docs'
TEXT = {'.md', '.txt', '.json', '.html', '.htm', '.css', '.js', '.py', '.sh', '.yml', '.yaml', '.php', '.svg'}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.duplicate_ids = []
        self.links = []
        self.images = 0
        self.missing_alt = 0
        self.h1 = 0
        self.lang = ''
        self.viewport = False
        self.csp = False
        self.title_text = ''
        self.in_title = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        ident = attrs.get('id')
        if ident:
            if ident in self.ids: self.duplicate_ids.append(ident)
            self.ids.add(ident)
        if tag == 'html': self.lang = attrs.get('lang', '')
        if tag == 'h1': self.h1 += 1
        if tag == 'title': self.in_title = True
        if tag == 'meta' and attrs.get('name', '').lower() == 'viewport': self.viewport = True
        if tag == 'meta' and attrs.get('http-equiv', '').lower() == 'content-security-policy': self.csp = True
        if tag == 'img':
            self.images += 1
            if not attrs.get('alt', '').strip(): self.missing_alt += 1
        for attr in ('href', 'src', 'poster'):
            if attrs.get(attr): self.links.append((tag, attr, attrs[attr]))
        if attrs.get('srcset'):
            for item in attrs['srcset'].split(','):
                self.links.append((tag, 'src', item.strip().split()[0]))

    def handle_endtag(self, tag):
        if tag == 'title': self.in_title = False

    def handle_data(self, data):
        if self.in_title: self.title_text += data


def main():
    errors = []
    pages = {}
    if not (SITE/'index.html').is_file(): errors.append('Missing generated index.html')
    if not (SITE/'.nojekyll').is_file(): errors.append('Missing .nojekyll')
    for path in sorted(SITE.rglob('*.html')):
        page = Page()
        try: page.feed(path.read_text(encoding='utf-8'))
        except (UnicodeError, ValueError) as exc:
            errors.append(f'{path.relative_to(SITE)}: {exc}')
            continue
        pages[path.resolve()] = page
        rel = path.relative_to(SITE)
        if not page.lang or not page.viewport or not page.title_text.strip() or not page.csp:
            errors.append(f'{rel}: missing language, viewport, title or CSP')
        if page.h1 != 1: errors.append(f'{rel}: expected one main heading')
        if page.missing_alt: errors.append(f'{rel}: image without explanatory alt text')
        if page.duplicate_ids: errors.append(f'{rel}: duplicate HTML IDs')
    references = 0
    for path, page in pages.items():
        for tag, attr, raw in page.links:
            link = urlsplit(raw)
            if link.scheme or link.netloc:
                if link.scheme == 'data' and tag in {'img', 'image', 'link'} and raw.startswith('data:image/'): continue
                if tag == 'a' and link.scheme in {'http', 'https', 'mailto'}: continue
                errors.append(f'{path.relative_to(SITE)}: remote or unsupported embedded resource')
                continue
            if not link.path and not link.fragment: continue
            references += 1
            target = (path.parent / unquote(link.path)).resolve() if link.path else path
            try: target.relative_to(SITE.resolve())
            except ValueError:
                errors.append(f'{path.relative_to(SITE)}: link escapes generated site')
                continue
            if target.is_dir(): target = target/'index.html'
            if not target.is_file():
                errors.append(f'{path.relative_to(SITE)}: missing local target {link.path}')
            elif link.fragment and target in pages and unquote(link.fragment) not in pages[target].ids:
                errors.append(f'{path.relative_to(SITE)}: missing section {link.fragment}')
    # Patterns are assembled so this checker does not itself contain disallowed branding.
    blocked = [re.compile('EMCI' + r'\s+Tech', re.I), re.compile('EMCICalc' + r'[^\n]{0,30}\b2\.0\.0', re.I),
               re.compile(r'(?:personal|private)\s+(?:builds?|versions?|development)', re.I)]
    secrets = re.compile(r'(?:github_' + r'pat_[A-Za-z0-9_]{25,}|gh[pousr]_[A-Za-z0-9_]{25,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)')
    private_paths = re.compile(r'(?:/work' + r'space/(?:scratch|projects)/|/(?:home|Users)/[A-Za-z0-9_.-]+/|[A-Za-z]:\\Users\\[^\\]+\\)')
    checked_text = 0
    for directory in ['content', 'docs', 'tools', '.github']:
        for path in (ROOT/directory).rglob('*'):
            if not path.is_file() or path.suffix.lower() not in TEXT: continue
            if '__pycache__' in path.parts: continue
            text = path.read_text(errors='replace')
            checked_text += 1
            if secrets.search(text): errors.append(f'{path.relative_to(ROOT)}: credential marker')
            if private_paths.search(text): errors.append(f'{path.relative_to(ROOT)}: private filesystem path')
            if path.name != 'check_site.py' and any(pattern.search(text) for pattern in blocked):
                errors.append(f'{path.relative_to(ROOT)}: unrelated/private development reference')
    for name in ['README.md', 'LICENSE']:
        text = (ROOT/name).read_text()
        if secrets.search(text) or private_paths.search(text) or any(p.search(text) for p in blocked):
            errors.append(name+': source privacy guard failed')
    provenance = json.loads((ROOT/'vendor/gopher/PROVENANCE.json').read_text())
    for name, digest in provenance['files'].items():
        if hashlib.sha256((ROOT/'vendor/gopher'/name).read_bytes()).hexdigest() != digest:
            errors.append('Gopher publisher integrity mismatch: '+name)
    if errors:
        print('\n'.join('FAIL '+error for error in errors))
        return 1
    print(f'PASS: {len(pages)} HTML pages, {references} local references, {checked_text} text inputs; links, assets, accessibility basics, source privacy and Gopher integrity.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
