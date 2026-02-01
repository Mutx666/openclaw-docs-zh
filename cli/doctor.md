# doctor 命令 (自愈诊断)

用于对网关、频道和配置文件进行健康检查并提供快速修复方案。

## 常用命令示例
- **基础诊断**：`openclaw doctor`
- **执行修复**：`openclaw doctor --fix` (或 `--repair`)
- **深度扫描**：`openclaw doctor --deep`

## 注意事项
- **交互式提示**：只有在终端环境下才会弹出修复确认提示。在后台（如 Cron 或远程脚本）运行时会自动跳过。
- **自动备份**：执行 `--fix` 时，系统会自动将旧配置备份为 `~/.openclaw/openclaw.json.bak`。
- **配置清理**：修复过程中会自动剔除过时或未知的配置键，以确保网关能正常启动。

## macOS 环境变量提示
如果在 macOS 上遇到持续的“未授权”错误，请检查是否有残留的 `launchctl` 环境变量：
- 查看：`launchctl getenv OPENCLAW_GATEWAY_TOKEN`
- 清除：`launchctl unsetenv OPENCLAW_GATEWAY_TOKEN`
