---
name: official-docs-skill-builder
description: Build or update a Codex skill from official documentation websites. Use when the task is to crawl official docs, extract stable technical content, organize references, and generate skill files (SKILL.md plus agents metadata) for a specific product or API.
---

# Official Docs Skill Builder

## Overview

Turn official documentation pages into a reusable Codex skill package.
Use the bundled scripts to crawl docs pages, clean content, generate references, and scaffold the target skill.

## Workflow

1. Confirm scope before crawling.
2. Crawl and extract official docs content into Markdown pages.
3. Re-read each page and remove navigation/boilerplate noise.
4. Generate the target skill from crawled content.
5. Validate structure and metadata.

## Step 1: Confirm Scope

Collect:
- Target topic name (example: "TradingView Charting Library v29")
- Seed URLs (official docs landing page and key subsections)
- Crawl limits (`max_pages`, `max_depth`)
- Allowed domains and optional include path prefixes

Prefer narrow scope first. Expand later if coverage is missing.

## Step 2: Crawl Official Docs

Run:

```bash
scripts/crawl_docs.py \
  --start-url https://example.com/docs \
  --allow-domain example.com \
  --include-prefix https://example.com/docs \
  --output-dir /tmp/docs-crawl \
  --max-pages 120 \
  --max-depth 3 \
  --max-retries 2 \
  --respect-robots
```

Crawler outputs:
- `index.json`: crawl manifest and page metadata
- `pages/**/*.md`: cleaned per-page markdown files, stored by docs hierarchy

The crawler now applies two cleanup layers automatically:
- Extract only probable main content regions (`main/article/content` containers).
- Re-read generated markdown pages and remove navigation/TOC/header/footer noise lines.

When using `build_skill_from_docs.py`, scope is automatically expanded by version:
- Example: start URL `.../en/v0.15.0/usage/` auto-adds `.../en/v0.15.0/` to include prefixes.
- This allows sibling sections like `features/` and `training/` to be crawled in the same run.
- Use `--no-auto-scope-by-version` only when you intentionally want a narrow subtree.

Naming and output conventions:
- If `--skill-name` is omitted, derive it from URL as `{project}-{version}`.
- Example: `https://docs.vllm.ai/en/v0.15.0/usage/` -> `vllm-0-15-0`.
- Markdown files are saved by section path under `references/pages/`.
- Example: `.../en/v0.15.0/deployment/frameworks/anything-llm/` ->
  `references/pages/deployment/frameworks/anything-llm.md`.

## Step 3: Curate References

Read `references/curation-checklist.md`.
Keep only high-signal pages:
- API definitions and constraints
- Configuration and flags
- Error behavior and edge cases
- Version-specific notes

Drop:
- Marketing pages
- Blog/news pages
- Duplicate nav-heavy pages

Run a code-fidelity pass on sampled pages:
- Keep inline code in sentence flow (example: `` `float32` ``).
- Keep multi-line examples as fenced code blocks (`` ```text ... ``` ``).
- Keep HTML tables as Markdown tables with header separator row (`| --- |`).
- If code formatting is broken, re-crawl with narrower prefixes and re-check.

## Step 4: Build Target Skill

Run:

```bash
scripts/build_skill_from_docs.py \
  --skill-name tv-docs-v29 \
  --topic "TradingView Charting Library v29" \
  --skills-root /Users/tal/projects/trade-practice/.codex/skills \
  --start-url https://www.tradingview.com/charting-library-docs/latest \
  --allow-domain tradingview.com \
  --include-prefix https://www.tradingview.com/charting-library-docs \
  --max-pages 140 \
  --max-depth 3 \
  --respect-robots
```

Generator creates:
- `<skill>/SKILL.md`
- `<skill>/agents/openai.yaml`
- `<skill>/references/docs-index.md`
- `<skill>/references/pages/*.md`

## Step 5: Validate

Run:

```bash
python /Users/tal/.codex/skills/.system/skill-creator/scripts/quick_validate.py \
  /Users/tal/projects/trade-practice/.codex/skills/tv-docs-v29
```

If validation fails, fix frontmatter name/description first.

## Quality Gates

- Keep references focused on official sources only.
- Keep `SKILL.md` procedural and concise.
- Keep reference files grouped by topic when page count is high.
- Keep trigger description explicit in frontmatter so the skill activates correctly.
- Keep inline code and code blocks readable after extraction.
- Keep table structure readable after extraction (header + rows).
- Re-run crawl when docs version changes.

## Resources

- `scripts/crawl_docs.py`: crawl and extract docs pages.
- `scripts/build_skill_from_docs.py`: assemble a skill from docs crawl output.
- `references/curation-checklist.md`: manual cleanup checklist before finalizing the generated skill.
