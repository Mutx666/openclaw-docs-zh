# Mattermost 频道插件 (WebSocket 模式)

**当前状态**：作为可选插件提供。支持公聊频道、私有组及私聊 (DM)。

## 插件安装
该插件未包含在核心包中，需手动安装：
\`\`\`bash
openclaw plugins install @openclaw/mattermost
\`\`\`

## 快速上手
1. 在 Mattermost 系统控制台创建一个 **Bot 账户**。
2. 复制产生的 **Bot Token**。
3. 获取 Mattermost 服务器的 **Base URL** (例如 \`https://chat.yourteam.com\`)。
4. 配置 OpenClaw 配置文件。

## 核心配置
```json
{
  "channels": {
    "mattermost": {
      "enabled": true,
      "botToken": "你的TOKEN",
      "baseUrl": "你的服务器URL",
      "dmPolicy": "pairing"
    }
  }
}
```

## 聊天模式 (Chat Modes)
你可以控制机器人在频道内的活跃程度：
- **oncall (默认)**：仅在被 @提及 时回复。
- **onmessage**：回复频道内的每一条消息。
- **onchar**：当消息以特定字符（如 \`>\` 或 \`!\`）开头时回复。

## 交付目标
在推送消息时，可以使用以下格式：
- \`channel:ID\` (公聊频道)
- \`user:ID\` (私聊)
- \`@用户名\` (私聊，通过 API 自动解析)
