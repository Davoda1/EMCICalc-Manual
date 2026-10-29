#!/usr/bin/env python3
"""Add accessible figure legends and vector callouts to Gopher's static output.

The publisher and original screenshot bytes stay unchanged. This hook runs only
after a fresh Gopher build, so its output is deterministic and not cumulative.
"""
from pathlib import Path
from html import escape, unescape
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', type=Path, required=True)
    args = parser.parse_args()
    images = json.loads((ROOT/'manual-images.json').read_text())
    annotations = json.loads((ROOT/'manual-annotations.json').read_text())
    css = (ROOT/'tools/manual.css').read_text()
    by_asset = {}
    for item in images:
        original = ROOT/'content/images'/item['file']
        if hashlib.sha256(original.read_bytes()).hexdigest() != item['sha256']:
            raise SystemExit('Screenshot integrity mismatch: '+item['file'])
        asset = hashlib.sha256(('images/'+item['file']).encode()).hexdigest()+'.png'
        by_asset[asset] = item
    figures = 0
    overlays = 0
    for page in sorted(args.site.rglob('*.html')):
        text = page.read_text()
        page_figures = 0
        def figure(match):
            nonlocal figures, overlays, page_figures
            attrs = dict(re.findall(r'(\w+)="([^"]*)"', match[1]))
            src = unescape(attrs.get('src', ''))
            item = by_asset.get(src.rsplit('/', 1)[-1])
            if item is None:
                return match[0]
            width, height = item['width'], item['height']
            marks = annotations.get(item['file'], [])
            figures += 1
            page_figures += 1
            ident = f'manual-arrow-{page_figures}'
            picture = f'<img src="{escape(src, quote=True)}" alt="{escape(item["alt"], quote=True)}" width="{width}" height="{height}" loading="lazy" decoding="async">'
            overlay = ''
            legend = ''
            if marks:
                overlays += 1
                radius = 18 if width > 600 else 13
                overlay = f'<svg class="manual-callouts" viewBox="0 0 {width} {height}" aria-hidden="true" focusable="false"><defs><marker id="{ident}" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto" markerUnits="strokeWidth"><path d="M0,0 L6,3 L0,6 Z" fill="#ffd166" stroke="#17212b" stroke-width="0.4"/></marker></defs>'
                for number, mark in enumerate(marks, 1):
                    x,y = mark['label']
                    tx,ty = mark['target']
                    overlay += f'<path d="M{x},{y} L{tx},{ty}" stroke="#17212b" stroke-width="7" fill="none"/><path d="M{x},{y} L{tx},{ty}" stroke="#ffd166" stroke-width="3" fill="none" marker-end="url(#{ident})"/><circle cx="{x}" cy="{y}" r="{radius}" fill="#ffd166" stroke="#17212b" stroke-width="2"/><text x="{x}" y="{y}" dy=".35em" text-anchor="middle" fill="#17212b" font-family="sans-serif" font-size="{radius+2}" font-weight="700">{number}</text>'
                overlay += '</svg>'
                legend = '<ol class="manual-legend">'+''.join('<li>'+escape(mark['text'])+'</li>' for mark in marks)+'</ol>'
            return f'<figure class="manual-figure" style="max-width:{width}px"><div class="manual-image">{picture}{overlay}</div><figcaption>{escape(item["alt"])}.{legend}<a href="{escape(src, quote=True)}">Open original screenshot at full size</a></figcaption></figure>'
        # Gopher emits standalone Markdown images inside paragraphs.
        text = re.sub(r'<p><img\s+([^>]+)></p>', figure, text)
        # Chapters carry explicit previous/contents/next links in authored text.
        # Keep Gopher's sibling navigation for image pages and other entries.
        if page.name.endswith('.md.html'):
            text = re.sub(r'<nav class="siblings"[^>]*>.*?</nav>', '', text)
        text = text.replace('</head>', '<style id="manual-reading-style">'+css+'</style></head>', 1)
        page.write_text(text)
    print(f'Enhanced {figures} figures, including {overlays} annotated interface tours.')


if __name__ == '__main__':
    main()
