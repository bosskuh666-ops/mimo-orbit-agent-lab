import json
import sys
from pathlib import Path


def build_thread(topic):
    return {
        "topic": topic["topic"],
        "draft": [
            f"Public-interest question: what does {topic['topic']} mean for ordinary citizens?",
            f"Signal to verify: {topic['signal']}.",
            f"Suggested angle: {topic['angle']}.",
            "Before posting, add at least two source links and avoid claims about named individuals unless verified."
        ],
        "safety_notes": [
            "Keep criticism focused on policy and public data.",
            "Avoid hate speech, SARA content, and unsupported allegations.",
            "Use cautious language when numbers are still developing."
        ]
    }


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python -m mimo_orbit_agent_lab.run_demo examples/indonesia_policy_topics.json")
    data = json.loads(Path(sys.argv[1]).read_text())
    output = {
        "date": data.get("date"),
        "workflow": "trend_scout -> research -> policy_analyst -> content_studio -> safety_review",
        "threads": [build_thread(topic) for topic in data.get("topics", [])]
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
