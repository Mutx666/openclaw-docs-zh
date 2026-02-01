# Discord 频道插件 (Discord Bot API)

**当前状态**：支持通过官方 Discord 机器人网关进行私聊 (DM) 和服务器文本频道交互。

## 快速上手
1. 在 [Discord Developer Portal](https://discord.com/developers/applications) 创建一个应用并添加 Bot。
2. 开启 **Message Content Intent** 和 **Server Members Intent**。
3. 获取 Bot Token 并配置到 OpenClaw：
   - 环境变量：`DISCORD_BOT_TOKEN=...`
   - 或配置文件：`channels.discord.token: "..."`
4. 将机器人邀请至你的服务器。
5. 首次私聊需要通过配对码认证：`openclaw pairing approve discord <用户ID>`。

## 核心配置
```json
{
  "channels": {
    "discord": {
      "enabled": true,
      "token": "你的BOT_TOKEN"
    }
  }
}
```

## 运行机制
- **私聊 (DM)**：自动归入 Agent 的主会话。
- **群组/服务器频道**：会话将按频道隔离（例如 `agent::discord:channel:ID`）。
- **提及触发**：在服务器频道中，默认需要 @机器人 才能触发回复。

## 常见操作
- **消息发送/编辑/删除**：Agent 可以完全管理频道内的消息。
- **表情回应**：支持添加和读取 Reaction。
- **成员信息查询**：可以检索服务器成员的身份组和详细信息。
