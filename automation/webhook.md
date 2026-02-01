# Webhooks (外部触发器)

OpenClaw 网关可以公开一个 HTTP Webhook 端点，用于接收来自外部系统（如 GitHub、IFTTT、Zapier 等）的触发指令。

## 启用 Webhooks
在你的 \`openclaw.json\` 中进行如下配置：
\`\`\`json
{
  "hooks": {
    "enabled": true,
    "token": "你的安全Token",
    "path": "/hooks"
  }
}
\`\`\`
*注：\`hooks.token\` 是强制要求的。*

## 认证方式
所有发送到 Webhook 的请求都必须携带 Token。推荐使用以下 Header 之一：
- \`Authorization: Bearer <TOKEN>\` (推荐)
- \`x-openclaw-token: <TOKEN>\`

## 核心接口 (Endpoints)

### 1. 唤醒接口：\`POST /hooks/wake\`
仅在主会话中注入一个系统事件并唤醒 Agent。
- **Payload 示例**：\`{ "text": "收到新邮件", "mode": "now" }\`
- **效果**：Agent 会收到该事件描述，并根据 \`mode\` 决定是立即响应还是等待下一次心跳。

### 2. 代理接口：\`POST /hooks/agent\`
让 Agent 立即运行一个指定的任务轮次。
- **Payload 示例**：
  \`\`\`json
  {
    "message": "总结收件箱内容",
    "name": "邮件助手",
    "deliver": true,
    "channel": "dingtalk"
  }
  \`\`\`
- **效果**：Agent 会在一个隔离会话中运行该任务，并将结果推送到指定的频道（如钉钉）。

## 安全建议
- **不要公开暴露**：建议将 Webhook 端点保留在本地回环地址（Loopback）或通过 Tailscale 等安全隧道访问。
- **独立 Token**：为 Webhook 使用专用的 Token，不要与网关的登录密码混用。
- **内容过滤**：默认情况下，Webhook 接收的内容会被包裹在安全边界内，以防潜在的 Prompt 注入攻击。
