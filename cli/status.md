# status 命令 (状态检查)

`status` 命令用于诊断 OpenClaw 的频道、会话以及整体健康状况。

## 常用语法
- `openclaw status`：显示基础概览（网关状态、已加载插件、活跃会话）。
- `openclaw status --all`：显示所有详细信息，包括已禁用的频道。
- `openclaw status --deep`：执行实时探测（尝试连接 WhatsApp, Telegram, Discord 等），检查认证是否失效。
- `openclaw status --usage`：查看当前 Token 的使用额度统计。

## 输出项说明
- **Gateway**: 显示网关进程的 PID、运行时间和监听端口。
- **Update**: 显示当前版本分支、Git SHA 码，并提示是否有新版本可更新。
- **Agents**: 列出所有配置的 Agent 及其独立的工作空间路径。
