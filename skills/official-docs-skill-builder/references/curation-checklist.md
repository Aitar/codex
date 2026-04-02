# Docs Curation Checklist

Use this checklist after crawling and before shipping the generated skill.
The crawler already performs automatic navigation/boilerplate cleanup; use this checklist for final manual review.

## 1. Verify Source Quality

- Keep pages only from official docs domains.
- Remove marketing, blog, changelog news, and landing pages with little technical content.
- Keep versioned pages when version behavior matters.

## 2. Remove Noise

- Drop pages dominated by navigation text.
- Drop duplicate pages with the same core API content.
- Merge near-duplicate pages by preserving the more complete one.

## 3. Improve Retrieval Quality

- Keep file names stable and descriptive.
- Group by topic when page count is high (`references/pages/api-*`, `references/pages/config-*` style).
- Ensure `references/docs-index.md` maps title to source URL and local file.
- Confirm code fidelity:
  - inline code stays inline with backticks
  - multi-line snippets remain fenced code blocks with preserved newlines
- Confirm table fidelity:
  - HTML tables are converted to Markdown tables
  - header separator row (`| --- |`) is present

## 4. Harden Skill Triggering

- Write frontmatter `description` with clear trigger phrases:
  - API usage
  - configuration
  - limits and constraints
  - version-specific behavior
- Keep scope explicit so Codex does not over-trigger.

## 5. Final Validation

- Run `quick_validate.py` on the generated skill.
- Manually test at least 3 prompts:
  - one API behavior question
  - one configuration question
  - one edge-case/constraint question
- If answers miss key details, crawl more pages and rebuild.
