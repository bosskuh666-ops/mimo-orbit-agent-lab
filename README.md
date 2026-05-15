# MiMo Orbit Agent Lab

[![CI](https://github.com/bosskuh666-ops/mimo-orbit-agent-lab/actions/workflows/ci.yml/badge.svg)](https://github.com/bosskuh666-ops/mimo-orbit-agent-lab/actions/workflows/ci.yml)

A multi-agent content & policy intelligence workflow for Indonesian creators, powered by **Xiaomi MiMo API**.

> Open-source agent lab for high-quality, AI-driven civic content. Long-chain reasoning, multi-agent collaboration, structured output, human-in-the-loop review. Designed to test MiMo v2.5 inside agentic coding tools (Codex, Claude Code, Cursor, OpenClaw, Hermes Agent).

## Why this exists

Indonesian creators who cover policy, economics, and AI/tech (politik fiskal, BBM, subsidi, RUU, makroekonomi) face three real pains:

1. **Source verification is slow.** A single ministerial statement requires cross-checking against BPS data, Kemenkeu releases, and historical context.
2. **Drafting under platform constraints is expensive.** A claim must survive Twitter (280 char), Instagram caption (~2,200 char), TikTok hook (first 3 seconds), and YouTube Shorts script — each with different tone and compliance rules.
3. **Quality control is manual.** Avoiding SARA, hate speech, defamation, and policy-platform violations is non-negotiable for a serious creator.

`mimo-orbit-agent-lab` is a reusable agent pipeline that takes a single news lead and produces verified, multi-format, ready-for-review drafts — never auto-publishing.

## Pipeline (6 agents)

```
Trend Scout  ─►  Researcher  ─►  Policy Analyst  ─►  Content Studio  ─►  Safety Reviewer  ─►  Human Approval
   (RSS)         (claims)        (data + context)     (TW/IG/TT/YT)       (SARA / facts)        (creator)
```

| Agent | Role | Model |
|-------|------|-------|
| Trend Scout | Pulls trending Indonesian news/RSS, picks lead with highest civic relevance | mimo-v2.5-pro |
| Researcher | Extracts claims, entities, dates, numbers; generates a structured fact sheet (JSON) | mimo-v2.5-pro |
| Policy Analyst | Long-chain reasoning over BPS/Kemenkeu/historical context; flags inconsistencies | mimo-v2.5-pro |
| Content Studio | Generates 4 formats (X thread, IG carousel, TikTok hook, YT Shorts script) | mimo-v2.5-pro |
| Safety Reviewer | SARA / hate-speech / defamation scan; cites which lines need rewording | mimo-v2-pro |
| Human Approval | Creator reviews drafts in CLI; nothing publishes without explicit approval | — |

Each agent emits a JSON artifact, so the pipeline is testable, replayable, and auditable.

## Quickstart

```bash
git clone https://github.com/bosskuh666-ops/mimo-orbit-agent-lab.git
cd mimo-orbit-agent-lab
python -m venv .venv && source .venv/bin/activate
pip install -e .
pip install -r requirements.txt
cp .env.example .env   # fill MIMO_API_KEY from https://platform.xiaomimimo.com

# Live pipeline (calls MiMo API)
python -m mimo_orbit_agent_lab.cli run --topic "subsidi BBM 2026"

# Offline demo (no API call, prints sample structure)
python -m mimo_orbit_agent_lab.run_demo examples/indonesia_policy_topics.json
```

Live-pipeline output:

```
[1/6] Trend Scout    → examples/outputs/01_trend.json
[2/6] Researcher     → examples/outputs/02_facts.json
[3/6] Policy Analyst → examples/outputs/03_analysis.json
[4/6] Content Studio → examples/outputs/04_drafts.json
[5/6] Safety Review  → examples/outputs/05_safety.json
[6/6] Awaiting human approval...
```

A pre-generated end-to-end sample (`subsidi BBM 2026`) is committed under `examples/outputs/` for reviewers without an API key.

## MiMo integration

The lab uses the OpenAI-compatible MiMo endpoint:

```python
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["MIMO_API_KEY"],
    base_url="https://token-plan-sgp.xiaomimimo.com/v1",
)
```

Why MiMo for this workload:

- **Long-chain reasoning** — Policy Analyst needs 8-12k tokens of context (article + BPS table + 3 historical references) per call.
- **Structured JSON output** — every stage emits a strict schema; saves a full validation/repair loop.
- **Multilingual** — Indonesian + English mixed sources, Indonesian output.
- **Cost-effective at scale** — daily creator workflow runs 6-12 leads × 6 agents × ~10k context = ~500k tokens/day.

## Token usage estimate

| Workload | Tokens / run | Runs / day | Daily |
|----------|--------------|------------|-------|
| Lead analysis (full pipeline) | ~30k | 8 | 240k |
| Multi-agent eval / regression tests | ~20k | 5 | 100k |
| Long-context policy briefs (week-end) | ~120k | 1 | 120k |
| Agentic coding (Codex/Claude Code/Hermes) on this repo | — | — | ~250k |
| **Total daily (active dev)** | | | **~700k** |

Sustained 30-day usage: **~20-25M tokens**. Bursty: 50M during election / budget cycles.

## Repository structure

```
src/mimo_orbit_agent_lab/
├── __init__.py
├── client.py              # OpenAI-compatible MiMo client
├── cli.py                 # typer entry point
├── run_demo.py            # offline demo (no API key)
└── agents/
    ├── trend_scout.py
    ├── researcher.py
    ├── policy_analyst.py
    ├── content_studio.py
    └── safety_reviewer.py
docs/
├── architecture.md        # pipeline diagram, token budget, failure modes
└── application-answer.md  # MiMo Orbit form draft
examples/
├── indonesia_policy_topics.json   # sample input
└── outputs/                       # pre-generated end-to-end JSON artifacts
demo/index.html             # static product mockup
tests/test_run_demo.py      # CI-runnable smoke test
.github/workflows/ci.yml    # automated test execution
```

## Responsible use

- **No auto-publish.** Drafts are written to disk; only the creator publishes.
- **Source citations required** for every numeric claim.
- **SARA filter is mandatory** — Safety Reviewer blocks the export if any clause triggers it.
- **No targeting individuals** by ethnicity, religion, race, or political affiliation.
- **Compliance with Indonesian platform rules** (UU ITE, Pedoman Komunitas Twitter/IG/TikTok).

## Roadmap

- [x] Core 6-agent pipeline (MVP)
- [x] CLI runner + JSON artifacts
- [x] End-to-end example: subsidi BBM 2026
- [x] CI workflow + offline smoke test
- [x] Static product demo page (`demo/index.html`)
- [ ] Web dashboard for human approval
- [ ] BPS / Kemenkeu API connectors
- [ ] Bahasa-aware tone presets (formal kebijakan / santai meme / akademik)
- [ ] Eval harness against gold-labeled fact sheets

## License

MIT

## Author

Bosskuh — [@Kkkuh_](https://x.com/Kkkuh_) on X. Indonesian creator covering AI, mindset, economics, and policy.
