# OpenClaw 中文文档

> “EXFOLIATE! EXFOLIATE!” —— 可能是一只来自外星的龙虾说的。

OpenClaw 是一个多功能的通讯网关，支持 WhatsApp、Telegram、Discord 和 iMessage，旨在为 AI Agent（如 Pi）提供连接桥梁。通过插件，你还可以接入 Mattermost 等更多平台。

只需发送一条消息，Agent 的回复就会即刻送达你的口袋。

[GitHub](https://github.com/openclaw/openclaw) · [发布日志](https://github.com/openclaw/openclaw/releases) · [在线文档](https://mutx666.github.io/openclaw-docs-zh/)

---

## 快速开始

- **从零开始安装**：[点击查看安装指南](install/updating.md)
- **引导式设置 (推荐)**：使用向导 `openclaw onboard`。
- **打开仪表盘**：[http://127.0.0.1:18789/](http://127.0.0.1:18789/)

如果你在本地运行网关，该链接将直接打开浏览器控制台。如果无法打开，请先运行 `openclaw gateway`。

## 核心特性

- 📱 **多平台集成**：深度支持 WhatsApp Web、Telegram Bot、Discord Bot、iMessage 等。
- 🧠 **多 Agent 路由**：支持将不同的账号或联系人路由到互相隔离的 Agent（拥有独立的内存空间）。
- 🔐 **订阅认证**：支持通过 OAuth 接入 Anthropic (Claude Pro/Max) 和 OpenAI (ChatGPT/Codex)。
- ⏱️ **流式输出**：支持流式回复和 Telegram 的草稿预览。
- 👥 **群聊支持**：默认基于提及（@提及）触发，支持灵活的激活模式切换。
- 📎 **媒体交互**：支持发送和接收图像、音频、文档。
- 🖥️ **伴侣应用**：提供 Web 端、macOS 菜单栏应用、iOS/Android 节点。

## 运行机制

大多数操作通过网关（`openclaw gateway`）完成。这是一个长期运行的单一进程，负责持有所有频道的连接和 WebSocket 控制平面。

## 许可证
本项目采用 MIT 许可证 —— 像海洋里的龙虾一样自由 🦞。

---
> **注**：本项目为官方文档的中文翻译版，由 AI 助手小爱同学自动维护。
