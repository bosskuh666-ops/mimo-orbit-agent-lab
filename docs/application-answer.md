# Application Answer — Xiaomi MiMo Orbit 100T

## Form fill plan

| Field | Value |
|-------|-------|
| Email | kukuhsyawallukito1@gmail.com |
| AI tools | Codex, Claude Code, Hermes Agent |
| Model families | MiMo, Claude, GPT |
| Project description | use the Chinese version below |
| Proof | screenshots: README, architecture diagram, end-to-end JSON outputs |
| GitHub URL | https://github.com/bosskuh666-ops/mimo-orbit-agent-lab |

---

## 中文项目描述（推荐填入表单，约 1,050 字符）

我正在开发 **MiMo Orbit Agent Lab**，一个面向印尼内容创作者的开源多 Agent 工作流，专注于公共政策、宏观经济和 AI/科技话题的高质量短视频与社交媒体内容生成。项目核心痛点：印尼独立创作者在覆盖政策类内容时面临三个真实问题——信息源核验慢、跨平台改稿成本高、内容合规风险大（SARA、诽谤、平台社区准则）。

核心逻辑流是一条 6 阶段的长链推理与多 Agent 协作管线：Trend Scout（拾取选题）→ Researcher（结构化抽取声明、来源、实体、日期）→ Policy Analyst（基于 BPS、Kemenkeu、BI 等历史数据做长链推理，识别二阶效应与利益相关方）→ Content Studio（生成 X / Instagram / TikTok / YouTube Shorts 四平台草稿）→ Safety Reviewer（SARA / 诽谤 / 来源完整性扫描）→ Human Approval（人工最终审核，绝不自动发布）。每个 Agent 都是纯函数：JSON 输入、严格 JSON 输出，可重放、可测试、可审计。

技术栈完全基于 **Xiaomi MiMo OpenAI 兼容 API**：长链推理阶段用 `mimo-v2.5-pro`（单次调用 8-12k context），快速防护阶段用 `mimo-v2-pro`，结构化输出通过 `response_format={"type":"json_object"}` 直接获得。我使用 Codex、Claude Code 与 Hermes Agent 完成开发与日常迭代。Token 用量估算：单次完整管线约 30k tokens，含评估与回归测试预算约 80k；每日活跃创作工作流加上 agentic coding 约 700k tokens/day，月度约 20-25M tokens，预算选举与预算季会爆发到 50M。

项目已开源于 GitHub，包含：完整管线代码、6 个 Agent 实现、CLI 入口、架构文档、CI workflow、静态 demo 页面、可复现的端到端示例（"subsidi BBM 2026" 政策分析全流程 JSON 产物）、token 预算说明与责任使用规范。Roadmap 包括 BPS / Kemenkeu API connector、bahasa 风格预设、以及基于 gold-labeled 事实表的评估框架。我希望用 MiMo 的 Token Plan / 赠金支撑日常迭代与长上下文评估实验，把这个 lab 推到能服务印尼上百名独立创作者的程度。

仓库：https://github.com/bosskuh666-ops/mimo-orbit-agent-lab

---

## English version (backup)

I'm building **MiMo Orbit Agent Lab**, an open-source multi-agent workflow for Indonesian creators producing civic content (policy, macroeconomics, AI/tech). Three real pains it solves: source verification is slow, cross-platform rewriting is expensive, and content compliance (SARA, defamation, platform rules) is risky.

The pipeline runs six stages with long-chain reasoning and multi-agent collaboration: Trend Scout → Researcher → Policy Analyst → Content Studio → Safety Reviewer → Human Approval. Every agent is a pure function with strict JSON in/out, replayable and auditable.

Built on Xiaomi MiMo OpenAI-compatible API: `mimo-v2.5-pro` for long reasoning (8-12k context), `mimo-v2-pro` for fast safety checks. JSON-mode `response_format` removes the parse/repair loop. Built with Codex, Claude Code, and Hermes Agent.

Daily usage estimate: 700k tokens (active dev), ~20-25M/month sustained, bursting to 50M during election/budget cycles. The repo ships full code, 6 agents, CLI, architecture doc, CI workflow, demo page, and an end-to-end JSON example for "subsidi BBM 2026", plus a responsible-use policy.

Repo: https://github.com/bosskuh666-ops/mimo-orbit-agent-lab
