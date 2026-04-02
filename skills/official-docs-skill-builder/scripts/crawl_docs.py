#!/usr/bin/env python3
"""Crawl official docs pages and export cleaned Markdown files."""

from __future__ import annotations

import argparse
import http.client
import json
import re
import ssl
import time
from collections import deque
from dataclasses import dataclass
from html import unescape
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urljoin, urlparse, urlunparse
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser


BLOCK_TAGS = {
    'p',
    'div',
    'section',
    'article',
    'li',
    'ul',
    'ol',
    'pre',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
    'br',
    'hr',
    'dl',
    'dt',
    'dd',
}
TABLE_TAGS = {'table', 'tr', 'td', 'th'}
VOID_TAGS = {
    'area',
    'base',
    'br',
    'col',
    'embed',
    'hr',
    'img',
    'input',
    'link',
    'meta',
    'param',
    'source',
    'track',
    'wbr',
}
SKIP_TAGS = {'script', 'style', 'noscript', 'svg', 'canvas', 'iframe'}
CONTENT_CLASS_HINTS = {
    'md-content__inner',
    'md-content',
    'rst-content',
    'markdown-body',
    'theme-doc-markdown',
    'doc-content',
    'article-content',
    'content-main',
    'wy-nav-content',
}
NOISE_CLASS_HINTS = {
    'md-sidebar',
    'md-header',
    'md-footer',
    'toc',
    'navbar',
    'breadcrumb',
    'pagination',
    'menu',
    'search',
}
NOISE_EXACT_LINES = {
    'navigation',
    'table of contents',
    'skip to content',
    'back to top',
    'edit this page',
    'show source',
    'report a bug',
    'search',
    'theme',
}
NOISE_LINE_PATTERNS = [
    re.compile(r'^(previous(\s+topic)?|next(\s+topic)?)$', re.IGNORECASE),
    re.compile(r'^modules?\s*\|\s*next\s*\|\s*previous$', re.IGNORECASE),
    re.compile(r'^(index|home|github)$', re.IGNORECASE),
    re.compile(r'^python\s*».*documentation\s*»$', re.IGNORECASE),
]


def normalize_url(raw_url: str, keep_query: bool = False) -> str:
    parsed = urlparse(raw_url.strip())
    if parsed.scheme not in {'http', 'https'}:
        return ''

    netloc = parsed.netloc.lower()
    path = parsed.path or '/'
    query = parsed.query if keep_query else ''
    normalized = parsed._replace(netloc=netloc, path=path, params='', query=query, fragment='')
    return urlunparse(normalized)


def domain_from_url(url: str) -> str:
    return urlparse(url).netloc.split(':')[0].lower()


def sanitize_segment(segment: str) -> str:
    value = re.sub(r'[^a-zA-Z0-9._-]+', '-', segment).strip('-_.').lower()
    return value or 'index'


def safe_slug(url: str) -> Path:
    parsed = urlparse(url)
    parts = [part for part in parsed.path.split('/') if part]

    if len(parts) >= 3 and re.fullmatch(r'[a-z]{2}(?:-[a-z]{2})?', parts[0]):
        if parts[1] == 'latest' or re.fullmatch(r'v\d+(?:\.\d+){1,3}', parts[1]):
            parts = parts[2:]

    if not parts:
        parts = ['index']

    last = parts[-1]
    if last.endswith('.html'):
        last = last[:-5] or 'index'
    last = sanitize_segment(last)
    directories = [sanitize_segment(item) for item in parts[:-1]]
    return Path(*directories, f'{last}.md')


