# Architecture

MiMo Orbit Agent Lab uses a five-agent pipeline: Trend Scout, Research, Policy Analyst, Content Studio, and Safety Reviewer. Each stage produces structured JSON so a human can audit the chain before publishing.

The intended MiMo integration uses OpenAI-compatible API settings in coding agents and workflow runners. MiMo models are evaluated for long-context Indonesian synthesis, policy-sensitive rewriting, and multi-format content generation.
