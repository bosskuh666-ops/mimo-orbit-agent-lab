# Architecture

## Goals

- Make AI-assisted civic content creation **auditable**, **multi-platform**, and **safe**.
- Treat each agent as a pure function: `(JSON_in) -> JSON_out`. Replayable. Testable. Cacheable.
- Use **MiMo v2.5-pro** for long-chain reasoning stages (analysis), **mimo-v2-pro** for fast guardrail checks.

## Pipeline

```
                ┌─────────────┐
                │ Topic seed  │  e.g. "subsidi BBM 2026"
                └──────┬──────┘
                       ▼
        ┌──────────────────────────┐
        │  1. Trend Scout          │  pick concrete angle
        │  (mimo-v2.5-pro)         │  → 01_trend.json
        └──────────┬───────────────┘
                   ▼
        ┌──────────────────────────┐
        │  2. Researcher           │  extract claims + sources
        │  (mimo-v2.5-pro)         │  → 02_facts.json
        └──────────┬───────────────┘
                   ▼
        ┌──────────────────────────┐
        │  3. Policy Analyst       │  long-chain reasoning
        │  (mimo-v2.5-pro, 8-12k)  │  → 03_analysis.json
        └──────────┬───────────────┘
                   ▼
        ┌──────────────────────────┐
        │  4. Content Studio       │  X / IG / TT / YT drafts
        │  (mimo-v2.5-pro)         │  → 04_drafts.json
        └──────────┬───────────────┘
                   ▼
        ┌──────────────────────────┐
        │  5. Safety Reviewer      │  SARA / defamation / source
        │  (mimo-v2-pro)           │  → 05_safety.json
        └──────────┬───────────────┘
                   ▼
        ┌──────────────────────────┐
        │  6. Human Approval       │  creator decides
        └──────────────────────────┘
```

## Why MiMo

| Requirement | Why MiMo fits |
|-------------|----------------|
| Long-chain reasoning over 8-12k context | mimo-v2.5-pro handles long Bahasa Indonesia + English mixed inputs |
| Strict structured output | `response_format={"type": "json_object"}` works out-of-the-box |
| OpenAI-compatible | drop-in `OpenAI(base_url="https://token-plan-sgp.xiaomimimo.com/v1")` |
| Bahasa Indonesia fluency | strong Indonesian generation across casual + formal registers |
| Cost-effective at scale | sustained ~25M tokens/month per active creator |

## Failure modes & guards

| Failure | Guard |
|---------|-------|
| Model emits non-JSON | `chat_json` repair pass strips fences and retries parse |
| Hallucinated numbers | Researcher tags `needs_verification` if source missing; Safety Reviewer blocks export |
| SARA / defamation | dedicated agent with "block" verdict halts pipeline before drafts ship |
| Stale facts | Each artifact stores `created_at`; CLI refuses to publish artifacts older than 24h |
| Token blowup | per-stage `max_tokens` cap; observed p95 ~8k for analysis stage |

## Token budget per run

| Stage | Input | Output | Total |
|-------|-------|--------|-------|
| Trend Scout | 200 | 600 | 800 |
| Researcher | 800 | 2,000 | 2,800 |
| Policy Analyst | 3,000 | 5,000 | 8,000 |
| Content Studio | 6,000 | 6,000 | 12,000 |
| Safety Reviewer | 5,000 | 1,500 | 6,500 |
| **Total** | | | **~30k** |

Counting evaluation, regression tests, and rerun-on-revise: budget ~80k tokens per topic, ~600k per active day.

## Extension points

- Replace Trend Scout with an RSS/Twitter ingestion job (cron + `feedparser`).
- Plug BPS/Kemenkeu API connectors into Researcher for real-time data.
- Swap Safety Reviewer for a fine-tuned classifier as more labeled data arrives.
- Add an Eval Harness stage that scores drafts against gold-labeled fact sheets (BLEU on facts, F1 on SARA flags).
