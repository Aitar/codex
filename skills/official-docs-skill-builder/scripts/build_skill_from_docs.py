#!/usr/bin/env python3
"""Build a new Codex skill folder from official docs pages."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Iterable
from urllib.parse import urlparse


def normalize_skill_name(raw_name: str) -> str:
    normalized = raw_name.strip().lower()
    normalized = re.sub(r'[^a-z0-9]+', '-', normalized)
    normalized = re.sub(r'-{2,}', '-', normalized).strip('-')
    return normalized[:64]


def title_case_skill_name(skill_name: str) -> str:
    return ' '.join(part.capitalize() for part in skill_name.split('-') if part)


def normalize_short_description(text: str) -> str:
    value = re.sub(r'\s+', ' ', text.strip())
    if len(value) < 25:
        value = f'{value} docs workflow and references'
    if len(value) > 64:
        value = value[:61].rstrip() + '...'
    return value


def write_openai_yaml(
    target_dir: Path,
    display_name: str,
    short_description: str,
    default_prompt: str,
) -> None:
    content = (
        'interface:\n'
        f'  display_name: "{display_name}"\n'
        f'  short_description: "{short_description}"\n'
        f'  default_prompt: "{default_prompt}"\n'
    )
    agents_dir = target_dir / 'agents'
    agents_dir.mkdir(parents=True, exist_ok=True)
    (agents_dir / 'openai.yaml').write_text(content, encoding='utf-8')


def write_skill_md(target_dir: Path, skill_name: str, topic: str) -> None:
    description = (
        f'Reference skill generated from official {topic} documentation. '
        f'Use when answering {topic} APIs, configs, constraints, version behavior, or integration details.'
    )
    content = f"""---
name: {skill_name}
description: {description}
---

# {title_case_skill_name(skill_name)}

## Overview

Answer questions using the bundled official docs references first.
Load only relevant files from `references/pages/` based on the question topic.

## Working Rules

1. Locate relevant pages by scanning `references/docs-index.md`.
2. Read only the minimum set of files needed to answer.
3. Prefer documented behavior over assumptions.
4. Include caveats when docs are version-dependent.
5. Flag missing coverage when the references do not contain the needed detail.

## Reference Map

