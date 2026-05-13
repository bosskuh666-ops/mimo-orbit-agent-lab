# Xiaomi MiMo Orbit Application Draft

Email: use the same email registered on Xiaomi MiMo Open Platform and GitHub.

AI tools: Codex, Claude Code, Cursor, Hermes Agent, OpenClaw.

Model families: GPT series, Claude series, MiMo series, DeepSeek series.

Project URL: paste the GitHub repository URL after publishing.

## Project Description

I am building MiMo Orbit Agent Lab, an open-source multi-agent workflow for Indonesian civic content and policy intelligence. The project helps creators and small teams transform fast-moving public information into verified, publish-ready drafts for X/Twitter, Instagram, TikTok, Telegram, and YouTube Shorts. It is designed for human-in-the-loop publishing and responsible political content creation.

The core pain point is that Indonesian creators need to respond quickly to public policy issues, economic news, and trending topics, but doing this manually is slow and risky. They must gather sources, extract key claims and numbers, write platform-specific content, and avoid unsupported allegations or harmful language. MiMo Orbit Agent Lab solves this with a long-chain AI workflow: Trend Scout Agent collects trending topics and public signals; Research Agent summarizes sources and extracts claims; Policy Analyst Agent turns facts into civic context and public-interest questions; Content Studio Agent generates X threads, short-video scripts, Instagram captions, and Telegram summaries; Safety Reviewer Agent checks for unsupported claims, personal attacks, SARA content, and excessive certainty before anything is posted manually.

I currently use Codex, Hermes Agent, Claude Code, and Cursor to build and operate this workflow. The project is a strong fit for Xiaomi MiMo because it requires high-volume reasoning and generation in Indonesian, structured JSON/Markdown outputs, repeated safety-review passes, and agentic coding support through OpenAI-compatible APIs. During active development I expect to use MiMo for daily trend research, batch content calendar generation, multilingual rewriting, safety evaluation, test generation, and code implementation. Initial usage is estimated at 5M-15M tokens per day, with higher usage when generating 30-day content calendars and running multi-agent evaluation batches.

Evidence and impact: I will publish the project on GitHub with architecture docs, demo input/output, responsible-use guidelines, and a roadmap for Telegram/n8n integration. The project targets Indonesian creators, civic-tech builders, and small media teams who need a safer workflow for AI-assisted public-interest content.
