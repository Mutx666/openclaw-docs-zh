# 身份验证监控 (Auth Monitoring)

OpenClaw 通过 `openclaw models status` 暴露 OAuth 过期健康状态。建议将其用于自动化和告警；脚本是针对手机工作流的可选附加功能。

## 推荐方案：CLI 检查（便携式）

`openclaw models status --check`

退出代码：

- 0: 正常 (OK)
- 1: 凭据已过期或缺失
- 2: 即将过期（24小时内）

该方案适用于 cron/systemd，无需额外脚本。

## 可选脚本（运维 / 手机工作流）

这些脚本位于 `scripts/` 目录下，是可选的。它们假设您拥有网关主机的 SSH 访问权限，并针对 systemd 和 Termux 进行了优化。

- \`scripts/claude-auth-status.sh\`: 现在使用 \`openclaw models status --json\` 作为事实来源（如果 CLI 不可用，则回退到直接读取文件），因此请确保将 \`openclaw\` 保留在 \`PATH\` 中以供定时器使用。
- \`scripts/auth-monitor.sh\`: cron/systemd 定时器目标；发送告警（ntfy 或手机）。
- \`scripts/systemd/openclaw-auth-monitor.{service,timer}\`: systemd 用户定时器。
- \`scripts/claude-auth-status.sh\`: Claude Code + OpenClaw 身份验证检查器（完整/json/简单）。
- \`scripts/mobile-reauth.sh\`: 通过 SSH 的引导式重新认证流程。
- \`scripts/termux-quick-auth.sh\`: 一键式小组件状态 + 打开认证 URL。
- \`scripts/termux-auth-widget.sh\`: 完整的引导式小组件流程。
- \`scripts/termux-sync-widget.sh\`: 同步 Claude Code 凭据 → OpenClaw。

如果您不需要手机自动化或 systemd 定时器，可以忽略这些脚本。
