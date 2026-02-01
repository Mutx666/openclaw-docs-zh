# 投票功能 (Polls)

OpenClaw 支持在 WhatsApp, Discord, MS Teams 频道发起交互式投票。

## 命令行操作 (CLI)
- **WhatsApp**: \`openclaw message poll --target <号> --poll-question "吃啥？" --poll-option "火锅" --poll-option "烧烤"\`
- **Discord**: \`openclaw message poll --channel discord --target channel:<ID> --poll-question "选A还是B？" --poll-option "A" --poll-option "B"\`

## 平台差异
- **Discord**: 支持 2-10 个选项，支持设置持续时间。
- **MS Teams**: 通过 Adaptive Cards 实现，需网关保持在线以计票。
