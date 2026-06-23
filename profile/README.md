<div align="center">

<img src="https://avatars.githubusercontent.com/u/289767358?s=200&v=4" width="120" alt="codecora" />

# codecoradev

**Developer tools for AI agents — offline-first, privacy-first, open source.**

[![Website](https://img.shields.io/badge/codecora.dev-%E2%86%92-blue?style=flat-square)](https://codecora.dev)
[![Org stars](https://img.shields.io/badge/dynamic/json?url=https://api.github.com/orgs/codecoradev/repos&query=%24%5B%3F%28%40.full_name%3D%3D%27codecoradev%2Futeke%27%29%5D.stargazers_count%20%2B%20%24%5B%3F%28%40.full_name%3D%3D%27codecoradev%2Fcora-cli%27%29%5D.stargazers_count%20%2B%20%24%5B%3F%28%40.full_name%3D%3D%27codecoradev%2Fcorin%27%29%5D.stargazers_count%20%2B%20%24%5B%3F%28%40.full_name%3D%3D%27codecoradev%2Ftrapfall%27%29%5D.stargazers_count&label=total%20stars&style=social)](https://github.com/codecoradev)
[![Rust](https://img.shields.io/badge/built%20with-Rust-orange?style=flat-square)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/license-Apache%202.0%20·%20MIT-blue?style=flat-square)](LICENSE)

</div>

---

<table>
<tr>
<td width="50%" valign="top">

### 🧠 Uteke
**Offline-first semantic memory engine for AI agents.**

Store, recall, and connect memories — ~30ms recall, zero cloud, single binary.

**Hybrid search:** HNSW vector + FTS5, fused via RRF (k=60).
**Embeddings:** ONNX EmbeddingGemma Q4, 768d.
**Storage:** SQLite WAL · Schema v12.

![Stars](https://img.shields.io/github/stars/codecoradev/uteke?style=social)
![CI](https://github.com/codecoradev/uteke/actions/workflows/ci.yml/badge.svg)
![License](https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square)
![Version](https://img.shields.io/badge/version-v0.4.2-green?style=flat-square)

```bash
curl -sSL https://codecora.dev/install-uteke | sh
```

[📖 GitHub](https://github.com/codecoradev/uteke) · [📦 crates.io](https://crates.io/crates/uteke) · [📚 Docs](https://github.com/codecoradev/uteke/tree/develop/docs)

</td>
<td width="50%" valign="top">

### 🔍 Cora CLI
**AI-powered code review CLI. BYOK.**

Multi-LLM review (OpenAI, Anthropic, Groq, Ollama, Z.AI). Pre-commit hooks, SARIF output, MCP server.

**Deterministic:** 11 security patterns + 12 secret detection patterns.
**Languages:** Dart, Svelte, TS, Go, Rust, Python.
**Integrations:** GitHub Actions, Claude Code, Cursor, Copilot.

![Stars](https://img.shields.io/github/stars/codecoradev/cora-cli?style=social)
![CI](https://github.com/codecoradev/cora-cli/actions/workflows/ci.yml/badge.svg)
![crates.io](https://img.shields.io/crates/v/cora-cli?style=flat-square)
![License](https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square)

```bash
curl -fsSL https://codecora.dev/install-cora | sh
```

[📖 GitHub](https://github.com/codecoradev/cora-cli) · [📦 crates.io](https://crates.io/crates/cora-cli) · [🛒 GH Marketplace](https://github.com/marketplace/actions/cora-ai-code-review)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🖥️ CorIn
**Desktop knowledge workstation for AI memory.**

Visualize memory graphs, manage rooms, edit markdown. Think Obsidian — but for AI memory.

**Stack:** Tauri 2 + Svelte 5 (runes).
**Viz:** D3.js force-directed graph.
**Editor:** CodeMirror 6 + marked + DOMPurify.
**Theme:** Catppuccin Mocha.

![Stars](https://img.shields.io/github/stars/codecoradev/corin?style=social)
![License](https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square)
![Version](https://img.shields.io/badge/version-v0.1.1-green?style=flat-square)
![Tauri](https://img.shields.io/badge/Tauri-2-blueviolet?style=flat-square)

[📖 GitHub](https://github.com/codecoradev/corin) · [⬇️ Releases](https://github.com/codecoradev/corin/releases)

</td>
<td width="50%" valign="top">

### 🪤 TrapFall
**Self-hosted error tracking. Sentry-compatible.**

Drop-in DSN swap — works with any Sentry SDK. Rust + SvelteKit 5.

**Size:** 5.75MB Docker image (scratch + MUSL + rustls).
**Grouping:** Blake3 fingerprinting.
**Dashboard:** Real-time WebSocket · SvelteKit 5 + Tailwind v4.
**DB:** SQLite (default) or Postgres (built-in).
**MCP:** 12 AI agent tools.

![Stars](https://img.shields.io/github/stars/codecoradev/trapfall?style=social)
![License](https://img.shields.io/badge/license-Apache%202.0-blue?style=flat-square)
![Version](https://img.shields.io/badge/version-v0.1.4-green?style=flat-square)
![Docker](https://img.shields.io/badge/image-5.75MB-blue?style=flat-square)

```bash
docker run -p 3000:3000 -v trapfall-data:/data \
  ghcr.io/codecoradev/trapfall:latest
```

[📖 GitHub](https://github.com/codecoradev/trapfall) · [⬇️ Releases](https://github.com/codecoradev/trapfall/releases)

</td>
</tr>
</table>

---

<div align="center">

## 🧬 Shared DNA

</div>

Every Codecora product shares the same engineering principles:

| Principle | What it means |
|-----------|---------------|
| 🦀 **Rust-native** | Fast, memory-safe, single binary — no runtime, no Node, no Python |
| 🔌 **MCP server** | Every tool exposes an MCP server for AI agent integration |
| 🔒 **Local-first** | Your data stays on your machine. Zero telemetry, zero cloud (BYOK where LLM needed) |
| 🔓 **Open source** | Apache 2.0 or MIT. Fork it, ship it, own it. |
| 📦 **Zero-config** | One install command. No Docker (unless you want it). No API keys (unless your LLM needs them). |
| 🧪 **Battle-tested** | Hundreds of unit tests per product. CI-gated. Production-used. |

---

<div align="center">

## 💡 Why Codecora?

</div>

- **Your AI forgets.** Agents lose context between sessions. Uteke gives them persistent memory — offline.
- **Your code deserves review.** Not after merge, not in a dashboard — in your terminal, before commit. That's Cora.
- **Your data stays yours.** No cloud lock-in. No telemetry. No "phone home." Every tool runs locally or self-hosted.
- **Your stack should be Rust.** Fast binaries, tiny Docker images, memory safety. No 500MB Node runtimes.

---

<div align="center">

## ⚡ Quick Install

</div>

```bash
# 🧠 Uteke — memory engine
curl -sSL https://raw.githubusercontent.com/codecoradev/uteke/main/install.sh | sh

# 🔍 Cora — code review CLI (or: install-bundle.sh for Cora + Uteke together)
curl -fsSL https://raw.githubusercontent.com/codecoradev/cora-cli/main/install.sh | sh

# 🖥️ CorIn — desktop workstation
#    Download from https://github.com/codecoradev/corin/releases

# 🪤 TrapFall — error tracking
docker run -p 3000:3000 -v trapfall-data:/data \
  ghcr.io/codecoradev/trapfall:latest
```

---

<div align="center">

## 🔗 Links

</div>

| | Link |
|---|---|
| 🌐 Website | [codecora.dev](https://codecora.dev) |
| 🧠 Uteke | [github.com/codecoradev/uteke](https://github.com/codecoradev/uteke) |
| 🔍 Cora CLI | [github.com/codecoradev/cora-cli](https://github.com/codecoradev/cora-cli) |
| 🖥️ CorIn | [github.com/codecoradev/corin](https://github.com/codecoradev/corin) |
| 🪤 TrapFall | [github.com/codecoradev/trapfall](https://github.com/codecoradev/trapfall) |
| 📦 crates.io | [uteke](https://crates.io/crates/uteke) · [cora-cli](https://crates.io/crates/cora-cli) |
| 🛒 GitHub Marketplace | [Cora AI Code Review](https://github.com/marketplace/actions/cora-ai-code-review) |

---

<div align="center">

<sub>Built with Rust · Svelte 5 · Tauri 2 · SQLite · ONNX · HNSW</sub><br>
<sub>Your AI remembers. Your data stays.</sub>

</div>
