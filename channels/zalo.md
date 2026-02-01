# Zalo 频道插件 (Bot API)

**当前状态**：实验性阶段。目前仅支持私聊 (DM)，群组支持待 Zalo 官方开放。

## 插件安装
\`\`\`bash
openclaw plugins install @openclaw/zalo
\`\`\`

## 快速上手
1. 在 [Zalo Bot Platform](https://bot.zaloplatforms.com) 创建并配置机器人。
2. 获取 **Bot Token**。
3. 配置 OpenClaw 配置文件。
4. 启动网关，首次发起聊天需通过配对认证。

## 核心配置
```json
{
  "channels": {
    "zalo": {
      "enabled": true,
      "botToken": "你的TOKEN",
      "dmPolicy": "pairing"
    }
  }
}
```

## 运行机制
- **限制**：由于 Zalo API 限制，单条消息上限为 2000 字符。
- **媒体支持**：支持发送和接收图片。
- **轮询与 Webhook**：默认使用长轮询（无需公网 IP），也可通过 \`webhookUrl\` 切换为回调模式。

## 交付目标
在推送消息时，使用数字形式的聊天 ID 作为目标。
