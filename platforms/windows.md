# Windows (WSL2) 平台指南

强烈建议在 Windows 上通过 **WSL2** (推荐使用 Ubuntu) 运行 OpenClaw。这能确保运行时环境与 Linux 保持一致，极大提高工具和技能的兼容性。

## 为什么选择 WSL2？
- **环境一致性**：避免了 Windows 原生路径名或权限导致的怪异 Bug。
- **命令行友好**：完美支持 pnpm, Node.js 以及各种 Linux 命令行工具。
- **一键安装**：只需在 PowerShell 运行 `wsl --install`。

## 安装步骤
### 1. 开启 Systemd (关键)
为了支持网关服务自动运行，你必须在 WSL 中启用 systemd。在 Ubuntu 终端运行：
\`\`\`bash
sudo tee /etc/wsl.conf >/dev/null <<'EOF'
[boot]
systemd=true
