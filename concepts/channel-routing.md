# 频道路由 (Channel Routing)

OpenClaw 采用确定性的路由机制：回复总是会自动原路返回消息的来源频道。模型本身不参与频道的选择，一切由网关配置控制。

## 关键术语
- **Channel (频道)**：如 whatsapp, telegram, discord, slack, imessage 等。
- **AgentId**：代表一个独立的“大脑”（拥有独立的工作空间、模型配置和会话存储）。
- **SessionKey**：用于隔离上下文和控制并发的唯一键。

## 会话 ID 格式示例
- **私聊**：所有平台的私聊默认都会归并到 Agent 的主会话（例如 \`agent:main:main\`）。
- **群组/频道**：根据频道 ID 进行隔离（例如 \`agent:main:telegram:group:ID\`）。
- **话题/线程**：支持在 ID 后追加 \`:thread:ID\` 或 \`:topic:ID\`。

## 路由优先级 (如何选择 Agent)
当一条消息进来时，网关按以下顺序匹配 Agent：
1. **精确匹配**：根据特定用户 ID 或手机号绑定。
2. **群组/服务器匹配**：根据 Discord Guild ID 或 Slack Team ID 绑定。
3. **账户匹配**：根据特定频道账号绑定。
4. **默认 Agent**：如果都没有匹配，则使用默认设置（通常是名为 \`main\` 的 Agent）。

## 广播组 (多 Agent 并行)
通过配置 \`broadcast\` 组，你可以让多个 Agent 同时响应同一个群组或私聊请求（如一个负责回答，一个负责记录日志）。

## 核心配置示例
```json
{
  "agents": {
    "list": [{ "id": "support", "workspace": "~/workspace-support" }]
  },
  "bindings": [
    { "match": { "channel": "slack", "teamId": "T123" }, "agentId": "support" }
  ]
}
```