- `references/docs-index.md`: page inventory with titles and URLs.
- `references/pages/*.md`: cleaned official documentation content.
"""
    (target_dir / 'SKILL.md').write_text(content, encoding='utf-8')


def write_docs_index(references_dir: Path, topic: str, index: dict) -> None:
    lines = [
        f'# {topic} Docs Index',
        '',
        f'- Captured pages: {index.get("captured_count", 0)}',
        f'- Visited URLs: {index.get("visited_count", 0)}',
        f'- Removed noise lines: {index.get("total_removed_noise_lines", 0)}',
        '',
        '| Title | Words | Removed Lines | Source | File |',
        '| --- | ---: | ---: | --- | --- |',
    ]

    pages = sorted(index.get('pages', []), key=lambda item: (item.get('depth', 0), item.get('title', '')))
    for page in pages:
        title = (page.get('title') or '').replace('|', '\\|')
        source = page.get('url') or ''
        file_path = page.get('path') or ''
        words = page.get('word_count', 0)
        removed = page.get('removed_noise_lines', 0)
        lines.append(f'| {title} | {words} | {removed} | {source} | `{file_path}` |')

    if index.get('errors'):
        lines.extend(['', '## Crawl Errors', ''])
        for err in index['errors'][:50]:
            url = err.get('url', '')
            msg = err.get('error', '').replace('\n', ' ')
            lines.append(f'- `{url}`: {msg}')

    (references_dir / 'docs-index.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def flatten_repeatable(values: Iterable[str]) -> list[str]:
    return [item for item in values if item and item.strip()]


def derive_project_slug(url: str) -> str:
    parsed = urlparse(url.strip())
    host = parsed.netloc.lower()
    labels = [label for label in host.split('.') if label]
    if not labels:
        return 'docs'
    if labels[0] == 'docs' and len(labels) >= 2:
        base = labels[1]
    else:
        base = labels[0]
    return normalize_skill_name(base) or 'docs'


def derive_version_slug(url: str) -> str:
    parsed = urlparse(url.strip())
    parts = [part for part in parsed.path.split('/') if part]
    if len(parts) >= 2 and re.fullmatch(r'[a-z]{2}(?:-[a-z]{2})?', parts[0]):
        version = parts[1]
        if version == 'latest':
            return 'latest'
        if re.fullmatch(r'v\d+(?:\.\d+){1,3}', version):
            return version[1:].replace('.', '-')
        return normalize_skill_name(version) or 'docs'
    return 'docs'


def derive_skill_name_from_start_urls(start_urls: list[str]) -> str:
    if not start_urls:
        return 'official-docs'
    base = start_urls[0]
    project = derive_project_slug(base)
    version = derive_version_slug(base)
    return normalize_skill_name(f'{project}-{version}') or 'official-docs'


def derive_version_scope_prefix(url: str) -> str | None:
    parsed = urlparse(url.strip())
    if parsed.scheme not in {'http', 'https'} or not parsed.netloc:
        return None

    parts = [part for part in parsed.path.split('/') if part]
    if len(parts) < 2:
        return None

    lang = parts[0]
    version = parts[1]
    if not re.fullmatch(r'[a-z]{2}(?:-[a-z]{2})?', lang):
        return None
    if version != 'latest' and not re.fullmatch(r'v\d+(?:\.\d+){1,3}', version):
        return None

    return f'{parsed.scheme}://{parsed.netloc}/{lang}/{version}/'


def build_effective_prefixes(args: argparse.Namespace) -> list[str]:
    prefixes = flatten_repeatable(args.include_prefix)
    if args.no_auto_scope_by_version:
        return prefixes

    derived: list[str] = []
    for url in flatten_repeatable(args.start_url):
        scope = derive_version_scope_prefix(url)
        if scope:
            derived.append(scope)

    for item in derived:
        if item not in prefixes:
            prefixes.append(item)
    return prefixes


def run_crawler(args: argparse.Namespace, skill_dir: Path) -> dict:
    script_dir = Path(__file__).resolve().parent
    crawler_script = script_dir / 'crawl_docs.py'
    references_dir = skill_dir / 'references'
    cmd = [
        sys.executable,
        str(crawler_script),
        '--output-dir',
        str(references_dir),
        '--max-pages',
        str(args.max_pages),
        '--max-depth',
        str(args.max_depth),
        '--min-chars',
        str(args.min_chars),
        '--timeout',
        str(args.timeout),
        '--max-retries',
        str(args.max_retries),
    ]

    if args.respect_robots:
        cmd.append('--respect-robots')
    if args.keep_query:
        cmd.append('--keep-query')
    if args.delay_seconds > 0:
        cmd.extend(['--delay-seconds', str(args.delay_seconds)])

    for value in flatten_repeatable(args.start_url):
        cmd.extend(['--start-url', value])
    for value in flatten_repeatable(args.allow_domain):
        cmd.extend(['--allow-domain', value])
    for value in build_effective_prefixes(args):
        cmd.extend(['--include-prefix', value])
    for value in flatten_repeatable(args.exclude_regex):
        cmd.extend(['--exclude-regex', value])

    subprocess.run(cmd, check=True)

    index_path = references_dir / 'index.json'
    if not index_path.exists():
        raise FileNotFoundError(f'Missing crawler output: {index_path}')
    return json.loads(index_path.read_text(encoding='utf-8'))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Create a new skill from official docs URLs.')
    parser.add_argument(
        '--skill-name',
        default='',
        help='Target skill name (hyphen-case or plain text). If omitted, derive from start URL.',
    )
    parser.add_argument('--topic', required=True, help='Human-readable topic for descriptions.')
    parser.add_argument('--skills-root', required=True, type=Path, help='Root directory that stores skills.')
    parser.add_argument('--start-url', action='append', required=True, help='Seed URL. Repeatable.')
    parser.add_argument('--allow-domain', action='append', default=[], help='Allowed domain. Repeatable.')
    parser.add_argument('--include-prefix', action='append', default=[], help='URL prefix filter. Repeatable.')
    parser.add_argument('--exclude-regex', action='append', default=[], help='Regex URL deny rule.')
    parser.add_argument('--max-pages', type=int, default=120)
    parser.add_argument('--max-depth', type=int, default=3)
    parser.add_argument('--min-chars', type=int, default=40)
    parser.add_argument('--timeout', type=float, default=20.0)
    parser.add_argument('--max-retries', type=int, default=2)
    parser.add_argument('--delay-seconds', type=float, default=0.0)
    parser.add_argument('--respect-robots', action='store_true')
    parser.add_argument('--keep-query', action='store_true')
    parser.add_argument(
        '--no-auto-scope-by-version',
        action='store_true',
        help='Disable automatic expansion from /<lang>/<version>/... to /<lang>/<version>/',
    )
    parser.add_argument('--overwrite', action='store_true', help='Remove existing target folder first.')
    parser.add_argument('--display-name', default='', help='Override display_name in agents/openai.yaml')
    parser.add_argument('--short-description', default='', help='Override short_description in agents/openai.yaml')
    parser.add_argument('--default-prompt', default='', help='Override default_prompt in agents/openai.yaml')
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    raw_skill_name = args.skill_name.strip() or derive_skill_name_from_start_urls(
        flatten_repeatable(args.start_url)
    )
    skill_name = normalize_skill_name(raw_skill_name)
    if not skill_name:
        print('Invalid --skill-name')
        return 1

    skill_dir = args.skills_root.resolve() / skill_name
    if skill_dir.exists():
        if not args.overwrite:
            print(f'Target directory exists: {skill_dir}. Use --overwrite to replace it.')
            return 1
        shutil.rmtree(skill_dir)

    (skill_dir / 'references').mkdir(parents=True, exist_ok=True)
    index = run_crawler(args, skill_dir)

    write_skill_md(skill_dir, skill_name, args.topic)
    write_docs_index(skill_dir / 'references', args.topic, index)

    display_name = args.display_name.strip() or title_case_skill_name(skill_name)
    short_description = args.short_description.strip() or f'Official {args.topic} docs references'
    short_description = normalize_short_description(short_description)
    default_prompt = args.default_prompt.strip() or (
        f'Answer {args.topic} questions using bundled official documentation references.'
    )
    write_openai_yaml(skill_dir, display_name, short_description, default_prompt)

    print(f'Skill generated at: {skill_dir}')
    print(f'Captured pages: {index.get("captured_count", 0)}')
    print(f'Index file: {skill_dir / "references" / "docs-index.md"}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
