#!/usr/bin/env python3
"""Build the manual with the pinned, unchanged Gopher HTTP publisher."""
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--php', default=os.environ.get('PHP_BIN', 'php'))
    args = parser.parse_args()
    publisher = ROOT / 'vendor/gopher'
    provenance = json.loads((publisher / 'PROVENANCE.json').read_text())
    for name, expected in provenance['files'].items():
        actual = hashlib.sha256((publisher / name).read_bytes()).hexdigest()
        if actual != expected:
            raise SystemExit('Vendored Gopher integrity mismatch: ' + name)
    subprocess.run([args.php, '-r', 'exit(PHP_VERSION_ID >= 80200 && extension_loaded("ctype") ? 0 : 1);'], check=True, timeout=20)
    entry = str(publisher / 'index.php')
    subprocess.run([args.php, entry, 'check', '--source', 'content', '--strict'], cwd=ROOT, check=True, timeout=90)
    subprocess.run([args.php, entry, 'build', '--source', 'content', '--output', 'docs', '--replace', '--strict'], cwd=ROOT, check=True, timeout=90)
    enhancer = ROOT / 'tools/enhance.py'
    if enhancer.is_file():
        subprocess.run([sys.executable, str(enhancer), '--site', 'docs'], cwd=ROOT, check=True, timeout=60)
    (ROOT / 'docs/.nojekyll').write_text('')
    print('Gopher manual build completed.')


if __name__ == '__main__':
    main()
