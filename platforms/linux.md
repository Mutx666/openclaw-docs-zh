# Linux 平台指南

OpenClaw 完美支持 Linux 系统。推荐使用 **Node.js 22+** 作为运行时。

## 快速上手 (针对 VPS)
1. **安装环境**：确保已安装 Node.js。
2. **全局安装**：`npm i -g openclaw@latest`。
3. **配置向导**：`openclaw onboard --install-daemon` (安装守护进程)。
4. **远程访问**：在你的个人电脑上建立 SSH 隧道：`ssh -N -L 18789:127.0.0.1:18789 用户名@服务器IP`。
5. **打开后台**：在浏览器访问 `http://127.0.0.1:18789/`。

## 服务管理 (Systemd)
OpenClaw 默认会安装一个 Systemd 用户级服务。
- **启动/开启自启**：`systemctl --user enable --now openclaw-gateway.service`
- **查看日志**：`journalctl --user -u openclaw-gateway.service -f`
- **重启**：`openclaw gateway restart`

## 运行时建议
**不要使用 Bun** 运行网关（可能会导致 WhatsApp/Telegram 插件出现非预期 Bug），请务必使用 Node.js。
