"""CLI entry point for the lab."""
from __future__ import annotations

import json
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel

from mimo_orbit_agent_lab.agents import (
    content_studio,
    policy_analyst,
    researcher,
    safety_reviewer,
    trend_scout,
)

app = typer.Typer(add_completion=False, help="MiMo Orbit Agent Lab")
console = Console()

OUT = Path("examples/outputs")


def _save(name: str, data: dict) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / name
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2))
    return path


@app.command()
def run(topic: str = typer.Option(..., help="Topic seed, e.g. 'subsidi BBM 2026'")) -> None:
    """Run the full 6-stage pipeline."""
    console.print(Panel.fit(f"[bold cyan]MiMo Orbit Agent Lab[/]\nTopic: {topic}"))

    console.print("[1/6] Trend Scout")
    brief = trend_scout.run(topic)
    _save("01_trend.json", brief)

    console.print("[2/6] Researcher")
    facts = researcher.run(brief)
    _save("02_facts.json", facts)

    console.print("[3/6] Policy Analyst")
    analysis = policy_analyst.run(brief, facts)
    _save("03_analysis.json", analysis)

    console.print("[4/6] Content Studio")
    drafts = content_studio.run(brief, facts, analysis)
    _save("04_drafts.json", drafts)

    console.print("[5/6] Safety Reviewer")
    safety = safety_reviewer.run(drafts, facts)
    _save("05_safety.json", safety)

    console.print(
        Panel.fit(
            f"[bold]Safety verdict:[/] {safety.get('verdict', '?')}\n"
            "[6/6] Awaiting human approval — review examples/outputs/04_drafts.json",
            border_style="green" if safety.get("verdict") == "pass" else "yellow",
        )
    )


if __name__ == "__main__":
    app()
