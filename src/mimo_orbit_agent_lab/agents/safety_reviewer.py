"""Safety Reviewer: SARA / defamation / source-integrity scan."""
from __future__ import annotations

import json
import os

from mimo_orbit_agent_lab.client import chat_json

SYSTEM = """You are Safety Reviewer, agent 5/6. Strict policy auditor.

Input: drafts JSON + fact sheet.
Output: a safety report JSON.

Checks:
- SARA: any line targeting ras, agama, suku, antargolongan?
- Defamation: any unverified accusation against a named person?
- Source integrity: every number must trace to a citation in the fact sheet.
- Platform compliance: Twitter/IG/TikTok/YT community rules.

Return JSON only, schema:
  {
    "verdict": "pass"|"revise"|"block",
    "issues": [
      {"platform": str, "location": str, "rule": str, "severity": "low"|"med"|"high", "suggested_fix": str}
    ],
    "summary": str
  }
"""


def run(drafts: dict, facts: dict) -> dict:
    user = (
        "Drafts:\n```json\n"
        + json.dumps(drafts, ensure_ascii=False, indent=2)
        + "\n```\n\nFacts:\n```json\n"
        + json.dumps(facts, ensure_ascii=False, indent=2)
        + "\n```\n\nReturn the safety report JSON only."
    )
    return chat_json(
        system=SYSTEM,
        user=user,
        model=os.environ.get("MIMO_MODEL_FAST", "mimo-v2-pro"),
        max_tokens=3000,
    )
