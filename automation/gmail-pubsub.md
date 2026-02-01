# Gmail 消息推送 (Gmail Pub/Sub)

**目标**：实现 Gmail 邮件监听 -> Google Cloud Pub/Sub 推送 -> OpenClaw Webhook 自动处理。

## 必备条件
- **gcloud CLI**: 已安装并登录。
- **gog (gogcli)**: 已安装并完成 Gmail 账号授权。
- **OpenClaw Hooks**: 已在配置中启用。
- **Tailscale**: 已登录（官方支持使用 Tailscale Funnel 作为公网 HTTPS 终点）。

## 推荐方案：向导设置 (Wizard)
使用 OpenClaw 助手可以一键完成所有环节的对接：
\`openclaw webhooks gmail setup\`

## 核心配置示例
在你的 \`openclaw.json\` 中启用 Gmail 预设：
\`\`\`json
{
  "hooks": {
    "enabled": true,
    "token": "你的HOOK_TOKEN",
    "presets": ["gmail"],
    "gmail": {
      "model": "openai/gpt-5.2-mini",
      "thinking": "off"
    }
  }
}
\`\`\`

## 运行机制
- **自动启动**：网关启动时会自动运行 \`gog gmail watch serve\` 并自动续订监听状态。
- **即时通知**：当有新邮件到达时，Agent 会根据模板生成摘要，并即时推送到你最后使用的聊天频道（如钉钉、WhatsApp 等）。
- **安全边界**：默认情况下，Gmail Hook 内容会被包裹在外部内容安全边界内，防止注入攻击。

## 常见问题
- **无法接收消息**：检查 GCP 项目 ID 是否匹配，以及是否为该 Topic 赋予了 \`roles/pubsub.publisher\` 权限。
- **消息为空**：Gmail 推送通常只提供 \`historyId\`，需要确保网关可以正常调用 \`gog\` 来获取历史详情。
