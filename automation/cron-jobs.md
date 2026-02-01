# 定时任务 (Cron Jobs - 网关调度器)

Cron 是网关内置的调度器。它会持久化保存任务，在指定时间唤醒 Agent，并可以选择将输出发送回聊天频道。

## 快速上手 (Actionable)

创建一个一次性提醒：
\`openclaw cron add --name "提醒" --at "2026-02-01T16:00:00Z" --session main --system-event "提醒：检查文档草稿" --wake now --delete-after-run\`

设置一个带交付功能的循环任务：
\`openclaw cron add --name "早报" --cron "0 7 * * *" --tz "Asia/Shanghai" --session isolated --message "总结昨晚的更新。" --deliver --channel slack --to "channel:C1234567890"\`

## 核心概念

### 执行模式
- **主会话 (Main session)**：通过 \`payload.kind = "systemEvent"\` 运行。任务排队进入系统事件，在下次心跳或立即（\`wake now\`）触发。适合需要主会话上下文的任务。
- **隔离会话 (Isolated session)**：通过 \`payload.kind = "agentTurn"\` 运行。在一个独立的会话中执行，不会干扰主会话的历史记录。适合频繁的后台任务。

### 调度类型
- **at**: 一次性时间戳（支持 ISO 8601 格式）。
- **every**: 固定间隔（毫秒）。
- **cron**: 标准的 5 字段 cron 表达式（支持时区配置）。

### 存储位置
默认保存在网关主机的 \`~/.openclaw/cron/jobs.json\` 中。

## 常见操作 (CLI)
- **列出任务**：\`openclaw cron list\`
- **手动运行**：\`openclaw cron run <job-id> --force\`
- **运行记录**：\`openclaw cron runs --id <job-id>\`
- **编辑任务**：\`openclaw cron edit <jobId> --message "新指令"\`
- **删除任务**：\`openclaw cron remove <job-id>\`

## 故障排除
- **任务不运行**：检查 \`cron.enabled\` 是否为 true，以及网关进程是否正在运行。
- **Telegram 交付失败**：如果是论坛话题，建议使用 \`-100...:topic:ID\` 这种显式的格式。
