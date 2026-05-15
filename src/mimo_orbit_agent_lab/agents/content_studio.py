"""Content Studio: generate platform-aware drafts in Bahasa Indonesia."""
from __future__ import annotations

import json

from mimo_orbit_agent_lab.client import chat_json

SYSTEM = """You are Content Studio, agent 4/6.

Input: full upstream context (brief + facts + analysis).
Output: drafts for 4 platforms, in Bahasa Indonesia (lowercase casual style for X/TikTok, formal for YT).

Rules:
- X thread: 5-8 tweets, each <=280 chars. First tweet is the hook.
- IG carousel: 6 slides, each <=180 chars.
- TikTok hook: first 3 seconds (one sentence) + 30s script outline.
- YT Shorts: 60-second script with cue marks.
- Every numeric claim must include "(sumber: X, YYYY)" inline.
- No SARA, no targeting, no defamation.
- Return JSON only, schema:
  {
    "x_thread": [str],
    "ig_carousel": [{"slide": int, "text": str}],
    "tiktok": {"hook": str, "script": str},
    "yt_shorts": {"hook": str, "script": str, "cues": [str]}
  }
"""


def run(brief: dict, facts: dict, analysis: dict) -> dict:
    user = (
        "Brief:\n```json\n"
        + json.dumps(brief, ensure_ascii=False, indent=2)
        + "\n```\n\nFacts:\n```json\n"
        + json.dumps(facts, ensure_ascii=False, indent=2)
        + "\n```\n\nAnalysis:\n```json\n"
        + json.dumps(analysis, ensure_ascii=False, indent=2)
        + "\n```\n\nReturn the drafts JSON only."
    )
    return chat_json(system=SYSTEM, user=user, max_tokens=8000)
