# cron 命令 (任务管理)

用于管理网关调度器中的定时任务。

## 常见操作示例
- **列出任务**：`openclaw cron list`
- **更新交付设置**（不改变消息内容）：
  `openclaw cron edit <job-id> --deliver --channel telegram --to "123456789"`
- **取消交付**：
  `openclaw cron edit <job-id> --no-deliver`
- **手动立即运行**：
  `openclaw cron run <job-id> --force`

更多用法请运行 `openclaw cron --help` 查看。