def clean_text(raw: str) -> str:
    text = raw.replace('\r', '\n')
    text = re.sub(r'[ \t\f\v]+', ' ', text)
    text = re.sub(r'\n[ \t]+', '\n', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def collapse_blank_lines(lines: list[str]) -> list[str]:
    out: list[str] = []
    prev_blank = False
    in_fence = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('```'):
            in_fence = not in_fence
            out.append(stripped)
            prev_blank = False
            continue
        if in_fence:
            out.append(line.rstrip())
            prev_blank = False
            continue
        if line == '':
            if prev_blank:
                continue
            prev_blank = True
        else:
            prev_blank = False
        out.append(line)
    return out


def should_drop_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if re.match(r'^\|.*\|$', stripped):
        return False

    lower = stripped.lower()
    if lower in NOISE_EXACT_LINES:
        return True
    if any(pattern.match(lower) for pattern in NOISE_LINE_PATTERNS):
        return True
    if re.fullmatch(r'[\W_]+', stripped):
        return True
    if lower.startswith('theme ') and len(lower.split()) <= 3:
        return True
    if lower.startswith('made with ') and 'mkdocs' in lower:
        return True
    if lower.startswith('go to repository'):
        return True
    if lower.endswith(' documentation »') and '»' in lower:
        return True
    return False


def denoise_text(raw: str) -> str:
    lines = raw.replace('\r\n', '\n').replace('\r', '\n').split('\n')
    cleaned: list[str] = []
    in_fence = False
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('```'):
            in_fence = not in_fence
            cleaned.append(stripped)
            continue
        if in_fence:
            cleaned.append(line.rstrip())
            continue

        line = re.sub(r'[ \t\f\v]+', ' ', line)
        value = line.strip()
        if should_drop_line(value):
            continue
        if cleaned and cleaned[-1] == value:
            continue
        cleaned.append(value)
    return '\n'.join(collapse_blank_lines(cleaned)).strip()


def attrs_to_tokens(attr_map: dict[str, str]) -> set[str]:
    tokens: set[str] = set()
    for key in ('id', 'class', 'role', 'data-md-component', 'aria-label'):
        raw = attr_map.get(key, '')
        for token in re.split(r'[\s_:/.-]+', raw.lower()):
            if token:
                tokens.add(token)
    return tokens


def is_content_container(tag: str, attr_map: dict[str, str], tokens: set[str]) -> bool:
    if tag == 'article':
        return True
    attr_id = attr_map.get('id', '').lower()
    if attr_id in {'content', 'main-content', 'docs-content', 'article-content'}:
        return True
    classes = attr_map.get('class', '').lower()
    if tag == 'main' and any(hint in classes for hint in CONTENT_CLASS_HINTS):
        return True
    if attr_map.get('role', '').lower() == 'main' and any(hint in classes for hint in CONTENT_CLASS_HINTS):
        return True
    if any(hint in classes for hint in CONTENT_CLASS_HINTS):
        return True
    return bool({'markdown', 'readme', 'typeset', 'document', 'article'} & tokens)


def is_noise_container(tag: str, attr_map: dict[str, str], tokens: set[str]) -> bool:
    if tag in {'nav', 'header', 'footer', 'aside'}:
        return True
    classes = attr_map.get('class', '').lower()
    if any(hint in classes for hint in NOISE_CLASS_HINTS):
        return True
    return bool({'nav', 'sidebar', 'menu', 'breadcrumb', 'pagination', 'toc', 'search'} & tokens)


class DocHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self._skip_depth = 0
        self._in_title = False
        self._code_depth = 0
        self._pre_depth = 0
        self._pre_buffer: list[str] = []
        self._table_depth = 0
        self._table_rows: list[list[str]] = []
        self._table_row_has_header: list[bool] = []
        self._current_row: list[str] | None = None
        self._current_row_has_header = False
        self._current_cell_parts: list[str] | None = None
        self._content_depth = 0
        self._noise_depth = 0
        self._stack: list[tuple[str, bool, bool]] = []
        self._has_content_region = False
        self.title_parts: list[str] = []
        self._all_text_parts: list[str] = []
        self._focused_text_parts: list[str] = []
        self._all_links: list[str] = []
        self._all_link_seen: set[str] = set()

    def _record_link(self, href: str) -> None:
        if href in self._all_link_seen:
            return
        self._all_link_seen.add(href)
        self._all_links.append(href)

    def _append_text_piece(self, value: str) -> None:
        self._all_text_parts.append(value)
        if self._content_depth > 0 and self._noise_depth == 0:
            self._focused_text_parts.append(value)

    def _append_piece(self, value: str) -> None:
        if self._table_depth > 0 and self._current_cell_parts is not None:
            self._current_cell_parts.append(value)
            return
        self._append_text_piece(value)

    def _push_block_newline(self) -> None:
        self._append_text_piece('\n')

    @staticmethod
    def _normalize_table_cell(value: str) -> str:
        text = value.replace('\r\n', '\n').replace('\r', '\n')
        text = text.strip()
        text = re.sub(r'[ \t\f\v]+', ' ', text)
        text = re.sub(r'\n+', '<br>', text)
        text = text.replace('|', r'\|')
        return text

    @staticmethod
    def _format_table_row(cells: list[str]) -> str:
        return '| ' + ' | '.join(cells) + ' |'

    def _emit_table_markdown(self) -> None:
        rows = [row for row in self._table_rows if any(cell.strip() for cell in row)]
        if not rows:
            return

        width = max(len(row) for row in rows)
        normalized_rows = []
        for row in rows:
            padded = row + [''] * (width - len(row))
            normalized_rows.append([self._normalize_table_cell(cell) for cell in padded])

        header_idx = 0
        for idx, flag in enumerate(self._table_row_has_header):
            if idx < len(normalized_rows) and flag:
                header_idx = idx
                break

        header = normalized_rows[header_idx]
        data_rows = [row for idx, row in enumerate(normalized_rows) if idx != header_idx]
        separator = ['---'] * width

        lines = [self._format_table_row(header), self._format_table_row(separator)]
        lines.extend(self._format_table_row(row) for row in data_rows)
        self._append_text_piece('\n' + '\n'.join(lines) + '\n')

    def _close_open_tag(self, tag: str) -> None:
        while self._stack:
            popped_tag, is_content, is_noise = self._stack.pop()
            if is_content:
                self._content_depth = max(0, self._content_depth - 1)
            if is_noise:
                self._noise_depth = max(0, self._noise_depth - 1)
            if popped_tag == tag:
                break

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in SKIP_TAGS:
            self._skip_depth += 1
            return
        if self._skip_depth > 0:
            return

        if tag == 'title':
            self._in_title = True

        attr_map = {key: (value or '') for key, value in attrs}
        tokens = attrs_to_tokens(attr_map)
        is_content = is_content_container(tag, attr_map, tokens)
        is_noise = is_noise_container(tag, attr_map, tokens)

        if tag == 'pre':
            self._pre_depth += 1
            if self._pre_depth == 1:
                self._pre_buffer = []
        elif tag == 'code':
            self._code_depth += 1
            if self._pre_depth == 0:
                self._append_piece('`')
        elif tag == 'table':
            self._table_depth += 1
            if self._table_depth == 1:
                self._table_rows = []
                self._table_row_has_header = []
                self._current_row = None
                self._current_row_has_header = False
                self._current_cell_parts = None
        elif tag == 'tr' and self._table_depth > 0:
            self._current_row = []
            self._current_row_has_header = False
        elif tag in {'td', 'th'} and self._table_depth > 0 and self._current_row is not None:
            self._current_cell_parts = []
            if tag == 'th':
                self._current_row_has_header = True

        if tag not in VOID_TAGS:
            if is_content:
                self._content_depth += 1
                self._has_content_region = True
            if is_noise:
                self._noise_depth += 1
            self._stack.append((tag, is_content, is_noise))

        if tag in BLOCK_TAGS and not (self._table_depth > 0 and tag in TABLE_TAGS):
            self._push_block_newline()

        if tag == 'a':
            href = (attr_map.get('href') or '').strip()
            if href:
                self._record_link(href)

    def handle_endtag(self, tag: str) -> None:
        if tag in SKIP_TAGS and self._skip_depth > 0:
            self._skip_depth -= 1
            return
        if self._skip_depth > 0:
            return

        if tag == 'title':
            self._in_title = False
        if tag == 'code' and self._code_depth > 0:
            if self._pre_depth == 0:
                self._append_piece('`')
            self._code_depth -= 1
        elif tag == 'pre' and self._pre_depth > 0:
            self._pre_depth -= 1
            if self._pre_depth == 0:
                code = ''.join(self._pre_buffer).replace('\r\n', '\n').replace('\r', '\n')
                code = code.strip('\n').rstrip()
                if code:
                    self._append_piece(f'\n```text\n{code}\n```\n')
                self._pre_buffer = []
        elif tag in {'td', 'th'} and self._table_depth > 0 and self._current_cell_parts is not None:
            value = ''.join(self._current_cell_parts)
            if self._current_row is not None:
                self._current_row.append(value)
            self._current_cell_parts = None
        elif tag == 'tr' and self._table_depth > 0 and self._current_row is not None:
            self._table_rows.append(self._current_row)
            self._table_row_has_header.append(self._current_row_has_header)
            self._current_row = None
            self._current_row_has_header = False
        elif tag == 'table' and self._table_depth > 0:
            self._table_depth -= 1
            if self._table_depth == 0:
                self._emit_table_markdown()
                self._table_rows = []
                self._table_row_has_header = []
                self._current_row = None
                self._current_cell_parts = None

        self._close_open_tag(tag)

        if tag in BLOCK_TAGS and not (self._table_depth > 0 and tag in TABLE_TAGS):
            self._push_block_newline()

    def handle_data(self, data: str) -> None:
        if self._skip_depth > 0:
            return
        value = unescape(data)
        if self._pre_depth > 0:
            self._pre_buffer.append(value)
            return
        if not value.strip():
            return
        if self._in_title:
            self.title_parts.append(value)
        else:
            self._append_piece(value)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        if tag not in VOID_TAGS:
            self.handle_endtag(tag)

    @property
    def title(self) -> str:
        return clean_text(' '.join(self.title_parts))

    @property
    def text(self) -> str:
        focused = denoise_text(''.join(self._focused_text_parts))
        if self._has_content_region and focused:
            return focused
        return denoise_text(''.join(self._all_text_parts))

    @property
    def links(self) -> list[str]:
        return list(self._all_links)


@dataclass
class CrawlConfig:
    start_urls: list[str]
    output_dir: Path
    allow_domains: set[str]
    include_prefixes: list[str]
    exclude_patterns: list[re.Pattern[str]]
    max_pages: int
    max_depth: int
    min_chars: int
    timeout: float
    max_retries: int
    delay_seconds: float
    keep_query: bool
    user_agent: str
    respect_robots: bool


def post_clean_markdown(path: Path) -> tuple[int, int]:
    text = path.read_text(encoding='utf-8')
    match = re.match(r'^(# .*?\n\nSource: .*?\n\n)(.*)$', text, re.DOTALL)
    if match:
        header = match.group(1)
        body = match.group(2)
    else:
        header = ''
        body = text

    original_lines = [line for line in body.split('\n')]
    cleaned_body = denoise_text(body)
    cleaned_lines = [line for line in cleaned_body.split('\n') if line.strip()]
    removed_lines = max(0, len([l for l in original_lines if l.strip()]) - len(cleaned_lines))
    output = f'{header}{cleaned_body}\n'
    path.write_text(output, encoding='utf-8')
    return removed_lines, len(cleaned_body.split())


def allowed_by_rules(
    url: str,
    allow_domains: set[str],
    include_prefixes: list[str],
    exclude_patterns: list[re.Pattern[str]],
) -> bool:
    domain = domain_from_url(url)
    in_domain = any(domain == item or domain.endswith(f'.{item}') for item in allow_domains)
    if not in_domain:
        return False
    if include_prefixes and not any(url.startswith(prefix) for prefix in include_prefixes):
        return False
    return not any(pattern.search(url) for pattern in exclude_patterns)


def can_fetch_with_robots(
    url: str,
    user_agent: str,
    robots_cache: dict[str, RobotFileParser],
    respect_robots: bool,
) -> bool:
    if not respect_robots:
        return True

    parsed = urlparse(url)
    key = f'{parsed.scheme}://{parsed.netloc}'
    if key not in robots_cache:
        # RobotFileParser.read() uses urllib without any headers, which can get blocked
        # (for example by Read the Docs returning 403). We still want to respect robots.txt,
        # so we fetch it ourselves with the same User-Agent we use for docs pages and then
        # parse the content.
        robots = RobotFileParser()
        robots_url = f'{key}/robots.txt'
        try:
            request = Request(
                robots_url,
                headers={
                    'User-Agent': user_agent,
                    'Accept': 'text/plain,*/*;q=0.1',
                },
            )
            with urlopen(request, timeout=10) as response:
                body = response.read()
                charset = response.headers.get_content_charset() or 'utf-8'
                text = body.decode(charset, errors='replace')
                robots.parse(text.splitlines())
        except Exception:
            # Match previous behavior: if we can't determine robots rules, do not block crawling.
            return True
        robots_cache[key] = robots
    return robots_cache[key].can_fetch(user_agent, url)


def fetch_html(url: str, timeout: float, user_agent: str, max_retries: int) -> tuple[str, str]:
    request = Request(
        url,
        headers={
            'User-Agent': user_agent,
            'Accept': 'text/html,application/xhtml+xml;q=0.9,*/*;q=0.1',
        },
    )
    retries = max(0, max_retries)
    last_error: Exception | None = None
    for attempt in range(retries + 1):
        try:
            with urlopen(request, timeout=timeout) as response:
                content_type = response.headers.get_content_type()
                if content_type not in {'text/html', 'application/xhtml+xml'}:
                    raise ValueError(f'unsupported content type: {content_type}')
                body = response.read()
                charset = response.headers.get_content_charset() or 'utf-8'
                html = body.decode(charset, errors='replace')
                return response.geturl(), html
        except (
            URLError,
            TimeoutError,
            ssl.SSLError,
            http.client.IncompleteRead,
            http.client.HTTPException,
            OSError,
        ) as exc:
            last_error = exc
            if attempt >= retries:
                raise
            time.sleep(min(5.0, 0.8 * (2 ** attempt)))
    assert last_error is not None
    raise last_error


def export_markdown(path: Path, title: str, source_url: str, content: str) -> None:
    text = (
        f'# {title or "Untitled"}\n\n'
        f'Source: {source_url}\n\n'
        f'{content}\n'
    )
    path.write_text(text, encoding='utf-8')


def run_crawl(config: CrawlConfig) -> dict:
    pages_dir = config.output_dir / 'pages'
    pages_dir.mkdir(parents=True, exist_ok=True)

    queue: deque[tuple[str, int]] = deque()
    for raw in config.start_urls:
        normalized = normalize_url(raw, keep_query=config.keep_query)
        if normalized:
            queue.append((normalized, 0))

    visited: set[str] = set()
    results: list[dict] = []
    path_to_result_index: dict[str, int] = {}
    errors: list[dict] = []
    robots_cache: dict[str, RobotFileParser] = {}
    total_removed_lines = 0

    while queue and len(results) < config.max_pages:
        url, depth = queue.popleft()
        if url in visited:
            continue
        visited.add(url)

        if not allowed_by_rules(url, config.allow_domains, config.include_prefixes, config.exclude_patterns):
            continue
        if not can_fetch_with_robots(url, config.user_agent, robots_cache, config.respect_robots):
            continue

        try:
            final_url, html = fetch_html(
                url,
                timeout=config.timeout,
                user_agent=config.user_agent,
                max_retries=config.max_retries,
            )
        except (
            HTTPError,
            URLError,
            TimeoutError,
            ValueError,
            ssl.SSLError,
            http.client.IncompleteRead,
            http.client.HTTPException,
            OSError,
        ) as exc:
            errors.append({'url': url, 'error': str(exc)})
            continue

        parser = DocHTMLParser()
        parser.feed(html)
        parser.close()

        content = parser.text
        title = parser.title or urlparse(final_url).path.strip('/').split('/')[-1] or 'index'
        word_count = len(content.split())

        if word_count >= config.min_chars:
            rel_file_path = safe_slug(final_url)
            file_path = pages_dir / rel_file_path
            file_path.parent.mkdir(parents=True, exist_ok=True)
            export_markdown(file_path, title, final_url, content)
            removed_lines, cleaned_word_count = post_clean_markdown(file_path)
            total_removed_lines += removed_lines
            if cleaned_word_count < config.min_chars:
                file_path.unlink(missing_ok=True)
                continue
            result_item = {
                'url': final_url,
                'title': title,
                'path': f'pages/{rel_file_path.as_posix()}',
                'depth': depth,
                'word_count': cleaned_word_count,
                'removed_noise_lines': removed_lines,
            }
            result_key = result_item['path']
            if result_key in path_to_result_index:
                results[path_to_result_index[result_key]] = result_item
            else:
                path_to_result_index[result_key] = len(results)
                results.append(result_item)

        if depth < config.max_depth:
            for href in parser.links:
                joined = urljoin(final_url, href)
                normalized = normalize_url(joined, keep_query=config.keep_query)
                if not normalized:
                    continue
                if normalized in visited:
                    continue
                if not allowed_by_rules(
                    normalized,
                    config.allow_domains,
                    config.include_prefixes,
                    config.exclude_patterns,
                ):
                    continue
                queue.append((normalized, depth + 1))

        if config.delay_seconds > 0:
            time.sleep(config.delay_seconds)

    output = {
        'generated_at_epoch': int(time.time()),
        'start_urls': config.start_urls,
        'allow_domains': sorted(config.allow_domains),
        'max_pages': config.max_pages,
        'max_depth': config.max_depth,
        'visited_count': len(visited),
        'captured_count': len(results),
        'total_removed_noise_lines': total_removed_lines,
        'pages': results,
        'errors': errors,
    }
    (config.output_dir / 'index.json').write_text(
        json.dumps(output, ensure_ascii=False, indent=2),
        encoding='utf-8',
    )
    return output


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description='Crawl documentation pages into markdown references.')
    parser.add_argument('--start-url', action='append', required=True, help='Seed URL. Repeatable.')
    parser.add_argument('--allow-domain', action='append', default=[], help='Allowed domain. Repeatable.')
    parser.add_argument(
        '--include-prefix',
        action='append',
        default=[],
        help='Only crawl URLs with these prefixes. Repeatable.',
    )
    parser.add_argument(
        '--exclude-regex',
        action='append',
        default=[],
        help='Skip URLs matching this regex. Repeatable.',
    )
    parser.add_argument('--output-dir', required=True, type=Path, help='Output directory.')
    parser.add_argument('--max-pages', type=int, default=120)
    parser.add_argument('--max-depth', type=int, default=3)
    parser.add_argument('--min-chars', type=int, default=40, help='Minimum word count after cleanup.')
    parser.add_argument('--timeout', type=float, default=20.0)
    parser.add_argument('--max-retries', type=int, default=2)
    parser.add_argument('--delay-seconds', type=float, default=0.0)
    parser.add_argument('--keep-query', action='store_true')
    parser.add_argument('--respect-robots', action='store_true')
    parser.add_argument(
        '--user-agent',
        default='CodexDocsSkillCrawler/1.0 (+https://openai.com)',
        help='HTTP User-Agent header.',
    )
    return parser.parse_args()


