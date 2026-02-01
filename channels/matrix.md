# Matrix 频道插件 (Bot SDK)

**当前状态**：作为可选插件提供。支持私聊、房间 (Room)、线程、媒体附件及端到端加密 (E2EE)。

## 插件安装
\`\`\`bash
openclaw plugins install @openclaw/matrix
\`\`\`

## 快速上手
1. 在任意 Matrix 主服务器 (Homeserver) 上创建一个机器人账号。
2. 获取该账号的 **Access Token**（可以通过 \`curl\` 调用登录接口获取）。
3. 配置 OpenClaw 指向你的主服务器地址和 Token。
4. 在 Element 或 Beeper 等客户端发起私聊或邀请机器人进入房间。

## 核心配置
```json
{
  "channels": {
    "matrix": {
      "enabled": true,
      "homeserver": "https://matrix.org",
      "accessToken": "你的TOKEN",
      "encryption": true
    }
  }
}
```

## 端到端加密 (E2EE)
- **支持情况**：通过 Rust SDK 支持加密。
- **设备验证**：开启加密后，机器人启动时会向你的其他会话发送验证请求。请在手机端通过验证以启用密钥共享。
- **依赖说明**：如果报错缺少 \`matrix-sdk-crypto\`，请运行 \`pnpm rebuild\`。

## 运行机制
- **私聊 (DM)**：会话共享主 Agent 上下文。
- **房间 (Room)**：会话将按房间 ID 隔离。
- **自动加入**：默认会自动接受所有邀请并进入房间（可配置 \`autoJoin\`）。

## 交付目标
在推送消息时，可以使用 \`!roomId:example.org\` 或 \`#alias:example.org\`。
