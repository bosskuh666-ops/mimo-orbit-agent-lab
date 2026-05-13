import json
import subprocess
import sys
from pathlib import Path


def test_run_demo_outputs_threads():
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, "-m", "mimo_orbit_agent_lab.run_demo", "examples/indonesia_policy_topics.json"],
        cwd=root,
        env={"PYTHONPATH": "src"},
        text=True,
        capture_output=True,
        check=True,
    )
    payload = json.loads(result.stdout)
    assert payload["workflow"].startswith("trend_scout")
    assert len(payload["threads"]) == 3
    assert "safety_notes" in payload["threads"][0]