def normalize_domains(raw_domains: Iterable[str], start_urls: Iterable[str]) -> set[str]:
    domains = {domain.strip().lower() for domain in raw_domains if domain.strip()}
    if domains:
        return domains
    auto = set()
    for url in start_urls:
        normalized = normalize_url(url)
        if normalized:
            auto.add(domain_from_url(normalized))
    return auto


def main() -> int:
    args = parse_args()
    allow_domains = normalize_domains(args.allow_domain, args.start_url)
    if not allow_domains:
        print('No valid domains were found from --allow-domain or --start-url')
        return 1

    compiled_excludes = [re.compile(pattern) for pattern in args.exclude_regex]
    config = CrawlConfig(
        start_urls=args.start_url,
        output_dir=args.output_dir,
        allow_domains=allow_domains,
        include_prefixes=args.include_prefix,
        exclude_patterns=compiled_excludes,
        max_pages=max(1, args.max_pages),
        max_depth=max(0, args.max_depth),
        min_chars=max(0, args.min_chars),
        timeout=max(1.0, args.timeout),
        max_retries=max(0, args.max_retries),
        delay_seconds=max(0.0, args.delay_seconds),
        keep_query=args.keep_query,
        user_agent=args.user_agent,
        respect_robots=args.respect_robots,
    )

    result = run_crawl(config)
    print(
        f'Crawl complete: captured {result["captured_count"]} pages, '
        f'visited {result["visited_count"]} URLs, errors {len(result["errors"])}'
    )
    print(f'Output: {args.output_dir}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
