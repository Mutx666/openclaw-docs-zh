# Gmail 消息推送 (Gmail Pub/Sub)

**目标**：实现 Gmail 邮件监听 -> Google Cloud Pub/Sub 推送 -> OpenClaw Webhook 自动处理。

## 必备条件
- **gcloud CLI**: 已安装并登录。
- **gog (gogcli)**: 已安装并完成 Gmail 授权。
- **Tailscale**: 推荐使用 Tailscale Funnel 作为公网 HTTPS 终点。

## 核心配置
\`\`\`json
{
  "hooks": {
    "enabled": true,
    "presets": ["gmail"]
  }
}
\`\`\`

## 运行机制
- **自动续订**：网关启动时会自动运行监听服务。
- **即时通知**：当有新邮件到达时，Agent 会生成摘要并即时推送到你的聊天频道。
