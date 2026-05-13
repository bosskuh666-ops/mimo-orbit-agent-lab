# MiMo Orbit Agent Lab

MiMo Orbit Agent Lab is an open-source, multi-agent content and policy intelligence workflow designed for Indonesian creators, civic-tech builders, and small teams who want to turn fast-moving public information into verified, publish-ready content.

The project is built to test Xiaomi MiMo models inside agentic coding tools such as Codex, Claude Code, Cursor, OpenClaw, and Hermes Agent. It emphasizes long-chain reasoning, source-grounded synthesis, multilingual generation, and human-in-the-loop publishing.

## Why This Project

Creators in Indonesia often need to react to fast-moving topics: policy changes, public budgets, currency movements, regional issues, and social-media trends. The hard part is not only writing posts, but doing it responsibly:

- Find current topics from public sources and trend pages.
- Separate verified facts from opinion and speculation.
- Generate several platform-specific formats: X threads, TikTok scripts, Instagram captions, Telegram summaries, and short-video storyboards.
- Keep a human approval step before publishing.
- Avoid defamation, SARA content, and unsupported claims.

MiMo Orbit Agent Lab is designed as a practical benchmark project for large-token workflows. A single daily run can combine trend scanning, article summarization, claim extraction, draft generation, risk review, and multi-platform packaging.

## Core Workflow

1. **Trend Scout Agent** collects signals from X trend mirrors, public news pages, RSS feeds, and user-provided topics.
2. **Research Agent** extracts key claims, numbers, timelines, and source links.
3. **Policy Analyst Agent** transforms raw facts into neutral context, criticism angles, and public-interest questions.
4. **Content Studio Agent** creates X threads, short-video scripts, Instagram captions, and Telegram-ready summaries.
5. **Safety Reviewer Agent** checks for unsupported claims, personal attacks, hate speech, and excessive certainty.
6. **Human Approval Queue** exports final drafts as Markdown/JSON for manual posting.

## MiMo Evaluation Goals

This repository is intended to evaluate MiMo V2.5 on:

- Long-context synthesis across noisy trend data and news snippets.
- Indonesian language generation with clear civic tone.
- Multi-agent planning and role separation.
- Structured output generation for social media workflows.
- Risk-aware rewriting for politically sensitive content.
- Agentic coding integration through OpenAI-compatible APIs.

## Planned MiMo API Usage

The project will use MiMo API tokens heavily for:

- Daily trend and news summarization runs.
- Batch generation of 30-day content calendars.
- Multi-variant copy generation and A/B testing.
- Automated critique + safety review passes.
- Code generation inside agent tools while building connectors, tests, and UI.

Estimated initial usage target: **5M-15M tokens/day** during active development and evaluation, increasing as more connectors and content pipelines are added.

## Repository Structure

```text
src/mimo_orbit_agent_lab/   Python package
examples/                   Sample inputs and generated outputs
docs/                       Architecture and application materials
```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m mimo_orbit_agent_lab.run_demo examples/indonesia_policy_topics.json
```

## Current Status

This is an early public prototype created for the Xiaomi MiMo Orbit creator program. The first milestone focuses on a CLI workflow and reproducible Markdown/JSON outputs. Future milestones include a web dashboard, Telegram delivery, and optional n8n integration.

## Responsible Use

This project does not auto-publish political content. It produces drafts for human review. Users must verify facts, add source links, and comply with local laws and platform rules before posting.
