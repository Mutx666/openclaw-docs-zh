# Webhooks (外部触发器)

OpenClaw 网关公开一个 HTTP Webhook 端点，用于接收来自外部系统的触发指令。

## 启用 Webhooks
在 \`openclaw.json\` 中配置：
\`\`\`json
{
  "hooks": {
    "enabled": true,
    "token": "你的安全Token",
    "path": "/hooks"
  }
}
\`\`\`

## 核心接口 (Endpoints)

### 1. 唤醒接口：\`POST /hooks/wake\`
仅在主会话中注入系统事件并唤醒 Agent。适合“收到新邮件”这种简单提醒。

### 2. 代理接口：\`POST /hooks/agent\`
让 Agent 立即运行指定任务轮次。适合需要 Agent 立即处理某项外部请求的场景。

## 安全建议
- **本地或隧道**：建议仅在本地回环或通过安全隧道（如 Tailscale）访问。
- **独立 Token**：不要与网关密码混用。
