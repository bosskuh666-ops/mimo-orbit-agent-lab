"""Researcher: extract structured facts and citations from the angle."""
from __future__ import annotations

import json

from mimo_orbit_agent_lab.client import chat_json

SYSTEM = """You are Researcher, agent 2/6.

Input: a Trend Scout JSON brief.
Output: a fact sheet (JSON) with claims, numbers, dates, entities, and required citations.

Rules:
- Every numeric claim MUST have a `source` field naming the agency (BPS, Kemenkeu, BI, DPR, Bappenas, etc).
- Mark claims as "verified" only if the agency + year is explicit; otherwise "needs_verification".
- Identify at least 3 entities (persons / institutions) and 3 dates.
- Return JSON only, schema:
  {
    "claims": [
      {"text": str, "source": str, "status": "verified"|"needs_verification", "year": int|null}
    ],
    "entities": [{"name": str, "role": str}],
    "key_dates": [{"date": "YYYY-MM-DD"|"YYYY", "event": str}],
    "open_questions": [str]
  }
"""


def run(brief: dict) -> dict:
    return chat_json(
        system=SYSTEM,
        user=f"Trend Scout brief:\n```json\n{json.dumps(brief, ensure_ascii=False, indent=2)}\n```\n\nReturn the fact sheet JSON only.",
    )
