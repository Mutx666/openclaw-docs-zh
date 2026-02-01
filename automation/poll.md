# 投票功能 (Polls)

OpenClaw 支持在特定通讯频道发起交互式投票。

## 支持的频道
- **WhatsApp** (Web 频道)
- **Discord**
- **MS Teams** (通过 Adaptive Cards 实现)

## 命令行操作示例 (CLI)

### WhatsApp 投票
```bash
openclaw message poll --target <手机号> \
  --poll-question "今天午饭吃什么？" \
  --poll-option "火锅" --poll-option "日料" --poll-option "快餐"
```

### Discord 投票
```bash
openclaw message poll --channel discord --target channel:<ID> \
  --poll-question "项目计划选哪个？" \
  --poll-option "方案A" --poll-option "方案B" --poll-duration-hours 48
```

## 平台差异说明
- **WhatsApp**: 支持 2-12 个选项，不支持设置持续时间。
- **Discord**: 支持 2-10 个选项，持续时间默认为 24 小时（最长 768 小时）。
- **MS Teams**: 通过 OpenClaw 托管的 Adaptive Cards 实现，需要网关保持在线以记录投票数据。

## Agent 工具调用
Agent 可以通过调用 `message` 工具的 `poll` 动作来发起投票。例如：“帮我在群里发起一个关于下周团建地点的投票”。
