# Google Chat 频道插件 (Webhook 模式)

**当前状态**：支持通过 Google Chat API Webhooks 实现私聊 (DM) 和空间 (Space) 交互。

## 快速上手
1. 在 Google Cloud 控制台启用 **Google Chat API**。
2. 创建一个 **Service Account** 并下载 JSON 格式的秘钥文件。
3. 在 Google Cloud 中创建一个 Chat App：
   - 配置连接方式为 **HTTP Endpoint**。
   - 填写你的网关公网 URL，后缀为 \`/googlechat\`。
4. 将你的邮箱地址加入 App 的可见性名单并发布。
5. 在 OpenClaw 配置文件中指定 Service Account 文件路径。

## 核心配置
```json
{
  "channels": {
    "googlechat": {
      "enabled": true,
      "serviceAccountFile": "/path/to/service-account.json",
      "audienceType": "app-url",
      "audience": "https://your-public-url/googlechat"
    }
  }
}
```

## 网络暴露建议
由于 Google Chat 需要公网 HTTPS 回调，推荐使用 **Tailscale Funnel**：
- 它能将你的本地网关端口安全地暴露给 Google，而无需配置复杂的防火墙规则。

## 运行机制
- **私聊 (DM)**：会话隔离为 \`agent::googlechat:dm:ID\`。
- **空间 (Space)**：默认需要 @机器人 才能触发。
- **提及检测**：如果发现 @机器人 不响应，请在配置中显式设置 \`botUser\`。

## 常用操作
- **表情回应**：支持通过 \`reactions\` 工具添加回应。
- **输入指示**：支持在 Agent 思考时显示“正在输入”。
