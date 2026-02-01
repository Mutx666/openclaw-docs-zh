# 安全性 (Security)

运行一个拥有 Shell 权限的 AI Agent 是一件“刺激”且有风险的事情。本指南旨在帮助你构建坚固的安全防线。

## 快速检查
定期运行安全审计命令：
- `openclaw security audit`：检查常见的配置漏洞（如网关暴露、权限过大）。
- `openclaw security audit --fix`：自动应用安全补丁（例如收紧组策略）。

## 安全三原则
1. **身份第一**：决定谁可以和机器人说话（私聊配对 / 白名单）。
2. **范围第二**：决定机器人在哪里可以行动（提及触发 / 组限制 / 沙箱）。
3. **模型最后**：假设模型可能会被恶意操控，因此必须从外部工具层面进行限制。

## 核心防线

### 1. 私聊访问控制 (DM Policy)
- **pairing (默认)**：陌生人发消息会收到配对码，需你手动运行 `openclaw pairing approve` 才能通过。
- **allowlist**：仅允许名单内的用户。
- **open**：极度不推荐，除非你完全信任所有人。

### 2. 网关绑定与认证
- **绑定地址**：默认 `loopback`（仅本地访问）。如果需要远程访问，推荐使用 **Tailscale** 而不是直接监听 `0.0.0.0`。
- **认证方式**：强制开启 `gateway.auth`，使用 Token 或强密码。

### 3. 沙箱 (Sandboxing)
建议为处理不可信输入的 Agent 开启沙箱：
- `agents.defaults.sandbox.mode: "all"`
- 限制 Agent 对主机会话文件系统的访问权限（设置为 `ro` 或 `none`）。

## 应急响应
如果你怀疑机器人被“玩坏了”或凭据泄露：
1. **切断扩散**：立即停止网关 `openclaw gateway stop`。
2. **收缩权限**：将 `gateway.bind` 设回 `loopback`。
3. **重置秘钥**：修改网关 Token，并重置所有关联频道的 Bot Token。
4. **审计日志**：检查 `/tmp/openclaw/` 下的日志，确认是否有非预期的工具调用。
