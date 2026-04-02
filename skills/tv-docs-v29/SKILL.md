---
name: tv-docs-v29
description: TradingView Advanced Charts/Charting Library v29 documentation. Use when answering questions about Charting Library APIs, datafeeds (UDF), customization, features, limitations, or integration details based on TradingView_Docs_v29.
---

# TV Docs v29

## Overview
- Use the bundled docs in `references/TradingView_Docs_v29` as the source of truth for Advanced Charts/Charting Library v29.
- Prefer exact wording and parameter details from the docs.

## Quick start
1. Find the relevant section with `rg -n "<keyword>" references/TradingView_Docs_v29`.
2. Open the most specific file (e.g. Core Concepts, Customization, Connecting Data, Trading Platform, Tutorials).
3. Cite the file path in reasoning and follow the docs even if prior knowledge differs.

## Navigation
- Start with `Overview.md` for scope and terminology.
- For datafeeds and UDF adapter, search under `Connecting Data/` and `Core Concepts/`.
- For UI/appearance and feature flags, search under `Customization/`.
- For version changes, use `Releases/`.

## Working rules
- Prefer the most specific or newest doc when multiple files differ.
- Ask for the user's Charting Library version if behavior is unclear.
- Avoid guessing; quote or paraphrase the doc section and align code to it.
