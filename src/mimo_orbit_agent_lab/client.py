"""Thin wrapper around the OpenAI-compatible MiMo client."""
from __future__ import annotations

import json
import os
from typing import Any

try:
    from dotenv import load_dotenv  # type: ignore
    load_dotenv()
except Exception:
    pass

try:
    from openai import OpenAI  # type: ignore
except Exception:  # pragma: no cover - import guard for offline test envs
    OpenAI = None  # type: ignore


def get_client() -> Any:
    if OpenAI is None:
        raise RuntimeError(
            "openai package not installed. Run: pip install -r requirements.txt"
        )
    return OpenAI(
        api_key=os.environ.get("MIMO_API_KEY", "tp-demo"),
        base_url=os.environ.get(
            "MIMO_BASE_URL", "https://token-plan-sgp.xiaomimimo.com/v1"
        ),
    )


def chat_json(
    *,
    system: str,
    user: str,
    model: str | None = None,
    temperature: float = 0.3,
    max_tokens: int = 4096,
) -> dict[str, Any]:
    """Call MiMo chat completion and parse the response as JSON."""
    client = get_client()
    model = model or os.environ.get("MIMO_MODEL_REASON", "mimo-v2.5-pro")
    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": user},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        response_format={"type": "json_object"},
    )
    text = resp.choices[0].message.content or "{}"
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        text = text.strip().strip("`")
        if text.startswith("json"):
            text = text[4:]
        return json.loads(text)
