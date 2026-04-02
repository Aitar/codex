---
name: tensorrt-llm-docs-1-3-0rc7
description: Reference skill generated from official TensorRT-LLM 1.3.0rc7 documentation. Use when answering TensorRT-LLM 1.3.0rc7 APIs, configs, constraints, version behavior, or integration details.
---

# TensorRT-LLM Docs 1.3.0rc7

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
