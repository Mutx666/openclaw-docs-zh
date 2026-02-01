# WhatsApp 频道插件 (Baileys Web)

**当前状态**：支持通过 WhatsApp Web 协议接入。网关持有会话，无需官方 API。

## 快速上手
1. 使用一个独立的手机号（推荐）或你的个人号。
2. 在 \`openclaw.json\` 中配置 WhatsApp 策略。
3. 运行 \`openclaw channels login\`，并在手机 WhatsApp 上扫描出现的 QR 码（已连接设备）。
4. 启动网关。

## 核心配置
```json
{
  "channels": {
    "whatsapp": {
      "dmPolicy": "allowlist",
      "allowFrom": ["+8613800000000"]
    }
  }
}
```

## 两种运行模式
### 1. 独立号码模式 (推荐)
使用备用手机和独立号码。这种方式最稳定，不会有“自言自语”的逻辑冲突。
### 2. 个人号码模式 (Self-Chat)
使用你自己的主号。需开启 \`selfChatMode: true\`。建议通过“给往自己发消息”来测试。

## 关键特性
- **自动已读**：默认会自动发送已读回执（蓝钩），可在配置中关闭。
- **语音消息**：Agent 可以发送语音泡泡（PTT），支持 OGG/Opus 格式。
- **自动回应 (Ack Reaction)**：可以在收到消息后立刻自动回复一个表情（如 👀），表示 Agent 正在处理。

## 常见问题
- **无法连接**：如果显示 “Not linked”，请重新运行 \`openclaw channels login\` 扫码。
- **运行时环境**：**不要使用 Bun 运行**，WhatsApp 驱动在 Bun 下极不稳定，请务必使用 Node.js。
