# sessions 命令 (会话管理)

用于列出和管理网关存储的所有聊天会话。

## 常用操作示例
- **列出所有会话**：`openclaw sessions`
- **查看最近活跃的会话**：
  `openclaw sessions --active 120` (列出过去 120 分钟内有活动的会话)
- **输出 JSON 格式**：`openclaw sessions --json`

## 会话存储说明
- 会话记录保存在网关主机的 `~/.openclaw/agents/<agentId>/sessions/` 目录下。
- 包含会话元数据（`sessions.json`）和原始消息记录（`.jsonl` 文件）。
