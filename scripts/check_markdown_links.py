#!/usr/bin/env python3
"""Check local destinations in Markdown (Python standard library only).

Run: python3 scripts/check_markdown_links.py
Checks inline links/images, reference definitions and HTML href/src attributes.
External URLs and fragments are not fetched/validated. This is a lightweight
source-path check, not a full Markdown parser or a rendered-site crawler.
"""
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DESTINATION = r'\s*(?:<([^>]*?)>|([^\s)]*))'
PATTERNS = [
    re.compile(r'!?\[[^\]\n]*\]\(' + DESTINATION),
    re.compile(r'^ {0,3}\[[^\]\n]+\]:' + DESTINATION, re.MULTILINE),
    re.compile(r'\b(?:href|src)\s*=\s*[\"\']([^\"\']*)[\"\']', re.IGNORECASE),
]


def strip_code(text):
    # Preserve newlines so failures report the source line number.
    def blank(match):
        return re.sub(r'[^\n]', ' ', match.group())
    text = re.sub(r'^ {0,3}(`{3,}|~{3,})[^\n]*\n.*?^ {0,3}\1[^\n]*$',
                  blank, text, flags=re.MULTILINE | re.DOTALL)
    text = re.sub(r'<!--.*?-->', blank, text, flags=re.DOTALL)
    return re.sub(r'(`+)[^\n]*?\1', blank, text)


def destination_error(source, target):
    if not target.strip():
        return 'empty destination; use plain text for unfinished ideas'
    url = urlsplit(target)
    if url.scheme or url.netloc:
        return None
    if not url.path:  # Same-page fragment or query.
        return None
    path = unquote(url.path)
    base = ROOT if path.startswith('/') else source.parent
    resolved = (base / path.lstrip('/')).resolve()
    if not resolved.is_relative_to(ROOT):
        return 'destination escapes repository'
    if resolved.is_file():
        return None
    if resolved.is_dir() and any(
        (resolved / name).is_file()
        for name in ('README.md', 'readme.md', 'index.md', 'index.html')
    ):
        return None
    return 'missing file or directory index'


def main():
    names = subprocess.check_output(
        ['git', 'ls-files', '-z'], cwd=ROOT, text=True
    ).split('\0')
    sources = [ROOT / name for name in names if name.lower().endswith('.md')]
    errors = []
    for source in sources:
        text = strip_code(source.read_text(encoding='utf-8'))
        for pattern in PATTERNS:
            for match in pattern.finditer(text):
                target = next(value for value in match.groups() if value is not None)
                error = destination_error(source, target)
                if error:
                    line = text.count('\n', 0, match.start()) + 1
                    errors.append(f'{source.relative_to(ROOT)}:{line}: {target!r}: {error}')
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Checked local link destinations in {len(sources)} Markdown files.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
