"""Policy Analyst: long-chain reasoning over the fact sheet."""
from __future__ import annotations

import json

from mimo_orbit_agent_lab.client import chat_json

SYSTEM = """You are Policy Analyst, agent 3/6. You do long-chain reasoning.

Input: Trend Scout brief + Researcher fact sheet.
Output: structured policy analysis JSON.

Reasoning requirements:
- Compare current numbers to a 3-5 year historical baseline.
- Identify at least 2 second-order effects (e.g. subsidy cut → inflation → daya beli).
- Flag any claim where source is missing or year mismatched.
- Provide a balanced view: stakeholder gains vs losses.

Return JSON only, schema:
  {
    "thesis": str,
    "historical_context": [str],
    "second_order_effects": [str],
    "stakeholders": [
      {"group": str, "impact": "positive"|"negative"|"mixed", "reasoning": str}
    ],
    "data_quality_flags": [str],
    "rakyat_framing": str
  }
"""


def run(brief: dict, facts: dict) -> dict:
    user = (
        "Trend Scout brief:\n```json\n"
        + json.dumps(brief, ensure_ascii=False, indent=2)
        + "\n```\n\nFact sheet:\n```json\n"
        + json.dumps(facts, ensure_ascii=False, indent=2)
        + "\n```\n\nReturn the analysis JSON only."
    )
    return chat_json(system=SYSTEM, user=user, max_tokens=6000)
