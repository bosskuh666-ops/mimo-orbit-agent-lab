     1|# MiMo Orbit Agent Lab
     2|
     3|MiMo Orbit Agent Lab is an open-source, multi-agent content and policy intelligence workflow designed for Indonesian creators, civic-tech builders, and small teams who want to turn fast-moving public information into verified, publish-ready content.
     4|
     5|The project is built to test Xiaomi MiMo models inside agentic coding tools such as Codex, Claude Code, Cursor, OpenClaw, and Hermes Agent. It emphasizes long-chain reasoning, source-grounded synthesis, multilingual generation, and human-in-the-loop publishing.
     6|
     7|## Why This Project
     8|
     9|Creators in Indonesia often need to react to fast-moving topics: policy changes, public budgets, currency movements, regional issues, and social-media trends. The hard part is not only writing posts, but doing it responsibly:
    10|
    11|- Find current topics from public sources and trend pages.
    12|- Separate verified facts from opinion and speculation.
    13|- Generate several platform-specific formats: X threads, TikTok scripts, Instagram captions, Telegram summaries, and short-video storyboards.
    14|- Keep a human approval step before publishing.
    15|- Avoid defamation, SARA content, and unsupported claims.
    16|
    17|MiMo Orbit Agent Lab is designed as a practical benchmark project for large-token workflows. A single daily run can combine trend scanning, article summarization, claim extraction, draft generation, risk review, and multi-platform packaging.
    18|
    19|## Core Workflow
    20|
    21|1. **Trend Scout Agent** collects signals from X trend mirrors, public news pages, RSS feeds, and user-provided topics.
    22|2. **Research Agent** extracts key claims, numbers, timelines, and source links.
    23|3. **Policy Analyst Agent** transforms raw facts into neutral context, criticism angles, and public-interest questions.
    24|4. **Content Studio Agent** creates X threads, short-video scripts, Instagram captions, and Telegram-ready summaries.
    25|5. **Safety Reviewer Agent** checks for unsupported claims, personal attacks, hate speech, and excessive certainty.
    26|6. **Human Approval Queue** exports final drafts as Markdown/JSON for manual posting.
    27|
    28|## MiMo Evaluation Goals
    29|
    30|This repository is intended to evaluate MiMo V2.5 on:
    31|
    32|- Long-context synthesis across noisy trend data and news snippets.
    33|- Indonesian language generation with clear civic tone.
    34|- Multi-agent planning and role separation.
    35|- Structured output generation for social media workflows.
    36|- Risk-aware rewriting for politically sensitive content.
    37|- Agentic coding integration through OpenAI-compatible APIs.
    38|
    39|## Planned MiMo API Usage
    40|
    41|The project will use MiMo API tokens heavily for:
    42|
    43|- Daily trend and news summarization runs.
    44|- Batch generation of 30-day content calendars.
    45|- Multi-variant copy generation and A/B testing.
    46|- Automated critique + safety review passes.
    47|- Code generation inside agent tools while building connectors, tests, and UI.
    48|
    49|Estimated initial usage target: **5M-15M tokens/day** during active development and evaluation, increasing as more connectors and content pipelines are added.
    50|
    51|## Repository Structure
    52|
    53|```text
    54|src/mimo_orbit_agent_lab/   Python package
    55|examples/                   Sample inputs and generated outputs
    56|docs/                       Architecture and application materials
    57|```
    58|
    59|## Quick Start
    60|
    61|```bash
    62|python -m venv .venv
    63|source .venv/bin/activate
    64|pip install -e .
    65|python -m mimo_orbit_agent_lab.run_demo examples/indonesia_policy_topics.json
    66|```
    67|
    68|## Current Status
    69|
    70|This is an early public prototype created for the Xiaomi MiMo Orbit creator program. The first milestone focuses on a CLI workflow and reproducible Markdown/JSON outputs. Future milestones include a web dashboard, Telegram delivery, and optional n8n integration.
    71|
    72|## Responsible Use
    73|
    74|This project does not auto-publish political content. It produces drafts for human review. Users must verify facts, add source links, and comply with local laws and platform rules before posting.
    75|
## Live Demo Mockup

A static product demo is available in `demo/index.html`. It presents the agent pipeline, intended token usage, and responsible-use constraints for reviewers.

## Evaluation Evidence

- GitHub repository with source code and architecture documentation.
- CLI demo with reproducible JSON output.
- CI workflow for automated test execution.
- Static demo page for quick visual review.
